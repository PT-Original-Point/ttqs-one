import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const internalSource = fs.readFileSync('apps-script/ConsultView.gs', 'utf8');
const externalSource = fs.readFileSync('external-viewer/Code.gs', 'utf8');

const internal = {};
vm.createContext(internal);
vm.runInContext(internalSource, internal);
const external = {};
vm.createContext(external);
vm.runInContext(externalSource, external);

const internalHtml = internal.ttqsRenderWebAppHtml_({
  view: 'INTERNAL',
  version: '0.6.5',
  dataClass: '示範資料（SAMPLE）',
  coveredIndicators: 1,
  gapIndicators: 18,
  formLaunchers: [{ label: '需求調查', status: '可填答', url: 'https://example.test/form' }],
  health: { state: '正常', total: 10, failed: 0 },
  modules: [{ name: '需求調查', state: '示範（SAMPLE）', note: '示範資料' }],
  indicators: [{ no: '1', stage: '規劃', title: '測試指標', evidenceCount: 1, status: '已有測試佐證' }]
});
// Use the canonical external snapshot model so this language contract follows the current
// product render contract instead of maintaining a second, stale partial fixture.
const externalHtml = external.ttqsExternalRender_(external.ttqsExternalSnapshotModel_());
const errorHtml = internal.ttqsWebErrorHtml_() + '\n' + external.ttqsExternalErrorHtml_();
const visibleHtml = internalHtml + '\n' + externalHtml + '\n' + errorHtml;
const bannedVisibleTerms = [
  'CourseMaster', 'PII Vault', 'Enrollment', 'Queue', 'Worker',
  'Reconciliation', 'Retry', 'Snapshot', 'REAL Start', 'TEST / SAMPLE'
];

test('both web entrypoints remain valid JavaScript', () => {
  new vm.Script(internalSource, { filename: 'ConsultView.gs' });
  new vm.Script(externalSource, { filename: 'external-viewer/Code.gs' });
});

test('rendered UI does not expose banned internal or untranslated terms', () => {
  for (const term of bannedVisibleTerms) assert.equal(visibleHtml.includes(term), false, `禁止裸露：${term}`);
});

test('formal environment markers use Chinese-first labels', () => {
  assert.match(internalHtml, /測試／示範資料（TEST／SAMPLE）/);
  assert.match(internalHtml, /正式資料寫入（REAL）/);
  assert.match(externalHtml, /測試／示範資料（TEST／SAMPLE）/);
});

test('snapshot wording is localized as 唯讀快照', () => {
  assert.match(internalHtml, /唯讀快照/);
  assert.match(externalHtml, /唯讀快照/);
});

test('friendly error pages do not expose internal error details', () => {
  assert.match(errorHtml, /目前無法載入/);
  assert.doesNotMatch(errorHtml, /SNAPSHOT_SCHEMA|SNAPSHOT_INDICATOR|error_message|last_error|stack|Exception/);
});

test('source error handlers never render err.message', () => {
  const internalErrorBody = internalSource.match(/function ttqsWebErrorHtml_\(\) \{([\s\S]*?)\n\}/)?.[1] || '';
  const externalErrorBody = externalSource.match(/function ttqsExternalErrorHtml_\(\) \{([\s\S]*?)\n\}/)?.[1] || '';
  assert.doesNotMatch(internalErrorBody, /err\.message|String\(err/);
  assert.doesNotMatch(externalErrorBody, /err\.message|String\(err/);
});
