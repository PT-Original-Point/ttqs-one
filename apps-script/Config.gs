var TTQS_CONFIG = Object.freeze({
  VERSION: '0.6.5',
  AUDIT_LOG_VERSION: 2,
  ENVIRONMENT: 'TEST',
  TIME_ZONE: 'Asia/Taipei',
  CORE_SPREADSHEET_ID: '1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is',
  CONSULT_VIEW_SPREADSHEET_ID: '1U7mn98TzRN7Wnm7Yi7hOgtEi85Xyc9kcBUBbK9UYOAE',
  CLASS_RUN_ID: 'SAMPLE-CLASS-001',
  ENABLE_REAL_WRITES: false,
  PII_VAULT_READY: false,
  MAX_ATTEMPTS: 3,
  RETRY_MINUTES: 1,
  RUNNING_LEASE_MINUTES: 5,
  RECONCILIATION_GRACE_MINUTES: 70,
  LOCK_WAIT_MS: 30000,
  FORM_RESPONSE_WAIT_MS: 10000,
  FORM_RESPONSE_POLL_MS: 500,
  SHEETS: Object.freeze({
    RULES: '01_RuleRegistry_規則主檔',
    INDICATORS: '02_TTQSIndicator_19指標',
    CHECKPOINTS: '03_InternalCheckpoint_內部檢查',
    ANNUAL_GOAL: '04_AnnualGoal_年度目標',
    COURSE_MASTER: '05_CourseMaster_課程主檔',
    COURSE_VERSION: '06_CourseVersion_課程版本',
    CLASS_RUN: '07_ClassRun_班次',
    PARTY_ALIAS: '08_PartyAlias_人員代碼',
    ATTENDANCE: '09_AttendanceAssessment_出勤評量',
    SURVEY: '10_SurveyResponse_問卷追蹤',
    DOCUMENT_MASTER: '11_DocumentMaster_文件主檔',
    DOCUMENT_VERSION: '12_DocumentVersion_文件版本',
    APPROVAL: '13_ApprovalEvent_核准紀錄',
    EVIDENCE: '14_EvidenceMaster_證據總索引',
    LEDGER: '15_EventJobLedger_工作總帳',
    ATTEMPT_HISTORY: '16_AttemptHistory_嘗試歷史'
  }),
  AUTO_CONSULT_SHEET: 'AUTO_19指標證據索引'
});

function ttqsConfig_() {
  return TTQS_CONFIG;
}

function ttqsAssertTestOnly_() {
  var cfg = ttqsConfig_();
  if (cfg.ENVIRONMENT !== 'TEST') throw new Error('TEST_ONLY_ENVIRONMENT_REQUIRED');
  if (cfg.ENABLE_REAL_WRITES !== false) throw new Error('REAL_WRITES_MUST_REMAIN_DISABLED');
  if (cfg.PII_VAULT_READY !== false) throw new Error('PII_VAULT_MUST_REMAIN_DISABLED');
  return true;
}
