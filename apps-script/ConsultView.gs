function ttqsIndicatorEvidenceMap_() {
  var evidenceRows = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.EVIDENCE));
  var map = {};
  for (var i = 1; i <= 19; i++) map[String(i)] = [];
  evidenceRows.forEach(function(entry) {
    var tags = String(entry.object.ttqs_indicator_tags || '').split(',').map(function(v) { return v.trim(); }).filter(Boolean);
    tags.forEach(function(tag) {
      if (map[tag]) map[tag].push(entry.object);
    });
  });
  return map;
}

function ttqsRefreshConsultView() {
  ttqsAssertTestOnly_();
  var indicators = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.INDICATORS));
  var evidenceMap = ttqsIndicatorEvidenceMap_();
  var consult = SpreadsheetApp.openById(ttqsConfig_().CONSULT_VIEW_SPREADSHEET_ID);
  var sheet = consult.getSheetByName(ttqsConfig_().AUTO_CONSULT_SHEET) || consult.insertSheet(ttqsConfig_().AUTO_CONSULT_SHEET);
  sheet.clearContents();
  var header = ['indicator_no', 'pddro_stage', 'indicator_title', 'evidence_ids', 'evidence_count', 'data_classes', 'health_summary', 'formal_status', 'refreshed_at', 'notes'];
  var out = [header];
  indicators.forEach(function(entry) {
    var no = String(entry.object.indicator_no);
    var evidence = evidenceMap[no] || [];
    var ids = evidence.map(function(e) { return e.evidence_id; }).filter(Boolean);
    var dataClasses = ttqsUnique_(evidence.map(function(e) { return e.data_class; }).filter(Boolean));
    var health = ttqsUnique_(evidence.map(function(e) { return e.health_status; }).filter(Boolean));
    var formalStatus = Number(no) >= 17 ? 'FORMAL_BLOCKED_NEEDS_REAL' : (evidence.length ? 'WORKING_EVIDENCE_AVAILABLE' : 'GAP');
    out.push([
      no,
      entry.object.pddro_stage,
      entry.object.indicator_title,
      ids.join(', '),
      ids.length,
      dataClasses.join(', '),
      health.join(', '),
      formalStatus,
      ttqsNow_(),
      'Auto index only; SAMPLE/CONTROL evidence is not a formal TTQS score.'
    ]);
  });
  sheet.getRange(1, 1, out.length, header.length).setValues(out);
  sheet.setFrozenRows(1);
  return { rows: out.length - 1, sheet: ttqsConfig_().AUTO_CONSULT_SHEET };
}
