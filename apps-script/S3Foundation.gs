var TTQS_S3_OBSERVATION_TRIGGER_SOURCE = 'SCHEDULER_OBSERVATION';
var TTQS_S3_SYNTHETIC_EVENT_PREFIX = 'EVT-OBS-';

function ttqsS3ParseSourceLocator_(locator) {
  var match = /^SHEET:(\d+):ROW:(\d+)$/.exec(String(locator || ''));
  if (!match) throw new Error('S3_OBSERVATION_SOURCE_LOCATOR_INVALID:' + String(locator || ''));
  var sheetId = Number(match[1]);
  var rowNumber = Number(match[2]);
  if (!isFinite(sheetId) || sheetId <= 0 || !isFinite(rowNumber) || rowNumber < 2) {
    throw new Error('S3_OBSERVATION_SOURCE_LOCATOR_RANGE_INVALID:' + String(locator || ''));
  }
  return { sheetId: sheetId, rowNumber: rowNumber };
}

function ttqsS3ObservationEventId_(sourceKey) {
  var key = String(sourceKey || '').trim();
  if (!/^[0-9a-f]{64}$/i.test(key)) throw new Error('S3_OBSERVATION_SOURCE_KEY_INVALID');
  return ttqsStableId_(TTQS_S3_SYNTHETIC_EVENT_PREFIX, key.toLowerCase(), 24);
}

function ttqsS3ObservationLocator_(sheetId, rowNumber) {
  return 'SHEET:' + String(Number(sheetId)) + ':ROW:' + String(Number(rowNumber));
}

function ttqsS3ObservationEntryBySourceKey_(sourceKey) {
  var key = String(sourceKey || '').trim();
  if (!key) throw new Error('S3_OBSERVATION_SOURCE_KEY_REQUIRED');
  return ttqsFindUniqueRowByValue_(ttqsEnsureObservationSheet_(), 'source_key', key, 'S3_DUPLICATE_OBSERVATION_SOURCE_KEY');
}

function ttqsS3ObservationEntryByLocator_(sheetId, rowNumber) {
  var locator = ttqsS3ObservationLocator_(sheetId, rowNumber);
  return ttqsFindUniqueRowByValue_(ttqsEnsureObservationSheet_(), 'source_locator', locator, 'S3_DUPLICATE_OBSERVATION_SOURCE_LOCATOR');
}

function ttqsS3ObservationProvenance_(observation) {
  return {
    observationId: String(observation.observation_id || ''),
    observationSourceKey: String(observation.source_key || ''),
    observationSourceLocator: String(observation.source_locator || ''),
    observationPayloadHash: String(observation.payload_hash || ''),
    observationProviderTimestamp: String(observation.provider_timestamp || ''),
    observationIdentityMode: String(observation.observation_identity_mode || '')
  };
}

function ttqsS3AssertObservationIdentity_(observation, candidate, locator) {
  if (String(observation.source_type || '') !== 'GOOGLE_FORM_SHEET') throw new Error('S3_OBSERVATION_SOURCE_TYPE_INVALID');
  if (String(observation.source_locator || '') !== ttqsS3ObservationLocator_(locator.sheetId, locator.rowNumber)) {
    throw new Error('S3_OBSERVATION_SOURCE_LOCATOR_MISMATCH');
  }
  if (String(observation.source_sheet_id || '') !== String(locator.sheetId)) throw new Error('S3_OBSERVATION_SOURCE_SHEET_MISMATCH');
  if (String(observation.source_kind || '') !== String(candidate.source_kind || '')) throw new Error('S3_OBSERVATION_SOURCE_KIND_MISMATCH');
  if (String(observation.source_form_id || '') !== String(candidate.source_form_id || '')) throw new Error('S3_OBSERVATION_SOURCE_FORM_MISMATCH');
  if (String(observation.provider_timestamp || '') !== String(candidate.provider_timestamp || '')) throw new Error('S3_OBSERVATION_PROVIDER_TIMESTAMP_MISMATCH');
  if (String(observation.payload_hash || '') !== String(candidate.payload_hash || '')) throw new Error('S3_OBSERVATION_PAYLOAD_HASH_MISMATCH');
  if (String(observation.source_key || '') !== String(candidate.source_key || '')) throw new Error('S3_OBSERVATION_SOURCE_KEY_MISMATCH');
  return true;
}

function ttqsS3ResolveObservationRaw_(entryOrObservation) {
  ttqsAssertTestOnly_();
  var observation = entryOrObservation && entryOrObservation.object ? entryOrObservation.object : entryOrObservation;
  if (!observation) throw new Error('S3_OBSERVATION_REQUIRED');
  if (String(observation.processing_status || '') === 'QUARANTINED' || String(observation.processing_status || '') === 'REJECTED') {
    throw new Error('S3_OBSERVATION_NOT_PROCESSABLE:' + String(observation.processing_status || ''));
  }

  var locator = ttqsS3ParseSourceLocator_(observation.source_locator);
  if (String(observation.source_sheet_id || '') !== String(locator.sheetId)) throw new Error('S3_OBSERVATION_SOURCE_SHEET_MISMATCH');

  var ss = ttqsOpenCore_();
  var sheet = ss.getSheets().filter(function(item) { return Number(item.getSheetId()) === Number(locator.sheetId); })[0];
  if (!sheet) throw new Error('S3_OBSERVATION_SOURCE_SHEET_MISSING:' + locator.sheetId);

  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), {});
  var kind = String(map[String(locator.sheetId)] || '');
  if (!kind) throw new Error('S3_OBSERVATION_SOURCE_SHEET_UNMAPPED:' + locator.sheetId);
  var formId = ttqsFormIdForKind_(kind);
  var candidate = ttqsObservationCandidateFromRow_(sheet, locator.rowNumber, kind, formId);
  ttqsS3AssertObservationIdentity_(observation, candidate, locator);

  // Strictly read-only: false forbids TTQS_EVENT_ID creation/write on the provider row.
  var raw = ttqsRawSubmission_(locator.sheetId, locator.rowNumber, false);
  var legacyEventId = String(raw.eventId || '').trim();
  var eventId = legacyEventId || ttqsS3ObservationEventId_(observation.source_key);
  var identityMode = legacyEventId ? 'LEGACY_EVENT_ID' : 'OBSERVATION_SOURCE_KEY';
  var rawRef = 'FORM_SUITE:' + String(raw.formId) + ':' + eventId;
  var provenance = ttqsS3ObservationProvenance_(Object.assign({}, observation, { observation_identity_mode: identityMode }));

  return Object.assign({}, raw, {
    eventId: eventId,
    rawRef: rawRef,
    triggerSource: TTQS_S3_OBSERVATION_TRIGGER_SOURCE,
    observationProvenance: provenance,
    observationIdentityMode: identityMode,
    providerEventIdPresent: !!legacyEventId
  });
}

function ttqsS3ResolveUnifiedRawBySheetRow_(sheetId, rowNumber) {
  ttqsAssertTestOnly_();
  var raw = ttqsRawSubmission_(Number(sheetId), Number(rowNumber), false);
  if (raw.eventId && raw.rawRef) {
    return Object.assign({}, raw, {
      observationIdentityMode: 'LEGACY_EVENT_ID',
      providerEventIdPresent: true
    });
  }
  var entry = ttqsS3ObservationEntryByLocator_(sheetId, rowNumber);
  if (!entry) throw new Error('S3_OBSERVATION_PROVENANCE_REQUIRED:' + ttqsS3ObservationLocator_(sheetId, rowNumber));
  return ttqsS3ResolveObservationRaw_(entry);
}

function ttqsS3ResolveRetryRaw_(job) {
  ttqsAssertTestOnly_();
  if (!job || !job.object) throw new Error('S3_RETRY_JOB_REQUIRED');
  var notes = ttqsParseJson_(job.object.notes, {});
  var sourceKey = String(notes.observationSourceKey || '').trim();
  if (sourceKey) {
    var entry = ttqsS3ObservationEntryBySourceKey_(sourceKey);
    if (!entry) throw new Error('S3_RETRY_OBSERVATION_NOT_FOUND:' + sourceKey);
    return ttqsS3ResolveObservationRaw_(entry);
  }
  if (!notes.rawRef || notes.sheetId === undefined || notes.sheetId === null) throw new Error('FORM_SUITE_RETRY_PROVENANCE_MISSING');
  return ttqsFindRawSubmissionByRef_(Number(notes.sheetId), String(notes.rawRef));
}

function ttqsS3JobNotesFromRaw_(raw) {
  var provenance = raw && raw.observationProvenance ? raw.observationProvenance : {};
  return {
    kind: String(raw && raw.kind || ''),
    rawRef: String(raw && raw.rawRef || ''),
    rawFingerprint: String(raw && raw.rawFingerprint || ''),
    formId: String(raw && raw.formId || ''),
    sheetId: Number(raw && raw.sheetId || 0),
    eventId: String(raw && raw.eventId || ''),
    originalRowNumber: Number(raw && raw.rowNumber || 0),
    observationId: String(provenance.observationId || ''),
    observationSourceKey: String(provenance.observationSourceKey || ''),
    observationSourceLocator: String(provenance.observationSourceLocator || ''),
    observationPayloadHash: String(provenance.observationPayloadHash || ''),
    observationProviderTimestamp: String(provenance.observationProviderTimestamp || ''),
    observationIdentityMode: String(raw && raw.observationIdentityMode || provenance.observationIdentityMode || '')
  };
}
