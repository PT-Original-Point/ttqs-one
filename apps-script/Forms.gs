function ttqsFormDefinitions_() {
  return {
    NEEDS: {
      title: '【顧問示範／測試資料】TTQS ONE－課前需求調查',
      description: '此表單用來展示 TTQS ONE 如何把課前需求自動帶入訓練資料與證據鏈。請只使用畫面提供的示範代碼與固定選項，不要填寫真實姓名、Email、電話、身分證字號、醫療資訊或其他個人資料。'
    },
    REGISTRATION: {
      title: '【顧問示範／測試資料】TTQS ONE－課程報名',
      description: '此表單用來展示報名資料如何進入 TTQS ONE 的班次與學員追蹤流程。請選擇系統提供的示範學員代碼；本表單不收集真實個人資料。'
    },
    REACTION: {
      title: '【顧問示範／測試資料】TTQS ONE－課後滿意度',
      description: '此表單用來展示課後反應資料如何形成可追溯的訓練成效紀錄。以下分數與回饋皆為示範資料，只用來展示 TTQS ONE 流程，不代表正式 TTQS 成果。'
    },
    FOLLOWUP30: {
      title: '【顧問示範／測試資料】TTQS ONE－30 日追蹤',
      description: '此表單用來展示課後追蹤如何延伸到行為與成果證據。請使用系統提供的示範選項，不要填寫真實個人、醫療或其他敏感資訊。'
    }
  };
}

function ttqsSampleAliasChoices_() {
  return ['S-L01', 'S-L02', 'S-L03', 'S-L04', 'S-L05', 'S-L06', 'S-L07'];
}

function ttqsFieldUiSpec_() {
  return {
    TTQS_ALIAS_CODE: {
      title: '示範學員代碼',
      type: 'MULTIPLE_CHOICE',
      help: '請選一個 S-Lxx 示範代碼，用來展示同一位學員如何跨表單被持續追蹤。',
      choices: ttqsSampleAliasChoices_()
    },
    TTQS_NEED_SCORE: {
      title: '本次課程需求程度',
      type: 'SCALE',
      help: '1 代表需求較低，5 代表需求較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_NEED_TEXT: {
      title: '最希望增加的內容',
      type: 'MULTIPLE_CHOICE',
      help: '請選一項示範需求，系統會把它連結到後續課程與證據資料。',
      choices: [
        '【示範】希望增加更多安全情境案例',
        '【示範】希望增加更多實作練習',
        '【示範】目前沒有其他需求'
      ]
    },
    TTQS_SAMPLE_CONFIRM: {
      title: '確認本次為示範填答',
      type: 'MULTIPLE_CHOICE',
      help: '這是顧問 DEMO 測試資料，不會作為正式 TTQS 證據。',
      choices: ['我確認：本次只使用示範資料，不填寫真實個資']
    },
    TTQS_REACTION_CLARITY: {
      title: '課程內容清楚度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_REACTION_RELEVANCE: {
      title: '課程內容與需求的相關程度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_REACTION_SAFETY: {
      title: '安全界線說明清楚度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_REACTION_PRACTICE: {
      title: '實作練習的幫助程度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_REACTION_OVERALL: {
      title: '整體滿意度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_REACTION_TEXT: {
      title: '本次課程回饋',
      type: 'MULTIPLE_CHOICE',
      help: '請選一項示範回饋，展示課後反應如何進入證據鏈。',
      choices: [
        '【示範】內容清楚，安全界線與實作方式容易理解',
        '【示範】情境演練有助於理解與應用',
        '【示範】目前沒有其他回饋'
      ]
    },
    TTQS_30D_SAFE_ACTION: {
      title: '30 日後安全行動實踐程度',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_30D_BOUNDARY: {
      title: '30 日後界線判斷信心',
      type: 'SCALE',
      help: '1 代表較低，5 代表較高。',
      lowLabel: '1｜較低',
      highLabel: '5｜較高'
    },
    TTQS_30D_TEXT: {
      title: '30 日後追蹤回饋',
      type: 'MULTIPLE_CHOICE',
      help: '請選一項示範追蹤結果，展示訓後資料如何延伸到成果證據。',
      choices: [
        '【示範】遇到不確定情境時，會先辨識警訊並尋求專業協助',
        '【示範】能依安全原則調整日常行為',
        '【示範】目前沒有其他追蹤回饋'
      ]
    }
  };
}

function ttqsFieldDisplayMap_() {
  var specs = ttqsFieldUiSpec_();
  var map = {};
  Object.keys(specs).forEach(function(code) { map[code] = specs[code].title; });
  return map;
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

function ttqsApplyItemUi_(item, code) {
  var spec = ttqsFieldUiSpec_()[String(code)];
  if (!spec) throw new Error('UNKNOWN_FORM_FIELD_CODE:' + code);
  if (spec.type === 'MULTIPLE_CHOICE') {
    if (item.getType() !== FormApp.ItemType.MULTIPLE_CHOICE) throw new Error('FORM_ITEM_TYPE_MISMATCH:' + code);
    item.asMultipleChoiceItem()
      .setTitle(spec.title)
      .setHelpText(spec.help)
      .setChoiceValues(spec.choices)
      .setRequired(true);
    return;
  }
  if (spec.type === 'SCALE') {
    if (item.getType() !== FormApp.ItemType.SCALE) throw new Error('FORM_ITEM_TYPE_MISMATCH:' + code);
    item.asScaleItem()
      .setTitle(spec.title)
      .setHelpText(spec.help)
      .setBounds(1, 5)
      .setLabels(spec.lowLabel, spec.highLabel)
      .setRequired(true);
    return;
  }
  throw new Error('UNKNOWN_FORM_FIELD_TYPE:' + code + ':' + spec.type);
}

function ttqsBuildFormItems_(form, kind) {
  ttqsExpectedFieldCodes_(kind).forEach(function(code) {
    var spec = ttqsFieldUiSpec_()[code];
    var item;
    if (spec.type === 'MULTIPLE_CHOICE') item = form.addMultipleChoiceItem();
    else if (spec.type === 'SCALE') item = form.addScaleItem();
    else throw new Error('UNKNOWN_FORM_FIELD_TYPE:' + code + ':' + spec.type);
    ttqsApplyItemUi_(item, code);
  });
}

function ttqsFormItemTitles_(form) {
  return form.getItems().map(function(item) { return String(item.getTitle()); });
}

function ttqsSyncExistingFormItems_(form, kind) {
  var items = form.getItems();
  var expectedCodes = ttqsExpectedFieldCodes_(kind);
  var currentCodes = items.map(function(item) { return ttqsCanonicalFieldCode_(item.getTitle()); });
  var sameShape = currentCodes.length === expectedCodes.length && currentCodes.every(function(code, i) { return code === expectedCodes[i]; });
  if (!sameShape) return false;
  items.forEach(function(item, i) { ttqsApplyItemUi_(item, expectedCodes[i]); });
  return true;
}

function ttqsPublishedPermissions_(formId) {
  var result = Drive.Permissions.list(String(formId), {
    includePermissionsForView: 'published',
    fields: 'permissions(id,type,role,view)'
  });
  return result && result.permissions ? result.permissions : [];
}

function ttqsIsAnyoneWithLinkResponderPermission_(permission) {
  return !!permission && permission.type === 'anyone' && permission.view === 'published' && permission.role === 'reader';
}

function ttqsEnsureAnyoneWithLinkResponder_(formId) {
  var before = ttqsPublishedPermissions_(formId);
  var exists = before.some(ttqsIsAnyoneWithLinkResponderPermission_);
  var created = false;
  if (!exists) {
    Drive.Permissions.create({
      type: 'anyone',
      view: 'published',
      role: 'reader'
    }, String(formId));
    created = true;
  }
  var after = ttqsPublishedPermissions_(formId);
  if (!after.some(ttqsIsAnyoneWithLinkResponderPermission_)) throw new Error('FORM_ANYONE_WITH_LINK_RESPONDER_NOT_CONFIRMED:' + formId);
  return { anyoneWithLinkResponder: true, permissionCreated: created };
}

function ttqsEnsureFormShape_(form, kind, def) {
  var shapeCompatible = ttqsSyncExistingFormItems_(form, kind);
  if (!shapeCompatible) {
    if (form.getResponses().length > 0) throw new Error('FORM_SCHEMA_MISMATCH_WITH_RESPONSES:' + kind);
    for (var i = form.getItems().length - 1; i >= 0; i--) form.deleteItem(i);
    ttqsBuildFormItems_(form, kind);
  }
  form.setTitle(def.title);
  form.setDescription(def.description);
  form.setConfirmationMessage('示範資料已送出。TTQS ONE 會把這筆 TEST／SAMPLE 回覆帶入後續追蹤與證據鏈展示；本資料不會作為正式 REAL TTQS 證據。');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setPublished(true);
  if (form.isPublished() !== true) throw new Error('FORM_NOT_PUBLISHED:' + kind);
  var publishedUrl = String(form.getPublishedUrl() || '');
  if (!publishedUrl) throw new Error('FORM_PUBLISHED_URL_EMPTY:' + kind);
  var responderAccess = ttqsEnsureAnyoneWithLinkResponder_(form.getId());
  return { publishedUrl: publishedUrl, responderAccess: responderAccess };
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

  var shape = ttqsEnsureFormShape_(form, kind, def);

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
    publishedUrl: shape.publishedUrl,
    anyoneWithLinkResponder: shape.responderAccess.anyoneWithLinkResponder,
    responderPermissionCreated: shape.responderAccess.permissionCreated,
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
