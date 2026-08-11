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
  var required = Object.keys(cfg.SHEETS).map(function(k) { return cfg.SHEETS[k]; });
  var names = ss.getSheets().map(function(s) { return s.getName(); });
  required.forEach(function(name) { checks.push({ check: 'sheet:' + name, pass: names.indexOf(name) >= 0, actual: names.indexOf(name) >= 0 }); });
  var failed = checks.filter(function(c) { return !c.pass; });
  return { version: cfg.VERSION, status: failed.length ? 'FAIL' : 'PASS', checks: checks, failed: failed };
}
