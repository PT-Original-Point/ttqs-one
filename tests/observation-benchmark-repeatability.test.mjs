import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/BenchmarkRepeatability.gs', 'utf8');

test('repeatability source parses', () => {
  assert.doesNotThrow(() => new vm.Script(source));
});

test('repeatability exposes one TEST-only entrypoint', () => {
  assert.match(source, /function ttqsBenchmarkObservationRepeatability\(\)/);
  assert.match(source, /function ttqsBenchmarkObservationRepeatability\(\)[\s\S]*ttqsAssertTestOnly_\(\)/);
  assert.match(source, /OBSERVATION_SHADOW_MODE_REQUIRED/);
});

test('repeatability plan uses independent 200x3 and 600x5 runs', () => {
  assert.match(source, /\{ target: 200, runs: 3 \}/);
  assert.match(source, /\{ target: 600, runs: 5 \}/);
  assert.match(source, /ttqsBenchmarkRunLevel_\(target\)/);
  assert.doesNotMatch(source, /ttqsBenchmarkObservationAll\(\)/);
});

test('repeatability records provenance and independent repeat identity', () => {
  for (const field of ['suite_id', 'repeatability_revision', 'source_fingerprint', 'workload_kind', 'repeat_index', 'repeat_total', 'run_order', 'run_id']) {
    assert.match(source, new RegExp(field));
  }
  assert.match(source, /SYNTHETIC_TEST_SAMPLE/);
  assert.match(source, /REPEATABILITY_V1/);
});

test('source fingerprint covers production and benchmark reconciliation paths', () => {
  for (const fn of ['ttqsObservationRawLocators_', 'ttqsBenchmarkRawLocators_', 'ttqsBenchmarkScanSources_', 'ttqsBenchmarkReconcile_', 'ttqsBenchmarkRunLevel_']) {
    assert.match(source, new RegExp(`String\\(${fn}\\)`));
  }
  assert.match(source, /ttqsDigest_/);
});

test('repeatability summary persists timings and integrity outcomes', () => {
  for (const field of [
    'first_scan_ms', 'first_ingest_ms', 'first_reconcile_ms', 'first_total_ms',
    'second_scan_ms', 'second_ingest_ms', 'second_reconcile_ms', 'second_total_ms',
    'first_inserted', 'second_inserted', 'second_unchanged',
    'first_quarantined', 'second_quarantined',
    'first_raw_mutation', 'second_raw_mutation',
    'first_collision', 'second_collision',
    'first_reconciliation', 'second_reconciliation',
    'observation_count', 'cleanup_status'
  ]) assert.match(source, new RegExp(field));
});

test('repeatability uses dedicated non-PII TEST summary sheet', () => {
  assert.match(source, /99_TEST_Benchmark_重複性紀錄/);
  assert.match(source, /ttqsEnsureStructuredSheet_/);
  assert.match(source, /ttqsAppendObject_/);
});

test('repeatability never mutates formal response map or formal Observation path', () => {
  assert.doesNotMatch(source, /setProperty\(['"]TTQS_RESPONSE_SHEET_MAP/);
  assert.doesNotMatch(source, /deleteProperty\(['"]TTQS_RESPONSE_SHEET_MAP/);
  assert.doesNotMatch(source, /ttqsEnsureObservationSheet_\(/);
  assert.doesNotMatch(source, /ttqsObservationApplyCandidates_\(/);
  assert.match(source, /real_or_prod_touched: false/);
  assert.match(source, /formal_raw_sheets_touched: false/);
  assert.match(source, /formal_observation_touched: false/);
});

test('repeatability is cleanup-safe and fails closed', () => {
  assert.match(source, /REPEATABILITY_STALE_TEMP_CLEANUP_FAILED/);
  assert.match(source, /REPEATABILITY_FAILURE_AND_CLEANUP_FAILED/);
  assert.match(source, /REPEATABILITY_FINAL_CLEANUP_FAILED/);
  assert.match(source, /REPEATABILITY_RUN_NOT_PASS/);
});
