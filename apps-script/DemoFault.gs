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

var TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY = 'TTQS_S3_MISSED_TRIGGER_SUPPRESS_ONCE';
var TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED_PROPERTY = 'TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED';
var TTQS_S3_MISSED_TRIGGER_SUPPRESSION_VERSION = 'S3_MISSED_TRIGGER_SUPPRESSION_V1';

function ttqsS3MissedTriggerSuppressionTtlMs_() {
  return 10 * 60 * 1000;
}

function ttqsS3MissedTriggerSuppressionParse_(rawState) {
  var state = ttqsParseJson_(String(rawState || ''), null);
  var armedAtMs = Number(state && state.armedAtMs || 0);
  var expiresAtMs = Number(state && state.expiresAtMs || 0);
  var expectedAlias = ttqsP0AuditProviderAlias_();
  if (!state ||
      String(state.version || '') !== TTQS_S3_MISSED_TRIGGER_SUPPRESSION_VERSION ||
      String(state.alias || '') !== expectedAlias ||
      String(state.kind || '') !== 'REGISTRATION' ||
      !String(state.nonce || '') ||
      !isFinite(armedAtMs) || armedAtMs <= 0 ||
      !isFinite(expiresAtMs) || expiresAtMs <= armedAtMs ||
      expiresAtMs - armedAtMs > ttqsS3MissedTriggerSuppressionTtlMs_()) {
    throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_STATE_INVALID');
  }
  return {
    version: TTQS_S3_MISSED_TRIGGER_SUPPRESSION_VERSION,
    nonce: String(state.nonce),
    alias: expectedAlias,
    kind: 'REGISTRATION',
    armedAtMs: armedAtMs,
    expiresAtMs: expiresAtMs
  };
}

function ttqsArmS3MissedTriggerRecoveryTest() {
  ttqsAssertTestOnly_();
  var props = PropertiesService.getScriptProperties();
  var formId = String(props.getProperty('TTQS_FORM_REGISTRATION_ID') || '');
  if (!formId) throw new Error('S3_MISSED_TRIGGER_REGISTRATION_FORM_ID_MISSING');

  return ttqsWithScriptLock_(function() {
    var nowMs = new Date().getTime();
    var existingRaw = String(props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY) || '');
    if (existingRaw) {
      var existing = ttqsS3MissedTriggerSuppressionParse_(existingRaw);
      if (existing.expiresAtMs > nowMs) throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_ALREADY_ARMED');
      props.deleteProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY);
      if (props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY)) {
        throw new Error('S3_MISSED_TRIGGER_EXPIRED_ARM_CLEAR_FAILED');
      }
    }

    var state = {
      version: TTQS_S3_MISSED_TRIGGER_SUPPRESSION_VERSION,
      nonce: String(Utilities.getUuid()),
      alias: ttqsP0AuditProviderAlias_(),
      kind: 'REGISTRATION',
      armedAtMs: nowMs,
      expiresAtMs: nowMs + ttqsS3MissedTriggerSuppressionTtlMs_()
    };
    props.setProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY, JSON.stringify(state));
    props.deleteProperty(TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED_PROPERTY);

    var readback = ttqsS3MissedTriggerSuppressionParse_(props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY));
    if (readback.nonce !== state.nonce || readback.expiresAtMs !== state.expiresAtMs) {
      throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_ARM_READBACK_MISMATCH');
    }
    return {
      armed: true,
      version: state.version,
      nonce: state.nonce,
      alias: state.alias,
      kind: state.kind,
      form_id: formId,
      expires_at: new Date(state.expiresAtMs).toISOString()
    };
  });
}

function ttqsCancelS3MissedTriggerRecoveryTest() {
  ttqsAssertTestOnly_();
  var props = PropertiesService.getScriptProperties();
  return ttqsWithScriptLock_(function() {
    props.deleteProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY);
    if (props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY)) {
      throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_CANCEL_FAILED');
    }
    return { armed: false, alias: ttqsP0AuditProviderAlias_(), kind: 'REGISTRATION' };
  });
}

function ttqsMaybeSuppressS3MissedTriggerFormSubmit_(e) {
  var cfg = ttqsConfig_();
  if (!cfg || String(cfg.ENVIRONMENT || '') !== 'TEST') return { suppressed: false, reason: 'NOT_TEST' };
  ttqsAssertTestOnly_();
  if (!e || !e.range) throw new Error('REAL_SPREADSHEET_FORM_EVENT_REQUIRED');

  var props = PropertiesService.getScriptProperties();
  var initialRaw = String(props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY) || '');
  if (!initialRaw) return { suppressed: false, reason: 'NOT_ARMED' };
  var initialState = ttqsS3MissedTriggerSuppressionParse_(initialRaw);
  var nowMs = new Date().getTime();

  if (initialState.expiresAtMs <= nowMs) {
    return ttqsWithScriptLock_(function() {
      var currentRaw = String(props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY) || '');
      if (!currentRaw) return { suppressed: false, reason: 'NOT_ARMED' };
      var current = ttqsS3MissedTriggerSuppressionParse_(currentRaw);
      var lockedNowMs = new Date().getTime();
      if (current.expiresAtMs > lockedNowMs) return { suppressed: false, reason: 'ARM_REFRESHED' };
      props.deleteProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY);
      if (props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY)) {
        throw new Error('S3_MISSED_TRIGGER_EXPIRED_ARM_CLEAR_FAILED');
      }
      return { suppressed: false, reason: 'EXPIRED' };
    });
  }

  var sheetId = Number(e.range.getSheet().getSheetId());
  var rowNumber = Number(e.range.getRow());
  var raw = ttqsRawSubmission_(sheetId, rowNumber, false);
  var aliasCode = String(raw && raw.named && raw.named.TTQS_ALIAS_CODE || '').trim().toUpperCase();
  if (String(raw && raw.kind || '') !== 'REGISTRATION' || aliasCode !== initialState.alias) {
    return { suppressed: false, reason: 'NON_TARGET' };
  }

  return ttqsWithScriptLock_(function() {
    var currentRaw = String(props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY) || '');
    if (!currentRaw) return { suppressed: false, reason: 'ALREADY_CONSUMED' };
    var current = ttqsS3MissedTriggerSuppressionParse_(currentRaw);
    if (current.nonce !== initialState.nonce) throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_ARM_CHANGED');
    var consumedAtMs = new Date().getTime();
    if (current.expiresAtMs <= consumedAtMs) {
      props.deleteProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY);
      if (props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY)) {
        throw new Error('S3_MISSED_TRIGGER_EXPIRED_ARM_CLEAR_FAILED');
      }
      return { suppressed: false, reason: 'EXPIRED' };
    }

    var consumed = {
      version: current.version,
      nonce: current.nonce,
      alias: current.alias,
      kind: current.kind,
      source_locator: 'SHEET:' + String(sheetId) + ':ROW:' + String(rowNumber),
      raw_fingerprint: String(raw.rawFingerprint || ''),
      consumedAtMs: consumedAtMs
    };
    props.deleteProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY);
    props.setProperty(TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED_PROPERTY, JSON.stringify(consumed));
    if (props.getProperty(TTQS_S3_MISSED_TRIGGER_SUPPRESSION_PROPERTY)) {
      throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_CONSUME_FAILED');
    }
    var consumedReadback = ttqsParseJson_(props.getProperty(TTQS_S3_MISSED_TRIGGER_LAST_CONSUMED_PROPERTY), null);
    if (!consumedReadback ||
        String(consumedReadback.nonce || '') !== consumed.nonce ||
        String(consumedReadback.source_locator || '') !== consumed.source_locator ||
        String(consumedReadback.raw_fingerprint || '') !== consumed.raw_fingerprint) {
      throw new Error('S3_MISSED_TRIGGER_SUPPRESSION_CONSUMED_READBACK_MISMATCH');
    }
    return {
      suppressed: true,
      reason: 'P0_AUDIT_MISSED_TRIGGER_TEST',
      nonce: consumed.nonce,
      alias: consumed.alias,
      kind: consumed.kind,
      source_locator: consumed.source_locator,
      raw_fingerprint: consumed.raw_fingerprint
    };
  });
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
