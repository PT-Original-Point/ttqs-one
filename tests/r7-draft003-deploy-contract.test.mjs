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
const matrixItemVerifier=fs.readFileSync('scripts/r7-matrix-item-verifier.mjs','utf8');
const runtime=fs.readFileSync('release/official129/Official129Runtime.gs','utf8');
const legacyRegression=fs.readFileSync('release/official129/Official129LegacyRegression.gs','utf8');

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

test('LegacyRegression artifact override preserves canonical R7 identity while keeping human navigation',()=>{
  for(const marker of ['data-artifact-id=','data-official-ref-id=','data-release-id=','data-frozen-pdf-sha256=','data-text-sha256=','data-offline-relative-path=','Frozen PDF 文字投影']) assert.ok(legacyRegression.includes(marker),marker);
  assert.ok(legacyRegression.includes('data-top-level-nav='),'top-level navigation marker missing');
  assert.ok(legacyRegression.includes('查看文件與證據'),'home human-facing navigation missing');
  assert.ok(legacyRegression.includes('開啟文件'),'matrix human-facing navigation missing');
});

test('V-06 homepage diagnostics no longer require second-layer 開啟文件',()=>{
  assert.ok(R7_REQUIRED_PRODUCT_MARKERS.includes('data-top-level-nav='));
  assert.ok(R7_REQUIRED_PRODUCT_MARKERS.includes('data-indicator='));
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes('開啟文件'),false);
  assert.ok(REQUIRED_PRODUCT_MARKERS.includes('查看文件與證據'),'R2 human-facing contract must remain unchanged');
});

test('V-03 live homepage navigation uses actual data-indicator card plus exact canonical route and stays fail-closed',()=>{
  for(const marker of ['homeNavigationDiagnostic','normalizedDataIndicatorTokenCount','normalizedIndicatorQueryTokenCount','safeNavigationSnippet','rawEscapedEquals','verifyHomeIndicatorRoute','routeVerifierPass','exactCanonicalRoute','exactTargetTop']) assert.ok(liveProbe.includes(marker),marker);
  assert.match(liveProbe,/require_\(route\.pass,route\.code\|\|'HOME_INDICATOR_LINK_MISSING'/);
  assert.equal(liveProbe.includes('cold.normalized.includes(`data-matrix-indicator="${i}"`)'),false,'homepage must not require Matrix-only attribute');
  assert.ok(liveProbe.includes("safeSnippet(normalized,['data-indicator=\"1\"','data-top-level-nav=\"true\"','?indicator=1','查看文件與證據'])"));
});

test('V-07 exhaustive live Matrix layer explicitly verifies Chinese document layer before all 129 item checks',()=>{
  assert.ok(liveProbe.includes('verifyEvidenceMatrixLayer'));
  assert.match(liveProbe,/require_\(matrixContract\.pass,matrixContract\.code\|\|'MATRIX_DOCUMENT_LAYER_FAIL'/);
  for(const marker of ['documentCardCount','chineseDocumentCardCount','openDocumentCount','firstCanonicalArtifactUrl']) assert.ok(liveProbe.includes(marker),marker);
  assert.match(liveProbe,/import \{verifyEvidenceMatrixItemIdentity\} from '\.\/r7-matrix-item-verifier\.mjs';/);
  assert.match(liveProbe,/const matrixContract=verifyEvidenceMatrixLayer[\s\S]*require_\(matrixContract\.pass[\s\S]*for\(const x of expected\)\{[\s\S]*verifyEvidenceMatrixItemIdentity/);
  for(const marker of ['MATRIX_REF_MISSING','MATRIX_ARTIFACT_CODE_MISSING','MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING']) assert.ok(matrixItemVerifier.includes(marker),marker);
});

test('DRAFT-003 evaluator homepage must satisfy R2 G02-M01..M19; R7 diagnostics alone can never pass',()=>{
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
