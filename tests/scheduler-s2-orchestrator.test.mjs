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

function cadenceHarness() {
  const cadence = functionBody('ttqsS2CadenceMs_', 'ttqsS2TaskNextDue_');
  const nextDue = functionBody('ttqsS2TaskNextDue_', 'ttqsS2TaskDue_');
  const due = functionBody('ttqsS2TaskDue_', 'ttqsS2AdvanceNextDue_');
  const advance = functionBody('ttqsS2AdvanceNextDue_', 'ttqsS2ClaimTask_');
  const context = {};
  vm.createContext(context);
  vm.runInContext(`
    var TTQS_S2_CADENCE_EARLY_TOLERANCE_MS = 5000;
    function ttqsS2CadenceMs_(definition) {${cadence}\n}
    function ttqsS2TaskNextDue_(task, definition) {${nextDue}\n}
    function ttqsS2TaskDue_(task, definition, scheduleMillis, currentMillis) {${due}\n}
    function ttqsS2AdvanceNextDue_(task, definition, scheduleMillis, due) {${advance}\n}
  `, context);
  return context;
}

function plain(value) {
  return JSON.parse(JSON.stringify(value));
}

test('S2 orchestrator source parses', () => {
  new vm.Script(source, { filename: 'SchedulerOrchestrator.gs' });
});

test('S2 preserves exact 1/5/60/60 task cadence with one-minute master tick', () => {
  assert.match(source, /TTQS_S2_MASTER_INTERVAL_MINUTES = 1/);
  assert.match(source, /TTQS_S2_CADENCE_EARLY_TOLERANCE_MS = 5000/);
  assert.match(source, /\{ name: 'RETRY', cadenceMinutes: 1 \}/);
  assert.match(source, /\{ name: 'OBSERVATION', cadenceMinutes: 5 \}/);
  assert.match(source, /\{ name: 'RECONCILE', cadenceMinutes: 60 \}/);
  assert.match(source, /\{ name: 'CONSULT', cadenceMinutes: 60 \}/);
  assert.match(source, /newTrigger\(TTQS_S2_MASTER_HANDLER\)\.timeBased\(\)\.everyMinutes\(TTQS_S2_MASTER_INTERVAL_MINUTES\)\.create\(\)/);
  assert.match(source, /ttqsS2ClaimTask_\(definition, tickId, startedAt\)/);
});

test('S2 cadence is anchored to scheduler slots, not task completion time', () => {
  const context = cadenceHarness();
  const definition = { name: 'RETRY', cadenceMinutes: 1 };
  const t0 = 1_000_000;
  const task = {
    next_due_ms: 0,
    last_success_ms: 0,
    last_claimed_ms: 0,
    last_finished_ms: 0,
    lease_until_ms: 0
  };

  let due = plain(context.ttqsS2TaskDue_(task, definition, t0, t0));
  assert.equal(due.due, true);
  assert.equal(due.reason, 'NEVER_ATTEMPTED');
  context.ttqsS2AdvanceNextDue_(task, definition, t0, due);
  assert.equal(task.next_due_ms, t0 + 60_000);

  task.last_claimed_ms = t0 + 500;
  task.last_success_ms = t0 + 45_000;
  task.last_finished_ms = t0 + 45_000;

  due = plain(context.ttqsS2TaskDue_(task, definition, t0 + 59_500, t0 + 59_500));
  assert.equal(due.due, true, 'slightly early next master tick must still claim the next one-minute slot');
  assert.equal(due.reason, 'CADENCE_DUE');
  context.ttqsS2AdvanceNextDue_(task, definition, t0 + 59_500, due);
  assert.equal(task.next_due_ms, t0 + 120_000, 'next slot must advance from scheduled due time, not the 45-second completion time');

  due = plain(context.ttqsS2TaskDue_(task, definition, t0 + 70_000, t0 + 70_000));
  assert.equal(due.due, false, 'duplicate/jitter tick inside the same slot must be suppressed');
  assert.equal(due.reason, 'NOT_DUE');
});

test('S2 five-minute Observation cadence uses fixed slots with bounded trigger jitter', () => {
  const context = cadenceHarness();
  const definition = { name: 'OBSERVATION', cadenceMinutes: 5 };
  const t0 = 2_000_000;
  const task = { next_due_ms: 0, last_claimed_ms: 0, last_success_ms: 0, last_finished_ms: 0, lease_until_ms: 0 };
  const first = plain(context.ttqsS2TaskDue_(task, definition, t0, t0));
  context.ttqsS2AdvanceNextDue_(task, definition, t0, first);

  assert.equal(plain(context.ttqsS2TaskDue_(task, definition, t0 + 4 * 60_000 + 30_000, t0 + 4 * 60_000 + 30_000)).due, false);
  const nearSlot = plain(context.ttqsS2TaskDue_(task, definition, t0 + 5 * 60_000 - 2_000, t0 + 5 * 60_000 - 2_000));
  assert.equal(nearSlot.due, true);
  context.ttqsS2AdvanceNextDue_(task, definition, t0 + 5 * 60_000 - 2_000, nearSlot);
  assert.equal(task.next_due_ms, t0 + 10 * 60_000);
});

test('S2 failed hourly task does not retry every minute', () => {
  const context = cadenceHarness();
  const definition = { name: 'RECONCILE', cadenceMinutes: 60 };
  const t0 = 3_000_000;
  const task = { next_due_ms: 0, last_claimed_ms: 0, last_success_ms: 0, last_finished_ms: 0, lease_until_ms: 0 };
  const first = plain(context.ttqsS2TaskDue_(task, definition, t0, t0));
  context.ttqsS2AdvanceNextDue_(task, definition, t0, first);
  task.last_claimed_ms = t0;
  task.last_finished_ms = t0 + 50_000;
  task.last_success_ms = 0;

  assert.equal(plain(context.ttqsS2TaskDue_(task, definition, t0 + 60_000, t0 + 60_000)).due, false);
  const hourlySlot = plain(context.ttqsS2TaskDue_(task, definition, t0 + 60 * 60_000 - 1_000, t0 + 60 * 60_000 - 1_000));
  assert.equal(hourlySlot.due, true);
  assert.equal(hourlySlot.reason, 'CADENCE_DUE');
});

test('S2 legacy V1 state migrates lazily without completion-time drift', () => {
  const context = cadenceHarness();
  const definition = { name: 'RETRY', cadenceMinutes: 1 };
  const t0 = 4_000_000;
  const task = {
    last_claimed_ms: t0,
    last_success_ms: t0 + 45_000,
    last_finished_ms: t0 + 45_000,
    lease_until_ms: 0
  };
  const schedule = t0 + 59_000;
  const due = plain(context.ttqsS2TaskDue_(task, definition, schedule, schedule));
  assert.equal(due.due, true, 'legacy state must use last claim rather than last finish as the migration cadence anchor');
  assert.equal(due.persisted, false);
  context.ttqsS2AdvanceNextDue_(task, definition, schedule, due);
  assert.equal(task.next_due_ms, schedule + 60_000, 'first migrated claim must realign to the master scheduler slot');
});

test('S2 missed slots collapse to one catch-up run instead of a burst', () => {
  const context = cadenceHarness();
  const definition = { name: 'RETRY', cadenceMinutes: 1 };
  const t0 = 5_000_000;
  const task = { next_due_ms: t0 + 60_000, last_claimed_ms: t0, last_success_ms: t0, last_finished_ms: t0, lease_until_ms: 0 };
  const late = plain(context.ttqsS2TaskDue_(task, definition, t0 + 3 * 60_000 + 1_000, t0 + 3 * 60_000 + 1_000));
  assert.equal(late.due, true);
  context.ttqsS2AdvanceNextDue_(task, definition, t0 + 3 * 60_000 + 1_000, late);
  assert.equal(task.next_due_ms, t0 + 4 * 60_000);
  assert.equal(plain(context.ttqsS2TaskDue_(task, definition, t0 + 3 * 60_000 + 10_000, t0 + 3 * 60_000 + 10_000)).due, false);
});

test('S2 due-state keeps lease protection and bounded jitter suppression', () => {
  assert.match(source, /TTQS_S2_TASK_LEASE_MINUTES = 10/);
  assert.match(source, /next_due_ms/);
  assert.match(source, /reason: 'LEASE_ACTIVE'/);
  assert.match(source, /reason: 'NOT_DUE'/);
  assert.match(source, /reason: 'CADENCE_DUE'/);
  assert.match(source, /TTQS_S2_CADENCE_EARLY_TOLERANCE_MS/);
});

test('S2 master does not hold one outer script lock across existing locked tasks', () => {
  const master = functionBody('ttqsSchedulerMasterTrigger', 'ttqsS2MasterTriggers_');
  assert.doesNotMatch(master, /ttqsWithScriptLock_/);
  assert.match(master, /ttqsS2ClaimTask_\(definition, tickId, startedAt\)/);
  assert.match(master, /ttqsS2ExecuteTask_\(definition\.name\)/);
  assert.match(master, /ttqsS2CommitTask_\(claim, taskStartedAt, result, taskError\)/);
  const claim = functionBody('ttqsS2ClaimTask_', 'ttqsS2ResultSummary_');
  const commit = functionBody('ttqsS2CommitTask_', 'ttqsS2RecordTick_');
  assert.match(claim, /ttqsWithScriptLock_/);
  assert.match(claim, /ttqsS2AdvanceNextDue_/);
  assert.match(commit, /ttqsWithScriptLock_/);
});

test('S2 reuses existing task entrypoints and delegates Observation to S3 dual-run cycle', () => {
  const execute = functionBody('ttqsS2ExecuteTask_', 'ttqsS2AppendLogObject_');
  assert.match(execute, /RETRY'\) return ttqsRetryFailedJobs\(\)/);
  assert.match(execute, /OBSERVATION'\) return ttqsS3ObservationCycle\(\)/);
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
  assert.equal(health('OBSERVATION', { ingest: { quarantined: 0, rawMutation: 0, sourceKeyCollision: 0 }, processing: { deferred: 1, quarantined: 0, rejected: 0 }, reconciliation: { status: 'PASS' } }).pass, true);
  assert.equal(health('OBSERVATION', { ingest: { quarantined: 0, rawMutation: 0, sourceKeyCollision: 0 }, processing: { quarantined: 1, rejected: 0 }, reconciliation: { status: 'PASS_WITH_QUARANTINE' } }).pass, false);
  assert.equal(health('OBSERVATION', { ingest: { quarantined: 0, rawMutation: 0, sourceKeyCollision: 0 }, processing: { quarantined: 0, rejected: 1 }, reconciliation: { status: 'PASS' } }).pass, false);
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
