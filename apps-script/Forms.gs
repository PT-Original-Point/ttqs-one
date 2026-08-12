function ttqsFormDefinitions_() {
  return {
    NEEDS: {
      title: '【示範／測試】TTQS ONE－課前需求調查',
      description: '顧問 DEMO 用測試表單。請只使用畫面提供的示範代碼與選項，不要填寫真實姓名、Email、電話、身分證字號、醫療資訊或其他個人資料。'
    },
    REGISTRATION: {
      title: '【示範／測試】TTQS ONE－課程報名',
      description: '顧問 DEMO 用測試表單。請選擇系統提供的示範學員代碼；本表單不收集真實個人資料。'
    },
    REACTION: {
      title: '【示範／測試】TTQS ONE－課後滿意度',
      description: '顧問 DEMO 用測試表單。以下分數與回饋皆為示範資料，只用來展示 TTQS ONE 的流程與證據鏈，不代表正式 TTQS 成果。'
    },
    FOLLOWUP30: {
      title: '【示範／測試】TTQS ONE－30 日追蹤',
      description: '顧問 DEMO 用測試表單。請使用系統提供的示範選項，不要填寫真實個人、醫療或其他敏感資訊。'
    }
  };
}

function ttqsSampleAliasChoices_() {
  return ['S-L01', 'S-L02', 'S-L03', 'S-L04', 'S-L05', 'S-L06', 'S-L07'];
}

function ttqsFieldDisplayMap_() {
  return {
    TTQS_ALIAS_CODE: '示範學員代碼',
    TTQS_NEED_SCORE: '本次課程需求程度',
    TTQS_NEED_TEXT: '最希望增加的內容',
    TTQS_SAMPLE_CONFIRM: '確認本次為示範填答',
    TTQS_REACTION_CLARITY: '課程內容清楚度',
    TTQS_REACTION_RELEVANCE: '課程內容與需求的相關程度',
    TTQS_REACTION_SAFETY: '安全界線說明清楚度',
    TTQS_REACTION_PRACTICE: '實作練習的幫助程度',
    TTQS_REACTION_OVERALL: '整體滿意度',
    TTQS_REACTION_TEXT: '本次課程回饋',
    TTQS_30D_SAFE_ACTION: '30 日後安全行動實踐程度',
    TTQS_30D_BOUNDARY: '30 日後界線判斷信心',
    TTQS_30D_TEXT: '30 日後追蹤回饋'
  };
}

function ttqsDisplayTitleForCode_(code) {
  var map = ttqsFieldDisplayMap_();
  return String(map[String(code)] || code);
}

function ttqsCanonicalFieldCode_(title) {
  var value = String(title || '');
  var map = ttqsFieldDisplayMap_();
  if (Object.prototype.hasOwnProperty.call(map, value)) return value;
  var codes = Object.keys(map);
  for (var i = 0; i < codes.length; i++) {
    if (String(map[codes[i]]) === value) return codes[i];
  }
  return value;
}

function ttqsExpectedFieldCodes_(kind) {
  var common = ['TTQS_ALIAS_CODE'];
  if (kind === 'NEEDS') return common.concat(['TTQS_NEED_SCORE', 'TTQS_NEED_TEXT']);
  if (kind === 'REGISTRATION') return common.concat(['TTQS_SAMPLE_CONFIRM']);
  if (kind === 'REACTION') return common.concat(['TTQS_REACTION_CLARITY', 'TTQS_REACTION_RELEVANCE', 'TTQS_REACTION_SAFETY', 'TTQS_REACTION_PRACTICE', 'TTQS_REACTION_OVERALL', 'TTQS_REACTION_TEXT']);
  if (kind === 'FOLLOWUP30') return common.concat(['TTQS_30D_SAFE_ACTION', 'TTQS_30D_BOUNDARY', 'TTQS_30D_TEXT']);
  throw new Error('UNKNOWN_FORM_KIND:' + kind);
}

function ttqsExpectedFormTitles_(kind) {
  return ttqsExpectedFieldCodes_(kind).map(ttqsDisplayTitleForCode_);
}

function ttqsBuildFormItems_(form, kind) {
  form.addMultipleChoiceItem().setTitle(ttqsDisplayTitleForCode_('TTQS_ALIAS_CODE')).setChoiceValues(ttqsSampleAliasChoices_()).setRequired(true);
  if (kind === 'NEEDS') {
    form.addScaleItem().setTitle(ttqsDisplayTitleForCode_('TTQS_NEED_SCORE')).setBounds(1, 5).setLabels('較低', '較高').setRequired(true);
    form.addMultipleChoiceItem().setTitle(ttqsDisplayTitleForCode_('TTQS_NEED_TEXT')).setChoiceValues([
      '【示範】希望增加更多安全情境案例',
      '【示範】希望增加更多實作練習',
      '【示範】目前沒有其他需求'
    ]).setRequired(true);
  } else if (kind === 'REGISTRATION') {
    form.addMultipleChoiceItem().setTitle(ttqsDisplayTitleForCode_('TTQS_SAMPLE_CONFIRM')).setChoiceValues(['我確認：本次只使用示範資料，不填寫真實個資']).setRequired(true);
  } else if (kind === 'REACTION') {
    [
      'TTQS_REACTION_CLARITY',
      'TTQS_REACTION_RELEVANCE',
      'TTQS_REACTION_SAFETY',
      'TTQS_REACTION_PRACTICE',
      'TTQS_REACTION_OVERALL'
    ].forEach(function(code) {
      form.addScaleItem().setTitle(ttqsDisplayTitleForCode_(code)).setBounds(1, 5).setLabels('較低', '較高').setRequired(true);
    });
    form.addMultipleChoiceItem().setTitle(ttqsDisplayTitleForCode_('TTQS_REACTION_TEXT')).setChoiceValues([
      '【示範】內容清楚，安全界線與實作方式容易理解',
      '【示範】情境演練有助於理解與應用',
      '【示範】目前沒有其他回饋'
    ]).setRequired(true);
  } else if (kind === 'FOLLOWUP30') {
    form.addScaleItem().setTitle(ttqsDisplayTitleForCode_('TTQS_30D_SAFE_ACTION')).setBounds(1, 5).setLabels('較低', '較高').setRequired(true);
    form.addScaleItem().setTitle(ttqsDisplayTitleForCode_('TTQS_30D_BOUNDARY')).setBounds(1, 5).setLabels('較低', '較高').setRequired(true);
    form.addMultipleChoiceItem().setTitle(ttqsDisplayTitleForCode_('TTQS_30D_TEXT')).setChoiceValues([
      '【示範】遇到不確定情境時，會先辨識警訊並尋求專業協助',
      '【示範】能依安全原則調整日常行為',
      '【示範】目前沒有其他追蹤回饋'
    ]).setRequired(true);
  } else {
    throw new Error('UNKNOWN_FORM_KIND:' + kind);
  }
}

function ttqsFormItemTitles_(form) {
  return form.getItems().map(function(item) { return String(item.getTitle()); });
}

function ttqsNormalizeExistingFormTitles_(form, kind) {
  var items = form.getItems();
  var expectedCodes = ttqsExpectedFieldCodes_(kind);
  var currentCodes = items.map(function(item) { return ttqsCanonicalFieldCode_(item.getTitle()); });
  var sameShape = currentCodes.length === expectedCodes.length && currentCodes.every(function(code, i) { return code === expectedCodes[i]; });
  if (!sameShape) return false;
  items.forEach(function(item, i) {
    var displayTitle = ttqsDisplayTitleForCode_(expectedCodes[i]);
    if (String(item.getTitle()) !== displayTitle) item.setTitle(displayTitle);
  });
  return true;
}

function ttqsEnsureFormShape_(form, kind, def) {
  var shapeCompatible = ttqsNormalizeExistingFormTitles_(form, kind);
  if (!shapeCompatible) {
    if (form.getResponses().length > 0) throw new Error('FORM_SCHEMA_MISMATCH_WITH_RESPONSES:' + kind);
    for (var i = form.getItems().length - 1; i >= 0; i--) form.deleteItem(i);
    ttqsBuildFormItems_(form, kind);
  }
  form.setTitle(def.title);
  form.setDescription(def.description);
  form.setConfirmationMessage('示範資料已送出。這是 TTQS ONE TEST／SAMPLE 流程展示，不是正式 REAL TTQS 證據。');
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
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getDisplayValues()[0].map(function(header) {
    return ttqsCanonicalFieldCode_(header);
  });
  return ttqsExpectedFieldCodes_(kind).every(function(code) { return headers.indexOf(code) >= 0; });
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
