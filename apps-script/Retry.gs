function ttqsRetryFailedJobs() {
  ttqsAssertTestOnly_();
  var now = new Date().getTime();
  var rows = ttqsReadObjects_(ttqsLedgerSheet_());
  var results = [];
  rows.forEach(function(entry) {
    var job = { rowNumber: entry.rowNumber, object: entry.object };
    if (job.object.status !== 'FAILED') return;
    var attempt = Number(job.object.attempt_no || 0);
    var maxAttempts = Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS);
    if (attempt >= maxAttempts) return;
    var retryAt = job.object.retry_at ? new Date(job.object.retry_at).getTime() : 0;
    if (retryAt && retryAt > now) return;
    try {
      if (job.object.event_type === 'FORM_SUITE') {
        var parts = String(job.object.object_id).split(':');
        results.push(ttqsHandleRawSubmission_(Number(parts[0]), Number(parts[1]), true));
      } else if (job.object.event_type === 'FAULT_PROBE') {
        ttqsLedgerStart_(job, true);
        ttqsLedgerSuccess_(job, { recovered: true, faultProbe: true });
        results.push({ jobId: job.object.job_id, recovered: true });
      }
    } catch (err) {
      results.push({ jobId: job.object.job_id, error: String(err.message || err) });
    }
  });
  return results;
}
