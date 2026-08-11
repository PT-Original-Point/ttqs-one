function ttqsRetryJobEligible_(job, nowMillis) {
  var status = String(job.object.status || '');
  var attempt = Number(job.object.attempt_no || 0);
  var maxAttempts = Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS);
  if (attempt >= maxAttempts) return false;
  if (status === 'RUNNING') return ttqsLedgerRunningLeaseExpired_(job, nowMillis);
  if (status !== 'FAILED') return false;
  var retryAt = job.object.retry_at ? new Date(job.object.retry_at).getTime() : 0;
  return !retryAt || retryAt <= nowMillis;
}

function ttqsRetryFailedJobsUnlocked_() {
  ttqsAssertTestOnly_();
  var now = new Date().getTime();
  var rows = ttqsReadObjects_(ttqsLedgerSheet_());
  var results = [];
  rows.forEach(function(entry) {
    var job = { rowNumber: entry.rowNumber, object: entry.object };
    if (!ttqsRetryJobEligible_(job, now)) return;
    var wasStaleRunning = String(job.object.status) === 'RUNNING';
    try {
      if (wasStaleRunning) {
        ttqsLedgerStage_(job, 'STALE_RUNNING_TAKEOVER', {
          staleRunningRecovered: true,
          staleRunningObservedAt: ttqsNow_()
        });
      }
      if (job.object.event_type === 'FORM_SUITE') {
        var notes = ttqsParseJson_(job.object.notes, {});
        if (!notes.rawRef || notes.sheetId === undefined || notes.sheetId === null) {
          throw new Error('FORM_SUITE_RETRY_PROVENANCE_MISSING');
        }
        var raw = ttqsFindRawSubmissionByRef_(Number(notes.sheetId), String(notes.rawRef));
        results.push(ttqsHandleRawObjectUnlocked_(raw, true));
      } else if (job.object.event_type === 'FAULT_PROBE') {
        ttqsLedgerStart_(job, true);
        ttqsLedgerSuccess_(job, { recovered: true, faultProbe: true, staleRunningRecovered: wasStaleRunning });
        results.push({ jobId: job.object.job_id, recovered: true, staleRunningRecovered: wasStaleRunning });
      }
    } catch (err) {
      if (String(job.object.status) === 'RUNNING') ttqsLedgerFail_(job, err);
      results.push({ jobId: job.object.job_id, error: String(err.message || err), staleRunningRecovered: wasStaleRunning });
    }
  });
  return results;
}

function ttqsRetryFailedJobs() {
  return ttqsWithScriptLock_(ttqsRetryFailedJobsUnlocked_);
}
