function ttqsLedgerSheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.LEDGER);
}

function ttqsLedgerFind_(idempotencyKey) {
  return ttqsFindUniqueRowByValue_(ttqsLedgerSheet_(), 'idempotency_key', idempotencyKey, 'DUPLICATE_LEDGER_IDEMPOTENCY_KEY');
}

function ttqsLedgerEnsure_(spec) {
  var existing = ttqsLedgerFind_(spec.idempotencyKey);
  if (existing) return existing;
  var now = ttqsNow_();
  var jobId = ttqsStableId_('JOB-', spec.idempotencyKey, 18);
  var traceId = ttqsStableId_('TRACE-', spec.idempotencyKey, 18);
  var row = {
    job_id: jobId,
    event_type: spec.eventType,
    environment: 'TEST',
    object_type: spec.objectType,
    object_id: spec.objectId,
    idempotency_key: spec.idempotencyKey,
    trigger_source: spec.triggerSource || 'SYSTEM',
    scheduled_at: now,
    started_at: '',
    finished_at: '',
    status: 'QUEUED',
    attempt_no: 0,
    max_attempts: spec.maxAttempts || ttqsConfig_().MAX_ATTEMPTS,
    error_class: '',
    error_message: '',
    retry_at: '',
    reconciliation_date: '',
    reconciliation_status: '',
    operator: spec.operator || 'Apps Script',
    trace_id: traceId,
    notes: JSON.stringify(spec.notes || {})
  };
  var rowNumber = ttqsAppendObject_(ttqsLedgerSheet_(), row);
  return { rowNumber: rowNumber, object: row, headers: ttqsHeaders_(ttqsLedgerSheet_()) };
}

function ttqsLedgerPatch_(job, patch) {
  ttqsUpdateObjectRow_(ttqsLedgerSheet_(), job.rowNumber, patch);
  Object.keys(patch).forEach(function(k) { job.object[k] = patch[k]; });
  return job;
}

function ttqsLedgerStage_(job, stage, extra) {
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}), extra || {}, { stage: stage, stageAt: ttqsNow_() });
  return ttqsLedgerPatch_(job, { notes: JSON.stringify(notes) });
}

function ttqsLedgerStart_(job, isRetry) {
  var attempt = Number(job.object.attempt_no || 0) + 1;
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}));
  if (!notes.initialTriggerSource) notes.initialTriggerSource = job.object.trigger_source;
  notes.retry = !!isRetry;
  if (isRetry) notes.retryTrigger = 'TIME_RETRY';
  return ttqsLedgerPatch_(job, {
    status: 'RUNNING',
    attempt_no: attempt,
    trigger_source: isRetry ? 'TIME_RETRY' : job.object.trigger_source,
    started_at: ttqsNow_(),
    finished_at: '',
    error_class: '',
    error_message: '',
    retry_at: '',
    notes: JSON.stringify(notes)
  });
}

function ttqsLedgerSuccess_(job, notesPatch) {
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}), notesPatch || {});
  ttqsLedgerPatch_(job, {
    status: 'SUCCESS',
    finished_at: ttqsNow_(),
    retry_at: '',
    notes: JSON.stringify(notes)
  });
  if (job.object.event_type === 'FORM_SUITE' && notes.recovered === true) {
    var recoveryEvidence = ttqsEnsureRuntimeRecoveryEvidence_(job);
    notes.recoveryEvidenceId = recoveryEvidence.evidenceId;
    ttqsLedgerPatch_(job, { notes: JSON.stringify(notes) });
  }
  return job;
}

function ttqsLedgerFail_(job, err) {
  var attempt = Number(job.object.attempt_no || 0);
  var maxAttempts = Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS);
  var retryDate = new Date(Date.now() + ttqsConfig_().RETRY_MINUTES * 60000);
  return ttqsLedgerPatch_(job, {
    status: attempt >= maxAttempts ? 'FAILED_FINAL' : 'FAILED',
    finished_at: ttqsNow_(),
    error_class: err && err.name ? err.name : 'Error',
    error_message: String(err && err.message ? err.message : err).slice(0, 500),
    retry_at: attempt >= maxAttempts ? '' : Utilities.formatDate(retryDate, ttqsConfig_().TIME_ZONE, "yyyy-MM-dd'T'HH:mm:ssZ")
  });
}
