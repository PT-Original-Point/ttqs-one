import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const dir = 'apps-script';
const files = fs.readdirSync(dir).filter((n) => n.endsWith('.gs')).sort();
const all = files.map((n) => fs.readFileSync(path.join(dir, n), 'utf8')).join('\n');
const ledgerSource = fs.readFileSync(path.join(dir, 'Ledger.gs'), 'utf8');
const manifest = JSON.parse(fs.readFileSync('apps-script/appsscript.json', 'utf8'));

const checks = [
  ['13 gs sources', () => assert.equal(files.length, 13)],
  ['version 0.6.5', () => assert.match(all, /VERSION: '0\.6\.5'/)],
  ['audit log version 2', () => assert.match(all, /AUDIT_LOG_VERSION: 2/)],
  ['TEST environment fixed', () => assert.match(all, /ENVIRONMENT: 'TEST'/)],
  ['real writes disabled', () => assert.match(all, /ENABLE_REAL_WRITES: false/)],
  ['pii vault disabled', () => assert.match(all, /PII_VAULT_READY: false/)],
  ['timezone fixed', () => assert.match(all, /TIME_ZONE: 'Asia\/Taipei'/)],
  ['TEST core id present', () => assert.match(all, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/)],
  ['consult id present', () => assert.match(all, /1U7mn98TzRN7Wnm7Yi7hOgtEi85Xyc9kcBUBbK9UYOAE/)],
  ['script lock present', () => assert.match(all, /LockService\.getScriptLock\(\)/)],
  ['lock timeout fail closed', () => assert.match(all, /TTQS_SCRIPT_LOCK_TIMEOUT/)],
  ['retry worker uses lock wrapper', () => assert.match(all, /function ttqsRetryFailedJobs\(\)[\s\S]*ttqsWithScriptLock_\(ttqsRetryFailedJobsUnlocked_\)/)],
  ['reconcile uses lock wrapper', () => assert.match(all, /function ttqsReconcile\(\)[\s\S]*ttqsWithScriptLock_\(ttqsReconcileUnlocked_\)/)],
  ['consult refresh uses lock wrapper', () => assert.match(all, /function ttqsRefreshConsultView\(\)[\s\S]*ttqsWithScriptLock_\(ttqsRefreshConsultViewUnlocked_\)/)],
  ['bounded stale RUNNING lease present', () => assert.match(all, /RUNNING_LEASE_MINUTES/)],
  ['stale RUNNING takeover present', () => assert.match(all, /STALE_RUNNING_TAKEOVER/)],
  ['immutable event id header present', () => assert.match(all, /TTQS_EVENT_ID/)],
  ['raw ref uses persisted event id', () => assert.match(all, /'FORM_SUITE:' \+ formId \+ ':' \+ eventId/)],
  ['raw ref retry resolver present', () => assert.match(all, /ttqsFindRawSubmissionByRef_/)],
  ['reconcile raw trust root present', () => assert.match(all, /observedRawResponses/)],
  ['reconcile detects missing event id', () => assert.match(all, /MISMATCH_EVENT_ID_MISSING/)],
  ['reconcile detects missed trigger', () => assert.match(all, /MISMATCH_TRIGGER_MISSED/)],
  ['reconcile exact cross-link status', () => assert.match(all, /MATCHED_EXACTLY_ONCE/)],
  ['bootstrap journal before side effects', () => assert.match(all, /ttqsLedgerStage_\(job, 'ENSURE_FORMS'\)/)],
  ['bootstrap failure ledger present', () => assert.match(all, /ttqsLedgerFail_\(job, err\)/)],
  ['bounded response sheet polling', () => assert.match(all, /FORM_RESPONSE_SHEET_NOT_CREATED_WITHIN_TIMEOUT/)],
  ['partial form recovery present', () => assert.match(all, /recoveredPartialState/)],
  ['orphan sheet state fails closed', () => assert.match(all, /FORM_ORPHAN_SHEET_STATE_REQUIRES_REPAIR/)],
  ['form destination recovery reads provider state', () => assert.match(all, /getDestinationId\(\)/)],
  ['form publication readback present', () => assert.match(all, /isPublished\(\)/)],
  ['real event required', () => assert.match(all, /REAL_SPREADSHEET_FORM_EVENT_REQUIRED/)],
  ['no FormResponse submit', () => assert.doesNotMatch(all, /FormResponse\s*\.\s*submit|\.submit\(\)/)],
  ['retry handler present', () => assert.match(all, /function ttqsRetryFailedJobs\(/)],
  ['retry provenance updates trigger source', () => assert.match(all, /'TIME_RETRY'/)],
  ['P0 provider audit alias contract present', () => assert.match(all, /S-P0AUDIT-RUNTIME/)],
  ['P0 provider contract self-heal hook present', () => assert.match(all, /ttqsMaintainP0AuditRegistrationProviderContract_/)],
  ['runtime evidence registration present', () => assert.match(all, /function ttqsEnsureRuntimeEvidence_\(/)],
  ['recovery evidence registration present', () => assert.match(all, /function ttqsEnsureRuntimeRecoveryEvidence_\(/)],
  ['runtime evidence provider linkage present', () => assert.match(all, /evidence_origin: 'GOOGLE_FORM_RUNTIME'/)],
  ['runtime evidence formal inadmissibility present', () => assert.match(all, /formal_admissibility: 'NOT_FORMAL'/)],
  ['indicator 16 recovery evidence', () => assert.match(all, /ttqs_indicator_tags: '16'/)],
  ['17-19 formal gate present', () => assert.match(all, /FORMAL_BLOCKED_NEEDS_REAL/)],
  ['health required headers present', () => assert.match(all, /ttqsHealthRequiredHeaders_/)],
  ['health FULL authorization state present', () => assert.match(all, /full_authorization/)],
  ['health sample class uniqueness present', () => assert.match(all, /sample_class_unique/)],
  ['health consult timezone present', () => assert.match(all, /consult_time_zone/)],
  ['health response map verification present', () => assert.match(all, /response_sheet_map:/)],
  ['managed trigger source ID verification present', () => assert.match(all, /MANAGED_TRIGGER_SOURCE_ID_INVALID/)],
  ['managed trigger event type verification present', () => assert.match(all, /MANAGED_TRIGGER_EVENT_TYPE_INVALID/)],
  ['trigger install repeats FULL auth barrier', () => assert.match(all, /function ttqsInstallManagedTriggers_\(\)[\s\S]*requireAllScopes/)],
  ['append-only AttemptHistory sheet contract present', () => assert.match(all, /16_AttemptHistory_嘗試歷史/)],
  ['immutable AttemptHistory update guard present', () => assert.match(all, /ATTEMPT_HISTORY_IMMUTABLE_UPDATE_FORBIDDEN/)],
  ['hash-chained audit records present', () => assert.match(all, /previous_event_hash[\s\S]*record_hash/)],
  ['retry start JobLedger patch preserves prior error fields', () => {
    const match = ledgerSource.match(/function ttqsLedgerStart_\(job, isRetry\) \{([\s\S]*?)\n\}\n\nfunction ttqsLedgerRunningLeaseExpired_/);
    assert.ok(match, 'ttqsLedgerStart_ function body must be isolatable');
    const patchMatch = match[1].match(/var patch = \{([\s\S]*?)\n  \};/);
    assert.ok(patchMatch, 'ttqsLedgerStart_ JobLedger patch must exist');
    assert.doesNotMatch(patchMatch[1], /error_class|error_message/);
  }],
  ['final acceptance gate present', () => assert.match(all, /FINAL_ACCEPTED/)],
  ['reconciliation watchdog present', () => assert.match(all, /function ttqsReconciliationWatchdog_\(/)],
  ['health validates audit hash chain', () => assert.match(all, /attempt_history_hash_chain/)],
  ['health validates reconciliation watchdog', () => assert.match(all, /reconciliation_watchdog/)],
  ['no DriveApp usage', () => assert.doesNotMatch(all, /DriveApp/)],
  ['no UrlFetchApp usage', () => assert.doesNotMatch(all, /UrlFetchApp/)],
  ['no GmailApp usage', () => assert.doesNotMatch(all, /GmailApp/)],
  ['manifest timezone Asia Taipei', () => assert.equal(manifest.timeZone, 'Asia/Taipei')],
  ['manifest V8 runtime', () => assert.equal(manifest.runtimeVersion, 'V8')],
  ['manifest no executionApi', () => assert.equal(Object.hasOwn(manifest, 'executionApi'), false)],
  ['manifest no broad drive scope', () => assert.equal(manifest.oauthScopes.some((s) => s === 'https://www.googleapis.com/auth/drive'), false)],
  ['manifest exactly four least-privilege scopes', () => assert.equal(manifest.oauthScopes.length, 4)],
  ['forms scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/forms'))],
  ['spreadsheets scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/spreadsheets'))],
  ['trigger scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/script.scriptapp'))],
  ['per-file Drive scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/drive.file'))]
];
for (const [name, fn] of checks) test(name, fn);
