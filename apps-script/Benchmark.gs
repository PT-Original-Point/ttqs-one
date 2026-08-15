var TTQS_BENCHMARK_RESULT_SHEET = '99_TEST_Benchmark_效能紀錄';
var TTQS_BENCHMARK_OBSERVATION_SHEET = '__TTQS_BENCH_OBSERVATION';
var TTQS_BENCHMARK_SOURCE_PREFIX = '__TTQS_BENCH_SOURCE_';

function ttqsBenchmarkResultColumns_() {
  return [
    { header: 'run_id', description: 'TEST benchmark run ID.' },
    { header: 'executed_at', description: 'Benchmark completion time in TEST timezone.' },
    { header: 'source_version', description: 'TTQS ONE source version.' },
    { header: 'target_rows', description: 'Synthetic raw rows for this benchmark level.' },
    { header: 'source_count', description: 'Synthetic source sheet count.' },
    { header: 'status', description: 'PASS / FAIL.' },
    { header: 'seed_ms', description: 'Temporary source creation and seeding time.' },
    { header: 'first_scan_ms', description: 'First-pass scan time.' },
    { header: 'first_ingest_ms', description: 'First-pass ingest time.' },
    { header: 'first_reconcile_ms', description: 'First-pass reconciliation time.' },
    { header: 'first_total_ms', description: 'First-pass scan + ingest + reconcile time.' },
    { header: 'first_range_read_calls', description: 'First-pass provider range read calls.' },
    { header: 'first_inserted', description: 'First-pass inserted observations.' },
    { header: 'first_unchanged', description: 'First-pass unchanged observations.' },
    { header: 'first_quarantined', description: 'First-pass quarantined observations.' },
    { header: 'first_raw_mutation', description: 'First-pass raw mutation detections.' },
    { header: 'first_collision', description: 'First-pass source-key collisions.' },
    { header: 'first_reconciliation', description: 'First-pass reconciliation status.' },
    { header: 'second_scan_ms', description: 'Idempotency-pass scan time.' },
    { header: 'second_ingest_ms', description: 'Idempotency-pass ingest time.' },
    { header: 'second_reconcile_ms', description: 'Idempotency-pass reconciliation time.' },
    { header: 'second_total_ms', description: 'Idempotency-pass total time.' },
    { header: 'second_inserted', description: 'Idempotency-pass inserted observations; must be 0.' },
    { header: 'second_unchanged', description: 'Idempotency-pass unchanged observations; must equal target.' },
    { header: 'second_quarantined', description: 'Idempotency-pass quarantined observations.' },
    { header: 'second_raw_mutation', description: 'Idempotency-pass raw mutation detections.' },
    { header: 'second_collision', description: 'Idempotency-pass source-key collisions.' },
    { header: 'second_reconciliation', description: 'Idempotency-pass reconciliation status.' },
    { header: 'observation_count', description: 'Temporary Observation rows after second pass.' },
    { header: 'cleanup_status', description: 'PASS only when all temporary sheets were removed.' },
    { header: 'error', description: 'Bounded TEST-only failure summary; empty on PASS.' }
  ];
}

function ttqsBenchmarkEnsureResultSheet_(ss) {
  return ttqsEnsureStructuredSheet_(ss, TTQS_BENCHMARK_RESULT_SHEET, ttqsBenchmarkResultColumns_());
}

function ttqsBenchmarkTempSheetNames_() {
  return [
    TTQS_BENCHMARK_OBSERVATION_SHEET,
    TTQS_BENCHMARK_SOURCE_PREFIX + 'NEEDS',
    TTQS_BENCHMARK_SOURCE_PREFIX + 'REGISTRATION',
    TTQS_BENCHMARK_SOURCE_PREFIX + 'REACTION',
    TTQS_BENCHMARK_SOURCE_PREFIX + 'FOLLOWUP30'
  ];
}

function ttqsBenchmarkCleanupTempSheets_(ss) {
  var failed = [];
  ttqsBenchmarkTempSheetNames_().forEach(function(name) {
    var sheet = ss.getSheetByName(name);
    if (!sheet) return;
    try {
      ss.deleteSheet(sheet);
    } catch (err) {
      failed.push(name + ':' + String(err && err.message ? err.message : err).slice(0, 120));
    }
  });
  return { status: failed.length ? 'FAIL' : 'PASS', errors: failed };
}

function ttqsBenchmarkSafeError_(err) {
  return String(err && err.message ? err.message : err || '').slice(0, 500);
}

function ttqsBenchmarkDistributeRows_(target, sources) {
  var base = Math.floor(Number(target) / sources.length);
  var remainder = Number(target) % sources.length;
  return sources.map(function(source, index) {
    return { source: source, rows: base + (index < remainder ? 1 : 0) };
  });
}

function ttqsBenchmarkSyntheticCell_(header, columnIndex, globalIndex) {
  if (columnIndex === 0) return new Date(Date.UTC(2026, 0, 1, 0, 0, globalIndex));
  if (String(header) === 'TTQS_EVENT_ID') return 'BENCH-EVT-' + String(globalIndex + 1);
  var code = String(ttqsCanonicalFieldCode_(header));
  if (code === 'TTQS_ALIAS_CODE') return 'S-BENCH-' + String(globalIndex + 1);
  if (code === 'TTQS_SAMPLE_CONFIRM') return '我確認：本次只使用示範資料，不填寫真實個資';
  if (code === 'TTQS_NEED_TEXT') return '【壓測示範】希望增加更多實作練習';
  if (code === 'TTQS_REACTION_TEXT') return '【壓測示範】內容清楚，安全界線與實作方式容易理解';
  if (code === 'TTQS_30D_TEXT') return '【壓測示範】能依安全原則調整日常行為';
  if (code === 'TTQS_NEED_SCORE' || code.indexOf('TTQS_REACTION_') === 0 || code === 'TTQS_30D_SAFE_ACTION' || code === 'TTQS_30D_BOUNDARY') return 4;
  return 'SAMPLE_BENCHMARK';
}

function ttqsBenchmarkSeedSources_(ss, target) {
  var liveSources = ttqsObservationSourceDescriptors_().slice().sort(function(a, b) {
    return String(a.kind).localeCompare(String(b.kind));
  });
  if (liveSources.length !== 4) throw new Error('BENCHMARK_REQUIRES_EXACTLY_FOUR_SOURCES:' + liveSources.length);

  var sheetsById = {};
  ss.getSheets().forEach(function(sheet) { sheetsById[String(sheet.getSheetId())] = sheet; });
  var distributed = ttqsBenchmarkDistributeRows_(target, liveSources);
  var descriptors = [];
  var globalIndex = 0;

  distributed.forEach(function(item) {
    var live = sheetsById[String(item.source.sheetId)];
    if (!live) throw new Error('BENCHMARK_LIVE_SOURCE_MISSING:' + item.source.kind);
    var lastColumn = live.getLastColumn();
    var headers = live.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String);
    var name = TTQS_BENCHMARK_SOURCE_PREFIX + String(item.source.kind);
    var temp = ss.insertSheet(name);
    temp.getRange(1, 1, 1, headers.length).setValues([headers]);
    var rows = [];
    for (var i = 0; i < item.rows; i++) {
      var rowIndex = globalIndex++;
      rows.push(headers.map(function(header, columnIndex) {
        return ttqsBenchmarkSyntheticCell_(header, columnIndex, rowIndex);
      }));
    }
    if (rows.length) temp.getRange(2, 1, rows.length, headers.length).setValues(rows);
    descriptors.push({
      sheetId: temp.getSheetId(),
      kind: String(item.source.kind),
      formId: 'BENCHMARK_FORM_' + String(item.source.kind)
    });
  });

  var observation = ttqsEnsureStructuredSheet_(ss, TTQS_BENCHMARK_OBSERVATION_SHEET, ttqsObservationColumns_());
  SpreadsheetApp.flush();
  return { sources: descriptors, observationSheet: observation };
}

function ttqsBenchmarkScanSources_(ss, sources) {
  var sheetsById = {};
  ss.getSheets().forEach(function(sheet) { sheetsById[String(sheet.getSheetId())] = sheet; });
  var candidates = [];
  var rawCount = 0;
  var rangeReadCalls = 0;
  var sourceStats = [];
  sources.forEach(function(source) {
    var sheet = sheetsById[String(source.sheetId)];
    if (!sheet) throw new Error('BENCHMARK_SOURCE_SHEET_MISSING:' + source.sheetId);
    var lastRow = sheet.getLastRow();
    var lastColumn = sheet.getLastColumn();
    var rows = Math.max(0, lastRow - 1);
    rawCount += rows;
    if (rawCount > Number(ttqsConfig_().OBSERVATION_SCAN_MAX_ROWS)) throw new Error('BENCHMARK_SCAN_LIMIT_EXCEEDED:' + rawCount);
    if (!rows) {
      sourceStats.push({ kind: source.kind, sheet_id: String(source.sheetId), rows: 0, range_read_calls: 0 });
      return;
    }
    var headers = sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String);
    rangeReadCalls += 1;
    var dataRange = sheet.getRange(2, 1, rows, lastColumn);
    var valueRows = dataRange.getValues();
    var displayRows = dataRange.getDisplayValues();
    rangeReadCalls += 2;
    for (var i = 0; i < rows; i++) {
      candidates.push(ttqsObservationCandidateFromValues_(
        sheet.getSheetId(),
        i + 2,
        source.kind,
        source.formId,
        headers,
        displayRows[i],
        valueRows[i][0]
      ));
    }
    sourceStats.push({ kind: source.kind, sheet_id: String(source.sheetId), rows: rows, range_read_calls: 3 });
  });
  return {
    candidates: candidates,
    rawCount: rawCount,
    sourceCount: sources.length,
    readStrategy: 'BATCH_PER_SOURCE',
    rangeReadCalls: rangeReadCalls,
    sourceStats: sourceStats
  };
}

function ttqsBenchmarkApplyCandidates_(sheet, candidates) {
  var existing = ttqsReadObjects_(sheet);
  var byLocator = {};
  var bySourceKey = {};
  var patches = [];
  var pending = [];
  var stats = { inserted: 0, unchanged: 0, quarantined: 0, rawMutation: 0, sourceKeyCollision: 0 };
  function addMap(map, key, entry) { if (!map[key]) map[key] = []; map[key].push(entry); }
  function quarantineEntry(entry, code) {
    if (entry.pendingObject) {
      entry.pendingObject.processing_status = 'QUARANTINED';
      entry.pendingObject.last_error = code;
      return;
    }
    if (String(entry.object.processing_status) !== 'QUARANTINED' || String(entry.object.last_error) !== code) {
      patches.push({ rowNumber: entry.rowNumber, patch: { processing_status: 'QUARANTINED', last_error: code } });
    }
  }
  existing.forEach(function(entry) {
    addMap(byLocator, String(entry.object.source_locator), entry);
    addMap(bySourceKey, String(entry.object.source_key), entry);
  });
  candidates.forEach(function(candidate) {
    var locatorEntries = byLocator[String(candidate.source_locator)] || [];
    if (locatorEntries.length > 1) {
      locatorEntries.forEach(function(entry) { quarantineEntry(entry, 'DUPLICATE_SOURCE_LOCATOR'); });
      stats.quarantined += locatorEntries.length;
      return;
    }
    if (locatorEntries.length === 1) {
      var existingEntry = locatorEntries[0];
      if (String(existingEntry.object.source_key) !== String(candidate.source_key) || String(existingEntry.object.payload_hash) !== String(candidate.payload_hash)) {
        quarantineEntry(existingEntry, 'RAW_MUTATION_DETECTED');
        stats.rawMutation += 1;
        stats.quarantined += 1;
      } else {
        stats.unchanged += 1;
      }
      return;
    }
    var keyEntries = bySourceKey[String(candidate.source_key)] || [];
    if (keyEntries.length) {
      keyEntries.forEach(function(entry) { quarantineEntry(entry, 'SOURCE_KEY_COLLISION'); });
      candidate.processing_status = 'QUARANTINED';
      candidate.last_error = 'SOURCE_KEY_COLLISION';
      stats.sourceKeyCollision += 1;
      stats.quarantined += keyEntries.length + 1;
    } else if (candidate.processing_status === 'QUARANTINED') {
      stats.quarantined += 1;
    }
    pending.push(candidate);
    var pendingEntry = { pendingObject: candidate, object: candidate };
    addMap(byLocator, String(candidate.source_locator), pendingEntry);
    addMap(bySourceKey, String(candidate.source_key), pendingEntry);
  });
  patches.forEach(function(item) { ttqsUpdateObjectRow_(sheet, item.rowNumber, item.patch); });
  stats.inserted = ttqsObservationAppendBatch_(sheet, pending);
  SpreadsheetApp.flush();
  return stats;
}

function ttqsBenchmarkRawLocators_(ss, sources) {
  var sheetsById = {};
  ss.getSheets().forEach(function(sheet) { sheetsById[String(sheet.getSheetId())] = sheet; });
  var locators = {};
  sources.forEach(function(source) {
    var sheet = sheetsById[String(source.sheetId)];
    if (!sheet) throw new Error('BENCHMARK_SOURCE_SHEET_MISSING:' + source.sheetId);
    for (var rowNumber = 2; rowNumber <= sheet.getLastRow(); rowNumber++) {
      locators['SHEET:' + String(source.sheetId) + ':ROW:' + String(rowNumber)] = true;
    }
  });
  return locators;
}

function ttqsBenchmarkReconcile_(ss, sources, observationSheet) {
  var rawLocators = ttqsBenchmarkRawLocators_(ss, sources);
  var rows = ttqsReadObjects_(observationSheet);
  var locatorCounts = {};
  var acceptedBySourceKey = {};
  var quarantined = 0;
  rows.forEach(function(entry) {
    var locator = String(entry.object.source_locator || '');
    locatorCounts[locator] = Number(locatorCounts[locator] || 0) + 1;
    if (String(entry.object.processing_status) === 'ACCEPTED') {
      var key = String(entry.object.source_key || '');
      acceptedBySourceKey[key] = Number(acceptedBySourceKey[key] || 0) + 1;
    }
    if (String(entry.object.processing_status) === 'QUARANTINED') quarantined += 1;
  });
  var unexplained = Object.keys(rawLocators).filter(function(locator) { return !locatorCounts[locator]; }).length;
  var unknownInternal = Object.keys(locatorCounts).filter(function(locator) { return !rawLocators[locator]; }).length;
  var duplicateLocator = Object.keys(locatorCounts).filter(function(locator) { return locatorCounts[locator] > 1; }).length;
  var formalDuplicateAcceptance = Object.keys(acceptedBySourceKey).filter(function(key) { return acceptedBySourceKey[key] > 1; }).length;
  var structuralPass = unexplained === 0 && unknownInternal === 0 && duplicateLocator === 0 && formalDuplicateAcceptance === 0;
  return {
    status: structuralPass ? (quarantined > 0 ? 'PASS_WITH_QUARANTINE' : 'PASS') : 'FAIL',
    raw_count: Object.keys(rawLocators).length,
    observation_count: rows.length,
    unexplained: unexplained,
    unknown_internal: unknownInternal,
    duplicate_locator: duplicateLocator,
    formal_duplicate_acceptance: formalDuplicateAcceptance,
    quarantined: quarantined
  };
}

function ttqsBenchmarkPass_(target, scan, ingest, reconciliation, secondScan, secondIngest, secondReconciliation, observationRows) {
  return scan.sourceCount === 4 &&
    scan.rawCount === target &&
    scan.rangeReadCalls === 12 &&
    ingest.inserted === target &&
    ingest.unchanged === 0 &&
    ingest.quarantined === 0 &&
    ingest.rawMutation === 0 &&
    ingest.sourceKeyCollision === 0 &&
    reconciliation.status === 'PASS' &&
    reconciliation.raw_count === target &&
    reconciliation.observation_count === target &&
    reconciliation.unexplained === 0 &&
    reconciliation.unknown_internal === 0 &&
    reconciliation.duplicate_locator === 0 &&
    secondScan.rawCount === target &&
    secondIngest.inserted === 0 &&
    secondIngest.unchanged === target &&
    secondIngest.quarantined === 0 &&
    secondIngest.rawMutation === 0 &&
    secondIngest.sourceKeyCollision === 0 &&
    secondReconciliation.status === 'PASS' &&
    secondReconciliation.raw_count === target &&
    secondReconciliation.observation_count === target &&
    observationRows.length === target &&
    observationRows.every(function(entry) {
      return String(entry.object.processing_status) === 'PENDING' &&
        Number(entry.object.attempt_count || 0) === 0 &&
        String(entry.object.last_error || '') === '';
    });
}

function ttqsBenchmarkWriteResult_(ss, result) {
  ttqsAppendObject_(ttqsBenchmarkEnsureResultSheet_(ss), result);
}

function ttqsBenchmarkRunLevel_(target) {
  ttqsAssertTestOnly_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');
  if ([50, 200, 600].indexOf(Number(target)) === -1) throw new Error('BENCHMARK_TARGET_NOT_ALLOWED:' + target);

  var ss = ttqsOpenCore_();
  var preCleanup = ttqsBenchmarkCleanupTempSheets_(ss);
  if (preCleanup.status !== 'PASS') throw new Error('BENCHMARK_STALE_TEMP_CLEANUP_FAILED:' + preCleanup.errors.join('|'));

  var result = {
    run_id: ttqsStableId_('BENCH-', Utilities.getUuid(), 24),
    executed_at: '',
    source_version: ttqsConfig_().VERSION,
    target_rows: Number(target),
    source_count: 0,
    status: 'FAIL',
    seed_ms: 0,
    first_scan_ms: 0,
    first_ingest_ms: 0,
    first_reconcile_ms: 0,
    first_total_ms: 0,
    first_range_read_calls: 0,
    first_inserted: 0,
    first_unchanged: 0,
    first_quarantined: 0,
    first_raw_mutation: 0,
    first_collision: 0,
    first_reconciliation: '',
    second_scan_ms: 0,
    second_ingest_ms: 0,
    second_reconcile_ms: 0,
    second_total_ms: 0,
    second_inserted: 0,
    second_unchanged: 0,
    second_quarantined: 0,
    second_raw_mutation: 0,
    second_collision: 0,
    second_reconciliation: '',
    observation_count: 0,
    cleanup_status: 'NOT_RUN',
    error: ''
  };

  var thrown = null;
  try {
    var seedStart = Date.now();
    var seeded = ttqsBenchmarkSeedSources_(ss, Number(target));
    var seededAt = Date.now();
    result.seed_ms = seededAt - seedStart;
    result.source_count = seeded.sources.length;

    var firstStart = Date.now();
    var scan = ttqsBenchmarkScanSources_(ss, seeded.sources);
    var firstScannedAt = Date.now();
    var ingest = ttqsWithScriptLock_(function() {
      return ttqsBenchmarkApplyCandidates_(seeded.observationSheet, scan.candidates);
    });
    var firstIngestedAt = Date.now();
    var reconciliation = ttqsBenchmarkReconcile_(ss, seeded.sources, seeded.observationSheet);
    var firstReconciledAt = Date.now();

    result.first_scan_ms = firstScannedAt - firstStart;
    result.first_ingest_ms = firstIngestedAt - firstScannedAt;
    result.first_reconcile_ms = firstReconciledAt - firstIngestedAt;
    result.first_total_ms = firstReconciledAt - firstStart;
    result.first_range_read_calls = scan.rangeReadCalls;
    result.first_inserted = ingest.inserted;
    result.first_unchanged = ingest.unchanged;
    result.first_quarantined = ingest.quarantined;
    result.first_raw_mutation = ingest.rawMutation;
    result.first_collision = ingest.sourceKeyCollision;
    result.first_reconciliation = reconciliation.status;

    var secondStart = Date.now();
    var secondScan = ttqsBenchmarkScanSources_(ss, seeded.sources);
    var secondScannedAt = Date.now();
    var secondIngest = ttqsWithScriptLock_(function() {
      return ttqsBenchmarkApplyCandidates_(seeded.observationSheet, secondScan.candidates);
    });
    var secondIngestedAt = Date.now();
    var secondReconciliation = ttqsBenchmarkReconcile_(ss, seeded.sources, seeded.observationSheet);
    var secondReconciledAt = Date.now();

    result.second_scan_ms = secondScannedAt - secondStart;
    result.second_ingest_ms = secondIngestedAt - secondScannedAt;
    result.second_reconcile_ms = secondReconciledAt - secondIngestedAt;
    result.second_total_ms = secondReconciledAt - secondStart;
    result.second_inserted = secondIngest.inserted;
    result.second_unchanged = secondIngest.unchanged;
    result.second_quarantined = secondIngest.quarantined;
    result.second_raw_mutation = secondIngest.rawMutation;
    result.second_collision = secondIngest.sourceKeyCollision;
    result.second_reconciliation = secondReconciliation.status;

    var observationRows = ttqsReadObjects_(seeded.observationSheet);
    result.observation_count = observationRows.length;
    if (!ttqsBenchmarkPass_(Number(target), scan, ingest, reconciliation, secondScan, secondIngest, secondReconciliation, observationRows)) {
      throw new Error('BENCHMARK_GATE_FAIL:' + String(target));
    }
    result.status = 'PASS';
  } catch (err) {
    thrown = err;
    result.error = ttqsBenchmarkSafeError_(err);
  } finally {
    var cleanup = ttqsBenchmarkCleanupTempSheets_(ss);
    result.cleanup_status = cleanup.status;
    if (cleanup.status !== 'PASS') {
      var cleanupError = new Error('BENCHMARK_TEMP_CLEANUP_FAILED:' + cleanup.errors.join('|'));
      result.status = 'FAIL';
      result.error = [result.error, ttqsBenchmarkSafeError_(cleanupError)].filter(String).join('|').slice(0, 500);
      if (!thrown) thrown = cleanupError;
    }
    result.executed_at = ttqsNow_();
    ttqsBenchmarkWriteResult_(ss, result);
  }

  if (thrown) throw thrown;
  return result;
}

function ttqsBenchmarkObservationAll() {
  ttqsAssertTestOnly_();
  var targets = [50, 200, 600];
  var results = [];
  for (var i = 0; i < targets.length; i++) {
    var result = ttqsBenchmarkRunLevel_(targets[i]);
    results.push(result);
    if (result.status !== 'PASS') throw new Error('BENCHMARK_LEVEL_NOT_PASS:' + targets[i]);
  }
  return {
    mode: 'OBSERVATION_TEST_BENCHMARK',
    targets: targets,
    results: results,
    real_or_prod_touched: false,
    formal_raw_sheets_touched: false,
    formal_observation_touched: false
  };
}
