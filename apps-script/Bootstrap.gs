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

function ttqsInstallManagedTriggers_() {
  ttqsRemoveManagedTriggers_();
  var ss = ttqsOpenCore_();
  ScriptApp.newTrigger('ttqsOnSpreadsheetFormSubmit').forSpreadsheet(ss).onFormSubmit().create();
  ScriptApp.newTrigger('ttqsRetryFailedJobs').timeBased().everyMinutes(1).create();
  ScriptApp.newTrigger('ttqsReconcile').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('ttqsRefreshConsultView').timeBased().everyHours(1).create();
  return true;
}

function ttqsBootstrapTest() {
  ttqsAssertTestOnly_();
  var preHealth = ttqsHealthCheck();
  if (preHealth.status !== 'PASS') throw new Error('PRE_BOOTSTRAP_HEALTH_FAIL:' + JSON.stringify(preHealth.failed));
  var forms = ttqsEnsureForms_();
  ttqsInstallManagedTriggers_();
  var consult = ttqsRefreshConsultView();
  var key = 'TEST:BOOTSTRAP:' + ttqsConfig_().VERSION;
  var job = ttqsLedgerEnsure_({
    eventType: 'TEST_BOOTSTRAP',
    objectType: 'Runtime',
    objectId: ttqsConfig_().VERSION,
    idempotencyKey: key,
    triggerSource: 'MANUAL_BOOTSTRAP',
    maxAttempts: 1,
    notes: { forms: forms.map(function(f) { return { kind: f.kind, formId: f.formId, responseSheetId: f.responseSheetId }; }) }
  });
  if (job.object.status !== 'SUCCESS') {
    ttqsLedgerStart_(job, false);
    ttqsLedgerSuccess_(job, { consultRows: consult.rows, bootstrap: true });
  }
  return {
    version: ttqsConfig_().VERSION,
    environment: 'TEST',
    health: ttqsHealthCheck(),
    forms: forms,
    consult: consult,
    realWrites: false,
    piiVaultReady: false,
    next: 'Submit the published forms through the real Google Forms UI; do not synthesize submissions programmatically.'
  };
}
