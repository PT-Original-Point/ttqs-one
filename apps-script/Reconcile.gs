function ttqsExpectedSurveyTypeForKind_(kind) {
  var map = { NEEDS: 'NEEDS', REGISTRATION: 'REGISTRATION', REACTION: 'REACTION', FOLLOWUP30: '30_DAY_BEHAVIOR' };
  var value = map[String(kind)];
  if (!value) throw new Error('UNKNOWN_FORM_KIND_FOR_RECONCILE:' + kind);
  return value;
}

function ttqsReconciliationAcceptanceStatus_(reconciliationStatus) {
  return String(reconciliationStatus) === 'MATCHED_EXACTLY_ONCE' ? 'FINAL_ACCEPTED' : 'RECONCILIATION_EXCEPTION';
}

function ttqsApplyReconciliationResult_(ledger, reconciliationStatus, detail) {
  var desiredAcceptance = ttqsReconciliationAcceptanceStatus_(reconciliationStatus);
  var now = ttqsNow_();
  var currentStatus = String(ledger.object.reconciliation_status || '');
  var currentAcceptance = String(ledger.object.final_acceptance_status || '');
  var patch = {
    reconciliation_date: ttqsDateOnly_(new Date()),
    reconciliation_status: String(reconciliationStatus),
    final_acceptance_status: desiredAcceptance,
    final_accepted_at: desiredAcceptance === 'FINAL_ACCEPTED' ? (ledger.object.final_accepted_at || now) : ''
  };
  var changed = currentStatus !== patch.reconciliation_status || currentAcceptance !== patch.final_acceptance_status || (desiredAcceptance === 'FINAL_ACCEPTED' && !ledger.object.final_accepted_at);
  ttqsLedgerPatch_(ledger, patch);
  if (changed && ttqsJobUsesAppendOnlyAudit_(ledger)) {
    ttqsAttemptHistoryAppend_(ledger, 'RECONCILIATION', {
      status: ledger.object.status,
      reconciliation_status: String(reconciliationStatus),
      recovered: ttqsAuditNotes_(ledger.object.notes).recovered === true,
      notes: {
        finalAcceptanceStatus: desiredAcceptance,
        linkageErrors: detail && detail.linkageErrors ? detail.linkageErrors : [],
        ledgerCount: detail && detail.ledgerCount !== undefined ? detail.ledgerCount : '',
        partyCount: detail && detail.partyCount !== undefined ? detail.partyCount : '',
        surveyCount: detail && detail.surveyCount !== undefined ? detail.surveyCount : '',
        evidenceCount: detail && detail.evidenceCount !== undefined ? detail.evidenceCount : ''
      }
    });
  }
  return ledger;
}

function ttqsReconcileRaw_(raw) {
  var cfg = ttqsConfig_();
  var detail = {
    rawRef: raw.rawRef,
    eventId: raw.eventId,
    rawFingerprint: raw.rawFingerprint,
    formId: raw.formId,
    sheetId: raw.sheetId,
    observedRowNumber: raw.rowNumber,
    kind: raw.kind,
    ledgerCount: 0,
    surveyCount: 0,
    partyCount: 0,
    evidenceCount: 0,
    linkageErrors: []
  };

  if (!raw.eventId || !raw.rawRef) {
    detail.status = 'MISMATCH_EVENT_ID_MISSING';
    return detail;
  }

  var idempotencyKey = 'TEST:' + raw.rawRef;
  detail.idempotencyKey = idempotencyKey;
  var ledgerRows = ttqsFindRowsByValue_(ttqsLedgerSheet_(), 'idempotency_key', idempotencyKey);
  detail.ledgerCount = ledgerRows.length;
  if (ledgerRows.length === 0) {
    detail.status = 'MISMATCH_TRIGGER_MISSED';
    return detail;
  }
  if (ledgerRows.length > 1) {
    detail.status = 'MISMATCH_LEDGER_DUPLICATE';
    return detail;
  }

  var ledger = ledgerRows[0];
  var job = ledger.object;
  var notes = ttqsParseJson_(job.notes, {});
  detail.jobId = job.job_id;
  detail.jobStatus = job.status;

  if (String(job.status) !== 'SUCCESS') detail.linkageErrors.push('JOB_NOT_SUCCESS:' + String(job.status));
  if (String(job.environment) !== 'TEST') detail.linkageErrors.push('JOB_ENVIRONMENT:' + String(job.environment));
  if (String(job.object_type) !== String(raw.kind)) detail.linkageErrors.push('JOB_OBJECT_TYPE:' + String(job.object_type));
  if (String(job.object_id) !== String(raw.rawRef)) detail.linkageErrors.push('JOB_OBJECT_ID');
  if (String(notes.rawRef || '') !== String(raw.rawRef)) detail.linkageErrors.push('JOB_RAW_REF');
  if (String(notes.eventId || '') !== String(raw.eventId)) detail.linkageErrors.push('JOB_EVENT_ID');
  if (String(notes.rawFingerprint || '') !== String(raw.rawFingerprint)) detail.linkageErrors.push('JOB_RAW_FINGERPRINT');
  if (String(notes.formId || '') !== String(raw.formId)) detail.linkageErrors.push('JOB_FORM_ID');

  var surveyRows = ttqsFindRowsByValue_(ttqsSurveySheet_(), 'source_ref', raw.rawRef);
  detail.surveyCount = surveyRows.length;
  var aliasCode = String(notes.aliasCode || raw.named.TTQS_ALIAS_CODE || '');
  var partyRows = aliasCode ? ttqsFindRowsByValue_(ttqsPartySheet_(), 'alias_code', aliasCode) : [];
  detail.partyCount = partyRows.length;
  var evidenceId = String(notes.evidenceId || '');
  var evidenceRows = evidenceId ? ttqsFindRowsByValue_(ttqsEvidenceSheet_(), 'evidence_id', evidenceId) : [];
  detail.evidenceCount = evidenceRows.length;

  if (surveyRows.length !== 1) detail.linkageErrors.push('SURVEY_COUNT:' + surveyRows.length);
  if (partyRows.length !== 1) detail.linkageErrors.push('PARTY_COUNT:' + partyRows.length);
  if (evidenceRows.length !== 1) detail.linkageErrors.push('EVIDENCE_COUNT:' + evidenceRows.length);

  if (surveyRows.length === 1 && partyRows.length === 1) {
    var survey = surveyRows[0].object;
    var party = partyRows[0].object;
    var surveyNotes = ttqsParseJson_(survey.notes, {});
    if (String(survey.class_run_id) !== String(cfg.CLASS_RUN_ID)) detail.linkageErrors.push('SURVEY_CLASS_RUN');
    if (String(survey.party_alias_id) !== String(party.party_alias_id)) detail.linkageErrors.push('SURVEY_PARTY_LINK');
    if (String(survey.survey_type) !== ttqsExpectedSurveyTypeForKind_(raw.kind)) detail.linkageErrors.push('SURVEY_TYPE');
    if (String(survey.source_ref) !== String(raw.rawRef)) detail.linkageErrors.push('SURVEY_SOURCE_REF');
    if (String(surveyNotes.job_id || '') !== String(job.job_id)) detail.linkageErrors.push('SURVEY_JOB_LINK');
    if (String(surveyNotes.provider_form_id || '') !== String(raw.formId)) detail.linkageErrors.push('SURVEY_FORM_ID');
    if (String(surveyNotes.provider_raw_fingerprint || '') !== String(raw.rawFingerprint)) detail.linkageErrors.push('SURVEY_RAW_FINGERPRINT');
  }

  if (surveyRows.length === 1 && evidenceRows.length === 1) {
    var surveyObject = surveyRows[0].object;
    var evidence = evidenceRows[0].object;
    var evidenceNotes = ttqsParseJson_(evidence.notes, {});
    if (String(evidence.environment) !== 'TEST') detail.linkageErrors.push('EVIDENCE_ENVIRONMENT');
    if (String(evidence.data_class) !== 'SAMPLE') detail.linkageErrors.push('EVIDENCE_DATA_CLASS');
    if (String(evidence.class_run_id) !== String(cfg.CLASS_RUN_ID)) detail.linkageErrors.push('EVIDENCE_CLASS_RUN');
    if (String(evidence.source_object_type) !== 'SurveyResponse') detail.linkageErrors.push('EVIDENCE_SOURCE_TYPE');
    if (String(evidence.source_object_id) !== String(surveyObject.response_id)) detail.linkageErrors.push('EVIDENCE_SURVEY_LINK');
    if (String(evidenceNotes.formal_admissibility || '') !== 'NOT_FORMAL') detail.linkageErrors.push('EVIDENCE_FORMAL_ADMISSIBILITY');
    if (String(evidenceNotes.source_ref || '') !== String(raw.rawRef)) detail.linkageErrors.push('EVIDENCE_SOURCE_REF');
    if (String(evidenceNotes.job_id || '') !== String(job.job_id)) detail.linkageErrors.push('EVIDENCE_JOB_LINK');
    if (String(evidenceNotes.provider_form_id || '') !== String(raw.formId)) detail.linkageErrors.push('EVIDENCE_FORM_ID');
    if (String(evidenceNotes.provider_raw_fingerprint || '') !== String(raw.rawFingerprint)) detail.linkageErrors.push('EVIDENCE_RAW_FINGERPRINT');
  }

  detail.status = detail.linkageErrors.length ? 'MISMATCH_CROSS_LINK' : 'MATCHED_EXACTLY_ONCE';
  ttqsApplyReconciliationResult_(ledger, detail.status, detail);
  return detail;
}

function ttqsReconciliationWatchdog_() {
  var cfg = ttqsConfig_();
  var now = Date.now();
  var graceMs = Number(cfg.RECONCILIATION_GRACE_MINUTES || 70) * 60000;
  var issues = [];
  var pendingWithinGrace = [];
  ttqsReadObjects_(ttqsLedgerSheet_()).forEach(function(entry) {
    var job = entry.object;
    if (String(job.event_type || '') !== 'FORM_SUITE') return;
    var notes = ttqsAuditNotes_(job.notes);
    if (Number(notes.auditLogVersion || 0) < Number(cfg.AUDIT_LOG_VERSION || 2)) return;
    var jobId = String(job.job_id || '');
    var status = String(job.status || '');
    var reconciliation = String(job.reconciliation_status || '');
    var acceptance = String(job.final_acceptance_status || '');
    if (acceptance === 'FINAL_ACCEPTED' && (status !== 'SUCCESS' || reconciliation !== 'MATCHED_EXACTLY_ONCE')) {
      issues.push({ jobId: jobId, code: 'INVALID_FINAL_ACCEPTANCE', status: status, reconciliation: reconciliation, acceptance: acceptance });
      return;
    }
    if (status !== 'SUCCESS') return;
    if (reconciliation === 'MATCHED_EXACTLY_ONCE') {
      if (acceptance !== 'FINAL_ACCEPTED') issues.push({ jobId: jobId, code: 'MATCHED_BUT_NOT_FINAL_ACCEPTED', acceptance: acceptance });
      return;
    }
    if (reconciliation) {
      issues.push({ jobId: jobId, code: 'RECONCILIATION_MISMATCH', reconciliation: reconciliation, acceptance: acceptance });
      return;
    }
    var finished = job.finished_at ? new Date(String(job.finished_at)).getTime() : 0;
    if (finished && isFinite(finished) && now - finished > graceMs) {
      issues.push({ jobId: jobId, code: 'RECONCILIATION_OVERDUE', finishedAt: job.finished_at, acceptance: acceptance });
    } else {
      pendingWithinGrace.push(jobId);
    }
  });
  return { status: issues.length ? 'FAIL' : 'PASS', issues: issues, pendingWithinGrace: pendingWithinGrace };
}

function ttqsReconciliationMarkEngineFailure_(err) {
  var message = String(err && err.message ? err.message : err).slice(0, 500);
  var updated = [];
  ttqsReadObjects_(ttqsLedgerSheet_()).forEach(function(entry) {
    var job = { rowNumber: entry.rowNumber, object: entry.object };
    if (String(job.object.event_type || '') !== 'FORM_SUITE') return;
    if (String(job.object.status || '') !== 'SUCCESS') return;
    if (String(job.object.reconciliation_status || '') === 'MATCHED_EXACTLY_ONCE') return;
    if (!ttqsJobUsesAppendOnlyAudit_(job)) return;
    ttqsLedgerPatch_(job, { final_acceptance_status: 'RECONCILIATION_EXCEPTION', final_accepted_at: '' });
    ttqsAttemptHistoryAppend_(job, 'RECONCILIATION_ENGINE_FAILED', {
      status: job.object.status,
      error_class: err && err.name ? err.name : 'Error',
      error_message: message,
      reconciliation_status: job.object.reconciliation_status || '',
      notes: { finalAcceptanceStatus: 'RECONCILIATION_EXCEPTION' }
    });
    updated.push(job.object.job_id);
  });
  return updated;
}

function ttqsS3ReconcileSourceFailureDetail_(sheetId, rowNumber, kind, err) {
  return {
    sheetId: Number(sheetId),
    observedRowNumber: Number(rowNumber),
    kind: String(kind || ''),
    status: 'MISMATCH_SOURCE_PROVENANCE',
    error: String(err && err.message ? err.message : err).slice(0, 500)
  };
}

function ttqsReconcileUnlocked_() {
  ttqsAssertTestOnly_();
  var ss = ttqsOpenCore_();
  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), null);
  if (!map || typeof map !== 'object' || !Object.keys(map).length) throw new Error('RECONCILE_RESPONSE_SHEET_MAP_REQUIRED');

  var details = [];
  Object.keys(map).forEach(function(sheetId) {
    var sheet = ttqsFindSheetById_(ss, Number(sheetId));
    if (!sheet) {
      details.push({ sheetId: Number(sheetId), kind: map[sheetId], status: 'MISMATCH_RESPONSE_SHEET_MISSING' });
      return;
    }
    for (var rowNumber = 2; rowNumber <= sheet.getLastRow(); rowNumber++) {
      try {
        details.push(ttqsReconcileRaw_(ttqsS3ResolveUnifiedRawBySheetRow_(Number(sheetId), rowNumber)));
      } catch (err) {
        details.push(ttqsS3ReconcileSourceFailureDetail_(Number(sheetId), rowNumber, map[sheetId], err));
      }
    }
  });

  var mismatches = details.filter(function(detail) { return detail.status !== 'MATCHED_EXACTLY_ONCE'; });
  var watchdog = ttqsReconciliationWatchdog_();
  return {
    matched: details.length - mismatches.length,
    mismatched: mismatches.length,
    observedRawResponses: details.length,
    status: mismatches.length === 0 && watchdog.status === 'PASS' ? 'PASS' : 'FAIL',
    details: details,
    watchdog: watchdog
  };
}

function ttqsReconcile() {
  try {
    return ttqsWithScriptLock_(ttqsReconcileUnlocked_);
  } catch (err) {
    try {
      ttqsWithScriptLock_(function() { return ttqsReconciliationMarkEngineFailure_(err); });
    } catch (logErr) {
      console.error('RECONCILIATION_FAILURE_LOGGING_FAILED', String(logErr && logErr.message ? logErr.message : logErr));
    }
    throw err;
  }
}
