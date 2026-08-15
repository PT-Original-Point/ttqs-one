function ttqsOpenCore_() {
  ttqsAssertTestOnly_();
  return SpreadsheetApp.openById(ttqsConfig_().CORE_SPREADSHEET_ID);
}

function ttqsGetSheet_(name) {
  var sheet = ttqsOpenCore_().getSheetByName(name);
  if (!sheet) throw new Error('MISSING_CORE_SHEET:' + name);
  return sheet;
}

function ttqsHeaders_(sheet) {
  var lastColumn = sheet.getLastColumn();
  if (lastColumn < 1) return [];
  return sheet.getRange(1, 1, 1, lastColumn).getValues()[0].map(String);
}

function ttqsHeaderIndex_(headers) {
  var index = {};
  headers.forEach(function(h, i) { index[h] = i; });
  return index;
}

function ttqsRowObject_(headers, row) {
  var out = {};
  headers.forEach(function(h, i) { out[h] = row[i]; });
  return out;
}

function ttqsAppendObject_(sheet, object) {
  var headers = ttqsHeaders_(sheet);
  if (!headers.length) throw new Error('SHEET_HAS_NO_HEADERS:' + sheet.getName());
  var row = headers.map(function(h) {
    return Object.prototype.hasOwnProperty.call(object, h) ? object[h] : '';
  });
  sheet.appendRow(row);
  return sheet.getLastRow();
}

function ttqsFindRowsByValue_(sheet, header, value) {
  var headers = ttqsHeaders_(sheet);
  var index = ttqsHeaderIndex_(headers);
  if (index[header] === undefined) throw new Error('MISSING_HEADER:' + header);
  var lastRow = sheet.getLastRow();
  if (lastRow < 3) return [];
  var values = sheet.getRange(3, 1, lastRow - 2, headers.length).getValues();
  var found = [];
  for (var i = 0; i < values.length; i++) {
    if (String(values[i][index[header]]) === String(value)) {
      found.push({ rowNumber: i + 3, object: ttqsRowObject_(headers, values[i]), headers: headers });
    }
  }
  return found;
}

function ttqsFindRowByValue_(sheet, header, value) {
  var rows = ttqsFindRowsByValue_(sheet, header, value);
  return rows.length ? rows[0] : null;
}

function ttqsFindUniqueRowByValue_(sheet, header, value, duplicateCode) {
  var rows = ttqsFindRowsByValue_(sheet, header, value);
  if (rows.length > 1) {
    throw new Error((duplicateCode || 'DUPLICATE_VALUE') + ':' + header + ':' + String(value) + ':' + rows.length);
  }
  return rows.length === 1 ? rows[0] : null;
}

function ttqsCountRowsByValue_(sheet, header, value) {
  return ttqsFindRowsByValue_(sheet, header, value).length;
}

function ttqsMissingHeaders_(sheet, requiredHeaders) {
  var present = ttqsHeaderIndex_(ttqsHeaders_(sheet));
  return requiredHeaders.filter(function(header) { return present[header] === undefined; });
}

function ttqsAssertHeaders_(sheet, requiredHeaders) {
  var missing = ttqsMissingHeaders_(sheet, requiredHeaders);
  if (missing.length) throw new Error('MISSING_REQUIRED_HEADERS:' + sheet.getName() + ':' + missing.join(','));
  return true;
}

function ttqsReadObjects_(sheet) {
  var headers = ttqsHeaders_(sheet);
  var lastRow = sheet.getLastRow();
  if (lastRow < 3) return [];
  return sheet.getRange(3, 1, lastRow - 2, headers.length).getValues().map(function(row, i) {
    return { rowNumber: i + 3, object: ttqsRowObject_(headers, row) };
  });
}

function ttqsImmutableSheetName_() {
  try {
    var cfg = ttqsConfig_();
    return cfg && cfg.SHEETS ? String(cfg.SHEETS.ATTEMPT_HISTORY || '') : '';
  } catch (err) {
    return '';
  }
}

function ttqsAssertMutableSheet_(sheet) {
  var immutableName = ttqsImmutableSheetName_();
  var sheetName = sheet && sheet.getName ? String(sheet.getName()) : '';
  if (immutableName && sheetName === immutableName) {
    throw new Error('ATTEMPT_HISTORY_IMMUTABLE_UPDATE_FORBIDDEN');
  }
  return true;
}

function ttqsUpdateObjectRow_(sheet, rowNumber, patch) {
  ttqsAssertMutableSheet_(sheet);
  var headers = ttqsHeaders_(sheet);
  var current = sheet.getRange(rowNumber, 1, 1, headers.length).getValues()[0];
  headers.forEach(function(h, i) {
    if (Object.prototype.hasOwnProperty.call(patch, h)) current[i] = patch[h];
  });
  sheet.getRange(rowNumber, 1, 1, headers.length).setValues([current]);
}

function ttqsEnsureColumns_(sheet, columns) {
  var headers = ttqsHeaders_(sheet);
  var index = ttqsHeaderIndex_(headers);
  columns.forEach(function(column) {
    var header = String(column.header);
    if (index[header] !== undefined) return;
    var targetColumn = sheet.getLastColumn() + 1;
    sheet.getRange(1, targetColumn).setValue(header);
    if (column.description) sheet.getRange(2, targetColumn).setValue(String(column.description));
    index[header] = targetColumn - 1;
  });
  return sheet;
}

function ttqsEnsureStructuredSheet_(spreadsheet, name, columns) {
  var sheet = spreadsheet.getSheetByName(name);
  if (!sheet) sheet = spreadsheet.insertSheet(name);
  if (sheet.getLastColumn() < 1) {
    var headers = columns.map(function(column) { return String(column.header); });
    var descriptions = columns.map(function(column) { return String(column.description || ''); });
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    sheet.getRange(2, 1, 1, descriptions.length).setValues([descriptions]);
    if (sheet.setFrozenRows) sheet.setFrozenRows(2);
  } else {
    ttqsEnsureColumns_(sheet, columns);
  }
  return sheet;
}

function ttqsObservationColumns_() {
  return [
    { header: 'observation_id', description: 'Observation immutable internal ID; never derived from raw row number.' },
    { header: 'source_type', description: 'GOOGLE_FORM_SHEET in current TEST shadow mode.' },
    { header: 'source_kind', description: 'NEEDS / REGISTRATION / REACTION / FOLLOWUP30.' },
    { header: 'source_form_id', description: 'Google Form provider ID.' },
    { header: 'source_sheet_id', description: 'Linked raw response sheet ID; locator metadata only.' },
    { header: 'source_locator', description: 'Current raw locator for investigation; never used as source identity.' },
    { header: 'provider_timestamp', description: 'Provider timestamp normalized to UTC ISO-8601 with milliseconds.' },
    { header: 'payload_hash', description: 'SHA-256 of canonical expected form fields only.' },
    { header: 'source_key', description: 'SHA-256(form ID + provider timestamp + payload hash); idempotency identity.' },
    { header: 'observed_at', description: 'Time TTQS ONE first indexed the raw row.' },
    { header: 'processing_status', description: 'PENDING / ACCEPTED / QUARANTINED / REJECTED.' },
    { header: 'attempt_count', description: 'Reserved for future processing worker; shadow ingest starts at 0.' },
    { header: 'next_retry_at', description: 'Reserved for future scheduler retry.' },
    { header: 'last_error', description: 'Latest processing or source-integrity error.' },
    { header: 'processed_object_id', description: 'Future canonical object ID after accepted processing.' },
    { header: 'disposition', description: 'Final quarantine/rejection disposition when resolved.' }
  ];
}

function ttqsEnsureObservationSheet_() {
  ttqsAssertTestOnly_();
  return ttqsEnsureStructuredSheet_(ttqsOpenCore_(), ttqsConfig_().SHEETS.OBSERVATION, ttqsObservationColumns_());
}

function ttqsObservationProviderTimestamp_(value, displayValue) {
  if (value instanceof Date && !isNaN(value.getTime())) {
    return Utilities.formatDate(value, 'GMT', "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
  }
  return 'INVALID:' + String(displayValue || '');
}

function ttqsObservationSourceKey_(kind, formId, providerTimestamp, payloadHash) {
  return ttqsDigest_(JSON.stringify({
    sourceType: 'GOOGLE_FORM_SHEET',
    kind: String(kind),
    formId: String(formId),
    providerTimestamp: String(providerTimestamp),
    payloadHash: String(payloadHash)
  }));
}

function ttqsObservationCandidateFromValues_(sheetId, rowNumber, kind, formId, headers, displayValues, timestampValue) {
  var values = displayValues.map(String);
  var byCode = {};
  headers.forEach(function(header, index) {
    if (String(header) === 'TTQS_EVENT_ID') return;
    byCode[String(ttqsCanonicalFieldCode_(header))] = String(values[index] || '');
  });
  var expectedCodes = ttqsExpectedFieldCodes_(kind);
  var missing = expectedCodes.filter(function(code) { return !Object.prototype.hasOwnProperty.call(byCode, code); });
  if (missing.length) throw new Error('OBSERVATION_RAW_SCHEMA_MISMATCH:' + kind + ':' + missing.join(','));
  var payload = {};
  expectedCodes.forEach(function(code) { payload[code] = byCode[code]; });
  var payloadHash = ttqsDigest_(JSON.stringify(payload));
  var providerTimestamp = ttqsObservationProviderTimestamp_(timestampValue, values[0]);
  var timestampValid = providerTimestamp.indexOf('INVALID:') !== 0;
  var sourceKey = ttqsObservationSourceKey_(kind, formId, providerTimestamp, payloadHash);
  return {
    observation_id: ttqsStableId_('OBS-', Utilities.getUuid(), 24),
    source_type: 'GOOGLE_FORM_SHEET',
    source_kind: String(kind),
    source_form_id: String(formId),
    source_sheet_id: String(sheetId),
    source_locator: 'SHEET:' + String(sheetId) + ':ROW:' + String(rowNumber),
    provider_timestamp: providerTimestamp,
    payload_hash: payloadHash,
    source_key: sourceKey,
    observed_at: ttqsNow_(),
    processing_status: timestampValid ? 'PENDING' : 'QUARANTINED',
    attempt_count: 0,
    next_retry_at: '',
    last_error: timestampValid ? '' : 'PROVIDER_TIMESTAMP_INVALID',
    processed_object_id: '',
    disposition: ''
  };
}

function ttqsObservationCandidateFromRow_(sheet, rowNumber, kind, formId) {
  var lastColumn = sheet.getLastColumn();
  var headers = sheet.getRange(1, 1, 1, lastColumn).getDisplayValues()[0].map(String);
  var rowRange = sheet.getRange(rowNumber, 1, 1, lastColumn);
  var displayValues = rowRange.getDisplayValues()[0].map(String);
  var timestampValue = rowRange.getValues()[0][0];
  return ttqsObservationCandidateFromValues_(sheet.getSheetId(), rowNumber, kind, formId, headers, displayValues, timestampValue);
}

function ttqsObservationSourceDescriptors_() {
  var map = ttqsParseJson_(PropertiesService.getScriptProperties().getProperty('TTQS_RESPONSE_SHEET_MAP'), {});
  return Object.keys(map).map(function(sheetId) {
    var kind = String(map[sheetId]);
    return { sheetId: Number(sheetId), kind: kind, formId: ttqsFormIdForKind_(kind) };
  });
}

function ttqsObservationScanRaw_() {
  ttqsAssertTestOnly_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');
  var ss = ttqsOpenCore_();
  var sources = ttqsObservationSourceDescriptors_();
  var sheetsById = {};
  ss.getSheets().forEach(function(sheet) { sheetsById[String(sheet.getSheetId())] = sheet; });
  var candidates = [];
  var rawCount = 0;
  var rangeReadCalls = 0;
  var sourceStats = [];
  sources.forEach(function(source) {
    var sheet = sheetsById[String(source.sheetId)];
    if (!sheet) throw new Error('OBSERVATION_SOURCE_SHEET_MISSING:' + source.sheetId);
    var lastRow = sheet.getLastRow();
    var lastColumn = sheet.getLastColumn();
    var rows = Math.max(0, lastRow - 1);
    rawCount += rows;
    if (rawCount > Number(ttqsConfig_().OBSERVATION_SCAN_MAX_ROWS)) throw new Error('OBSERVATION_SHADOW_SCAN_LIMIT_EXCEEDED:' + rawCount);
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

function ttqsObservationAppendBatch_(sheet, objects) {
  if (!objects.length) return 0;
  var headers = ttqsHeaders_(sheet);
  var rows = objects.map(function(object) {
    return headers.map(function(header) { return Object.prototype.hasOwnProperty.call(object, header) ? object[header] : ''; });
  });
  var startRow = Math.max(3, sheet.getLastRow() + 1);
  sheet.getRange(startRow, 1, rows.length, headers.length).setValues(rows);
  return rows.length;
}

function ttqsObservationApplyCandidates_(candidates) {
  var sheet = ttqsEnsureObservationSheet_();
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
  return stats;
}

function ttqsObservationRawLocators_() {
  var ss = ttqsOpenCore_();
  var locators = {};
  ttqsObservationSourceDescriptors_().forEach(function(source) {
    var sheet = ss.getSheets().filter(function(item) { return item.getSheetId() === Number(source.sheetId); })[0];
    if (!sheet) throw new Error('OBSERVATION_SOURCE_SHEET_MISSING:' + source.sheetId);
    for (var rowNumber = 2; rowNumber <= sheet.getLastRow(); rowNumber++) {
      locators['SHEET:' + String(source.sheetId) + ':ROW:' + String(rowNumber)] = true;
    }
  });
  return locators;
}

function ttqsObservationReconcileShadow_() {
  var rawLocators = ttqsObservationRawLocators_();
  var rows = ttqsReadObjects_(ttqsEnsureObservationSheet_());
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

function ttqsScheduler() {
  ttqsAssertTestOnly_();
  if (ttqsConfig_().OBSERVATION_SHADOW_MODE !== true) throw new Error('OBSERVATION_SHADOW_MODE_REQUIRED');
  var startedAt = Date.now();
  var scan = ttqsObservationScanRaw_();
  var scannedAt = Date.now();
  var ingest = ttqsWithScriptLock_(function() { return ttqsObservationApplyCandidates_(scan.candidates); });
  var ingestedAt = Date.now();
  var reconciliation = ttqsObservationReconcileShadow_();
  var reconciledAt = Date.now();
  return {
    mode: 'OBSERVATION_SHADOW',
    sources: scan.sourceCount,
    raw_rows_scanned: scan.rawCount,
    read_strategy: scan.readStrategy,
    range_read_calls: scan.rangeReadCalls,
    source_stats: scan.sourceStats,
    timings_ms: {
      scan: scannedAt - startedAt,
      ingest: ingestedAt - scannedAt,
      reconcile: reconciledAt - ingestedAt,
      total: reconciledAt - startedAt
    },
    ingest: ingest,
    reconciliation: reconciliation,
    legacy_processing_unchanged: true
  };
}
