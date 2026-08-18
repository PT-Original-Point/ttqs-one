var TTQS_EXTERNAL_SNAPSHOT_ID_ = '1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA';
var TTQS_EXTERNAL_SNAPSHOT_TITLE_ = 'TTQS ONE 外部唯讀快照（測試／示範）';
var TTQS_EXTERNAL_CAUSAL_SHEET_ = 'SAMPLE因果鏈';
var TTQS_EXTERNAL_SOURCE_SHEET_ = '佐證來源定位';

function ttqsExternalEscape_(value) {
  return String(value === null || value === undefined ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function ttqsExternalSafeSourceUrl_(value) {
  var url = String(value || '').trim();
  if (!url) return '';
  if (!/^https:\/\/(docs\.google\.com|drive\.google\.com)\//.test(url)) {
    throw new Error('SNAPSHOT_SOURCE_URL_UNSAFE');
  }
  return url;
}

function ttqsExternalRows_(range, width) {
  var response = Sheets.Spreadsheets.Values.get(TTQS_EXTERNAL_SNAPSHOT_ID_, range);
  var values = response && response.values ? response.values : [];
  return values.map(function(row) {
    var normalized = [];
    for (var i = 0; i < width; i++) normalized.push(String(row[i] === undefined ? '' : row[i]));
    return normalized;
  });
}

function ttqsExternalSummary_(rows) {
  if (!rows.length || rows[0][0] !== '欄位' || rows[0][1] !== '值') throw new Error('SNAPSHOT_SUMMARY_SCHEMA_MISMATCH');
  var summary = {};
  rows.slice(1).forEach(function(row) {
    if (row[0]) summary[row[0]] = row[1] || '';
  });
  return summary;
}

function ttqsExternalIndicators_(rows) {
  var expectedHeader = ['指標編號', 'PDDRO 階段', '指標名稱', '佐證筆數', '公開狀態', '來源更新時間'];
  if (rows.length !== 20 || JSON.stringify(rows[0]) !== JSON.stringify(expectedHeader)) throw new Error('SNAPSHOT_SCHEMA_MISMATCH');
  var seen = {};
  var indicators = rows.slice(1).map(function(row) {
    var no = row[0].trim();
    if (!/^(?:[1-9]|1[0-9])$/.test(no) || seen[no]) throw new Error('SNAPSHOT_INDICATOR_ID_INVALID');
    seen[no] = true;
    return { no: no, stage: row[1], title: row[2], evidenceCount: row[3] || '0', status: row[4], refreshedAt: row[5] };
  });
  if (indicators.length !== 19 || Object.keys(seen).length !== 19) throw new Error('SNAPSHOT_INDICATOR_COUNT_INVALID');
  return indicators;
}

function ttqsExternalCausalFlow_(rows) {
  var expectedHeader = ['步驟', '階段名稱', '對應指標', '代表佐證', '資料分類', '目前狀態', '說明'];
  var expectedSteps = [
    ['1', '需求蒐集', '7'],
    ['2', '需求／職能落差分析', '7、8'],
    ['3', '課程設計／目標／審查', '9、10、11'],
    ['4', '執行／資源／班次', '12、13、14'],
    ['5', '評量／檢討', '15、16、17'],
    ['6', '追蹤／改善', '18、19']
  ];
  if (rows.length !== 7 || JSON.stringify(rows[0]) !== JSON.stringify(expectedHeader)) throw new Error('SNAPSHOT_CAUSAL_SCHEMA_MISMATCH');
  return rows.slice(1).map(function(row, index) {
    var expected = expectedSteps[index];
    if (row[0] !== expected[0] || row[1] !== expected[1] || row[2] !== expected[2]) throw new Error('SNAPSHOT_CAUSAL_SEQUENCE_INVALID');
    if (row[4].indexOf('SAMPLE') === -1 || row[4].indexOf('REAL') !== -1) throw new Error('SNAPSHOT_CAUSAL_DATA_CLASS_INVALID');
    return { step: row[0], name: row[1], indicators: row[2], representativeEvidence: row[3], dataClass: row[4], status: row[5], note: row[6] };
  });
}

function ttqsExternalEvidence_(rows) {
  var expectedHeader = ['指標編號', 'evidence_id', '佐證名稱', '關係', '資料分類', '證據類型', '來源物件類型', '來源物件ID', 'Observation ID', '原始收件定位', '來源連結', '公開說明'];
  if (rows.length < 20 || rows.length > 120) throw new Error('SNAPSHOT_EVIDENCE_ROW_COUNT_INVALID');
  if (JSON.stringify(rows[0]) !== JSON.stringify(expectedHeader)) throw new Error('SNAPSHOT_EVIDENCE_SCHEMA_MISMATCH');
  var coverage = {};
  var items = [];
  rows.slice(1).forEach(function(row) {
    var no = row[0].trim();
    if (!no && row.join('').trim() === '') return;
    if (!/^(?:[1-9]|1[0-9])$/.test(no)) throw new Error('SNAPSHOT_EVIDENCE_INDICATOR_INVALID');
    if (row[3] !== 'SUPPORTS') throw new Error('SNAPSHOT_EVIDENCE_RELATION_INVALID');
    if (row[4] !== 'SAMPLE' && row[4] !== 'CONTROL') throw new Error('SNAPSHOT_EVIDENCE_DATA_CLASS_INVALID');
    var item = {
      indicatorNo: no,
      evidenceId: row[1],
      title: row[2],
      relation: 'SUPPORTS',
      dataClass: row[4],
      evidenceType: row[5],
      sourceObjectType: row[6],
      sourceObjectId: row[7],
      observationId: row[8],
      sourceLocator: row[9],
      sourceUrl: ttqsExternalSafeSourceUrl_(row[10]),
      publicNote: row[11]
    };
    if (!item.evidenceId || !item.title || !item.sourceObjectType || !item.sourceObjectId) throw new Error('SNAPSHOT_EVIDENCE_REQUIRED_FIELD_MISSING');
    coverage[no] = (coverage[no] || 0) + 1;
    items.push(item);
  });
  for (var i = 1; i <= 19; i++) if (!coverage[String(i)]) throw new Error('SNAPSHOT_EVIDENCE_COVERAGE_INVALID');
  return items;
}

function ttqsExternalSnapshotModel_() {
  var summaryRows = ttqsExternalRows_("'發布摘要'!A1:B10", 2);
  var indicatorRows = ttqsExternalRows_("'19指標佐證'!A1:F20", 6);
  var causalRows = ttqsExternalRows_("'" + TTQS_EXTERNAL_CAUSAL_SHEET_ + "'!A1:G7", 7);
  var evidenceRows = ttqsExternalRows_("'" + TTQS_EXTERNAL_SOURCE_SHEET_ + "'!A1:L120", 12);
  var indicators = ttqsExternalIndicators_(indicatorRows);
  var evidence = ttqsExternalEvidence_(evidenceRows);
  var byIndicator = {};
  indicators.forEach(function(item) { byIndicator[item.no] = []; });
  evidence.forEach(function(item) { byIndicator[item.indicatorNo].push(item); });
  indicators.forEach(function(item) { item.evidenceDetails = byIndicator[item.no] || []; });
  return {
    title: TTQS_EXTERNAL_SNAPSHOT_TITLE_,
    summary: ttqsExternalSummary_(summaryRows),
    indicators: indicators,
    causalFlow: ttqsExternalCausalFlow_(causalRows),
    evidence: evidence
  };
}

function ttqsExternalCausalHtml_(steps) {
  return '<section><div class="section-title"><h2>SAMPLE 評核因果鏈</h2><p>需求→分析→課程設計→執行→評量→追蹤→改善。所有內容皆為 TEST／SAMPLE，不得轉作 REAL 證據。</p></div><div class="flow">' + steps.map(function(item) {
    var anchor = item.indicators.split('、')[0];
    return '<a class="flow-step" href="#indicator-' + ttqsExternalEscape_(anchor) + '"><span>' + ttqsExternalEscape_(item.step) + '</span><strong>' + ttqsExternalEscape_(item.name) + '</strong><small>指標 ' + ttqsExternalEscape_(item.indicators) + ' · ' + ttqsExternalEscape_(item.status) + '</small><p>' + ttqsExternalEscape_(item.note) + '</p></a>';
  }).join('') + '</div></section>';
}

function ttqsExternalEvidenceHtml_(items) {
  if (!items || !items.length) return '<p class="empty">此指標目前沒有公開定位資料。</p>';
  return '<div class="evidence-list">' + items.map(function(item) {
    var source = '<div class="locator"><strong>來源物件</strong><code>' + ttqsExternalEscape_(item.sourceObjectType + ':' + item.sourceObjectId) + '</code></div>';
    var observation = item.observationId || item.sourceLocator ? '<div class="locator"><strong>原始收件定位</strong>' + (item.observationId ? '<span>Observation：' + ttqsExternalEscape_(item.observationId) + '</span>' : '') + (item.sourceLocator ? '<code>' + ttqsExternalEscape_(item.sourceLocator) + '</code>' : '') + '</div>' : '';
    var link = item.sourceUrl ? '<a class="source-link" target="_blank" rel="noopener noreferrer" href="' + ttqsExternalEscape_(item.sourceUrl) + '">開啟受控來源（依 Drive 權限）</a>' : '';
    return '<details class="evidence"><summary><span>' + ttqsExternalEscape_(item.evidenceId) + '</span>' + ttqsExternalEscape_(item.title) + '</summary><div class="tags"><b>' + item.relation + '</b><b>' + item.dataClass + '</b><b>' + ttqsExternalEscape_(item.evidenceType) + '</b></div>' + source + observation + (item.publicNote ? '<p class="note">' + ttqsExternalEscape_(item.publicNote) + '</p>' : '') + link + '</details>';
  }).join('') + '</div>';
}

function ttqsExternalRender_(model) {
  var cards = model.indicators.map(function(item) {
    var klass = Number(item.no) >= 17 ? 'outcome' : 'evidence-card';
    return '<article id="indicator-' + item.no + '" class="card ' + klass + '"><div class="top"><span class="no">' + item.no + '</span><span class="stage">' + ttqsExternalEscape_(item.stage) + '</span></div><h3>' + ttqsExternalEscape_(item.title) + '</h3><p class="status">' + ttqsExternalEscape_(item.status) + '</p><div class="meta"><span>索引佐證筆數：' + ttqsExternalEscape_(item.evidenceCount) + '</span><span>更新：' + ttqsExternalEscape_(item.refreshedAt) + '</span></div><details class="drill"><summary>查看佐證與來源（' + item.evidenceDetails.length + '）</summary>' + ttqsExternalEvidenceHtml_(item.evidenceDetails) + '</details></article>';
  }).join('');
  var runtimeLocators = model.evidence.filter(function(item) { return item.observationId && item.sourceLocator; }).length;
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE 外部唯讀</title><style>' +
    ':root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",sans-serif;color:#17202a;background:#f4f6f8}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f6f8}main{max-width:1180px;margin:auto;padding:22px}header,.card,.stat,.flow-step{background:#fff;border:1px solid #dce3e8;border-radius:16px}header{padding:24px;margin-bottom:16px}.eyebrow{font-size:13px;font-weight:800;color:#586674}h1{font-size:30px;margin:7px 0 8px}h2{font-size:22px}h3{font-size:16px}.notice{background:#fff7dd;border:1px solid #ead18a;border-radius:12px;padding:13px 15px;line-height:1.6}.security{background:#edf7ef;border:1px solid #c8dfcd;border-radius:12px;padding:13px 15px;line-height:1.6;margin-top:10px}.stats,.flow,.grid{display:grid;gap:11px}.stats{grid-template-columns:repeat(3,1fr);margin:16px 0}.stat{padding:14px}.stat strong{display:block;font-size:24px}.flow{grid-template-columns:repeat(3,1fr)}.flow-step{padding:15px;text-decoration:none;color:#17202a;display:grid;gap:6px}.grid{grid-template-columns:repeat(2,1fr)}.card{padding:16px;border-left:5px solid #60886b}.card.outcome{border-left-color:#a98945}.top{display:flex;justify-content:space-between}.no{font-weight:800}.stage,.tags b{font-size:12px;background:#eef2f5;padding:4px 8px;border-radius:999px}.meta,.note,.status,.flow-step small,.foot{color:#66737e;font-size:12px;line-height:1.55}.drill{border-top:1px solid #e1e7eb;margin-top:12px;padding-top:10px}.drill>summary,.evidence>summary{cursor:pointer;font-weight:800}.evidence-list{display:grid;gap:9px;margin-top:10px}.evidence{border:1px solid #e1e7eb;border-radius:10px;padding:10px;background:#fafbfc}.tags{display:flex;gap:5px;flex-wrap:wrap;margin:9px 0}.locator{display:grid;gap:4px;margin:7px 0;padding:8px;border-radius:8px;background:#f1f4f6;font-size:12px}.locator code{overflow-wrap:anywhere}.source-link{display:inline-block;margin-top:4px;text-decoration:none;color:#17202a;border:1px solid #c9d3dc;border-radius:9px;padding:7px 9px;background:#fff;font-size:12px;font-weight:800}@media(max-width:820px){main{padding:13px}.grid,.stats,.flow{grid-template-columns:1fr}}' +
    '</style></head><body><main><header><div class="eyebrow">TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</div><h1>' + ttqsExternalEscape_(model.title) + '</h1><div>用途：' + ttqsExternalEscape_(model.summary['用途']) + '</div><div class="notice">本畫面不計算 TTQS 官方分數，不宣稱評核通過或準備完成。17–19 的正式成果仍須以實際營運證據（REAL）為準。</div><div class="security">唯讀安全邊界：此 Web App 只透過 Google Sheets API 唯讀讀取去識別快照，不直接連線 TTQS ONE 核心資料庫、不讀取問卷原始回答，也不提供新增、修改、刪除、核准、正式啟動或背景工作控制。</div></header>' +
    '<section class="stats"><div class="stat">官方指標範圍<strong>19 / 19</strong></div><div class="stat">公開來源定位<strong>' + model.evidence.length + '</strong></div><div class="stat">TEST 原始收件定位<strong>' + runtimeLocators + '</strong></div></section>' +
    ttqsExternalCausalHtml_(model.causalFlow) + '<section><div class="section-title"><h2>19 指標佐證與來源下鑽</h2><p>每張卡片可展開去識別的 SUPPORTS 佐證、來源物件與可用的 Observation locator；來源文件連結仍受 Google Drive 本身權限控制。</p></div><div class="grid">' + cards + '</div></section><p class="foot">資料更新：' + ttqsExternalEscape_(model.summary['來源更新時間']) + '。資料分類：' + ttqsExternalEscape_(model.summary['資料分類']) + '。本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</p></main></body></html>';
}

function ttqsExternalErrorHtml_() {
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE 外部唯讀</title></head><body><main><h1>目前無法載入唯讀快照</h1><p>安全檢查未通過或資料暫時不可用。請聯絡承辦窗口協助確認。</p></main></body></html>';
}

function doGet() {
  try {
    return HtmlService.createHtmlOutput(ttqsExternalRender_(ttqsExternalSnapshotModel_())).setTitle('TTQS ONE 外部唯讀').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  } catch (err) {
    return HtmlService.createHtmlOutput(ttqsExternalErrorHtml_()).setTitle('TTQS ONE 外部唯讀').addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
}
