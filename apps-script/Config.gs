var TTQS_CONFIG = Object.freeze({
  VERSION: '0.6.3',
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
  LOCK_WAIT_MS: 30000,
  FORM_RESPONSE_WAIT_MS: 10000,
  FORM_RESPONSE_POLL_MS: 500,
  SHEETS: Object.freeze({
    RULES: '01_RuleRegistry_\u898f\u5247\u4e3b\u6a94',
    INDICATORS: '02_TTQSIndicator_19\u6307\u6a19',
    CHECKPOINTS: '03_InternalCheckpoint_\u5167\u90e8\u6aa2\u67e5',
    ANNUAL_GOAL: '04_AnnualGoal_\u5e74\u5ea6\u76ee\u6a19',
    COURSE_MASTER: '05_CourseMaster_\u8ab2\u7a0b\u4e3b\u6a94',
    COURSE_VERSION: '06_CourseVersion_\u8ab2\u7a0b\u7248\u672c',
    CLASS_RUN: '07_ClassRun_\u73ed\u6b21',
    PARTY_ALIAS: '08_PartyAlias_\u4eba\u54e1\u4ee3\u78bc',
    ATTENDANCE: '09_AttendanceAssessment_\u51fa\u52e4\u8a55\u91cf',
    SURVEY: '10_SurveyResponse_\u554f\u5377\u8ffd\u8e64',
    DOCUMENT_MASTER: '11_DocumentMaster_\u6587\u4ef6\u4e3b\u6a94',
    DOCUMENT_VERSION: '12_DocumentVersion_\u6587\u4ef6\u7248\u672c',
    APPROVAL: '13_ApprovalEvent_\u6838\u51c6\u7d00\u9304',
    EVIDENCE: '14_EvidenceMaster_\u8b49\u64da\u7e3d\u7d22\u5f15',
    LEDGER: '15_EventJobLedger_\u5de5\u4f5c\u7e3d\u5e33'
  }),
  AUTO_CONSULT_SHEET: 'AUTO_19\u6307\u6a19\u8b49\u64da\u7d22\u5f15'
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
