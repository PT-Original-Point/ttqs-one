function ttqsPartySheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.PARTY_ALIAS);
}

function ttqsSurveySheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.SURVEY);
}

function ttqsEvidenceSheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.EVIDENCE);
}

function ttqsFindPartyByAlias_(aliasCode) {
  return ttqsFindUniqueRowByValue_(ttqsPartySheet_(), 'alias_code', aliasCode, 'DUPLICATE_PARTY_ALIAS');
}

function ttqsEnsurePartyAlias_(aliasCode) {
  aliasCode = ttqsRequireSampleAlias_(aliasCode);
  var existing = ttqsFindPartyByAlias_(aliasCode);
  if (existing) return existing.object.party_alias_id;
  var partyId = ttqsStableId_('SAMPLE-LRN-RUNTIME-', aliasCode, 10);
  ttqsAppendObject_(ttqsPartySheet_(), {
    party_alias_id: partyId,
    party_type: 'LEARNER',
    alias_code: aliasCode,
    display_name_masked: 'SAMPLE ' + aliasCode,
    pii_vault_ref: 'NONE_SAMPLE',
    consent_status: 'SAMPLE_ONLY_NOT_REAL_CONSENT',
    consent_ref: '',
    retention_class: 'SAMPLE',
    active_status: 'ACTIVE',
    created_at: ttqsNow_(),
    notes: 'Runtime SAMPLE alias; no real PII allowed'
  });
  return partyId;
}

function ttqsSurveyFindBySource_(sourceRef) {
  return ttqsFindUniqueRowByValue_(ttqsSurveySheet_(), 'source_ref', sourceRef, 'DUPLICATE_SURVEY_SOURCE_REF');
}

function ttqsRuntimeEvidenceSpec_(surveyType) {
  var map = {
    NEEDS: { tags: '7,11', stage: 'Design', title: 'TEST SAMPLE runtime needs response' },
    REGISTRATION: { tags: '12', stage: 'Do', title: 'TEST SAMPLE runtime registration response' },
    REACTION: { tags: '15,17', stage: 'Review,Outcome', title: 'TEST SAMPLE runtime reaction response' },
    '30_DAY_BEHAVIOR': { tags: '13,17,18', stage: 'Do,Outcome', title: 'TEST SAMPLE runtime 30-day behavior response' }
  };
  var spec = map[String(surveyType)];
  if (!spec) throw new Error('UNKNOWN_RUNTIME_EVIDENCE_SURVEY_TYPE:' + surveyType);
  return spec;
}

function ttqsRuntimeEvidenceNotes_(spec, responseId) {
  return JSON.stringify({
    evidence_origin: 'GOOGLE_FORM_RUNTIME',
    formal_admissibility: 'NOT_FORMAL',
    environment: 'TEST',
    data_class: 'SAMPLE',
    provider_form_id: String(spec.providerFormId || ''),
    provider_raw_fingerprint: String(spec.rawFingerprint || ''),
    source_ref: String(spec.sourceRef || ''),
    job_id: String(spec.jobId || ''),
    survey_response_id: String(responseId || '')
  });
}

function ttqsEnsureRuntimeEvidence_(spec, responseId) {
  var evidenceSpec = ttqsRuntimeEvidenceSpec_(spec.surveyType);
  var evidenceId = ttqsStableId_('EV-RUN-', spec.sourceRef, 16);
  var existing = ttqsFindUniqueRowByValue_(ttqsEvidenceSheet_(), 'evidence_id', evidenceId, 'DUPLICATE_RUNTIME_EVIDENCE_ID');
  if (!existing) {
    ttqsAppendObject_(ttqsEvidenceSheet_(), {
      evidence_id: evidenceId,
      evidence_title: evidenceSpec.title,
      evidence_type: 'STRUCTURED_DATA',
      environment: 'TEST',
      data_class: 'SAMPLE',
      source_object_type: 'SurveyResponse',
      source_object_id: responseId,
      drive_file_id: '',
      drive_url: '',
      document_version_id: '',
      class_run_id: ttqsConfig_().CLASS_RUN_ID,
      ttqs_indicator_tags: evidenceSpec.tags,
      pddro_stage: evidenceSpec.stage,
      approval_status: 'SAMPLE_SIMULATED',
      approved_by: '',
      sha256: spec.rawFingerprint || '',
      health_status: 'HEALTHY_SAMPLE_RUNTIME',
      retrieval_tested_at: ttqsNow_(),
      archive_status: 'NOT_APPLICABLE_SAMPLE',
      notes: ttqsRuntimeEvidenceNotes_(spec, responseId)
    });
  }
  return { evidenceId: evidenceId, duplicate: !!existing };
}

function ttqsEnsureRuntimeRecoveryEvidence_(job) {
  var evidenceId = ttqsStableId_('EV-RUN-REC-', job.object.job_id, 16);
  var existing = ttqsFindUniqueRowByValue_(ttqsEvidenceSheet_(), 'evidence_id', evidenceId, 'DUPLICATE_RUNTIME_RECOVERY_EVIDENCE_ID');
  if (!existing) {
    var notes = ttqsParseJson_(job.object.notes, {});
    ttqsAppendObject_(ttqsEvidenceSheet_(), {
      evidence_id: evidenceId,
      evidence_title: 'TEST SAMPLE runtime automatic retry recovery',
      evidence_type: 'SYSTEM_EVENT',
      environment: 'TEST',
      data_class: 'SAMPLE',
      source_object_type: 'EventJobLedger',
      source_object_id: job.object.job_id,
      drive_file_id: '',
      drive_url: '',
      document_version_id: '',
      class_run_id: ttqsConfig_().CLASS_RUN_ID,
      ttqs_indicator_tags: '16',
      pddro_stage: 'Review',
      approval_status: 'SAMPLE_SIMULATED',
      approved_by: '',
      sha256: notes.rawFingerprint || '',
      health_status: 'HEALTHY_SAMPLE_RUNTIME',
      retrieval_tested_at: ttqsNow_(),
      archive_status: 'NOT_APPLICABLE_SAMPLE',
      notes: JSON.stringify({
        evidence_origin: 'TIME_DRIVEN_RETRY_RECOVERY',
        formal_admissibility: 'NOT_FORMAL',
        environment: 'TEST',
        data_class: 'SAMPLE',
        job_id: job.object.job_id,
        trace_id: job.object.trace_id,
        source_ref: notes.rawRef || '',
        provider_form_id: notes.formId || '',
        provider_raw_fingerprint: notes.rawFingerprint || ''
      })
    });
  }
  return { evidenceId: evidenceId, duplicate: !!existing };
}

function ttqsWriteSurvey_(spec) {
  var existing = ttqsSurveyFindBySource_(spec.sourceRef);
  var responseId;
  if (existing) {
    responseId = existing.object.response_id;
  } else {
    responseId = ttqsStableId_('S-RUN-SUR-', spec.sourceRef, 14);
    ttqsAppendObject_(ttqsSurveySheet_(), {
      response_id: responseId,
      class_run_id: ttqsConfig_().CLASS_RUN_ID,
      party_alias_id: spec.partyAliasId,
      survey_type: spec.surveyType,
      response_date: ttqsDateOnly_(new Date()),
      question_set_version: spec.questionSetVersion,
      score_total: spec.scoreTotal,
      score_max: spec.scoreMax,
      free_text_redacted: ttqsRedactFreeText_(spec.freeText),
      followup_due_date: spec.followupDueDate || '',
      followup_completed_date: spec.followupCompletedDate || '',
      source_ref: spec.sourceRef,
      ai_allowed: 'YES_SAMPLE_NO_PII',
      verification_status: 'SAMPLE_RUNTIME_CAPTURED',
      notes: JSON.stringify({
        environment: 'TEST',
        data_class: 'SAMPLE',
        formal_admissibility: 'NOT_FORMAL',
        job_id: String(spec.jobId || ''),
        provider_form_id: String(spec.providerFormId || ''),
        provider_raw_fingerprint: String(spec.rawFingerprint || '')
      })
    });
  }
  var evidence = ttqsEnsureRuntimeEvidence_(spec, responseId);
  return { duplicate: !!existing, responseId: responseId, evidenceId: evidence.evidenceId };
}
