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
