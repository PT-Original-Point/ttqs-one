import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/SchedulerShadow.gs', 'utf8');
const bootstrap = fs.readFileSync('apps-script/Bootstrap.gs', 'utf8');

test('S1 shadow scheduler source parses', () => {
  new vm.Script(source, { filename: 'SchedulerShadow.gs' });
});

test('S1 uses one TEST-only wrapper around the existing scheduler', () => {
  assert.match(source, /function ttqsSchedulerShadowTrigger\(\)/);
  assert.match(source, /ttqsAssertTestOnly_\(\)/);
  assert.match(source, /OBSERVATION_SHADOW_MODE !== true/);
  const body = source.match(/function ttqsSchedulerShadowTrigger\(\) \{([\s\S]*?)\n\}\n\nfunction ttqsShadowSchedulerTriggers_/);
  assert.ok(body, 'shadow trigger body must be isolatable');
  assert.equal((body[1].match(/ttqsScheduler\(\)/g) || []).length, 1);
});

test('S1 clock cadence is fixed to five minutes', () => {
  assert.match(source, /TTQS_S1_SHADOW_INTERVAL_MINUTES = 5/);
  assert.match(source, /\.timeBased\(\)\.everyMinutes\(TTQS_S1_SHADOW_INTERVAL_MINUTES\)\.create\(\)/);
});

test('S1 installer preserves the legacy four-trigger contract', () => {
  const install = source.match(/function ttqsInstallShadowSchedulerTest\(\) \{([\s\S]*?)\n\}\n\nfunction ttqsRemoveShadowSchedulerTest/);
  assert.ok(install, 'installer body must be isolatable');
  assert.ok((install[1].match(/ttqsAssertManagedTriggerContract_\(\)/g) || []).length >= 2);
  assert.doesNotMatch(install[1], /ttqsRemoveManagedTriggers_|ttqsInstallManagedTriggers_/);
  for (const name of ['ttqsOnSpreadsheetFormSubmit', 'ttqsRetryFailedJobs', 'ttqsReconcile', 'ttqsRefreshConsultView']) {
    assert.match(bootstrap, new RegExp(`newTrigger\\('${name}'\\)`));
  }
});

test('S1 removal targets only the shadow wrapper trigger', () => {
  const remove = source.match(/function ttqsRemoveShadowSchedulerTrigger_\(\) \{([\s\S]*?)\n\}/);
  assert.ok(remove, 'shadow removal body must be isolatable');
  assert.match(remove[1], /ttqsShadowSchedulerTriggers_\(\)/);
  assert.doesNotMatch(remove[1], /ttqsRemoveManagedTriggers_|ttqsOnSpreadsheetFormSubmit|ttqsRetryFailedJobs|ttqsReconcile|ttqsRefreshConsultView/);
});

test('S1 heartbeat is TEST-only hidden summary telemetry', () => {
  assert.match(source, /99_TEST_SchedulerShadow_執行紀錄/);
  assert.match(source, /sheet\.hideSheet\(\)/);
  assert.match(source, /legacy_processing_unchanged/);
  assert.doesNotMatch(source, /payload_hash|provider_timestamp|free_text|display_name|email|phone/i);
});

test('S1 heartbeat records scheduler integrity outcomes without business processing', () => {
  for (const field of ['raw_rows_scanned', 'range_read_calls', 'inserted', 'unchanged', 'quarantined', 'raw_mutation', 'source_key_collision', 'reconciliation_status', 'observation_count', 'total_ms']) {
    assert.match(source, new RegExp(field));
  }
  assert.doesNotMatch(source, /ttqsRetryFailedJobs\(|ttqsReconcile\(|ttqsRefreshConsultView\(|ttqsOnSpreadsheetFormSubmit\(/);
});

test('S1 handler records PASS and FAIL paths', () => {
  assert.match(source, /status: err \? 'FAIL' : 'PASS'/);
  assert.match(source, /ttqsRecordSchedulerShadowRun_\(runId, startedAt, startedAtText, result, null\)/);
  assert.match(source, /ttqsRecordSchedulerShadowRun_\(runId, startedAt, startedAtText, result, err\)/);
});

test('S1 rollback verifies zero shadow triggers and legacy contract remains intact', () => {
  const rollback = source.match(/function ttqsRemoveShadowSchedulerTest\(\) \{([\s\S]*)\n\}/);
  assert.ok(rollback, 'rollback body must be isolatable');
  assert.match(rollback[1], /remaining !== 0/);
  assert.match(rollback[1], /ttqsAssertManagedTriggerContract_\(\)/);
});
