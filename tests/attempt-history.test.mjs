import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import vm from 'node:vm';

function load(file, sandbox) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(`apps-script/${file}`, 'utf8'), sandbox, { filename: file });
  return sandbox;
}

function base(extra = {}) {
  return Object.assign({ Object, JSON, String, Number, Date, Error, isFinite, console }, extra);
}

test('P0: retry start preserves prior failure summary and appends a new retry-start event', () => {
  const events = [];
  const sandbox = load('Ledger.gs', base({
    ttqsConfig_() { return { AUDIT_LOG_VERSION: 2, MAX_ATTEMPTS: 3, RUNNING_LEASE_MINUTES: 5, TIME_ZONE: 'Asia/Taipei' }; },
    ttqsParseJson_(v, f) { try { return v ? JSON.parse(v) : f; } catch { return f; } },
    ttqsNow_() { return '2026-08-13T00:20:00+0800'; },
    Utilities: { formatDate() { return '2026-08-13T00:25:00+0800'; } }
  }));
  sandbox.ttqsLedgerPatch_ = function(job, patch) { Object.assign(job.object, patch); return job; };
  sandbox.ttqsAttemptHistoryAppend_ = function(job, phase, patch) { events.push({ phase, patch: Object.assign({}, patch) }); };
  const job = {
    rowNumber: 3,
    object: {
      environment: 'TEST', event_type: 'FORM_SUITE', status: 'FAILED', attempt_no: 1, max_attempts: 3,
      trigger_source: 'GOOGLE_FORM', error_class: 'Error', error_message: 'FIRST_FAILURE_MUST_SURVIVE',
      notes: JSON.stringify({ auditLogVersion: 2, initialTriggerSource: 'GOOGLE_FORM' })
    }
  };
  sandbox.ttqsLedgerStart_(job, true);
  assert.equal(job.object.status, 'RUNNING');
  assert.equal(job.object.attempt_no, 2);
  assert.equal(job.object.error_class, 'Error');
  assert.equal(job.object.error_message, 'FIRST_FAILURE_MUST_SURVIVE');
  assert.equal(events.length, 1);
  assert.equal(events[0].phase, 'RETRY_STARTED');
  assert.equal(events[0].patch.error_message, '');
});

test('P0: append-only record hash changes if a stored failure fact is tampered', () => {
  const sandbox = load('Ledger.gs', base({
    ttqsDigest_(value) { return crypto.createHash('sha256').update(String(value)).digest('hex'); }
  }));
  const row = {};
  sandbox.ttqsAttemptHistoryColumns_().forEach((column) => { row[column.header] = ''; });
  Object.assign(row, {
    attempt_event_id: 'ATT-1', job_id: 'JOB-1', attempt_no: '1', event_phase: 'ATTEMPT_FAILED',
    status: 'FAILED', error_class: 'Error', error_message: 'ORIGINAL_FAILURE', recorded_at: 'NOW', previous_event_hash: ''
  });
  row.record_hash = sandbox.ttqsAttemptHistoryRecordHash_(row);
  const original = row.record_hash;
  row.error_message = 'TAMPERED';
  assert.notEqual(sandbox.ttqsAttemptHistoryRecordHash_(row), original);
});

test('P0: generic row update is forbidden for AttemptHistory', () => {
  const sandbox = load('Schema.gs', base({
    ttqsConfig_() { return { SHEETS: { ATTEMPT_HISTORY: '16_AttemptHistory_嘗試歷史' } }; }
  }));
  const sheet = { getName() { return '16_AttemptHistory_嘗試歷史'; } };
  assert.throws(() => sandbox.ttqsUpdateObjectRow_(sheet, 3, { status: 'SUCCESS' }), /ATTEMPT_HISTORY_IMMUTABLE_UPDATE_FORBIDDEN/);
});

test('P0: reconciliation MATCH is the only path to FINAL_ACCEPTED', () => {
  const history = [];
  const sandbox = load('Reconcile.gs', base({
    ttqsNow_() { return 'NOW'; },
    ttqsDateOnly_() { return '2026-08-13'; },
    ttqsJobUsesAppendOnlyAudit_() { return true; },
    ttqsAuditNotes_() { return { recovered: true }; },
    ttqsAttemptHistoryAppend_(job, phase, patch) { history.push({ phase, patch }); }
  }));
  sandbox.ttqsLedgerPatch_ = function(job, patch) { Object.assign(job.object, patch); return job; };
  const matched = { rowNumber: 3, object: { status: 'SUCCESS', reconciliation_status: '', final_acceptance_status: 'RECONCILIATION_PENDING', final_accepted_at: '', notes: '{}' } };
  sandbox.ttqsApplyReconciliationResult_(matched, 'MATCHED_EXACTLY_ONCE', { linkageErrors: [] });
  assert.equal(matched.object.final_acceptance_status, 'FINAL_ACCEPTED');
  assert.equal(matched.object.final_accepted_at, 'NOW');
  assert.equal(history.at(-1).patch.reconciliation_status, 'MATCHED_EXACTLY_ONCE');

  const mismatch = { rowNumber: 4, object: { status: 'SUCCESS', reconciliation_status: '', final_acceptance_status: 'RECONCILIATION_PENDING', final_accepted_at: '', notes: '{}' } };
  sandbox.ttqsApplyReconciliationResult_(mismatch, 'MISMATCH_CROSS_LINK', { linkageErrors: ['SURVEY_COUNT:2'] });
  assert.equal(mismatch.object.final_acceptance_status, 'RECONCILIATION_EXCEPTION');
  assert.equal(mismatch.object.final_accepted_at, '');
});
