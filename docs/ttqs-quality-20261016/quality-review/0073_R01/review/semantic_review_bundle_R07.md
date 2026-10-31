# Independent semantic review request — DOCX 0073 R07

Review target exact DOCX SHA-256: `25f33eb58f9401b33d3ed9f56bb0d99985be564677050848a68937bdca51221c`
Extracted text SHA-256 (derived from that DOCX): `04152746fda290207d324c6ba54b0c80796c05ea2b9961f43378f5c2a06a695a`
Review route: independent OpenCode v2 CLI model `opencode/beam-free`; the writer used `opencode/deepseek-v4.1-flash-free`.

Perform an independent semantic review. Do not treat builder receipts or this prompt as evidence of PASS; decide from the source mapping, blueprint, underlying synthetic data summaries and the complete extracted candidate content below. This review covers semantic content; it does not claim pixel inspection. The separately recorded visual receipt covers the rendered pages.

## Binding and official requirement
- Document ID: 0073.
- Official requirement: I17A-E01.
- Official checkbox serial: 080 (not the document ID).
- Official requirement text: 「課後滿意度調查分析與課後檢討講師、學員、人資、部門主管等利害關係人的建議回饋紀錄。」
- Official source is the training-institution evidence form, printed page 5 / PDF page 5, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Unique Blueprint source: `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`, blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`, checkbox row 080.
- Neighbor boundaries: 0072 = I16-E03 / checkbox 078 (audit-process evidence); 0074 = I17A-E02 / checkbox 081 (course closure report, planning, opening recommendation). Do not let this 0073 report claim those deliverables.
- All example data below are synthetic: 16 forms distributed/returned, 15 valid, S16 excluded for missing Q4/Q6/Q7; 120 valid item responses; total score 479; 90 positive responses; mean 3.9917 (3.99); positive rate 75.00%; returned 16/16; valid/returned 15/16 (93.75%). Stakeholder groups are separate: learner n=15, instructor n=1, HR/training administration n=1, department managers n=2. No real evidence is supplied; REAL=UNKNOWN/HOLD.
- Sample case identifier: SYN-0073-2026-A01; example course date 2026-08-15 is synthetic. Sample recommendations are unapproved proposals, never association decisions.

## Required review
Check: (1) exact official purpose and proper document genre; (2) unique, document-specific Blueprint coverage and adequate source locators; (3) a mature, directly usable post-course satisfaction and multi-stakeholder feedback analysis record, with questionnaire, distribution/return/validity rules, complete results, separate stakeholder feedback, synthesis/divergence, follow-up proposals and reusable forms; (4) internal math and consistency of counts, percentages, sample sizes and case identifiers; (5) clear SAMPLE/SYNTHETIC versus REAL/UNKNOWN/HOLD boundary and no fabricated approvals, actual execution, signatures, credentials or third-party originals; (6) correct distinction from 0072 and 0074; (7) whether a training administrator and evaluator could use it without another manual; (8) any material omission or misleading inference.

Return a clear `PASS`, `PARTIAL`, or `FAIL` tied to this exact SHA. Give section/table locators (by section title and distinctive row/text; page numbers only if inferable), explain every material gap, and separate semantic verdict from visual verdict. If a material requirement is missing, do not soften it because the document is long or polished. Do not invent acceptance or real records.

---
## Source: unique blueprint (complete)

# UNIQUE BLUEPRINT 0073 R01

## Binding and source identity
- Project: TTQS_ONE; candidate only.
- Document ID: 0073.
- Requirement ID: I17A-E01.
- Official checkbox serial: 080. It is not the document ID.
- Indicator: 17, sub-item 17a Reaction Evaluation.
- Official evidence table: training-institution edition, PDF printed page 5 / physical page 5; SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Exact evidence text: 「課後滿意度調查分析與課後檢討講師、學員、人資、部門主管等利益關係人的建議回饋紀錄。」
- Current official 157-row blueprint source: `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`, Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; row 080 says 「滿意度與各方回饋：問卷、分佈、講師學員意見及分析」 and requires specific source location, substantive example, result/decision, and cross-document fact links.
- Current Human Mission source blob: `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md`, `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`.
- Current Goal execution source blob: `docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md`, `62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d`.
- Official 129-to-142 crosswalk SHA-256: `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`; requirement reconciliation SHA-256: `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9`. Their verified source readback binds I17A-E01 to deliverable 0073, with R04 crosswalk title 「課後滿意度調查分析與課後檢討講師、學員、人資_可直接使用成品」.
- Prior expanded blueprint JSON and all archived DOCX are discovery/history only; do not copy or reuse archived body text. Rebuild FROM_SOURCE_ONLY.

## Unique document purpose and genre
A post-training satisfaction and stakeholder-feedback analysis report that records and analyzes the learner questionnaire plus instructor, HR/training administration, and department-manager feedback, explains evidence strength and response distribution, and turns findings into traceable proposed improvements for the next course. It must work as a real operating report when genuine records are later inserted, while the current filled example is clearly SAMPLE/SYNTHETIC.

This is not the complete course-closure report, course plan, opening recommendation, or action-plan record assigned to adjacent I17A evidence. The closest neighbor is DOCX 0074 / I17A-E02 / checkbox 081, which owns the course-closure analysis, course-planning record, and opening recommendation. 0073 may point to that document type as a downstream destination, but must not claim that a real 0074 or a real shared case already exists. A sample handoff key may be labelled proposed and unverified.

## Reader and use
Reader: association training administrator and evaluator. Use after a training session when learner surveys and stakeholder comments are available. The report must explain how to check the survey denominator, validate responses, compute statistics, code feedback, distinguish signal from small-group opinion, record decisions, and follow up. A reader should be able to reuse the questionnaire and tables without another manual.

## Required complete body
1. Cover/first page: exact doc ID, requirement, checkbox, candidate/revision, status; purpose, intended reader, when/how to use, output; prominent 「SAMPLE/SYNTHETIC 示範，非本會實際調查、辦訓、決議或核准」 and REAL=UNKNOWN/HOLD.
2. Official requirement and scope: reproduce exact official text and identify PDF page 5. Explain 17a tiers: 0 not performed; 1 satisfaction survey; 2 analyze satisfaction and learner/instructor feedback and use the analysis as a basis to revise the next course. Do not claim this candidate proves actual tier attainment.
3. Method and controlled instrument: complete eight 1–5 scale questions and all five anchored response labels, eligibility, distribution/return/validity rules, nonresponse and exclusion rules, anonymity and privacy controls, open-ended questions, stakeholder-feedback log fields and coding instructions.
4. Complete worked SAMPLE dataset, not an empty template: 15 valid learner response rows with eight item scores, one returned but invalid/incomplete response, question-by-question frequency distribution, response rate, valid rate, mean and positive rate, denominator, and overall calculation. Preserve the supplied data exactly and show calculations that can be recomputed.
5. Stakeholder feedback records: learner comment themes and one record each for synthetic instructor, HR/training administrator, and two department managers (report n=2 for managers; do not infer a population from this small sample). Each record links feedback, evidence basis, analysis, proposed response, status, responsibility role, timing, follow-up measure, and limitation.
6. Findings and analysis: rank low areas, distinguish closed-question scores from multi-stakeholder comments, identify converging/diverging evidence, give bounded conclusions, and state why the example is not real performance evidence.
7. Traceable next-course recommendations: each has finding, evidence, proposed change, role-based owner, due trigger, measure, and hold/escalation condition. Every such item must be explicitly a synthetic proposal, not an association decision or approval. Keep full course plan/closure artifacts within 0074's scope.
8. Cross-document mapping and negative-neighbor check: 0072/I16-E03/checkbox 078 is internal/external audit records; 0073/I17A-E01/checkbox 080 is post-course satisfaction plus stakeholder feedback analysis; 0074/I17A-E02/checkbox 081 is course closure/analysis/planning/opening recommendation. Explain why this body cannot be substituted for either neighbor. Do not invent 0074 content or claim an actual cross-document case link.
9. Practical reusable forms/appendices: blank 8-item questionnaire; feedback log; analysis table; decision/follow-up register; evidence locator and reviewer checklist. Blank operating instruments may be blank, but the worked example must be complete.
10. Synthetic replacement register: every synthetic date, count, score, role, comment, formula output and proposed decision must have an ID, document locator, data type, and exact real source to replace it. Current REAL values remain UNKNOWN/HOLD.

## Supplied worked-example dataset
Use only the attached/generated R01 input files. Case ID `SYN-0073-2026-A01`; synthetic training session date `2026-08-15`; sample distribution 16 learners, 16 returned, 15 valid, one incomplete returned form excluded by the stated rule. Valid learner dataset rows S01–S15. Scale is 1–5; positive means 4 or 5. Stakeholder feedback is separate from learner survey denominator: learners n=15; instructor n=1; HR/training administrator n=1; department managers n=2. All codes, dates, text, and values are synthetic.

The report must preserve calculated results from `question_summary_R01.csv` and raw rows from `learner_scores_R01.csv`; do not alter score values or denominators. It must state overall: 120 valid item responses, 479 points, mean 3.99 (479/120=3.9917 before rounding), positive answers 90/120 = 75.00%; returned rate 16/16 = 100%; valid response rate 15/16 = 93.75%; valid/returned = 15/16 = 93.75%. Per item means and positive rates are in the supplied summary.

## Acceptance/hold rules
- If document binding, official source text, or checkbox mapping differs, stop and report the mismatch; do not silently relabel.
- If any score distribution, sum, denominator, or percentage fails recomputation, mark technical QA FAIL and repair only the data/text inconsistency.
- If REAL data is absent, keep SAMPLE/SYNTHETIC throughout and REAL UNKNOWN/HOLD; never invent actual respondents, instructor identities, approvals, attendance, decisions, or outcomes.
- Small stakeholder counts are descriptive only; do not infer prevalence. Avoid exposing names or personally identifiable learner data.
- Any proposed improvement not supported by the supplied example must be labelled as an optional future consideration, not a finding.
- Candidate is not formally accepted. Do not represent the organization as having adopted the report or its recommendations.
- Typography target: body >=10.5 pt, table text >=9.5 pt. Maintain readable tables and avoid shrinking to force page count.


---
## Source: question summary CSV (synthetic)

item_id,question,n_valid,score_sum,mean,count_1,count_2,count_3,count_4,count_5,positive_n,positive_rate
Q1,課程內容與志工服務溝通及紀錄情境相關,15,61,4.07,0,0,3,8,4,12,80.00%
Q2,課程目標清楚且知道完成後要能做什麼,15,62,4.13,0,0,3,7,5,12,80.00%
Q3,教材順序與內容安排容易理解,15,67,4.47,0,0,1,6,8,14,93.33%
Q4,講師說明、示範與回應問題有幫助,15,57,3.80,0,1,4,7,3,10,66.67%
Q5,實作練習時間足以完成交接與紀錄步驟,15,54,3.60,0,2,5,5,3,8,53.33%
Q6,教材與流程提示在課後容易查找使用,15,57,3.80,0,1,4,7,3,10,66.67%
Q7,我有信心依步驟完成基本服務紀錄與交接,15,58,3.87,0,1,3,8,3,11,73.33%
Q8,整體而言我對本次示範課程感到滿意,15,63,4.20,0,0,2,8,5,13,86.67%


---
## Source: stakeholder feedback CSV (synthetic)

record_id,group,n,synthetic_feedback,analysis,proposed_response,status
T01,講師,1,學員能跟上分步示範；練習時間偏短，容易跳過紀錄欄位的自我核對。,與Q5較低及學員增加練習主題方向一致；單一講師意見只作案例觀察。,示範後加入第二輪交接與欄位核對練習；不宣稱已採納。,SAMPLE提案，未核准
H01,人資／訓練行政,1,彙整表應保留發放、回收、有效份數與排除理由；報告不要呈現可辨識個人的資料。,屬資料品質與隱私控制建議，不可併入學員滿意度分母。,每次調查以匿名代碼彙總；小群組只報實際n並加限制說明。,SAMPLE提案，未核准
M01,部門主管,1,希望示範交接情境對應不同服務角色，減少只看單一例子的情形。,與學員提出增加角色案例相互呼應；僅為單一樣本回饋。,下一輪案例卡試列不同角色情境，待課程負責人確認適切性。,SAMPLE提案，未核准
M02,部門主管,1,建議流程提示卡能列出交接前後需核對的欄位。,與學員要求流程卡及欄位示範一致；不得推論所有部門主管均有此意見。,先用合成案例試作提示卡，再由實際使用者核對。,SAMPLE提案，未核准


---
## Source: returned forms CSV (synthetic)

respondent_id,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,response_status
S01,3,5,5,5,5,5,5,5,VALID
S02,4,4,4,4,4,4,4,4,VALID
S03,4,4,5,3,3,3,3,4,VALID
S04,3,4,4,4,4,4,4,4,VALID
S05,4,3,5,4,4,4,4,3,VALID
S06,4,4,4,3,3,3,4,4,VALID
S07,5,5,5,4,4,4,4,4,VALID
S08,4,5,5,4,4,4,4,4,VALID
S09,4,4,4,3,3,3,3,4,VALID
S10,5,5,5,4,5,4,4,5,VALID
S11,4,3,4,4,3,4,5,5,VALID
S12,3,4,3,3,3,3,3,3,VALID
S13,4,5,5,5,5,5,5,5,VALID
S14,5,4,4,5,2,5,4,4,VALID
S15,5,3,5,2,2,2,2,5,VALID
S16,5,4,4,,5,,,4,EXCLUDED: 3 of 8 scale items missing; no imputation


---
## Candidate DOCX text and tables, extracted from the exact SHA above


SAMPLE/SYNTHETIC 示範；非本會實際調查、辦訓、回饋、決議或核准
課後滿意度調查分析與課後檢討講師、學員、人資、部門主管等利益關係人的建議回饋紀錄
文件編號：0073　要求編號：I17A-E01　指標：17（17a 反應評估）　官方勾選序號：080
文件狀態：R01 候選版本（candidate only，尚未正式核定）
文件製作日期（修訂日）：2026-10-19（僅為文件準備日期，非示範課程日期）
示範課程日期（合成）：2026-08-15　示範案件編號：SYN-0073-2026-A01
本文件中所有日期、人數、分數、回應、意見、發現、提案與狀態，全部為 SAMPLE/SYNTHETIC（合成示範） 資料。真實證據狀態為 REAL=UNKNOWN/HOLD（未知／暫緩，尚未取得）。本文件不得被理解為本會已完成任何實際調查、辦訓、回饋、決議或核准。
第 1 節　文件目的、閱讀對象與使用方式
1.1 文件目的
本文件是一份課後滿意度調查分析與多方利益關係人（講師、學員、人資／訓練行政、部門主管）建議回饋紀錄的操作型報告。其目的有四：
1. 留下可查核的紀錄：說明某一次訓練課程的學習者滿意度問卷如何發放、回收、判定有效、計算與分析，並同時收錄講師、人資／訓練行政、部門主管的回饋。
2. 把分數與意見連起來看：不是只呈現滿意度數字，而是把「封閉式問卷分數」與「多方質性回饋」並列，辨識一致與不一致之處。
3. 把發現轉成可追溯的下一步：每一項低分項目或匯聚回饋，都能對應到「發現→證據→下一期課程調整→負責角色→時機→追蹤措施→暫緩／升級規則」。
4. 可被重複使用：文件內的問卷、紀錄表、分析表與決策登錄表，在真實資料到位後可直接沿用填寫，無須再找另一份操作手冊。
本文件對應官方要求 I17A-E01、官方勾選序號 080，屬指標 17a「反應評估（Reaction Evaluation）」層級。
1.2 閱讀對象
主要讀者：本會訓練行政人員（負責問卷發放、回收、有效性判定、統計與紀錄保存）。
次要讀者：本會 TTQS 評核人員／內部稽核人員（負責查核此份紀錄是否具備來源位置、實質內容、結果或決策，以及跨文件事實連結）。
1.3 何時使用
在一場訓練課程結束後、且已取得學習者問卷與利害關係人回饋時使用。使用前應先備妥：簽到／發放回收台帳、原始（去識別化）問卷、有效性覆核紀錄、講師與主管回饋原件。
1.4 操作步驟（總覽）
1. 依第 3 節確認問卷版本、發放對象與匿名規則。
2. 回收後逐份判定有效／無效，記錄排除理由（第 3、4 節）。
3. 依第 4 節公式逐題計次、計算平均與正向率，並算出整體指標。
4. 依第 5 節整理講師、人資／訓練行政、部門主管回饋，逐筆編碼（第 3 節編碼規則）。
5. 依第 6 節合併分數與回饋做收斂／分歧分析，標示低分項目與證據限制。
6. 依第 7 節把發現轉成可追溯建議（每項皆為合成提案，非本會決策）。
7. 依第 8 節核對文件邊界（與 0072、0074 之區別）。
8. 真實使用時，依第 9 節附錄表單填寫，並依第 10 節替換登錄逐項以真實資料取代合成值。
1.5 產出（Output）
一份填寫完成的課後滿意度與多方回饋分析紀錄（本文件即為已填寫的示範版本）。
逐題統計表、整體統計、利害關係人回饋紀錄、發現與分析、可追溯建議矩陣。
可供下一期課程修正使用的提案清單（非核准決策）。
1.6 SAMPLE 與 REAL 邊界
第 2 節　官方要求、來源位置與適用範圍
2.1 官方證據要求（原文照錄）
「課後滿意度調查分析與課後檢討講師、學員、人資、部門主管等利益關係人的建議回饋紀錄。」
2.2 來源位置與版本身分
依官方勾選藍圖，第 080 列要求本項證據具備四項要素：(a) 具體來源位置、(b) 實質內容或範例、(c) 結果或決策、(d) 跨文件事實連結。本文件正文即針對此四要素逐項提供（分別見第 4、5、6、7、8、9 節）。
2.3 指標 17a（反應評估）等級區分
重要聲明：本文件為 R01 候選示範，不得被解讀為本會已達到第 1 級或第 2 級。等級判定須以本會真實紀錄與評核人員現地查核為準；本文件不主張任何等級成就。
2.4 適用範圍
本文件處理的是「課後」的滿意度與多方回饋；不涵蓋課程前規劃、辦訓過程記錄、或完整結案報告（見第 8 節文件邊界）。
第 3 節　方法與受控工具
3.1 問卷架構
問卷採 1–5 分李克特量表，共 8 題封閉式題目，並於其後設開放式意見欄位。量表五個錨點標籤如下：
正向（positive）定義為分數 4 或 5。
3.2 八題題目（題目文字須與資料集一致）
3.3 開放式題目（建議題目）
1. 本次課程中，哪一個部分對您最有幫助？請說明。
2. 您建議下一期課程可以增加、減少或調整什麼？
3. 其他補充（可自由填寫）。
（示範資料集中，開放式回覆以逐位學習者的「合成意見摘要」形式呈現，見第 5 節與附錄 C。）
3.4 發放、回收與有效性規則
發放對象：完成課程之學習者（志工）。示範案件中發放對象為 16 位學習者。
回收：所有交回之問卷（含填寫不完整者）均計入「回收份數」。
有效性判定（完整性規則）：8 題封閉式題目中，任一題缺答即視為不完整；本報告採不放寬、不插補（no imputation）規則，缺答之問卷整份排除於統計之外，且不得以其餘已填分數替代或補值。
分母使用：學習者問卷統計之有效 n，僅計入通過完整性規則的問卷；講師、人資、部門主管之回饋不併入學習者滿意度分母。
不回覆處理：未交回者計入「未回收」，不插補、不以均值代替。
3.5 匿名與隱私控制
問卷以匿名代碼（如 S01、S02……）彙整，不記錄姓名或可辨識個人的資訊。
開放式意見於分析前先去識別化；若意見含可辨識資訊，於彙整時移除。
小群組（例如部門主管 n=2）僅呈現實際 n 並加註限制說明，不得據此推論全體。
3.6 利害關係人回饋紀錄欄位（回饋登錄表欄位定義）
3.7 質性回饋編碼規則
1. 逐筆閱讀開放式意見與回饋，萃取關鍵需求語意。
2. 以主題（primary_theme）歸類，同義合併（例如「練習時間偏短」「想多做一次」歸為「增加練習」）。
3. 每個編碼保留來源（respondent_id／record_id）與來源狀態（SAMPLE/SYNTHETIC）。
4. 編碼結果須可回溯至原始回覆；同一意見可跨主題時，標註主要主題並保留次主題備註。
5. 小樣本意見不得計數成「全體比例」，僅作描述性說明。
第 4 節　完整示範資料集與統計（已填寫，可直接重算）
本節全部數值為 SAMPLE/SYNTHETIC。示範案件編號 SYN-0073-2026-A01，示範課程日期 2026-08-15。
發放 16 份、回收 16 份、有效 15 份、無效 1 份（S16）。
4.1 有效學習者逐筆分數矩陣（S01–S15，Q1–Q8）
為維持欄位寬度與可讀性，逐筆分數分成兩張表；以匿名代碼逐列配對，兩表共同構成同一筆完整 Q1–Q8 回覆。
同一匿名代碼之後四題
4.2 回收但無效之問卷（S16）與排除理由
排除理由（原文）：EXCLUDED: 3 of 8 scale items missing; no imputation。
處理：S16 之全部量表數值（含已填的 Q1、Q2、Q3、Q5、Q8）一律排除於統計之外，且不以其已填值代替缺答值。S16 之缺答狀態亦納入替換登錄（見第 10 節）。
4.3 逐題頻率、總分、有效 n、平均與正向率
計算公式：
題項平均 = 題項總分 ÷ 有效 n
題項正向率 = 正向回答數（4 分及 5 分）÷ 有效 n × 100%
A. 分數分布（各列分數次數合計應等於有效 n=15）
B. 逐題計算結果（正向定義為 4–5 分）
逐題平均之代入示例（可重算）：
Q1：61 ÷ 15 = 4.0667 → 4.07
Q3：67 ÷ 15 = 4.4667 → 4.47
Q5：54 ÷ 15 = 3.6000 → 3.60
Q7：58 ÷ 15 = 3.8667 → 3.87
Q8：63 ÷ 15 = 4.2000 → 4.20
逐題正向率之代入示例（可重算）：
Q3：14 ÷ 15 = 0.9333 → 93.33%
Q5：8 ÷ 15 = 0.5333 → 53.33%
Q7：11 ÷ 15 = 0.7333 → 73.33%
Q8：13 ÷ 15 = 0.8667 → 86.67%
4.4 整體統計
計算公式
有效題項回答數 = 有效 n × 題數 = 15 × 8 = 120
整體平均 = 全部題項總分 ÷ 有效題項回答數 = 479 ÷ 120 = 3.9917 → 3.99
整體正向率 = 全部正向回答數 ÷ 有效題項回答數 × 100% = 90 ÷ 120 = 75.00%
回收率 = 回收份數 ÷ 發放份數 = 16 ÷ 16 = 100.00%
有效／發放率 = 有效份數 ÷ 發放份數 = 15 ÷ 16 = 93.75%
有效／回收率 = 有效份數 ÷ 回收份數 = 15 ÷ 16 = 93.75%
4.5 分母分離原則
多方回饋以獨立紀錄呈現（第 5 節），不得與學習者問卷分母混合計算。
4.6 資料品質核對
本節的 15 份有效問卷逐筆分數、8 題彙總表與合成替換登錄已交叉核對。登錄共 264 筆；有效問卷矩陣重算為 120 個題項回答、總分 479、正向回答 90、整體平均 3.9917（四捨五入 3.99）、整體正向率 75.00%。各題分數分布、分母、平均與正向率均與矩陣一致。S16 的 5 個已填答案及 3 個缺答狀態只留作排除紀錄，不納入任何題項統計。
若日後替換任何 REAL 原件，應重新計算並更新各題統計、整體統計和 replacement register；若任一數值無法逐筆重算，該版應標示 QA HOLD，暫不供評核引用。
第 5 節　利害關係人回饋紀錄（多方，獨立於學習者分母）
以下均為 SAMPLE/SYNTHETIC 合成回饋。小樣本僅作描述，不得推論全體。
5.1 學習者意見主題彙整（n=15）
主題分布（描述性）：增加練習 3 筆（S02、S04、S09）、分步示範 3 筆（S06、S10、S12）、保留案例 2 筆（S07、S15）、其餘主題各 1 筆。
5.2 非學習者利害關係人回饋紀錄
人數說明：講師 n=1；人資／訓練行政 n=1；部門主管 n=2（M01、M02 兩位，僅此二人，不得推論為全體部門主管之意見）。
第 6 節　發現與分析
6.1 低分項目排序（以題項平均由低至高）
6.2 示例決策規則（非官方 TTQS 門檻）
為使分析可操作，本報告以示例決策規則標示關注項目：
示例規則 A：題項平均 < 4.00 者，列為「需優先檢視」。
示例規則 B：題項正向率 < 80% 者，列為「需優先檢視」。
必須聲明：上述 4.00 與 80% 僅為本示範報告為使流程可運作而設的示例門檻，不是 TTQS 官方門檻，也不代表本會既有規定。真實使用時，門檻應由本會依自身制度設定。
依示例規則，Q5、Q4、Q6、Q7 四項落入「需優先檢視」。
6.3 整體表現
整體平均 3.99（479 ÷ 120），略低於示例門檻 4.00。
整體正向率 75.00%（90 ÷ 120），低於示例門檻 80%。
高分項為 Q3（4.47／93.33%） 與 Q8（4.20／86.67%），顯示教材順序與整體滿意度相對受到肯定。
低分項集中在實作練習時間（Q5）、講師說明與示範（Q4）、課後查找便利性（Q6）、信心（Q7）。
6.4 收斂（convergent）證據
1. 練習時間：Q5 為最低分（3.60／53.33%）；講師 T01 亦指出練習時間偏短；學員 S02、S04、S09 均提出增加練習。三類來源方向一致。
2. 流程提示與欄位：Q6 偏低（3.80／66.67%）；學員 S05、S11 要求錯誤提醒卡／流程卡；部門主管 M02 建議提示卡列出核對欄位。方向一致。
3. 分步示範與信心：學員 S06、S10、S12 肯定分步示範；S03 希望欄位再示範；與 Q7 信心題（3.87／73.33%）之偏弱呼應。
4. 角色情境：學員 S08 提出增加角色案例；部門主管 M01 亦有相同方向。
6.5 分歧（differing）證據
1. 滿意度分數 vs. 整體回饋：Q8 整體滿意度 4.20 屬高分，但多筆開放式意見仍指向練習時間與查找性不足；顯示「整體滿意」與「特定執行面向待改」可並存，不可只取平均數下結論。
2. Q4 相對偏低但屬「講師」面向：講師 T01 自述練習時間不足，與 Q4（講師說明、示範有幫助）3.80 之分數方向不衝突但角度不同：Q4 反映學員對講師之評價，T01 反映講師對課程安排之觀察——兩者來源與分母不同，不得合併為同一比率。
6.6 證據限制（Limitations）
本案為小型且非隨機之示範樣本（學習者 n=15；各利害關係人 n=1～2），僅能描述這一個合成案例，不得推論母體。
學習者意見為合成摘要，非真人逐字紀錄；不能作為任何真實人物立場之證明。
部門主管僅 2 筆回饋，不得推論「所有主管」皆持相同意見。
平均數與正向率受極端值影響有限但仍受小樣本影響；例如 Q5、Q7 之部分低分（2 分）拉低平均。
本示範不構成真實績效證據：所有數字來自合成案件 SYN-0073-2026-A01，真實資料狀態為 UNKNOWN/HOLD。
第 7 節　可追溯的下一期課程建議（每項皆為合成提案，非本會決策）
聲明：以下每一列均為 SAMPLE/SYNTHETIC 提案，不是本會之決議或核准。每項建議均須待本會相關角色正式會議與核准後方可能成為決策。完整課程計畫與結案報告屬 0074 之範圍，本節僅保留「由回饋導出的下一期調整提案」。
執行與追蹤欄位（以建議編號連結上表）
選項性未來考量（非發現）：如未來有更多場次資料，可考慮建立跨場次趨勢比較；此為未由本示範資料支持的未來選項，不列為本次發現。
第 8 節　跨文件對照與負向鄰項檢查
8.1 三份鄰近文件之界線
8.2 為何本文件不能替代 0072 或 0074
不能替代 0072（I16-E03／078）：0072 是稽核程序與稽核紀錄，其證據核心在稽核計畫、稽核發現與稽核追蹤；本文件是課後滿意度與回饋分析，兩者的紀錄類型、責任角色與查核目的不同。若把本文件放入 078，會缺少稽核程序與稽核紀錄要素。
不能替代 0074（I17A-E02／081）：0074 是課程結案／課程規劃／開課建議，其核心為完整結案分析與下一期課程規劃文件；本文件僅止於「由課後回饋導出的調整提案」，不含完整課程計畫或結案結論。完整課程計畫與結案報告保留於 0074 範圍。本文件僅可指向該下游文件類型，不得宣稱已存在真實的 0074 或真實共用案件；示範交棒鍵僅可標為「建議、未驗證」。
8.3 什麼內容會使文件變成錯誤的證據項目（判別法）
若文件主要內容是稽核程序、稽核發現與稽核追蹤 → 屬 0072，不是本項。
若文件主要內容是完整結案報告、課程設計計畫或開課建議 → 屬 0074，不是本項。
若文件只有問卷分數、沒有講師／學員／人資／部門主管之多方差異與回饋分析 → 不滿足 080 要求（缺多方回饋與實質分析）。
若文件只有各方意見、沒有課後滿意度問卷與分佈統計 → 亦不滿足 080 要求（缺滿意度調查與分佈）。
本文件的正確證據項目應同時具備：課後滿意度問卷 + 分佈統計 + 多方（講師／學員／人資／部門主管）回饋 + 分析 + 結果或決策 + 跨文件事實連結。
8.4 跨文件事實連結（合成、未驗證）
本示範可提出一個建議、未驗證的交棒鍵：SYN-CROSSLINK-0073→0074（由本文件之課後回饋提案，交棒給 0074 之課程規劃）。此鍵為合成、未經證實，不得視為真實跨文件案件連結。
第 9 節　可重用表單與附錄
空白操作表單可留空，供真實使用時填寫；本文件之示範資料集（第 4、5 節）已完整填寫。
附錄 A　空白問卷（8 題）
課程名稱：＿＿＿＿＿＿＿＿＿＿　開課日期：＿＿＿＿＿＿　版本：＿＿＿＿
匿名代碼：＿＿＿＿　（1＝非常不滿意／非常不同意；2＝不滿意／不同意；3＝普通／無意見；4＝滿意／同意；5＝非常滿意／非常同意）
開放式意見：
1. 最有幫助的部分：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
2. 建議調整：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
3. 其他補充：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
附錄 B　回收與有效性登錄表
學習者回覆分數（第一段）
學習者回覆分數（第二段；以相同匿名代碼配對）
有效性判定
（示範填入值見第 4.1、4.2 節。）
附錄 C　學習者意見編碼表
（示範填入值見第 5.1 節。）
附錄 D　利害關係人回饋登錄表
（示範填入值見第 5.2 節。）
附錄 E　逐題分析表
分數次數表
彙總指標表
（示範填入值見第 4.3 節。）
附錄 F　決策與追蹤登錄表
（示範填入值見第 7 節。）
附錄 G　證據位置登錄（Evidence Locator）
附錄 H　評核人員檢查清單（Reviewer Checklist）
第 10 節　合成替換登錄（Replacement Register）使用說明
本示範之合成替換登錄為 synthetic_replacement_register_R01.csv，共 264 筆資料列；每筆欄位為：fact_id、case_id、data_type、synthetic_value、document_locator、real_replacement_source、status。
用途：真實使用時，須逐項以真實來源取代合成值；在取得真實來源之前，該筆狀態維持 SAMPLE/SYNTHETIC；REAL=UNKNOWN/HOLD。
涵蓋範圍（以 fact_id 分類）：
替換作業步驟：
1. 對照 fact_id，於 document_locator 指示之位置找到合成值。
2. 取得 real_replacement_source 所述之真實來源。
3. 以真實值取代，並將 status 由 SAMPLE/SYNTHETIC 更新為 REAL（附來源與日期）。
4. 重算所有比率與平均，確認與新資料一致；不得沿用舊合成數值。
5. 逐筆核對問卷矩陣、題項彙總、整體統計與 replacement register；若數值不一致，先標示 QA HOLD，修正後保留重算收據，不得以報告數字覆蓋原始來源。
提醒：替換過程中，所有真實值於取得並經驗證前，狀態一律維持 REAL=UNKNOWN/HOLD；不得以推測值、平均數或他人資料填補。

[TABLE 1]
類別 | 本文件內容 | 狀態
課程日期、發放／回收／有效份數 | 2026-08-15、16、16、15 | SAMPLE/SYNTHETIC
學習者分數 S01–S15、無效份 S16 | 全部為合成值 | SAMPLE/SYNTHETIC
學習者意見摘要、主題分類 | 合成摘要，非真人逐字紀錄 | SAMPLE/SYNTHETIC
講師／人資／部門主管回饋 | 合成回饋 | SAMPLE/SYNTHETIC
統計數字、平均、正向率 | 由合成資料計算 | SAMPLE/SYNTHETIC
改善提案與狀態 | 合成提案、未核准 | SAMPLE/SYNTHETIC
真實調查、辦訓、回饋、決議、核准、簽核 | 尚未取得 | REAL=UNKNOWN/HOLD

[TABLE 2]
項目 | 內容
文件編號 | 0073
要求編號 | I17A-E01
官方勾選序號 | 080（為勾選序號，不是文件編號）
指標 | 17（子項 17a 反應評估）
官方證據表版本 | 訓練機構版
官方證據表頁次 | 實體／列印頁 5（PDF page 5）
官方證據表 PDF SHA-256 | 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
勾選藍圖來源 | docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md（Git blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63）
藍圖第 080 列用語 | 「滿意度與各方回饋：問卷、分佈、講師學員意見及分析」
藍圖第 080 列要求 | 具體來源位置、實質內容／範例、結果或決策、跨文件事實連結

[TABLE 3]
等級 | 定義 | 本文件之關係
0 | 未執行 | —
1 | 執行滿意度調查 | 本文件示範版本包含問卷與統計，屬第 1 級所涵蓋之動作
2 | 將滿意度與學習者／講師回饋一併分析，並以分析結果作為修正下一期課程的依據 | 本文件示範版本包含多方回饋與「下一期課程建議」

[TABLE 4]
分數 | 錨點標籤（滿意／同意向）
1 | 非常不滿意／非常不同意
2 | 不滿意／不同意
3 | 普通／無意見
4 | 滿意／同意
5 | 非常滿意／非常同意

[TABLE 5]
題項 | 題目文字
Q1 | 課程內容與志工服務溝通及紀錄情境相關
Q2 | 課程目標清楚且知道完成後要能做什麼
Q3 | 教材順序與內容安排容易理解
Q4 | 講師說明、示範與回應問題有幫助
Q5 | 實作練習時間足以完成交接與紀錄步驟
Q6 | 教材與流程提示在課後容易查找使用
Q7 | 我有信心依步驟完成基本服務紀錄與交接
Q8 | 整體而言我對本次示範課程感到滿意

[TABLE 6]
欄位 | 說明
紀錄代碼（record_id） | 回饋紀錄唯一代碼（如 T01、H01、M01、M02）
群組（group） | 講師／人資／訓練行政／部門主管
人數（n） | 該群組此次提供回饋的人數（僅描述該群人數）
回饋內容（synthetic_feedback） | 回饋摘要；以中性敘述記錄，不指涉可辨識個人
分析（analysis） | 與問卷分數或其他回饋之關聯分析
建議回應（proposed_response） | 建議之後續動作（提案，非決策）
狀態（status） | 紀錄目前狀態（示範案件中均為「SAMPLE 提案，未核准」）
責任角色 | 建議之負責角色（非人名）
時機觸發 | 何時啟動（如「下一期開課前」）
追蹤措施 | 如何追蹤是否落實
限制說明 | 該筆回饋之證據限制

[TABLE 7]
學習者 | Q1 | Q2 | Q3 | Q4 | 主要主題
S01 | 3 | 5 | 5 | 5 | 保留示範
S02 | 4 | 4 | 4 | 4 | 增加練習
S03 | 4 | 4 | 5 | 3 | 加強欄位示範
S04 | 3 | 4 | 4 | 4 | 增加練習
S05 | 4 | 3 | 5 | 4 | 提供錯誤提醒
S06 | 4 | 4 | 4 | 3 | 分步示範
S07 | 5 | 5 | 5 | 4 | 保留案例
S08 | 4 | 5 | 5 | 4 | 增加角色案例
S09 | 4 | 4 | 4 | 3 | 增加練習
S10 | 5 | 5 | 5 | 4 | 分步示範
S11 | 4 | 3 | 4 | 4 | 提供流程卡
S12 | 3 | 4 | 3 | 3 | 分步示範
S13 | 4 | 5 | 5 | 5 | 錯誤案例
S14 | 5 | 4 | 4 | 5 | 增加問答
S15 | 5 | 3 | 5 | 2 | 保留案例

[TABLE 8]
學習者 | Q5 | Q6 | Q7 | Q8
S01 | 5 | 5 | 5 | 5
S02 | 4 | 4 | 4 | 4
S03 | 3 | 3 | 3 | 4
S04 | 4 | 4 | 4 | 4
S05 | 4 | 4 | 4 | 3
S06 | 3 | 3 | 4 | 4
S07 | 4 | 4 | 4 | 4
S08 | 4 | 4 | 4 | 4
S09 | 3 | 3 | 3 | 4
S10 | 5 | 4 | 4 | 5
S11 | 3 | 4 | 5 | 5
S12 | 3 | 3 | 3 | 3
S13 | 5 | 5 | 5 | 5
S14 | 2 | 5 | 4 | 4
S15 | 2 | 2 | 2 | 5

[TABLE 9]
學習者 | 已填答案 | 缺答題項 | 排除判定
S16 | Q1=5；Q2=4；Q3=4；Q5=5；Q8=4 | Q4、Q6、Q7 | 8 題中缺 3 題，整份排除，不插補

[TABLE 10]
題項 | 題目 | 1分 | 2分 | 3分 | 4分 | 5分
Q1 | 課程內容與志工服務溝通及紀錄情境相關 | 0 | 0 | 3 | 8 | 4
Q2 | 課程目標清楚且知道完成後要能做什麼 | 0 | 0 | 3 | 7 | 5
Q3 | 教材順序與內容安排容易理解 | 0 | 0 | 1 | 6 | 8
Q4 | 講師說明、示範與回應問題有幫助 | 0 | 1 | 4 | 7 | 3
Q5 | 實作練習時間足以完成交接與紀錄步驟 | 0 | 2 | 5 | 5 | 3
Q6 | 教材與流程提示在課後容易查找使用 | 0 | 1 | 4 | 7 | 3
Q7 | 我有信心依步驟完成基本服務紀錄與交接 | 0 | 1 | 3 | 8 | 3
Q8 | 整體而言我對本次示範課程感到滿意 | 0 | 0 | 2 | 8 | 5

[TABLE 11]
題項 | 總分 | 有效 n | 平均 | 正向 n | 正向率
Q1 | 61 | 15 | 4.07 | 12 | 80.00%
Q2 | 62 | 15 | 4.13 | 12 | 80.00%
Q3 | 67 | 15 | 4.47 | 14 | 93.33%
Q4 | 57 | 15 | 3.80 | 10 | 66.67%
Q5 | 54 | 15 | 3.60 | 8 | 53.33%
Q6 | 57 | 15 | 3.80 | 10 | 66.67%
Q7 | 58 | 15 | 3.87 | 11 | 73.33%
Q8 | 63 | 15 | 4.20 | 13 | 86.67%

[TABLE 12]
指標 | 計算 | 結果
有效題項回答數 | 15 × 8 | 120
全部題項總分 | 61+62+67+57+54+57+58+63 | 479
整體平均 | 479 ÷ 120 | 3.9917 → 3.99
整體正向回答數 | 12+12+14+10+8+10+11+13 | 90
整體正向率 | 90 ÷ 120 | 75.00%
回收率 | 16 ÷ 16 | 100.00%
有效／發放率 | 15 ÷ 16 | 93.75%
有效／回收率 | 15 ÷ 16 | 93.75%

[TABLE 13]
群體 | 有效 n | 併入學習者滿意度分母？
學習者 | 15 | 是
講師 | 1 | 否
人資／訓練行政 | 1 | 否
部門主管 | 2 | 否

[TABLE 14]
學習者 | 合成意見摘要 | 主要主題
S01 | 依角色順序演練交接較清楚，建議保留分步示範。 | 保留示範
S02 | 希望每個步驟後多留一點實際練習時間。 | 增加練習
S03 | 服務紀錄欄位可再示範一次，避免漏填。 | 加強欄位示範
S04 | 小組練習有幫助，希望增加一輪練習。 | 增加練習
S05 | 建議加一頁常見錯誤提醒卡。 | 提供錯誤提醒
S06 | 先示範再操作會更容易跟上。 | 分步示範
S07 | 交接情境容易理解，建議保留。 | 保留案例
S08 | 可以增加不同角色的情境案例。 | 增加角色案例
S09 | 練習時間偏短，想多做一次。 | 增加練習
S10 | 老師分步示範後比較能自行完成。 | 分步示範
S11 | 希望課後有一張簡短流程卡。 | 提供流程卡
S12 | 紀錄與交接的順序可以講慢一點。 | 分步示範
S13 | 建議加入一個錯誤示例供比較。 | 錯誤案例
S14 | 問答時間可以再多留幾分鐘。 | 增加問答
S15 | 案例有幫助，結尾複習清楚。 | 保留案例

[TABLE 15]
紀錄／群組／n | 回饋內容（合成摘要） | 分析 | 建議回應（提案） | 狀態
T01／講師／n=1 | 學員能跟上分步示範；練習時間偏短，容易跳過紀錄欄位的自我核對。 | 與Q5較低及學員增加練習主題方向一致；單一講師意見只作案例觀察。 | 示範後加入第二輪交接與欄位核對練習；不宣稱已採納。 | SAMPLE提案，未核准
H01／人資／訓練行政／n=1 | 彙整表應保留發放、回收、有效份數與排除理由；報告不要呈現可辨識個人的資料。 | 屬資料品質與隱私控制建議，不可併入學員滿意度分母。 | 每次調查以匿名代碼彙總；小群組只報實際n並加限制說明。 | SAMPLE提案，未核准
M01／部門主管／n=1 | 希望示範交接情境對應不同服務角色，減少只看單一例子的情形。 | 與學員提出增加角色案例相互呼應；僅為單一樣本回饋。 | 下一輪案例卡試列不同角色情境，待課程負責人確認適切性。 | SAMPLE提案，未核准
M02／部門主管／n=1 | 建議流程提示卡能列出交接前後需核對的欄位。 | 與學員要求流程卡及欄位示範一致；不得推論所有部門主管均有此意見。 | 先用合成案例試作提示卡，再由實際使用者核對。 | SAMPLE提案，未核准

[TABLE 16]
排序 | 題項 | 題目 | 平均 | 正向率 | 標記
1 | Q5 | 實作練習時間足以完成交接與紀錄步驟 | 3.60 | 53.33% | 低於示例門檻
2 | Q4 | 講師說明、示範與回應問題有幫助 | 3.80 | 66.67% | 低於示例門檻
2 | Q6 | 教材與流程提示在課後容易查找使用 | 3.80 | 66.67% | 低於示例門檻
4 | Q7 | 我有信心依步驟完成基本服務紀錄與交接 | 3.87 | 73.33% | 低於示例門檻
5 | Q1 | 課程內容與志工服務溝通及紀錄情境相關 | 4.07 | 80.00% | 達示例門檻
6 | Q2 | 課程目標清楚且知道完成後要能做什麼 | 4.13 | 80.00% | 達示例門檻
7 | Q8 | 整體而言我對本次示範課程感到滿意 | 4.20 | 86.67% | 達示例門檻
8 | Q3 | 教材順序與內容安排容易理解 | 4.47 | 93.33% | 高

[TABLE 17]
編號 | 發現 | 證據 | 建議調整（提案）
R-01 | 實作練習時間不足 | Q5 3.60／53.33%；T01；S02、S04、S09 | 示範後加入第二輪交接與欄位核對練習
R-02 | 課後查找與欄位提示不足 | Q6 3.80／66.67%；S05、S11；M02 | 編製流程提示卡，列出交接前後需核對欄位
R-03 | 分步示範有助理解、欄位示範可再加強 | S06、S10、S12；Q7 3.87／73.33% | 保留分步示範，並加強紀錄欄位示範
R-04 | 情境單一、角色覆蓋不足 | S08；M01 | 下一輪案例卡試列不同服務角色情境
R-05 | 資料品質與隱私控制 | H01 | 彙整表保留發放／回收／有效份數與排除理由；以匿名代碼彙總；小群組只報實際 n

[TABLE 18]
編號 | 負責角色 | 時機觸發 | 追蹤措施 | 暫緩／升級規則
R-01 | 課程負責人／講師 | 下一期開課前完成設計 | 下一期 Q5 分數與練習時數對照 | 若排課時數無法增加，升級由訓練行政協調
R-02 | 訓練行政（教材） | 下一期開課前完成草案 | 下一期 Q6 分數；使用者核對紀錄 | 若欄位定義不明，暫緩至講師與主管確認後再發布
R-03 | 講師 | 下一期開課時執行 | 下一期 Q4、Q7 分數 | 若時間衝突，優先保留欄位示範、精簡其他示例
R-04 | 課程負責人 | 下一期開課前 | 案例卡版本與 Q1／Q2 分數 | 若角色情境涉及敏感資訊，暫緩並改以通用案例
R-05 | 訓練行政／人資 | 每次調查常態執行 | 每份報告之來源位置與匿名檢核 | 若出現可辨識資訊，立即升級處理並重製彙整

[TABLE 19]
文件 | 要求 | 勾選序號 | 主題
0072 | I16-E03 | 078 | 內部／外部稽核程序與紀錄
0073（本文件） | I17A-E01 | 080 | 課後滿意度 + 多方利害關係人回饋分析
0074 | I17A-E02 | 081 | 課程結案報告、課程規劃、開課建議

[TABLE 20]
題項 | 題目 | 1 | 2 | 3 | 4 | 5
Q1 | 課程內容與志工服務溝通及紀錄情境相關 | ☐ | ☐ | ☐ | ☐ | ☐
Q2 | 課程目標清楚且知道完成後要能做什麼 | ☐ | ☐ | ☐ | ☐ | ☐
Q3 | 教材順序與內容安排容易理解 | ☐ | ☐ | ☐ | ☐ | ☐
Q4 | 講師說明、示範與回應問題有幫助 | ☐ | ☐ | ☐ | ☐ | ☐
Q5 | 實作練習時間足以完成交接與紀錄步驟 | ☐ | ☐ | ☐ | ☐ | ☐
Q6 | 教材與流程提示在課後容易查找使用 | ☐ | ☐ | ☐ | ☐ | ☐
Q7 | 我有信心依步驟完成基本服務紀錄與交接 | ☐ | ☐ | ☐ | ☐ | ☐
Q8 | 整體而言我對本次示範課程感到滿意 | ☐ | ☐ | ☐ | ☐ | ☐

[TABLE 21]
匿名代碼 | Q1 | Q2 | Q3 | Q4

[TABLE 22]
匿名代碼 | Q5 | Q6 | Q7 | Q8

[TABLE 23]
匿名代碼 | 狀態（VALID／EXCLUDED） | 缺答題項 | 排除原因／覆核

[TABLE 24]
學習者代碼 | 意見摘要 | 主要主題 | 次主題備註 | 來源狀態 | 位置
 |  |  |  | SAMPLE/SYNTHETIC | 依 respondent_id

[TABLE 25]
紀錄／群組／n | 回饋內容及來源 | 分析 | 建議回應及狀態 | 責任角色／時機／追蹤／限制
 |  |  | 提案（未核准） | 

[TABLE 26]
題項 | 1分 | 2分 | 3分 | 4分 | 5分
Q1 |  |  |  |  | 
Q2 |  |  |  |  | 
Q3 |  |  |  |  | 
Q4 |  |  |  |  | 
Q5 |  |  |  |  | 
Q6 |  |  |  |  | 
Q7 |  |  |  |  | 
Q8 |  |  |  |  | 

[TABLE 27]
題項 | 總分 | 有效 n | 平均 | 正向 n | 正向率
Q1 |  |  |  |  | 
Q2 |  |  |  |  | 
Q3 |  |  |  |  | 
Q4 |  |  |  |  | 
Q5 |  |  |  |  | 
Q6 |  |  |  |  | 
Q7 |  |  |  |  | 
Q8 |  |  |  |  | 

[TABLE 28]
建議編號 | 發現 | 負責角色 | 時機觸發 | 追蹤措施 | 狀態 | 升級條件
 |  |  |  |  | 提案（未核准） | 

[TABLE 29]
證據 | 位置 | 狀態
官方要求原文 | 訓練機構版證據表，實體頁 5（PDF page 5）；SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709 | 官方
勾選藍圖第 080 列 | docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md（blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63） | 官方來源
學習者分數 | 附錄 B（依 respondent_id／Qn） | SAMPLE/SYNTHETIC
學習者意見 | 附錄 C（依 respondent_id） | SAMPLE/SYNTHETIC
利害關係人回饋 | 第 5.2 節／record_id（T01、H01、M01、M02） | SAMPLE/SYNTHETIC
統計結果 | 第 4.3 節（逐題）與第 4.4 節（整體） | SAMPLE/SYNTHETIC
真實問卷／回饋／決議原件 | 尚未取得 | REAL=UNKNOWN/HOLD

[TABLE 30]
檢核項 | 是 | 否 | 備註
文件 ID（0073）／要求（I17A-E01）／勾選序號（080）是否正確標示 | ☐ | ☐ | 
官方要求原文是否照錄、是否標明 PDF 頁 5 | ☐ | ☐ | 
是否說明 17a 等級 0／1／2 且未宣稱已達等級 | ☐ | ☐ | 
問卷是否含 8 題與 5 個錨點標籤 | ☐ | ☐ | 
15 筆有效分數是否完整、S16 是否列為無效並附理由 | ☐ | ☐ | 
逐題頻率、總分、有效 n、平均、正向率是否可重算 | ☐ | ☐ | 
整體（120、479、3.99、75.00%、回收／有效率）是否可重算 | ☐ | ☐ | 
講師／人資／部門主管回饋是否各具紀錄且分母分離 | ☐ | ☐ | 
是否標示低分項、示例門檻（非官方）與證據限制 | ☐ | ☐ | 
建議是否皆標為合成提案（非本會決策） | ☐ | ☐ | 
是否與 0072／0074 明確區別、未捏造 0074 或真實案件 | ☐ | ☐ | 
全篇是否維持 SAMPLE/SYNTHETIC 與 REAL=UNKNOWN/HOLD | ☐ | ☐ | 

[TABLE 31]
資料類型 | 內容 | 文件位置 | 真實替換來源（示例）
問卷評分 | 每位學習者 Q1–Q8 分數（15×8 筆） | 附錄 B；respondent_id／Qn | 去識別化原始問卷及有效性覆核
匿名學員意見摘要 | 15 筆合成意見 | 附錄 C；respondent_id | 實際去識別化開放題回覆及編碼覆核
主題分類 | 15 筆主題 | 附錄 C；respondent_id | 實際編碼表與覆核紀錄
無效回覆內容 | S16 已填值與缺答狀態 | 附錄 B；S16／Qn；排除於統計之外 | 原始去識別問卷與排除判定覆核
無效回覆排除原因 | S16 排除理由 | 附錄 B；S16 | 原始問卷與完整性規則覆核
利害關係人回饋 | T01／H01／M01／M02 各欄 | 第 5.2 節／record_id | 實際講師／人資／部門主管回饋原件與授權存取紀錄
彙總統計 | 發放／回收／有效／無效、總分、平均、正向率 | 第 4.4 節 | 實際簽到／發放回收台帳／有效性覆核／原始問卷重算
題項統計 | 各題平均、正向率、總分、各分數計次 | 第 4.3 節／item_id | 實際有效問卷逐筆重算，不得沿用示範數值
合成改善提案 | 第二輪練習、分步示範欄位、匿名化與小樣本限制、角色情境卡、提示卡試作 | 第 7 節 | 實際會議紀錄、核准者決議與後續執行紀錄；未取得前維持提案
