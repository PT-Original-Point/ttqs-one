import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const probe=fs.readFileSync(new URL('../scripts/external-official129-live-probe.mjs',import.meta.url),'utf8');

test('artifact hard threshold remains 4000ms and confirmation load is bounded',()=>{
  assert.ok(probe.includes('const ARTIFACT_PERF_HARD_MS=4000;'));
  assert.ok(probe.includes('const MAX_ARTIFACT_PERF_CONFIRMATIONS=3;'));
  assert.ok(probe.includes('row.ms>ARTIFACT_PERF_HARD_MS'));
  assert.ok(probe.includes('artifactPerfCandidates.length>MAX_ARTIFACT_PERF_CONFIRMATIONS'));
});

test('initial artifact scan stays concurrent while confirmations are sequential',()=>{
  assert.ok(probe.includes('results.artifacts=await mapLimit(data.items,6,probeArtifact);'));
  assert.ok(probe.includes('for(const initial of artifactPerfCandidates)'));
  assert.ok(probe.includes('const confirmation=await probeArtifact(x);'));
  assert.equal(probe.includes('Promise.all(artifactPerfCandidates'),false);
});

test('confirmation is fail-closed and preserves first-sample evidence',()=>{
  assert.ok(probe.includes('const confirmedSlow=confirmation.ms>ARTIFACT_PERF_HARD_MS;'));
  assert.ok(probe.includes('initialMs:initial.ms'));
  assert.ok(probe.includes('confirmationMs:confirmation.ms'));
  assert.ok(probe.includes("reason:'CONFIRMED_OVER_HARD_THRESHOLD'"));
  assert.ok(probe.includes("reason:'TOO_MANY_INITIAL_OUTLIERS'"));
  assert.ok(probe.includes("'ARTIFACT_PERFORMANCE_HARD_FAIL'"));
});

test('confirmation reuses the full artifact correctness contract',()=>{
  assert.ok(probe.includes('async function probeArtifact(x)'));
  for(const marker of ['data-artifact-id','data-official-ref-id','data-release-id','data-frozen-pdf-sha256','data-text-sha256','data-offline-relative-path','ARTIFACT_HTTP_STATUS','ARTIFACT_FRIENDLY_ERROR','ARTIFACT_IDENTITY_OR_HASH_FAIL','ARTIFACT_PAYLOAD_TOO_SHORT'])assert.ok(probe.includes(marker),marker);
});
