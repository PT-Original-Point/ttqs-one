import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {
  REQUIRED_PRODUCT_MARKERS,
  R7_REQUIRED_PRODUCT_MARKERS,
  classifyExternalBlackbox
} from '../scripts/external-blackbox-classifier.mjs';

const deploy=fs.readFileSync('.github/workflows/deploy-external-test.yml','utf8');
const liveWorkflow=fs.readFileSync('.github/workflows/verify-external-r7-live.yml','utf8');
const liveProbe=fs.readFileSync('scripts/external-official129-live-probe.mjs','utf8');
const runtime=fs.readFileSync('release/official129/Official129Runtime.gs','utf8');

const release='ER-DEMO-20260901-DRAFT-003';
const projection='94590a9bbfdca699235815fb96e4c37c69156f10689e70b6c3caa74527165a53';
const manifest='e9e5e2145e915a5eac53905239ce52e25b9ea90911756bc707821f0ec568dd79';
const zip='8b79687329b03c08e971cde0ccd8f8efd312487543e2d285e05f4838b1cc3059';

test('deployment pushes deterministic R7 build output and product-change detector covers derived sources',()=>{
  assert.match(deploy,/node scripts\/build-external-official129\.mjs/);
  assert.match(deploy,/--root-dir \.external-viewer-build/);
  assert.match(deploy,/release\/official129 scripts\/build-external-official129\.mjs/);
  assert.match(deploy,new RegExp(release));
  assert.match(deploy,new RegExp(projection));
});

test('exhaustive live verification is pinned to DRAFT-003 registered identity',()=>{
  for(const value of [release,projection,manifest,zip])assert.ok(liveProbe.includes(value),value);
  assert.ok(liveWorkflow.includes(`release=${release}`));
  assert.equal(liveProbe.includes('ER-DEMO-20260901-DRAFT-002'),false);
  assert.equal(liveWorkflow.includes('ER-DEMO-20260901-DRAFT-002'),false);
});

test('exhaustive live verification always publishes durable R2 per-marker evidence in Issue 39',()=>{
  assert.match(liveWorkflow,/issues: write/);
  assert.match(liveWorkflow,/EXTERNAL_RECEIPT_ISSUE: '39'/);
  assert.match(liveWorkflow,/Publish durable Issue 39 evidence receipts/);
  assert.match(liveWorkflow,/if: always\(\)/);
  assert.match(liveWorkflow,/TTQS_R2_G02_MARKER_EVIDENCE_V1/);
  assert.match(liveWorkflow,/R2_G02_19_REQUIRED/);
  assert.match(liveWorkflow,/marker_evidence_sha256/);
  assert.match(liveWorkflow,/cat \.r7-live-evidence\/BLACKBOX_MARKER_EVIDENCE\.json/);
  assert.match(liveWorkflow,/workflow_run_id/);
  assert.match(liveWorkflow,/source_sha/);
  assert.match(liveWorkflow,/artifact_secondary_copy/);
  assert.match(liveWorkflow,/gh issue comment "\$EXTERNAL_RECEIPT_ISSUE"/);
});

test('live verifier uses supported Node, bounded transport-only retry, and never retries semantic failures',()=>{
  assert.match(liveWorkflow,/node-version: '22'/);
  assert.match(liveWorkflow,/MAX_TRANSPORT_ATTEMPTS=3/);
  assert.match(liveWorkflow,/OFFICIAL129_LIVE_BLACKBOX_FAIL fetch failed/);
  assert.match(liveWorkflow,/R7_LIVE_TRANSPORT_RETRY/);
  assert.match(liveWorkflow,/exit "\$PROBE_STATUS"/);
  assert.equal(liveWorkflow.includes("OFFICIAL129_LIVE_BLACKBOX_FAIL ARTIFACT_IDENTITY_OR_HASH_FAIL"),false);
  assert.equal(liveWorkflow.includes("OFFICIAL129_LIVE_BLACKBOX_FAIL HOME_INDICATOR_LINK_MISSING"),false);
});

test('full live evidence is durably machine-readable in Issue 39 and artifact is secondary only',()=>{
  assert.match(liveWorkflow,/R7_LIVE_PROBE_EVIDENCE\.json/);
  assert.match(liveWorkflow,/JSON\.stringify\(parsed\)/);
  assert.match(liveWorkflow,/TTQS_R7_LIVE_EVIDENCE_V1/);
  assert.match(liveWorkflow,/live_evidence_sha256/);
  assert.match(liveWorkflow,/fenced JSON below is the exact compact live evidence payload/);
  assert.match(liveWorkflow,/include-hidden-files: true/);
  assert.match(liveWorkflow,/Preserve live probe evidence as secondary human-download copy/);
});

test('R7 homepage diagnostic wording is byte-for-text aligned across runtime, classifier and live probe',()=>{
  const exact='並非官方強制 129 份文件';
  const stale='不是官方強制 129 份文件';
  assert.ok(runtime.includes(exact),'runtime canonical wording missing');
  assert.ok(R7_REQUIRED_PRODUCT_MARKERS.includes(exact),'classifier diagnostic marker drift');
  assert.ok(liveProbe.includes(exact),'live probe marker drift');
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes(stale),false,'stale classifier wording revived');
  assert.equal(liveProbe.includes(stale),false,'stale live-probe wording revived');
});

test('live homepage navigation failure emits bounded serialization diagnostics while the strict T4b gate remains fail-closed',()=>{
  for(const marker of ['homeNavigationDiagnostic','normalizedDataMatrixIndicatorTokenCount','normalizedIndicatorQueryTokenCount','safeNavigationSnippet','backslashQuotedDataAttr','rawEscapedEquals'])assert.ok(liveProbe.includes(marker),marker);
  assert.match(liveProbe,/HOME_INDICATOR_LINK_MISSING/);
  assert.match(liveProbe,/cold\.normalized\.includes\(`data-matrix-indicator=/);
  assert.ok(liveProbe.includes("slice(0,500)"),'diagnostic snippet must stay bounded');
  assert.equal(liveProbe.includes('HOME_INDICATOR_LINK_MISSING_BYPASSED'),false);
});

test('DRAFT-003 evaluator homepage must satisfy R2 G02-M01..M19; R7 11 diagnostics alone can never pass',()=>{
  const completeProduct=[...REQUIRED_PRODUCT_MARKERS,...R7_REQUIRED_PRODUCT_MARKERS].join(' | ');
  const pass=classifyExternalBlackbox(completeProduct);
  assert.equal(pass.pass,true);
  assert.equal(pass.mode,'R7_DRAFT003');
  assert.equal(pass.contractId,'R2_G02_19_REQUIRED');
  assert.equal(pass.derivation.markerPassCount,19);
  assert.equal(pass.derivation.markerTotal,19);

  const diagnosticsOnly=classifyExternalBlackbox(R7_REQUIRED_PRODUCT_MARKERS.join(' | '));
  assert.equal(diagnosticsOnly.mode,'R7_DRAFT003');
  assert.equal(diagnosticsOnly.derivation.r7DiagnosticsPass,true);
  assert.equal(diagnosticsOnly.derivation.requiredContractPass,false);
  assert.equal(diagnosticsOnly.pass,false);

  for(const marker of REQUIRED_PRODUCT_MARKERS){
    const result=classifyExternalBlackbox(completeProduct.replace(marker,''));
    assert.equal(result.pass,false,marker);
    assert.ok(result.missing.includes(marker),marker);
  }
});
