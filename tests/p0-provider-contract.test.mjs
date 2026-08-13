import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function load(sandbox) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync('apps-script/DemoFault.gs', 'utf8'), sandbox, { filename: 'DemoFault.gs' });
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
