var TTQS_EVENT_ID_HEADER = 'TTQS_EVENT_ID';

function ttqsFormIdForKind_(kind) {
  var formId = PropertiesService.getScriptProperties().getProperty('TTQS_FORM_' + kind + '_ID');
  if (!formId) throw new Error('MISSING_FORM_ID_FOR_KIND:' + kind);
  return String(formId);
}

function ttqsRawFingerprint_(kind, formId, sheetId, headers, values) {
  return ttqsDigest_(JSON.stringify({
    kind: String(kind),
    formId: String(formId),
    sheetId: Number(sheetId),
    headers: headers.map(String),
    values: values.map(String)
  }));
}

function ttqsEventIdColumn_(sheet, createIfMissing) {
  var lastColumn = sheet.getLastColumn();
  var headers = lastColumn > 0 ? sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String) : [];
  var matches = [];
  headers.forEach(function(header, i) {
    if (header === TTQS_EVENT_ID_HEADER) matches.push(i + 1);
  });
  if (matches.length > 1) throw new Error('DUPLICATE_EVENT_ID_HEADER:' + matches.length);
  if (matches.length === 1) return matches[0];
  if (!createIfMissing) return 0;
  var column = lastColumn + 1;
  sheet.getRange(1, column).setValue(TTQS_EVENT_ID_HEADER);
  return column;
}

function ttqsEnsureEventId_(sheet, rowNumber) {
  var column = ttqsEventIdColumn_(sheet, true);
  var cell = sheet.getRange(rowNumber, column);
  var existing = String(cell.getDisplayValue() || '').trim();
  if (existing) return existing;
  var eventId = ttqsStableId_('EVT-', Utilities.getUuid(), 24);
  cell.setValue(eventId);
  SpreadsheetApp.flush();
  var readback = String(cell.getDisplayValue() || '').trim();
  if (readback !== eventId) throw new Error('EVENT_ID_WRITE_READBACK_MISMATCH');
  return eventId;
}

function ttqsRawSubmission_(sheetId, rowNumber, ensureEventId) {
  var ss = ttqsOpenCore_();
  var sheet = ss.getSheets().filter(function(s) { return s.getSheetId() === Number(sheetId); })[0];
  if (!sheet) throw new Error('UNKNOWN_RESPONSE_SHEET:' + sheetId);
  if (rowNumber < 2 || rowNumber > sheet.getLastRow()) throw new Error('INVALID_RESPONSE_ROW');

  var eventColumn = ttqsEventIdColumn_(sheet, !!ensureEventId);
  var eventId = eventColumn ? (ensureEventId ? ttqsEnsureEventId_(sheet, rowNumber) : String(sheet.getRange(rowNumber, eventColumn).getDisplayValue() || '').trim()) : '';
  var lastColumn = sheet.getLastColumn();
  var allHeaders = sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String);
  var allValues = sheet.getRange(rowNumber, 1, 1, lastColumn).getDisplayValues()[0].map(String);
  var headers = [];
  var values = [];
  var named = {};
  allHeaders.forEach(function(header, i) {
    if (header === TTQS_EVENT_ID_HEADER) return;
    var canonicalHeader = ttqsCanonicalFieldCode_(header);
    headers.push(String(canonicalHeader));
    values.push(String(allValues[i]));
    named[String(canonicalHeader)] = allValues[i];
  });

  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), {});
  var kind = map[String(sheetId)];
  if (!kind) throw new Error('UNMAPPED_RESPONSE_SHEET:' + sheetId);
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
    var props = PropertiesService.getScriptProperties();
    if (props.getProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY') === 'TRUE') {
      props.deleteProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY');
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
