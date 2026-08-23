import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const probe = fs.readFileSync('scripts/r7-nav-browser-probe.mjs', 'utf8');
const workflow = fs.readFileSync('.github/workflows/verify-r7-nav-browser.yml', 'utf8');

const exactChecks = [
  'a_topLevelCanonicalUrl',
  'b_windowTopEqualsSelf',
  'c_scriptGoogleIframeCountZero',
  'd_chineseHeadingPresent',
  'e_chineseDocumentCardAndOpenButton',
  'f_refusedToConnectAbsent',
  'g_mobile390NoHorizontalOverflow'
];

test('R7 browser probe implements every human-specified a-g route check', () => {
  for (const check of exactChecks) assert.ok(probe.includes(check), check);
  assert.ok(probe.includes('page.url()'));
  assert.ok(probe.includes('window.top === window.self'));
  assert.ok(probe.includes('iframe[src*="script.google.com"]'));
  assert.ok(probe.includes('指標 ${id}｜查看文件與證據'));
  assert.ok(probe.includes("getByText('開啟文件', { exact: true })"));
  assert.ok(probe.includes('拒絕連線|refused to connect'));
  assert.ok(probe.includes("width: 390"));
  assert.ok(probe.includes('horizontalOverflow'));
});

test('R7 browser probe never mistakes the top canonical frame itself for a nested bad iframe', () => {
  assert.ok(probe.includes('iframe[src*="script.google.com"]'));
  assert.ok(!probe.includes('forbiddenExecFrame'));
  assert.ok(!probe.includes('page.frames().map(frame => frame.url()).filter(url => forbiddenExecFrame.test(url))'));
});

test('R7 browser probe records all 38 rows before failing the aggregate gate', () => {
  assert.ok(probe.includes('evidence.push(row)'));
  assert.ok(probe.includes("result: 'FAIL'"));
  assert.ok(probe.includes('passCount'));
  assert.ok(probe.includes("throw new Error(`R7_NAV_BROWSER_FAIL:${passCount}/38`)"));
  assert.ok(probe.includes("schema: 'TTQS_R7_NAV_ROUTE_EVIDENCE_V2'"));
});

test('browser workflow permanently publishes the complete JSON and preserves human gate failure', () => {
  assert.ok(workflow.includes('TTQS_R7_NAV_ROUTE_EVIDENCE_V2'));
  assert.ok(workflow.includes('cat r7-nav-browser-evidence.json'));
  assert.ok(workflow.includes('complete 38-row evidence payload'));
  assert.ok(workflow.includes('GAP remains BLOCKER; FA-08=FAIL; NAV-02=FAIL; T Gate=NOT PASS'));
  assert.ok(workflow.includes("r.evidence.length!==38"));
  for (const check of exactChecks) assert.ok(workflow.includes(check), check);
});
