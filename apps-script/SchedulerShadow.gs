var TTQS_S1_SHADOW_HANDLER = 'ttqsSchedulerShadowTrigger';
var TTQS_S1_SHADOW_INTERVAL_MINUTES = 5;
var TTQS_S1_SHADOW_HEARTBEAT_SHEET = '99_TEST_SchedulerShadow_執行紀錄';

function ttqsSchedulerShadowColumns_() {
  return [
    { header: 'run_id', description: 'S1 TEST shadow scheduler run ID.' },
    { header: 'started_at', description: 'Scheduler shadow run start time in TEST timezone.' },
    { header: 'finished_at', description: 'Scheduler shadow run finish time in TEST timezone.' },
    { header: 'status', description: 'PASS / FAIL for this TEST-only shadow run.' },
    { header: 'handler', description: 'Installable trigger handler name.' },
    { header: 'source_count', description: 'Number of raw source sheets scanned.' },
    { header: 'raw_rows_scanned', description: 'Number of synthetic/sample raw rows scanned.' },
    { header: 'range_read_calls', description: 'Provider range reads reported by the shadow scanner.' },
    { header: 'inserted', description: 'Observation rows inserted during this shadow run.' },
    { header: 'unchanged', description: 'Observation rows already present and unchanged.' },
    { header: 'quarantined', description: 'Observation rows quarantined by source-integrity controls.' },
    { header: 'raw_mutation', description: 'Detected raw mutation count.' },
    { header: 'source_key_collision', description: 'Detected source-key collision count.' },
    { header: 'reconciliation_status', description: 'Shadow reconciliation status.' },
    { header: 'reconciliation_raw_count', description: 'Raw locator count seen by shadow reconciliation.' },
    { header: 'observation_count', description: 'Observation row count seen by shadow reconciliation.' },
    { header: 'unexplained', description: 'Raw locators without Observation rows.' },
    { header: 'unknown_internal', description: 'Observation locators without raw rows.' },
    { header: 'duplicate_locator', description: 'Duplicate Observation source locator count.' },
    { header: 'formal_duplicate_acceptance', description: 'Duplicate ACCEPTED source-key count.' },
    { header: 'total_ms', description: 'Total ttqsScheduler runtime in milliseconds.' },
    { header: 'legacy_processing_unchanged', description: 'Must remain TRUE during S1 shadow mode.' },
    { header: 'error', description: 'Bounded TEST-only error summary; empty on PASS.' }
  ];
}

function ttqsEnsureSchedulerShadowSheet_() {
  ttqsAssertTestOnly_();
  var sheet = ttqsEnsureStructuredSheet_(ttqsOpenCore_(), TTQS_S1_SHADOW_HEARTBEAT_SHEET, ttqsSchedulerShadowColumns_());
  try {
    if (!sheet.isSheetHidden()) sheet.hideSheet();
  } catch (err) {
    // Hidden telemetry is a presentation preference, not a runtime safety dependency.
  }
  return sheet;
}

function ttqsSchedulerShadowBoundedError_(err) {
  if (!err) return '';
  return String(err && err.message ? err.message : err).slice(0, 500);
}

function ttqsRecordSchedulerShadowRun_(runId, startedAt, startedAtText, result, err) {
  var reconciliation = result && result.reconciliation ? result.reconciliation : {};
  var ingest = result && result.ingest ? result.ingest : {};
  var finishedAt = Date.now();
  var object = {
    run_id: String(runId),
    started_at: String(startedAtText),
    finished_at: ttqsNow_(),
    status: err ? 'FAIL' : 'PASS',
    handler: TTQS_S1_SHADOW_HANDLER,
    source_count: result ? Number(result.sources || 0) : '',
    raw_rows_scanned: result ? Number(result.raw_rows_scanned || 0) : '',
    range_read_calls: result ? Number(result.range_read_calls || 0) : '',
    inserted: result ? Number(ingest.inserted || 0) : '',
    unchanged: result ? Number(ingest.unchanged || 0) : '',
    quarantined: result ? Number(ingest.quarantined || 0) : '',
    raw_mutation: result ? Number(ingest.rawMutation || 0) : '',
    source_key_collision: result ? Number(ingest.sourceKeyCollision || 0) : '',
    reconciliation_status: result ? String(reconciliation.status || '') : '',
    reconciliation_raw_count: result ? Number(reconciliation.raw_count || 0) : '',
    observation_count: result ? Number(reconciliation.observation_count || 0) : '',
    unexplained: result ? Number(reconciliation.unexplained || 0) : '',
    unknown_internal: result ? Number(reconciliation.unknown_internal || 0) : '',
    duplicate_locator: result ? Number(reconciliation.duplicate_locator || 0) : '',
    formal_duplicate_acceptance: result ? Number(reconciliation.formal_duplicate_acceptance || 0) : '',
    total_ms: result && result.timings_ms ? Number(result.timings_ms.total || (finishedAt - startedAt)) : Number(finishedAt - startedAt),
    legacy_processing_unchanged: result ? String(result.legacy_processing_unchanged === true).toUpperCase() : '',
    error: ttqsSchedulerShadowBoundedError_(err)
  };
  ttqsAppendObject_(ttqsEnsureSchedulerShadowSheet_(), object);
  return object;
}

function ttqsSchedulerShadowTrigger() {
  ttqsAssertTestOnly_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');
  var runId = ttqsStableId_('S1RUN-', Utilities.getUuid(), 24);
  var startedAt = Date.now();
  var startedAtText = ttqsNow_();
  var result = null;
  try {
    result = ttqsScheduler();
    ttqsWithScriptLock_(function() {
      ttqsRecordSchedulerShadowRun_(runId, startedAt, startedAtText, result, null);
    });
    return result;
  } catch (err) {
    try {
      ttqsWithScriptLock_(function() {
        ttqsRecordSchedulerShadowRun_(runId, startedAt, startedAtText, result, err);
      });
    } catch (recordErr) {
      throw new Error('S1_SHADOW_RECORD_FAIL:' + ttqsSchedulerShadowBoundedError_(recordErr) + '|ORIGINAL:' + ttqsSchedulerShadowBoundedError_(err));
    }
    throw err;
  }
}

function ttqsShadowSchedulerTriggers_() {
  return ScriptApp.getProjectTriggers().filter(function(trigger) {
    return trigger.getHandlerFunction() === TTQS_S1_SHADOW_HANDLER;
  });
}

function ttqsRemoveShadowSchedulerTrigger_() {
  ttqsShadowSchedulerTriggers_().forEach(function(trigger) {
    ScriptApp.deleteTrigger(trigger);
  });
}

function ttqsAssertShadowSchedulerTriggerContract_() {
  var triggers = ttqsShadowSchedulerTriggers_();
  if (triggers.length !== 1) throw new Error('S1_SHADOW_TRIGGER_COUNT_INVALID:' + triggers.length);
  var trigger = triggers[0];
  if (trigger.getEventType() !== ScriptApp.EventType.CLOCK) throw new Error('S1_SHADOW_TRIGGER_EVENT_TYPE_INVALID');
  if (trigger.getTriggerSource() !== ScriptApp.TriggerSource.CLOCK) throw new Error('S1_SHADOW_TRIGGER_SOURCE_INVALID');
  return {
    handler: trigger.getHandlerFunction(),
    eventType: String(trigger.getEventType()),
    triggerSource: String(trigger.getTriggerSource()),
    intervalMinutes: TTQS_S1_SHADOW_INTERVAL_MINUTES
  };
}

function ttqsInstallShadowSchedulerTest() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  return ttqsWithScriptLock_(function() {
    ttqsAssertTestOnly_();
    if (typeof ttqsSchedulerRuntimeMode_ === 'function' && typeof TTQS_S2_MODE !== 'undefined' && ttqsSchedulerRuntimeMode_() === TTQS_S2_MODE) {
      throw new Error('S2_RUNTIME_MODE_ACTIVE');
    }
    if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');
    var legacyBefore = ttqsAssertManagedTriggerContract_();
    ttqsRemoveShadowSchedulerTrigger_();
    ScriptApp.newTrigger(TTQS_S1_SHADOW_HANDLER).timeBased().everyMinutes(TTQS_S1_SHADOW_INTERVAL_MINUTES).create();
    ttqsEnsureSchedulerShadowSheet_();
    var shadow = ttqsAssertShadowSchedulerTriggerContract_();
    var legacyAfter = ttqsAssertManagedTriggerContract_();
    return {
      mode: 'S1_OBSERVATION_SHADOW',
      environment: 'TEST',
      shadow: shadow,
      legacy_before: legacyBefore.counts,
      legacy_after: legacyAfter.counts,
      legacy_processing_unchanged: true
    };
  });
}

function ttqsRemoveShadowSchedulerTest() {
  ScriptApp.requireAllScopes(ScriptApp.AuthMode.FULL);
  return ttqsWithScriptLock_(function() {
    ttqsAssertTestOnly_();
    ttqsRemoveShadowSchedulerTrigger_();
    var remaining = ttqsShadowSchedulerTriggers_().length;
    if (remaining !== 0) throw new Error('S1_SHADOW_TRIGGER_REMOVE_FAILED:' + remaining);
    var legacy = ttqsAssertManagedTriggerContract_();
    return {
      mode: 'S1_OBSERVATION_SHADOW',
      environment: 'TEST',
      shadow_trigger_count: 0,
      legacy: legacy.counts,
      legacy_processing_unchanged: true
    };
  });
}
