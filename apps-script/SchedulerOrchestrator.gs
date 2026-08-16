var TTQS_S2_MODE = 'S2_CLOCK_CONSOLIDATED';
var TTQS_S2_MODE_PROPERTY = 'TTQS_SCHEDULER_RUNTIME_MODE';
var TTQS_S2_STATE_PROPERTY = 'TTQS_S2_TASK_STATE';
var TTQS_S2_MASTER_HANDLER = 'ttqsSchedulerMasterTrigger';
var TTQS_S2_MASTER_INTERVAL_MINUTES = 1;
var TTQS_S2_TASK_LEASE_MINUTES = 10;
var TTQS_S2_LOG_SHEET = '99_TEST_SchedulerS2_執行紀錄';

function ttqsSchedulerRuntimeMode_() {
  return String(PropertiesService.getScriptProperties().getProperty(TTQS_S2_MODE_PROPERTY) || 'LEGACY_S1');
}

function ttqsS2TaskDefinitions_() {
  return [
    { name: 'RETRY', cadenceMinutes: 1 },
    { name: 'OBSERVATION', cadenceMinutes: 5 },
    { name: 'RECONCILE', cadenceMinutes: 60 },
    { name: 'CONSULT', cadenceMinutes: 60 }
  ];
}

function ttqsS2LogColumns_() {
  return [
    { header: 'record_id', description: 'S2 TEST scheduler telemetry record ID.' },
    { header: 'record_type', description: 'TICK or TASK.' },
    { header: 'tick_id', description: 'Master tick ID.' },
    { header: 'task_run_id', description: 'Task claim/run ID; blank for TICK rows.' },
    { header: 'task_name', description: 'RETRY / OBSERVATION / RECONCILE / CONSULT / __TICK__.' },
    { header: 'cadence_minutes', description: 'Configured task cadence in minutes.' },
    { header: 'started_at', description: 'TEST scheduler/task start time.' },
    { header: 'finished_at', description: 'TEST scheduler/task finish time.' },
    { header: 'status', description: 'PASS / FAIL / SKIPPED.' },
    { header: 'reason', description: 'Bounded non-PII scheduling reason.' },
    { header: 'duration_ms', description: 'Task or tick runtime in milliseconds.' },
    { header: 'summary', description: 'Bounded non-PII result summary.' },
    { header: 'error', description: 'Bounded non-PII error summary.' }
  ];
}

function ttqsEnsureS2LogSheet_() {
  ttqsAssertTestOnly_();
  var sheet = ttqsEnsureStructuredSheet_(ttqsOpenCore_(), TTQS_S2_LOG_SHEET, ttqsS2LogColumns_());
  try {
    if (!sheet.isSheetHidden()) sheet.hideSheet();
  } catch (err) {
    // Hidden telemetry is presentation-only; safety does not depend on hidden state.
  }
  return sheet;
}

function ttqsS2Bounded_(value, limit) {
  return String(value === null || value === undefined ? '' : value).slice(0, Number(limit || 500));
}

function ttqsS2InitialState_() {
  var state = { revision: 'S2_STATE_V1', tasks: {} };
  ttqsS2TaskDefinitions_().forEach(function(definition) {
    state.tasks[definition.name] = {
      cadence_minutes: definition.cadenceMinutes,
      last_success_ms: 0,
      last_claimed_ms: 0,
      last_finished_ms: 0,
      last_status: 'PENDING',
      last_error: '',
      lease_run_id: '',
      lease_until_ms: 0
    };
  });
  return state;
}

function ttqsS2ValidateState_(state) {
  if (!state || state.revision !== 'S2_STATE_V1' || !state.tasks) throw new Error('S2_TASK_STATE_INVALID');
  ttqsS2TaskDefinitions_().forEach(function(definition) {
    var task = state.tasks[definition.name];
    if (!task) throw new Error('S2_TASK_STATE_MISSING:' + definition.name);
    if (Number(task.cadence_minutes) !== Number(definition.cadenceMinutes)) throw new Error('S2_TASK_CADENCE_DRIFT:' + definition.name);
  });
  return state;
}

function ttqsS2LoadState_() {
  var raw = PropertiesService.getScriptProperties().getProperty(TTQS_S2_STATE_PROPERTY);
  if (!raw) throw new Error('S2_TASK_STATE_REQUIRED');
  return ttqsS2ValidateState_(ttqsParseJson_(raw, null));
}

function ttqsS2SaveState_(state) {
  ttqsS2ValidateState_(state);
  PropertiesService.getScriptProperties().setProperty(TTQS_S2_STATE_PROPERTY, JSON.stringify(state));
  return state;
}

function ttqsS2TaskDue_(task, definition, nowMillis) {
  if (Number(task.lease_until_ms || 0) > Number(nowMillis)) return { due: false, reason: 'LEASE_ACTIVE' };
  var lastAttempt = Math.max(Number(task.last_success_ms || 0), Number(task.last_finished_ms || 0));
  if (!lastAttempt) return { due: true, reason: 'NEVER_ATTEMPTED' };
  var cadenceMs = Number(definition.cadenceMinutes) * 60000;
  if (Number(nowMillis) - lastAttempt >= cadenceMs) return { due: true, reason: 'CADENCE_DUE' };
  return { due: false, reason: 'NOT_DUE' };
}

function ttqsS2ClaimTask_(definition, tickId) {
  return ttqsWithScriptLock_(function() {
    ttqsAssertTestOnly_();
    if (ttqsSchedulerRuntimeMode_() !== TTQS_S2_MODE) return { claimed: false, task: definition.name, reason: 'MODE_NOT_S2' };
    var state = ttqsS2LoadState_();
    var task = state.tasks[definition.name];
    var now = Date.now();
    var due = ttqsS2TaskDue_(task, definition, now);
    if (!due.due) return { claimed: false, task: definition.name, reason: due.reason };
    var runId = ttqsStableId_('S2RUN-', Utilities.getUuid(), 24);
    task.last_claimed_ms = now;
    task.last_status = 'CLAIMED';
    task.last_error = '';
    task.lease_run_id = runId;
    task.lease_until_ms = now + TTQS_S2_TASK_LEASE_MINUTES * 60000;
    ttqsS2SaveState_(state);
    return {
      claimed: true,
      task: definition.name,
      cadenceMinutes: definition.cadenceMinutes,
      tickId: String(tickId),
      runId: runId,
      claimedAt: now,
      reason: due.reason
    };
  });
}

function ttqsS2ResultSummary_(taskName, result) {
  if (taskName === 'RETRY') {
    var rows = Array.isArray(result) ? result : [];
    return { result_count: rows.length, error_count: rows.filter(function(item) { return !!(item && item.error); }).length };
  }
  if (taskName === 'OBSERVATION') {
    var ingest = result && result.ingest ? result.ingest : {};
    var reconciliation = result && result.reconciliation ? result.reconciliation : {};
    return {
      sources: Number(result && result.sources || 0),
      raw_rows_scanned: Number(result && result.raw_rows_scanned || 0),
      inserted: Number(ingest.inserted || 0),
      unchanged: Number(ingest.unchanged || 0),
      quarantined: Number(ingest.quarantined || 0),
      reconciliation_status: String(reconciliation.status || ''),
      observation_count: Number(reconciliation.observation_count || 0),
      legacy_processing_unchanged: result && result.legacy_processing_unchanged === true
    };
  }
  if (taskName === 'RECONCILE') {
    return {
      status: String(result && result.status || ''),
      matched: Number(result && result.matched || 0),
      mismatched: Number(result && result.mismatched || 0),
      observed_raw_responses: Number(result && result.observedRawResponses || 0),
      watchdog_status: String(result && result.watchdog && result.watchdog.status || '')
    };
  }
  if (taskName === 'CONSULT') {
    return { rows: Number(result && result.rows || 0), sheet: String(result && result.sheet || '') };
  }
  return {};
}

function ttqsS2TaskResultHealth_(taskName, result) {
  if (taskName === 'RETRY') {
    var retryRows = Array.isArray(result) ? result : [];
    var retryErrors = retryRows.filter(function(item) { return !!(item && item.error); }).length;
    return { pass: retryErrors === 0, reason: retryErrors ? ('RETRY_ITEM_ERRORS:' + retryErrors) : 'PASS' };
  }
  if (taskName === 'OBSERVATION') {
    var ingest = result && result.ingest ? result.ingest : {};
    var reconciliation = result && result.reconciliation ? result.reconciliation : {};
    var observationPass = String(reconciliation.status || '') === 'PASS' &&
      Number(ingest.quarantined || 0) === 0 &&
      Number(ingest.rawMutation || 0) === 0 &&
      Number(ingest.sourceKeyCollision || 0) === 0;
    return {
      pass: observationPass,
      reason: observationPass ? 'PASS' : ('OBSERVATION_INTEGRITY:' + String(reconciliation.status || '') + ':Q' + Number(ingest.quarantined || 0) + ':M' + Number(ingest.rawMutation || 0) + ':C' + Number(ingest.sourceKeyCollision || 0))
    };
  }
  if (taskName === 'RECONCILE') {
    var reconcilePass = String(result && result.status || '') === 'PASS' && String(result && result.watchdog && result.watchdog.status || '') === 'PASS';
    return { pass: reconcilePass, reason: reconcilePass ? 'PASS' : ('RECONCILE_STATUS:' + String(result && result.status || '') + ':WATCHDOG:' + String(result && result.watchdog && result.watchdog.status || '')) };
  }
  if (taskName === 'CONSULT') {
    var consultRows = Number(result && result.rows || 0);
    return { pass: consultRows === 19, reason: consultRows === 19 ? 'PASS' : ('CONSULT_ROWS:' + consultRows) };
  }
  return { pass: false, reason: 'UNKNOWN_TASK' };
}

function ttqsS2ExecuteTask_(taskName) {
  if (taskName === 'RETRY') return ttqsRetryFailedJobs();
  if (taskName === 'OBSERVATION') return ttqsScheduler();
  if (taskName === 'RECONCILE') return ttqsReconcile();
  if (taskName === 'CONSULT') return ttqsRefreshConsultView();
  throw new Error('S2_UNKNOWN_TASK:' + taskName);
}

function ttqsS2AppendLogObject_(object) {
  ttqsAppendObject_(ttqsEnsureS2LogSheet_(), object);
  return object;
}

function ttqsS2CommitTask_(claim, startedAtMillis, result, err) {
  return ttqsWithScriptLock_(function() {
    var state = ttqsS2LoadState_();
    var task = state.tasks[claim.task];
    if (String(task.lease_run_id || '') !== String(claim.runId)) throw new Error('S2_TASK_LEASE_OWNERSHIP_LOST:' + claim.task);
    var finished = Date.now();
    task.last_finished_ms = finished;
    task.last_status = err ? 'FAIL' : 'PASS';
    task.last_error = err ? ttqsS2Bounded_(err && err.message ? err.message : err, 500) : '';
    if (!err) task.last_success_ms = finished;
    task.lease_run_id = '';
    task.lease_until_ms = 0;
    ttqsS2SaveState_(state);
    return ttqsS2AppendLogObject_({
      record_id: ttqsStableId_('S2LOG-', Utilities.getUuid(), 24),
      record_type: 'TASK',
      tick_id: claim.tickId,
      task_run_id: claim.runId,
      task_name: claim.task,
      cadence_minutes: claim.cadenceMinutes,
      started_at: new Date(startedAtMillis).toISOString(),
      finished_at: new Date(finished).toISOString(),
      status: err ? 'FAIL' : 'PASS',
      reason: claim.reason,
      duration_ms: finished - startedAtMillis,
      summary: ttqsS2Bounded_(JSON.stringify(ttqsS2ResultSummary_(claim.task, result)), 1000),
      error: err ? ttqsS2Bounded_(err && err.message ? err.message : err, 500) : ''
    });
  });
}

function ttqsS2RecordTick_(tickId, startedAtMillis, outcomes) {
  return ttqsWithScriptLock_(function() {
    var finished = Date.now();
    var failed = outcomes.filter(function(item) { return item.status === 'FAIL'; }).length;
    var claimed = outcomes.filter(function(item) { return item.claimed === true; }).map(function(item) { return item.task; });
    var skipped = outcomes.filter(function(item) { return item.claimed !== true; }).map(function(item) { return item.task + ':' + item.reason; });
    return ttqsS2AppendLogObject_({
      record_id: ttqsStableId_('S2LOG-', Utilities.getUuid(), 24),
      record_type: 'TICK',
      tick_id: tickId,
      task_run_id: '',
      task_name: '__TICK__',
      cadence_minutes: TTQS_S2_MASTER_INTERVAL_MINUTES,
      started_at: new Date(startedAtMillis).toISOString(),
      finished_at: new Date(finished).toISOString(),
      status: failed ? 'FAIL' : 'PASS',
      reason: 'claimed=' + claimed.join(',') + ';skipped=' + skipped.join(','),
      duration_ms: finished - startedAtMillis,
      summary: 'task_count=' + outcomes.length + ';failed=' + failed,
      error: ''
    });
  });
}

function ttqsSchedulerMasterTrigger() {
  ttqsAssertTestOnly_();
  if (ttqsSchedulerRuntimeMode_() !== TTQS_S2_MODE) throw new Error('S2_RUNTIME_MODE_REQUIRED');
  var tickId = ttqsStableId_('S2TICK-', Utilities.getUuid(), 24);
  var startedAt = Date.now();
  var outcomes = [];
  ttqsS2TaskDefinitions_().forEach(function(definition) {
    var claim = ttqsS2ClaimTask_(definition, tickId);
    if (!claim.claimed) {
      outcomes.push({ task: definition.name, claimed: false, status: 'SKIPPED', reason: claim.reason });
      return;
    }
    var taskStartedAt = Date.now();
    var result = null;
    var taskError = null;
    try {
      result = ttqsS2ExecuteTask_(definition.name);
      var resultHealth = ttqsS2TaskResultHealth_(definition.name, result);
      if (!resultHealth.pass) taskError = new Error('S2_TASK_RESULT_INVALID:' + definition.name + ':' + resultHealth.reason);
    } catch (err) {
      taskError = err;
    }
    ttqsS2CommitTask_(claim, taskStartedAt, result, taskError);
    outcomes.push({ task: definition.name, claimed: true, status: taskError ? 'FAIL' : 'PASS', reason: claim.reason });
  });
  ttqsS2RecordTick_(tickId, startedAt, outcomes);
  return { mode: TTQS_S2_MODE, tick_id: tickId, outcomes: outcomes };
}

function ttqsS2MasterTriggers_() {
  return ScriptApp.getProjectTriggers().filter(function(trigger) {
    return trigger.getHandlerFunction() === TTQS_S2_MASTER_HANDLER;
  });
}

function ttqsRemoveS2MasterTrigger_() {
  ttqsS2MasterTriggers_().forEach(function(trigger) { ScriptApp.deleteTrigger(trigger); });
}

function ttqsS2LegacyClockHandlers_() {
  return { ttqsRetryFailedJobs: true, ttqsReconcile: true, ttqsRefreshConsultView: true };
}

function ttqsS2RemoveLegacyClockTriggers_() {
  var handlers = ttqsS2LegacyClockHandlers_();
  ScriptApp.getProjectTriggers().forEach(function(trigger) {
    if (handlers[trigger.getHandlerFunction()]) ScriptApp.deleteTrigger(trigger);
  });
}

function ttqsS2InstallLegacyClockTriggers_() {
  ttqsS2RemoveLegacyClockTriggers_();
  ScriptApp.newTrigger('ttqsRetryFailedJobs').timeBased().everyMinutes(1).create();
  ScriptApp.newTrigger('ttqsReconcile').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('ttqsRefreshConsultView').timeBased().everyHours(1).create();
}

function ttqsAssertS2TriggerContract_() {
  var cfg = ttqsConfig_();
  var counts = {};
  var forbidden = ttqsS2LegacyClockHandlers_();
  forbidden[TTQS_S1_SHADOW_HANDLER] = true;
  var masterCount = 0;
  var submitCount = 0;
  ScriptApp.getProjectTriggers().forEach(function(trigger) {
    var handler = trigger.getHandlerFunction();
    counts[handler] = Number(counts[handler] || 0) + 1;
    if (forbidden[handler]) throw new Error('S2_FORBIDDEN_LEGACY_TRIGGER:' + handler);
    if (handler === TTQS_S2_MASTER_HANDLER) {
      masterCount++;
      if (trigger.getEventType() !== ScriptApp.EventType.CLOCK || trigger.getTriggerSource() !== ScriptApp.TriggerSource.CLOCK) throw new Error('S2_MASTER_TRIGGER_CONTRACT_INVALID');
    }
    if (handler === 'ttqsOnSpreadsheetFormSubmit') {
      submitCount++;
      if (trigger.getEventType() !== ScriptApp.EventType.ON_FORM_SUBMIT) throw new Error('S2_FORM_SUBMIT_EVENT_TYPE_INVALID');
      if (trigger.getTriggerSource() !== ScriptApp.TriggerSource.SPREADSHEETS) throw new Error('S2_FORM_SUBMIT_SOURCE_INVALID');
      if (String(trigger.getTriggerSourceId ? trigger.getTriggerSourceId() : '') !== String(cfg.CORE_SPREADSHEET_ID)) throw new Error('S2_FORM_SUBMIT_SOURCE_ID_INVALID');
    }
  });
  if (masterCount !== 1) throw new Error('S2_MASTER_TRIGGER_COUNT_INVALID:' + masterCount);
  if (submitCount !== 1) throw new Error('S2_FORM_SUBMIT_TRIGGER_COUNT_INVALID:' + submitCount);
  return { counts: counts, mode: TTQS_S2_MODE, master: masterCount, formSubmit: submitCount };
}

function ttqsS2InitializeState_() {
  return ttqsS2SaveState_(ttqsS2InitialState_());
}

function ttqsS2RestoreLegacyS1_(previousMode) {
  return ttqsWithScriptLock_(function() {
    ttqsRemoveS2MasterTrigger_();
    ttqsS2InstallLegacyClockTriggers_();
    ttqsRemoveShadowSchedulerTrigger_();
    ScriptApp.newTrigger(TTQS_S1_SHADOW_HANDLER).timeBased().everyMinutes(TTQS_S1_SHADOW_INTERVAL_MINUTES).create();
    var props = PropertiesService.getScriptProperties();
    props.deleteProperty(TTQS_S2_STATE_PROPERTY);
    if (previousMode && previousMode !== TTQS_S2_MODE && previousMode !== 'LEGACY_S1') props.setProperty(TTQS_S2_MODE_PROPERTY, previousMode);
    else props.deleteProperty(TTQS_S2_MODE_PROPERTY);
    return true;
  });
}

function ttqsInstallS2ClockConsolidationTest() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  ttqsAssertTestOnly_();
  if (ttqsSchedulerRuntimeMode_() === TTQS_S2_MODE) return ttqsAssertS2TriggerContract_();
  var legacyBefore = ttqsAssertLegacyManagedTriggerContract_();
  var shadowBefore = ttqsAssertShadowSchedulerTriggerContract_();
  var previousMode = ttqsSchedulerRuntimeMode_();
  try {
    ttqsWithScriptLock_(function() {
      ttqsS2InitializeState_();
      ttqsRemoveS2MasterTrigger_();
      ScriptApp.newTrigger(TTQS_S2_MASTER_HANDLER).timeBased().everyMinutes(TTQS_S2_MASTER_INTERVAL_MINUTES).create();
      ttqsS2RemoveLegacyClockTriggers_();
      ttqsRemoveShadowSchedulerTrigger_();
      PropertiesService.getScriptProperties().setProperty(TTQS_S2_MODE_PROPERTY, TTQS_S2_MODE);
      ttqsEnsureS2LogSheet_();
    });
    var contract = ttqsAssertS2TriggerContract_();
    return {
      mode: TTQS_S2_MODE,
      environment: 'TEST',
      before_legacy: legacyBefore.counts,
      before_shadow: shadowBefore,
      after: contract,
      state_revision: ttqsS2LoadState_().revision,
      form_submit_preserved: true
    };
  } catch (err) {
    try {
      ttqsS2RestoreLegacyS1_(previousMode);
      ttqsAssertLegacyManagedTriggerContract_();
      ttqsAssertShadowSchedulerTriggerContract_();
    } catch (rollbackErr) {
      throw new Error('S2_INSTALL_FAIL:' + ttqsS2Bounded_(err && err.message ? err.message : err, 400) + '|ROLLBACK_FAIL:' + ttqsS2Bounded_(rollbackErr && rollbackErr.message ? rollbackErr.message : rollbackErr, 400));
    }
    throw err;
  }
}

function ttqsRollbackS2ClockConsolidationTest() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  ttqsAssertTestOnly_();
  ttqsS2RestoreLegacyS1_('LEGACY_S1');
  var legacy = ttqsAssertLegacyManagedTriggerContract_();
  var shadow = ttqsAssertShadowSchedulerTriggerContract_();
  return {
    mode: 'LEGACY_S1',
    environment: 'TEST',
    legacy: legacy.counts,
    shadow: shadow,
    s2_master_trigger_count: ttqsS2MasterTriggers_().length
  };
}
