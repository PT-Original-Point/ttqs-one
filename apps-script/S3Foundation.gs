var TTQS_S3_OBSERVATION_TRIGGER_SOURCE = 'SCHEDULER_OBSERVATION';
var TTQS_S3_SYNTHETIC_EVENT_PREFIX = 'EVT-OBS-';
var TTQS_S3_OBSERVATION_BATCH_LIMIT = 50;

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

function ttqsS3ObservationBoundedError_(err) {
  return String(err && err.message ? err.message : err || '').slice(0, 500);
}

function ttqsS3ObservationIntegrityError_(err) {
  var message = ttqsS3ObservationBoundedError_(err);
  return /^S3_OBSERVATION_(SOURCE_(TYPE|LOCATOR|SHEET|KIND|FORM|KEY)_|PROVIDER_TIMESTAMP_MISMATCH|PAYLOAD_HASH_MISMATCH)/.test(message) ||
    /^S3_DUPLICATE_OBSERVATION_/.test(message);
}

function ttqsS3ObservationBusinessIntegrityError_(err) {
  var message = ttqsS3ObservationBoundedError_(err);
  return /^S3_OBSERVATION_(RECONCILIATION_|FINAL_ACCEPTANCE_|JOB_(NOT_FOUND|NOT_SUCCESS|RAW_REF|NOTES_RAW_REF|FINGERPRINT|EVENT_ID|SOURCE_KEY))/.test(message) ||
    /^S3_DUPLICATE_JOB_ID/.test(message);
}

function ttqsS3ObservationDue_(entry, nowMillis) {
  if (!entry || !entry.object) return false;
  if (String(entry.object.processing_status || '') !== 'PENDING') return false;
  var retryAt = String(entry.object.next_retry_at || '').trim();
  if (!retryAt) return true;
  var retryMillis = new Date(retryAt).getTime();
  return !isFinite(retryMillis) || retryMillis <= Number(nowMillis || Date.now());
}

function ttqsS3PatchObservation_(entry, patch) {
  ttqsUpdateObjectRow_(ttqsEnsureObservationSheet_(), entry.rowNumber, patch);
  Object.keys(patch).forEach(function(key) { entry.object[key] = patch[key]; });
  return entry;
}

function ttqsS3ObservationJobByRaw_(raw) {
  if (!raw || !raw.rawRef) throw new Error('S3_OBSERVATION_RAW_REF_REQUIRED');
  return ttqsLedgerFind_('TEST:' + String(raw.rawRef));
}

function ttqsS3ObservationFinalJob_(jobId, raw) {
  var job = ttqsFindUniqueRowByValue_(ttqsLedgerSheet_(), 'job_id', String(jobId || ''), 'S3_DUPLICATE_JOB_ID');
  if (!job) throw new Error('S3_OBSERVATION_JOB_NOT_FOUND:' + String(jobId || ''));
  var notes = ttqsParseJson_(job.object.notes, {});
  if (String(job.object.status || '') !== 'SUCCESS') throw new Error('S3_OBSERVATION_JOB_NOT_SUCCESS:' + String(job.object.status || ''));
  if (String(job.object.reconciliation_status || '') !== 'MATCHED_EXACTLY_ONCE') throw new Error('S3_OBSERVATION_RECONCILIATION_NOT_EXACT:' + String(job.object.reconciliation_status || ''));
  if (String(job.object.final_acceptance_status || '') !== 'FINAL_ACCEPTED') throw new Error('S3_OBSERVATION_FINAL_ACCEPTANCE_MISSING:' + String(job.object.final_acceptance_status || ''));
  if (String(job.object.object_id || '') !== String(raw.rawRef || '')) throw new Error('S3_OBSERVATION_JOB_RAW_REF_MISMATCH');
  if (String(notes.rawRef || '') !== String(raw.rawRef || '')) throw new Error('S3_OBSERVATION_JOB_NOTES_RAW_REF_MISMATCH');
  if (String(notes.rawFingerprint || '') !== String(raw.rawFingerprint || '')) throw new Error('S3_OBSERVATION_JOB_FINGERPRINT_MISMATCH');
  if (String(notes.eventId || '') !== String(raw.eventId || '')) throw new Error('S3_OBSERVATION_JOB_EVENT_ID_MISMATCH');
  if (String(raw.observationIdentityMode || '') === 'OBSERVATION_SOURCE_KEY') {
    var sourceKey = String(raw.observationProvenance && raw.observationProvenance.observationSourceKey || '');
    if (!sourceKey || String(notes.observationSourceKey || '') !== sourceKey) throw new Error('S3_OBSERVATION_JOB_SOURCE_KEY_MISMATCH');
  }
  return {
    job: job,
    processedObjectId: String(notes.responseId || ''),
    evidenceId: String(notes.evidenceId || '')
  };
}

function ttqsS3AcceptObservation_(entry, raw, jobId, disposition, attemptCount) {
  var finalJob = ttqsS3ObservationFinalJob_(jobId, raw);
  ttqsS3PatchObservation_(entry, {
    processing_status: 'ACCEPTED',
    attempt_count: Number(attemptCount),
    next_retry_at: '',
    last_error: '',
    processed_object_id: finalJob.processedObjectId || String(jobId),
    disposition: String(disposition || 'ACCEPTED')
  });
  return {
    status: 'ACCEPTED',
    jobId: String(jobId),
    processedObjectId: finalJob.processedObjectId || String(jobId),
    disposition: String(disposition || 'ACCEPTED')
  };
}

function ttqsS3ProcessObservationEntryUnlocked_(entry) {
  ttqsAssertTestOnly_();
  var currentAttempts = Number(entry && entry.object && entry.object.attempt_count || 0);
  var raw;
  try {
    raw = ttqsS3ResolveObservationRaw_(entry);
  } catch (resolveErr) {
    var resolveMessage = ttqsS3ObservationBoundedError_(resolveErr);
    if (ttqsS3ObservationIntegrityError_(resolveErr)) {
      ttqsS3PatchObservation_(entry, {
        processing_status: 'QUARANTINED',
        attempt_count: currentAttempts + 1,
        next_retry_at: '',
        last_error: resolveMessage,
        disposition: 'SOURCE_INTEGRITY_BLOCKED'
      });
      return { status: 'QUARANTINED', error: resolveMessage };
    }
    ttqsS3PatchObservation_(entry, {
      processing_status: 'PENDING',
      attempt_count: currentAttempts,
      last_error: resolveMessage
    });
    return { status: 'DEFERRED', error: resolveMessage };
  }

  var existingJob = ttqsS3ObservationJobByRaw_(raw);
  if (existingJob) {
    var existingStatus = String(existingJob.object.status || '');
    if (existingStatus === 'SUCCESS') {
      var reconciliation = ttqsImmediateReconcile_(raw);
      if (String(reconciliation.status || '') !== 'MATCHED_EXACTLY_ONCE') {
        var mismatch = 'S3_OBSERVATION_RECONCILIATION_MISMATCH:' + String(reconciliation.status || 'UNKNOWN');
        ttqsS3PatchObservation_(entry, {
          processing_status: 'QUARANTINED',
          attempt_count: currentAttempts + 1,
          next_retry_at: '',
          last_error: mismatch.slice(0, 500),
          disposition: 'BUSINESS_LINKAGE_BLOCKED'
        });
        return { status: 'QUARANTINED', jobId: existingJob.object.job_id, error: mismatch };
      }
      return ttqsS3AcceptObservation_(entry, raw, existingJob.object.job_id, 'LINKED_EXISTING', currentAttempts + 1);
    }
    if (existingStatus === 'FAILED_FINAL') {
      var terminalMessage = 'S3_OBSERVATION_JOB_FAILED_FINAL';
      ttqsS3PatchObservation_(entry, {
        processing_status: 'REJECTED',
        attempt_count: currentAttempts,
        next_retry_at: '',
        last_error: terminalMessage,
        disposition: 'JOB_FAILED_FINAL'
      });
      return { status: 'REJECTED', jobId: existingJob.object.job_id, error: terminalMessage };
    }
    if (existingStatus === 'FAILED' || existingStatus === 'RUNNING') {
      ttqsS3PatchObservation_(entry, {
        processing_status: 'PENDING',
        attempt_count: currentAttempts,
        next_retry_at: String(existingJob.object.retry_at || ''),
        last_error: 'WAITING_JOB_' + existingStatus,
        disposition: 'AWAITING_JOB_RECOVERY'
      });
      return { status: 'DEFERRED', jobId: existingJob.object.job_id, jobStatus: existingStatus };
    }
  }

  try {
    var result = ttqsHandleRawObjectUnlocked_(raw, false);
    if (String(result && result.reconciliationStatus || '') !== 'MATCHED_EXACTLY_ONCE') {
      throw new Error('S3_OBSERVATION_RECONCILIATION_MISMATCH:' + String(result && result.reconciliationStatus || 'UNKNOWN'));
    }
    return ttqsS3AcceptObservation_(entry, raw, result.jobId, result && result.duplicate ? 'LINKED_EXISTING' : 'SCHEDULER_PROCESSED', currentAttempts + 1);
  } catch (processErr) {
    var processMessage = ttqsS3ObservationBoundedError_(processErr);
    if (ttqsS3ObservationBusinessIntegrityError_(processErr)) {
      ttqsS3PatchObservation_(entry, {
        processing_status: 'QUARANTINED',
        attempt_count: currentAttempts + 1,
        next_retry_at: '',
        last_error: processMessage,
        disposition: 'BUSINESS_LINKAGE_BLOCKED'
      });
      return { status: 'QUARANTINED', error: processMessage };
    }
    var jobAfter = ttqsS3ObservationJobByRaw_(raw);
    if (jobAfter && String(jobAfter.object.status || '') === 'FAILED_FINAL') {
      ttqsS3PatchObservation_(entry, {
        processing_status: 'REJECTED',
        attempt_count: currentAttempts + 1,
        next_retry_at: '',
        last_error: processMessage,
        disposition: 'JOB_FAILED_FINAL'
      });
      return { status: 'REJECTED', jobId: jobAfter.object.job_id, error: processMessage };
    }
    ttqsS3PatchObservation_(entry, {
      processing_status: 'PENDING',
      attempt_count: currentAttempts + 1,
      next_retry_at: String(jobAfter && jobAfter.object.retry_at || ''),
      last_error: processMessage,
      disposition: 'AWAITING_JOB_RECOVERY'
    });
    return { status: 'DEFERRED', jobId: jobAfter ? jobAfter.object.job_id : '', error: processMessage };
  }
}

function ttqsS3ProcessPendingObservationsUnlocked_() {
  ttqsAssertTestOnly_();
  var now = Date.now();
  var pending = ttqsReadObjects_(ttqsEnsureObservationSheet_()).filter(function(entry) {
    return ttqsS3ObservationDue_(entry, now);
  }).slice(0, TTQS_S3_OBSERVATION_BATCH_LIMIT);
  var summary = {
    selected: pending.length,
    accepted: 0,
    linked_existing: 0,
    scheduler_processed: 0,
    deferred: 0,
    quarantined: 0,
    rejected: 0,
    results: []
  };
  pending.forEach(function(entry) {
    var result = ttqsS3ProcessObservationEntryUnlocked_(entry);
    summary.results.push({
      observation_id: String(entry.object.observation_id || ''),
      status: String(result.status || ''),
      job_id: String(result.jobId || ''),
      error: ttqsS3ObservationBoundedError_(result.error || '')
    });
    if (result.status === 'ACCEPTED') {
      summary.accepted += 1;
      if (result.disposition === 'LINKED_EXISTING') summary.linked_existing += 1;
      if (result.disposition === 'SCHEDULER_PROCESSED') summary.scheduler_processed += 1;
    } else if (result.status === 'DEFERRED') {
      summary.deferred += 1;
    } else if (result.status === 'QUARANTINED') {
      summary.quarantined += 1;
    } else if (result.status === 'REJECTED') {
      summary.rejected += 1;
    }
  });
  return summary;
}

function ttqsS3ObservationCycle() {
  ttqsAssertTestOnly_();
  var startedAt = Date.now();
  var shadow = ttqsScheduler();
  var processedAt = Date.now();
  var processing = ttqsWithScriptLock_(ttqsS3ProcessPendingObservationsUnlocked_);
  var postProcessingAt = Date.now();
  var reconciliation = ttqsObservationReconcileShadow_();
  var finishedAt = Date.now();
  return Object.assign({}, shadow, {
    mode: 'OBSERVATION_S3_DUAL_RUN',
    processing: processing,
    reconciliation: reconciliation,
    legacy_processing_unchanged: false,
    timings_ms: Object.assign({}, shadow.timings_ms || {}, {
      shadow_total: processedAt - startedAt,
      processing: postProcessingAt - processedAt,
      post_processing_reconcile: finishedAt - postProcessingAt,
      total: finishedAt - startedAt
    })
  });
}

var TTQS_GATE_A_SOURCE_TYPE = 'GOOGLE_FORM_RESPONSE';
var TTQS_GATE_A_SCHEMA_VERSION = 'GATE_A_V1';

function ttqsGateARequireString_(value, code) {
  var text = String(value === undefined || value === null ? '' : value).trim();
  if (!text) throw new Error(code || 'GATE_A_VALUE_REQUIRED');
  return text;
}

function ttqsGateACanonicalize_(value) {
  if (value === null) return null;
  var type = typeof value;
  if (type === 'string' || type === 'boolean') return value;
  if (type === 'number') {
    if (!isFinite(value)) throw new Error('GATE_A_CANONICAL_NUMBER_INVALID');
    return value;
  }
  if (Array.isArray(value)) {
    return value.map(function(item) { return ttqsGateACanonicalize_(item); });
  }
  if (type === 'object') {
    var out = {};
    Object.keys(value).sort().forEach(function(key) {
      if (value[key] === undefined) throw new Error('GATE_A_CANONICAL_UNDEFINED:' + key);
      out[key] = ttqsGateACanonicalize_(value[key]);
    });
    return out;
  }
  throw new Error('GATE_A_CANONICAL_TYPE_UNSUPPORTED:' + type);
}

function ttqsGateACanonicalJson_(value) {
  return JSON.stringify(ttqsGateACanonicalize_(value));
}

function ttqsGateADigestCanonical_(value) {
  return ttqsDigest_(ttqsGateACanonicalJson_(value));
}

function ttqsGateAResponseIdentity_(formId, responseId) {
  var form = ttqsGateARequireString_(formId, 'GATE_A_FORM_ID_REQUIRED');
  var response = ttqsGateARequireString_(responseId, 'GATE_A_RESPONSE_ID_REQUIRED');
  return ttqsGateADigestCanonical_({
    sourceType: TTQS_GATE_A_SOURCE_TYPE,
    formId: form,
    responseId: response
  });
}

function ttqsGateANormalizeProviderTimestamp_(value, code) {
  var text = ttqsGateARequireString_(value, code || 'GATE_A_TIMESTAMP_REQUIRED');
  var match = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{3}|\d{6}|\d{9}))?Z$/.exec(text);
  if (!match) throw new Error((code || 'GATE_A_TIMESTAMP_INVALID') + ':' + text);
  var millis = Date.parse(match[1] + (match[2] ? '.' + match[2].slice(0, 3) : '') + 'Z');
  if (!isFinite(millis)) throw new Error((code || 'GATE_A_TIMESTAMP_INVALID') + ':' + text);
  return text;
}

function ttqsGateATimestampParts_(value) {
  var normalized = ttqsGateANormalizeProviderTimestamp_(value, 'GATE_A_TIMESTAMP_INVALID');
  var match = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{3}|\d{6}|\d{9}))?Z$/.exec(normalized);
  var seconds = Date.parse(match[1] + 'Z') / 1000;
  var nanos = Number(String(match[2] || '').padEnd(9, '0') || '0');
  return { seconds: seconds, nanos: nanos };
}

function ttqsGateAMaxTimestamp_(current, candidate) {
  var next = ttqsGateANormalizeProviderTimestamp_(candidate, 'GATE_A_PROVIDER_LAST_SUBMITTED_TIME_INVALID');
  if (!current) return next;
  var currentNormalized = ttqsGateANormalizeProviderTimestamp_(current, 'GATE_A_CANDIDATE_WATERMARK_INVALID');
  var a = ttqsGateATimestampParts_(currentNormalized);
  var b = ttqsGateATimestampParts_(next);
  if (b.seconds > a.seconds || (b.seconds === a.seconds && b.nanos > a.nanos)) return next;
  return currentNormalized;
}

function ttqsGateAUniqueSortedIds_(values, code) {
  if (!Array.isArray(values)) throw new Error((code || 'GATE_A_FIELD_IDS_INVALID') + ':NOT_ARRAY');
  var seen = Object.create(null);
  var out = [];
  values.forEach(function(value) {
    var id = ttqsGateARequireString_(value, code || 'GATE_A_FIELD_ID_REQUIRED');
    if (seen[id]) throw new Error((code || 'GATE_A_DUPLICATE_FIELD_ID') + ':' + id);
    seen[id] = true;
    out.push(id);
  });
  out.sort();
  return out;
}

function ttqsGateASchemaContract_(schemaVersion, expectedFieldIds, requiredFieldIds) {
  var version = ttqsGateARequireString_(schemaVersion || TTQS_GATE_A_SCHEMA_VERSION, 'GATE_A_SCHEMA_VERSION_REQUIRED');
  var expected = ttqsGateAUniqueSortedIds_(expectedFieldIds, 'GATE_A_SCHEMA_EXPECTED_FIELD_INVALID');
  if (!expected.length) throw new Error('GATE_A_SCHEMA_EXPECTED_FIELDS_REQUIRED');
  var required = ttqsGateAUniqueSortedIds_(requiredFieldIds || [], 'GATE_A_SCHEMA_REQUIRED_FIELD_INVALID');
  var expectedMap = Object.create(null);
  expected.forEach(function(id) { expectedMap[id] = true; });
  required.forEach(function(id) {
    if (!expectedMap[id]) throw new Error('GATE_A_SCHEMA_REQUIRED_NOT_EXPECTED:' + id);
  });
  return {
    schema_version: version,
    expected_field_ids: expected,
    required_field_ids: required,
    field_signature: ttqsGateADigestCanonical_({ schemaVersion: version, fieldIds: expected })
  };
}

function ttqsGateAValidateResponseSchema_(response, schema) {
  if (!schema || !Array.isArray(schema.expected_field_ids)) throw new Error('GATE_A_SCHEMA_CONTRACT_REQUIRED');
  var answers = response && response.answers ? response.answers : {};
  if (!answers || typeof answers !== 'object' || Array.isArray(answers)) throw new Error('GATE_A_ANSWERS_INVALID');
  var expected = Object.create(null);
  schema.expected_field_ids.forEach(function(id) { expected[id] = true; });
  Object.keys(answers).forEach(function(id) {
    if (!expected[id]) throw new Error('GATE_A_SCHEMA_DRIFT_UNKNOWN_FIELD:' + id);
  });
  schema.required_field_ids.forEach(function(id) {
    if (!Object.prototype.hasOwnProperty.call(answers, id)) throw new Error('GATE_A_SCHEMA_REQUIRED_FIELD_MISSING:' + id);
  });
  return true;
}

function ttqsGateAResponsePayload_(response) {
  var answers = response && response.answers ? response.answers : {};
  return ttqsGateACanonicalize_({ answers: answers });
}

function ttqsGateAPlanOverlapRequest_(formId, committedWatermark, overlapMs, initialWindowStart) {
  var form = ttqsGateARequireString_(formId, 'GATE_A_FORM_ID_REQUIRED');
  var overlap = Number(overlapMs || 0);
  if (!isFinite(overlap) || overlap < 0 || Math.floor(overlap) !== overlap) throw new Error('GATE_A_OVERLAP_MS_INVALID');
  var committed = String(committedWatermark || '').trim();
  var windowStart;
  if (committed) {
    var normalizedCommitted = ttqsGateANormalizeProviderTimestamp_(committed, 'GATE_A_COMMITTED_WATERMARK_INVALID');
    var startMillis = Date.parse(normalizedCommitted) - overlap;
    if (!isFinite(startMillis)) throw new Error('GATE_A_OVERLAP_WINDOW_INVALID');
    windowStart = new Date(startMillis).toISOString();
    committed = normalizedCommitted;
  } else {
    windowStart = ttqsGateANormalizeProviderTimestamp_(initialWindowStart, 'GATE_A_INITIAL_WINDOW_START_REQUIRED');
  }
  return {
    form_id: form,
    filter: 'timestamp >= ' + windowStart,
    window_start: windowStart,
    committed_watermark_snapshot: committed
  };
}

function ttqsGateANewRun_(requestContext, runId) {
  if (!requestContext) throw new Error('GATE_A_REQUEST_CONTEXT_REQUIRED');
  return {
    run_id: ttqsGateARequireString_(runId, 'GATE_A_RUN_ID_REQUIRED'),
    form_id: ttqsGateARequireString_(requestContext.form_id, 'GATE_A_FORM_ID_REQUIRED'),
    filter: ttqsGateARequireString_(requestContext.filter, 'GATE_A_FILTER_REQUIRED'),
    window_start: ttqsGateANormalizeProviderTimestamp_(requestContext.window_start, 'GATE_A_WINDOW_START_INVALID'),
    committed_watermark_snapshot: String(requestContext.committed_watermark_snapshot || ''),
    next_page_token: '',
    page_ordinal: 0,
    staged_response_ids: [],
    staged_records: {},
    candidate_high_watermark: String(requestContext.committed_watermark_snapshot || ''),
    page_checkpoints: [],
    last_checkpoint: null,
    run_complete: false,
    reconciliation: null,
    final_watermark_candidate: ''
  };
}

function ttqsGateARequestForPage_(state) {
  if (!state) throw new Error('GATE_A_RUN_STATE_REQUIRED');
  if (state.run_complete) throw new Error('GATE_A_RUN_ALREADY_COMPLETE');
  return {
    formId: ttqsGateARequireString_(state.form_id, 'GATE_A_FORM_ID_REQUIRED'),
    filter: ttqsGateARequireString_(state.filter, 'GATE_A_FILTER_REQUIRED'),
    pageToken: String(state.next_page_token || '')
  };
}

function ttqsGateABuildL1Record_(request, response, schema, observedAt, runId, pageOrdinal) {
  if (!request) throw new Error('GATE_A_PAGE_REQUEST_REQUIRED');
  var requestFormId = ttqsGateARequireString_(request.formId, 'GATE_A_FORM_ID_REQUIRED');
  var providerFormId = ttqsGateARequireString_(response && response.formId, 'GATE_A_PROVIDER_FORM_ID_REQUIRED');
  if (providerFormId !== requestFormId) throw new Error('GATE_A_PROVIDER_FORM_ID_MISMATCH');
  var responseId = ttqsGateARequireString_(response && response.responseId, 'GATE_A_RESPONSE_ID_REQUIRED');
  ttqsGateAValidateResponseSchema_(response, schema);
  var payload = ttqsGateAResponsePayload_(response);
  var ordinal = Number(pageOrdinal);
  if (!isFinite(ordinal) || ordinal < 1 || Math.floor(ordinal) !== ordinal) throw new Error('GATE_A_PAGE_ORDINAL_INVALID');
  return {
    environment: 'TEST',
    source_type: TTQS_GATE_A_SOURCE_TYPE,
    form_id: requestFormId,
    response_id: responseId,
    source_identity: ttqsGateAResponseIdentity_(requestFormId, responseId),
    provider_create_time: ttqsGateANormalizeProviderTimestamp_(response.createTime, 'GATE_A_PROVIDER_CREATE_TIME_INVALID'),
    provider_last_submitted_time: ttqsGateANormalizeProviderTimestamp_(response.lastSubmittedTime, 'GATE_A_PROVIDER_LAST_SUBMITTED_TIME_INVALID'),
    schema_version: schema.schema_version,
    field_signature: schema.field_signature,
    payload_hash: ttqsGateADigestCanonical_(payload),
    observed_at: ttqsGateANormalizeProviderTimestamp_(observedAt, 'GATE_A_OBSERVED_AT_INVALID'),
    ingestion_run_id: ttqsGateARequireString_(runId, 'GATE_A_RUN_ID_REQUIRED'),
    page_ordinal: ordinal,
    provider_filter: ttqsGateARequireString_(request.filter, 'GATE_A_FILTER_REQUIRED')
  };
}

function ttqsGateAAssertImmutableReplay_(existingRecord, incomingRecord) {
  if (String(existingRecord.source_identity || '') !== String(incomingRecord.source_identity || '')) {
    throw new Error('GATE_A_RESPONSE_IDENTITY_MISMATCH');
  }
  if (String(existingRecord.payload_hash || '') !== String(incomingRecord.payload_hash || '')) {
    throw new Error('GATE_A_RESPONSE_ID_CONTENT_CONFLICT:' + String(incomingRecord.response_id || ''));
  }
  if (String(existingRecord.field_signature || '') !== String(incomingRecord.field_signature || '') ||
      String(existingRecord.schema_version || '') !== String(incomingRecord.schema_version || '')) {
    throw new Error('GATE_A_RESPONSE_ID_SCHEMA_CONFLICT:' + String(incomingRecord.response_id || ''));
  }
  return true;
}

function ttqsGateAClone_(value) {
  return JSON.parse(JSON.stringify(value));
}

function ttqsGateACheckpointBody_(state) {
  return {
    version: 'GATE_A_CHECKPOINT_V1',
    run_id: String(state.run_id || ''),
    form_id: String(state.form_id || ''),
    filter: String(state.filter || ''),
    window_start: String(state.window_start || ''),
    committed_watermark_snapshot: String(state.committed_watermark_snapshot || ''),
    page_ordinal: Number(state.page_ordinal || 0),
    next_page_token: String(state.next_page_token || ''),
    staged_response_ids: (state.staged_response_ids || []).slice().sort(),
    staged_records: ttqsGateAClone_(state.staged_records || {}),
    candidate_high_watermark: String(state.candidate_high_watermark || ''),
    run_complete: state.run_complete === true,
    checkpoint_history: ttqsGateAClone_(state.page_checkpoints || [])
  };
}

function ttqsGateAMakeCheckpoint_(state) {
  var body = ttqsGateACheckpointBody_(state);
  var checkpoint = ttqsGateAClone_(body);
  checkpoint.checkpoint_hash = ttqsGateADigestCanonical_(body);
  return checkpoint;
}

function ttqsGateARestoreCheckpoint_(checkpoint) {
  if (!checkpoint) throw new Error('GATE_A_CHECKPOINT_REQUIRED');
  var suppliedHash = ttqsGateARequireString_(checkpoint.checkpoint_hash, 'GATE_A_CHECKPOINT_HASH_REQUIRED');
  var body = ttqsGateAClone_(checkpoint);
  delete body.checkpoint_hash;
  if (ttqsGateADigestCanonical_(body) !== suppliedHash) throw new Error('GATE_A_CHECKPOINT_HASH_MISMATCH');
  var history = ttqsGateAClone_(body.checkpoint_history || []);
  history.push({ page_ordinal: Number(body.page_ordinal || 0), checkpoint_hash: suppliedHash });
  return {
    run_id: body.run_id,
    form_id: body.form_id,
    filter: body.filter,
    window_start: body.window_start,
    committed_watermark_snapshot: body.committed_watermark_snapshot,
    next_page_token: body.next_page_token,
    page_ordinal: Number(body.page_ordinal || 0),
    staged_response_ids: (body.staged_response_ids || []).slice().sort(),
    staged_records: ttqsGateAClone_(body.staged_records || {}),
    candidate_high_watermark: body.candidate_high_watermark,
    page_checkpoints: history,
    last_checkpoint: ttqsGateAClone_(checkpoint),
    run_complete: body.run_complete === true,
    reconciliation: null,
    final_watermark_candidate: ''
  };
}

function ttqsGateAApplyPage_(state, request, page, schema, observedAt) {
  if (!state || !request || !page) throw new Error('GATE_A_PAGE_INPUT_REQUIRED');
  if (state.run_complete) throw new Error('GATE_A_RUN_ALREADY_COMPLETE');
  if (String(request.formId || '') !== String(state.form_id || '') || String(request.filter || '') !== String(state.filter || '')) {
    throw new Error('GATE_A_PAGE_REQUEST_CONTEXT_MISMATCH');
  }
  if (String(request.pageToken || '') !== String(state.next_page_token || '')) throw new Error('GATE_A_PAGE_TOKEN_MISMATCH');
  var responses = page.responses === undefined ? [] : page.responses;
  if (!Array.isArray(responses)) throw new Error('GATE_A_PAGE_RESPONSES_INVALID');
  var next = ttqsGateAClone_(state);
  var ordinal = Number(state.page_ordinal || 0) + 1;
  responses.forEach(function(response) {
    var record = ttqsGateABuildL1Record_(request, response, schema, observedAt, state.run_id, ordinal);
    var existing = next.staged_records[record.response_id];
    if (existing) {
      ttqsGateAAssertImmutableReplay_(existing, record);
    } else {
      next.staged_records[record.response_id] = record;
    }
    next.candidate_high_watermark = ttqsGateAMaxTimestamp_(next.candidate_high_watermark, record.provider_last_submitted_time);
  });
  next.staged_response_ids = Object.keys(next.staged_records).sort();
  next.page_ordinal = ordinal;
  var nextToken = String(page.nextPageToken || '').trim();
  if (nextToken && nextToken === String(request.pageToken || '')) throw new Error('GATE_A_PAGINATION_TOKEN_STALLED');
  next.next_page_token = nextToken;
  next.run_complete = nextToken === '';
  next.reconciliation = null;
  next.final_watermark_candidate = '';
  var checkpoint = ttqsGateAMakeCheckpoint_(next);
  next.page_checkpoints.push({ page_ordinal: ordinal, checkpoint_hash: checkpoint.checkpoint_hash });
  next.last_checkpoint = checkpoint;
  return next;
}

function ttqsGateAIdSetInfo_(values, label) {
  if (!Array.isArray(values)) throw new Error('GATE_A_ID_SET_INVALID:' + label);
  var counts = Object.create(null);
  values.forEach(function(value) {
    var id = ttqsGateARequireString_(value, 'GATE_A_RESPONSE_ID_REQUIRED');
    counts[id] = Number(counts[id] || 0) + 1;
  });
  var ids = Object.keys(counts).sort();
  var duplicates = ids.filter(function(id) { return counts[id] > 1; });
  return { ids: ids, duplicates: duplicates };
}

function ttqsGateAReconcileIdSets_(providerResponseIds, l1ResponseIds) {
  var provider = ttqsGateAIdSetInfo_(providerResponseIds, 'PROVIDER');
  var l1 = ttqsGateAIdSetInfo_(l1ResponseIds, 'L1');
  var providerMap = Object.create(null);
  var l1Map = Object.create(null);
  provider.ids.forEach(function(id) { providerMap[id] = true; });
  l1.ids.forEach(function(id) { l1Map[id] = true; });
  var missing = provider.ids.filter(function(id) { return !l1Map[id]; });
  var unexpected = l1.ids.filter(function(id) { return !providerMap[id]; });
  var duplicates = provider.duplicates.map(function(id) { return 'PROVIDER:' + id; })
    .concat(l1.duplicates.map(function(id) { return 'L1:' + id; })).sort();
  return {
    provider_response_ids: provider.ids,
    l1_response_ids: l1.ids,
    missing_in_l1: missing,
    unexpected_in_l1: unexpected,
    duplicate_identities: duplicates,
    exact_match: missing.length === 0 && unexpected.length === 0 && duplicates.length === 0
  };
}

function ttqsGateAFinalizeRun_(state, l1ResponseIds) {
  if (!state || state.run_complete !== true) throw new Error('GATE_A_PAGINATION_INCOMPLETE');
  var reconciliation = ttqsGateAReconcileIdSets_(state.staged_response_ids || [], l1ResponseIds);
  if (!reconciliation.exact_match) {
    throw new Error('GATE_A_ID_SET_MISMATCH:' + ttqsGateACanonicalJson_({
      missing_in_l1: reconciliation.missing_in_l1,
      unexpected_in_l1: reconciliation.unexpected_in_l1,
      duplicate_identities: reconciliation.duplicate_identities
    }));
  }
  var next = ttqsGateAClone_(state);
  next.reconciliation = reconciliation;
  next.final_watermark_candidate = String(state.candidate_high_watermark || state.committed_watermark_snapshot || '');
  return next;
}

function ttqsGateACommitWatermark_(state) {
  if (!state || state.run_complete !== true) throw new Error('GATE_A_PAGINATION_INCOMPLETE');
  if (!state.reconciliation || state.reconciliation.exact_match !== true) throw new Error('GATE_A_RECONCILIATION_REQUIRED');
  return ttqsGateARequireString_(state.final_watermark_candidate, 'GATE_A_WATERMARK_UNAVAILABLE');
}
