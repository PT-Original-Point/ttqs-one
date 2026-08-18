var TTQS_EXTERNAL_SOURCE_SNAPSHOT_ID_ = '1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA';
var TTQS_EXTERNAL_SNAPSHOT_TITLE_ = 'TTQS ONE 外部唯讀快照（測試／示範）';

var TTQS_EXTERNAL_SUMMARY_ = {
  '用途': '2026/09/01 顧問 TEST／SAMPLE 實機驗收的外部唯讀入口',
  '資料分類': '測試／示範／控制資料（TEST／SAMPLE／CONTROL）；不得視為正式營運（REAL）的正式評核證據',
  '來源': '受控文件與 TEST 核心權威 readback 的去識別靜態投影；外部 Viewer 不在執行期直連核心',
  '來源更新時間': '2026-08-18 22:20 台北時區（Asia/Taipei）；D8 顧問驗收層 readback 基線',
  '官方語意來源': '勞動部勞動力發展署現行 TTQS 訓練機構版評核表與查核佐證文件資料表之顧問導航摘要；正式評核仍以官方最新文件為準',
  '指標範圍': '1–19；19/19 均至少有一筆去識別 SUPPORTS 來源定位',
  '四類TEST表單': 'NEEDS／REGISTRATION／REACTION／FOLLOWUP30；目前靜態 readback 共 14 筆 Observation，4/4 類別均有 ACCEPTED 來源',
  '17–19 狀態': '已有 TEST／SAMPLE 方法與追溯佐證；正式成果仍待實際營運，不宣稱正式達成',
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

// 依 2026-08-18 讀回的官方訓練機構版評核表／查核佐證表整理為顧問導航摘要。
// 這是語意導覽，不複製官方評分，也不取代正式官方文件。
var TTQS_EXTERNAL_OFFICIAL_FOCUS_ = [
  ['1','確認訓練機構的未來經營方向、營運目標、定位與目標客戶是否明確。',[], '先看方向與目標，再看 SAMPLE 年度目標如何連到訓練。'],
  ['2','確認訓練政策是否由目標市場需求形成，並有年度訓練計畫、行動方案及對外揭露。',[], '本畫面只示範制度與方法；不把 SAMPLE 政策當正式對外承諾。'],
  ['3','確認 PDDRO 訓練規劃是否完整反映訓練定位、發展重點與核心訓練類別。',[], '沿 SAMPLE 因果鏈檢查 Plan 到 Outcome 的上下連結。'],
  ['4','確認訓練品質管理是否有系統化文件，且文件具有核准、公告、更新與保存紀錄的控制。',[], '調閱制度政策與19程序主手冊的受控章節摘要與版本定位。'],
  ['5','確認訓練規劃、年度營運目標與重點課程／行動計畫是否有可追溯連結。',[], 'SAMPLE 只示範連結方法，不預先決定 REAL 課程。'],
  ['6','確認訓練行政分工、主管與相關人員是否具備執行對外訓練所需職能。',[], '調閱治理手冊的 A／B／C 分工、不可替代責任與 Gate。'],
  ['7','確認課程設計前是否有客戶／市場需求確認、職能需求與落差分析，以及方法與紀錄。',[], '從 TEST 需求表單 Observation 下鑽，再接 SAMPLE 落差分析。'],
  ['8','確認訓練方案是否系統化設計：目標、方法、時程、師資、學員、教材、環境與評估彼此一致，並有檢討改善。',[], '看需求→目標→內容／方法→評量→資源的完整設計鏈。'],
  ['9','確認學員、客戶、主管、訓練人員、講師／專家等利益關係人有適當參與設計與審查，且留下紀錄。',[], 'SAMPLE 文件只示範參與與決議如何被追溯。'],
  ['10','確認師資、教材或合作資源具有評估／甄選標準，以及採購、契約或後續管理等適當流程。',[], 'SAMPLE 資源甄選只能證明方法；REAL 資格與採購將重新取證。'],
  ['11','確認課程規劃產出與訓練目標、客戶／學員需求及職能需求相互吻合。',[], '從需求 Observation 與 SAMPLE CourseVersion 交叉檢查。'],
  ['12','確認實際訓練內涵按計畫執行，且五個核心要素都與訓練／課程目標切合。',['12a 學員遴選','12b 教材選擇','12c 師資遴選','12d 教學方法','12e 教學環境與設備'], '展開五個子項，再看 SAMPLE 資源甄選與 TEST 報名來源。'],
  ['13','確認有提供學員／客戶把所學移轉到工作或實務的建議、機制或協助，並能留下成果資料。',[], '由 SAMPLE 班次與 30 日追蹤示範移轉／追蹤路徑。'],
  ['14','確認訓練資料有系統化分類、編碼、建檔、保存、分析、運用與查詢／檢索機制。',[], '由架構文件與 Observation／Evidence locator 示範「找得到、追得回」。'],
  ['15','確認有定期課後檢討、結案／評估報告與綜合分析，並把回饋轉成改善。',[], '調閱 SAMPLE 結案分析，再接反應評估 Observation。'],
  ['16','確認訓練過程持續受控；異常有紀錄、因應與必要矯正，並可定期審查。',[], '直接看已驗證的失敗→重試→對帳→最終接受 trace，不重跑故障。'],
  ['17','確認成果評估不是只有單一滿意度，而能依層級留下反應、學習、行為與成果紀錄。',['17a 反應評估','17b 學習評估','17c 行為評估','17d 成果評估'], '目前只展示 TEST／SAMPLE 方法與追溯；正式 Outcome 必須由 REAL 取代。'],
  ['18','確認目標客戶及學員對訓練功能／效果的評價具有具體紀錄與適當評量。',[], '目前僅 SAMPLE；不得把滿意度直接等同正式績效。'],
  ['19','確認目標市場／顧客是否能提出可驗證的價值創造或市場功能證據。',[], '目前僅 1 筆合成合作單位回饋流程；正式市場價值必須等 REAL。']
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
  ['4','EV-POLPROC-001','TTQS ONE 制度政策與19程序主手冊 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-POLPROC-20260817T230900','','','https://docs.google.com/document/d/1TzJVJrw-K7OoCLgIe18JGdI-QyDa3UGRkU9Khog87SQ/edit','CURRENT 工作版；不是已正式核准制度。'],
  ['5','EV-S001-001','SAMPLE 年度目標與課程方向連結','SUPPORTS','SAMPLE','STRUCTURED_DATA','AnnualGoal','SAMPLE-AG-2026-001','','','','SAMPLE 目標與訓練規劃連結。'],
  ['6','EV-GOV-CTRL-001','TTQS ONE 治理控制手冊 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-GOV-CTRL-20260818T004500','','','https://docs.google.com/document/d/1fvocxiyS-_-fqs_1P835tai1jA_aBlqHDKKoxeYVUTI/edit','治理控制工作版；正式制度仍依必要 A 核准。'],
  ['7','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','合成 SAMPLE 需求/落差文件；非 REAL 市場需求。'],
  ['7','EV-RUN-A1788F62F85532C2','TEST SAMPLE runtime needs response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-A1788F62F85532','OBS-5DF457DAE87CE85418F35E8B','SHEET:1145488986:ROW:5','','真實 Google Forms TEST submission 的去識別索引；ACCEPTED，非正式證據。'],
  ['8','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','需求→目標→評量追溯 SAMPLE 示範。'],
  ['9','EV-S001-013','SAMPLE 利益關係人參與與課程審查','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','4 類虛構利益關係人；REAL 需真實參與證據。'],
  ['10','EV-S001-014','SAMPLE 講師教材場地資源甄選與切合','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','SAMPLE 資源甄選與切合；非 REAL 採購/資格。'],
  ['11','EV-S001-012','SAMPLE 需求與職能落差→課程設計鏈','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','需求與訓練目標結合 SAMPLE 示範。'],
  ['11','EV-RUN-A1788F62F85532C2','TEST SAMPLE runtime needs response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-A1788F62F85532','OBS-5DF457DAE87CE85418F35E8B','SHEET:1145488986:ROW:5','','TEST needs submission；只公開不可逆識別資訊與 locator，不公開回覆內容。'],
  ['12','EV-S001-014','SAMPLE 講師教材場地資源甄選與切合','SUPPORTS','SAMPLE','DOCUMENT_SECTION','DocumentVersion','DV-S001-PREDESIGN-20260817T235900','','','https://docs.google.com/document/d/1x9HR8pWyKQvAOjiresBfNObho7rvakPP_igLuURzkNM/edit','SAMPLE 執行資源；非正式班次。'],
  ['12','EV-RUN-D72493E5294CD5B2','TEST SAMPLE runtime registration response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-D72493E5294CD5','OBS-0BDC55AF857F2A31861AF73F','SHEET:1407831401:ROW:7','','真實 Google Forms TEST 報名 submission 去識別定位；ACCEPTED / SCHEDULER_PROCESSED。'],
  ['13','EV-S001-005','SAMPLE 班次執行與學習成果移轉','SUPPORTS','SAMPLE','STRUCTURED_DATA','ClassRun','SAMPLE-CLASS-001','','','','班次、出勤與追蹤皆為 SAMPLE。'],
  ['13','EV-RUN-99545B2AB6B10D3F','TEST SAMPLE runtime 30-day behavior response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-99545B2AB6B10D','OBS-B6FCD3304656E8618BD552CA','SHEET:332084943:ROW:2','','真實 Google Forms TEST 30日追蹤 submission 去識別定位；ACCEPTED。'],
  ['14','EV-ARCH-001','TTQS ONE 系統架構與平台對接說明 CURRENT','SUPPORTS','CONTROL','DOCUMENT','DocumentVersion','DV-ARCH-20260817T230900','','','https://docs.google.com/document/d/1XP1xagkTb5MSn7IgL9d5ekmI8FYw4XNTsHktZgZiC3M/edit','CURRENT 架構控制文件。'],
  ['15','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','SAMPLE 結案文件；非 REAL 正式實績。'],
  ['15','EV-RUN-574145BB8CD6BF6F','TEST SAMPLE runtime reaction response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-574145BB8CD6BF','OBS-05BA7E0619D4E63D86151795','SHEET:480064116:ROW:3','','真實 Google Forms TEST 反應 submission 去識別定位；ACCEPTED。'],
  ['16','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','SAMPLE 異常/改善閉環；不代表正式治理核准。'],
  ['17','EV-S001-011','SAMPLE 結案分析與改善閉環文件','SUPPORTS','SAMPLE','DOCUMENT','DocumentVersion','DV-S001-CLOSE-20260817T235900','','','https://docs.google.com/document/d/1ZjrRPzobM73TIfPKpnOwvlo8gpaULzWMlmpu7ct1dEk/edit','正式成果仍待 REAL；此列只示範 TEST/SAMPLE 追溯。'],
  ['17','EV-RUN-574145BB8CD6BF6F','TEST SAMPLE runtime reaction response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-574145BB8CD6BF','OBS-05BA7E0619D4E63D86151795','SHEET:480064116:ROW:3','','TEST/SAMPLE 反應評估來源；不可作正式成果。'],
  ['18','EV-RUN-99545B2AB6B10D3F','TEST SAMPLE runtime 30-day behavior response','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-RUN-SUR-99545B2AB6B10D','OBS-B6FCD3304656E8618BD552CA','SHEET:332084943:ROW:2','','TEST/SAMPLE 30日追蹤；正式學員評價待 REAL。'],
  ['19','EV-S001-010','SAMPLE 市場／顧客價值回饋','SUPPORTS','SAMPLE','STRUCTURED_DATA','SurveyResponse','S-SUR-011','','','','1筆虛構合作單位/目標客戶回饋；正式市場價值待 REAL。']
];

// Google 文件連結在顧問裝置上可能需要登入；Portal 因此內嵌最小充分的受控章節定位與去識別摘要。
// Drive 連結只是選配深挖，不是 9/1 調閱成功的單點依賴。
var TTQS_EXTERNAL_SOURCE_BRIEFS_ = {
  'EV-POLPROC-001': {
    locator: '制度政策與19程序主手冊：P14-01～P14-07、PR-01～PR-19、第三部 9/1 T Gate',
    summary: '工作版制度明確要求 T Gate 前只用 TEST／SAMPLE；正式課程必須在 REAL 需求與職能落差分析後才形成；證據保存一次並可索引至多個指標。'
  },
  'EV-GOV-CTRL-001': {
    locator: '治理控制手冊：四 Mission 投影、五角色責任、八 T/R/C/E Gate、九外部寫入驗證',
    summary: 'A 負責正式治理；B 負責辦訓營運；C 負責 TTQS／品質／技術治理。T Gate 前禁止 REAL_WRITE、PROD_ENABLE、REAL_COURSE_LOCK、SAMPLE_AS_REAL。'
  },
  'EV-S001-012': {
    locator: 'SAMPLE-001 前置證據包：一需求來源、二落差分析、三需求→課程設計、八 12a–12e',
    summary: '以合成需求與三組能力落差示範需求→目標→內容／方法→評量的可追溯設計；明示不得當成協會真實市場需求。'
  },
  'EV-S001-013': {
    locator: 'SAMPLE-001 前置證據包：四、SAMPLE 利益關係人參與紀錄',
    summary: '以學員、講師、合作單位及 B/C 等合成角色示範課程設計／審查意見、決議與系統編號追溯；不冒充真人會議或核准。'
  },
  'EV-S001-014': {
    locator: 'SAMPLE-001 前置證據包：五講師、六教材、七場地、八 12a–12e 切合性',
    summary: '示範講師、教材、場地與教學方法都有選擇／審查標準並回扣課程目標；REAL 時必須重新做真實資格、教材與場地查核。'
  },
  'EV-ARCH-001': {
    locator: '系統架構與平台對接說明：五外部收件、六已驗證 runtime、八 Evaluator Portal、九 Evidence/Locator',
    summary: 'TEST 四類表單經 Observation→業務主表→Ledger／AttemptHistory→reconciliation→FINAL_ACCEPTED；S3 已驗證單一 Scheduler、exactly-once、append-only 與 duplicate=0。'
  },
  'EV-S001-011': {
    locator: 'SAMPLE-001 結案分析：三模擬結果、五主要發現、六改善行動、七故障恢復、八19指標狀態',
    summary: '合成結案示範反應／學習／30日追蹤、改善行動與 S3 runtime trace；17–19 僅示範方法，正式 Outcome 必須由 REAL 證據取代。'
  }
};

// 2026-08-18 live TEST 讀回。只保留去識別生命週期摘要與代表 locator。
var TTQS_EXTERNAL_FORM_LIFECYCLE_ = [
  ['NEEDS','需求調查',4,'OBS-5DF457DAE87CE85418F35E8B','SHEET:1145488986:ROW:5','S-RUN-SUR-A1788F62F85532','ACCEPTED','LINKED_EXISTING','4 筆 TEST Observation 均已接受；代表來源可由 Observation 回到原始收件列。'],
  ['REGISTRATION','課程報名',6,'OBS-0BDC55AF857F2A31861AF73F','SHEET:1407831401:ROW:7','S-RUN-SUR-D72493E5294CD5','ACCEPTED','SCHEDULER_PROCESSED','6 筆 TEST Observation 均已接受；代表列由單一 Scheduler 發現與處理。'],
  ['REACTION','課後滿意度',2,'OBS-05BA7E0619D4E63D86151795','SHEET:480064116:ROW:3','S-RUN-SUR-574145BB8CD6BF','ACCEPTED','LINKED_EXISTING','2 筆 TEST Observation 均已接受；只展示去識別索引，不展示回答內容。'],
  ['FOLLOWUP30','30日追蹤',2,'OBS-B6FCD3304656E8618BD552CA','SHEET:332084943:ROW:2','S-RUN-SUR-99545B2AB6B10D','ACCEPTED','LINKED_EXISTING','2 筆 TEST Observation 均已接受；用於示範後續追蹤與行為層來源。']
];

// 已完成且不為 9/1 重跑的 S3 真實 TEST 故障／恢復證據。
var TTQS_EXTERNAL_S3_TRACE_ = {
  topology: 'S3_SINGLE_SCHEDULER：1 master / 0 form-submit',
  jobId: 'JOB-63831AEA86216EA8B1',
  observationId: 'OBS-A319BCBB94CA4A5956E68B80',
  sourceLocator: 'SHEET:1407831401:ROW:6',
  failure: {
    attemptEventId: 'ATT-FD9077D2CE6AB18E1A1648FE',
    attemptNo: '1',
    trigger: 'SCHEDULER_OBSERVATION',
    status: 'FAILED',
    errorClass: 'Error',
    errorMessage: 'TTQS_INJECTED_PARTIAL_FAILURE_AFTER_PARTY_ALIAS',
    retryAt: '2026-08-17T10:13:39+0800'
  },
  recovery: {
    attemptEventId: 'ATT-3EEECFBB3D2A9DED5897DBEA',
    attemptNo: '2',
    trigger: 'TIME_RETRY',
    status: 'SUCCESS',
    recovered: 'true',
    recoveryEvidenceId: 'EV-RUN-REC-CF43A0C33DC3EACD'
  },
  reconciliationStatus: 'MATCHED_EXACTLY_ONCE',
  finalAcceptanceStatus: 'FINAL_ACCEPTED',
  resultObjectId: 'S-RUN-SUR-C2CDCEDD26C2E0',
  attemptHistory: 'append-only；FAILED 與 SUCCESS 是不同 attempt event，hash chain 保留失敗歷史',
  duplicateCounts: {job:0, party:0, survey:0, evidence:0},
  rawProviderWrite: '0'
};

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

function ttqsExternalOfficialModel_() {
  if (TTQS_EXTERNAL_OFFICIAL_FOCUS_.length !== 19) throw new Error('SNAPSHOT_OFFICIAL_FOCUS_COUNT_INVALID');
  var seen = {};
  return TTQS_EXTERNAL_OFFICIAL_FOCUS_.map(function(row) {
    var no = String(row[0]);
    if (!/^(?:[1-9]|1[0-9])$/.test(no) || seen[no]) throw new Error('SNAPSHOT_OFFICIAL_FOCUS_ID_INVALID');
    seen[no] = true;
    var subitems = Array.isArray(row[2]) ? row[2].slice() : [];
    if (no === '12' && subitems.length !== 5) throw new Error('SNAPSHOT_INDICATOR_12_SUBITEMS_INVALID');
    if (no === '17' && subitems.length !== 4) throw new Error('SNAPSHOT_INDICATOR_17_SUBITEMS_INVALID');
    return {no:no, focus:String(row[1] || ''), subitems:subitems, demoPath:String(row[3] || '')};
  });
}

function ttqsExternalFormLifecycleModel_() {
  if (TTQS_EXTERNAL_FORM_LIFECYCLE_.length !== 4) throw new Error('SNAPSHOT_FORM_LIFECYCLE_COUNT_INVALID');
  var allowed = {NEEDS:true,REGISTRATION:true,REACTION:true,FOLLOWUP30:true};
  var seen = {};
  var total = 0;
  var items = TTQS_EXTERNAL_FORM_LIFECYCLE_.map(function(row) {
    var kind = String(row[0]);
    if (!allowed[kind] || seen[kind]) throw new Error('SNAPSHOT_FORM_LIFECYCLE_KIND_INVALID');
    seen[kind] = true;
    var count = Number(row[2]);
    if (!Number.isFinite(count) || count < 1) throw new Error('SNAPSHOT_FORM_LIFECYCLE_COUNT_INVALID');
    if (row[6] !== 'ACCEPTED') throw new Error('SNAPSHOT_FORM_LIFECYCLE_STATUS_INVALID');
    total += count;
    return {kind:kind,label:row[1],count:count,observationId:row[3],sourceLocator:row[4],processedObjectId:row[5],status:row[6],disposition:row[7],note:row[8]};
  });
  if (total !== 14) throw new Error('SNAPSHOT_FORM_OBSERVATION_TOTAL_INVALID');
  return {items:items,total:total};
}

function ttqsExternalS3TraceModel_() {
  var trace = TTQS_EXTERNAL_S3_TRACE_;
  if (!trace || trace.failure.status !== 'FAILED' || trace.recovery.status !== 'SUCCESS') throw new Error('SNAPSHOT_S3_TRACE_ATTEMPTS_INVALID');
  if (trace.failure.attemptNo !== '1' || trace.recovery.attemptNo !== '2') throw new Error('SNAPSHOT_S3_TRACE_SEQUENCE_INVALID');
  if (trace.reconciliationStatus !== 'MATCHED_EXACTLY_ONCE' || trace.finalAcceptanceStatus !== 'FINAL_ACCEPTED') throw new Error('SNAPSHOT_S3_TRACE_ACCEPTANCE_INVALID');
  var dup = trace.duplicateCounts || {};
  if (Number(dup.job) !== 0 || Number(dup.party) !== 0 || Number(dup.survey) !== 0 || Number(dup.evidence) !== 0) throw new Error('SNAPSHOT_S3_TRACE_DUPLICATE_INVALID');
  if (trace.rawProviderWrite !== '0') throw new Error('SNAPSHOT_S3_TRACE_PROVIDER_WRITE_INVALID');
  return trace;
}

function ttqsExternalSnapshotModel_() {
  if (TTQS_EXTERNAL_INDICATORS_.length !== 19) throw new Error('SNAPSHOT_INDICATOR_COUNT_INVALID');
  if (TTQS_EXTERNAL_CAUSAL_.length !== 6) throw new Error('SNAPSHOT_CAUSAL_SEQUENCE_INVALID');
  var official = ttqsExternalOfficialModel_();
  var officialByNo = {};
  official.forEach(function(item) { officialByNo[item.no] = item; });
  var seen = {};
  var indicators = TTQS_EXTERNAL_INDICATORS_.map(function(row) {
    var no = row[0];
    if (!/^(?:[1-9]|1[0-9])$/.test(no) || seen[no]) throw new Error('SNAPSHOT_INDICATOR_ID_INVALID');
    seen[no] = true;
    if (!officialByNo[no]) throw new Error('SNAPSHOT_OFFICIAL_FOCUS_MISSING');
    return {no:no, stage:row[1], title:row[2], evidenceCount:row[3], status:row[4], refreshedAt:row[5], officialFocus:officialByNo[no], evidenceDetails:[]};
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
    var sourceUrl = ttqsExternalSafeSourceUrl_(row[10]);
    var brief = TTQS_EXTERNAL_SOURCE_BRIEFS_[row[1]] || null;
    if (sourceUrl && (!brief || !brief.locator || !brief.summary)) throw new Error('SNAPSHOT_DOCUMENT_SOURCE_BRIEF_REQUIRED');
    var item = {indicatorNo:no,evidenceId:row[1],title:row[2],relation:row[3],dataClass:row[4],evidenceType:row[5],sourceObjectType:row[6],sourceObjectId:row[7],observationId:row[8],sourceLocator:row[9],sourceUrl:sourceUrl,publicNote:row[11],controlledLocator:brief ? brief.locator : '',embeddedSummary:brief ? brief.summary : ''};
    if (!item.evidenceId || !item.title || !item.sourceObjectType || !item.sourceObjectId) throw new Error('SNAPSHOT_EVIDENCE_REQUIRED_FIELD_MISSING');
    coverage[no] = (coverage[no] || 0) + 1;
    byIndicator[no].push(item);
    return item;
  });
  for (var i = 1; i <= 19; i++) if (!coverage[String(i)]) throw new Error('SNAPSHOT_EVIDENCE_COVERAGE_INVALID');
  indicators.forEach(function(item) { item.evidenceDetails = byIndicator[item.no]; });
  var forms = ttqsExternalFormLifecycleModel_();
  return {title:TTQS_EXTERNAL_SNAPSHOT_TITLE_, summary:TTQS_EXTERNAL_SUMMARY_, official:official, indicators:indicators, causalFlow:causalFlow, evidence:evidence, forms:forms.items, formObservationTotal:forms.total, s3Trace:ttqsExternalS3TraceModel_()};
}

function ttqsExternalSubitemsHtml_(items) {
  if (!items || !items.length) return '';
  return '<div class="subitems">' + items.map(function(item) { return '<span>' + ttqsExternalEscape_(item) + '</span>'; }).join('') + '</div>';
}

function ttqsExternalOfficialHtml_(items) {
  return '<section id="official-semantics"><div class="section-title"><h2>官方 19 指標評核語意導航</h2><p>依現行訓練機構版評核表／查核佐證表摘要；只協助顧問知道「這個指標要看什麼」，不在系統內自動評分。</p></div><div class="official-grid">' + items.map(function(item) {
    return '<a class="official-card" href="#indicator-' + item.no + '"><div class="top"><span class="no">' + item.no + '</span><span class="stage">抽查焦點</span></div><p>' + ttqsExternalEscape_(item.focus) + '</p>' + ttqsExternalSubitemsHtml_(item.subitems) + '<small>最短路徑：' + ttqsExternalEscape_(item.demoPath) + '</small></a>';
  }).join('') + '</div></section>';
}

function ttqsExternalCausalHtml_(steps) {
  return '<section id="sample-causal"><div class="section-title"><h2>SAMPLE 評核因果鏈</h2><p>需求→分析→課程設計→執行→評量→追蹤→改善。所有內容皆為 TEST／SAMPLE，不得轉作 REAL 證據。</p></div><div class="flow">' + steps.map(function(item) {
    var anchor = item.indicators.split('、')[0];
    return '<a class="flow-step" href="#indicator-' + ttqsExternalEscape_(anchor) + '"><span>' + ttqsExternalEscape_(item.step) + '</span><strong>' + ttqsExternalEscape_(item.name) + '</strong><small>指標 ' + ttqsExternalEscape_(item.indicators) + ' · ' + ttqsExternalEscape_(item.status) + '</small><p>' + ttqsExternalEscape_(item.note) + '</p></a>';
  }).join('') + '</div></section>';
}

function ttqsExternalFormsHtml_(items, total) {
  return '<section id="form-lifecycle"><div class="section-title"><h2>四類 TEST Google Forms 生命週期</h2><p>目前只展示去識別 readback。共 ' + ttqsExternalEscape_(total) + ' 筆 Observation；4/4 類別都有 ACCEPTED 來源，不公開原始回答。</p></div><div class="form-grid">' + items.map(function(item) {
    return '<article class="form-card"><div class="top"><strong>' + ttqsExternalEscape_(item.label) + '</strong><span class="stage">' + ttqsExternalEscape_(item.kind) + '</span></div><div class="metric">Observation <b>' + ttqsExternalEscape_(item.count) + '</b></div><div class="tags"><b>' + ttqsExternalEscape_(item.status) + '</b><b>' + ttqsExternalEscape_(item.disposition) + '</b></div><div class="locator"><strong>代表 Observation</strong><code>' + ttqsExternalEscape_(item.observationId) + '</code><strong>原始收件定位</strong><code>' + ttqsExternalEscape_(item.sourceLocator) + '</code><strong>處理物件</strong><code>' + ttqsExternalEscape_(item.processedObjectId) + '</code></div><p class="note">' + ttqsExternalEscape_(item.note) + '</p></article>';
  }).join('') + '</div></section>';
}

function ttqsExternalS3TraceHtml_(trace) {
  return '<section id="runtime-trace"><div class="section-title"><h2>故障 → 重試 → 對帳 → FINAL_ACCEPTED</h2><p>這是已經通過的 S3 真實 TEST runtime 證據；9/1 只讀展示，不為表演而重跑故障。</p></div><article class="trace-card"><div class="trace-head"><b>' + ttqsExternalEscape_(trace.topology) + '</b><code>' + ttqsExternalEscape_(trace.jobId) + '</code></div><div class="trace-grid"><div class="trace-step bad"><span>1</span><strong>第一次處理失敗</strong><code>' + ttqsExternalEscape_(trace.failure.attemptEventId) + '</code><p>' + ttqsExternalEscape_(trace.failure.trigger + ' · ' + trace.failure.status) + '</p><p class="note">' + ttqsExternalEscape_(trace.failure.errorMessage) + '</p></div><div class="trace-step"><span>2</span><strong>TIME_RETRY 恢復</strong><code>' + ttqsExternalEscape_(trace.recovery.attemptEventId) + '</code><p>' + ttqsExternalEscape_(trace.recovery.status + ' · recovered=' + trace.recovery.recovered) + '</p><p class="note">Recovery Evidence：' + ttqsExternalEscape_(trace.recovery.recoveryEvidenceId) + '</p></div><div class="trace-step"><span>3</span><strong>唯一對帳</strong><p>' + ttqsExternalEscape_(trace.reconciliationStatus) + '</p><p class="note">job / party / survey / evidence duplicate = 0 / 0 / 0 / 0</p></div><div class="trace-step good"><span>4</span><strong>最終接受</strong><p>' + ttqsExternalEscape_(trace.finalAcceptanceStatus) + '</p><code>' + ttqsExternalEscape_(trace.resultObjectId) + '</code><p class="note">provider raw write=' + ttqsExternalEscape_(trace.rawProviderWrite) + '；AttemptHistory=' + ttqsExternalEscape_(trace.attemptHistory) + '</p></div></div><div class="locator"><strong>原始來源</strong><span>Observation：' + ttqsExternalEscape_(trace.observationId) + '</span><code>' + ttqsExternalEscape_(trace.sourceLocator) + '</code></div></article></section>';
}

function ttqsExternalEvidenceHtml_(items) {
  if (!items || !items.length) return '<p class="empty">此指標目前沒有公開定位資料。</p>';
  return '<div class="evidence-list">' + items.map(function(item) {
    var source = '<div class="locator"><strong>來源物件</strong><code>' + ttqsExternalEscape_(item.sourceObjectType + ':' + item.sourceObjectId) + '</code></div>';
    var observation = item.observationId || item.sourceLocator ? '<div class="locator"><strong>原始收件定位</strong>' + (item.observationId ? '<span>Observation：' + ttqsExternalEscape_(item.observationId) + '</span>' : '') + (item.sourceLocator ? '<code>' + ttqsExternalEscape_(item.sourceLocator) + '</code>' : '') + '</div>' : '';
    var controlled = item.controlledLocator ? '<div class="controlled"><strong>受控章節／物件定位</strong><p>' + ttqsExternalEscape_(item.controlledLocator) + '</p><strong>去識別摘要</strong><p>' + ttqsExternalEscape_(item.embeddedSummary) + '</p></div>' : '';
    var link = item.sourceUrl ? '<a class="source-link" target="_blank" rel="noopener noreferrer" href="' + ttqsExternalEscape_(item.sourceUrl) + '">選配：開啟受控 Drive 來源（可能需登入）</a>' : '';
    return '<details class="evidence"><summary><span>' + ttqsExternalEscape_(item.evidenceId) + '</span>' + ttqsExternalEscape_(item.title) + '</summary><div class="tags"><b>' + item.relation + '</b><b>' + item.dataClass + '</b><b>' + ttqsExternalEscape_(item.evidenceType) + '</b></div>' + source + observation + controlled + (item.publicNote ? '<p class="note">' + ttqsExternalEscape_(item.publicNote) + '</p>' : '') + link + '</details>';
  }).join('') + '</div>';
}

function ttqsExternalRender_(model) {
  var cards = model.indicators.map(function(item) {
    var klass = Number(item.no) >= 17 ? 'outcome' : 'evidence-card';
    return '<article id="indicator-' + item.no + '" class="card ' + klass + '"><div class="top"><span class="no">' + item.no + '</span><span class="stage">' + ttqsExternalEscape_(item.stage) + '</span></div><h3>' + ttqsExternalEscape_(item.title) + '</h3><div class="focus"><strong>官方查核焦點摘要</strong><p>' + ttqsExternalEscape_(item.officialFocus.focus) + '</p>' + ttqsExternalSubitemsHtml_(item.officialFocus.subitems) + '<small>顧問最短路徑：' + ttqsExternalEscape_(item.officialFocus.demoPath) + '</small></div><p class="status">' + ttqsExternalEscape_(item.status) + '</p><div class="meta"><span>核心索引佐證筆數：' + ttqsExternalEscape_(item.evidenceCount) + '</span><span>快照更新：' + ttqsExternalEscape_(item.refreshedAt) + '</span></div><details class="drill"><summary>查看佐證與來源（' + item.evidenceDetails.length + '）</summary>' + ttqsExternalEvidenceHtml_(item.evidenceDetails) + '</details></article>';
  }).join('');
  var runtimeLocators = model.evidence.filter(function(item) { return item.observationId && item.sourceLocator; }).length;
  return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TTQS ONE 外部唯讀</title><style>' +
    ':root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",sans-serif;color:#17202a;background:#f4f6f8}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f6f8}main{max-width:1220px;margin:auto;padding:22px}header,.card,.stat,.flow-step,.official-card,.form-card,.trace-card{background:#fff;border:1px solid #dce3e8;border-radius:16px}header{padding:24px;margin-bottom:16px}.eyebrow{font-size:13px;font-weight:800;color:#586674}h1{font-size:30px;margin:7px 0 8px}h2{font-size:22px}h3{font-size:16px}.notice{background:#fff7dd;border:1px solid #ead18a;border-radius:12px;padding:13px 15px;line-height:1.6}.security{background:#edf7ef;border:1px solid #c8dfcd;border-radius:12px;padding:13px 15px;line-height:1.6;margin-top:10px}.jump{display:flex;gap:8px;flex-wrap:wrap;margin-top:13px}.jump a{padding:7px 10px;border:1px solid #c9d3dc;border-radius:999px;text-decoration:none;color:#17202a;font-size:12px;font-weight:800;background:#fff}.stats,.flow,.grid,.official-grid,.form-grid,.trace-grid{display:grid;gap:11px}.stats{grid-template-columns:repeat(4,1fr);margin:16px 0}.stat{padding:14px}.stat strong{display:block;font-size:24px}.flow{grid-template-columns:repeat(3,1fr)}.flow-step,.official-card{padding:15px;text-decoration:none;color:#17202a;display:grid;gap:6px}.official-grid{grid-template-columns:repeat(3,1fr)}.official-card small{color:#66737e;line-height:1.5}.grid{grid-template-columns:repeat(2,1fr)}.form-grid{grid-template-columns:repeat(2,1fr)}.form-card{padding:15px}.metric{margin:9px 0}.metric b{font-size:22px}.trace-card{padding:16px}.trace-head{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}.trace-grid{grid-template-columns:repeat(4,1fr);margin-top:12px}.trace-step{border:1px solid #dce3e8;border-radius:12px;padding:12px;background:#fafbfc;display:grid;gap:5px}.trace-step>span{font-weight:900}.trace-step.bad{border-color:#e2b8b8}.trace-step.good{border-color:#a9cfb2}.card{padding:16px;border-left:5px solid #60886b}.card.outcome{border-left-color:#a98945}.top{display:flex;justify-content:space-between}.no{font-weight:800}.stage,.tags b,.subitems span{font-size:12px;background:#eef2f5;padding:4px 8px;border-radius:999px}.subitems{display:flex;gap:5px;flex-wrap:wrap;margin:8px 0}.focus{border:1px solid #dce3e8;background:#f8fafb;border-radius:10px;padding:10px;line-height:1.55}.focus p{margin:6px 0}.focus small{color:#66737e}.meta,.note,.status,.flow-step small,.foot{color:#66737e;font-size:12px;line-height:1.55}.drill{border-top:1px solid #e1e7eb;margin-top:12px;padding-top:10px}.drill>summary,.evidence>summary{cursor:pointer;font-weight:800}.evidence-list{display:grid;gap:9px;margin-top:10px}.evidence{border:1px solid #e1e7eb;border-radius:10px;padding:10px;background:#fafbfc}.tags{display:flex;gap:5px;flex-wrap:wrap;margin:9px 0}.locator,.controlled{display:grid;gap:4px;margin:7px 0;padding:8px;border-radius:8px;background:#f1f4f6;font-size:12px}.controlled{background:#fffbe9;border:1px solid #eadca3}.locator code,.trace-step code,.trace-head code{overflow-wrap:anywhere}.controlled p{margin:3px 0;line-height:1.55}.source-link{display:inline-block;margin-top:4px;text-decoration:none;color:#17202a;border:1px solid #c9d3dc;border-radius:9px;padding:7px 9px;background:#fff;font-size:12px;font-weight:800}.section-title{margin-top:25px}.section-title p{line-height:1.6;color:#586674}@media(max-width:920px){.official-grid,.trace-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:720px){main{padding:13px}.grid,.stats,.flow,.official-grid,.form-grid,.trace-grid{grid-template-columns:1fr}}' +
    '</style></head><body><main><header><div class="eyebrow">TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</div><h1>' + ttqsExternalEscape_(model.title) + '</h1><div>用途：' + ttqsExternalEscape_(model.summary['用途']) + '</div><div class="notice">本畫面不計算 TTQS 官方分數，不宣稱評核通過或準備完成。17–19 的正式成果仍須以實際營運證據（REAL）為準。</div><div class="security">唯讀安全邊界：此 Web App 僅呈現部署版本內嵌的去識別靜態快照，不在執行期呼叫 Google Sheets／Drive API、不直接連線 TTQS ONE 核心資料庫、不讀取問卷原始回答，也不提供新增、修改、刪除、核准、正式啟動或背景工作控制。</div><nav class="jump"><a href="#official-semantics">官方19指標</a><a href="#sample-causal">SAMPLE因果鏈</a><a href="#form-lifecycle">四表生命週期</a><a href="#runtime-trace">故障／重試</a><a href="#evidence-drilldown">19指標佐證</a></nav></header>' +
    '<section class="stats"><div class="stat">官方指標範圍<strong>19 / 19</strong></div><div class="stat">公開 SUPPORTS 定位<strong>' + model.evidence.length + '</strong></div><div class="stat">四類 TEST Forms<strong>4 / 4</strong></div><div class="stat">TEST Observation<strong>' + ttqsExternalEscape_(model.formObservationTotal) + '</strong></div></section>' +
    ttqsExternalOfficialHtml_(model.official) + ttqsExternalCausalHtml_(model.causalFlow) + ttqsExternalFormsHtml_(model.forms, model.formObservationTotal) + ttqsExternalS3TraceHtml_(model.s3Trace) + '<section id="evidence-drilldown"><div class="section-title"><h2>19 指標佐證與來源下鑽</h2><p>每張卡片先顯示官方查核焦點，再展開去識別 SUPPORTS 佐證、來源物件、Observation locator 與受控章節摘要。Google Drive 連結只是選配，不是顧問調閱成功的必要條件。</p></div><div class="grid">' + cards + '</div></section><p class="foot">資料更新：' + ttqsExternalEscape_(model.summary['來源更新時間']) + '。資料分類：' + ttqsExternalEscape_(model.summary['資料分類']) + '。官方語意：' + ttqsExternalEscape_(model.summary['官方語意來源']) + '。代表 runtime locator：' + runtimeLocators + '。來源快照：' + ttqsExternalEscape_(TTQS_EXTERNAL_SOURCE_SNAPSHOT_ID_) + '。本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</p></main></body></html>';
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
