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

function ttqsWebIndicatorModel_() {
  var indicators = ttqsReadObjects_(ttqsGetSheet_(ttqsConfig_().SHEETS.INDICATORS));
  var evidenceMap = ttqsIndicatorEvidenceMap_();
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
      status: ttqsWebIndicatorStatus_(i, evidence.length)
    });
  }
  return out;
}

function ttqsWebModuleModel_() {
  return [
    { name: '需求調查', state: 'SAMPLE', note: '既有測試表單與問卷資料' },
    { name: '課程決策', state: 'TEST', note: '沿用目前課程主檔／版本資料' },
    { name: '師資', state: 'TEST', note: '先以現有課程與班次資料投影' },
    { name: '教材', state: 'TEST', note: '沿用目前文件與版本資料' },
    { name: '招生', state: 'SAMPLE', note: '既有測試報名表單' },
    { name: '班級', state: 'SAMPLE', note: '目前示範班次資料' },
    { name: '出勤', state: 'TEST', note: '沿用目前出勤評量資料' },
    { name: '評量', state: 'TEST', note: '沿用目前出勤評量資料' },
    { name: '滿意度', state: 'SAMPLE', note: '既有測試反應問卷' },
    { name: '結案', state: '原型', note: '先呈現里程碑，不宣稱正式結案能力' },
    { name: '追蹤', state: 'SAMPLE', note: '既有測試追蹤問卷' },
    { name: '改善', state: '原型', note: '先呈現異常與改善入口' },
    { name: '19 指標', state: 'TEST', note: '依現有佐證即時計算投影' },
    { name: '佐證主張與定位', state: '原型', note: '待精簡核心資料架構正式落地' }
  ];
}

function ttqsWebDashboardModel_(requestedView) {
  ttqsAssertTestOnly_();
  var view = String(requestedView || '').toLowerCase() === 'external' ? 'EXTERNAL_PREVIEW' : 'INTERNAL';
  var indicators = ttqsWebIndicatorModel_();
  var covered = indicators.filter(function(item) { return item.evidenceCount > 0; }).length;
  return {
    version: ttqsConfig_().VERSION,
    environment: 'TEST',
    dataClass: 'SAMPLE',
    view: view,
    indicators: indicators,
    coveredIndicators: covered,
    gapIndicators: 19 - covered,
    modules: view === 'INTERNAL' ? ttqsWebModuleModel_() : []
  };
}

function ttqsWebIndicatorCardsHtml_(indicators) {
  return indicators.map(function(item) {
    var tone = item.evidenceCount > 0 ? 'ok' : (Number(item.no) >= 17 ? 'wait' : 'gap');
    return '<article class="indicator ' + tone + '">' +
      '<div class="indicator-top"><span class="indicator-no">' + ttqsWebEscape_(item.no) + '</span><span class="stage">' + ttqsWebEscape_(item.stage) + '</span></div>' +
      '<h3>' + ttqsWebEscape_(item.title) + '</h3>' +
      '<p class="status">' + ttqsWebEscape_(item.status) + '</p>' +
      '<p class="count">佐證筆數：' + ttqsWebEscape_(item.evidenceCount) + '</p>' +
    '</article>';
  }).join('');
}

function ttqsWebModuleCardsHtml_(modules) {
  if (!modules.length) return '';
  return '<section><div class="section-heading"><h2>日常辦訓工作</h2><p>這些卡片是目前 TEST／SAMPLE 能力投影，不代表正式營運已完成。</p></div>' +
    '<div class="module-grid">' + modules.map(function(item) {
      return '<article class="module"><div class="module-title"><h3>' + ttqsWebEscape_(item.name) + '</h3><span>' + ttqsWebEscape_(item.state) + '</span></div><p>' + ttqsWebEscape_(item.note) + '</p></article>';
    }).join('') + '</div></section>';
}

function ttqsRenderWebAppHtml_(model) {
  var externalPreview = model.view === 'EXTERNAL_PREVIEW';
  var viewTitle = externalPreview ? '外部唯讀預覽' : '內部辦訓總覽';
  var viewNote = externalPreview
    ? '目前僅為外部唯讀畫面預覽；尚未建立正式外部部署，也不讀取 REAL 個資。'
    : '目前為 TEST／SAMPLE 內部畫面；所有 REAL 寫入仍停用。';
  var modules = ttqsWebModuleCardsHtml_(model.modules);
  var indicators = ttqsWebIndicatorCardsHtml_(model.indicators);
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' +
    '<title>TTQS ONE</title><style>' +
    ':root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",sans-serif;color:#17202a;background:#f5f7f9}*{box-sizing:border-box}body{margin:0;background:#f5f7f9}main{max-width:1180px;margin:0 auto;padding:24px}header{background:#fff;border:1px solid #dfe6ec;border-radius:18px;padding:24px;margin-bottom:18px}.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;color:#52606d}.title-row{display:flex;gap:16px;justify-content:space-between;align-items:flex-start;flex-wrap:wrap}h1{margin:6px 0 4px;font-size:32px}h2{margin:0;font-size:22px}h3{margin:0;font-size:16px}.badge{display:inline-flex;gap:8px;align-items:center;padding:8px 12px;border-radius:999px;background:#eef2f5;font-size:13px;font-weight:700}.notice{margin:16px 0 0;padding:14px 16px;border-radius:12px;background:#fff8e5;border:1px solid #f0d48a;line-height:1.55}.switch{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}.switch a{text-decoration:none;color:#17202a;border:1px solid #c9d3dc;border-radius:10px;padding:9px 12px;background:#fff}.switch a.active{font-weight:700;border-color:#66788a;background:#eef2f5}.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0}.stat{background:#fff;border:1px solid #dfe6ec;border-radius:14px;padding:16px}.stat strong{display:block;font-size:24px;margin-top:6px}.section-heading{display:flex;justify-content:space-between;gap:20px;align-items:end;margin:26px 0 12px}.section-heading p{margin:0;color:#5f6b76}.module-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.module,.indicator{background:#fff;border:1px solid #dfe6ec;border-radius:14px;padding:16px}.module-title,.indicator-top{display:flex;justify-content:space-between;gap:10px;align-items:center}.module-title span,.stage{font-size:12px;font-weight:700;padding:4px 7px;border-radius:999px;background:#eef2f5}.module p,.indicator p{color:#5f6b76;line-height:1.45}.indicator-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.indicator-no{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:#eef2f5;font-weight:800}.indicator.ok{border-left:5px solid #5b8c64}.indicator.gap{border-left:5px solid #a86464}.indicator.wait{border-left:5px solid #a98a4a}.status{min-height:42px}.count{font-size:13px;margin-bottom:0}.footnote{margin:24px 0 0;color:#68737d;font-size:13px;line-height:1.6}@media(max-width:820px){main{padding:14px}.stats,.module-grid,.indicator-grid{grid-template-columns:1fr}.section-heading{display:block}.section-heading p{margin-top:6px}h1{font-size:27px}}' +
    '</style></head><body><main><header><div class="title-row"><div><div class="eyebrow">TTQS ONE · TEST / SAMPLE</div><h1>' + ttqsWebEscape_(viewTitle) + '</h1><div>' + ttqsWebEscape_(viewNote) + '</div></div><div class="badge">版本 ' + ttqsWebEscape_(model.version) + '</div></div>' +
    '<div class="notice">此切換僅為內部測試預覽，不是權限控制。真正外部唯讀部署必須先完成伺服器函式隔離與發布安全驗證。</div>' +
    '<nav class="switch"><a class="' + (externalPreview ? '' : 'active') + '" href="?view=internal">內部辦訓總覽</a><a class="' + (externalPreview ? 'active' : '') + '" href="?view=external">外部唯讀預覽</a></nav></header>' +
    '<section class="stats"><div class="stat">資料分類<strong>' + ttqsWebEscape_(model.dataClass) + '</strong></div><div class="stat">已有測試佐證指標<strong>' + ttqsWebEscape_(model.coveredIndicators) + ' / 19</strong></div><div class="stat">目前缺少佐證指標<strong>' + ttqsWebEscape_(model.gapIndicators) + '</strong></div></section>' +
    modules +
    '<section><div class="section-heading"><h2>TTQS 19 指標佐證投影</h2><p>只呈現佐證狀態，不計算官方分數，也不宣稱評核結果。</p></div><div class="indicator-grid">' + indicators + '</div></section>' +
    '<p class="footnote">目前畫面直接讀取既有 TEST／SAMPLE 核心資料。外部預覽不等於正式 Snapshot；正式評核發布仍需獨立的唯讀快照與核准流程。</p>' +
    '</main></body></html>';
}

function doGet(e) {
  var view = e && e.parameter ? e.parameter.view : '';
  var model = ttqsWebDashboardModel_(view);
  return HtmlService.createHtmlOutput(ttqsRenderWebAppHtml_(model))
    .setTitle('TTQS ONE')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}
