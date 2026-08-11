function ttqsExpectedSurveyTypeForKind_(kind) {
  var map = {
    NEEDS: 'NEEDS',
    REGISTRATION: 'REGISTRATION',
    REACTION: 'REACTION',
    FOLLOWUP30: '30_DAY_BEHAVIOR'
  };
  var value = map[String(kind)];
  if (!value) throw new Error('UNKNOWN_FORM_KIND_FOR_RECONCILE:' + kind);
  return value;
}

function ttqsReconcileRaw_(raw) {
  var cfg = ttqsConfig_();
  var idempotencyKey = 'TEST:' + raw.rawRef;
  var ledgerRows = ttqsFindRowsByValue_(ttqsLedgerSheet_(), 'idempotency_key', idempotencyKey);
  var detail = {
    rawRef: raw.rawRef,
    rawFingerprint: raw.rawFingerprint,
    formId: raw.formId,
    sheetId: raw.sheetId,
    observedRowNumber: raw.rowNumber,
    kind: raw.kind,
    idempotencyKey: idempotencyKey,
    ledgerCount: ledgerRows.length,
    surveyCount: 0,
    partyCount: 0,
    evidenceCount: 0,
    linkageErrors: []
  };

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
    if (String(survey.class_run_id) !== String(cfg.CLASS_RUN_ID)) detail.linkageErrors.push('SURVEY_CLASS_RUN');
    if (String(survey.party_alias_id) !== String(party.party_alias_id)) detail.linkageErrors.push('SURVEY_PARTY_LINK');
    if (String(survey.survey_type) !== ttqsExpectedSurveyTypeForKind_(raw.kind)) detail.linkageErrors.push('SURVEY_TYPE');
    if (String(survey.source_ref) !== String(raw.rawRef)) detail.linkageErrors.push('SURVEY_SOURCE_REF');
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
  ttqsUpdateObjectRow_(ttqsLedgerSheet_(), ledger.rowNumber, {
    reconciliation_date: ttqsDateOnly_(new Date()),
    reconciliation_status: detail.status
  });
  return detail;
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
      details.push(ttqsReconcileRaw_(ttqsRawSubmission_(Number(sheetId), rowNumber)));
    }
  });

  var mismatches = details.filter(function(detail) { return detail.status !== 'MATCHED_EXACTLY_ONCE'; });
  return {
    matched: details.length - mismatches.length,
    mismatched: mismatches.length,
    observedRawResponses: details.length,
    status: mismatches.length === 0 ? 'PASS' : 'FAIL',
    details: details
  };
}

function ttqsReconcile() {
  return ttqsWithScriptLock_(ttqsReconcileUnlocked_);
}
