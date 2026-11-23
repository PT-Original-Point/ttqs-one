var TTQS_BENCHMARK_REPEATABILITY_SHEET = '99_TEST_Benchmark_重複性紀錄';
var TTQS_BENCHMARK_REPEATABILITY_REVISION = 'REPEATABILITY_V1';

function ttqsBenchmarkRepeatabilityColumns_() {
  return [
    { header: 'suite_id', description: 'Independent repeatability suite ID.' },
    { header: 'repeatability_revision', description: 'Repeatability harness revision.' },
    { header: 'source_fingerprint', description: 'SHA-256 fingerprint of the benchmark and production reconciliation code paths measured by this suite.' },
    { header: 'workload_kind', description: 'Always SYNTHETIC_TEST_SAMPLE; never REAL participant data.' },
    { header: 'target_rows', description: 'Synthetic raw rows for this independent run.' },
    { header: 'repeat_index', description: '1-based independent repeat index within this target.' },
    { header: 'repeat_total', description: 'Required independent run count for this target.' },
    { header: 'run_order', description: '1-based run order across the whole suite.' },
    { header: 'run_id', description: 'Underlying benchmark run ID from 99_TEST_Benchmark_效能紀錄.' },
    { header: 'executed_at', description: 'Underlying benchmark completion time in TEST timezone.' },
    { header: 'status', description: 'PASS only when the underlying independent run passes.' },
    { header: 'source_count', description: 'Synthetic source sheet count.' },
    { header: 'first_range_read_calls', description: 'First-pass provider range read calls.' },
    { header: 'first_scan_ms', description: 'First-pass scan time.' },
    { header: 'first_ingest_ms', description: 'First-pass ingest time.' },
    { header: 'first_reconcile_ms', description: 'First-pass reconciliation time.' },
    { header: 'first_total_ms', description: 'First-pass total time.' },
    { header: 'second_scan_ms', description: 'Idempotency-pass scan time.' },
    { header: 'second_ingest_ms', description: 'Idempotency-pass ingest time.' },
    { header: 'second_reconcile_ms', description: 'Idempotency-pass reconciliation time.' },
    { header: 'second_total_ms', description: 'Idempotency-pass total time.' },
    { header: 'first_inserted', description: 'Must equal target_rows.' },
    { header: 'second_inserted', description: 'Must equal 0.' },
    { header: 'second_unchanged', description: 'Must equal target_rows.' },
    { header: 'first_quarantined', description: 'Must equal 0.' },
    { header: 'second_quarantined', description: 'Must equal 0.' },
    { header: 'first_raw_mutation', description: 'Must equal 0.' },
    { header: 'second_raw_mutation', description: 'Must equal 0.' },
    { header: 'first_collision', description: 'Must equal 0.' },
    { header: 'second_collision', description: 'Must equal 0.' },
    { header: 'first_reconciliation', description: 'Must equal PASS.' },
    { header: 'second_reconciliation', description: 'Must equal PASS.' },
    { header: 'observation_count', description: 'Must equal target_rows.' },
    { header: 'cleanup_status', description: 'Must equal PASS.' },
    { header: 'error', description: 'Bounded TEST-only failure summary; empty on PASS.' }
  ];
}

function ttqsBenchmarkRepeatabilityEnsureSheet_(ss) {
  return ttqsEnsureStructuredSheet_(ss, TTQS_BENCHMARK_REPEATABILITY_SHEET, ttqsBenchmarkRepeatabilityColumns_());
}

function ttqsBenchmarkRepeatabilityPlan_() {
  return [
    { target: 200, runs: 3 },
    { target: 600, runs: 5 }
  ];
}

function ttqsBenchmarkRepeatabilitySourceFingerprint_() {
  return ttqsDigest_([
    String(ttqsObservationRawLocators_),
    String(ttqsBenchmarkRawLocators_),
    String(ttqsBenchmarkScanSources_),
    String(ttqsBenchmarkReconcile_),
    String(ttqsBenchmarkRunLevel_)
  ].join('\n---\n'));
}

function ttqsBenchmarkRepeatabilityWrite_(ss, record) {
  ttqsAppendObject_(ttqsBenchmarkRepeatabilityEnsureSheet_(ss), record);
}

function ttqsBenchmarkRepeatabilityRecord_(suiteId, fingerprint, target, repeatIndex, repeatTotal, runOrder, result) {
  return {
    suite_id: suiteId,
    repeatability_revision: TTQS_BENCHMARK_REPEATABILITY_REVISION,
    source_fingerprint: fingerprint,
    workload_kind: 'SYNTHETIC_TEST_SAMPLE',
    target_rows: Number(target),
    repeat_index: Number(repeatIndex),
    repeat_total: Number(repeatTotal),
    run_order: Number(runOrder),
    run_id: result ? String(result.run_id || '') : '',
    executed_at: result ? String(result.executed_at || '') : ttqsNow_(),
    status: result ? String(result.status || 'FAIL') : 'FAIL',
    source_count: result ? Number(result.source_count || 0) : 0,
    first_range_read_calls: result ? Number(result.first_range_read_calls || 0) : 0,
    first_scan_ms: result ? Number(result.first_scan_ms || 0) : 0,
    first_ingest_ms: result ? Number(result.first_ingest_ms || 0) : 0,
    first_reconcile_ms: result ? Number(result.first_reconcile_ms || 0) : 0,
    first_total_ms: result ? Number(result.first_total_ms || 0) : 0,
    second_scan_ms: result ? Number(result.second_scan_ms || 0) : 0,
    second_ingest_ms: result ? Number(result.second_ingest_ms || 0) : 0,
    second_reconcile_ms: result ? Number(result.second_reconcile_ms || 0) : 0,
    second_total_ms: result ? Number(result.second_total_ms || 0) : 0,
    first_inserted: result ? Number(result.first_inserted || 0) : 0,
    second_inserted: result ? Number(result.second_inserted || 0) : 0,
    second_unchanged: result ? Number(result.second_unchanged || 0) : 0,
    first_quarantined: result ? Number(result.first_quarantined || 0) : 0,
    second_quarantined: result ? Number(result.second_quarantined || 0) : 0,
    first_raw_mutation: result ? Number(result.first_raw_mutation || 0) : 0,
    second_raw_mutation: result ? Number(result.second_raw_mutation || 0) : 0,
    first_collision: result ? Number(result.first_collision || 0) : 0,
    second_collision: result ? Number(result.second_collision || 0) : 0,
    first_reconciliation: result ? String(result.first_reconciliation || '') : '',
    second_reconciliation: result ? String(result.second_reconciliation || '') : '',
    observation_count: result ? Number(result.observation_count || 0) : 0,
    cleanup_status: result ? String(result.cleanup_status || '') : '',
    error: result ? String(result.error || '') : ''
  };
}

function ttqsBenchmarkObservationRepeatability() {
  ttqsAssertTestOnly_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');

  var ss = ttqsOpenCore_();
  var preCleanup = ttqsBenchmarkCleanupTempSheets_(ss);
  if (preCleanup.status !== 'PASS') throw new Error('REPEATABILITY_STALE_TEMP_CLEANUP_FAILED:' + preCleanup.errors.join('|'));

  var suiteId = ttqsStableId_('BENCHSUITE-', Utilities.getUuid(), 24);
  var fingerprint = ttqsBenchmarkRepeatabilitySourceFingerprint_();
  var plan = ttqsBenchmarkRepeatabilityPlan_();
  var records = [];
  var runOrder = 0;

  try {
    for (var p = 0; p < plan.length; p++) {
      var target = Number(plan[p].target);
      var repeatTotal = Number(plan[p].runs);
      for (var repeatIndex = 1; repeatIndex <= repeatTotal; repeatIndex++) {
        runOrder += 1;
        var result = null;
        try {
          result = ttqsBenchmarkRunLevel_(target);
          var record = ttqsBenchmarkRepeatabilityRecord_(suiteId, fingerprint, target, repeatIndex, repeatTotal, runOrder, result);
          ttqsBenchmarkRepeatabilityWrite_(ss, record);
          records.push(record);
          if (record.status !== 'PASS' || record.cleanup_status !== 'PASS') {
            throw new Error('REPEATABILITY_RUN_NOT_PASS:' + target + ':' + repeatIndex);
          }
        } catch (err) {
          if (!result) {
            var failed = ttqsBenchmarkRepeatabilityRecord_(suiteId, fingerprint, target, repeatIndex, repeatTotal, runOrder, null);
            failed.error = ttqsBenchmarkSafeError_(err);
            ttqsBenchmarkRepeatabilityWrite_(ss, failed);
          }
          throw err;
        }
      }
    }
  } catch (err) {
    var failureCleanup = ttqsBenchmarkCleanupTempSheets_(ss);
    if (failureCleanup.status !== 'PASS') {
      throw new Error('REPEATABILITY_FAILURE_AND_CLEANUP_FAILED:' + ttqsBenchmarkSafeError_(err) + '|' + failureCleanup.errors.join('|'));
    }
    throw err;
  }

  var finalCleanup = ttqsBenchmarkCleanupTempSheets_(ss);
  if (finalCleanup.status !== 'PASS') throw new Error('REPEATABILITY_FINAL_CLEANUP_FAILED:' + finalCleanup.errors.join('|'));

  return {
    mode: 'OBSERVATION_TEST_BENCHMARK_REPEATABILITY',
    suite_id: suiteId,
    repeatability_revision: TTQS_BENCHMARK_REPEATABILITY_REVISION,
    source_fingerprint: fingerprint,
    workload_kind: 'SYNTHETIC_TEST_SAMPLE',
    plan: plan,
    independent_runs: records.length,
    results: records,
    real_or_prod_touched: false,
    formal_raw_sheets_touched: false,
    formal_observation_touched: false
  };
}
