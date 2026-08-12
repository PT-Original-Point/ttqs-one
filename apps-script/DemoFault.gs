function ttqsP0AuditAlias_(aliasCode) {
  var value = String(aliasCode || '').trim().toUpperCase();
  return /^S-P0AUDIT-[A-Z0-9]{4,12}$/.test(value) ? value : '';
}

function ttqsP0AuditProviderAlias_() {
  return 'S-P0AUDIT-RUNTIME';
}

function ttqsP0AuditRegistrationChoices_() {
  var choices = ttqsSampleAliasChoices_().slice();
  var auditAlias = ttqsP0AuditProviderAlias_();
  if (choices.indexOf(auditAlias) === -1) choices.push(auditAlias);
  return choices;
}

function ttqsP0AuditProviderContractVersion_() {
  return 'P0_AUDIT_REGISTRATION_ALIAS_V1:' + ttqsP0AuditProviderAlias_();
}

function ttqsP0AuditProviderContractCheckIntervalMs_() {
  return 5 * 60 * 1000;
}

function ttqsEnsureP0AuditRegistrationProviderContract_() {
  ttqsAssertTestOnly_();
  var props = PropertiesService.getScriptProperties();
  var formId = String(props.getProperty('TTQS_FORM_REGISTRATION_ID') || '');
  if (!formId) throw new Error('P0_AUDIT_REGISTRATION_FORM_ID_MISSING');

  var form = FormApp.openById(formId);
  var aliasItems = form.getItems().filter(function(item) {
    return ttqsCanonicalFieldCode_(item.getTitle()) === 'TTQS_ALIAS_CODE';
  });
  if (aliasItems.length !== 1) throw new Error('P0_AUDIT_ALIAS_ITEM_COUNT_INVALID:' + aliasItems.length);

  var item = aliasItems[0];
  if (item.getType() !== FormApp.ItemType.MULTIPLE_CHOICE) throw new Error('P0_AUDIT_ALIAS_ITEM_TYPE_INVALID');
  var choiceItem = item.asMultipleChoiceItem();
  var desired = ttqsP0AuditRegistrationChoices_();
  var before = choiceItem.getChoices().map(function(choice) { return String(choice.getValue()); });
  var changed = JSON.stringify(before) !== JSON.stringify(desired);

  if (changed) choiceItem.setChoiceValues(desired);
  choiceItem
    .setHelpText('一般示範請選 S-Lxx；S-P0AUDIT-RUNTIME 僅供 TEST 工程稽核，請勿作一般展示使用。')
    .setRequired(true);

  var after = choiceItem.getChoices().map(function(choice) { return String(choice.getValue()); });
  if (JSON.stringify(after) !== JSON.stringify(desired)) throw new Error('P0_AUDIT_PROVIDER_ALIAS_READBACK_MISMATCH');

  var contractVersion = ttqsP0AuditProviderContractVersion_();
  var checkedAtMs = String(new Date().getTime());
  props.setProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_VERSION', contractVersion);
  props.setProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS', 'PASS');
  props.setProperty('TTQS_P0_AUDIT_PROVIDER_LAST_CHECK_MS', checkedAtMs);
  props.deleteProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_ERROR');

  if (props.getProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_VERSION') !== contractVersion) {
    throw new Error('P0_AUDIT_PROVIDER_CONTRACT_MARKER_READBACK_MISMATCH');
  }
  return {
    status: 'PASS',
    changed: changed,
    formId: formId,
    alias: ttqsP0AuditProviderAlias_(),
    choices: after,
    contractVersion: contractVersion,
    checkedAtMs: checkedAtMs
  };
}

function ttqsMaintainP0AuditRegistrationProviderContract_() {
  ttqsAssertTestOnly_();
  var props = PropertiesService.getScriptProperties();
  var expectedVersion = ttqsP0AuditProviderContractVersion_();
  var lastVersion = String(props.getProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_VERSION') || '');
  var lastStatus = String(props.getProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS') || '');
  var lastCheckMs = Number(props.getProperty('TTQS_P0_AUDIT_PROVIDER_LAST_CHECK_MS') || 0);
  var nowMs = new Date().getTime();
  var stillFresh = lastCheckMs > 0 && nowMs - lastCheckMs < ttqsP0AuditProviderContractCheckIntervalMs_();
  if (lastVersion === expectedVersion && lastStatus === 'PASS' && stillFresh) {
    return { status: 'PASS', skippedFreshCheck: true, alias: ttqsP0AuditProviderAlias_(), contractVersion: expectedVersion };
  }

  try {
    return ttqsEnsureP0AuditRegistrationProviderContract_();
  } catch (err) {
    var message = String(err && err.message ? err.message : err).slice(0, 500);
    props.setProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_STATUS', 'FAIL');
    props.setProperty('TTQS_P0_AUDIT_PROVIDER_LAST_CHECK_MS', String(nowMs));
    props.setProperty('TTQS_P0_AUDIT_PROVIDER_CONTRACT_ERROR', message);
    return { status: 'FAIL', alias: ttqsP0AuditProviderAlias_(), contractVersion: expectedVersion, error: message };
  }
}

function ttqsP0FaultConsumedKey_(rawRef) {
  if (!rawRef) throw new Error('P0_AUDIT_RAW_REF_REQUIRED');
  return 'TTQS_P0_FAULT_CONSUMED_' + ttqsDigest_(String(rawRef)).slice(0, 24).toUpperCase();
}

function ttqsShouldInjectRegistrationFailure_(raw, aliasCode) {
  ttqsAssertTestOnly_();
  var props = PropertiesService.getScriptProperties();

  if (props.getProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY') === 'TRUE') {
    props.deleteProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY');
    return true;
  }

  var auditAlias = ttqsP0AuditAlias_(aliasCode);
  if (!auditAlias) return false;
  if (!raw || String(raw.kind || '') !== 'REGISTRATION') throw new Error('P0_AUDIT_REGISTRATION_ONLY');
  if (!raw.eventId || !raw.rawRef) throw new Error('P0_AUDIT_EVENT_ID_REQUIRED');

  var key = ttqsP0FaultConsumedKey_(raw.rawRef);
  if (props.getProperty(key) === 'TRUE') return false;
  props.setProperty(key, 'TRUE');
  if (props.getProperty(key) !== 'TRUE') throw new Error('P0_AUDIT_FAULT_MARKER_WRITE_FAILED');
  return true;
}

function ttqsInjectNextRegistrationFailure() {
  ttqsAssertTestOnly_();
  PropertiesService.getScriptProperties().setProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY', 'TRUE');
  return { armed: true, target: 'next REGISTRATION after PartyAlias write' };
}

function ttqsCreateFaultProbe() {
  ttqsAssertTestOnly_();
  var key = 'TEST:FAULT_PROBE:' + new Date().getTime();
  var job = ttqsLedgerEnsure_({
    eventType: 'FAULT_PROBE',
    objectType: 'SystemFault',
    objectId: key,
    idempotencyKey: key,
    triggerSource: 'MANUAL_DEMO',
    notes: { faultProbe: true }
  });
  ttqsLedgerStart_(job, false);
  ttqsLedgerFail_(job, new Error('TTQS_CONTROLLED_FAULT_PROBE'));
  return { jobId: job.object.job_id, traceId: job.object.trace_id, idempotencyKey: key, status: 'FAILED', next: 'ttqsRetryFailedJobs' };
}
