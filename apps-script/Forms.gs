function ttqsFormDefinitions_() {
  return {
    NEEDS: {
      title: '[SAMPLE][TEST] TTQS ONE - Needs Survey',
      description: 'TEST SAMPLE only. All responses are controlled SAMPLE values. Do not enter real names, email, phone, ID numbers, or medical information.'
    },
    REGISTRATION: {
      title: '[SAMPLE][TEST] TTQS ONE - Registration',
      description: 'TEST SAMPLE only. Select a synthetic alias. No real personal data.'
    },
    REACTION: {
      title: '[SAMPLE][TEST] TTQS ONE - Satisfaction',
      description: 'TEST SAMPLE only. Scores and controlled SAMPLE choices are demonstration data and are not formal TTQS outcomes.'
    },
    FOLLOWUP30: {
      title: '[SAMPLE][TEST] TTQS ONE - 30 Day Follow-up',
      description: 'TEST SAMPLE only. All narrative content is selected from controlled SAMPLE choices. Do not enter real personal or medical information.'
    }
  };
}

function ttqsSampleAliasChoices_() {
  return ['S-L01', 'S-L02', 'S-L03', 'S-L04', 'S-L05', 'S-L06', 'S-L07'];
}

function ttqsExpectedFormTitles_(kind) {
  var common = ['TTQS_ALIAS_CODE'];
  if (kind === 'NEEDS') return common.concat(['TTQS_NEED_SCORE', 'TTQS_NEED_TEXT']);
  if (kind === 'REGISTRATION') return common.concat(['TTQS_SAMPLE_CONFIRM']);
  if (kind === 'REACTION') return common.concat(['TTQS_REACTION_CLARITY', 'TTQS_REACTION_RELEVANCE', 'TTQS_REACTION_SAFETY', 'TTQS_REACTION_PRACTICE', 'TTQS_REACTION_OVERALL', 'TTQS_REACTION_TEXT']);
  if (kind === 'FOLLOWUP30') return common.concat(['TTQS_30D_SAFE_ACTION', 'TTQS_30D_BOUNDARY', 'TTQS_30D_TEXT']);
  throw new Error('UNKNOWN_FORM_KIND:' + kind);
}

function ttqsBuildFormItems_(form, kind) {
  form.addMultipleChoiceItem().setTitle('TTQS_ALIAS_CODE').setChoiceValues(ttqsSampleAliasChoices_()).setRequired(true);
  if (kind === 'NEEDS') {
    form.addScaleItem().setTitle('TTQS_NEED_SCORE').setBounds(1, 5).setLabels('Low', 'High').setRequired(true);
    form.addMultipleChoiceItem().setTitle('TTQS_NEED_TEXT').setChoiceValues([
      'SAMPLE：希望增加更多安全情境案例',
      'SAMPLE：希望增加更多實作練習',
      'SAMPLE：無其他需求'
    ]).setRequired(true);
  } else if (kind === 'REGISTRATION') {
    form.addMultipleChoiceItem().setTitle('TTQS_SAMPLE_CONFIRM').setChoiceValues(['SAMPLE_ONLY']).setRequired(true);
  } else if (kind === 'REACTION') {
    ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL'].forEach(function(code) {
      form.addScaleItem().setTitle('TTQS_REACTION_' + code).setBounds(1, 5).setLabels('1', '5').setRequired(true);
    });
    form.addMultipleChoiceItem().setTitle('TTQS_REACTION_TEXT').setChoiceValues([
      'SAMPLE：內容清楚，安全界線與實作方式容易理解',
      'SAMPLE：情境演練有助於理解',
      'SAMPLE：無其他回饋'
    ]).setRequired(true);
  } else if (kind === 'FOLLOWUP30') {
    form.addScaleItem().setTitle('TTQS_30D_SAFE_ACTION').setBounds(1, 5).setLabels('1', '5').setRequired(true);
    form.addScaleItem().setTitle('TTQS_30D_BOUNDARY').setBounds(1, 5).setLabels('1', '5').setRequired(true);
    form.addMultipleChoiceItem().setTitle('TTQS_30D_TEXT').setChoiceValues([
      'SAMPLE：遇到不確定情境時會先辨識警訊並尋求專業協助',
      'SAMPLE：能依安全原則調整日常行為',
      'SAMPLE：無其他追蹤回饋'
    ]).setRequired(true);
  } else {
    throw new Error('UNKNOWN_FORM_KIND:' + kind);
  }
}

function ttqsFormItemTitles_(form) {
  return form.getItems().map(function(item) { return String(item.getTitle()); });
}

function ttqsEnsureFormShape_(form, kind, def) {
  var expected = ttqsExpectedFormTitles_(kind);
  var current = ttqsFormItemTitles_(form);
  var same = current.length === expected.length && current.every(function(title, i) { return title === expected[i]; });
  if (!same) {
    if (form.getResponses().length > 0) throw new Error('FORM_SCHEMA_MISMATCH_WITH_RESPONSES:' + kind);
    for (var i = form.getItems().length - 1; i >= 0; i--) form.deleteItem(i);
    ttqsBuildFormItems_(form, kind);
  }
  form.setTitle(def.title);
  form.setDescription(def.description);
  form.setConfirmationMessage('SAMPLE TEST response captured. This is not formal REAL TTQS evidence.');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setPublished(true);
  if (form.isPublished() !== true) throw new Error('FORM_NOT_PUBLISHED:' + kind);
  var publishedUrl = String(form.getPublishedUrl() || '');
  if (!publishedUrl) throw new Error('FORM_PUBLISHED_URL_EMPTY:' + kind);
  return publishedUrl;
}

function ttqsSheetMatchesFormKind_(sheet, kind) {
  if (!sheet || sheet.getLastColumn() < 1 || sheet.getLastRow() < 1) return false;
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getDisplayValues()[0].map(String);
  return ttqsExpectedFormTitles_(kind).every(function(title) { return headers.indexOf(title) >= 0; });
}

function ttqsMatchingResponseSheets_(ss, kind) {
  return ss.getSheets().filter(function(sheet) { return ttqsSheetMatchesFormKind_(sheet, kind); });
}

function ttqsResponseSheetAfterDestination_(ss, beforeIds, kind) {
  var cfg = ttqsConfig_();
  var deadline = new Date().getTime() + Number(cfg.FORM_RESPONSE_WAIT_MS);
  while (true) {
    SpreadsheetApp.flush();
    var created = ss.getSheets().filter(function(sheet) {
      return beforeIds.indexOf(sheet.getSheetId()) === -1 && ttqsSheetMatchesFormKind_(sheet, kind);
    });
    if (created.length === 1) return created[0];
    if (created.length > 1) throw new Error('FORM_RESPONSE_SHEET_AMBIGUOUS:' + kind + ':' + created.length);
    if (new Date().getTime() >= deadline) break;
    Utilities.sleep(Number(cfg.FORM_RESPONSE_POLL_MS));
  }
  throw new Error('FORM_RESPONSE_SHEET_NOT_CREATED_WITHIN_TIMEOUT:' + kind);
}

function ttqsWaitForExistingResponseSheet_(ss, kind) {
  var cfg = ttqsConfig_();
  var deadline = new Date().getTime() + Number(cfg.FORM_RESPONSE_WAIT_MS);
  while (true) {
    SpreadsheetApp.flush();
    var matches = ttqsMatchingResponseSheets_(ss, kind);
    if (matches.length === 1) return matches[0];
    if (matches.length > 1) throw new Error('FORM_RESPONSE_SHEET_AMBIGUOUS:' + kind + ':' + matches.length);
    if (new Date().getTime() >= deadline) break;
    Utilities.sleep(Number(cfg.FORM_RESPONSE_POLL_MS));
  }
  throw new Error('FORM_RESPONSE_SHEET_RECOVERY_TIMEOUT:' + kind);
}

function ttqsFindSheetById_(ss, sheetId) {
  var id = Number(sheetId);
  return ss.getSheets().filter(function(sheet) { return sheet.getSheetId() === id; })[0] || null;
}

function ttqsNameResponseSheet_(ss, responseSheet, kind) {
  var expectedName = 'RUNTIME_' + kind + '_RESPONSES';
  var collision = ss.getSheetByName(expectedName);
  if (collision && collision.getSheetId() !== responseSheet.getSheetId()) {
    throw new Error('FORM_RESPONSE_SHEET_NAME_COLLISION:' + kind + ':' + collision.getSheetId());
  }
  if (responseSheet.getName() !== expectedName) responseSheet.setName(expectedName);
  return responseSheet;
}

function ttqsFormDestinationSnapshot_(form) {
  try {
    return {
      id: String(form.getDestinationId() || ''),
      type: form.getDestinationType()
    };
  } catch (err) {
    var message = String(err && err.message ? err.message : err).toLowerCase();
    if (message.indexOf('no response destination') !== -1) return { id: '', type: null };
    throw err;
  }
}

function ttqsEnsureOneForm_(kind, def) {
  var props = PropertiesService.getScriptProperties();
  var formIdKey = 'TTQS_FORM_' + kind + '_ID';
  var sheetIdKey = 'TTQS_FORM_' + kind + '_SHEET_ID';
  var existingId = props.getProperty(formIdKey);
  var existingSheetId = props.getProperty(sheetIdKey);
  if (!existingId && existingSheetId) {
    throw new Error('FORM_ORPHAN_SHEET_STATE_REQUIRES_REPAIR:' + kind + ':' + existingSheetId);
  }

  var ss = ttqsOpenCore_();
  var form;
  var createdNow = false;
  if (existingId) {
    form = FormApp.openById(existingId);
  } else {
    form = FormApp.create(def.title);
    props.setProperty(formIdKey, form.getId());
    createdNow = true;
  }

  var publishedUrl = ttqsEnsureFormShape_(form, kind, def);

  var destination = ttqsFormDestinationSnapshot_(form);
  var destinationId = destination.id;
  var destinationType = destination.type;
  var responseSheet = null;

  if (existingSheetId) {
    if (String(destinationId || '') !== String(ttqsConfig_().CORE_SPREADSHEET_ID) || destinationType !== FormApp.DestinationType.SPREADSHEET) {
      throw new Error('FORM_DESTINATION_MISMATCH:' + kind + ':' + String(destinationId || 'NONE'));
    }
    responseSheet = ttqsFindSheetById_(ss, existingSheetId);
    if (!responseSheet) throw new Error('FORM_RESPONSE_SHEET_MISSING:' + kind + ':' + existingSheetId);
    if (!ttqsSheetMatchesFormKind_(responseSheet, kind)) throw new Error('FORM_RESPONSE_SHEET_SCHEMA_MISMATCH:' + kind + ':' + existingSheetId);
  } else if (destinationId) {
    if (String(destinationId) !== String(ttqsConfig_().CORE_SPREADSHEET_ID) || destinationType !== FormApp.DestinationType.SPREADSHEET) {
      throw new Error('FORM_DESTINATION_MISMATCH:' + kind + ':' + String(destinationId));
    }
    responseSheet = ttqsWaitForExistingResponseSheet_(ss, kind);
    props.setProperty(sheetIdKey, String(responseSheet.getSheetId()));
  } else {
    var beforeIds = ss.getSheets().map(function(sheet) { return sheet.getSheetId(); });
    form.setDestination(FormApp.DestinationType.SPREADSHEET, ttqsConfig_().CORE_SPREADSHEET_ID);
    responseSheet = ttqsResponseSheetAfterDestination_(ss, beforeIds, kind);
    props.setProperty(sheetIdKey, String(responseSheet.getSheetId()));
  }

  ttqsNameResponseSheet_(ss, responseSheet, kind);
  return {
    kind: kind,
    formId: form.getId(),
    responseSheetId: responseSheet.getSheetId(),
    editUrl: form.getEditUrl(),
    published: form.isPublished() === true,
    publishedUrl: publishedUrl,
    reused: !createdNow,
    recoveredPartialState: !!existingId && !existingSheetId
  };
}

function ttqsEnsureForms_() {
  ttqsAssertTestOnly_();
  var defs = ttqsFormDefinitions_();
  var forms = [];
  Object.keys(defs).forEach(function(kind) { forms.push(ttqsEnsureOneForm_(kind, defs[kind])); });
  var map = {};
  forms.forEach(function(form) { map[String(form.responseSheetId)] = form.kind; });
  PropertiesService.getScriptProperties().setProperty('TTQS_RESPONSE_SHEET_MAP', JSON.stringify(map));
  return forms;
}
