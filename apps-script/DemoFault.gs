function ttqsP0AuditAlias_(aliasCode) {
  var value = String(aliasCode || '').trim().toUpperCase();
  return /^S-P0AUDIT-[A-Z0-9]{4,12}$/.test(value) ? value : '';
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
