function ttqsEnsureEventId_(sheet, rowNumber) {
  var col = ttqsEventIdColumn_(sheet);
  var cell = sheet.getRange(rowNumber, col);
  var existing = String(cell.getDisplayValue() || '').trim();
  if (existing) return existing;
  var eventId = ttqsStableId_('EVT-', Utilities.getUuid() + '|' + sheet.getSheetId() + '|' + rowNumber + '|' + new Date().getTime(), 24);
  cell.setValue(eventId);
  SpreadsheetApp.flush();
  var readback = String(cell.getDisplayValue() || '').trim();
  if (readback !== eventId) throw new Error('EVENT_ID_PERSIST_READBACK_FAILED');
  return eventId;
}

function ttqsEventIdColumn_(sheet) {
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getDisplayValues()[0];
  var index = headers.indexOf('TTQS_EVENT_ID');
  if (index >= 0) return index + 1;
  var col = headers.length + 1;
  sheet.getRange(1, col).setValue('TTQS_EVENT_ID');
  SpreadsheetApp.flush();
  return col;
}

function ttqsRawFingerprint_(kind, formId, sheetId, headers, values) {
  var pairs = [];
  headers.forEach(function(header, i) {
    if (String(header) === 'TTQS_EVENT_ID') return;
    pairs.push([String(header), String(values[i] === undefined ? '' : values[i])]);
  });
  return ttqsDigest_(JSON.stringify({ kind: kind, formId: formId, sheetId: Number(sheetId), pairs: pairs }));
}

function ttqsCanonicalHeader_(kind, header) {
  var map = ttqsFormHeaderMap_();
  var kindMap = map[String(kind)] || {};
  var key = String(header || '');
  return kindMap[key] || key;
}

function ttqsRawSubmission_(sheetId, rowNumber, ensureEventId) {
  var ss = ttqsOpenCore_();
  var sheet = ss.getSheets().filter(function(s) { return s.getSheetId() === Number(sheetId); })[0];
  if (!sheet) throw new Error('UNKNOWN_RESPONSE_SHEET:' + sheetId);
  if (ensureEventId) ttqsEnsureEventId_(sheet, rowNumber);
  var lastColumn = sheet.getLastColumn();
  var headers = sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String);
  var values = sheet.getRange(rowNumber, 1, 1, lastColumn).getDisplayValues()[0];
  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), {});
  var kind = map[String(sheetId)];
  if (!kind) throw new Error('UNMAPPED_RESPONSE_SHEET:' + sheetId);
  var named = {};
  headers.forEach(function(header, i) { named[ttqsCanonicalHeader_(kind, header)] = values[i]; });
  var eventId = String(named.TTQS_EVENT_ID || '').trim();
  var formId = ttqsFormIdForKind_(kind);
  var fingerprint = ttqsRawFingerprint_(kind, formId, sheetId, headers, values);
  return {
    kind: kind,
    formId: formId,
    sheetId: Number(sheetId),
    rowNumber: Number(rowNumber),
    eventId: eventId,
    named: named,
    rawFingerprint: fingerprint,
    rawRef: eventId ? 'FORM_SUITE:' + formId + ':' + eventId : ''
  };
}

function ttqsFindRawSubmissionByRef_(sheetId, rawRef) {
  var ss = ttqsOpenCore_();
  var sheet = ss.getSheets().filter(function(s) { return s.getSheetId() === Number(sheetId); })[0];
  if (!sheet) throw new Error('UNKNOWN_RESPONSE_SHEET:' + sheetId);
  var matches = [];
  for (var rowNumber = 2; rowNumber <= sheet.getLastRow(); rowNumber++) {
    var raw = ttqsRawSubmission_(sheetId, rowNumber, false);
    if (raw.rawRef === String(rawRef)) matches.push(raw);
  }
  if (matches.length === 0) throw new Error('RAW_RESPONSE_REF_NOT_FOUND:' + rawRef);
  if (matches.length > 1) throw new Error('RAW_RESPONSE_REF_AMBIGUOUS:' + rawRef + ':' + matches.length);
  return matches[0];
}

function ttqsProcessSubmission_(raw, job) {
  var aliasCode = ttqsRequireSampleAlias_(raw.named.TTQS_ALIAS_CODE);
  var partyId = ttqsEnsurePartyAlias_(aliasCode);
  var common = {
    partyAliasId: partyId,
    sourceRef: raw.rawRef,
    rawFingerprint: raw.rawFingerprint,
    providerFormId: raw.formId,
    jobId: job.object.job_id
  };
  var surveyResult;
  if (raw.kind === 'REGISTRATION') {
    if (ttqsShouldInjectRegistrationFailure_(raw, aliasCode)) {
      throw new Error('TTQS_INJECTED_PARTIAL_FAILURE_AFTER_PARTY_ALIAS');
    }
    surveyResult = ttqsWriteSurvey_(Object.assign({}, common, {
      surveyType: 'REGISTRATION', questionSetVersion: 'SAMPLE-RUNTIME-REG-v1', scoreTotal: 1, scoreMax: 1, freeText: 'SAMPLE_ONLY'
    }));
  } else if (raw.kind === 'NEEDS') {
    surveyResult = ttqsWriteSurvey_(Object.assign({}, common, {
      surveyType: 'NEEDS', questionSetVersion: 'SAMPLE-RUNTIME-NEEDS-v1', scoreTotal: ttqsNumber_(raw.named.TTQS_NEED_SCORE, 1, 5), scoreMax: 5, freeText: raw.named.TTQS_NEED_TEXT
    }));
  } else if (raw.kind === 'REACTION') {
    var total = ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL'].reduce(function(sum, code) {
      return sum + ttqsNumber_(raw.named['TTQS_REACTION_' + code], 1, 5);
    }, 0);
    surveyResult = ttqsWriteSurvey_(Object.assign({}, common, {
      surveyType: 'REACTION', questionSetVersion: 'SAMPLE-RUNTIME-REACTION-v1', scoreTotal: total, scoreMax: 25, freeText: raw.named.TTQS_REACTION_TEXT
    }));
  } else if (raw.kind === 'FOLLOWUP30') {
    var score = ttqsNumber_(raw.named.TTQS_30D_SAFE_ACTION, 1, 5) + ttqsNumber_(raw.named.TTQS_30D_BOUNDARY, 1, 5);
    surveyResult = ttqsWriteSurvey_(Object.assign({}, common, {
      surveyType: '30_DAY_BEHAVIOR', questionSetVersion: 'SAMPLE-RUNTIME-30D-v1', scoreTotal: score, scoreMax: 10, freeText: raw.named.TTQS_30D_TEXT,
      followupDueDate: ttqsDateOnly_(new Date()), followupCompletedDate: ttqsDateOnly_(new Date())
    }));
  } else {
    throw new Error('UNKNOWN_FORM_KIND:' + raw.kind);
  }
  return { aliasCode: aliasCode, partyAliasId: partyId, responseId: surveyResult.responseId, evidenceId: surveyResult.evidenceId };
}

function ttqsHandleRawObjectUnlocked_(raw, isRetry) {
  ttqsAssertTestOnly_();
  if (!raw.eventId || !raw.rawRef) throw new Error('RAW_EVENT_ID_REQUIRED');
  var idempotencyKey = 'TEST:' + raw.rawRef;
  var job = ttqsLedgerEnsure_({
    eventType: 'FORM_SUITE', objectType: raw.kind, objectId: raw.rawRef, idempotencyKey: idempotencyKey,
    triggerSource: isRetry ? 'TIME_RETRY' : 'GOOGLE_FORM',
    notes: { kind: raw.kind, rawRef: raw.rawRef, rawFingerprint: raw.rawFingerprint, formId: raw.formId, sheetId: raw.sheetId, eventId: raw.eventId, originalRowNumber: raw.rowNumber }
  });
  if (job.object.status === 'SUCCESS') return { duplicate: true, jobId: job.object.job_id, traceId: job.object.trace_id };
  if (Number(job.object.attempt_no || 0) >= Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS)) throw new Error('MAX_ATTEMPTS_EXCEEDED');
  ttqsLedgerStart_(job, isRetry);
  try {
    var result = ttqsProcessSubmission_(raw, job);
    ttqsLedgerSuccess_(job, {
      aliasCode: result.aliasCode, partyAliasId: result.partyAliasId, responseId: result.responseId, evidenceId: result.evidenceId,
      sourceRef: raw.rawRef, rawFingerprint: raw.rawFingerprint, formId: raw.formId, eventId: raw.eventId, recovered: !!isRetry
    });
    return { duplicate: false, recovered: !!isRetry, jobId: job.object.job_id, traceId: job.object.trace_id, responseId: result.responseId, evidenceId: result.evidenceId };
  } catch (err) {
    ttqsLedgerFail_(job, err);
    throw err;
  }
}

function ttqsHandleRawSubmissionUnlocked_(sheetId, rowNumber, isRetry) {
  return ttqsHandleRawObjectUnlocked_(ttqsRawSubmission_(sheetId, rowNumber, !isRetry), isRetry);
}

function ttqsHandleRawSubmission_(sheetId, rowNumber, isRetry) {
  return ttqsWithScriptLock_(function() { return ttqsHandleRawSubmissionUnlocked_(sheetId, rowNumber, isRetry); });
}

function ttqsHandleRawRef_(sheetId, rawRef, isRetry) {
  return ttqsWithScriptLock_(function() { return ttqsHandleRawObjectUnlocked_(ttqsFindRawSubmissionByRef_(sheetId, rawRef), isRetry); });
}

function ttqsOnSpreadsheetFormSubmit(e) {
  if (!e || !e.range) throw new Error('REAL_SPREADSHEET_FORM_EVENT_REQUIRED');
  return ttqsHandleRawSubmission_(e.range.getSheet().getSheetId(), e.range.getRow(), false);
}
