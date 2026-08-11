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

function ttqsInstallManagedTriggers_() {
  ttqsRemoveManagedTriggers_();
  var ss = ttqsOpenCore_();
  ScriptApp.newTrigger('ttqsOnSpreadsheetFormSubmit').forSpreadsheet(ss).onFormSubmit().create();
  ScriptApp.newTrigger('ttqsRetryFailedJobs').timeBased().everyMinutes(1).create();
  ScriptApp.newTrigger('ttqsReconcile').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('ttqsRefreshConsultView').timeBased().everyHours(1).create();
  var counts = ttqsManagedTriggerSnapshot_();
  ['ttqsOnSpreadsheetFormSubmit', 'ttqsRetryFailedJobs', 'ttqsReconcile', 'ttqsRefreshConsultView'].forEach(function(handler) {
    if (Number(counts[handler] || 0) !== 1) throw new Error('MANAGED_TRIGGER_COUNT_INVALID:' + handler + ':' + Number(counts[handler] || 0));
  });
  return counts;
}

function ttqsBootstrapTestLocked_() {
  ttqsAssertTestOnly_();
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
    return {
      version: ttqsConfig_().VERSION,
      environment: 'TEST',
      health: ttqsHealthCheck(),
      forms: reusedForms,
      consult: { sheet: ttqsConfig_().AUTO_CONSULT_SHEET, reusedBootstrap: true },
      triggers: ttqsManagedTriggerSnapshot_(),
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
    ttqsLedgerStage_(job, 'INSTALL_TRIGGERS', { forms: forms.map(function(f) { return { kind: f.kind, formId: f.formId, responseSheetId: f.responseSheetId }; }) });
    var triggers = ttqsInstallManagedTriggers_();
    ttqsLedgerStage_(job, 'REFRESH_CONSULT');
    var consult = ttqsRefreshConsultViewUnlocked_();
    ttqsLedgerStage_(job, 'POST_HEALTH');
    var postHealth = ttqsHealthCheck();
    if (postHealth.status !== 'PASS') throw new Error('POST_BOOTSTRAP_HEALTH_FAIL:' + JSON.stringify(postHealth.failed));
    ttqsLedgerSuccess_(job, { bootstrap: true, forms: forms.map(function(f) { return { kind: f.kind, formId: f.formId, responseSheetId: f.responseSheetId }; }), triggers: triggers, consultRows: consult.rows, stage: 'COMPLETE' });
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
