import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const workflow = fs.readFileSync('.github/workflows/verify-external-r7-live.yml', 'utf8');

test('successful exhaustive live path enforces R2 19 required markers before 19 plus 129 traversal', () => {
  assert.match(workflow, /Persist auditable R2 19-marker live homepage evidence/);
  assert.match(workflow, /scripts\/external-blackbox-classifier\.mjs/);
  assert.match(workflow, /--evidence-out \.r7-live-evidence\/BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(workflow, /BLACKBOX_MARKERS_PASS contract=R2_G02_19_REQUIRED markers=19\/19 safety=PASS mode=R7_DRAFT003/);
  assert.match(workflow, /G02_V10_R2_MARKER_EVIDENCE_PASS contract=R2_G02_19_REQUIRED markers=19\/19 safety=PASS total=PASS/);
  const markers = workflow.indexOf('- name: Persist auditable R2 19-marker live homepage evidence');
  const exhaustive = workflow.indexOf('- name: Exhaustively probe 19 matrices, 129 FrozenArtifacts');
  assert.ok(markers >= 0 && exhaustive > markers);
});

test('workflow machine-validates R2 IDs expected actual PASS-FAIL evidence and safety markers', () => {
  assert.match(workflow, /TTQS_BLACKBOX_MARKER_EVIDENCE_V2/);
  assert.match(workflow, /R2_G02_19_REQUIRED/);
  assert.match(workflow, /r\.markerEvidence\?\.length!==19/);
  assert.match(workflow, /G02-M01/);
  assert.match(workflow, /G02-M17/);
  assert.match(workflow, /G02-M18/);
  assert.match(workflow, /G02-M19/);
  assert.match(workflow, /x\.expected&&x\.actual===x\.expected&&x\.result==='PASS'/);
  assert.match(workflow, /x\.evidence\?\.matchType==='NORMALIZED_SUBSTRING'/);
  assert.match(workflow, /x\.evidence\.normalizedIndex>=0/);
  assert.match(workflow, /String\(x\.evidence\.excerpt\|\|'\'\)\.includes\(x\.expected\)/);
  assert.match(workflow, /r\.safetyEvidence\?\.expected!=='ABSENT'/);
  assert.match(workflow, /r\.derivation\?\.markerPassCount!==19/);
  assert.match(workflow, /r\.derivation\?\.requiredContractPass!==true/);
  assert.match(workflow, /r\.derivation\?\.totalPass!==true/);
});

test('Issue 39 is the durable exact-byte marker evidence location and artifact is only a secondary copy', () => {
  assert.match(workflow, /TTQS_R2_G02_MARKER_EVIDENCE_V1/);
  assert.match(workflow, /G-02／V-10｜R2 逐 marker 永久證據/);
  assert.match(workflow, /marker_evidence_sha256/);
  assert.match(workflow, /durable_byte_location/);
  assert.match(workflow, /cat \.r7-live-evidence\/BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(workflow, /Derived summaries（不得取代上方逐 marker 明細）/);
  assert.match(workflow, /artifact_secondary_copy/);
  assert.match(workflow, /artifact_digest/);
  assert.match(workflow, /gh issue comment/);
  assert.doesNotMatch(workflow, /- marker_line:/);
});

test('same exhaustive artifact remains a secondary human-download copy of marker and downstream live evidence', () => {
  assert.match(workflow, /actions\/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a/);
  assert.match(workflow, /name: r7-external-test-live-evidence-\$\{\{ github\.run_id \}\}/);
  assert.match(workflow, /path: \.r7-live-evidence\//);
  assert.match(workflow, /retention-days: 30/);
  assert.match(workflow, /BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(workflow, /R7_LIVE_PROBE_OUTPUT\.txt/);
});

test('marker evidence workflow remains read-only toward provider and REAL PROD', () => {
  assert.doesNotMatch(workflow, /push-content|script\.deployments|CLASPRC_JSON_B64|environment:\s*PROD|REAL_WRITE|PROD_ENABLE/);
  assert.match(workflow, /TEST\/SAMPLE\/CONTROL only; REAL\/PROD\/formal scoring\/official submission = 0/);
});
