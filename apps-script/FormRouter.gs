function ttqsRawSubmission_(sheetId, rowNumber) {
  var ss = ttqsOpenCore_();
  var sheet = ss.getSheets().filter(function(s) { return s.getSheetId() === Number(sheetId); })[0];
  if (!sheet) throw new Error('UNKNOWN_RESPONSE_SHEET:' + sheetId);
  if (rowNumber < 2 || rowNumber > sheet.getLastRow()) throw new Error('INVALID_RESPONSE_ROW');
  var lastColumn = sheet.getLastColumn();
  var headers = sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0];
  var values = sheet.getRange(rowNumber, 1, 1, lastColumn).getDisplayValues()[0];
  var named = {};
  headers.forEach(function(h, i) { named[String(h)] = values[i]; });
  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), {});
  var kind = map[String(sheetId)];
  if (!kind) throw new Error('UNMAPPED_RESPONSE_SHEET:' + sheetId);
  return { kind: kind, sheetId: Number(sheetId), rowNumber: Number(rowNumber), named: named, rawRef: 'FORM_SUITE:' + sheetId + ':' + rowNumber };
}

function ttqsProcessSubmission_(raw) {
  var aliasCode = ttqsRequireSampleAlias_(raw.named.TTQS_ALIAS_CODE);
  var partyId = ttqsEnsurePartyAlias_(aliasCode);
  if (raw.kind === 'REGISTRATION') {
    var props = PropertiesService.getScriptProperties();
    if (props.getProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY') === 'TRUE') {
      props.deleteProperty('TTQS_FAIL_NEXT_REG_AFTER_PARTY');
      throw new Error('TTQS_INJECTED_PARTIAL_FAILURE_AFTER_PARTY_ALIAS');
    }
    ttqsWriteSurvey_({
      partyAliasId: partyId,
      surveyType: 'REGISTRATION',
      questionSetVersion: 'SAMPLE-RUNTIME-REG-v1',
      scoreTotal: 1,
      scoreMax: 1,
      freeText: '',
      sourceRef: raw.rawRef
    });
  } else if (raw.kind === 'NEEDS') {
    ttqsWriteSurvey_({
      partyAliasId: partyId,
      surveyType: 'NEEDS',
      questionSetVersion: 'SAMPLE-RUNTIME-NEEDS-v1',
      scoreTotal: ttqsNumber_(raw.named.TTQS_NEED_SCORE, 1, 5),
      scoreMax: 5,
      freeText: raw.named.TTQS_NEED_TEXT,
      sourceRef: raw.rawRef
    });
  } else if (raw.kind === 'REACTION') {
    var total = ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL'].reduce(function(sum, code) {
      return sum + ttqsNumber_(raw.named['TTQS_REACTION_' + code], 1, 5);
    }, 0);
    ttqsWriteSurvey_({
      partyAliasId: partyId,
      surveyType: 'REACTION',
      questionSetVersion: 'SAMPLE-RUNTIME-REACTION-v1',
      scoreTotal: total,
      scoreMax: 25,
      freeText: raw.named.TTQS_REACTION_TEXT,
      sourceRef: raw.rawRef
    });
  } else if (raw.kind === 'FOLLOWUP30') {
    var score = ttqsNumber_(raw.named.TTQS_30D_SAFE_ACTION, 1, 5) + ttqsNumber_(raw.named.TTQS_30D_BOUNDARY, 1, 5);
    ttqsWriteSurvey_({
      partyAliasId: partyId,
      surveyType: '30_DAY_BEHAVIOR',
      questionSetVersion: 'SAMPLE-RUNTIME-30D-v1',
      scoreTotal: score,
      scoreMax: 10,
      freeText: raw.named.TTQS_30D_TEXT,
      followupDueDate: ttqsDateOnly_(new Date()),
      followupCompletedDate: ttqsDateOnly_(new Date()),
      sourceRef: raw.rawRef
    });
  } else {
    throw new Error('UNKNOWN_FORM_KIND:' + raw.kind);
  }
  return { aliasCode: aliasCode, partyAliasId: partyId };
}

function ttqsHandleRawSubmission_(sheetId, rowNumber, isRetry) {
  ttqsAssertTestOnly_();
  var raw = ttqsRawSubmission_(sheetId, rowNumber);
  var idempotencyKey = 'TEST:' + raw.rawRef;
  var job = ttqsLedgerEnsure_({
    eventType: 'FORM_SUITE',
    objectType: raw.kind,
    objectId: raw.sheetId + ':' + raw.rowNumber,
    idempotencyKey: idempotencyKey,
    triggerSource: isRetry ? 'TIME_RETRY' : 'GOOGLE_FORM',
    notes: { kind: raw.kind, rawRef: raw.rawRef, sheetId: raw.sheetId, rowNumber: raw.rowNumber }
  });
  if (job.object.status === 'SUCCESS') return { duplicate: true, jobId: job.object.job_id };
  if (Number(job.object.attempt_no || 0) >= Number(job.object.max_attempts || ttqsConfig_().MAX_ATTEMPTS)) {
    throw new Error('MAX_ATTEMPTS_EXCEEDED');
  }
  ttqsLedgerStart_(job, isRetry);
  try {
    var result = ttqsProcessSubmission_(raw);
    ttqsLedgerSuccess_(job, { aliasCode: result.aliasCode, partyAliasId: result.partyAliasId, recovered: !!isRetry });
    return { duplicate: false, recovered: !!isRetry, jobId: job.object.job_id, traceId: job.object.trace_id };
  } catch (err) {
    ttqsLedgerFail_(job, err);
    throw err;
  }
}

function ttqsOnSpreadsheetFormSubmit(e) {
  if (!e || !e.range) throw new Error('REAL_SPREADSHEET_FORM_EVENT_REQUIRED');
  return ttqsHandleRawSubmission_(e.range.getSheet().getSheetId(), e.range.getRow(), false);
}
