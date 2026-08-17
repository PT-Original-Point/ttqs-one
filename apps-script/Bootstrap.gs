function ttqsRemoveManagedTriggers_() {
  var handlers = {
    ttqsOnSpreadsheetFormSubmit: true,
    ttqsRetryFailedJobs: true,
    ttqsReconcile: true,
    ttqsRefreshConsultView: true
  };
  ScriptApp.getProjectTriggers().forEach(function(trigger) {
    if (handlers[trigger.getHandlerFunction()]) ScriptApp.deleteTrigger(trigger);
  });
}

function ttqsManagedTriggerSnapshot_() {
  var counts = {};
  ScriptApp.getProjectTriggers().forEach(function(trigger) {
    var handler = trigger.getHandlerFunction();
    counts[handler] = Number(counts[handler] || 0) + 1;
  });
  return counts;
}

function ttqsManagedTriggerDetails_() {
  var handlers = {
    ttqsOnSpreadsheetFormSubmit: true,
    ttqsRetryFailedJobs: true,
    ttqsReconcile: true,
    ttqsRefreshConsultView: true
  };
  return ScriptApp.getProjectTriggers().filter(function(trigger) {
    return !!handlers[trigger.getHandlerFunction()];
  }).map(function(trigger) {
    return {
      handler: trigger.getHandlerFunction(),
      eventType: String(trigger.getEventType()),
      triggerSource: String(trigger.getTriggerSource()),
      triggerSourceId: trigger.getTriggerSourceId ? String(trigger.getTriggerSourceId() || '') : ''
    };
  });
}

function ttqsAssertLegacyManagedTriggerContract_() {
  var cfg = ttqsConfig_();
  var triggers = ScriptApp.getProjectTriggers();
  var expected = {
    ttqsOnSpreadsheetFormSubmit: { eventType: ScriptApp.EventType.ON_FORM_SUBMIT, source: ScriptApp.TriggerSource.SPREADSHEETS, sourceId: cfg.CORE_SPREADSHEET_ID },
    ttqsRetryFailedJobs: { eventType: ScriptApp.EventType.CLOCK, source: ScriptApp.TriggerSource.CLOCK },
    ttqsReconcile: { eventType: ScriptApp.EventType.CLOCK, source: ScriptApp.TriggerSource.CLOCK },
    ttqsRefreshConsultView: { eventType: ScriptApp.EventType.CLOCK, source: ScriptApp.TriggerSource.CLOCK }
  };
  var matched = {};
  triggers.forEach(function(trigger) {
    var handler = trigger.getHandlerFunction();
    if (!expected[handler]) return;
    matched[handler] = Number(matched[handler] || 0) + 1;
    var contract = expected[handler];
    if (trigger.getEventType() !== contract.eventType) throw new Error('MANAGED_TRIGGER_EVENT_TYPE_INVALID:' + handler);
    if (trigger.getTriggerSource() !== contract.source) throw new Error('MANAGED_TRIGGER_SOURCE_INVALID:' + handler);
    if (contract.sourceId && String(trigger.getTriggerSourceId ? trigger.getTriggerSourceId() : '') !== String(contract.sourceId)) {
      throw new Error('MANAGED_TRIGGER_SOURCE_ID_INVALID:' + handler);
    }
  });
  Object.keys(expected).forEach(function(handler) {
    if (Number(matched[handler] || 0) !== 1) throw new Error('MANAGED_TRIGGER_COUNT_INVALID:' + handler + ':' + Number(matched[handler] || 0));
  });
  return { counts: matched, details: ttqsManagedTriggerDetails_(), mode: 'LEGACY_S1' };
}

function ttqsAssertManagedTriggerContract_() {
  if (typeof ttqsSchedulerRuntimeMode_ === 'function' && typeof TTQS_S3_MODE !== 'undefined' && ttqsSchedulerRuntimeMode_() === TTQS_S3_MODE) {
    if (typeof ttqsAssertS3TriggerContract_ !== 'function') throw new Error('S3_TRIGGER_CONTRACT_REQUIRED');
    return ttqsAssertS3TriggerContract_();
  }
  if (typeof ttqsSchedulerRuntimeMode_ === 'function' && typeof TTQS_S2_MODE !== 'undefined' && ttqsSchedulerRuntimeMode_() === TTQS_S2_MODE) {
    if (typeof ttqsAssertS2TriggerContract_ !== 'function') throw new Error('S2_TRIGGER_CONTRACT_REQUIRED');
    return ttqsAssertS2TriggerContract_();
  }
  return ttqsAssertLegacyManagedTriggerContract_();
}

function ttqsInstallManagedTriggers_() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  if (typeof ttqsSchedulerRuntimeMode_ === 'function' && typeof TTQS_S3_MODE !== 'undefined' && ttqsSchedulerRuntimeMode_() === TTQS_S3_MODE) throw new Error('S3_MANAGED_TRIGGER_REINSTALL_FORBIDDEN');
  if (typeof ttqsSchedulerRuntimeMode_ === 'function' && typeof TTQS_S2_MODE !== 'undefined' && ttqsSchedulerRuntimeMode_() === TTQS_S2_MODE) {
    throw new Error('S2_MANAGED_TRIGGER_REINSTALL_FORBIDDEN');
  }
  ttqsRemoveManagedTriggers_();
  var ss = ttqsOpenCore_();
  ScriptApp.newTrigger('ttqsOnSpreadsheetFormSubmit').forSpreadsheet(ss).onFormSubmit().create();
  ScriptApp.newTrigger('ttqsRetryFailedJobs').timeBased().everyMinutes(1).create();
  ScriptApp.newTrigger('ttqsReconcile').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('ttqsRefreshConsultView').timeBased().everyHours(1).create();
  return ttqsAssertLegacyManagedTriggerContract_();
}

function ttqsBootstrapTestLocked_() {
  ttqsAssertTestOnly_();
  if (typeof ttqsEnsureAuditSchema_ === 'function') ttqsEnsureAuditSchema_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE === true && typeof ttqsEnsureObservationSheet_ === 'function') {
    ttqsEnsureObservationSheet_();
  }
  var preHealth = ttqsHealthCheck();
  if (preHealth.status !== 'PASS') throw new Error('PRE_BOOTSTRAP_HEALTH_FAIL:' + JSON.stringify(preHealth.failed));

  var key = 'TEST:BOOTSTRAP:' + ttqsConfig_().VERSION;
  var job = ttqsLedgerEnsure_({
    eventType: 'TEST_BOOTSTRAP',
    objectType: 'Runtime',
    objectId: ttqsConfig_().VERSION,
    idempotencyKey: key,
    triggerSource: 'MANUAL_BOOTSTRAP',
    maxAttempts: ttqsConfig_().MAX_ATTEMPTS,
    notes: { bootstrapVersion: ttqsConfig_().VERSION }
  });

  if (job.object.status === 'SUCCESS') {
    var reusedForms = ttqsEnsureForms_();
    var reusedTriggers = ttqsAssertManagedTriggerContract_();
    return {
      version: ttqsConfig_().VERSION,
      environment: 'TEST',
      health: ttqsHealthCheck(),
      forms: reusedForms,
      consult: { sheet: ttqsConfig_().AUTO_CONSULT_SHEET, reusedBootstrap: true },
      triggers: reusedTriggers,
      duplicateBootstrap: true,
      realWrites: false,
      piiVaultReady: false,
      next: 'Submit the published forms through the real Google Forms UI; do not synthesize submissions programmatically.'
    };
  }

  if (Number(job.object.attempt_no || 0) >= Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS)) {
    throw new Error('BOOTSTRAP_MAX_ATTEMPTS_EXCEEDED');
  }

  ttqsLedgerStart_(job, false);
  try {
    ttqsLedgerStage_(job, 'ENSURE_FORMS');
    var forms = ttqsEnsureForms_();
    ttqsLedgerStage_(job, 'INSTALL_TRIGGERS', { forms: forms.map(function(f) { return { kind: f.kind, formId: f.formId, responseSheetId: f.responseSheetId, published: f.published }; }) });
    var triggers = ttqsInstallManagedTriggers_();
    ttqsLedgerStage_(job, 'REFRESH_CONSULT');
    var consult = ttqsRefreshConsultViewUnlocked_();
    ttqsLedgerStage_(job, 'POST_HEALTH');
    var postHealth = ttqsHealthCheck();
    if (postHealth.status !== 'PASS') throw new Error('POST_BOOTSTRAP_HEALTH_FAIL:' + JSON.stringify(postHealth.failed));
    ttqsLedgerSuccess_(job, { bootstrap: true, forms: forms.map(function(f) { return { kind: f.kind, formId: f.formId, responseSheetId: f.responseSheetId, published: f.published }; }), triggers: triggers, consultRows: consult.rows, stage: 'COMPLETE' });
    return {
      version: ttqsConfig_().VERSION,
      environment: 'TEST',
      health: postHealth,
      forms: forms,
      consult: consult,
      triggers: triggers,
      duplicateBootstrap: false,
      realWrites: false,
      piiVaultReady: false,
      next: 'Submit the published forms through the real Google Forms UI; do not synthesize submissions programmatically.'
    };
  } catch (err) {
    ttqsLedgerFail_(job, err);
    throw err;
  }
}

function ttqsBootstrapTest() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  return ttqsWithScriptLock_(ttqsBootstrapTestLocked_);
}
