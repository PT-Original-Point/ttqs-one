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

test('P0: reserved TEST audit alias injects exactly one failure per real rawRef', () => {
  const store = new Map();
  const props = {
    getProperty(key) { return store.has(key) ? store.get(key) : null; },
    setProperty(key, value) { store.set(key, String(value)); },
    deleteProperty(key) { store.delete(key); }
  };
  const sandbox = load('DemoFault.gs', base({
    ttqsAssertTestOnly_() {},
    PropertiesService: { getScriptProperties() { return props; } },
    ttqsDigest_(value) { return crypto.createHash('sha256').update(String(value)).digest('hex'); }
  }));
  const raw = { kind: 'REGISTRATION', eventId: 'EVT-P0-1', rawRef: 'FORM_SUITE:F1:EVT-P0-1' };
  assert.equal(sandbox.ttqsShouldInjectRegistrationFailure_(raw, 'S-L01'), false);
  assert.equal(sandbox.ttqsShouldInjectRegistrationFailure_(raw, 'S-P0AUDIT-A1B2'), true);
  assert.equal(sandbox.ttqsShouldInjectRegistrationFailure_(raw, 'S-P0AUDIT-A1B2'), false);
  const other = { kind: 'REGISTRATION', eventId: 'EVT-P0-2', rawRef: 'FORM_SUITE:F1:EVT-P0-2' };
  assert.equal(sandbox.ttqsShouldInjectRegistrationFailure_(other, 'S-P0AUDIT-A1B2'), true);
});

test('P0: reserved fault alias is rejected outside registration and never affects normal alias', () => {
  const store = new Map();
  const props = {
    getProperty(key) { return store.has(key) ? store.get(key) : null; },
    setProperty(key, value) { store.set(key, String(value)); },
    deleteProperty(key) { store.delete(key); }
  };
  const sandbox = load('DemoFault.gs', base({
    ttqsAssertTestOnly_() {},
    PropertiesService: { getScriptProperties() { return props; } },
    ttqsDigest_(value) { return crypto.createHash('sha256').update(String(value)).digest('hex'); }
  }));
  assert.equal(sandbox.ttqsP0AuditAlias_('S-L01'), '');
  assert.equal(sandbox.ttqsP0AuditAlias_('S-P0AUDIT-A1B2'), 'S-P0AUDIT-A1B2');
  assert.throws(() => sandbox.ttqsShouldInjectRegistrationFailure_({ kind: 'NEEDS', eventId: 'E1', rawRef: 'R1' }, 'S-P0AUDIT-A1B2'), /P0_AUDIT_REGISTRATION_ONLY/);
});

test('P0: successful form processing immediately reconciles the same raw event', () => {
  let failCalls = 0;
  let reconcileCalls = 0;
  const job = { rowNumber: 3, object: { job_id: 'JOB-1', trace_id: 'TRACE-1', status: 'QUEUED', attempt_no: 0, max_attempts: 3 } };
  const sandbox = load('FormRouter.gs', base({
    ttqsAssertTestOnly_() {},
    ttqsConfig_() { return { MAX_ATTEMPTS: 3 }; },
    ttqsLedgerEnsure_() { return job; },
    ttqsLedgerStart_(j) { j.object.status = 'RUNNING'; j.object.attempt_no = 1; },
    ttqsLedgerSuccess_(j) { j.object.status = 'SUCCESS'; },
    ttqsLedgerFail_() { failCalls++; },
    ttqsProcessSubmission_() { return { aliasCode: 'S-L01', partyAliasId: 'P1', responseId: 'R1', evidenceId: 'E1' }; },
    ttqsReconcileRaw_(raw) { reconcileCalls++; assert.equal(raw.rawRef, 'FORM_SUITE:F1:EVT1'); return { status: 'MATCHED_EXACTLY_ONCE' }; },
    ttqsReconciliationMarkEngineFailure_() { throw new Error('SHOULD_NOT_MARK_FAILURE'); }
  }));
  const result = sandbox.ttqsHandleRawObjectUnlocked_({ kind: 'REGISTRATION', formId: 'F1', sheetId: 7, rowNumber: 2, eventId: 'EVT1', rawRef: 'FORM_SUITE:F1:EVT1', rawFingerprint: 'FP', named: {} }, false);
  assert.equal(job.object.status, 'SUCCESS');
  assert.equal(reconcileCalls, 1);
  assert.equal(failCalls, 0);
  assert.equal(result.reconciliationStatus, 'MATCHED_EXACTLY_ONCE');
});

test('P0: reconciliation engine failure never downgrades business SUCCESS into a retryable FAILED job', () => {
  let failCalls = 0;
  let engineFailureCalls = 0;
  const job = { rowNumber: 3, object: { job_id: 'JOB-2', trace_id: 'TRACE-2', status: 'QUEUED', attempt_no: 0, max_attempts: 3 } };
  const sandbox = load('FormRouter.gs', base({
    ttqsAssertTestOnly_() {},
    ttqsConfig_() { return { MAX_ATTEMPTS: 3 }; },
    ttqsLedgerEnsure_() { return job; },
    ttqsLedgerStart_(j) { j.object.status = 'RUNNING'; j.object.attempt_no = 1; },
    ttqsLedgerSuccess_(j) { j.object.status = 'SUCCESS'; },
    ttqsLedgerFail_() { failCalls++; },
    ttqsProcessSubmission_() { return { aliasCode: 'S-L01', partyAliasId: 'P1', responseId: 'R1', evidenceId: 'E1' }; },
    ttqsReconcileRaw_() { throw new Error('RECONCILE_ENGINE_BOOM'); },
    ttqsReconciliationMarkEngineFailure_(err) { engineFailureCalls++; assert.equal(err.message, 'RECONCILE_ENGINE_BOOM'); }
  }));
  const result = sandbox.ttqsHandleRawObjectUnlocked_({ kind: 'REGISTRATION', formId: 'F1', sheetId: 7, rowNumber: 2, eventId: 'EVT2', rawRef: 'FORM_SUITE:F1:EVT2', rawFingerprint: 'FP2', named: {} }, false);
  assert.equal(job.object.status, 'SUCCESS');
  assert.equal(failCalls, 0);
  assert.equal(engineFailureCalls, 1);
  assert.equal(result.reconciliationStatus, 'RECONCILIATION_EXCEPTION');
});
