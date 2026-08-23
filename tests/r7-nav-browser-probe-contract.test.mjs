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

test('R7 browser probe implements every human-specified a-g route check without threshold reduction', () => {
  for (const check of exactChecks) assert.ok(probe.includes(check), check);
  assert.ok(probe.includes('page.url()'));
  assert.ok(probe.includes('window.top === window.self'));
  assert.ok(probe.includes('iframe[src*="script.google.com"]'));
  assert.ok(probe.includes('指標 ${id}｜查看文件與證據'));
  assert.ok(probe.includes("getByText('開啟文件', { exact: true })"));
  assert.ok(probe.includes('拒絕連線|refused to connect'));
  assert.ok(probe.includes("width: 390"));
  assert.ok(probe.includes('horizontalOverflow'));
  assert.ok(probe.includes('canonicalOpenDocumentButtons'));
  assert.ok(probe.includes("matrixText.includes('TEST／SAMPLE／CONTROL')"));
});

test('R7 browser probe records actual DOM evidence for every route', () => {
  for (const marker of ['actualUrl','resolvedHref','domEvidence','cardDataIndicator','linkDataIndicator','hrefAttribute','resolvedHref','targetAttribute','linkOuterHTMLSha256','cardOuterHTMLSha256','firstChineseDocumentTitle','firstCanonicalOpenDocument']) assert.ok(probe.includes(marker),marker);
  assert.ok(probe.includes("if (cardDataIndicator !== String(id))"));
  assert.ok(probe.includes('if (row.href !== expectedUrl)'));
  assert.ok(probe.includes('if (row.resolvedHref !== expectedUrl)'));
  assert.ok(probe.includes("if (row.target !== '_top')"));
});

test('R7 browser probe never mistakes the top canonical page for a nested bad iframe', () => {
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
  assert.ok(probe.includes('R7-NAV-BLOCKER=OPEN; FA-08=FAIL; NAV-02=FAIL; T Gate=NOT PASS'));
});

test('browser workflow permanently publishes complete 19+19 rows before enforcing 38/38', () => {
  assert.ok(workflow.includes('TTQS_R7_NAV_ROUTE_EVIDENCE_V2'));
  assert.ok(workflow.includes('if: always()'));
  assert.ok(workflow.includes('r7-nav-desktop.json'));
  assert.ok(workflow.includes('r7-nav-mobile.json'));
  assert.ok(workflow.includes('VIEWPORT in desktop mobile'));
  assert.ok(workflow.includes("rows.length!==19"));
  assert.ok(workflow.includes('the next two Issue #39 comments contain desktop 19 rows and mobile 19 rows'));
  assert.ok(workflow.includes('Enforce exhaustive 38/38 browser gate after durable publication'));
  assert.ok(workflow.includes("r.checks!==38||r.passCount!==38||r.failCount!==0||r.result!=='PASS_MACHINE_BROWSER'"));
  assert.ok(workflow.includes('R7-NAV-BLOCKER=OPEN; FA-08=FAIL; NAV-02=FAIL; T Gate=NOT PASS'));
  assert.ok(workflow.includes('REAL/PROD/formal scoring/official submission = 0'));
  for (const check of exactChecks) assert.ok(workflow.includes(check), check);
});
