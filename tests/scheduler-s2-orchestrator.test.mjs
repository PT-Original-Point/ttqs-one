import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/SchedulerOrchestrator.gs', 'utf8');
const bootstrap = fs.readFileSync('apps-script/Bootstrap.gs', 'utf8');
const shadow = fs.readFileSync('apps-script/SchedulerShadow.gs', 'utf8');

function functionBody(name, nextName) {
  const pattern = new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}\\n\\nfunction ${nextName}`);
  const match = source.match(pattern);
  assert.ok(match, `${name} body must be isolatable`);
  return match[1];
}

test('S2 orchestrator source parses', () => {
  new vm.Script(source, { filename: 'SchedulerOrchestrator.gs' });
});

test('S2 preserves exact 1/5/60/60 task cadence with one-minute master tick', () => {
  assert.match(source, /TTQS_S2_MASTER_INTERVAL_MINUTES = 1/);
  assert.match(source, /\{ name: 'RETRY', cadenceMinutes: 1 \}/);
  assert.match(source, /\{ name: 'OBSERVATION', cadenceMinutes: 5 \}/);
  assert.match(source, /\{ name: 'RECONCILE', cadenceMinutes: 60 \}/);
  assert.match(source, /\{ name: 'CONSULT', cadenceMinutes: 60 \}/);
  assert.match(source, /newTrigger\(TTQS_S2_MASTER_HANDLER\)\.timeBased\(\)\.everyMinutes\(TTQS_S2_MASTER_INTERVAL_MINUTES\)\.create\(\)/);
});

test('S2 due-state absorbs duplicate or jitter ticks with lease and last-attempt cadence', () => {
  assert.match(source, /TTQS_S2_TASK_LEASE_MINUTES = 10/);
  assert.match(source, /lease_until_ms/);
  assert.match(source, /reason: 'LEASE_ACTIVE'/);
  assert.match(source, /Math\.max\(Number\(task\.last_success_ms \|\| 0\), Number\(task\.last_finished_ms \|\| 0\)\)/);
  assert.match(source, /reason: 'NOT_DUE'/);
  assert.match(source, /reason: 'CADENCE_DUE'/);
});

test('S2 failed hourly task does not retry every minute', () => {
  const match = source.match(/function ttqsS2TaskDue_\(task, definition, nowMillis\) \{([\s\S]*?)\n\}/);
  assert.ok(match, 'due function must be isolatable');
  const context = {};
  vm.createContext(context);
  vm.runInContext(`function ttqsS2TaskDue_(task, definition, nowMillis) {${match[1]}\n}`, context);
  const failedAt = 1_000_000;
  const task = { last_success_ms: 0, last_finished_ms: failedAt, lease_until_ms: 0 };
  assert.deepEqual(
    JSON.parse(JSON.stringify(context.ttqsS2TaskDue_(task, { cadenceMinutes: 60 }, failedAt + 59 * 60_000))),
    { due: false, reason: 'NOT_DUE' }
  );
  assert.deepEqual(
    JSON.parse(JSON.stringify(context.ttqsS2TaskDue_(task, { cadenceMinutes: 60 }, failedAt + 60 * 60_000))),
    { due: true, reason: 'CADENCE_DUE' }
  );
});

test('S2 master does not hold one outer script lock across existing locked tasks', () => {
  const master = functionBody('ttqsSchedulerMasterTrigger', 'ttqsS2MasterTriggers_');
  assert.doesNotMatch(master, /ttqsWithScriptLock_/);
  assert.match(master, /ttqsS2ClaimTask_\(definition, tickId\)/);
  assert.match(master, /ttqsS2ExecuteTask_\(definition\.name\)/);
  assert.match(master, /ttqsS2CommitTask_\(claim, taskStartedAt, result, taskError\)/);
  const claim = functionBody('ttqsS2ClaimTask_', 'ttqsS2ResultSummary_');
  const commit = functionBody('ttqsS2CommitTask_', 'ttqsS2RecordTick_');
  assert.match(claim, /ttqsWithScriptLock_/);
  assert.match(commit, /ttqsWithScriptLock_/);
});

test('S2 reuses existing task entrypoints instead of cloning business logic', () => {
  const execute = functionBody('ttqsS2ExecuteTask_', 'ttqsS2AppendLogObject_');
  assert.match(execute, /RETRY'\) return ttqsRetryFailedJobs\(\)/);
  assert.match(execute, /OBSERVATION'\) return ttqsScheduler\(\)/);
  assert.match(execute, /RECONCILE'\) return ttqsReconcile\(\)/);
  assert.match(execute, /CONSULT'\) return ttqsRefreshConsultView\(\)/);
  assert.doesNotMatch(execute, /ttqsRetryFailedJobsUnlocked_|ttqsReconcileUnlocked_|ttqsRefreshConsultViewUnlocked_/);
});

test('S2 treats unhealthy returned results as task failures, not successful execution', () => {
  const match = source.match(/function ttqsS2TaskResultHealth_\(taskName, result\) \{([\s\S]*?)\n\}\n\nfunction ttqsS2ExecuteTask_/);
  assert.ok(match, 'result health function must be isolatable');
  const context = {};
  vm.createContext(context);
  vm.runInContext(`function ttqsS2TaskResultHealth_(taskName, result) {${match[1]}\n}`, context);
  const health = (task, result) => JSON.parse(JSON.stringify(context.ttqsS2TaskResultHealth_(task, result)));

  assert.equal(health('RETRY', [{ error: 'synthetic' }]).pass, false);
  assert.equal(health('RETRY', []).pass, true);
  assert.equal(health('OBSERVATION', { ingest: { quarantined: 1, rawMutation: 0, sourceKeyCollision: 0 }, reconciliation: { status: 'PASS_WITH_QUARANTINE' } }).pass, false);
  assert.equal(health('OBSERVATION', { ingest: { quarantined: 0, rawMutation: 0, sourceKeyCollision: 0 }, reconciliation: { status: 'PASS' } }).pass, true);
  assert.equal(health('RECONCILE', { status: 'FAIL', watchdog: { status: 'FAIL' } }).pass, false);
  assert.equal(health('RECONCILE', { status: 'PASS', watchdog: { status: 'PASS' } }).pass, true);
  assert.equal(health('CONSULT', { rows: 18 }).pass, false);
  assert.equal(health('CONSULT', { rows: 19 }).pass, true);

  const master = functionBody('ttqsSchedulerMasterTrigger', 'ttqsS2MasterTriggers_');
  assert.match(master, /ttqsS2TaskResultHealth_\(definition\.name, result\)/);
  assert.match(master, /S2_TASK_RESULT_INVALID/);
});

test('S2 trigger topology keeps form-submit and forbids legacy clocks plus S1 shadow', () => {
  const contract = functionBody('ttqsAssertS2TriggerContract_', 'ttqsS2InitializeState_');
  assert.match(contract, /ttqsOnSpreadsheetFormSubmit/);
  assert.match(contract, /ON_FORM_SUBMIT/);
  assert.match(contract, /SPREADSHEETS/);
  assert.match(contract, /CORE_SPREADSHEET_ID/);
  assert.match(contract, /masterCount !== 1/);
  assert.match(contract, /submitCount !== 1/);
  assert.match(contract, /ttqsS2LegacyClockHandlers_/);
  assert.match(contract, /TTQS_S1_SHADOW_HANDLER/);
  for (const handler of ['ttqsRetryFailedJobs', 'ttqsReconcile', 'ttqsRefreshConsultView']) {
    assert.match(source, new RegExp(handler));
  }
});

test('S2 installer validates S1 baseline, switches topology, and has fail-closed rollback', () => {
  const install = functionBody('ttqsInstallS2ClockConsolidationTest', 'ttqsRollbackS2ClockConsolidationTest');
  assert.match(install, /ttqsAssertLegacyManagedTriggerContract_\(\)/);
  assert.match(install, /ttqsAssertShadowSchedulerTriggerContract_\(\)/);
  assert.match(install, /ttqsS2InitializeState_\(\)/);
  assert.match(install, /newTrigger\(TTQS_S2_MASTER_HANDLER\)/);
  assert.match(install, /ttqsS2RemoveLegacyClockTriggers_\(\)/);
  assert.match(install, /ttqsRemoveShadowSchedulerTrigger_\(\)/);
  assert.match(install, /setProperty\(TTQS_S2_MODE_PROPERTY, TTQS_S2_MODE\)/);
  assert.match(install, /ttqsAssertS2TriggerContract_\(\)/);
  assert.match(install, /ttqsS2RestoreLegacyS1_\(previousMode\)/);
  assert.match(install, /ROLLBACK_FAIL/);
});

test('S2 rollback restores legacy three clocks plus S1 shadow and removes master', () => {
  const restore = functionBody('ttqsS2RestoreLegacyS1_', 'ttqsInstallS2ClockConsolidationTest');
  assert.match(restore, /ttqsRemoveS2MasterTrigger_\(\)/);
  assert.match(restore, /ttqsS2InstallLegacyClockTriggers_\(\)/);
  assert.match(restore, /newTrigger\(TTQS_S1_SHADOW_HANDLER\).*everyMinutes\(TTQS_S1_SHADOW_INTERVAL_MINUTES\)/s);
  assert.match(restore, /deleteProperty\(TTQS_S2_STATE_PROPERTY\)/);
  const rollback = source.match(/function ttqsRollbackS2ClockConsolidationTest\(\) \{([\s\S]*)\n\}/);
  assert.ok(rollback, 'public rollback body must be isolatable');
  assert.match(rollback[1], /ttqsAssertLegacyManagedTriggerContract_\(\)/);
  assert.match(rollback[1], /ttqsAssertShadowSchedulerTriggerContract_\(\)/);
  assert.match(rollback[1], /ttqsS2MasterTriggers_\(\)\.length/);
});

test('Bootstrap becomes topology-aware and cannot recreate legacy clocks during S2', () => {
  assert.match(bootstrap, /function ttqsAssertLegacyManagedTriggerContract_\(\)/);
  assert.match(bootstrap, /function ttqsAssertManagedTriggerContract_\(\)[\s\S]*ttqsSchedulerRuntimeMode_\(\) === TTQS_S2_MODE[\s\S]*ttqsAssertS2TriggerContract_\(\)/);
  assert.match(bootstrap, /S2_MANAGED_TRIGGER_REINSTALL_FORBIDDEN/);
  const install = bootstrap.match(/function ttqsInstallManagedTriggers_\(\) \{([\s\S]*?)\n\}/);
  assert.ok(install, 'legacy installer body must be isolatable');
  assert.match(install[1], /ttqsSchedulerRuntimeMode_\(\) === TTQS_S2_MODE/);
  assert.match(install[1], /ttqsAssertLegacyManagedTriggerContract_\(\)/);
});

test('S1 installer fails closed once S2 runtime mode is active', () => {
  const install = shadow.match(/function ttqsInstallShadowSchedulerTest\(\) \{([\s\S]*?)\n\}\n\nfunction ttqsRemoveShadowSchedulerTest/);
  assert.ok(install, 'S1 installer body must be isolatable');
  assert.match(install[1], /ttqsSchedulerRuntimeMode_\(\) === TTQS_S2_MODE/);
  assert.match(install[1], /S2_RUNTIME_MODE_ACTIVE/);
});

test('S2 telemetry is hidden TEST-only and excludes raw payload or PII fields', () => {
  assert.match(source, /ttqsAssertTestOnly_\(\)/);
  assert.match(source, /99_TEST_SchedulerS2_執行紀錄/);
  assert.match(source, /sheet\.hideSheet\(\)/);
  assert.match(source, /record_type/);
  assert.match(source, /task_name/);
  assert.match(source, /duration_ms/);
  assert.doesNotMatch(source, /provider_timestamp|payload_hash|free_text|display_name|email|phone/i);
});
