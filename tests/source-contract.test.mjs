import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const dir = 'apps-script';
const files = fs.readdirSync(dir).filter((n) => n.endsWith('.gs')).sort();
const all = files.map((n) => fs.readFileSync(path.join(dir, n), 'utf8')).join('\n');
const manifest = JSON.parse(fs.readFileSync('apps-script/appsscript.json', 'utf8'));

const checks = [
  ['13 gs sources', () => assert.equal(files.length, 13)],
  ['version 0.6.2', () => assert.match(all, /VERSION: '0\.6\.2'/)],
  ['TEST environment fixed', () => assert.match(all, /ENVIRONMENT: 'TEST'/)],
  ['real writes disabled', () => assert.match(all, /ENABLE_REAL_WRITES: false/)],
  ['pii vault disabled', () => assert.match(all, /PII_VAULT_READY: false/)],
  ['timezone fixed', () => assert.match(all, /TIME_ZONE: 'Asia\/Taipei'/)],
  ['TEST core id present', () => assert.match(all, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/)],
  ['consult id present', () => assert.match(all, /1U7mn98TzRN7Wnm7Yi7hOgtEi85Xyc9kcBUBbK9UYOAE/)],
  ['script lock present', () => assert.match(all, /LockService\.getScriptLock\(\)/)],
  ['lock timeout fail closed', () => assert.match(all, /TTQS_SCRIPT_LOCK_TIMEOUT/)],
  ['reconcile uses lock wrapper', () => assert.match(all, /function ttqsReconcile\(\)[\s\S]*ttqsWithScriptLock_\(ttqsReconcileUnlocked_\)/)],
  ['consult refresh uses lock wrapper', () => assert.match(all, /function ttqsRefreshConsultView\(\)[\s\S]*ttqsWithScriptLock_\(ttqsRefreshConsultViewUnlocked_\)/)],
  ['bootstrap journal before side effects', () => assert.match(all, /ttqsLedgerStage_\(job, 'ENSURE_FORMS'\)/)],
  ['bootstrap failure ledger present', () => assert.match(all, /ttqsLedgerFail_\(job, err\)/)],
  ['bounded response sheet polling', () => assert.match(all, /FORM_RESPONSE_SHEET_NOT_CREATED_WITHIN_TIMEOUT/)],
  ['partial form recovery present', () => assert.match(all, /recoveredPartialState/)],
  ['orphan sheet state fails closed', () => assert.match(all, /FORM_ORPHAN_SHEET_STATE_REQUIRES_REPAIR/)],
  ['form destination recovery reads provider state', () => assert.match(all, /getDestinationId\(\)/)],
  ['real event required', () => assert.match(all, /REAL_SPREADSHEET_FORM_EVENT_REQUIRED/)],
  ['no FormResponse submit', () => assert.doesNotMatch(all, /FormResponse\s*\.\s*submit|\.submit\(\)/)],
  ['retry handler present', () => assert.match(all, /function ttqsRetryFailedJobs\(/)],
  ['retry provenance updates trigger source', () => assert.match(all, /'TIME_RETRY'/)],
  ['reconcile exact counts', () => assert.match(all, /surveyCount === 1 && partyCount === 1 && evidenceCount === 1/)],
  ['runtime evidence registration present', () => assert.match(all, /function ttqsEnsureRuntimeEvidence_\(/)],
  ['recovery evidence registration present', () => assert.match(all, /function ttqsEnsureRuntimeRecoveryEvidence_\(/)],
  ['indicator 16 recovery evidence', () => assert.match(all, /ttqs_indicator_tags: '16'/)],
  ['17-19 formal gate present', () => assert.match(all, /FORMAL_BLOCKED_NEEDS_REAL/)],
  ['health required headers present', () => assert.match(all, /ttqsHealthRequiredHeaders_/)],
  ['health sample class uniqueness present', () => assert.match(all, /sample_class_unique/)],
  ['health consult timezone present', () => assert.match(all, /consult_time_zone/)],
  ['health response map verification present', () => assert.match(all, /response_sheet_map:/)],
  ['no DriveApp usage', () => assert.doesNotMatch(all, /DriveApp/)],
  ['no UrlFetchApp usage', () => assert.doesNotMatch(all, /UrlFetchApp/)],
  ['no GmailApp usage', () => assert.doesNotMatch(all, /GmailApp/)],
  ['manifest timezone Asia Taipei', () => assert.equal(manifest.timeZone, 'Asia/Taipei')],
  ['manifest V8 runtime', () => assert.equal(manifest.runtimeVersion, 'V8')],
  ['manifest no executionApi', () => assert.equal(Object.hasOwn(manifest, 'executionApi'), false)],
  ['manifest no broad drive scope', () => assert.equal(manifest.oauthScopes.some((s) => s === 'https://www.googleapis.com/auth/drive'), false)],
  ['manifest only three scopes', () => assert.equal(manifest.oauthScopes.length, 3)],
  ['forms scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/forms'))],
  ['spreadsheets scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/spreadsheets'))],
  ['trigger scope present', () => assert.ok(manifest.oauthScopes.includes('https://www.googleapis.com/auth/script.scriptapp'))]
];
for (const [name, fn] of checks) test(name, fn);
