import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const workflow = fs.readFileSync('.github/workflows/verify-external-r7-live.yml', 'utf8');

test('successful exhaustive live path creates per-marker evidence before 19 plus 129 traversal', () => {
  assert.match(workflow, /Persist auditable per-marker live homepage evidence/);
  assert.match(workflow, /scripts\/external-blackbox-classifier\.mjs/);
  assert.match(workflow, /--evidence-out \.r7-live-evidence\/BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(workflow, /BLACKBOX_MARKERS_PASS mode=R7_DRAFT003 markers=11\/11 safety=PASS/);
  assert.match(workflow, /G02_V10_MARKER_EVIDENCE_PASS markers=11\/11 safety=PASS total=PASS/);
  const markers = workflow.indexOf('- name: Persist auditable per-marker live homepage evidence');
  const exhaustive = workflow.indexOf('- name: Exhaustively probe 19 matrices, 129 FrozenArtifacts');
  assert.ok(markers >= 0 && exhaustive > markers);
});

test('workflow machine-validates expected actual PASS-FAIL evidence before continuing', () => {
  assert.match(workflow, /TTQS_BLACKBOX_MARKER_EVIDENCE_V1/);
  assert.match(workflow, /r\.markerEvidence\?\.length!==11/);
  assert.match(workflow, /x\.expected&&x\.actual===x\.expected&&x\.result==='PASS'/);
  assert.match(workflow, /x\.evidence\?\.matchType==='NORMALIZED_SUBSTRING'/);
  assert.match(workflow, /x\.evidence\.normalizedIndex>=0/);
  assert.match(workflow, /String\(x\.evidence\.excerpt\|\|'\'\)\.includes\(x\.expected\)/);
  assert.match(workflow, /r\.safetyEvidence\?\.expected!=='ABSENT'/);
  assert.match(workflow, /r\.derivation\?\.markerPassCount!==11/);
  assert.match(workflow, /r\.derivation\?\.totalPass!==true/);
});

test('same exhaustive artifact durably contains marker detail and downstream full-live evidence', () => {
  assert.match(workflow, /actions\/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a/);
  assert.match(workflow, /name: r7-external-test-live-evidence-\$\{\{ github\.run_id \}\}/);
  assert.match(workflow, /path: \.r7-live-evidence\//);
  assert.match(workflow, /retention-days: 30/);
  assert.match(workflow, /BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(workflow, /R7_LIVE_PROBE_OUTPUT\.txt/);
  assert.match(workflow, /marker_line:/);
  assert.match(workflow, /pass_line:/);
});

test('marker evidence workflow remains read-only toward provider and REAL PROD', () => {
  assert.doesNotMatch(workflow, /push-content|script\.deployments|CLASPRC_JSON_B64|environment:\s*PROD|REAL_WRITE|PROD_ENABLE/);
  assert.match(workflow, /scope: TEST\/SAMPLE\/CONTROL only; REAL\/PROD\/formal scoring\/official submission = 0/);
});
