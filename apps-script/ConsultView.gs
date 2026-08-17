function ttqsIndicatorEvidenceMap_() {
  var evidenceRows = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.EVIDENCE));
  var map = {};
  for (var i = 1; i <= 19; i++) map[String(i)] = [];
  evidenceRows.forEach(function(entry) {
    var tags = String(entry.object.ttqs_indicator_tags || '').split(',').map(function(value) { return value.trim(); }).filter(Boolean);
    tags.forEach(function(tag) {
      if (map[tag]) map[tag].push(entry.object);
    });
  });
  return map;
}

function ttqsWebObservationByProcessedObject_() {
  var map = {};
  try {
    var rows = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.OBSERVATION));
    rows.forEach(function(entry) {
      var object = entry.object || {};
      var processedObjectId = String(object.processed_object_id || '').trim();
      if (processedObjectId && !map[processedObjectId]) map[processedObjectId] = object;
    });
  } catch (err) {
    return {};
  }
  return map;
}

function ttqsWebSafeDriveUrl_(value) {
  var url = String(value || '').trim();
  return /^https:\/\/(docs\.google\.com|drive\.google\.com)\//.test(url) ? url : '';
}

function ttqsWebEvidenceDetail_(evidence, observationByObject) {
  var sourceObjectId = String(evidence.source_object_id || '');
  var observation = observationByObject[sourceObjectId] || null;
  return {
    id: String(evidence.evidence_id || ''),
    title: String(evidence.evidence_title || evidence.evidence_id || '未命名佐證'),
    type: String(evidence.evidence_type || ''),
    dataClass: String(evidence.data_class || ''),
    health: String(evidence.health_status || ''),
    approvalStatus: String(evidence.approval_status || ''),
    sourceObjectType: String(evidence.source_object_type || ''),
    sourceObjectId: sourceObjectId,
    documentVersionId: String(evidence.document_version_id || ''),
    driveUrl: ttqsWebSafeDriveUrl_(evidence.drive_url),
    relation: 'SUPPORTS',
    relationBasis: 'EvidenceMaster.ttqs_indicator_tags 現行相容投影',
    observationId: observation ? String(observation.observation_id || '') : '',
    sourceKind: observation ? String(observation.source_kind || '') : '',
    sourceLocator: observation ? String(observation.source_locator || '') : '',
    providerTimestamp: observation ? String(observation.provider_timestamp || '') : '',
    processingStatus: observation ? String(observation.processing_status || '') : ''
  };
}

function ttqsRefreshConsultViewUnlocked_() {
  ttqsAssertTestOnly_();
  var indicators = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.INDICATORS));
  var evidenceMap = ttqsIndicatorEvidenceMap_();
  var consult = SpreadsheetApp.openById(ttqsConfig_().CONSULT_VIEW_SPREADSHEET_ID);
  var sheet = consult.getSheetByName(ttqsConfig_().AUTO_CONSULT_SHEET) || consult.insertSheet(ttqsConfig_().AUTO_CONSULT_SHEET);
  sheet.clearContents();
  var header = ['indicator_no', 'pddro_stage', 'indicator_title', 'evidence_ids', 'evidence_count', 'data_classes', 'health_summary', 'formal_status', 'refreshed_at', 'notes'];
  var out = [header];
  indicators.forEach(function(entry) {
    var no = String(entry.object.indicator_no);
    var evidence = evidenceMap[no] || [];
    var ids = evidence.map(function(item) { return item.evidence_id; }).filter(Boolean);
    var dataClasses = ttqsUnique_(evidence.map(function(item) { return item.data_class; }).filter(Boolean));
    var health = ttqsUnique_(evidence.map(function(item) { return item.health_status; }).filter(Boolean));
    var formalStatus = Number(no) >= 17 ? 'FORMAL_BLOCKED_NEEDS_REAL' : (evidence.length ? 'WORKING_EVIDENCE_AVAILABLE' : 'GAP');
    out.push([
      no,
      entry.object.pddro_stage,
      entry.object.indicator_title,
      ids.join(', '),
      ids.length,
      dataClasses.join(', '),
      health.join(', '),
      formalStatus,
      ttqsNow_(),
      'Auto index only; SAMPLE/CONTROL evidence is not a formal TTQS score.'
    ]);
  });
  sheet.getRange(1, 1, out.length, header.length).setValues(out);
  sheet.setFrozenRows(1);
  return { rows: out.length - 1, sheet: ttqsConfig_().AUTO_CONSULT_SHEET };
}

function ttqsRefreshConsultView() {
  return ttqsWithScriptLock_(ttqsRefreshConsultViewUnlocked_);
}

function ttqsWebEscape_(value) {
  return String(value === null || value === undefined ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function ttqsWebIndicatorStatus_(indicatorNo, evidenceCount) {
  var no = Number(indicatorNo);
  if (no >= 17) return evidenceCount > 0 ? '已有測試佐證；正式成果待實際營運' : '正式成果待實際營運';
  return evidenceCount > 0 ? '已有測試佐證' : '缺少佐證';
}

function ttqsWebIndicatorModel_(includeEvidenceDetails) {
  var indicators = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.INDICATORS));
  var evidenceMap = ttqsIndicatorEvidenceMap_();
  var observationByObject = includeEvidenceDetails ? ttqsWebObservationByProcessedObject_() : {};
  var byNo = {};
  indicators.forEach(function(entry) {
    byNo[String(entry.object.indicator_no)] = entry.object;
  });
  var out = [];
  for (var i = 1; i <= 19; i++) {
    var no = String(i);
    var definition = byNo[no] || {};
    var evidence = evidenceMap[no] || [];
    out.push({
      no: no,
      stage: String(definition.pddro_stage || ''),
      title: String(definition.indicator_title || ('指標 ' + no)),
      evidenceCount: evidence.length,
      evidence: includeEvidenceDetails ? evidence.map(function(item) { return ttqsWebEvidenceDetail_(item, observationByObject); }) : [],
      status: ttqsWebIndicatorStatus_(i, evidence.length)
    });
  }
  return out;
}

function ttqsWebCausalFlowModel_(indicators) {
  var byNo = {};
  indicators.forEach(function(item) { byNo[String(item.no)] = item; });
  var steps = [
    { step: '1', name: '需求蒐集', indicators: ['7'] },
    { step: '2', name: '需求／職能落差分析', indicators: ['8'] },
    { step: '3', name: '課程設計／目標／審查', indicators: ['9', '10', '11'] },
    { step: '4', name: '執行／資源／班次', indicators: ['12', '13', '14'] },
    { step: '5', name: '評量／檢討', indicators: ['15', '16', '17'] },
    { step: '6', name: '追蹤／改善', indicators: ['18', '19'] }
  ];
  return steps.map(function(item) {
    var covered = item.indicators.filter(function(no) {
      return byNo[no] && Number(byNo[no].evidenceCount || 0) > 0;
    }).length;
    return {
      step: item.step,
      name: item.name,
      indicators: item.indicators.join('、'),
      anchor: item.indicators[0],
      coverage: covered + ' / ' + item.indicators.length
    };
  });
}

function ttqsWebModuleModel_() {
  return [
    { name: '需求調查', state: '示範（SAMPLE）', note: '既有測試表單與問卷資料' },
    { name: '課程決策', state: '測試（TEST）', note: '沿用目前課程主檔／版本資料' },
    { name: '師資', state: '測試（TEST）', note: '先以現有課程與班次資料投影' },
    { name: '教材', state: '測試（TEST）', note: '沿用目前文件與版本資料' },
    { name: '招生', state: '示範（SAMPLE）', note: '既有測試報名表單' },
    { name: '班級', state: '示範（SAMPLE）', note: '目前示範班次資料' },
    { name: '出勤', state: '測試（TEST）', note: '沿用目前出勤評量資料' },
    { name: '評量', state: '測試（TEST）', note: '沿用目前出勤評量資料' },
    { name: '滿意度', state: '示範（SAMPLE）', note: '既有測試反應問卷' },
    { name: '結案', state: '原型', note: '先呈現里程碑，不宣稱正式結案能力' },
    { name: '追蹤', state: '示範（SAMPLE）', note: '既有測試追蹤問卷' },
    { name: '改善', state: '原型', note: '先呈現異常與改善入口' },
    { name: '19 指標', state: '測試（TEST）', note: '依現有佐證即時計算投影' },
    { name: '佐證主張與定位', state: '測試（TEST）', note: '由現行EvidenceMaster指標標籤投影SUPPORTS關係，下鑽至受控文件或Observation原始收件定位' }
  ];
}

function ttqsWebFormLaunchModel_() {
  var props = PropertiesService.getScriptProperties();
  var labels = { NEEDS: '需求調查', REGISTRATION: '課程報名', REACTION: '課後滿意度', FOLLOWUP30: '30 日追蹤' };
  return ['NEEDS', 'REGISTRATION', 'REACTION', 'FOLLOWUP30'].map(function(kind) {
    var formId = String(props.getProperty('TTQS_FORM_' + kind + '_ID') || '');
    if (!formId) return { kind: kind, label: labels[kind], url: '', status: '尚未建立' };
    try {
      var form = FormApp.openById(formId);
      var published = form.isPublished() === true;
      var url = published ? String(form.getPublishedUrl() || '') : '';
      return { kind: kind, label: labels[kind], url: url, status: published && url ? '可填答' : '需要檢查' };
    } catch (err) {
      return { kind: kind, label: labels[kind], url: '', status: '需要檢查' };
    }
  });
}

function ttqsWebHealthSummary_() {
  try {
    var health = ttqsHealthCheck();
    return {
      state: health && health.status === 'PASS' ? '正常' : '需要檢查',
      total: health && health.checks ? health.checks.length : 0,
      failed: health && health.failed ? health.failed.length : 0
    };
  } catch (err) {
    return { state: '需要檢查', total: 0, failed: 0 };
  }
}

function ttqsWebDashboardModel_(requestedView) {
  ttqsAssertTestOnly_();
  var view = String(requestedView || '').toLowerCase() === 'external' ? 'EXTERNAL_PREVIEW' : 'INTERNAL';
  var indicators = ttqsWebIndicatorModel_(view === 'INTERNAL');
  var covered = indicators.filter(function(item) { return item.evidenceCount > 0; }).length;
  return {
    version: ttqsConfig_().VERSION,
    environment: 'TEST',
    dataClass: '示範資料（SAMPLE）',
    view: view,
    indicators: indicators,
    causalFlow: ttqsWebCausalFlowModel_(indicators),
    coveredIndicators: covered,
    gapIndicators: 19 - covered,
    modules: view === 'INTERNAL' ? ttqsWebModuleModel_() : [],
    formLaunchers: view === 'INTERNAL' ? ttqsWebFormLaunchModel_() : [],
    health: view === 'INTERNAL' ? ttqsWebHealthSummary_() : null
  };
}

function ttqsWebEvidenceDetailHtml_(items) {
  if (!items || !items.length) return '';
  return '<div class="evidence-list">' + items.map(function(item) {
    var fileLink = item.driveUrl ? '<a class="source-link" target="_blank" rel="noopener noreferrer" href="' + ttqsWebEscape_(item.driveUrl) + '">開啟原始文件</a>' : '';
    var sourceObject = item.sourceObjectType || item.sourceObjectId
      ? '<div class="locator"><strong>系統來源</strong><code>' + ttqsWebEscape_(item.sourceObjectType + ':' + item.sourceObjectId) + '</code>' + (item.documentVersionId ? '<span>文件版本：' + ttqsWebEscape_(item.documentVersionId) + '</span>' : '') + '</div>'
      : '';
    var observation = item.sourceLocator
      ? '<div class="locator"><strong>原始收件定位</strong><code>' + ttqsWebEscape_(item.sourceLocator) + '</code>' + (item.observationId ? '<span>Observation：' + ttqsWebEscape_(item.observationId) + '</span>' : '') + (item.sourceKind ? '<span>來源類別：' + ttqsWebEscape_(item.sourceKind) + '</span>' : '') + (item.providerTimestamp ? '<span>來源時間：' + ttqsWebEscape_(item.providerTimestamp) + '</span>' : '') + (item.processingStatus ? '<span>處理狀態：' + ttqsWebEscape_(item.processingStatus) + '</span>' : '') + '</div>'
      : '';
    return '<details class="evidence-item"><summary><span>' + ttqsWebEscape_(item.id) + '</span>' + ttqsWebEscape_(item.title) + '</summary>' +
      '<div class="evidence-meta"><span>資料分類：' + ttqsWebEscape_(item.dataClass || '未標示') + '</span><span>證據類型：' + ttqsWebEscape_(item.type || '未標示') + '</span><span>健康狀態：' + ttqsWebEscape_(item.health || '未標示') + '</span><span>核准狀態：' + ttqsWebEscape_(item.approvalStatus || '未標示') + '</span></div>' +
      '<p class="relation-note">關係：' + ttqsWebEscape_(item.relation) + '；依據：' + ttqsWebEscape_(item.relationBasis) + '。此處只做TEST/SAMPLE追溯，不代表官方評分。</p>' +
      sourceObject + observation + fileLink + '</details>';
  }).join('') + '</div>';
}

function ttqsWebIndicatorCardsHtml_(indicators) {
  return indicators.map(function(item) {
    var tone = item.evidenceCount > 0 ? 'ok' : (Number(item.no) >= 17 ? 'wait' : 'gap');
    var drilldown = item.evidence && item.evidence.length ? '<details class="indicator-drill"><summary>查看佐證與來源（' + ttqsWebEscape_(item.evidence.length) + '）</summary>' + ttqsWebEvidenceDetailHtml_(item.evidence) + '</details>' : '';
    return '<article id="indicator-' + ttqsWebEscape_(item.no) + '" class="indicator ' + tone + '">' +
      '<div class="indicator-top"><span class="indicator-no">' + ttqsWebEscape_(item.no) + '</span><span class="stage">' + ttqsWebEscape_(item.stage) + '</span></div>' +
      '<h3>' + ttqsWebEscape_(item.title) + '</h3><p class="status">' + ttqsWebEscape_(item.status) + '</p><p class="count">佐證筆數：' + ttqsWebEscape_(item.evidenceCount) + '</p>' + drilldown + '</article>';
  }).join('');
}

function ttqsWebCausalFlowHtml_(steps) {
  if (!steps || !steps.length) return '';
  return '<section><div class="section-heading"><div><h2>SAMPLE 評核因果鏈</h2><p>需求→分析→課程設計→執行→評量→追蹤→改善；點擊任一步驟可跳到對應指標。</p></div></div><div class="flow-grid">' + steps.map(function(item) {
    return '<a class="flow-step" href="#indicator-' + ttqsWebEscape_(item.anchor) + '"><span>' + ttqsWebEscape_(item.step) + '</span><strong>' + ttqsWebEscape_(item.name) + '</strong><small>指標 ' + ttqsWebEscape_(item.indicators) + ' · 已有佐證 ' + ttqsWebEscape_(item.coverage) + '</small></a>';
  }).join('') + '</div></section>';
}

function ttqsWebModuleCardsHtml_(modules) {
  if (!modules.length) return '';
  return '<section><div class="section-heading"><h2>日常辦訓工作</h2><p>這些卡片是目前測試／示範能力（TEST／SAMPLE）投影，不代表正式營運已完成。</p></div><div class="module-grid">' + modules.map(function(item) {
    return '<article class="module"><div class="module-title"><h3>' + ttqsWebEscape_(item.name) + '</h3><span>' + ttqsWebEscape_(item.state) + '</span></div><p>' + ttqsWebEscape_(item.note) + '</p></article>';
  }).join('') + '</div></section>';
}

function ttqsWebFormLaunchHtml_(forms, health) {
  if (!forms.length) return '';
  var cards = forms.map(function(item) {
    var action = item.url ? '<a class="launch-action" target="_blank" rel="noopener noreferrer" href="' + ttqsWebEscape_(item.url) + '">開啟填答</a>' : '<span class="launch-action disabled">' + ttqsWebEscape_(item.status) + '</span>';
    return '<article class="launch-card"><div><span class="launch-state">' + ttqsWebEscape_(item.status) + '</span><h3>' + ttqsWebEscape_(item.label) + '</h3><p>使用 Google Forms 原生填答頁面；只使用示範資料（SAMPLE）。</p></div>' + action + '</article>';
  }).join('');
  var healthHtml = health ? '<div class="health-summary"><strong>系統狀態：' + ttqsWebEscape_(health.state) + '</strong><span>自動檢查 ' + ttqsWebEscape_(health.total) + ' 項；需檢查 ' + ttqsWebEscape_(health.failed) + ' 項</span></div>' : '';
  return '<section><div class="section-heading"><h2>顧問示範流程入口</h2><p>填答仍走 Google Forms 原生介面，不繞過既有測試處理流程（TEST）。</p></div>' + healthHtml + '<div class="launch-grid">' + cards + '</div></section>';
}

function ttqsRenderWebAppHtml_(model) {
  var externalPreview = model.view === 'EXTERNAL_PREVIEW';
  var viewTitle = externalPreview ? '外部唯讀預覽' : '內部辦訓總覽';
  var viewNote = externalPreview ? '目前僅為外部唯讀畫面預覽；尚未建立正式外部部署，也不讀取正式個資（REAL）。' : '目前為測試／示範資料（TEST／SAMPLE）內部畫面；所有正式資料寫入（REAL）仍停用。';
  var launchers = ttqsWebFormLaunchHtml_(model.formLaunchers || [], model.health);
  var modules = ttqsWebModuleCardsHtml_(model.modules);
  var causalFlow = ttqsWebCausalFlowHtml_(model.causalFlow || []);
  var indicators = ttqsWebIndicatorCardsHtml_(model.indicators);
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE</title><style>' +
    ':root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",sans-serif;color:#17202a;background:#f5f7f9}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f5f7f9}main{max-width:1180px;margin:0 auto;padding:24px}header,.module,.indicator,.launch-card,.stat,.flow-step{background:#fff;border:1px solid #dfe6ec;border-radius:14px}header{padding:24px;margin-bottom:18px}.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;color:#52606d}.title-row,.module-title,.indicator-top,.health-summary{display:flex;gap:12px;justify-content:space-between;align-items:center;flex-wrap:wrap}h1{margin:6px 0 4px;font-size:32px}h2{margin:0;font-size:22px}h3{margin:0;font-size:16px}.badge,.module-title span,.stage,.launch-state,.evidence-meta span{font-size:12px;font-weight:700;padding:4px 7px;border-radius:999px;background:#eef2f5}.notice{margin-top:16px;padding:14px 16px;border-radius:12px;background:#fff8e5;border:1px solid #f0d48a;line-height:1.55}.switch{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}.switch a,.launch-action,.source-link{text-decoration:none;color:#17202a;border:1px solid #c9d3dc;border-radius:10px;padding:9px 12px;background:#fff;font-weight:700}.switch a.active{border-color:#66788a;background:#eef2f5}.stats,.module-grid,.flow-grid,.indicator-grid,.launch-grid{display:grid;gap:12px}.stats{grid-template-columns:repeat(3,minmax(0,1fr));margin:18px 0}.module-grid,.flow-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.indicator-grid,.launch-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.stat,.module,.indicator,.launch-card,.flow-step{padding:16px}.stat strong{display:block;font-size:24px;margin-top:6px}.section-heading{margin:26px 0 12px}.section-heading p,.module p,.indicator p,.launch-card p{color:#5f6b76;line-height:1.5}.launch-card{display:flex;justify-content:space-between;gap:18px;align-items:center}.health-summary{background:#eef6ef;border:1px solid #cbdccc;border-radius:12px;padding:12px 14px;margin-bottom:12px}.indicator-no{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:#eef2f5;font-weight:800}.indicator.ok{border-left:5px solid #5b8c64}.indicator.gap{border-left:5px solid #a86464}.indicator.wait{border-left:5px solid #a98a4a}.flow-step{text-decoration:none;color:#17202a;display:grid;gap:6px}.flow-step>span{width:28px;height:28px;border-radius:50%;background:#eef2f5;display:flex;align-items:center;justify-content:center;font-weight:800}.flow-step small{color:#5f6b76}.indicator-drill{border-top:1px solid #e4e9ed;padding-top:10px}.indicator-drill>summary,.evidence-item>summary{cursor:pointer;font-weight:700}.evidence-list{display:grid;gap:8px;margin-top:10px}.evidence-item{border:1px solid #e1e7eb;border-radius:10px;padding:10px;background:#fafbfc}.evidence-item>summary span{display:inline-block;margin-right:8px;font-size:11px;padding:2px 6px;border-radius:999px;background:#eef2f5}.evidence-meta{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}.relation-note{font-size:12px}.locator{display:grid;gap:5px;margin:8px 0;padding:9px;border-radius:8px;background:#f1f4f6;font-size:12px}.locator code{white-space:normal;overflow-wrap:anywhere}.locator span{color:#5f6b76}.source-link{display:inline-block;font-size:12px;padding:7px 9px}.footnote{margin:24px 0 0;color:#68737d;font-size:13px;line-height:1.6}@media(max-width:820px){main{padding:14px}.stats,.module-grid,.flow-grid,.indicator-grid,.launch-grid{grid-template-columns:1fr}.launch-card{align-items:flex-start;flex-direction:column}h1{font-size:27px}}' +
    '</style></head><body><main><header><div class="title-row"><div><div class="eyebrow">TTQS ONE · 測試／示範資料（TEST／SAMPLE）</div><h1>' + ttqsWebEscape_(viewTitle) + '</h1><div>' + ttqsWebEscape_(viewNote) + '</div></div><div class="badge">版本 ' + ttqsWebEscape_(model.version) + '</div></div><div class="notice">此切換僅為內部測試預覽，不是權限控制。真正外部唯讀部署必須先完成伺服器函式隔離與發布安全驗證。</div><nav class="switch"><a class="' + (externalPreview ? '' : 'active') + '" href="?view=internal">內部辦訓總覽</a><a class="' + (externalPreview ? 'active' : '') + '" href="?view=external">外部唯讀預覽</a></nav></header>' +
    '<section class="stats"><div class="stat">資料分類<strong>' + ttqsWebEscape_(model.dataClass) + '</strong></div><div class="stat">已有測試佐證指標<strong>' + ttqsWebEscape_(model.coveredIndicators) + ' / 19</strong></div><div class="stat">目前缺少佐證指標<strong>' + ttqsWebEscape_(model.gapIndicators) + '</strong></div></section>' +
    launchers + modules + causalFlow + '<section><div class="section-heading"><h2>TTQS 19 指標佐證投影</h2><p>只呈現佐證狀態，不計算官方分數，也不宣稱評核結果。內部模式可展開每個指標的佐證與原始來源定位。</p></div><div class="indicator-grid">' + indicators + '</div></section>' +
    '<p class="footnote">目前畫面直接讀取既有測試／示範（TEST／SAMPLE）核心資料。外部預覽不等於正式唯讀快照；正式評核發布仍需獨立的唯讀快照與核准流程。</p></main></body></html>';
}

function ttqsWebErrorHtml_() {
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE</title></head><body><main style="max-width:760px;margin:40px auto;padding:24px;font-family:-apple-system,BlinkMacSystemFont,\"Segoe UI\",\"Noto Sans TC\",sans-serif"><h1>目前無法載入系統畫面</h1><p>請稍後再試；若持續發生，請聯絡系統管理者協助檢查。</p></main></body></html>';
}

function doGet(e) {
  try {
    var view = e && e.parameter ? e.parameter.view : '';
    var model = ttqsWebDashboardModel_(view);
    return HtmlService.createHtmlOutput(ttqsRenderWebAppHtml_(model)).setTitle('TTQS ONE').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  } catch (err) {
    return HtmlService.createHtmlOutput(ttqsWebErrorHtml_()).setTitle('TTQS ONE').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
}