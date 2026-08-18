var TTQS_EXTERNAL_SOURCE_SNAPSHOT_ID_ = '1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA';
var TTQS_EXTERNAL_SNAPSHOT_TITLE_ = 'TTQS ONE 外部唯讀快照（測試／示範）';

var TTQS_EXTERNAL_SUMMARY_ = {
  '用途': '2026/09/01 顧問測試與外部唯讀畫面資料來源',
  '資料分類': '測試／示範／控制資料（TEST／SAMPLE／CONTROL）；不得視為正式營運（REAL）的正式評核證據',
  '來源': 'TTQS ONE TEST 核心之去識別人工 readback 投影：19指標摘要＋SAMPLE因果鏈＋佐證來源定位；外部 Viewer 不直連核心',
  '來源更新時間': '2026-08-18 07:14 台北時區（Asia/Taipei）；D7 外部顧問入口施工基線',
  '指標範圍': '1–19；19/19 均至少有一筆去識別 SUPPORTS 來源定位；另含 4 條真實 Google Forms TEST submission 的 Observation locator',
  '17–19 狀態': '已有測試佐證；正式成果仍待實際營運，不宣稱正式達成',
  '評分聲明': '本唯讀快照不計算 TTQS 官方分數、不宣稱「通過」或「已準備完成」、不建議委員評分',
  '個資': '本檔不含學員姓名、電子郵件、電話、身分證字號或問卷原始回答；runtime 只公開不可逆識別碼、Observation ID 與原始收件 locator'
};

var TTQS_EXTERNAL_INDICATORS_ = [
  ['1','規劃','訓練機構未來經營方向及目標之訂定','4','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['2','規劃','對外明確的訓練政策','4','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['3','規劃','明確的 PDDRO 訓練課程及明確的核心訓練類別','4','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['4','規劃','訓練品質管理的系統化文件資訊','13','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['5','規劃','訓練規劃及經營目標的連結性','4','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['6','規劃','訓練機構的行政管理能力及訓練主管相關職能','10','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['7','設計','訓練需求相關的職能分析及應用','9','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['8','設計','訓練方案的系統設計','5','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['9','設計','利益關係人的參與過程','5','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['10','設計','訓練資源的採購程序及甄選標準','5','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['11','設計','訓練計畫及目標需求的結合','9','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['12','執行','訓練內涵按計畫執行的程度','10','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['13','執行','提供學習成果移轉的建議或協助','6','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['14','執行','訓練資料分類與建檔及管理資訊系統化','13','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['15','查核','評估報告及定期性綜合分析','7','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['16','查核','管控及異常矯正處理','14','已有測試佐證（非正式評分）','2026-08-15 14:40:37'],
  ['17','成果','訓練成果評估的多元性和完整性','10','已有測試佐證；正式成果待實際營運','2026-08-15 14:40:37'],
  ['18','成果','訓練系統的一般性功能─目標客戶及學員的評價','6','已有測試佐證；正式成果待實際營運','2026-08-15 14:40:37'],
  ['19','成果','訓練系統的市場功能─目標市場及顧客的價值創造','4','已有測試佐證；正式成果待實際營運','2026-08-15 14:40:37']
];

var TTQS_EXTERNAL_CAUSAL_ = [
  ['1','需求蒐集','7','EV-RUN-A1788F62F85532C2；EV-S001-012','TEST／SAMPLE','可追溯','由真實 Google Forms TEST 提交與 SAMPLE 需求/職能落差文件示範需求來源；不是 REAL 市場需求。'],
  ['2','需求／職能落差分析','7、8','EV-S001-012；EV-S001-002','TEST／SAMPLE','可追溯','SAMPLE 落差分析連到訓練目標與方案設計；T Gate 前不得據此鎖定 REAL 課程。'],
  ['3','課程設計／目標／審查','9、10、11','EV-S001-013；EV-S001-014；EV-S001-012','TEST／SAMPLE','可追溯','利益關係人、資源甄選與需求→目標→評量追溯均為合成 SAMPLE 情境。'],
  ['4','執行／資源／班次','12、13、14','EV-S001-014；EV-S001-005；EV-RUN-D72493E5294CD5B2','TEST／SAMPLE','可追溯','班次與資源為 SAMPLE；另含真實 Google Forms TEST 報名 submission 的去識別定位。'],
  ['5','評量／檢討','15、16、17','EV-S001-006；EV-S001-011；EV-RUN-574145BB8CD6BF6F','TEST／SAMPLE','可追溯','反應評估、異常控制與 SAMPLE 結案分析形成 Review/Outcome 示範；不代表正式成果。'],
  ['6','追蹤／改善','18、19','EV-S001-009；EV-S001-010；EV-S001-011；EV-RUN-99545B2AB6B10D3F','TEST／SAMPLE','可追溯','30日追蹤與市場/顧客價值皆為 SAMPLE；正式 17–19 成果仍待 REAL 營運。']
];

var TTQS_EXTERNAL_EVIDENCE_ = [
  ['1','EV-S001-001','SAMPLE 年度目標與課程方向連結','SUPPORTS','SAMPLE','STRUCTURED_DATA','AnnualGoal','SAMPLE-AG-2026-001','','','','結構化 SAMPLE 來源；非正式協會年度目標。'],
  ['2','EV-S001-001','SAMPLE 年度目標與課程方向連結','SUPPORTS','SAMPLE','STRUCTURED_DATA','AnnualGoal','SAMPLE-AG-2026-001','','','','結構化 SAMPLE 來源；非正式訓練政策。'],
  ['3','EV-S001-002','SAMPLE 課程需求、設計與目標','SUPPORTS','SAMPLE','STRUCTURED_DATA','CourseVersion','SAMPLE-CV-001','','','','SAMPLE 課程設計；T Gate 前不得轉為 REAL 課程。'],
  ['4','EV-POLPROC-001','TTQS ONE 制度政策與19程序主手冊 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-POLPROC-20260817T230900','','','https://docs.google.com/document/d/1TzJVJrw-K7OoCLgIe18JGdI-QyDa3UGRkU9Khog87SQ/edit','CURRENT 工作版；不是已正式核准制度。連結權限另由 D7 驗收。'],
  ['5','EV-S001-001','SAMPLE 年度目標與課程方向連結','SUPPORTS','SAMPLE','STRUCTURED_DATA','AnnualGoal','SAMPLE-AG-2026-001','','','','SAMPLE 目標與訓練規劃連結。'],
  ['6','EV-GOV-CTRL-001','TTQS ONE 治理控制手冊 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-GOV-CTRL-20260818T004500','','','https://docs.google.com/document/d/1fvocxiyS-_-fqs_1P835tai1jA_aBlqHDKKoxeYVUTI/edit','治理控制工作版；正式制度仍依必要 A 核准。連結權限另由 D7 驗收。'],
  ['7','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','合成 SAMPLE 需求/落差文件；非 REAL 市場需求。'],
  ['7','EV-RUN-A1788F62F85532C2','TEST SAMPLE runtime needs response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-A1788F62F85532','OBS-5DF457DAE87CE85418F35E8B','SHEET:1145488986:ROW:5','','真實 Google Forms TEST submission 的去識別索引；ACCEPTED，非正式證據。'],
  ['8','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','需求→目標→評量追溯 SAMPLE 示範。'],
  ['9','EV-S001-013','SAMPLE 利益關係人參與與課程審查','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','4 類虛構利益關係人；REAL 需真實參與證據。'],
  ['10','EV-S001-014','SAMPLE 講師教材場地資源甄選與切合','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','SAMPLE 資源甄選與切合；非 REAL 採購/資格。'],
  ['11','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','需求與訓練目標結合 SAMPLE 示範。'],
  ['11','EV-RUN-A1788F62F85532C2','TEST SAMPLE runtime needs response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-A1788F62F85532','OBS-5DF457DAE87CE85418F35E8B','SHEET:1145488986:ROW:5','','TEST needs submission；只公開不可逆識別資訊與 locator，不公開回覆內容。'],
  ['12','EV-S001-014','SAMPLE 講師教材場地資源甄選與切合','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','SAMPLE 執行資源；非正式班次。'],
  ['12','EV-RUN-D72493E5294CD5B2','TEST SAMPLE runtime registration response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-D72493E5294CD5','OBS-0BDC55AF857F2A31861AF73F','SHEET:1407831401:ROW:7','','真實 Google Forms TEST 報名 submission 去識別定位；SCHEDULER_PROCESSED。'],
  ['13','EV-S001-005','SAMPLE 班次執行與學習成果移轉','SUPPORTS','SAMPLE','STRUCTURED_DATA','ClassRun','SAMPLE-CLASS-001','','','','班次、出勤與追蹤皆為 SAMPLE。'],
  ['13','EV-RUN-99545B2AB6B10D3F','TEST SAMPLE runtime 30-day behavior response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-99545B2AB6B10D','OBS-B6FCD3304656E8618BD552CA','SHEET:332084943:ROW:2','','真實 Google Forms TEST 30日追蹤 submission 去識別定位；ACCEPTED。'],
  ['14','EV-ARCH-001','TTQS ONE 系統架構與平台對接說明 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-ARCH-20260817T230900','','','https://docs.google.com/document/d/1XP1xagkTb5MSn7IgL9d5ekmI8FYw4XNTsHktZgZiC3M/edit','CURRENT 架構控制文件；連結權限另由 D7 驗收。'],
  ['15','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','SAMPLE 結案文件；非 REAL 正式實績。'],
  ['15','EV-RUN-574145BB8CD6BF6F','TEST SAMPLE runtime reaction response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-574145BB8CD6BF','OBS-05BA7E0619D4E63D86151795','SHEET:480064116:ROW:3','','真實 Google Forms TEST 反應 submission 去識別定位；ACCEPTED。'],
  ['16','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','SAMPLE 異常/改善閉環；不代表正式治理核准。'],
  ['17','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','正式成果仍待 REAL；此列只示範 TEST/SAMPLE 追溯。'],
  ['17','EV-RUN-574145BB8CD6BF6F','TEST SAMPLE runtime reaction response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-574145BB8CD6BF','OBS-05BA7E0619D4E63D86151795','SHEET:480064116:ROW:3','','TEST/SAMPLE 反應評估來源；不可作正式成果。'],
  ['18','EV-RUN-99545B2AB6B10D3F','TEST SAMPLE runtime 30-day behavior response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-99545B2AB6B10D','OBS-B6FCD3304656E8618BD552CA','SHEET:332084943:ROW:2','','TEST/SAMPLE 30日追蹤；正式學員評價待 REAL。'],
  ['19','EV-S001-010','SAMPLE 市場／顧客價值回饋','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-SUR-011','','','','1筆虛構合作單位/目標客戶回饋；正式市場價值待 REAL。']
];

function ttqsExternalEscape_(value) {
  return String(value === null || value === undefined ? '' : value)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function ttqsExternalSafeSourceUrl_(value) {
  var url = String(value || '').trim();
  if (!url) return '';
  if (!/^https:\/\/(docs\.google\.com|drive\.google\.com)\//.test(url)) throw new Error('SNAPSHOT_SOURCE_URL_UNSAFE');
  return url;
}

function ttqsExternalSnapshotModel_() {
  if (TTQS_EXTERNAL_INDICATORS_.length !== 19) throw new Error('SNAPSHOT_INDICATOR_COUNT_INVALID');
  if (TTQS_EXTERNAL_CAUSAL_.length !== 6) throw new Error('SNAPSHOT_CAUSAL_SEQUENCE_INVALID');
  var seen = {};
  var indicators = TTQS_EXTERNAL_INDICATORS_.map(function(row) {
    var no = row[0];
    if (!/^(?:[1-9]|1[0-9])$/.test(no) || seen[no]) throw new Error('SNAPSHOT_INDICATOR_ID_INVALID');
    seen[no] = true;
    return {no:no, stage:row[1], title:row[2], evidenceCount:row[3], status:row[4], refreshedAt:row[5], evidenceDetails:[]};
  });
  var expectedCausal = [['1','需求蒐集','7'],['2','需求／職能落差分析','7、8'],['3','課程設計／目標／審查','9、10、11'],['4','執行／資源／班次','12、13、14'],['5','評量／檢討','15、16、17'],['6','追蹤／改善','18、19']];
  var causalFlow = TTQS_EXTERNAL_CAUSAL_.map(function(row, index) {
    var expected = expectedCausal[index];
    if (row[0] !== expected[0] || row[1] !== expected[1] || row[2] !== expected[2]) throw new Error('SNAPSHOT_CAUSAL_SEQUENCE_INVALID');
    if (row[4].indexOf('SAMPLE') === -1 || row[4].indexOf('REAL') !== -1) throw new Error('SNAPSHOT_CAUSAL_DATA_CLASS_INVALID');
    return {step:row[0], name:row[1], indicators:row[2], representativeEvidence:row[3], dataClass:row[4], status:row[5], note:row[6]};
  });
  var coverage = {};
  var byIndicator = {};
  indicators.forEach(function(item) { byIndicator[item.no] = []; });
  var evidence = TTQS_EXTERNAL_EVIDENCE_.map(function(row) {
    var no = row[0];
    if (!/^(?:[1-9]|1[0-9])$/.test(no)) throw new Error('SNAPSHOT_EVIDENCE_INDICATOR_INVALID');
    if (row[3] !== 'SUPPORTS') throw new Error('SNAPSHOT_EVIDENCE_RELATION_INVALID');
    if (row[4] !== 'SAMPLE' && row[4] !== 'CONTROL') throw new Error('SNAPSHOT_EVIDENCE_DATA_CLASS_INVALID');
    var item = {indicatorNo:no,evidenceId:row[1],title:row[2],relation:row[3],dataClass:row[4],evidenceType:row[5],sourceObjectType:row[6],sourceObjectId:row[7],observationId:row[8],sourceLocator:row[9],sourceUrl:ttqsExternalSafeSourceUrl_(row[10]),publicNote:row[11]};
    if (!item.evidenceId || !item.title || !item.sourceObjectType || !item.sourceObjectId) throw new Error('SNAPSHOT_EVIDENCE_REQUIRED_FIELD_MISSING');
    coverage[no] = (coverage[no] || 0) + 1;
    byIndicator[no].push(item);
    return item;
  });
  for (var i = 1; i <= 19; i++) if (!coverage[String(i)]) throw new Error('SNAPSHOT_EVIDENCE_COVERAGE_INVALID');
  indicators.forEach(function(item) { item.evidenceDetails = byIndicator[item.no]; });
  return {title:TTQS_EXTERNAL_SNAPSHOT_TITLE_, summary:TTQS_EXTERNAL_SUMMARY_, indicators:indicators, causalFlow:causalFlow, evidence:evidence};
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
    '</style></head><body><main><header><div class="eyebrow">TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</div><h1>' + ttqsExternalEscape_(model.title) + '</h1><div>用途：' + ttqsExternalEscape_(model.summary['用途']) + '</div><div class="notice">本畫面不計算 TTQS 官方分數，不宣稱評核通過或準備完成。17–19 的正式成果仍須以實際營運證據（REAL）為準。</div><div class="security">唯讀安全邊界：此 Web App 僅呈現部署版本內嵌的去識別唯讀快照，不在執行期呼叫 Google Sheets／Drive API、不直接連線 TTQS ONE 核心資料庫、不讀取問卷原始回答，也不提供新增、修改、刪除、核准、正式啟動或背景工作控制。</div></header>' +
    '<section class="stats"><div class="stat">官方指標範圍<strong>19 / 19</strong></div><div class="stat">公開來源定位<strong>' + model.evidence.length + '</strong></div><div class="stat">TEST 原始收件定位<strong>' + runtimeLocators + '</strong></div></section>' +
    ttqsExternalCausalHtml_(model.causalFlow) + '<section><div class="section-title"><h2>19 指標佐證與來源下鑽</h2><p>每張卡片可展開去識別的 SUPPORTS 佐證、來源物件與可用的 Observation locator；來源文件連結仍受 Google Drive 本身權限控制。</p></div><div class="grid">' + cards + '</div></section><p class="foot">資料更新：' + ttqsExternalEscape_(model.summary['來源更新時間']) + '。資料分類：' + ttqsExternalEscape_(model.summary['資料分類']) + '。來源快照：' + ttqsExternalEscape_(TTQS_EXTERNAL_SOURCE_SNAPSHOT_ID_) + '。本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</p></main></body></html>';
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
