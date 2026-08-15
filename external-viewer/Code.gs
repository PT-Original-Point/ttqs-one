var TTQS_EXTERNAL_SNAPSHOT_ID_ = '1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA';
var TTQS_EXTERNAL_SNAPSHOT_TITLE_ = 'TTQS ONE 外部唯讀快照（測試／示範）';

function ttqsExternalEscape_(value) {
  return String(value === null || value === undefined ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function ttqsExternalSnapshotModel_() {
  var book = SpreadsheetApp.openById(TTQS_EXTERNAL_SNAPSHOT_ID_);
  var summarySheet = book.getSheetByName('發布摘要');
  var indicatorSheet = book.getSheetByName('19指標佐證');
  if (!summarySheet || !indicatorSheet) throw new Error('SNAPSHOT_SCHEMA_MISSING');

  var summaryRows = summarySheet.getRange(1, 1, 10, 2).getDisplayValues();
  var indicatorRows = indicatorSheet.getRange(1, 1, 20, 6).getDisplayValues();
  var expectedHeader = ['指標編號', 'PDDRO 階段', '指標名稱', '佐證筆數', '公開狀態', '來源更新時間'];
  if (indicatorRows.length !== 20 || JSON.stringify(indicatorRows[0]) !== JSON.stringify(expectedHeader)) {
    throw new Error('SNAPSHOT_SCHEMA_MISMATCH');
  }

  var summary = {};
  summaryRows.slice(1).forEach(function(row) {
    if (row[0]) summary[String(row[0])] = String(row[1] || '');
  });
  var indicators = indicatorRows.slice(1).map(function(row) {
    return {
      no: String(row[0]),
      stage: String(row[1]),
      title: String(row[2]),
      evidenceCount: String(row[3]),
      status: String(row[4]),
      refreshedAt: String(row[5])
    };
  });
  if (indicators.length !== 19) throw new Error('SNAPSHOT_INDICATOR_COUNT_INVALID');

  return {
    title: TTQS_EXTERNAL_SNAPSHOT_TITLE_,
    summary: summary,
    indicators: indicators
  };
}

function ttqsExternalRender_(model) {
  var cards = model.indicators.map(function(item) {
    var outcome = Number(item.no) >= 17;
    var klass = outcome ? 'outcome' : 'evidence';
    return '<article class="card ' + klass + '">' +
      '<div class="top"><span class="no">' + ttqsExternalEscape_(item.no) + '</span><span class="stage">' + ttqsExternalEscape_(item.stage) + '</span></div>' +
      '<h2>' + ttqsExternalEscape_(item.title) + '</h2>' +
      '<p class="status">' + ttqsExternalEscape_(item.status) + '</p>' +
      '<div class="meta"><span>佐證筆數：' + ttqsExternalEscape_(item.evidenceCount) + '</span><span>更新：' + ttqsExternalEscape_(item.refreshedAt) + '</span></div>' +
    '</article>';
  }).join('');

  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' +
    '<title>TTQS ONE 外部唯讀</title><style>' +
    ':root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",sans-serif;color:#17202a;background:#f4f6f8}*{box-sizing:border-box}body{margin:0;background:#f4f6f8}main{max-width:1100px;margin:0 auto;padding:22px}header{background:#fff;border:1px solid #dce3e8;border-radius:18px;padding:22px;margin-bottom:16px}.eyebrow{font-size:13px;font-weight:800;letter-spacing:.08em;color:#586674}h1{font-size:30px;margin:7px 0 8px}.notice{background:#fff7dd;border:1px solid #ead18a;border-radius:12px;padding:13px 15px;line-height:1.55;margin-top:14px}.summary{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:16px 0}.summary div{background:#fff;border:1px solid #dce3e8;border-radius:12px;padding:14px}.summary strong{display:block;font-size:13px;color:#65717d;margin-bottom:5px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:11px}.card{background:#fff;border:1px solid #dce3e8;border-radius:14px;padding:15px;border-left:5px solid #60886b}.card.outcome{border-left-color:#a98945}.top{display:flex;justify-content:space-between;gap:8px;align-items:center}.no{width:32px;height:32px;border-radius:50%;background:#eef2f5;display:flex;align-items:center;justify-content:center;font-weight:800}.stage{font-size:12px;font-weight:700;background:#eef2f5;padding:4px 8px;border-radius:999px}.card h2{font-size:16px;line-height:1.45}.status{min-height:46px;color:#485662;line-height:1.45}.meta{display:flex;flex-direction:column;gap:3px;font-size:12px;color:#6b7782}.foot{margin:20px 0 0;font-size:13px;color:#66737e;line-height:1.55}@media(max-width:820px){main{padding:13px}.grid,.summary{grid-template-columns:1fr}h1{font-size:25px}}' +
    '</style></head><body><main><header><div class="eyebrow">TTQS ONE · 測試／示範資料（TEST／SAMPLE）· 外部唯讀</div><h1>' + ttqsExternalEscape_(model.title) + '</h1>' +
    '<div>用途：' + ttqsExternalEscape_(model.summary['用途']) + '</div>' +
    '<div class="notice">本畫面不計算 TTQS 官方分數，不宣稱評核通過或準備完成。17–19 的正式成果仍須以實際營運證據為準。</div></header>' +
    '<section class="summary"><div><strong>資料分類</strong>' + ttqsExternalEscape_(model.summary['資料分類']) + '</div><div><strong>來源更新時間</strong>' + ttqsExternalEscape_(model.summary['來源更新時間']) + '</div><div><strong>指標範圍</strong>' + ttqsExternalEscape_(model.summary['指標範圍']) + '</div><div><strong>17–19 狀態</strong>' + ttqsExternalEscape_(model.summary['17–19 狀態']) + '</div></section>' +
    '<section class="grid">' + cards + '</section><p class="foot">本唯讀檢視器僅讀取去識別快照，不直接連線 TTQS ONE 核心資料庫，也不提供新增、修改、刪除、核准、正式啟動或背景工作控制功能。</p>' +
    '</main></body></html>';
}

function ttqsExternalErrorHtml_() {
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE 外部唯讀</title></head><body><main style="max-width:760px;margin:40px auto;padding:24px;font-family:-apple-system,BlinkMacSystemFont,\"Segoe UI\",\"Noto Sans TC\",sans-serif"><h1>目前無法載入唯讀快照</h1><p>請稍後再試；若持續發生，請聯絡承辦窗口協助確認。</p></main></body></html>';
}

function doGet() {
  try {
    var model = ttqsExternalSnapshotModel_();
    return HtmlService.createHtmlOutput(ttqsExternalRender_(model))
      .setTitle('TTQS ONE 外部唯讀')
      .addMetaTag('viewport', 'width=device-width, initial-scale=1');
  } catch (err) {
    return HtmlService.createHtmlOutput(ttqsExternalErrorHtml_())
      .setTitle('TTQS ONE 外部唯讀')
      .addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
}
