import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function load(sandbox, withRouter = false) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync('apps-script/DemoFault.gs', 'utf8'), sandbox, { filename: 'DemoFault.gs' });
  if (withRouter) vm.runInContext(fs.readFileSync('apps-script/FormRouter.gs', 'utf8'), sandbox, { filename: 'FormRouter.gs' });
  return sandbox;
}

function base(extra = {}) {
  return Object.assign({ Object, JSON, String, Number, Date, Error, isFinite }, extra);
}

function propertyStore(seed = {}) {
  const store = new Map(Object.entries(seed).map(([k, v]) => [k, String(v)]));
  return {
    store,
    service: {
      getProperty(key) { return store.has(key) ? store.get(key) : null; },
      setProperty(key, value) { store.set(key, String(value)); },
      deleteProperty(key) { store.delete(key); }
    }
  };
}

function parseJson(value, fallback) {
  try { return JSON.parse(String(value || '')); } catch { return fallback; }
}

function formEvent(sheetId = 1407831401, rowNumber = 6) {
  return {
    range: {
      getSheet() { return { getSheetId() { return sheetId; } }; },
      getRow() { return rowNumber; }
    }
  };
}

function activeSuppression(now = Date.now(), nonce = 'NONCE-1') {
  return JSON.stringify({
    version: 'S3_MISSED_TRIGGER_SUPPRESSION_V1',
    nonce,
    alias: 'S-P0AUDIT-RUNTIME',
    kind: 'REGISTRATION',
    armedAtMs: now,
    expiresAtMs: now + 10 * 60 * 1000
  });
}

test('P0 provider alias is a valid reserved audit alias and is appended after normal SAMPLE aliases', () => {
  const props = propertyStore();
  const sandbox = load(base({
    ttqsSampleAliasChoices_() { return ['S-L01', 'S-L02']; },
    ttqsAssertTestOnly_() {},
    PropertiesService: { getScriptProperties() { return props.service; } }
  }));
  const alias = sandbox.ttqsP0AuditProviderAlias_();
  assert.equal(alias, 'S-P0AUDIT-RUNTIME');
  assert.equal(sandbox.ttqsP0AuditAlias_(alias), alias);
  assert.deepEqual(Array.from(sandbox.ttqsP0AuditRegistrationChoices_()), ['S-L01', 'S-L02', 'S-P0AUDIT-RUNTIME']);
});

test('P0 provider contract repairs the existing REGISTRATION form choice list and verifies readback', () => {
  const props = propertyStore({ TTQS_FORM_REGISTRATION_ID: 'FORM-REG' });
  const state = { choices: ['S-L01', 'S-L02'], help: '', required: false };
  const choiceItem = {
    getTitle() { return '示範學員代碼'; },
    getType() { return 'MULTIPLE_CHOICE_ENUM'; },
    asMultipleChoiceItem() { return choiceItem; },
    getChoices() { return state.choices.map((value) => ({ getValue() { return value; } })); },
    setChoiceValues(values) { state.choices = Array.from(values); return choiceItem; },
    setHelpText(value) { state.help = String(value); return choiceItem; },
    setRequired(value) { state.required = !!value; return choiceItem; }
  };
  const form = { getItems() { return [choiceItem]; } };
  const sandbox = load(base({
    ttqsSampleAliasChoices_() { return ['S-L01', 'S-L02']; },
    ttqsCanonicalFieldCode_(title) { return title === '示範學員代碼' ? 'TTQS_ALIAS_CODE' : title; },
    ttqsAssertTestOnly_() {},
    PropertiesService: { getScriptProperties() { return props.service; } },
    FormApp: {
      ItemType: { MULTIPLE_CHOICE: 'MULTIPLE_CHOICE_ENUM' },
      openById(id) { assert.equal(id, 'FORM-REG'); return form; }
    }
  }));

  const result = sandbox.ttqsEnsureP0AuditRegistrationProviderContract_();
  assert.equal(result.status, 'PASS');
  assert.equal(result.changed, true);
  assert.deepEqual(state.choices, ['S-L01', 'S-L02', 'S-P0AUDIT-RUNTIME']);
  assert.equal(state.required, true);
  assert.match(state.help, /工程稽核/);
  assert.equal(props.store.get('TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS'), 'PASS');
  assert.equal(props.store.has('TTQS_P0_AUDIT_PROVIDER_CONTRACT_ERROR'), false);
});

test('P0 provider maintenance skips a fresh verified contract and records failures fail-closed', () => {
  const now = Date.now();
  const props = propertyStore({
    TTQS_P0_AUDIT_PROVIDER_CONTRACT_VERSION: 'P0_AUDIT_REGISTRATION_ALIAS_V1:S-P0AUDIT-RUNTIME',
    TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS: 'PASS',
    TTQS_P0_AUDIT_PROVIDER_LAST_CHECK_MS: String(now)
  });
  let openCalls = 0;
  const sandbox = load(base({
    ttqsSampleAliasChoices_() { return ['S-L01']; },
    ttqsAssertTestOnly_() {},
    PropertiesService: { getScriptProperties() { return props.service; } },
    FormApp: { ItemType: { MULTIPLE_CHOICE: 'MULTIPLE_CHOICE_ENUM' }, openById() { openCalls++; throw new Error('SHOULD_NOT_OPEN'); } }
  }));

  const fresh = sandbox.ttqsMaintainP0AuditRegistrationProviderContract_();
  assert.equal(fresh.status, 'PASS');
  assert.equal(fresh.skippedFreshCheck, true);
  assert.equal(openCalls, 0);

  props.store.set('TTQS_P0_AUDIT_PROVIDER_LAST_CHECK_MS', '0');
  props.store.delete('TTQS_FORM_REGISTRATION_ID');
  const failed = sandbox.ttqsMaintainP0AuditRegistrationProviderContract_();
  assert.equal(failed.status, 'FAIL');
  assert.match(failed.error, /P0_AUDIT_REGISTRATION_FORM_ID_MISSING/);
  assert.equal(props.store.get('TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS'), 'FAIL');
  assert.match(props.store.get('TTQS_P0_AUDIT_PROVIDER_CONTRACT_ERROR'), /P0_AUDIT_REGISTRATION_FORM_ID_MISSING/);
});

test('S3 missed-trigger arm is TEST-only, exact-alias, one-shot and bounded to ten minutes', () => {
  const props = propertyStore({ TTQS_FORM_REGISTRATION_ID: 'FORM-REG' });
  const sandbox = load(base({
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    ttqsWithScriptLock_(fn) { return fn(); },
    PropertiesService: { getScriptProperties() { return props.service; } },
    Utilities: { getUuid() { return 'UUID-ARM-1'; } }
  }));

  const result = sandbox.ttqsArmS3MissedTriggerRecoveryTest();
  assert.equal(result.armed, true);
  assert.equal(result.alias, 'S-P0AUDIT-RUNTIME');
  assert.equal(result.kind, 'REGISTRATION');
  assert.equal(result.form_id, 'FORM-REG');
  const state = JSON.parse(props.store.get('TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE'));
  assert.equal(state.version, 'S3_MISSED_TRIGGER_SUPPRESSION_V1');
  assert.equal(state.nonce, 'UUID-ARM-1');
  assert.equal(state.expiresAtMs - state.armedAtMs, 10 * 60 * 1000);
  assert.throws(() => sandbox.ttqsArmS3MissedTriggerRecoveryTest(), /S3_MISSED_TRIGGER_SUPPRESSION_ALREADY_ARMED/);
});

test('S3 missed-trigger suppression is inert outside TEST and does not read provider raw', () => {
  const props = propertyStore({ TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: activeSuppression() });
  let rawReads = 0;
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'REAL' }; },
    ttqsAssertTestOnly_() { throw new Error('MUST_NOT_CALL'); },
    ttqsParseJson_: parseJson,
    PropertiesService: { getScriptProperties() { return props.service; } },
    ttqsRawSubmission_() { rawReads += 1; throw new Error('MUST_NOT_READ'); }
  }));
  const result = sandbox.ttqsMaybeSuppressS3MissedTriggerFormSubmit_(formEvent());
  assert.equal(result.suppressed, false);
  assert.equal(result.reason, 'NOT_TEST');
  assert.equal(rawReads, 0);
});

test('S3 missed-trigger exact target suppresses once without creating provider event ID and records bounded readback marker', () => {
  const now = Date.now();
  const props = propertyStore({ TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: activeSuppression(now, 'NONCE-EXACT') });
  const ensureFlags = [];
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'TEST' }; },
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    ttqsWithScriptLock_(fn) { return fn(); },
    PropertiesService: { getScriptProperties() { return props.service; } },
    ttqsRawSubmission_(sheetId, rowNumber, ensureEventId) {
      ensureFlags.push(ensureEventId);
      return {
        kind: 'REGISTRATION', formId: 'FORM-REG', sheetId, rowNumber,
        eventId: '', rawRef: '', rawFingerprint: 'FP-EXACT',
        named: { TTQS_ALIAS_CODE: 'S-P0AUDIT-RUNTIME' }
      };
    }
  }));

  const first = sandbox.ttqsMaybeSuppressS3MissedTriggerFormSubmit_(formEvent(1407831401, 6));
  assert.equal(first.suppressed, true);
  assert.equal(first.reason, 'P0_AUDIT_MISSED_TRIGGER_TEST');
  assert.equal(first.source_locator, 'SHEET:1407831401:ROW:6');
  assert.deepEqual(ensureFlags, [false]);
  assert.equal(props.store.has('TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE'), false);
  const consumed = JSON.parse(props.store.get('TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED'));
  assert.equal(consumed.nonce, 'NONCE-EXACT');
  assert.equal(consumed.raw_fingerprint, 'FP-EXACT');
  assert.equal(consumed.source_locator, 'SHEET:1407831401:ROW:6');

  const second = sandbox.ttqsMaybeSuppressS3MissedTriggerFormSubmit_(formEvent(1407831401, 6));
  assert.equal(second.suppressed, false);
  assert.equal(second.reason, 'NOT_ARMED');
  assert.deepEqual(ensureFlags, [false], 'second call must not even re-read provider raw after one-shot consumption');
});

test('S3 missed-trigger non-target alias preserves normal handler path and leaves arm intact', () => {
  const props = propertyStore({ TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: activeSuppression(Date.now(), 'NONCE-NONTARGET') });
  let normalCalls = 0;
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'TEST' }; },
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    ttqsWithScriptLock_(fn) { return fn(); },
    PropertiesService: { getScriptProperties() { return props.service; } }
  }), true);
  sandbox.ttqsRawSubmission_ = (sheetId, rowNumber, ensureEventId) => {
    assert.equal(ensureEventId, false);
    return {
      kind: 'REGISTRATION', formId: 'FORM-REG', sheetId, rowNumber,
      eventId: '', rawRef: '', rawFingerprint: 'FP-NONTARGET',
      named: { TTQS_ALIAS_CODE: 'S-L01' }
    };
  };
  sandbox.ttqsHandleRawSubmission_ = () => { normalCalls += 1; return { normal: true }; };

  const result = sandbox.ttqsOnSpreadsheetFormSubmit(formEvent());
  assert.equal(result.normal, true);
  assert.equal(normalCalls, 1);
  assert.equal(props.store.has('TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE'), true);
});

test('S3 missed-trigger expired arm self-clears and normal handler proceeds without raw pre-read', () => {
  const now = Date.now();
  const props = propertyStore({
    TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: JSON.stringify({
      version: 'S3_MISSED_TRIGGER_SUPPRESSION_V1', nonce: 'NONCE-OLD', alias: 'S-P0AUDIT-RUNTIME', kind: 'REGISTRATION',
      armedAtMs: now - 11 * 60 * 1000, expiresAtMs: now - 60 * 1000
    })
  });
  let rawReads = 0;
  let normalCalls = 0;
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'TEST' }; },
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    ttqsWithScriptLock_(fn) { return fn(); },
    PropertiesService: { getScriptProperties() { return props.service; } },
    ttqsRawSubmission_() { rawReads += 1; throw new Error('EXPIRED_MUST_NOT_PRE_READ'); }
  }), true);
  sandbox.ttqsHandleRawSubmission_ = () => { normalCalls += 1; return { normal: true }; };

  const result = sandbox.ttqsOnSpreadsheetFormSubmit(formEvent());
  assert.equal(result.normal, true);
  assert.equal(normalCalls, 1);
  assert.equal(rawReads, 0);
  assert.equal(props.store.has('TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE'), false);
});

test('S3 missed-trigger malformed armed state fails closed instead of silently processing', () => {
  const props = propertyStore({ TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: '{bad-json' });
  let normalCalls = 0;
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'TEST' }; },
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    PropertiesService: { getScriptProperties() { return props.service; } }
  }), true);
  sandbox.ttqsHandleRawSubmission_ = () => { normalCalls += 1; };
  assert.throws(() => sandbox.ttqsOnSpreadsheetFormSubmit(formEvent()), /S3_MISSED_TRIGGER_SUPPRESSION_STATE_INVALID/);
  assert.equal(normalCalls, 0);
});

test('FormRouter returns suppression result and does not enter normal business handler for exact armed target', () => {
  const props = propertyStore({ TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE: activeSuppression(Date.now(), 'NONCE-ROUTER') });
  let normalCalls = 0;
  const sandbox = load(base({
    ttqsConfig_() { return { ENVIRONMENT: 'TEST' }; },
    ttqsAssertTestOnly_() {},
    ttqsParseJson_: parseJson,
    ttqsWithScriptLock_(fn) { return fn(); },
    PropertiesService: { getScriptProperties() { return props.service; } }
  }), true);
  sandbox.ttqsRawSubmission_ = (sheetId, rowNumber, ensureEventId) => {
    assert.equal(ensureEventId, false, 'suppression path must never create TTQS_EVENT_ID');
    return {
      kind: 'REGISTRATION', formId: 'FORM-REG', sheetId, rowNumber,
      eventId: '', rawRef: '', rawFingerprint: 'FP-ROUTER',
      named: { TTQS_ALIAS_CODE: 'S-P0AUDIT-RUNTIME' }
    };
  };
  sandbox.ttqsHandleRawSubmission_ = () => { normalCalls += 1; throw new Error('NORMAL_HANDLER_MUST_NOT_RUN'); };

  const result = sandbox.ttqsOnSpreadsheetFormSubmit(formEvent(1407831401, 7));
  assert.equal(result.suppressed, true);
  assert.equal(normalCalls, 0);
  assert.equal(result.source_locator, 'SHEET:1407831401:ROW:7');
});
