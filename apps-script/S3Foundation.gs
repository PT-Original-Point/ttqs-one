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
