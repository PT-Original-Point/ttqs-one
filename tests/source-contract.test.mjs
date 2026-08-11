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
  ['TEST environment fixed', () => assert.match(all, /ENVIRONMENT: 'TEST'/)],
  ['real writes disabled', () => assert.match(all, /ENABLE_REAL_WRITES: false/)],
  ['pii vault disabled', () => assert.match(all, /PII_VAULT_READY: false/)],
  ['timezone fixed', () => assert.match(all, /TIME_ZONE: 'Asia\/Taipei'/)],
  ['TEST core id present', () => assert.match(all, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/)],
  ['consult id present', () => assert.match(all, /1U7mn98TzRN7Wnm7Yi7hOgtEi85Xyc9kcBUBbK9UYOAE/)],
  ['bootstrap entrypoint present', () => assert.match(all, /function ttqsBootstrapTest\(/)],
  ['real event required', () => assert.match(all, /REAL_SPREADSHEET_FORM_EVENT_REQUIRED/)],
  ['no FormResponse submit', () => assert.doesNotMatch(all, /FormResponse\s*\.\s*submit|\.submit\(\)/)],
  ['retry handler present', () => assert.match(all, /function ttqsRetryFailedJobs\(/)],
  ['reconcile handler present', () => assert.match(all, /function ttqsReconcile\(/)],
  ['consult refresh present', () => assert.match(all, /function ttqsRefreshConsultView\(/)],
  ['17-19 formal gate present', () => assert.match(all, /FORMAL_BLOCKED_NEEDS_REAL/)],
  ['partial failure injection present', () => assert.match(all, /TTQS_INJECTED_PARTIAL_FAILURE_AFTER_PARTY_ALIAS/)],
  ['recovered flag present', () => assert.match(all, /recovered: !!isRetry/)],
  ['ledger double dedupe source ref present', () => assert.match(all, /ttqsSurveyFindBySource_/)],
  ['party natural dedupe present', () => assert.match(all, /ttqsFindPartyByAlias_/)],
  ['max attempts enforced', () => assert.match(all, /MAX_ATTEMPTS_EXCEEDED/)],
  ['managed triggers cleanup present', () => assert.match(all, /ttqsRemoveManagedTriggers_/)],
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
