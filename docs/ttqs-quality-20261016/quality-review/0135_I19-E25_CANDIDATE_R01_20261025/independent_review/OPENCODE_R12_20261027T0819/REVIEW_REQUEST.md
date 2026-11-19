# Independent semantic review request — TTQS ONE 0135 / I19-E25

Review ONLY the supplied source packet, unique blueprint, and extracted text from the exact DOCX candidate. The DOCX itself is not to be edited. Do not invoke tools, browse, search, run commands, or infer facts that are absent from these inputs. Text locator P### corresponds to paragraph order in the DOCX body; table cells are included in document order. Cite exact section/table and P### locators when reporting a finding.

Identity binding:
- project_id: TTQS_ONE
- doc_id: 0135
- requirement_id: I19-E25
- candidate_sha256: cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da
- source_packet_sha256: fe4e433924b21b9891ca61ca52907e56a9dbd9ac62a4fd6fc43a9e4faef19696
- unique_blueprint_sha256: cb936466e92bb2d5976a2be1a013d85ccdd3a8bbe434dd8b51ac3d77e12d25c1
- requested reviewer model: OpenCode v2 opencode/glm-5.3-flash-free

Evaluate: (1) the correct official purpose and evidence scope; (2) the document genre and whether it is a usable, mature analysis report rather than generic instructions; (3) complete method, definitions, usable tables, calculations, interpretation, and decision/rejection/hold conditions; (4) all synthetic sample values clearly separated from REAL evidence, with no fabricated association execution, approvals, third-party facts, or credentials; (5) arithmetic and conclusions consistent throughout; (6) cross-document facts and shared case values only where supplied, otherwise mark UNKNOWN; (7) distinguish this requirement from adjacent I19 requirements using the supplied blueprint; (8) whether a small volunteer association administrator and an evaluator can use it; (9) whether it remains identifiable if the title is masked. Do not require unavailable real records to be fabricated: report them as a truthful hold/replace condition.

Return exactly one JSON object, no markdown fence:
{"doc_id":"0135","requirement_id":"I19-E25","candidate_sha256":"cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da","verdict":"PASS|PARTIAL|FAIL","review_scope":"...","findings":[{"severity":"critical|high|medium|low","locator":"section/table and P###","evidence":"...","required_correction":"..."}],"sample_real_boundary":"...","arithmetic_check":"...","cross_document_check":"...","limitations":[...]}
PASS only if no material defect remains within the supplied scope. If any required input is missing or a material assertion cannot be grounded, return PARTIAL or FAIL and identify it. This review does not grant formal acceptance.

## Official/source packet
# SOURCE PACKET｜0135 I19-E25 R01

Status: SOURCE_READY for a document-specific writer; no DOCX has been built in this source-preparation stage.

## Official requirement
The training-institution official evidence table, indicator 19, is “訓練系統的市場功能—目標市場及顧客的價值創造”. Pages 7–8 define levels from improvement without concrete records through significant concrete improvement performance. Page 8 lists quantitative improvement, training follow-up, employment/licensing, market/business outcomes, membership/dues trends, and other examples. The applicable official deliverable row is I19-E25, mapped in the current 129→142 crosswalk to document 0135. The printed official checkbox serial is UNKNOWN in the supplied source bundle.

## Distinct project mapping
The TTQS ONE 157-item blueprint maps project item 140 to “市場顧客價值量化：期間/分母/改善幅度”. Item 141 is individual training performance; item 142 is market competition/revenue/process/cost/complaints. Keep these distinct. This project index is not the official checkbox serial.

## Distinct neighboring documents
0133/I19-E22: annual training sessions and participant person-times. 0134/I19-E23: member counts and dues income. 0135/I19-E25: target-market reach AND customer value. Do not merge or reuse neighboring document facts.

## Writer-ready SAMPLE scenario
A fictional demonstration concerns nonprofit volunteer-organization administrators learning monthly service-record practices. The synthetic eligible frame is 80 organizations/year; served counts 20, 24, and 28 in 2023–2025. For 2025, 15 of 28 served organizations provide matched pre-course and 90-day follow-up observations. Their synthetic median monthly-record completion time is 120→90 minutes; on-time completion is 8/15→12/15. See SAMPLE_PAIRED_MEASUREMENT_DATA.csv. These data exist only to demonstrate complete calculations and cannot be represented as association results or a verified market estimate.

## Required next stage
Build a full evaluator-usable market/value analysis report from # 0135 Unique Blueprint R01｜I19-E25

## Identity and evidence boundary
- Deliverable: DOCX 0135, 「目標市場與顧客價值具體提升成效分析報告」.
- Official requirement: I19-E25, indicator 19「訓練系統的市場功能—目標市場及顧客的價值創造」; official source PDF pages 7–8. The printed checkbox serial is UNKNOWN; do not substitute document ID 0135 or 157 index 140 for that serial.
- Project evidence mapping: 03_157_CHECKBOX_BLUEPRINTS item 140「市場顧客價值量化：期間/分母/改善幅度」. Items 141 (individual training performance) and 142 (market competition/revenue/process/cost/complaints) are distinct; they are excluded as primary evidence here.
- Genre: quantified market-and-customer-value outcome analysis report. It is not a membership/dues trend report, course-count report, satisfaction-only report, or scoring sheet.
- All supplied metrics and case rows are SAMPLE/SYNTHETIC. No actual association market reach, customers, outcomes, approvals, or third-party facts are asserted.

## Exclusive purpose
Demonstrate how a training institution identifies a target market and measures whether both target-market reach and customer value improved over defined periods. The report must separate reach from value, state denominators and calculation rules, show period-to-period changes, explain decisions, and disclose measurement limits.

## Required report structure
1. Cover, document identity, version, reporting period, SAMPLE/SYNTHETIC notice.
2. Executive finding: two outcome lanes (target-market reach; customer value), periods, denominators, changes, and limitations; no self-awarded TTQS score.
3. Requirement-to-measurement map: official wording, operational definition, evidence location, owner/retention, and missing REAL source.
4. Target-market definition: nonprofit volunteer-organization administrators needing reliable monthly service records; eligibility, exclusions, de-duplication, source frame, and stability checks.
5. Multi-year market reach table for 2023–2025: eligible frame 80 each year; served organizations 20/24/28; rates 25%/30%/35%; changes +5.0 percentage points each year; relative changes +20.0% and +16.7%. Label this frame synthetic and not an external market-size estimate.
6. Customer-value measurement design: matched 2025 organizations, pre-course baseline and 90-day follow-up; response numerator/denominator; administration time and on-time completion measures; collection dates, item wording, missing-data rules, and bias limits.
7. Complete paired SAMPLE table: 15 synthetic case rows from SAMPLE_PAIRED_MEASUREMENT_DATA.csv. Median monthly-record time falls 120→90 minutes (25% reduction). On-time completion rises 8/15 (53.3%)→12/15 (80.0%), +26.7 percentage points. Matched response rate is 15/28 (53.6%) of served organizations. Show formulas and rounding.
8. Analysis: interpret reach and value independently; avoid causal claims because no control group or independent source is supplied. Identify nonresponse, frame stability, attribution, and small-sample limitations.
9. Management decision and action register: what to continue/change, accountable role, due date, evidence to review, and stop/hold trigger. These are proposed SAMPLE decisions only, not association approvals.
10. Cross-document evidence links: 0133/I19-E22 supports training sessions/person-times; 0134/I19-E23 supports membership/dues trends; neither supplies 0135 target-market/customer-value outcomes. Use separate case_id and do not reuse their counts or imply a shared real case.
11. REAL replacement register: list each synthetic field, acceptable primary source, owner, source locator, privacy minimization, reconciliation procedure, and release gate.
12. Evaluator-use checklist and explicit HOLD/REJECT conditions.

## Core formulas
- Annual reach rate (%) = unique served eligible organizations ÷ eligible target-market frame × 100.
- Change (percentage points) = current reach rate − prior reach rate.
- Relative change (%) = (current rate − prior rate) ÷ prior rate × 100.
- Time reduction (%) = (baseline paired median − 90-day paired median) ÷ baseline paired median × 100.
- On-time rate (%) = on-time organizations ÷ matched organizations × 100.
- Response rate (%) = matched follow-up organizations ÷ organizations served in the period × 100.

## HOLD / REJECT conditions
HOLD if target frame criteria or denominators vary without reconciliation; if numerator counts duplicates; if pre/post measurement windows differ; if follow-up or nonresponse denominator is missing; if evidence links cannot be located; if private participant details are exposed; or if a result relies only on satisfaction without market/value measures. REJECT any unlabeled synthetic values presented as REAL, unsupported causal claims, invented customer testimony/approval, undefined market size, or use of 0133/0134 facts as this report’s results. Do not claim level 3 or 4 from the sample.
_0135_I19-E25_R01.md, add an explicit replacement register and page-level sources, run arithmetic and cross-document checks, render with Word, inspect every page, then obtain an independent semantic review bound to the final DOCX SHA. Formal acceptance remains NOT_GRANTED.


## Unique Blueprint
# 0135 Unique Blueprint R01｜I19-E25

## Identity and evidence boundary
- Deliverable: DOCX 0135, 「目標市場與顧客價值具體提升成效分析報告」.
- Official requirement: I19-E25, indicator 19「訓練系統的市場功能—目標市場及顧客的價值創造」; official source PDF pages 7–8. The printed checkbox serial is UNKNOWN; do not substitute document ID 0135 or 157 index 140 for that serial.
- Project evidence mapping: 03_157_CHECKBOX_BLUEPRINTS item 140「市場顧客價值量化：期間/分母/改善幅度」. Items 141 (individual training performance) and 142 (market competition/revenue/process/cost/complaints) are distinct; they are excluded as primary evidence here.
- Genre: quantified market-and-customer-value outcome analysis report. It is not a membership/dues trend report, course-count report, satisfaction-only report, or scoring sheet.
- All supplied metrics and case rows are SAMPLE/SYNTHETIC. No actual association market reach, customers, outcomes, approvals, or third-party facts are asserted.

## Exclusive purpose
Demonstrate how a training institution identifies a target market and measures whether both target-market reach and customer value improved over defined periods. The report must separate reach from value, state denominators and calculation rules, show period-to-period changes, explain decisions, and disclose measurement limits.

## Required report structure
1. Cover, document identity, version, reporting period, SAMPLE/SYNTHETIC notice.
2. Executive finding: two outcome lanes (target-market reach; customer value), periods, denominators, changes, and limitations; no self-awarded TTQS score.
3. Requirement-to-measurement map: official wording, operational definition, evidence location, owner/retention, and missing REAL source.
4. Target-market definition: nonprofit volunteer-organization administrators needing reliable monthly service records; eligibility, exclusions, de-duplication, source frame, and stability checks.
5. Multi-year market reach table for 2023–2025: eligible frame 80 each year; served organizations 20/24/28; rates 25%/30%/35%; changes +5.0 percentage points each year; relative changes +20.0% and +16.7%. Label this frame synthetic and not an external market-size estimate.
6. Customer-value measurement design: matched 2025 organizations, pre-course baseline and 90-day follow-up; response numerator/denominator; administration time and on-time completion measures; collection dates, item wording, missing-data rules, and bias limits.
7. Complete paired SAMPLE table: 15 synthetic case rows from SAMPLE_PAIRED_MEASUREMENT_DATA.csv. Median monthly-record time falls 120→90 minutes (25% reduction). On-time completion rises 8/15 (53.3%)→12/15 (80.0%), +26.7 percentage points. Matched response rate is 15/28 (53.6%) of served organizations. Show formulas and rounding.
8. Analysis: interpret reach and value independently; avoid causal claims because no control group or independent source is supplied. Identify nonresponse, frame stability, attribution, and small-sample limitations.
9. Management decision and action register: what to continue/change, accountable role, due date, evidence to review, and stop/hold trigger. These are proposed SAMPLE decisions only, not association approvals.
10. Cross-document evidence links: 0133/I19-E22 supports training sessions/person-times; 0134/I19-E23 supports membership/dues trends; neither supplies 0135 target-market/customer-value outcomes. Use separate case_id and do not reuse their counts or imply a shared real case.
11. REAL replacement register: list each synthetic field, acceptable primary source, owner, source locator, privacy minimization, reconciliation procedure, and release gate.
12. Evaluator-use checklist and explicit HOLD/REJECT conditions.

## Core formulas
- Annual reach rate (%) = unique served eligible organizations ÷ eligible target-market frame × 100.
- Change (percentage points) = current reach rate − prior reach rate.
- Relative change (%) = (current rate − prior rate) ÷ prior rate × 100.
- Time reduction (%) = (baseline paired median − 90-day paired median) ÷ baseline paired median × 100.
- On-time rate (%) = on-time organizations ÷ matched organizations × 100.
- Response rate (%) = matched follow-up organizations ÷ organizations served in the period × 100.

## HOLD / REJECT conditions
HOLD if target frame criteria or denominators vary without reconciliation; if numerator counts duplicates; if pre/post measurement windows differ; if follow-up or nonresponse denominator is missing; if evidence links cannot be located; if private participant details are exposed; or if a result relies only on satisfaction without market/value measures. REJECT any unlabeled synthetic values presented as REAL, unsupported causal claims, invented customer testimony/approval, undefined market size, or use of 0133/0134 facts as this report’s results. Do not claim level 3 or 4 from the sample.


## Candidate DOCX extracted text
P001: 目標市場與顧客價值具體提升成效分析報告
P002: 文件編號：0135　｜　官方佐證要求：I19-E25　｜　版本：R01 候選稿
P003: 157 項專案藍圖：第 140 項「市場顧客價值量化：期間／分母／改善幅度」
P004: 官方查檢表勾選流水號：UNKNOWN（不得以 DOCX 0135 或藍圖第 140 項代替）
P005: 資料期間：示範市場覆蓋 2023–2025；配對顧客價值示範為 2025 年訓前與訓後 90 日
P006: 資料狀態：本報告所有結果數字與個案均為 SAMPLE／SYNTHETIC；不是原始點協會實績、不是實際市場普查、不是正式評核結果
P007: 使用界線：本件示範如何把「服務了哪些目標市場」與「顧客從訓練得到什麼可量化價值」分開測量，再以明確期間、母數、分母與計算呈現。現有材料沒有提供協會真實市場母體、名單、原始調查或營運紀錄；因此本文的 80 家、20／24／28 家、15 筆配對及其計算只能用於操作示範，不能複製到正式實績欄。
P008: 1. 摘要與使用結論
P009: 本報告對應訓練機構版指標 19「訓練系統的市場功能—目標市場及顧客的價值創造」。文件以兩條互不替代的證據線回答該要求：
P010: 1. 目標市場覆蓋：明確界定合格機構母體及年度去重服務機構數。SAMPLE／SYNTHETIC 示範值為 2023 年 20／80（25.0%）、2024 年 24／80（30.0%）、2025 年 28／80（35.0%）；逐年增加 5.0 個百分點。
P011: 2. 顧客價值：對 2025 年 28 家示範服務機構中的 15 家作訓前與訓後 90 日配對。SAMPLE／SYNTHETIC 示範的每月紀錄工時中位數由 120 分鐘降為 90 分鐘；準時完成數由 8／15 增至 12／15。
P012: 這些結果能示範完整計算和查核流程，不能證明原始點協會實際擴大了市場或提升了顧客績效。配對樣本沒有對照組，且 13／28 家未回覆；不得把變化宣稱為訓練的確定因果效果。本文不自評 TTQS 分數，也不代替評核委員判定。
P013: 2. 需求對應與文件邊界
P014: 對照欄位
P015: 正式對應與本件處理方式
P016: 文件／需求
P017: DOCX 0135 對應 I19-E25：目標市場及顧客價值創造；官方來源見《訓練機構版查核佐證文件資料表》第 7–8 頁。
P018: 157 項專案藍圖
P019: 第 140 項要求量化市場顧客價值並說明期間、分母、改善幅度；第 141 項個人訓練績效及第 142 項市場競爭／營收／流程／成本／客訴為不同證據方向。
P020: 官方查檢流水號
P021: UNKNOWN。正式流水號未從本來源包核實；0135 與 140 都是專案識別，不可冒充官方序號。
P022: 文類
P023: 多年度目標市場覆蓋及顧客價值成效分析報告，含完整示範數據、計算方法、追蹤工具、替換清冊及停收條件；不是滿意度問卷、會議紀錄或自評表。
P024: 明確排除
P025: 不把 0133／I19-E22 的班次與參訓人次當成市場分母；不把 0134／I19-E23 的會員人數或會費收入當成本件結果；不共用或暗示三件文件來自同一真實個案。
P026: 官方指標 19 的評分描述由「有提升但沒有具體紀錄評量」至「有部分提升」、「有一定程度量化效益」及「有顯著具體績效」。本段僅供定位官方題意，不表示本示範符合任何分數級距；實際評分由正式評核程序判斷。
P027: 3. 目標市場定義與計數規則（SAMPLE／SYNTHETIC）
P028: 3.1 示範客群
P029: 本示範設定的服務對象為非營利組織中負責志工排班、服務紀錄及月報彙整的行政管理人員。此客群只用來展示市場定義方式，不表示原始點協會已選定此市場或已服務這些組織。
P030: 3.2 納入、排除及去重
P031: 規則
P032: 操作定義
P033: 查核方式
P034: 納入
P035: 位於所界定服務範圍、確有志工服務活動，且至少有一名承辦人負責服務紀錄或月報的非營利組織。
P036: 依真實年度母體名冊與資格欄逐筆檢查；資料未提供前保持 UNKNOWN。
P037: 排除
P038: 無志工服務活動、無本件課程所需職務情境、重複或資格無法核實的機構。
P039: 保留排除原因代碼及覆核日期；不得以無資料者直接算入母體。
P040: 分母
P041: 當年度符合納入條件且完成去重的機構數 (N_t)。
P042: 每年保存名冊版本、納入排除規則及差異說明；真實數值目前 UNKNOWN。
P043: 分子
P044: 當年度至少一人完成本件相關訓練的合格機構去重數 (n_t)。
P045: 以機構識別碼與實際完訓證明核對；同機構多人參訓仍只計 1 家。
P046: 覆蓋率
P047: (n_t ÷ N_t × 100%)。
P048: 以相同資格和去重規則按年重算；母體變動必須披露。
P049: SAMPLE／SYNTHETIC 示例把年度母體固定為 80 家，只為清楚示範公式。這不是政府名錄、協會名冊、市場規模或市場占有率；正式分析不得照抄「80」。若不同年度的母體範圍或名冊來源改變，須先提供可比性說明，不能只比較覆蓋百分比。
P050: 4. 多年度目標市場覆蓋分析（SAMPLE／SYNTHETIC）
P051: 年度
P052: 合格目標機構母體 (N_t)
P053: 去重服務機構 (n_t)
P054: 覆蓋率 (n_t/N_t)
P055: 相較前期變化
P056: 相對變化
P057: 資料狀態
P058: 2023
P059: 80 家
P060: 20 家
P061: 25.0%
P062: 基準年
P063: 基準年
P064: SAMPLE／SYNTHETIC
P065: 2024
P066: 80 家
P067: 24 家
P068: 30.0%
P069: +5.0 個百分點
P070: +20.0%
P071: SAMPLE／SYNTHETIC
P072: 2025
P073: 80 家
P074: 28 家
P075: 35.0%
P076: +5.0 個百分點
P077: +16.7%
P078: SAMPLE／SYNTHETIC
P079: 計算：2023 覆蓋率＝20÷80＝25.0%；2024＝24÷80＝30.0%；2025＝28÷80＝35.0%。2024 較 2023 增加 30.0%−25.0%＝5.0 個百分點，相對變化為 5÷25＝20.0%。2025 較 2024 增加 35.0%−30.0%＝5.0 個百分點，相對變化為 5÷30＝16.7%（四捨五入至小數一位）。三年累計為 +10.0 個百分點；相對 2023 基準為 (35−25)÷25＝40.0%。
P080: 市場覆蓋的分子是「去重機構」，不是個人參訓人次；母體固定是假設，不是實際外部市場普查。若母體每年 80 家的假設不成立，應重算並解釋母體變動，不能保留本表結果。
P081: 5. 顧客價值測量設計（SAMPLE／SYNTHETIC）
P082: 5.1 配對方式與期間
P083: 示範於 2025 年服務的 28 家機構中取得 15 家可配對紀錄。每一列代表同一個 SAMPLE 機構在訓前基準期及課後第 90 日追蹤期的相同月報工作。因本件沒有任何真實機構或原始問卷，這 15 列全部是合成資料。
P084: 訓前工時：完成一份月度志工服務紀錄的示範分鐘數。實際調查應固定起訖點，並排除與月報無關的工作。
P085: 訓後工時：同一工作定義在課後第 90 日測量的示範分鐘數。
P086: 準時狀態：本示範以「是否在組織事前明訂的月報期限內完成」記為 1／0。示範並未取得真實期限或系統時間戳記；實際報告須引用機構適用的書面期限，否則不得計算準時率。
P087: 配對分母：15 家有兩期有效資料的機構；28 家為該年度示範服務機構總數。未回覆 13 家必須留在回覆率計算，不得刪除後只報 15 家。
P088: 5.2 測量表與資料控制
P089: 欄位
P090: 訓前基準
P091: 訓後 90 日
P092: 量測規則／必要佐證
P093: 合格機構識別碼
P094: 使用去識別化代碼
P095: 同一代碼配對
P096: 對照表另行限權保管，不放入報告或公開附件。
P097: 月報處理工時
P098: 一份相同定義月報所需分鐘
P099: 同一機構、相同工作定義的分鐘
P100: 填開始與完成日期、分鐘數、量測方式；若工作範圍不同，列為不可比並說明。
P101: 月報準時狀態
P102: 1＝在預先核實期限內；0＝逾期
P103: 使用同一期限與判定方式
P104: 保存期限來源及原始完成時間；若無期限或時間證據，填 UNKNOWN，不填 1。
P105: 訓後追蹤
P106: 不適用
P107: 課後第 90 日，允許窗口須事前固定
P108: 保存通知、回覆狀態與缺漏原因；不把未回覆者當作沒有成效。
P109: 可驗證來源
P110: 原始工時記錄或問卷
P111: 原始追蹤記錄；必要時以合法可取得的業務記錄覆核
P112: 記錄來源檔名、頁碼／欄位、版本及取得日期；目前真實來源均 UNKNOWN。
P113: 6. 15 筆配對示範資料（全數 SAMPLE／SYNTHETIC）
P114: 下表完整呈現來源包內 15 列合成資料。工時節省分鐘＝訓前分鐘−訓後分鐘，所以正數表示減少；準時欄以 1／0 表示同一測量規則下的狀態。
P115: SAMPLE 個案
P116: 訓前工時（分）
P117: 訓後 90 日（分）
P118: 節省（分）
P119: 訓前準時
P120: 訓後準時
P121: 狀態變化
P122: SYN-0135-VALUE-2025-01
P123: 180
P124: 140
P125: 40
P126: 1
P127: 1
P128: 維持準時
P129: SYN-0135-VALUE-2025-02
P130: 150
P131: 130
P132: 20
P133: 1
P134: 1
P135: 維持準時
P136: SYN-0135-VALUE-2025-03
P137: 150
P138: 120
P139: 30
P140: 1
P141: 1
P142: 維持準時
P143: SYN-0135-VALUE-2025-04
P144: 140
P145: 115
P146: 25
P147: 1
P148: 1
P149: 維持準時
P150: SYN-0135-VALUE-2025-05
P151: 135
P152: 110
P153: 25
P154: 1
P155: 1
P156: 維持準時
P157: SYN-0135-VALUE-2025-06
P158: 130
P159: 105
P160: 25
P161: 1
P162: 1
P163: 維持準時
P164: SYN-0135-VALUE-2025-07
P165: 120
P166: 95
P167: 25
P168: 1
P169: 1
P170: 維持準時
P171: SYN-0135-VALUE-2025-08
P172: 120
P173: 90
P174: 30
P175: 1
P176: 1
P177: 維持準時
P178: SYN-0135-VALUE-2025-09
P179: 115
P180: 85
P181: 30
P182: 0
P183: 1
P184: 由未準時轉為準時
P185: SYN-0135-VALUE-2025-10
P186: 110
P187: 80
P188: 30
P189: 0
P190: 1
P191: 由未準時轉為準時
P192: SYN-0135-VALUE-2025-11
P193: 100
P194: 75
P195: 25
P196: 0
P197: 1
P198: 由未準時轉為準時
P199: SYN-0135-VALUE-2025-12
P200: 95
P201: 70
P202: 25
P203: 0
P204: 1
P205: 由未準時轉為準時
P206: SYN-0135-VALUE-2025-13
P207: 90
P208: 65
P209: 25
P210: 0
P211: 0
P212: 仍未準時
P213: SYN-0135-VALUE-2025-14
P214: 85
P215: 60
P216: 25
P217: 0
P218: 0
P219: 仍未準時
P220: SYN-0135-VALUE-2025-15
P221: 80
P222: 55
P223: 25
P224: 0
P225: 0
P226: 仍未準時
P227: 7. 計算與解讀
P228: 指標
P229: SAMPLE／SYNTHETIC 計算
P230: 示範結果
P231: 訓前工時中位數
P232: 排序後第 8 筆，(n=15)：80, 85, 90, 95, 100, 110, 115, 120, 120, 130, 135, 140, 150, 150, 180
P233: 120 分鐘
P234: 訓後工時中位數
P235: 排序後第 8 筆：55, 60, 65, 70, 75, 80, 85, 90, 95, 105, 110, 115, 120, 130, 140
P236: 90 分鐘
P237: 中位數工時差
P238: 120−90
P239: 減少 30 分鐘
P240: 工時相對減幅
P241: (120−90)÷120×100%
P242: 25.0%
P243: 訓前準時率
P244: 8÷15×100%
P245: 53.3%
P246: 訓後準時率
P247: 12÷15×100%
P248: 80.0%
P249: 準時率變化
P250: 80.0%−53.3%
P251: +26.7 個百分點
P252: 配對回覆率
P253: 15÷28×100%
P254: 53.6%；未回覆 13 家，即 46.4%
P255: 以中位數比較，可降低單一極端工時對摘要數值的影響；仍須檢查兩期工作內容是否相同。這 15 組資料中的準時率改善和工時下降是合成的前後變化，不證明訓練是唯一原因。無對照組、13 家未回覆、外部工作量與人員變動均可能影響結果；未完成非回覆偏差分析前，不外推到 28 家或更大市場。
P256: 8. 可採取的管理決策示例
P257: 以下是如何把量測結果轉成可追蹤決策的 SAMPLE 範例，不是原始點協會已通過的決議。實際責任人、日期及決策須由機構依正式流程建立；目前均為 UNKNOWN。
P258: 決策議題
P259: SAMPLE 示範行動
P260: 追蹤證據
P261: 期限／責任人
P262: HOLD 觸發條件
P263: 母體穩定
P264: 每年度先凍結資格規則與名冊版本，再計算合格家數；母體變動時重算歷年可比範圍。
P265: 年度資格清單、納入／排除原因及版本差異表。
P266: 由實際機構指定；目前 UNKNOWN。
P267: 名冊來源或資格不明、重複機構未去重。
P268: 追蹤回覆
P269: 對未回覆者記錄一次以上合規提醒及未回覆原因，並比較回覆與未回覆樣本是否有明顯差異。
P270: 追蹤日期、回覆狀態、缺漏碼；不保留不必要的聯絡資訊於成果報告。
P271: 由實際機構指定；目前 UNKNOWN。
P272: 只報 15 家而隱去 28 家分母。
P273: 顧客價值
P274: 固定月報工作定義、起訖點與 90 日窗口，再重複測量；如流程已變更，將變更納入解讀。
P275: 配對測量表、同一期限證據、原始時間記錄。
P276: 由實際機構指定；目前 UNKNOWN。
P277: 前後工作定義不同或只有滿意度、沒有客觀價值量測。
P278: 9. 跨文件連結及隔離
P279: 文件
P280: 專屬證據範圍
P281: 本件如何引用／如何隔離
P282: 0133／I19-E22
P283: 年度訓練班次與參訓人次。
P284: 只可作為另一項訓練活動量文件的索引；不拿班次或人次作本件機構市場母體、服務機構分子或顧客價值結果。
P285: 0134／I19-E23
P286: 會員人數及會費收入逐年變化。
P287: 只可作為另一項會員／會費趨勢文件的索引；不拿會員或會費數字替代本件市場覆蓋與客戶結果。
P288: 0135／I19-E25
P289: 目標市場覆蓋和目標顧客價值。
P290: 本件 SAMPLE 個案代碼為 SYN-0135-VALUE-2025-XX；它與 0133、0134 的統計母體、期間及案例均分離。
P291: 若共用真實原始資料，須另外記錄來源定位及可重用欄位，並分別計算每一官方要求的指標；不得因同一來源而直接複製結果或把不同官方用途合併。
P292: 10. SAMPLE 追蹤工具（可用於未來真實蒐集；本表不是已完成原件）
P293: 10.1 訓前／資格與基準表
P294: 欄位
P295: 填寫規則
P296: 必填驗證
P297: 去識別機構代碼
P298: 使用不含姓名或聯絡資訊的唯一代碼；身分對照表另行限權保管。
P299: 代碼唯一，不跨組織重複。
P300: 市場資格
P301: 勾選符合／不符合並記錄理由。
P302: 依第 3.2 節納入標準覆核。
P303: 服務年度及課程
P304: 記錄年度、課程代碼及完成狀態。
P305: 以正式班級與出席／完訓原件核對。
P306: 月報工作範圍
P307: 記錄包含及排除的工作步驟。
P308: 前後測使用相同定義。
P309: 訓前分鐘數
P310: 記錄日期、分鐘數及量測來源。
P311: 必須是有效數字，不能以空白或估計冒充已量測。
P312: 訓前是否準時
P313: 1／0／UNKNOWN，並記錄使用的期限版本。
P314: 無可核對期限或完成日期即 UNKNOWN。
P315: 10.2 訓後 90 日追蹤問題
P316: 1. 您是否在本課程後持續負責相同類型的志工月報？（是／否；若否，記錄原因，不納入配對分析。）
P317: 2. 請依相同工作範圍，填寫最近一份月報從開始彙整至完成核對所需分鐘數；如非實測，勾選「自陳估計」，不得與實測混為一類。
P318: 3. 該份月報是否在機構預先訂定的期限前完成？（是／否／無可核期限）。請記錄期限版本及可核對的完成日期；本問卷本身不證明期限或時間戳記真實。
P319: 4. 課程內容是否實際用於這項月報工作？（已使用／部分使用／未使用／不適用）。說明具體工作步驟，不收集不必要的個人資料。
P320: 5. 期間是否有系統更換、人員異動、案件量變化或其他可能影響工時／準時的因素？（逐項勾選並簡述）。
P321: 6. 是否有可供合法抽核的原始工作記錄？（有／沒有／尚待取得）。填實際來源位置；未取得前狀態為 UNKNOWN。
P322: 7. 本次資料是否同意用於彙總分析？依實際蒐集法規與組織程序處理；未確認授權前不納入可識別資料。
P323: 10.3 資料品質處理
P324: 同一機構只保留一組有效配對值；重複提交需記錄保留規則。
P325: 缺漏、拒答、無期限、無法配對分別標記，不以零值補填。
P326: 極端值先核對原始記錄，不可只因影響中位數而刪除；如排除，記錄規則及前後數值。
P327: 追蹤回覆率以全部合格受服務機構為分母；報告未回覆數及原因分類。
P328: 公開報告以彙總數呈現；個人識別及機構秘密依權限分離保存。
P329: 11. REAL 資料替換與放行清冊
P330: 目前沒有協會真實母體名冊、參訓機構清單、問卷原件、時間記錄、期限證明或核准記錄提供給本文件。下表列的是未來可接受的原始證據種類，不是已取得的原件；所有現行來源定位標為 UNKNOWN。
P331: 清冊項目
P332: SAMPLE 示範值
P333: 可接受的 REAL 原始來源
P334: 現況／替換門檻
P335: 年度目標市場母體
P336: 每年 80 家
P337: 有權使用、定義一致的年度市場名冊或可重建的合格機構清單；保存納入／排除與去重依據。
P338: UNKNOWN；取得原件、來源日期、適用範圍並核對每年變動前不得標 REAL。
P339: 年度服務機構數
P340: 20／24／28 家
P341: 正式報名、實際出席／完訓或服務紀錄，依機構唯一碼去重。
P342: UNKNOWN；報名不等於已服務，須按文件所採服務定義核對。
P343: 訓前／訓後工時
P344: 中位數 120／90 分鐘；15 組配對
P345: 同一工作定義的原始量測表、日期與必要的操作紀錄；自陳資料須明示來源型態。
P346: UNKNOWN；兩期時間窗、工作步驟及配對碼核實後再計算。
P347: 準時率
P348: 8／15 → 12／15
P349: 機構事前設定的月報期限及可核對完成日期／系統紀錄。
P350: UNKNOWN；無可查期限或完成時間時不得計算準時率。
P351: 追蹤回覆率
P352: 15／28（53.6%）
P353: 當期合格服務機構總清單及回覆／未回覆狀態紀錄。
P354: UNKNOWN；不得只保存回覆者而刪除母數或未回覆數。
P355: 管理決策
P356: 依量測採取的 SAMPLE 追蹤行動
P357: 實際機構依正式程序形成的會議／核准／追蹤原件。
P358: UNKNOWN；不得以本報告示範行動冒充協會決議。
P359: 放行前需由實際資料保管人與另一覆核者完成逐列來源核對、公式重算、缺漏／未回覆檢查、隱私遮蔽及跨文件一致性檢查。覆核人、日期、來源定位及核准狀態須引用實際原件；目前沒有這些資料，不填造人名或簽核。
P360: 12. 評核員使用檢查表
P361: 此表只協助核對文件證據是否可追溯，不代替評核員判分。委員應以官方原件及適用版本自行判讀；本候選的示範欄不得勾為 REAL。
P362: 查核問題
P363: 合格所需證據
P364: 現場記錄
P365: 官方需求是否正確？
P366: I19-E25 正文、官方來源版本／頁碼及文件映射可核對；官方流水號保持 UNKNOWN 直到原件證明。
P367: □符合　□不符合　□待查；頁碼／原件：＿＿＿＿
P368: 目標市場母體是否可重建？
P369: 納入／排除、年度範圍、來源日期及去重程序明確，母體差異可解釋。
P370: □符合　□不符合　□待查；來源定位：＿＿＿＿
P371: 分子是否是機構而非人次？
P372: 每年度服務機構清單能去重並對應實際服務紀錄。
P373: □符合　□不符合　□待查；核對筆數：＿＿＿＿
P374: 顧客價值是否具體？
P375: 至少一項可重複測量的價值結果、定義、期間、分母與前後配對資料。
P376: □符合　□不符合　□待查；來源定位：＿＿＿＿
P377: 追蹤是否完整？
P378: 90 日窗口、回覆分母、未回覆數及資料缺漏均揭露。
P379: □符合　□不符合　□待查；未回覆數：＿＿＿＿
P380: 是否聲稱超過證據？
P381: 無未經控制的因果宣稱；無假造客戶原話、簽核、第三方證明或 TTQS 自評分數。
P382: □符合　□不符合　□待查；需更正處：＿＿＿＿
P383: SAMPLE／REAL 是否分明？
P384: 每一數字都能回到 SAMPLE 標示或實際原件；公開版不含不必要個資。
P385: □符合　□不符合　□待查；來源定位：＿＿＿＿
P386: 13. HOLD／REJECT 條件
P387: 以下是本候選的證據品質閘門，不是官方評分、扣分或處分決定。
P388: HOLD： 官方映射或適用版本未核實；目標市場母體來源、資格或去重不清；前後測工作定義不同；分母、未回覆或追蹤期間缺失；準時期限或完成日期無法核對；配對資料來源不明；跨文件事實未隔離；或真實資料尚未取得。HOLD 時保留 SAMPLE／UNKNOWN，不以估算替代。
P389: REJECT 本候選證據： 把合成值標成協會真實實績；以人次、會員或會費冒充本件市場價值；捏造政府名錄、組織名冊、客戶見證、時間戳、簽核或核准；把只有回覆者的比例當成全體；以單一滿意度分數取代客觀價值測量；或對無對照組的前後變化宣稱必然因果。此處「REJECT」只表示該證據包不可採用，不預判 TTQS 正式分數。
P390: 14. 來源定位與候選狀態
P391: 官方來源：訓練機構版《查核佐證文件資料表》，指標 19，PDF 第 7–8 頁；本地候選來源包保留官方原 PDF 及第 7–8 頁抽取件。
P392: 專案藍圖：03_157_CHECKBOX_BLUEPRINTS.md 第 140 項；相鄰 141、142 項僅用於排除錯件。
P393: 寫作規則：02_GENRE_WRITING_MANUAL.md 指標 19 段落。
P394: 來源分支快照：work/ttqs-one-document-quality-contract-20261016，本件來源準備的讀取基準 commit 8ff5f8cbe6df80be9ed60577ed324e5a0a18f382；精確 blob 與檔案雜湊見同包 SOURCE_MANIFEST_0135_R01.json。
P395: 本件仍是 SAMPLE／SYNTHETIC 候選；獨立 exact-SHA 語意審查待完成；正式接受及送審未授權。
P396: 結論：本報告展示了如何分開計算市場覆蓋與顧客價值、明示期間和分母、披露未回覆並把前後量測限制說清楚。由於 REAL 原件尚未提供，本報告不能證明原始點協會的實際成效；取得真實來源前，全部示範數值必須維持 SAMPLE／SYNTHETIC。
