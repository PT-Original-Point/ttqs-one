function ttqsPartySheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.PARTY_ALIAS);
}

function ttqsSurveySheet_() {
  return ttqsGetSheet_(ttqsConfig_().SHEETS.SURVEY);
}

function ttqsFindPartyByAlias_(aliasCode) {
  return ttqsFindRowByValue_(ttqsPartySheet_(), 'alias_code', aliasCode);
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
  return ttqsFindRowByValue_(ttqsSurveySheet_(), 'source_ref', sourceRef);
}

function ttqsWriteSurvey_(spec) {
  var existing = ttqsSurveyFindBySource_(spec.sourceRef);
  if (existing) return { duplicate: true, responseId: existing.object.response_id };
  var responseId = ttqsStableId_('S-RUN-SUR-', spec.sourceRef, 14);
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
    notes: 'Runtime TEST SAMPLE; not formal REAL evidence'
  });
  return { duplicate: false, responseId: responseId };
}
