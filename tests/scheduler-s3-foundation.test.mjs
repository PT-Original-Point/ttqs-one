import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const source = fs.readFileSync('apps-script/S3Foundation.gs', 'utf8');

function stableId(prefix, value, length = 16) {
  return prefix + crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, length).toUpperCase();
}

function baseContext() {
  const context = {
    isFinite,
    ttqsAssertTestOnly_: () => true,
    ttqsStableId_: stableId,
    ttqsParseJson_: (value, fallback) => {
      try { return value ? JSON.parse(value) : fallback; } catch { return fallback; }
    }
  };
  vm.createContext(context);
  vm.runInContext(source, context);
  return context;
}

test('S3 foundation source parses', () => {
  new vm.Script(source, { filename: 'S3Foundation.gs' });
});

test('source locator parser is fail-closed and round-trips valid provider locators', () => {
  const context = baseContext();
  assert.deepEqual(JSON.parse(JSON.stringify(context.ttqsS3ParseSourceLocator_('SHEET:1407831401:ROW:5'))), {
    sheetId: 1407831401,
    rowNumber: 5
  });
  assert.equal(context.ttqsS3ObservationLocator_(1407831401, 5), 'SHEET:1407831401:ROW:5');
  assert.throws(() => context.ttqsS3ParseSourceLocator_('ROW:5'), /S3_OBSERVATION_SOURCE_LOCATOR_INVALID/);
  assert.throws(() => context.ttqsS3ParseSourceLocator_('SHEET:1:ROW:1'), /S3_OBSERVATION_SOURCE_LOCATOR_RANGE_INVALID/);
});

test('scheduler-origin identity is deterministic and independent of provider row writes', () => {
  const context = baseContext();
  const sourceKey = 'ab'.repeat(32);
  const a = context.ttqsS3ObservationEventId_(sourceKey);
  const b = context.ttqsS3ObservationEventId_(sourceKey.toUpperCase());
  assert.equal(a, b);
  assert.match(a, /^EVT-OBS-[0-9A-F]{24}$/);
  assert.throws(() => context.ttqsS3ObservationEventId_('not-a-sha256'), /S3_OBSERVATION_SOURCE_KEY_INVALID/);
});

test('observation raw resolver is provider-read-only and validates source identity before business use', () => {
  assert.match(source, /ttqsObservationCandidateFromRow_\(sheet, locator\.rowNumber, kind, formId\)/);
  assert.match(source, /ttqsS3AssertObservationIdentity_\(observation, candidate, locator\)/);
  assert.match(source, /ttqsRawSubmission_\(locator\.sheetId, locator\.rowNumber, false\)/);
  const resolverStart = source.indexOf('function ttqsS3ResolveObservationRaw_');
  const resolverEnd = source.indexOf('function ttqsS3ResolveUnifiedRawBySheetRow_');
  const resolver = source.slice(resolverStart, resolverEnd);
  assert.doesNotMatch(resolver, /ttqsEnsureEventId_|setValue\(|setValues\(|appendRow\(/);
});

test('legacy provider event ID is preserved while scheduler-origin rows receive deterministic internal identity', () => {
  const sourceKey = '12'.repeat(32);
  const observation = {
    observation_id: 'OBS-1',
    source_type: 'GOOGLE_FORM_SHEET',
    source_kind: 'REGISTRATION',
    source_form_id: 'FORM-1',
    source_sheet_id: '101',
    source_locator: 'SHEET:101:ROW:2',
    provider_timestamp: '2026-08-16T00:00:00.000Z',
    payload_hash: '34'.repeat(32),
    source_key: sourceKey,
    processing_status: 'PENDING'
  };

  function contextWithProvider(eventId) {
    const context = baseContext();
    const sheet = { getSheetId: () => 101 };
    context.ttqsOpenCore_ = () => ({ getSheets: () => [sheet] });
    context.PropertiesService = { getScriptProperties: () => ({ getProperty: () => JSON.stringify({ 101: 'REGISTRATION' }) }) };
    context.ttqsFormIdForKind_ = () => 'FORM-1';
    context.ttqsObservationCandidateFromRow_ = () => ({
      source_type: 'GOOGLE_FORM_SHEET',
      source_kind: 'REGISTRATION',
      source_form_id: 'FORM-1',
      source_sheet_id: '101',
      source_locator: 'SHEET:101:ROW:2',
      provider_timestamp: observation.provider_timestamp,
      payload_hash: observation.payload_hash,
      source_key: observation.source_key
    });
    context.ttqsRawSubmission_ = () => ({
      kind: 'REGISTRATION',
      formId: 'FORM-1',
      sheetId: 101,
      rowNumber: 2,
      eventId,
      rawRef: eventId ? `FORM_SUITE:FORM-1:${eventId}` : '',
      rawFingerprint: 'fingerprint',
      named: { TTQS_ALIAS_CODE: 'S-L01' }
    });
    return context;
  }

  const legacy = contextWithProvider('EVT-LEGACY').ttqsS3ResolveObservationRaw_(observation);
  assert.equal(legacy.eventId, 'EVT-LEGACY');
  assert.equal(legacy.rawRef, 'FORM_SUITE:FORM-1:EVT-LEGACY');
  assert.equal(legacy.observationIdentityMode, 'LEGACY_EVENT_ID');
  assert.equal(legacy.providerEventIdPresent, true);

  const scheduler = contextWithProvider('').ttqsS3ResolveObservationRaw_(observation);
  assert.equal(scheduler.eventId, stableId('EVT-OBS-', sourceKey, 24));
  assert.equal(scheduler.rawRef, `FORM_SUITE:FORM-1:${scheduler.eventId}`);
  assert.equal(scheduler.observationIdentityMode, 'OBSERVATION_SOURCE_KEY');
  assert.equal(scheduler.providerEventIdPresent, false);
  assert.equal(scheduler.triggerSource, 'SCHEDULER_OBSERVATION');
  assert.equal(scheduler.observationProvenance.observationSourceKey, sourceKey);
});

test('resolver fails closed when indexed observation no longer matches provider content', () => {
  const context = baseContext();
  const sheet = { getSheetId: () => 101 };
  context.ttqsOpenCore_ = () => ({ getSheets: () => [sheet] });
  context.PropertiesService = { getScriptProperties: () => ({ getProperty: () => JSON.stringify({ 101: 'NEEDS' }) }) };
  context.ttqsFormIdForKind_ = () => 'FORM-1';
  context.ttqsObservationCandidateFromRow_ = () => ({
    source_kind: 'NEEDS',
    source_form_id: 'FORM-1',
    provider_timestamp: '2026-08-16T00:00:00.000Z',
    payload_hash: 'ff'.repeat(32),
    source_key: 'aa'.repeat(32)
  });
  context.ttqsRawSubmission_ = () => { throw new Error('raw read must occur only after identity validation'); };
  const observation = {
    source_type: 'GOOGLE_FORM_SHEET',
    source_kind: 'NEEDS',
    source_form_id: 'FORM-1',
    source_sheet_id: '101',
    source_locator: 'SHEET:101:ROW:2',
    provider_timestamp: '2026-08-16T00:00:00.000Z',
    payload_hash: '00'.repeat(32),
    source_key: 'aa'.repeat(32),
    processing_status: 'PENDING'
  };
  assert.throws(() => context.ttqsS3ResolveObservationRaw_(observation), /S3_OBSERVATION_PAYLOAD_HASH_MISMATCH/);
});

test('retry resolver prefers Observation provenance and preserves legacy fallback', () => {
  const context = baseContext();
  context.ttqsS3ObservationEntryBySourceKey_ = (key) => ({ object: { source_key: key } });
  context.ttqsS3ResolveObservationRaw_ = (entry) => ({ rawRef: `OBS:${entry.object.source_key}` });
  context.ttqsFindRawSubmissionByRef_ = (sheetId, rawRef) => ({ sheetId, rawRef });

  const observationJob = { object: { notes: JSON.stringify({ observationSourceKey: 'ab'.repeat(32) }) } };
  assert.equal(context.ttqsS3ResolveRetryRaw_(observationJob).rawRef, `OBS:${'ab'.repeat(32)}`);

  const legacyJob = { object: { notes: JSON.stringify({ sheetId: 101, rawRef: 'FORM_SUITE:FORM-1:EVT-1' }) } };
  assert.deepEqual(JSON.parse(JSON.stringify(context.ttqsS3ResolveRetryRaw_(legacyJob))), {
    sheetId: 101,
    rawRef: 'FORM_SUITE:FORM-1:EVT-1'
  });
});

test('ledger provenance helper carries bounded non-PII Observation identity fields', () => {
  const context = baseContext();
  const notes = context.ttqsS3JobNotesFromRaw_({
    kind: 'NEEDS', rawRef: 'FORM_SUITE:FORM-1:EVT-1', rawFingerprint: 'fp', formId: 'FORM-1', sheetId: 101, eventId: 'EVT-1', rowNumber: 2,
    observationIdentityMode: 'OBSERVATION_SOURCE_KEY',
    observationProvenance: {
      observationId: 'OBS-1',
      observationSourceKey: 'ab'.repeat(32),
      observationSourceLocator: 'SHEET:101:ROW:2',
      observationPayloadHash: 'cd'.repeat(32),
      observationProviderTimestamp: '2026-08-16T00:00:00.000Z'
    }
  });
  assert.equal(notes.observationId, 'OBS-1');
  assert.equal(notes.observationIdentityMode, 'OBSERVATION_SOURCE_KEY');
  assert.equal(notes.observationSourceLocator, 'SHEET:101:ROW:2');
  assert.equal(notes.originalRowNumber, 2);
});
