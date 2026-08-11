function ttqsHealthRequiredHeaders_() {
  var cfg = ttqsConfig_();
  var required = {};
  required[cfg.SHEETS.INDICATORS] = ['indicator_no', 'pddro_stage', 'indicator_title'];
  required[cfg.SHEETS.CLASS_RUN] = ['class_run_id', 'environment', 'data_class', 'real_start_gate_status'];
  required[cfg.SHEETS.PARTY_ALIAS] = ['party_alias_id', 'party_type', 'alias_code', 'display_name_masked', 'pii_vault_ref', 'consent_status', 'consent_ref', 'retention_class', 'active_status', 'created_at', 'notes'];
  required[cfg.SHEETS.SURVEY] = ['response_id', 'class_run_id', 'party_alias_id', 'survey_type', 'response_date', 'question_set_version', 'score_total', 'score_max', 'free_text_redacted', 'followup_due_date', 'followup_completed_date', 'source_ref', 'ai_allowed', 'verification_status', 'notes'];
  required[cfg.SHEETS.EVIDENCE] = ['evidence_id', 'evidence_title', 'evidence_type', 'environment', 'data_class', 'source_object_type', 'source_object_id', 'drive_file_id', 'drive_url', 'document_version_id', 'class_run_id', 'ttqs_indicator_tags', 'pddro_stage', 'approval_status', 'approved_by', 'sha256', 'health_status', 'retrieval_tested_at', 'archive_status', 'notes'];
  required[cfg.SHEETS.LEDGER] = ['job_id', 'event_type', 'environment', 'object_type', 'object_id', 'idempotency_key', 'trigger_source', 'scheduled_at', 'started_at', 'finished_at', 'status', 'attempt_no', 'max_attempts', 'error_class', 'error_message', 'retry_at', 'reconciliation_date', 'reconciliation_status', 'operator', 'trace_id', 'notes'];
  return required;
}

function ttqsHealthCheck() {
  ttqsAssertTestOnly_();
  var cfg = ttqsConfig_();
  var ss = ttqsOpenCore_();
  var checks = [];
  checks.push({ check: 'environment', pass: cfg.ENVIRONMENT === 'TEST', actual: cfg.ENVIRONMENT });
  checks.push({ check: 'real_writes_disabled', pass: cfg.ENABLE_REAL_WRITES === false, actual: cfg.ENABLE_REAL_WRITES });
  checks.push({ check: 'pii_vault_disabled', pass: cfg.PII_VAULT_READY === false, actual: cfg.PII_VAULT_READY });
  checks.push({ check: 'time_zone', pass: ss.getSpreadsheetTimeZone() === cfg.TIME_ZONE, actual: ss.getSpreadsheetTimeZone() });
  checks.push({ check: 'core_spreadsheet_id', pass: ss.getId() === cfg.CORE_SPREADSHEET_ID, actual: ss.getId() });

  var names = ss.getSheets().map(function(sheet) { return sheet.getName(); });
  Object.keys(cfg.SHEETS).forEach(function(key) {
    var name = cfg.SHEETS[key];
    checks.push({ check: 'sheet:' + name, pass: names.indexOf(name) >= 0, actual: names.indexOf(name) >= 0 });
  });

  var headerContract = ttqsHealthRequiredHeaders_();
  Object.keys(headerContract).forEach(function(name) {
    var sheet = ss.getSheetByName(name);
    var missing = sheet ? ttqsMissingHeaders_(sheet, headerContract[name]) : headerContract[name];
    checks.push({ check: 'headers:' + name, pass: missing.length === 0, actual: missing.length ? missing.join(',') : 'PASS' });
  });

  var classSheet = ss.getSheetByName(cfg.SHEETS.CLASS_RUN);
  var classRows = classSheet ? ttqsFindRowsByValue_(classSheet, 'class_run_id', cfg.CLASS_RUN_ID) : [];
  checks.push({ check: 'sample_class_unique', pass: classRows.length === 1, actual: classRows.length });
  if (classRows.length === 1) {
    checks.push({ check: 'sample_class_environment', pass: String(classRows[0].object.environment) === 'TEST', actual: classRows[0].object.environment });
    checks.push({ check: 'sample_class_data_class', pass: String(classRows[0].object.data_class) === 'SAMPLE', actual: classRows[0].object.data_class });
    checks.push({ check: 'sample_class_real_gate', pass: String(classRows[0].object.real_start_gate_status) === 'NOT_APPLICABLE_SAMPLE', actual: classRows[0].object.real_start_gate_status });
  }

  try {
    var consult = SpreadsheetApp.openById(cfg.CONSULT_VIEW_SPREADSHEET_ID);
    checks.push({ check: 'consult_spreadsheet_id', pass: consult.getId() === cfg.CONSULT_VIEW_SPREADSHEET_ID, actual: consult.getId() });
    checks.push({ check: 'consult_time_zone', pass: consult.getSpreadsheetTimeZone() === cfg.TIME_ZONE, actual: consult.getSpreadsheetTimeZone() });
  } catch (err) {
    checks.push({ check: 'consult_spreadsheet_open', pass: false, actual: String(err.message || err) });
  }

  var mapRaw = PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP');
  if (mapRaw) {
    var map = ttqsParseJson_(mapRaw, null);
    checks.push({ check: 'response_sheet_map_json', pass: !!map && typeof map === 'object', actual: mapRaw });
    if (map && typeof map === 'object') {
      Object.keys(map).forEach(function(sheetId) {
        var kind = String(map[sheetId]);
        var sheet = ttqsFindSheetById_(ss, Number(sheetId));
        var expectedName = 'RUNTIME_' + kind + '_RESPONSES';
        checks.push({ check: 'response_sheet_map:' + kind, pass: !!sheet && sheet.getName() === expectedName && ttqsSheetMatchesFormKind_(sheet, kind), actual: sheet ? sheet.getName() : 'MISSING' });
      });
    }
  }

  var failed = checks.filter(function(check) { return !check.pass; });
  return { version: cfg.VERSION, status: failed.length ? 'FAIL' : 'PASS', checks: checks, failed: failed };
}
