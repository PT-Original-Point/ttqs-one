function ttqsFormDefinitions_() {
  return {
    NEEDS: {
      title: '[SAMPLE][TEST] TTQS ONE - Needs Survey',
      description: 'TEST SAMPLE only. Use aliases such as S-L01. Do not enter real names, email, phone, ID numbers, or medical information.'
    },
    REGISTRATION: {
      title: '[SAMPLE][TEST] TTQS ONE - Registration',
      description: 'TEST SAMPLE only. Use a synthetic alias such as S-L06. No real personal data.'
    },
    REACTION: {
      title: '[SAMPLE][TEST] TTQS ONE - Satisfaction',
      description: 'TEST SAMPLE only. Scores are demonstration data and are not formal TTQS outcomes.'
    },
    FOLLOWUP30: {
      title: '[SAMPLE][TEST] TTQS ONE - 30 Day Follow-up',
      description: 'TEST SAMPLE only. Do not enter real personal or medical information.'
    }
  };
}

function ttqsBuildFormItems_(form, kind) {
  form.addTextItem().setTitle('TTQS_ALIAS_CODE').setRequired(true);
  if (kind === 'NEEDS') {
    form.addScaleItem().setTitle('TTQS_NEED_SCORE').setBounds(1, 5).setLabels('Low', 'High').setRequired(true);
    form.addParagraphTextItem().setTitle('TTQS_NEED_TEXT').setRequired(false);
  } else if (kind === 'REGISTRATION') {
    form.addMultipleChoiceItem().setTitle('TTQS_SAMPLE_CONFIRM').setChoiceValues(['SAMPLE_ONLY']).setRequired(true);
  } else if (kind === 'REACTION') {
    ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL'].forEach(function(code) {
      form.addScaleItem().setTitle('TTQS_REACTION_' + code).setBounds(1, 5).setLabels('1', '5').setRequired(true);
    });
    form.addParagraphTextItem().setTitle('TTQS_REACTION_TEXT').setRequired(false);
  } else if (kind === 'FOLLOWUP30') {
    form.addScaleItem().setTitle('TTQS_30D_SAFE_ACTION').setBounds(1, 5).setLabels('1', '5').setRequired(true);
    form.addScaleItem().setTitle('TTQS_30D_BOUNDARY').setBounds(1, 5).setLabels('1', '5').setRequired(true);
    form.addParagraphTextItem().setTitle('TTQS_30D_TEXT').setRequired(false);
  } else {
    throw new Error('UNKNOWN_FORM_KIND:' + kind);
  }
}

function ttqsResponseSheetAfterDestination_(ss, beforeIds) {
  SpreadsheetApp.flush();
  Utilities.sleep(750);
  var after = ss.getSheets();
  for (var i = 0; i < after.length; i++) {
    if (beforeIds.indexOf(after[i].getSheetId()) === -1) return after[i];
  }
  throw new Error('FORM_RESPONSE_SHEET_NOT_CREATED');
}

function ttqsEnsureOneForm_(kind, def) {
  var props = PropertiesService.getScriptProperties();
  var formIdKey = 'TTQS_FORM_' + kind + '_ID';
  var sheetIdKey = 'TTQS_FORM_' + kind + '_SHEET_ID';
  var existingId = props.getProperty(formIdKey);
  var existingSheetId = props.getProperty(sheetIdKey);
  if (existingId && existingSheetId) {
    try {
      var existingForm = FormApp.openById(existingId);
      return { kind: kind, formId: existingId, responseSheetId: Number(existingSheetId), editUrl: existingForm.getEditUrl(), publishedUrl: existingForm.getPublishedUrl(), reused: true };
    } catch (err) {
      props.deleteProperty(formIdKey);
      props.deleteProperty(sheetIdKey);
    }
  }
  var ss = ttqsOpenCore_();
  var beforeIds = ss.getSheets().map(function(s) { return s.getSheetId(); });
  var form = FormApp.create(def.title);
  form.setDescription(def.description);
  form.setConfirmationMessage('SAMPLE TEST response captured. This is not formal REAL TTQS evidence.');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  ttqsBuildFormItems_(form, kind);
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ttqsConfig_().CORE_SPREADSHEET_ID);
  var responseSheet = ttqsResponseSheetAfterDestination_(ss, beforeIds);
  responseSheet.setName('RUNTIME_' + kind + '_RESPONSES');
  props.setProperty(formIdKey, form.getId());
  props.setProperty(sheetIdKey, String(responseSheet.getSheetId()));
  return { kind: kind, formId: form.getId(), responseSheetId: responseSheet.getSheetId(), editUrl: form.getEditUrl(), publishedUrl: form.getPublishedUrl(), reused: false };
}

function ttqsEnsureForms_() {
  ttqsAssertTestOnly_();
  var defs = ttqsFormDefinitions_();
  var forms = [];
  Object.keys(defs).forEach(function(kind) { forms.push(ttqsEnsureOneForm_(kind, defs[kind])); });
  var map = {};
  forms.forEach(function(f) { map[String(f.responseSheetId)] = f.kind; });
  PropertiesService.getScriptProperties().setProperty('TTQS_RESPONSE_SHEET_MAP', JSON.stringify(map));
  return forms;
}
