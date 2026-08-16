import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const s3 = fs.readFileSync('apps-script/S3Foundation.gs', 'utf8');
const formRouter = fs.readFileSync('apps-script/FormRouter.gs', 'utf8');
const retry = fs.readFileSync('apps-script/Retry.gs', 'utf8');
const reconcile = fs.readFileSync('apps-script/Reconcile.gs', 'utf8');
const orchestrator = fs.readFileSync('apps-script/SchedulerOrchestrator.gs', 'utf8');

function load(source, extra = {}) {
  const context = { isFinite };
  vm.createContext(context);
  vm.runInContext(source, context);
  Object.assign(context, extra);
  return context;
}

function plain(value) {
  return JSON.parse(JSON.stringify(value));
}

test('S3 runtime wiring sources parse', () => {
  for (const [name, source] of Object.entries({ s3, formRouter, retry, reconcile, orchestrator })) {
    new vm.Script(source, { filename: name });
  }
});

test('FormRouter preserves legacy trigger semantics and records scheduler Observation provenance', () => {
  let captured;
  const context = load(formRouter, {
    ttqsAssertTestOnly_: () => true,
    ttqsS3JobNotesFromRaw_: () => ({ observationSourceKey: 'SOURCE-KEY', marker: 'S3' }),
    ttqsLedgerEnsure_: (spec) => {
      captured = spec;
      return { object: { status: 'SUCCESS', job_id: 'JOB-1', trace_id: 'TRACE-1' } };
    },
    ttqsImmediateReconcile_: () => ({ status: 'MATCHED_EXACTLY_ONCE' })
  });

  const schedulerRaw = {
    kind: 'NEEDS', eventId: 'EVT-OBS-1', rawRef: 'FORM_SUITE:F:EVT-OBS-1', rawFingerprint: 'fp', formId: 'F', sheetId: 10, rowNumber: 2,
    triggerSource: 'SCHEDULER_OBSERVATION', observationProvenance: { observationSourceKey: 'SOURCE-KEY' }
  };
  const schedulerResult = plain(context.ttqsHandleRawObjectUnlocked_(schedulerRaw, false));
  assert.equal(captured.triggerSource, 'SCHEDULER_OBSERVATION');
  assert.equal(captured.notes.observationSourceKey, 'SOURCE-KEY');
  assert.equal(captured.notes.marker, 'S3');
  assert.equal(schedulerResult.duplicate, true);

  const legacyRaw = {
    kind: 'NEEDS', eventId: 'EVT-LEGACY', rawRef: 'FORM_SUITE:F:EVT-LEGACY', rawFingerprint: 'legacy-fp', formId: 'F', sheetId: 10, rowNumber: 3
  };
  context.ttqsHandleRawObjectUnlocked_(legacyRaw, false);
  assert.equal(captured.triggerSource, 'GOOGLE_FORM');
  assert.equal(captured.notes.rawRef, legacyRaw.rawRef);
  assert.equal(Object.hasOwn(captured.notes, 'observationSourceKey'), false);
});

test('dual-run existing SUCCESS job is linked without invoking business creation path', () => {
  let handlerCalls = 0;
  let reconciliationCalls = 0;
  const context = load(s3, {
    ttqsAssertTestOnly_: () => true,
    ttqsS3ResolveObservationRaw_: () => ({ rawRef: 'FORM_SUITE:F:EVT-1' }),
    ttqsS3ObservationJobByRaw_: () => ({ object: { status: 'SUCCESS', job_id: 'JOB-1' } }),
    ttqsImmediateReconcile_: () => { reconciliationCalls += 1; return { status: 'MATCHED_EXACTLY_ONCE' }; },
    ttqsS3AcceptObservation_: (_entry, _raw, jobId, disposition, attemptCount) => ({ status: 'ACCEPTED', jobId, disposition, attemptCount }),
    ttqsHandleRawObjectUnlocked_: () => { handlerCalls += 1; throw new Error('must not create duplicate business objects'); }
  });
  const entry = { rowNumber: 3, object: { attempt_count: 0, processing_status: 'PENDING' } };
  const result = plain(context.ttqsS3ProcessObservationEntryUnlocked_(entry));
  assert.equal(result.status, 'ACCEPTED');
  assert.equal(result.disposition, 'LINKED_EXISTING');
  assert.equal(result.attemptCount, 1);
  assert.equal(handlerCalls, 0, 'existing finalized job must not re-enter business creation');
  assert.equal(reconciliationCalls, 1);
});

test('existing FAILED job is deferred to the one-minute retry worker instead of being retried by Observation', () => {
  let handlerCalls = 0;
  let patch;
  const context = load(s3, {
    ttqsAssertTestOnly_: () => true,
    ttqsS3ResolveObservationRaw_: () => ({ rawRef: 'FORM_SUITE:F:EVT-1' }),
    ttqsS3ObservationJobByRaw_: () => ({ object: { status: 'FAILED', job_id: 'JOB-1', retry_at: '2026-08-16T23:30:00+0800' } }),
    ttqsS3PatchObservation_: (_entry, value) => { patch = value; },
    ttqsHandleRawObjectUnlocked_: () => { handlerCalls += 1; }
  });
  const entry = { rowNumber: 3, object: { attempt_count: 1, processing_status: 'PENDING' } };
  const result = plain(context.ttqsS3ProcessObservationEntryUnlocked_(entry));
  assert.equal(result.status, 'DEFERRED');
  assert.equal(result.jobStatus, 'FAILED');
  assert.equal(handlerCalls, 0);
  assert.equal(patch.processing_status, 'PENDING');
  assert.equal(patch.attempt_count, 1, 'Observation must not consume a business attempt while retry owns recovery');
  assert.equal(patch.next_retry_at, '2026-08-16T23:30:00+0800');
});

test('source identity mismatch quarantines Observation before business processing', () => {
  let handlerCalls = 0;
  let patch;
  const context = load(s3, {
    ttqsAssertTestOnly_: () => true,
    ttqsS3ResolveObservationRaw_: () => { throw new Error('S3_OBSERVATION_PAYLOAD_HASH_MISMATCH'); },
    ttqsS3PatchObservation_: (_entry, value) => { patch = value; },
    ttqsHandleRawObjectUnlocked_: () => { handlerCalls += 1; }
  });
  const entry = { rowNumber: 3, object: { attempt_count: 0, processing_status: 'PENDING' } };
  const result = plain(context.ttqsS3ProcessObservationEntryUnlocked_(entry));
  assert.equal(result.status, 'QUARANTINED');
  assert.equal(handlerCalls, 0);
  assert.equal(patch.processing_status, 'QUARANTINED');
  assert.equal(patch.disposition, 'SOURCE_INTEGRITY_BLOCKED');
});

test('new scheduler-origin Observation delegates exactly once to existing business handler', () => {
  let handlerCalls = 0;
  const raw = { rawRef: 'FORM_SUITE:F:EVT-OBS-1', triggerSource: 'SCHEDULER_OBSERVATION' };
  const context = load(s3, {
    ttqsAssertTestOnly_: () => true,
    ttqsS3ResolveObservationRaw_: () => raw,
    ttqsS3ObservationJobByRaw_: () => null,
    ttqsHandleRawObjectUnlocked_: (received, isRetry) => {
      handlerCalls += 1;
      assert.equal(received, raw);
      assert.equal(isRetry, false);
      return { duplicate: false, jobId: 'JOB-NEW', reconciliationStatus: 'MATCHED_EXACTLY_ONCE' };
    },
    ttqsS3AcceptObservation_: (_entry, _raw, jobId, disposition, attemptCount) => ({ status: 'ACCEPTED', jobId, disposition, attemptCount })
  });
  const entry = { rowNumber: 3, object: { attempt_count: 0, processing_status: 'PENDING' } };
  const result = plain(context.ttqsS3ProcessObservationEntryUnlocked_(entry));
  assert.equal(handlerCalls, 1);
  assert.equal(result.status, 'ACCEPTED');
  assert.equal(result.disposition, 'SCHEDULER_PROCESSED');
  assert.equal(result.attemptCount, 1);
});

test('Observation cycle performs shadow ingest, bounded worker, then post-processing reconciliation', () => {
  const context = load(s3, {
    ttqsAssertTestOnly_: () => true,
    ttqsScheduler: () => ({ sources: 4, raw_rows_scanned: 12, ingest: { unchanged: 12 }, reconciliation: { status: 'PASS' }, timings_ms: { total: 10 } }),
    ttqsWithScriptLock_: (fn) => fn(),
    ttqsS3ProcessPendingObservationsUnlocked_: () => ({ selected: 12, accepted: 12, linked_existing: 12, scheduler_processed: 0, deferred: 0, quarantined: 0, rejected: 0 }),
    ttqsObservationReconcileShadow_: () => ({ status: 'PASS', observation_count: 12 })
  });
  const result = plain(context.ttqsS3ObservationCycle());
  assert.equal(result.mode, 'OBSERVATION_S3_DUAL_RUN');
  assert.equal(result.processing.accepted, 12);
  assert.equal(result.processing.linked_existing, 12);
  assert.equal(result.reconciliation.status, 'PASS');
  assert.equal(result.legacy_processing_unchanged, false);
});

test('runtime wiring uses unified retry/reconcile resolvers and keeps provider writes out of S3 path', () => {
  assert.match(retry, /var raw = ttqsS3ResolveRetryRaw_\(job\)/);
  assert.doesNotMatch(retry, /var raw = ttqsFindRawSubmissionByRef_/);
  assert.match(reconcile, /ttqsS3ResolveUnifiedRawBySheetRow_\(Number\(sheetId\), rowNumber\)/);
  assert.match(reconcile, /MISMATCH_SOURCE_PROVENANCE/);
  assert.match(orchestrator, /OBSERVATION'\) return ttqsS3ObservationCycle\(\)/);
  assert.match(orchestrator, /processing_linked_existing/);
  assert.match(orchestrator, /processing_scheduler_processed/);
  assert.match(orchestrator, /processing_quarantined/);
  assert.match(orchestrator, /processing_rejected/);
  assert.match(s3, /TTQS_S3_OBSERVATION_BATCH_LIMIT = 50/);
  assert.match(s3, /ttqsRawSubmission_\(locator\.sheetId, locator\.rowNumber, false\)/);
  assert.doesNotMatch(s3, /ttqsRawSubmission_\([^\n]*, true\)/);
  assert.doesNotMatch(s3, /ttqsEnsureEventId_|\.setValue\(|\.setValues\(|\.appendRow\(/);
});

test('hourly reconciliation converts source-resolution failure into an explicit mismatch instead of engine exception', () => {
  const sheet = { getLastRow: () => 2 };
  const context = load(reconcile, {
    ttqsAssertTestOnly_: () => true,
    ttqsOpenCore_: () => ({}),
    ttqsParseJson_: () => ({ 101: 'NEEDS' }),
    PropertiesService: { getScriptProperties: () => ({ getProperty: () => '{}' }) },
    ttqsFindSheetById_: () => sheet,
    ttqsS3ResolveUnifiedRawBySheetRow_: () => { throw new Error('S3_OBSERVATION_PROVENANCE_REQUIRED:SHEET:101:ROW:2'); },
    ttqsReconciliationWatchdog_: () => ({ status: 'PASS' })
  });
  const result = plain(context.ttqsReconcileUnlocked_());
  assert.equal(result.status, 'FAIL');
  assert.equal(result.matched, 0);
  assert.equal(result.mismatched, 1);
  assert.equal(result.details[0].status, 'MISMATCH_SOURCE_PROVENANCE');
});
