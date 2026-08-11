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
