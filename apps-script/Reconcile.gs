function ttqsReconcileUnlocked_() {
  ttqsAssertTestOnly_();
  var rows = ttqsReadObjects_(ttqsLedgerSheet_());
  var matched = 0;
  var mismatched = 0;
  var details = [];
  rows.forEach(function(entry) {
    if (entry.object.event_type !== 'FORM_SUITE' || entry.object.status !== 'SUCCESS') return;
    var notes = ttqsParseJson_(entry.object.notes, {});
    var rawRef = notes.rawRef;
    var aliasCode = notes.aliasCode;
    var evidenceId = notes.evidenceId;
    var surveyCount = rawRef ? ttqsCountRowsByValue_(ttqsSurveySheet_(), 'source_ref', rawRef) : 0;
    var partyCount = aliasCode ? ttqsCountRowsByValue_(ttqsPartySheet_(), 'alias_code', aliasCode) : 0;
    var evidenceCount = evidenceId ? ttqsCountRowsByValue_(ttqsEvidenceSheet_(), 'evidence_id', evidenceId) : 0;
    var status = surveyCount === 1 && partyCount === 1 && evidenceCount === 1 ? 'MATCHED' : 'MISMATCH_SURVEY_' + surveyCount + '_PARTY_' + partyCount + '_EVIDENCE_' + evidenceCount;
    if (status === 'MATCHED') {
      matched++;
    } else {
      mismatched++;
      details.push({ jobId: entry.object.job_id, surveyCount: surveyCount, partyCount: partyCount, evidenceCount: evidenceCount, status: status });
    }
    ttqsUpdateObjectRow_(ttqsLedgerSheet_(), entry.rowNumber, {
      reconciliation_date: ttqsDateOnly_(new Date()),
      reconciliation_status: status
    });
  });
  return { matched: matched, mismatched: mismatched, status: mismatched === 0 ? 'PASS' : 'FAIL', details: details };
}

function ttqsReconcile() {
  return ttqsWithScriptLock_(ttqsReconcileUnlocked_);
}
