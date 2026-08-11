function ttqsReconcile() {
  ttqsAssertTestOnly_();
  var rows = ttqsReadObjects_(ttqsLedgerSheet_());
  var matched = 0;
  var mismatched = 0;
  rows.forEach(function(entry) {
    if (entry.object.event_type !== 'FORM_SUITE' || entry.object.status !== 'SUCCESS') return;
    var notes = ttqsParseJson_(entry.object.notes, {});
    var rawRef = notes.rawRef;
    var aliasCode = notes.aliasCode;
    var surveyOk = !!ttqsSurveyFindBySource_(rawRef);
    var partyOk = !!ttqsFindPartyByAlias_(aliasCode);
    var status = surveyOk && partyOk ? 'MATCHED' : 'MISMATCH';
    if (status === 'MATCHED') matched++; else mismatched++;
    ttqsUpdateObjectRow_(ttqsLedgerSheet_(), entry.rowNumber, {
      reconciliation_date: ttqsDateOnly_(new Date()),
      reconciliation_status: status
    });
  });
  return { matched: matched, mismatched: mismatched, status: mismatched === 0 ? 'PASS' : 'FAIL' };
}
