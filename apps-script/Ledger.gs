function ttqsAttemptHistoryColumns_() {
  return [
    { header: 'attempt_event_id', description: '不可變事件編號' },
    { header: 'job_id', description: '工作編號' },
    { header: 'trace_id', description: '追蹤編號' },
    { header: 'event_type', description: '工作事件類型' },
    { header: 'object_type', description: '業務物件類型' },
    { header: 'object_id', description: '業務物件編號／原始來源' },
    { header: 'idempotency_key', description: '冪等鍵' },
    { header: 'source_ref', description: '原始提交來源參照' },
    { header: 'raw_fingerprint', description: '原始提交指紋' },
    { header: 'attempt_no', description: '第幾次嘗試' },
    { header: 'event_phase', description: 'JOB_CREATED／ATTEMPT_STARTED／STAGE／ATTEMPT_FAILED／ATTEMPT_SUCCEEDED／RECONCILIATION等' },
    { header: 'trigger_source', description: 'GOOGLE_FORM／TIME_RETRY／SYSTEM等' },
    { header: 'status', description: '當下狀態快照' },
    { header: 'started_at', description: '當次開始時間' },
    { header: 'finished_at', description: '當次結束時間' },
    { header: 'error_class', description: '當次錯誤類型；成功不得改寫既有失敗列' },
    { header: 'error_message', description: '當次錯誤訊息；成功不得改寫既有失敗列' },
    { header: 'retry_at', description: '預定重試時間' },
    { header: 'recovered', description: '是否為恢復成功' },
    { header: 'recovery_evidence_id', description: '恢復證據編號' },
    { header: 'reconciliation_status', description: '唯一對帳狀態' },
    { header: 'recorded_at', description: '此不可變事件寫入時間' },
    { header: 'previous_event_hash', description: '同一 Job 前一事件 hash' },
    { header: 'record_hash', description: '本事件 SHA-256；修改舊列會造成完整性失敗' },
    { header: 'notes', description: '結構化補充資訊' }
  ];
}

function ttqsEnsureAuditSchema_() {
  ttqsAssertTestOnly_();
  var cfg = ttqsConfig_();
  var ss = ttqsOpenCore_();
  var ledger = ss.getSheetByName(cfg.SHEETS.LEDGER);
  if (!ledger) throw new Error('MISSING_CORE_SHEET:' + cfg.SHEETS.LEDGER);
  ttqsEnsureColumns_(ledger, [
    { header: 'final_acceptance_status', description: 'FINAL_ACCEPTED／RECONCILIATION_PENDING／RECONCILIATION_EXCEPTION／NOT_ACCEPTED／NOT_APPLICABLE' },
    { header: 'final_accepted_at', description: '只有唯一對帳通過後才填入' }
  ]);
  var attemptHistory = ttqsEnsureStructuredSheet_(ss, cfg.SHEETS.ATTEMPT_HISTORY, ttqsAttemptHistoryColumns_());
  return { ledger: ledger, attemptHistory: attemptHistory };
}

function ttqsUpgradeAuditSchema() {
  return ttqsWithScriptLock_(function() {
    var schema = ttqsEnsureAuditSchema_();
    return {
      version: ttqsConfig_().VERSION,
      auditLogVersion: ttqsConfig_().AUDIT_LOG_VERSION,
      ledgerSheet: schema.ledger.getName(),
      attemptHistorySheet: schema.attemptHistory.getName(),
      status: 'PASS'
    };
  });
}

function ttqsLedgerSheet_() {
  return ttqsEnsureAuditSchema_().ledger;
}

function ttqsAttemptHistorySheet_() {
  return ttqsEnsureAuditSchema_().attemptHistory;
}

function ttqsLedgerFind_(idempotencyKey) {
  return ttqsFindUniqueRowByValue_(ttqsLedgerSheet_(), 'idempotency_key', idempotencyKey, 'DUPLICATE_LEDGER_IDEMPOTENCY_KEY');
}

function ttqsAuditNotes_(value) {
  return Object.assign({}, ttqsParseJson_(value, {}));
}

function ttqsJobUsesAppendOnlyAudit_(job) {
  var notes = ttqsAuditNotes_(job && job.object ? job.object.notes : '');
  return Number(notes.auditLogVersion || 0) >= Number(ttqsConfig_().AUDIT_LOG_VERSION || 2);
}

function ttqsAttemptHistoryCanonicalPayload_(row) {
  var columns = ttqsAttemptHistoryColumns_().map(function(column) { return column.header; });
  var canonical = {};
  columns.forEach(function(header) {
    if (header === 'record_hash') return;
    canonical[header] = String(Object.prototype.hasOwnProperty.call(row, header) ? row[header] : '');
  });
  return JSON.stringify(canonical);
}

function ttqsAttemptHistoryRecordHash_(row) {
  return ttqsDigest_(ttqsAttemptHistoryCanonicalPayload_(row));
}

function ttqsAttemptHistoryLastForJob_(jobId) {
  var rows = ttqsFindRowsByValue_(ttqsAttemptHistorySheet_(), 'job_id', jobId);
  return rows.length ? rows[rows.length - 1] : null;
}

function ttqsAttemptHistoryReadRow_(rowNumber) {
  var sheet = ttqsAttemptHistorySheet_();
  var headers = ttqsHeaders_(sheet);
  var values = sheet.getRange(rowNumber, 1, 1, headers.length).getDisplayValues()[0];
  return ttqsRowObject_(headers, values);
}

function ttqsAttemptHistoryAppend_(job, phase, patch) {
  patch = patch || {};
  if (!job || !job.object || !job.object.job_id) throw new Error('ATTEMPT_HISTORY_JOB_REQUIRED');
  var jobNotes = ttqsAuditNotes_(job.object.notes);
  var previous = ttqsAttemptHistoryLastForJob_(job.object.job_id);
  var recordedAt = String(patch.recorded_at || ttqsNow_());
  var attemptNo = String(Object.prototype.hasOwnProperty.call(patch, 'attempt_no') ? patch.attempt_no : (job.object.attempt_no || 0));
  var sourceRef = String(Object.prototype.hasOwnProperty.call(patch, 'source_ref') ? patch.source_ref : (jobNotes.sourceRef || jobNotes.rawRef || job.object.object_id || ''));
  var rawFingerprint = String(Object.prototype.hasOwnProperty.call(patch, 'raw_fingerprint') ? patch.raw_fingerprint : (jobNotes.rawFingerprint || ''));
  var recoveryEvidenceId = String(Object.prototype.hasOwnProperty.call(patch, 'recovery_evidence_id') ? patch.recovery_evidence_id : (jobNotes.recoveryEvidenceId || ''));
  var recoveredValue = Object.prototype.hasOwnProperty.call(patch, 'recovered') ? patch.recovered : (jobNotes.recovered === true);
  var row = {
    attempt_event_id: '',
    job_id: String(job.object.job_id || ''),
    trace_id: String(job.object.trace_id || ''),
    event_type: String(job.object.event_type || ''),
    object_type: String(job.object.object_type || ''),
    object_id: String(job.object.object_id || ''),
    idempotency_key: String(job.object.idempotency_key || ''),
    source_ref: sourceRef,
    raw_fingerprint: rawFingerprint,
    attempt_no: attemptNo,
    event_phase: String(phase || ''),
    trigger_source: String(Object.prototype.hasOwnProperty.call(patch, 'trigger_source') ? patch.trigger_source : (job.object.trigger_source || '')),
    status: String(Object.prototype.hasOwnProperty.call(patch, 'status') ? patch.status : (job.object.status || '')),
    started_at: String(Object.prototype.hasOwnProperty.call(patch, 'started_at') ? patch.started_at : (job.object.started_at || '')),
    finished_at: String(Object.prototype.hasOwnProperty.call(patch, 'finished_at') ? patch.finished_at : (job.object.finished_at || '')),
    error_class: String(Object.prototype.hasOwnProperty.call(patch, 'error_class') ? patch.error_class : (job.object.error_class || '')),
    error_message: String(Object.prototype.hasOwnProperty.call(patch, 'error_message') ? patch.error_message : (job.object.error_message || '')).slice(0, 500),
    retry_at: String(Object.prototype.hasOwnProperty.call(patch, 'retry_at') ? patch.retry_at : (job.object.retry_at || '')),
    recovered: recoveredValue === true ? 'TRUE' : 'FALSE',
    recovery_evidence_id: recoveryEvidenceId,
    reconciliation_status: String(Object.prototype.hasOwnProperty.call(patch, 'reconciliation_status') ? patch.reconciliation_status : (job.object.reconciliation_status || '')),
    recorded_at: recordedAt,
    previous_event_hash: previous ? String(previous.object.record_hash || '') : '',
    record_hash: '',
    notes: JSON.stringify(patch.notes || {})
  };
  row.attempt_event_id = ttqsStableId_('ATT-', row.job_id + '|' + row.attempt_no + '|' + row.event_phase + '|' + recordedAt + '|' + row.previous_event_hash + '|' + row.notes, 24);
  row.record_hash = ttqsAttemptHistoryRecordHash_(row);
  var sheet = ttqsAttemptHistorySheet_();
  var rowNumber = ttqsAppendObject_(sheet, row);
  SpreadsheetApp.flush();
  var readback = ttqsAttemptHistoryReadRow_(rowNumber);
  if (String(readback.attempt_event_id) !== String(row.attempt_event_id)) throw new Error('ATTEMPT_HISTORY_EVENT_ID_READBACK_MISMATCH');
  if (String(readback.record_hash) !== ttqsAttemptHistoryRecordHash_(readback)) throw new Error('ATTEMPT_HISTORY_HASH_READBACK_MISMATCH');
  return { rowNumber: rowNumber, object: readback };
}

function ttqsAdoptLegacyJobForAudit_(job) {
  if (ttqsJobUsesAppendOnlyAudit_(job)) return job;
  var oldNotes = ttqsAuditNotes_(job.object.notes);
  var adoptedNotes = Object.assign({}, oldNotes, {
    auditLogVersion: Number(ttqsConfig_().AUDIT_LOG_VERSION || 2),
    historyCompleteness: 'LEGACY_PARTIAL_PRE_V2',
    auditAdoptedAt: ttqsNow_()
  });
  var snapshotJob = {
    rowNumber: job.rowNumber,
    object: Object.assign({}, job.object, { notes: JSON.stringify(adoptedNotes) })
  };
  ttqsAttemptHistoryAppend_(snapshotJob, 'LEGACY_SNAPSHOT', {
    status: job.object.status,
    error_class: job.object.error_class || '',
    error_message: job.object.error_message || '',
    notes: { historicalCompleteness: 'PRE_V2_NOT_FULLY_AVAILABLE', originalAttemptNo: Number(job.object.attempt_no || 0) }
  });
  return ttqsLedgerPatch_(job, { notes: JSON.stringify(adoptedNotes) });
}

function ttqsLedgerEnsure_(spec) {
  var existing = ttqsLedgerFind_(spec.idempotencyKey);
  if (existing) return existing;
  var now = ttqsNow_();
  var jobId = ttqsStableId_('JOB-', spec.idempotencyKey, 18);
  var traceId = ttqsStableId_('TRACE-', spec.idempotencyKey, 18);
  var notes = Object.assign({}, spec.notes || {}, {
    auditLogVersion: Number(ttqsConfig_().AUDIT_LOG_VERSION || 2),
    historyCompleteness: 'COMPLETE_FROM_JOB_CREATION'
  });
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
    notes: JSON.stringify(notes),
    final_acceptance_status: spec.eventType === 'FORM_SUITE' ? 'NOT_PROCESSED' : 'NOT_APPLICABLE',
    final_accepted_at: ''
  };
  var rowNumber = ttqsAppendObject_(ttqsLedgerSheet_(), row);
  var job = { rowNumber: rowNumber, object: row, headers: ttqsHeaders_(ttqsLedgerSheet_()) };
  ttqsAttemptHistoryAppend_(job, 'JOB_CREATED', { status: 'QUEUED', attempt_no: 0, notes: { auditLogVersion: notes.auditLogVersion } });
  return job;
}

function ttqsLedgerPatch_(job, patch) {
  ttqsUpdateObjectRow_(ttqsLedgerSheet_(), job.rowNumber, patch);
  Object.keys(patch).forEach(function(k) { job.object[k] = patch[k]; });
  return job;
}

function ttqsLedgerStage_(job, stage, extra) {
  ttqsAdoptLegacyJobForAudit_(job);
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}), extra || {}, { stage: stage, stageAt: ttqsNow_() });
  ttqsLedgerPatch_(job, { notes: JSON.stringify(notes) });
  if (ttqsJobUsesAppendOnlyAudit_(job)) {
    ttqsAttemptHistoryAppend_(job, 'STAGE', { notes: Object.assign({ stage: stage }, extra || {}) });
  }
  return job;
}

function ttqsLedgerLeaseUntil_() {
  var leaseDate = new Date(Date.now() + Number(ttqsConfig_().RUNNING_LEASE_MINUTES || 5) * 60000);
  return Utilities.formatDate(leaseDate, ttqsConfig_().TIME_ZONE, "yyyy-MM-dd'T'HH:mm:ssZ");
}

function ttqsLedgerStart_(job, isRetry) {
  ttqsAdoptLegacyJobForAudit_(job);
  var attempt = Number(job.object.attempt_no || 0) + 1;
  var now = ttqsNow_();
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}));
  if (!notes.initialTriggerSource) notes.initialTriggerSource = job.object.trigger_source;
  notes.retry = !!isRetry;
  if (isRetry) notes.retryTrigger = 'TIME_RETRY';
  notes.leaseUntil = ttqsLedgerLeaseUntil_();
  notes.lastHeartbeatAt = now;
  var patch = {
    status: 'RUNNING',
    attempt_no: attempt,
    trigger_source: isRetry ? 'TIME_RETRY' : job.object.trigger_source,
    started_at: now,
    finished_at: '',
    retry_at: '',
    notes: JSON.stringify(notes)
  };
  if (job.object.event_type === 'FORM_SUITE') {
    patch.final_acceptance_status = 'PROCESSING';
    patch.final_accepted_at = '';
  }
  ttqsLedgerPatch_(job, patch);
  if (ttqsJobUsesAppendOnlyAudit_(job)) {
    ttqsAttemptHistoryAppend_(job, isRetry ? 'RETRY_STARTED' : 'ATTEMPT_STARTED', {
      attempt_no: attempt,
      status: 'RUNNING',
      trigger_source: patch.trigger_source,
      started_at: now,
      finished_at: '',
      error_class: '',
      error_message: '',
      retry_at: '',
      notes: { retry: !!isRetry, initialTriggerSource: notes.initialTriggerSource }
    });
  }
  return job;
}

function ttqsLedgerRunningLeaseExpired_(job, nowMillis) {
  if (String(job.object.status) !== 'RUNNING') return false;
  var now = Number(nowMillis || Date.now());
  var notes = ttqsParseJson_(job.object.notes, {});
  var leaseUntil = notes.leaseUntil ? new Date(notes.leaseUntil).getTime() : 0;
  if (!leaseUntil && job.object.started_at) {
    var started = new Date(job.object.started_at).getTime();
    if (isFinite(started)) leaseUntil = started + Number(ttqsConfig_().RUNNING_LEASE_MINUTES || 5) * 60000;
  }
  return !!leaseUntil && leaseUntil <= now;
}

function ttqsLedgerSuccess_(job, notesPatch) {
  ttqsAdoptLegacyJobForAudit_(job);
  var now = ttqsNow_();
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}), notesPatch || {});
  notes.leaseUntil = '';
  notes.lastHeartbeatAt = now;
  var patch = {
    status: 'SUCCESS',
    finished_at: now,
    retry_at: '',
    notes: JSON.stringify(notes)
  };
  if (job.object.event_type === 'FORM_SUITE') {
    patch.final_acceptance_status = 'RECONCILIATION_PENDING';
    patch.final_accepted_at = '';
  } else {
    patch.final_acceptance_status = 'NOT_APPLICABLE';
  }
  ttqsLedgerPatch_(job, patch);
  if (job.object.event_type === 'FORM_SUITE' && notes.recovered === true) {
    var recoveryEvidence = ttqsEnsureRuntimeRecoveryEvidence_(job);
    notes.recoveryEvidenceId = recoveryEvidence.evidenceId;
    ttqsLedgerPatch_(job, { notes: JSON.stringify(notes) });
  }
  if (ttqsJobUsesAppendOnlyAudit_(job)) {
    ttqsAttemptHistoryAppend_(job, 'ATTEMPT_SUCCEEDED', {
      attempt_no: Number(job.object.attempt_no || 0),
      status: 'SUCCESS',
      finished_at: now,
      error_class: '',
      error_message: '',
      retry_at: '',
      recovered: notes.recovered === true,
      recovery_evidence_id: notes.recoveryEvidenceId || '',
      notes: { recovered: notes.recovered === true, responseId: notes.responseId || '', evidenceId: notes.evidenceId || '' }
    });
  }
  return job;
}

function ttqsLedgerFail_(job, err) {
  ttqsAdoptLegacyJobForAudit_(job);
  var attempt = Number(job.object.attempt_no || 0);
  var maxAttempts = Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS);
  var retryDate = new Date(Date.now() + ttqsConfig_().RETRY_MINUTES * 60000);
  var now = ttqsNow_();
  var status = attempt >= maxAttempts ? 'FAILED_FINAL' : 'FAILED';
  var errorClass = err && err.name ? err.name : 'Error';
  var errorMessage = String(err && err.message ? err.message : err).slice(0, 500);
  var retryAt = attempt >= maxAttempts ? '' : Utilities.formatDate(retryDate, ttqsConfig_().TIME_ZONE, "yyyy-MM-dd'T'HH:mm:ssZ");
  var notes = Object.assign({}, ttqsParseJson_(job.object.notes, {}), {
    leaseUntil: '',
    lastHeartbeatAt: now
  });
  var patch = {
    status: status,
    finished_at: now,
    error_class: errorClass,
    error_message: errorMessage,
    retry_at: retryAt,
    notes: JSON.stringify(notes)
  };
  if (job.object.event_type === 'FORM_SUITE') {
    patch.final_acceptance_status = 'NOT_ACCEPTED';
    patch.final_accepted_at = '';
  }
  ttqsLedgerPatch_(job, patch);
  if (ttqsJobUsesAppendOnlyAudit_(job)) {
    ttqsAttemptHistoryAppend_(job, 'ATTEMPT_FAILED', {
      attempt_no: attempt,
      status: status,
      finished_at: now,
      error_class: errorClass,
      error_message: errorMessage,
      retry_at: retryAt,
      notes: { terminal: status === 'FAILED_FINAL' }
    });
  }
  return job;
}

function ttqsAttemptHistoryIntegrity_() {
  var historyRows = ttqsReadObjects_(ttqsAttemptHistorySheet_());
  var errors = [];
  var seenEventIds = {};
  var lastHashByJob = {};
  var eventsByJob = {};
  historyRows.forEach(function(entry) {
    var row = entry.object;
    var eventId = String(row.attempt_event_id || '');
    var jobId = String(row.job_id || '');
    if (!eventId) errors.push('MISSING_ATTEMPT_EVENT_ID:ROW_' + entry.rowNumber);
    if (seenEventIds[eventId]) errors.push('DUPLICATE_ATTEMPT_EVENT_ID:' + eventId);
    seenEventIds[eventId] = true;
    var expectedPrevious = String(lastHashByJob[jobId] || '');
    if (String(row.previous_event_hash || '') !== expectedPrevious) errors.push('HASH_CHAIN_PREVIOUS_MISMATCH:' + eventId);
    var computed = ttqsAttemptHistoryRecordHash_(row);
    if (String(row.record_hash || '') !== computed) errors.push('RECORD_HASH_MISMATCH:' + eventId);
    lastHashByJob[jobId] = String(row.record_hash || '');
    if (!eventsByJob[jobId]) eventsByJob[jobId] = [];
    eventsByJob[jobId].push(row);
  });

  var ledgerRows = ttqsReadObjects_(ttqsLedgerSheet_());
  var auditedJobs = 0;
  ledgerRows.forEach(function(entry) {
    var job = entry.object;
    var notes = ttqsAuditNotes_(job.notes);
    if (Number(notes.auditLogVersion || 0) < Number(ttqsConfig_().AUDIT_LOG_VERSION || 2)) return;
    auditedJobs++;
    var jobId = String(job.job_id || '');
    var events = eventsByJob[jobId] || [];
    if (!events.length) {
      errors.push('AUDITED_JOB_WITHOUT_HISTORY:' + jobId);
      return;
    }
    var currentAttempt = Number(job.attempt_no || 0);
    function hasPhase(attemptNo, phase) {
      return events.some(function(event) { return Number(event.attempt_no || 0) === Number(attemptNo) && String(event.event_phase) === phase; });
    }
    if (String(job.status) === 'SUCCESS' && !hasPhase(currentAttempt, 'ATTEMPT_SUCCEEDED')) errors.push('SUCCESS_WITHOUT_SUCCESS_EVENT:' + jobId + ':' + currentAttempt);
    if ((String(job.status) === 'FAILED' || String(job.status) === 'FAILED_FINAL') && !hasPhase(currentAttempt, 'ATTEMPT_FAILED')) errors.push('FAILED_WITHOUT_FAILURE_EVENT:' + jobId + ':' + currentAttempt);
    if (currentAttempt > 1 && notes.historyCompleteness !== 'LEGACY_PARTIAL_PRE_V2') {
      for (var attempt = 1; attempt < currentAttempt; attempt++) {
        if (!hasPhase(attempt, 'ATTEMPT_FAILED')) errors.push('RETRY_WITHOUT_PRIOR_FAILURE_EVENT:' + jobId + ':' + attempt);
      }
    }
    if (String(job.final_acceptance_status || '') === 'FINAL_ACCEPTED' && String(job.reconciliation_status || '') !== 'MATCHED_EXACTLY_ONCE') {
      errors.push('FINAL_ACCEPTED_WITHOUT_EXACT_RECONCILIATION:' + jobId);
    }
    if (String(job.reconciliation_status || '') === 'MATCHED_EXACTLY_ONCE' && String(job.event_type || '') === 'FORM_SUITE' && String(job.final_acceptance_status || '') !== 'FINAL_ACCEPTED') {
      errors.push('EXACT_RECONCILIATION_WITHOUT_FINAL_ACCEPTANCE:' + jobId);
    }
  });

  return {
    status: errors.length ? 'FAIL' : 'PASS',
    rows: historyRows.length,
    auditedJobs: auditedJobs,
    errors: errors
  };
}

function ttqsAuditJobSnapshot(jobId) {
  ttqsAssertTestOnly_();
  var jobs = ttqsFindRowsByValue_(ttqsLedgerSheet_(), 'job_id', jobId);
  if (jobs.length !== 1) throw new Error('AUDIT_JOB_NOT_UNIQUE:' + jobId + ':' + jobs.length);
  var attempts = ttqsFindRowsByValue_(ttqsAttemptHistorySheet_(), 'job_id', jobId).map(function(entry) { return entry.object; });
  return {
    job: jobs[0].object,
    attempts: attempts,
    integrity: ttqsAttemptHistoryIntegrity_()
  };
}
