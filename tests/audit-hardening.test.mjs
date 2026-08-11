import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function load(file, sandbox) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(`apps-script/${file}`, 'utf8'), sandbox, { filename: file });
  return sandbox;
}

function base(extra = {}) {
  return Object.assign({ Object, JSON, String, Number, Date, Error, isFinite }, extra);
}

test('audit: event identity is persisted with write-readback before ledger work', () => {
  let value = '';
  const cell = { getDisplayValue() { return value; }, setValue(v) { value = String(v); } };
  const sandbox = load('FormRouter.gs', base({
    SpreadsheetApp: { flush() {} },
    Utilities: { getUuid() { return 'UUID-1'; } },
    ttqsStableId_() { return 'EVT-IMMUTABLE-1'; }
  }));
  sandbox.ttqsEventIdColumn_ = () => 9;
  const sheet = { getRange(row, col) { assert.equal(row, 2); assert.equal(col, 9); return cell; } };
  assert.equal(sandbox.ttqsEnsureEventId_(sheet, 2), 'EVT-IMMUTABLE-1');
  assert.equal(value, 'EVT-IMMUTABLE-1');
});

test('audit: rawRef lookup follows immutable event identity after row movement', () => {
  const sandbox = load('FormRouter.gs', base({ ttqsOpenCore_() { return { getSheets() { return [sheet]; } }; } }));
  const sheet = { getSheetId() { return 77; }, getLastRow() { return 4; } };
  const refs = { 2: 'OTHER', 3: 'FORM_SUITE:FORM-1:EVT-1', 4: 'OTHER-2' };
  sandbox.ttqsRawSubmission_ = (sheetId, row) => ({ sheetId, rowNumber: row, rawRef: refs[row] });
  const result = sandbox.ttqsFindRawSubmissionByRef_(77, 'FORM_SUITE:FORM-1:EVT-1');
  assert.equal(result.rowNumber, 3);
});

test('audit: duplicate immutable event identity fails closed', () => {
  const sandbox = load('FormRouter.gs', base({ ttqsOpenCore_() { return { getSheets() { return [sheet]; } }; } }));
  const sheet = { getSheetId() { return 77; }, getLastRow() { return 3; } };
  sandbox.ttqsRawSubmission_ = (sheetId, row) => ({ sheetId, rowNumber: row, rawRef: 'FORM_SUITE:FORM-1:EVT-DUP' });
  assert.throws(() => sandbox.ttqsFindRawSubmissionByRef_(77, 'FORM_SUITE:FORM-1:EVT-DUP'), /RAW_RESPONSE_REF_AMBIGUOUS/);
});

test('audit: stale RUNNING lease expires but fresh RUNNING lease does not', () => {
  const sandbox = load('Ledger.gs', base({
    ttqsConfig_() { return { RUNNING_LEASE_MINUTES: 5 }; },
    ttqsParseJson_(v, f) { return v ? JSON.parse(v) : f; }
  }));
  const stale = { object: { status: 'RUNNING', notes: JSON.stringify({ leaseUntil: '2026-08-11T00:00:00Z' }) } };
  const fresh = { object: { status: 'RUNNING', notes: JSON.stringify({ leaseUntil: '2026-08-12T00:00:00Z' }) } };
  const now = Date.parse('2026-08-11T12:00:00Z');
  assert.equal(sandbox.ttqsLedgerRunningLeaseExpired_(stale, now), true);
  assert.equal(sandbox.ttqsLedgerRunningLeaseExpired_(fresh, now), false);
});

test('audit: retry eligibility includes due FAILED and stale RUNNING only', () => {
  const sandbox = load('Retry.gs', base({
    ttqsConfig_() { return { MAX_ATTEMPTS: 3 }; },
    ttqsLedgerRunningLeaseExpired_(job) { return job.object.notes === 'STALE'; }
  }));
  const now = Date.parse('2026-08-11T12:00:00Z');
  assert.equal(sandbox.ttqsRetryJobEligible_({ object: { status: 'FAILED', attempt_no: 1, max_attempts: 3, retry_at: '2026-08-11T11:00:00Z' } }, now), true);
  assert.equal(sandbox.ttqsRetryJobEligible_({ object: { status: 'RUNNING', attempt_no: 1, max_attempts: 3, notes: 'STALE' } }, now), true);
  assert.equal(sandbox.ttqsRetryJobEligible_({ object: { status: 'RUNNING', attempt_no: 1, max_attempts: 3, notes: 'FRESH' } }, now), false);
});

test('audit: reconciliation detects raw response with no event identity', () => {
  const sandbox = load('Reconcile.gs', base({ ttqsConfig_() { return {}; } }));
  const result = sandbox.ttqsReconcileRaw_({ kind: 'REGISTRATION', formId: 'F1', sheetId: 7, rowNumber: 2, eventId: '', rawRef: '', rawFingerprint: 'FP', named: { TTQS_ALIAS_CODE: 'S-L06' } });
  assert.equal(result.status, 'MISMATCH_EVENT_ID_MISSING');
});

test('audit: reconciliation detects event identity with no JobLedger as missed trigger', () => {
  const sandbox = load('Reconcile.gs', base({
    ttqsConfig_() { return {}; },
    ttqsFindRowsByValue_() { return []; },
    ttqsLedgerSheet_() { return 'ledger'; }
  }));
  const result = sandbox.ttqsReconcileRaw_({ kind: 'REGISTRATION', formId: 'F1', sheetId: 7, rowNumber: 2, eventId: 'EVT1', rawRef: 'FORM_SUITE:F1:EVT1', rawFingerprint: 'FP', named: { TTQS_ALIAS_CODE: 'S-L06' } });
  assert.equal(result.status, 'MISMATCH_TRIGGER_MISSED');
});

test('audit: reconciliation requires exact cross-layer linkage', () => {
  let patched;
  const raw = { kind: 'REGISTRATION', formId: 'F1', sheetId: 7, rowNumber: 2, eventId: 'EVT1', rawRef: 'FORM_SUITE:F1:EVT1', rawFingerprint: 'FP', named: { TTQS_ALIAS_CODE: 'S-L06' } };
  const jobNotes = { rawRef: raw.rawRef, eventId: raw.eventId, rawFingerprint: raw.rawFingerprint, formId: raw.formId, aliasCode: 'S-L06', evidenceId: 'E1' };
  const survey = { response_id: 'R1', class_run_id: 'CLASS', party_alias_id: 'P1', survey_type: 'REGISTRATION', source_ref: raw.rawRef, notes: JSON.stringify({ job_id: 'J1', provider_form_id: 'F1', provider_raw_fingerprint: 'FP' }) };
  const evidence = { environment: 'TEST', data_class: 'SAMPLE', class_run_id: 'CLASS', source_object_type: 'SurveyResponse', source_object_id: 'R1', notes: JSON.stringify({ formal_admissibility: 'NOT_FORMAL', source_ref: raw.rawRef, job_id: 'J1', provider_form_id: 'F1', provider_raw_fingerprint: 'FP' }) };
  const sandbox = load('Reconcile.gs', base({
    ttqsConfig_() { return { CLASS_RUN_ID: 'CLASS' }; },
    ttqsLedgerSheet_() { return 'ledger'; }, ttqsSurveySheet_() { return 'survey'; }, ttqsPartySheet_() { return 'party'; }, ttqsEvidenceSheet_() { return 'evidence'; },
    ttqsFindRowsByValue_(sheet) {
      if (sheet === 'ledger') return [{ rowNumber: 9, object: { job_id: 'J1', status: 'SUCCESS', environment: 'TEST', object_type: 'REGISTRATION', object_id: raw.rawRef, notes: JSON.stringify(jobNotes) } }];
      if (sheet === 'survey') return [{ object: survey }];
      if (sheet === 'party') return [{ object: { party_alias_id: 'P1', alias_code: 'S-L06' } }];
      if (sheet === 'evidence') return [{ object: evidence }];
      return [];
    },
    ttqsParseJson_(v, f) { return v ? JSON.parse(v) : f; },
    ttqsUpdateObjectRow_(sheet, row, patch) { patched = patch; },
    ttqsDateOnly_() { return '2026-08-11'; }
  }));
  const result = sandbox.ttqsReconcileRaw_(raw);
  assert.equal(result.status, 'MATCHED_EXACTLY_ONCE');
  assert.equal(patched.reconciliation_status, 'MATCHED_EXACTLY_ONCE');
});

test('audit: authorization health fails when FULL authorization is still required', () => {
  const sandbox = load('Health.gs', base({
    ScriptApp: {
      AuthMode: { FULL: 'FULL' },
      AuthorizationStatus: { NOT_REQUIRED: 'NOT_REQUIRED', REQUIRED: 'REQUIRED' },
      getAuthorizationInfo() { return { getAuthorizationStatus() { return 'REQUIRED'; } }; }
    }
  }));
  const result = sandbox.ttqsAuthorizationHealth_();
  assert.equal(result.pass, false);
  assert.equal(result.actual, 'REQUIRED');
});

test('audit: trigger contract rejects spreadsheet trigger bound to wrong sourceId', () => {
  const trigger = {
    getHandlerFunction() { return 'ttqsOnSpreadsheetFormSubmit'; },
    getEventType() { return 'ON_FORM_SUBMIT'; },
    getTriggerSource() { return 'SPREADSHEETS'; },
    getTriggerSourceId() { return 'WRONG'; }
  };
  const sandbox = load('Bootstrap.gs', base({
    ttqsConfig_() { return { CORE_SPREADSHEET_ID: 'CORE' }; },
    ScriptApp: {
      EventType: { ON_FORM_SUBMIT: 'ON_FORM_SUBMIT', CLOCK: 'CLOCK' },
      TriggerSource: { SPREADSHEETS: 'SPREADSHEETS', CLOCK: 'CLOCK' },
      getProjectTriggers() { return [trigger]; }
    }
  }));
  assert.throws(() => sandbox.ttqsAssertManagedTriggerContract_(), /MANAGED_TRIGGER_SOURCE_ID_INVALID/);
});
