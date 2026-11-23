import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import vm from 'node:vm';

function loadLedger(extra = {}) {
  const sandbox = Object.assign({ Object, JSON, String, Number, Date, Error, isFinite, console }, extra);
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync('apps-script/Ledger.gs', 'utf8'), sandbox, { filename: 'Ledger.gs' });
  return sandbox;
}

test('P0: AttemptHistory integrity hashes display values instead of provider-typed booleans', () => {
  const sandbox = loadLedger({
    ttqsDigest_(value) {
      return crypto.createHash('sha256').update(String(value), 'utf8').digest('hex');
    },
    ttqsConfig_() { return { AUDIT_LOG_VERSION: 2 }; },
    ttqsAuditNotes_() { return {}; }
  });

  const headers = sandbox.ttqsAttemptHistoryColumns_().map((column) => column.header);
  const row = Object.fromEntries(headers.map((header) => [header, '']));
  Object.assign(row, {
    attempt_event_id: 'ATT-DISPLAY-HASH',
    job_id: 'JOB-DISPLAY-HASH',
    trace_id: 'TRACE-DISPLAY-HASH',
    event_type: 'FORM_SUITE',
    object_type: 'REGISTRATION',
    object_id: 'FORM_SUITE:F1:E1',
    idempotency_key: 'TEST:FORM_SUITE:F1:E1',
    source_ref: 'FORM_SUITE:F1:E1',
    raw_fingerprint: 'abc123',
    attempt_no: '0',
    event_phase: 'JOB_CREATED',
    trigger_source: 'GOOGLE_FORM',
    status: 'QUEUED',
    recovered: 'FALSE',
    recorded_at: '2026-08-13T07:47:41+0800',
    notes: '{"auditLogVersion":2}'
  });
  row.record_hash = sandbox.ttqsAttemptHistoryRecordHash_(row);

  const displayValues = headers.map((header) => row[header]);
  const rawValues = displayValues.map((value, index) => headers[index] === 'recovered' ? false : value);
  assert.notEqual(String(rawValues[headers.indexOf('recovered')]), row.recovered);

  const attemptSheet = {
    getLastRow() { return 3; },
    getRange() {
      return {
        getDisplayValues() { return [displayValues]; },
        getValues() { throw new Error('ATTEMPT_HISTORY_INTEGRITY_MUST_NOT_USE_RAW_VALUES'); }
      };
    }
  };

  sandbox.ttqsAttemptHistorySheet_ = () => attemptSheet;
  sandbox.ttqsHeaders_ = () => headers;
  sandbox.ttqsRowObject_ = (hs, values) => Object.fromEntries(hs.map((header, index) => [header, values[index]]));
  sandbox.ttqsLedgerSheet_ = () => ({});
  sandbox.ttqsReadObjects_ = () => [];

  const result = sandbox.ttqsAttemptHistoryIntegrity_();
  assert.equal(result.status, 'PASS');
  assert.equal(result.rows, 1);
  assert.deepEqual(Array.from(result.errors), []);
});
