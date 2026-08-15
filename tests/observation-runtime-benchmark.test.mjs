import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/Benchmark.gs', 'utf8');

test('benchmark source parses', () => {
  assert.doesNotThrow(() => new vm.Script(source));
});

test('benchmark exposes one progressive 50 to 200 to 600 entrypoint', () => {
  assert.match(source, /function ttqsBenchmarkObservationAll\(\)/);
  assert.match(source, /var targets = \[50, 200, 600\]/);
  assert.match(source, /for \(var i = 0; i < targets\.length; i\+\+\)/);
  assert.match(source, /if \(result\.status !== 'PASS'\) throw new Error\('BENCHMARK_LEVEL_NOT_PASS:'/);
});

test('benchmark is hard TEST-only and leaves REAL or PROD untouched', () => {
  assert.match(source, /function ttqsBenchmarkRunLevel_\(target\)[\s\S]*ttqsAssertTestOnly_\(\)/);
  assert.match(source, /function ttqsBenchmarkObservationAll\(\)[\s\S]*ttqsAssertTestOnly_\(\)/);
  assert.match(source, /real_or_prod_touched: false/);
});

test('benchmark never mutates formal response map or formal Observation writer', () => {
  assert.doesNotMatch(source, /setProperty\(['"]TTQS_RESPONSE_SHEET_MAP/);
  assert.doesNotMatch(source, /deleteProperty\(['"]TTQS_RESPONSE_SHEET_MAP/);
  assert.doesNotMatch(source, /ttqsEnsureObservationSheet_\(/);
  assert.doesNotMatch(source, /ttqsObservationApplyCandidates_\(/);
  assert.match(source, /formal_raw_sheets_touched: false/);
  assert.match(source, /formal_observation_touched: false/);
});

test('benchmark uses exact disposable sheet namespace and persistent TEST-only result sheet', () => {
  assert.match(source, /99_TEST_Benchmark_效能紀錄/);
  assert.match(source, /__TTQS_BENCH_OBSERVATION/);
  assert.match(source, /__TTQS_BENCH_SOURCE_/);
  assert.match(source, /function ttqsBenchmarkCleanupTempSheets_\(ss\)/);
  assert.match(source, /ss\.deleteSheet\(sheet\)/);
});

test('benchmark cleanup is fail-safe in finally', () => {
  assert.match(source, /finally \{[\s\S]*ttqsBenchmarkCleanupTempSheets_\(ss\)[\s\S]*cleanup_status/);
  assert.match(source, /BENCHMARK_TEMP_CLEANUP_FAILED/);
});

test('benchmark first pass requires exact insert and zero integrity defects', () => {
  assert.match(source, /ingest\.inserted === target/);
  assert.match(source, /ingest\.unchanged === 0/);
  assert.match(source, /ingest\.quarantined === 0/);
  assert.match(source, /ingest\.rawMutation === 0/);
  assert.match(source, /ingest\.sourceKeyCollision === 0/);
  assert.match(source, /reconciliation\.status === 'PASS'/);
});

test('benchmark second pass is a strict idempotency gate', () => {
  assert.match(source, /secondIngest\.inserted === 0/);
  assert.match(source, /secondIngest\.unchanged === target/);
  assert.match(source, /secondIngest\.quarantined === 0/);
  assert.match(source, /secondIngest\.rawMutation === 0/);
  assert.match(source, /secondIngest\.sourceKeyCollision === 0/);
  assert.match(source, /secondReconciliation\.status === 'PASS'/);
});

test('benchmark scan retains production batch-per-source read strategy', () => {
  assert.match(source, /readStrategy: 'BATCH_PER_SOURCE'/);
  assert.match(source, /rangeReadCalls \+= 1/);
  assert.match(source, /rangeReadCalls \+= 2/);
  assert.match(source, /scan\.rangeReadCalls === 12/);
});
