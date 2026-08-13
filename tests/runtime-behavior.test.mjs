import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function load(file, sandbox) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(`apps-script/${file}`, 'utf8'), sandbox, { filename: file });
  return sandbox;
}

function baseGlobals(extra = {}) {
  return Object.assign({ Object, JSON, String, Number, Date, Error, isFinite }, extra);
}

test('script lock releases after success', () => {
  const events = [];
  const sandbox = load('Util.gs', baseGlobals({
    ttqsConfig_() { return { LOCK_WAIT_MS: 30000, TIME_ZONE: 'Asia/Taipei' }; },
    LockService: { getScriptLock() { return { tryLock() { events.push('try'); return true; }, releaseLock() { events.push('release'); } }; } },
    Utilities: { formatDate() { return 'NOW'; }, computeDigest() { return Array(32).fill(1); }, DigestAlgorithm: { SHA_256: 1 }, Charset: { UTF_8: 1 } }
  }));
  assert.equal(sandbox.ttqsWithScriptLock_(() => 'OK'), 'OK');
  assert.deepEqual(events, ['try', 'release']);
});

test('script lock releases after exception', () => {
  const events = [];
  const sandbox = load('Util.gs', baseGlobals({
    ttqsConfig_() { return { LOCK_WAIT_MS: 30000, TIME_ZONE: 'Asia/Taipei' }; },
    LockService: { getScriptLock() { return { tryLock() { events.push('try'); return true; }, releaseLock() { events.push('release'); } }; } },
    Utilities: { formatDate() { return 'NOW'; }, computeDigest() { return Array(32).fill(1); }, DigestAlgorithm: { SHA_256: 1 }, Charset: { UTF_8: 1 } }
  }));
  assert.throws(() => sandbox.ttqsWithScriptLock_(() => { throw new Error('BOOM'); }), /BOOM/);
  assert.deepEqual(events, ['try', 'release']);
});

test('script lock timeout fails closed', () => {
  const sandbox = load('Util.gs', baseGlobals({
    ttqsConfig_() { return { LOCK_WAIT_MS: 30000, TIME_ZONE: 'Asia/Taipei' }; },
    LockService: { getScriptLock() { return { tryLock() { return false; }, releaseLock() {} }; } },
    Utilities: { formatDate() { return 'NOW'; }, computeDigest() { return Array(32).fill(1); }, DigestAlgorithm: { SHA_256: 1 }, Charset: { UTF_8: 1 } }
  }));
  assert.throws(() => sandbox.ttqsWithScriptLock_(() => 'NO'), /TTQS_SCRIPT_LOCK_TIMEOUT/);
});

test('retry start updates primary trigger_source and preserves initial source in notes', () => {
  let patch;
  const history = [];
  const sandbox = load('Ledger.gs', baseGlobals({
    ttqsUpdateObjectRow_() {},
    ttqsLedgerSheet_() { return {}; },
    ttqsNow_() { return 'NOW'; },
    ttqsParseJson_(v, f) { try { return v ? JSON.parse(v) : f; } catch { return f; } },
    ttqsConfig_() { return { AUDIT_LOG_VERSION: 2, MAX_ATTEMPTS: 3, RETRY_MINUTES: 1, RUNNING_LEASE_MINUTES: 5, TIME_ZONE: 'Asia/Taipei' }; },
    ttqsEnsureRuntimeRecoveryEvidence_() { return { evidenceId: 'EV-REC' }; },
    Utilities: { formatDate() { return 'LATER'; } },
    ttqsGetSheet_() {}, ttqsFindUniqueRowByValue_() {}, ttqsStableId_() {}, ttqsAppendObject_() {}, ttqsHeaders_() {}
  }));
  sandbox.ttqsLedgerPatch_ = function(job, p) { patch = p; Object.assign(job.object, p); return job; };
  sandbox.ttqsAttemptHistoryAppend_ = function(job, phase, p) { history.push({ phase, patch: p }); };
  const job = { rowNumber: 3, object: { job_id: 'JOB1', event_type: 'FORM_SUITE', trigger_source: 'GOOGLE_FORM', attempt_no: 1, notes: JSON.stringify({ auditLogVersion: 2 }), status: 'FAILED', error_class: 'Error', error_message: 'FIRST_FAILURE' } };
  sandbox.ttqsLedgerStart_(job, true);
  assert.equal(patch.trigger_source, 'TIME_RETRY');
  assert.equal(patch.attempt_no, 2);
  const notes = JSON.parse(patch.notes);
  assert.equal(notes.initialTriggerSource, 'GOOGLE_FORM');
  assert.equal(notes.retryTrigger, 'TIME_RETRY');
  assert.equal(notes.retry, true);
  assert.equal(job.object.error_message, 'FIRST_FAILURE');
  assert.equal(history[0].phase, 'RETRY_STARTED');
});

test('reconcile is locked and summarizes raw-root exact matches and mismatches', () => {
  let locked = 0;
  let status = 'MATCHED_EXACTLY_ONCE';
  const sheet = { getLastRow() { return 2; } };
  const sandbox = load('Reconcile.gs', baseGlobals({
    ttqsWithScriptLock_(fn) { locked++; return fn(); },
    ttqsAssertTestOnly_() {},
    ttqsOpenCore_() { return {}; },
    ttqsParseJson_(v) { return JSON.parse(v); },
    PropertiesService: { getScriptProperties() { return { getProperty() { return JSON.stringify({ 77: 'REGISTRATION' }); } }; } },
    ttqsFindSheetById_() { return sheet; },
    ttqsRawSubmission_() { return { kind: 'REGISTRATION', eventId: 'EVT1', rawRef: 'FORM_SUITE:F1:EVT1' }; }
  }));
  sandbox.ttqsReconcileRaw_ = () => ({ status });
  sandbox.ttqsReconciliationWatchdog_ = () => ({ status: 'PASS', issues: [], pendingWithinGrace: [] });
  let result = sandbox.ttqsReconcile();
  assert.equal(locked, 1);
  assert.equal(result.status, 'PASS');
  assert.equal(result.matched, 1);
  status = 'MISMATCH_TRIGGER_MISSED';
  result = sandbox.ttqsReconcile();
  assert.equal(result.status, 'FAIL');
  assert.equal(result.mismatched, 1);
});

test('survey replay still ensures EvidenceMaster registration without appending duplicate survey', () => {
  const appended = [];
  const sandbox = load('SurveyWriter.gs', baseGlobals({
    ttqsGetSheet_(name) { return name; },
    ttqsConfig_() { return { CLASS_RUN_ID: 'SAMPLE-CLASS-001', SHEETS: { PARTY_ALIAS: 'party', SURVEY: 'survey', EVIDENCE: 'evidence' } }; },
    ttqsFindUniqueRowByValue_(sheet, header) {
      if (sheet === 'survey' && header === 'source_ref') return { object: { response_id: 'RESP-1' } };
      return null;
    },
    ttqsAppendObject_(sheet, obj) { appended.push({ sheet, obj }); },
    ttqsStableId_(prefix) { return prefix + 'ID'; },
    ttqsNow_() { return 'NOW'; },
    ttqsDateOnly_() { return 'DATE'; },
    ttqsRedactFreeText_(v) { return v; },
    ttqsRequireSampleAlias_(v) { return v; }
  }));
  const result = sandbox.ttqsWriteSurvey_({ partyAliasId: 'P1', surveyType: 'NEEDS', questionSetVersion: 'v1', scoreTotal: 4, scoreMax: 5, freeText: 'SAMPLE', sourceRef: 'FORM_SUITE:F1:EVT1', providerFormId: 'F1', rawFingerprint: 'FP', jobId: 'J1' });
  assert.equal(result.duplicate, true);
  assert.equal(result.responseId, 'RESP-1');
  assert.equal(appended.filter((x) => x.sheet === 'survey').length, 0);
  assert.equal(appended.filter((x) => x.sheet === 'evidence').length, 1);
});

test('response sheet polling tolerates delayed sheet creation', () => {
  let calls = 0;
  let sleeps = 0;
  const before = { getSheetId() { return 1; }, getLastColumn() { return 0; }, getLastRow() { return 0; } };
  const created = {
    getSheetId() { return 2; }, getLastColumn() { return 3; }, getLastRow() { return 1; },
    getRange() { return { getDisplayValues() { return [['Timestamp', 'TTQS_ALIAS_CODE', 'TTQS_SAMPLE_CONFIRM']]; } }; }
  };
  const sandbox = load('Forms.gs', baseGlobals({
    ttqsConfig_() { return { FORM_RESPONSE_WAIT_MS: 10000, FORM_RESPONSE_POLL_MS: 1 }; },
    SpreadsheetApp: { flush() {} },
    Utilities: { sleep() { sleeps++; } },
    PropertiesService: {}, FormApp: {}
  }));
  const ss = { getSheets() { calls++; return calls === 1 ? [before] : [before, created]; } };
  const result = sandbox.ttqsResponseSheetAfterDestination_(ss, [1], 'REGISTRATION');
  assert.equal(result.getSheetId(), 2);
  assert.equal(sleeps, 1);
});

test('partial form state reuses same form id and recovers response sheet mapping', () => {
  const stored = { TTQS_FORM_REGISTRATION_ID: 'FORM-1' };
  let createCalls = 0;
  const itemState = [];
  function mockChoiceItem(title) {
    const state = { title, help: '', choices: [], required: false };
    itemState.push(state);
    const item = {
      getTitle() { return state.title; },
      getType() { return 'MULTIPLE_CHOICE_ENUM'; },
      asMultipleChoiceItem() { return item; },
      setTitle(v) { state.title = String(v); return item; },
      setHelpText(v) { state.help = String(v); return item; },
      setChoiceValues(v) { state.choices = Array.from(v); return item; },
      setRequired(v) { state.required = !!v; return item; }
    };
    return item;
  }
  const items = [mockChoiceItem('TTQS_ALIAS_CODE'), mockChoiceItem('TTQS_SAMPLE_CONFIRM')];
  const form = {
    getItems() { return items; }, getResponses() { return []; }, deleteItem() {},
    setTitle() {}, setDescription() {}, setConfirmationMessage() {}, setCollectEmail() {}, setLimitOneResponsePerUser() {}, setPublished() {}, isPublished() { return true; },
    getDestinationId() { return 'CORE'; }, getDestinationType() { return 'SPREADSHEET_ENUM'; },
    getId() { return 'FORM-1'; }, getEditUrl() { return 'EDIT'; }, getPublishedUrl() { return 'VIEW'; }
  };
  const sheet = {
    getSheetId() { return 77; }, getLastColumn() { return 3; }, getLastRow() { return 1; }, getName() { return 'Form Responses 1'; }, setName() {},
    getRange() { return { getDisplayValues() { return [['Timestamp', 'TTQS_ALIAS_CODE', 'TTQS_SAMPLE_CONFIRM']]; } }; }
  };
  const ss = { getSheets() { return [sheet]; }, getSheetByName() { return null; } };
  let permissionCreated = 0;
  const permissions = [{ id: 'P-ORG', type: 'domain', role: 'reader', view: 'published' }];
  const sandbox = load('Forms.gs', baseGlobals({
    ttqsAssertTestOnly_() {},
    ttqsOpenCore_() { return ss; },
    ttqsConfig_() { return { CORE_SPREADSHEET_ID: 'CORE', FORM_RESPONSE_WAIT_MS: 1000, FORM_RESPONSE_POLL_MS: 1 }; },
    SpreadsheetApp: { flush() {} }, Utilities: { sleep() {} },
    PropertiesService: { getScriptProperties() { return { getProperty(k) { return stored[k] || null; }, setProperty(k, v) { stored[k] = String(v); } }; } },
    FormApp: {
      DestinationType: { SPREADSHEET: 'SPREADSHEET_ENUM' },
      ItemType: { MULTIPLE_CHOICE: 'MULTIPLE_CHOICE_ENUM', SCALE: 'SCALE_ENUM' },
      openById() { return form; }, create() { createCalls++; return form; }
    },
    Drive: { Permissions: {
      list() { return { permissions }; },
      create(permission) { permissionCreated++; permissions.push(Object.assign({ id: 'P-ANY' }, permission)); return permission; }
    } }
  }));
  const result = sandbox.ttqsEnsureOneForm_('REGISTRATION', sandbox.ttqsFormDefinitions_().REGISTRATION);
  assert.equal(createCalls, 0);
  assert.equal(result.formId, 'FORM-1');
  assert.equal(result.responseSheetId, 77);
  assert.equal(result.published, true);
  assert.equal(result.recoveredPartialState, true);
  assert.equal(result.anyoneWithLinkResponder, true);
  assert.equal(permissionCreated, 1);
  assert.equal(stored.TTQS_FORM_REGISTRATION_SHEET_ID, '77');
  assert.equal(itemState[0].title, '示範學員代碼');
  assert.equal(itemState[1].title, '確認本次為示範填答');
  assert.equal(itemState[0].required, true);
  assert.equal(itemState[1].required, true);
});

test('bootstrap failure is ledgered after job starts', () => {
  const order = [];
  const job = { rowNumber: 3, object: { status: 'QUEUED', attempt_no: 0, max_attempts: 3, notes: '{}' } };
  const sandbox = load('Bootstrap.gs', baseGlobals({
    ttqsWithScriptLock_(fn) { order.push('lock'); return fn(); },
    ttqsAssertTestOnly_() {},
    ttqsHealthCheck() { return { status: 'PASS', failed: [] }; },
    ttqsConfig_() { return { VERSION: '0.6.4', MAX_ATTEMPTS: 3, AUTO_CONSULT_SHEET: 'AUTO' }; },
    ttqsLedgerEnsure_() { order.push('ensureJob'); return job; },
    ttqsLedgerStart_() { order.push('startJob'); job.object.attempt_no = 1; },
    ttqsLedgerStage_(j, stage) { order.push('stage:' + stage); },
    ttqsEnsureForms_() { order.push('ensureForms'); throw new Error('FORM_FAIL'); },
    ttqsLedgerFail_() { order.push('ledgerFail'); },
    ttqsLedgerSuccess_() { order.push('ledgerSuccess'); },
    ttqsInstallManagedTriggers_() {}, ttqsRefreshConsultViewUnlocked_() {}, ttqsAssertManagedTriggerContract_() {},
    ScriptApp: { AuthMode: { FULL: 'FULL' }, requireAllScopes() {}, getProjectTriggers() { return []; } }
  }));
  assert.throws(() => sandbox.ttqsBootstrapTest(), /FORM_FAIL/);
  assert.deepEqual(order.slice(0, 6), ['lock', 'ensureJob', 'startJob', 'stage:ENSURE_FORMS', 'ensureForms', 'ledgerFail']);
});

test('recovered FORM_SUITE success registers recovery evidence and stores evidence id in notes', () => {
  const patches = [];
  const history = [];
  const sandbox = load('Ledger.gs', baseGlobals({
    ttqsUpdateObjectRow_() {}, ttqsLedgerSheet_() { return {}; },
    ttqsNow_() { return 'NOW'; },
    ttqsParseJson_(v, f) { return v ? JSON.parse(v) : f; },
    ttqsEnsureRuntimeRecoveryEvidence_() { return { evidenceId: 'EV-REC-1' }; },
    ttqsConfig_() { return { AUDIT_LOG_VERSION: 2, MAX_ATTEMPTS: 3, RETRY_MINUTES: 1, RUNNING_LEASE_MINUTES: 5, TIME_ZONE: 'Asia/Taipei' }; },
    Utilities: { formatDate() { return 'LATER'; } },
    ttqsGetSheet_() {}, ttqsFindUniqueRowByValue_() {}, ttqsStableId_() {}, ttqsAppendObject_() {}, ttqsHeaders_() {}
  }));
  sandbox.ttqsLedgerPatch_ = function(job, p) { patches.push(p); Object.assign(job.object, p); return job; };
  sandbox.ttqsAttemptHistoryAppend_ = function(job, phase, p) { history.push({ phase, patch: p }); };
  const job = { rowNumber: 9, object: { event_type: 'FORM_SUITE', job_id: 'JOB1', attempt_no: 2, notes: JSON.stringify({ auditLogVersion: 2 }), status: 'RUNNING' } };
  sandbox.ttqsLedgerSuccess_(job, { recovered: true });
  assert.equal(job.object.status, 'SUCCESS');
  assert.equal(JSON.parse(job.object.notes).recoveryEvidenceId, 'EV-REC-1');
  assert.equal(patches.length, 2);
  assert.equal(history[0].phase, 'ATTEMPT_SUCCEEDED');
  assert.equal(history[0].patch.recovery_evidence_id, 'EV-REC-1');
});

test('health check fails when a required machine header is missing', () => {
  const sheets = {};
  const cfg = {
    AUDIT_LOG_VERSION: 2, ENVIRONMENT: 'TEST', ENABLE_REAL_WRITES: false, PII_VAULT_READY: false, TIME_ZONE: 'Asia/Taipei', CORE_SPREADSHEET_ID: 'CORE', CONSULT_VIEW_SPREADSHEET_ID: 'CONSULT', CLASS_RUN_ID: 'SAMPLE-CLASS-001',
    SHEETS: { INDICATORS: 'ind', CLASS_RUN: 'class', PARTY_ALIAS: 'party', SURVEY: 'survey', EVIDENCE: 'evidence', LEDGER: 'ledger', ATTEMPT_HISTORY: 'attempt' }
  };
  for (const name of Object.values(cfg.SHEETS)) sheets[name] = { getName() { return name; } };
  const ss = { getSpreadsheetTimeZone() { return 'Asia/Taipei'; }, getId() { return 'CORE'; }, getSheets() { return Object.values(sheets); }, getSheetByName(name) { return sheets[name]; } };
  const sandbox = load('Health.gs', baseGlobals({
    ttqsAssertTestOnly_() {}, ttqsConfig_() { return cfg; }, ttqsOpenCore_() { return ss; },
    ttqsAttemptHistoryColumns_() { return [{ header: 'attempt_event_id' }]; },
    ttqsMissingHeaders_(sheet) { return sheet === sheets.survey ? ['source_ref'] : []; },
    ttqsFindRowsByValue_() { return [{ object: { environment: 'TEST', data_class: 'SAMPLE', real_start_gate_status: 'NOT_APPLICABLE_SAMPLE' } }]; },
    SpreadsheetApp: { openById() { return { getId() { return 'CONSULT'; }, getSpreadsheetTimeZone() { return 'Asia/Taipei'; } }; } },
    PropertiesService: { getScriptProperties() { return { getProperty() { return null; } }; } },
    ScriptApp: { AuthMode: { FULL: 'FULL' }, AuthorizationStatus: { NOT_REQUIRED: 'NOT_REQUIRED' }, getAuthorizationInfo() { return { getAuthorizationStatus() { return 'NOT_REQUIRED'; } }; } },
    ttqsParseJson_() {}, ttqsFindSheetById_() {}, ttqsSheetMatchesFormKind_() {},
    ttqsAttemptHistoryIntegrity_() { return { status: 'PASS', rows: 0, auditedJobs: 0, errors: [] }; },
    ttqsReconciliationWatchdog_() { return { status: 'PASS', issues: [], pendingWithinGrace: [] }; }
  }));
  const result = sandbox.ttqsHealthCheck();
  assert.equal(result.status, 'FAIL');
  assert.ok(result.failed.some((x) => x.check === 'headers:survey' && x.actual === 'source_ref'));
});
