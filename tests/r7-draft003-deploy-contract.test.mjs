import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {R7_REQUIRED_PRODUCT_MARKERS,classifyExternalBlackbox} from '../scripts/external-blackbox-classifier.mjs';

const deploy=fs.readFileSync('.github/workflows/deploy-external-test.yml','utf8');
const liveWorkflow=fs.readFileSync('.github/workflows/verify-external-r7-live.yml','utf8');
const liveProbe=fs.readFileSync('scripts/external-official129-live-probe.mjs','utf8');

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

test('exhaustive live verification always publishes a durable Issue 39 receipt',()=>{
  assert.match(liveWorkflow,/issues: write/);
  assert.match(liveWorkflow,/EXTERNAL_RECEIPT_ISSUE: '39'/);
  assert.match(liveWorkflow,/Publish durable exhaustive-live receipt/);
  assert.match(liveWorkflow,/if: always\(\)/);
  assert.match(liveWorkflow,/TTQS_R7_EXHAUSTIVE_LIVE_RECEIPT_V1/);
  assert.match(liveWorkflow,/workflow_run_id/);
  assert.match(liveWorkflow,/source_sha/);
  assert.match(liveWorkflow,/evidence_artifact/);
  assert.match(liveWorkflow,/gh issue comment "\$EXTERNAL_RECEIPT_ISSUE"/);
});

test('generic anonymous product classifier accepts complete DRAFT-003 evaluator homepage and fails closed when a marker is missing',()=>{
  const product=R7_REQUIRED_PRODUCT_MARKERS.join(' | ');
  const pass=classifyExternalBlackbox(product);
  assert.equal(pass.pass,true);
  assert.equal(pass.mode,'R7_DRAFT003');
  for(const marker of R7_REQUIRED_PRODUCT_MARKERS){
    const result=classifyExternalBlackbox(product.replace(marker,''));
    assert.equal(result.pass,false,marker);
    assert.ok(result.missing.includes(marker),marker);
  }
});
