# Semantic review packet: 0112 / I18-E21 / candidate R04

Candidate SHA-256: `9944db848d4554e56fe7e11092e6e7d059c880e1c927783c1a772ffaa85dc6e5`; bytes=50391. Numbered official checkbox: UNKNOWN (not asserted by source packet).
Source packet SHA-256: `5bcafc54c03ed636d8aa5fb6ce4d260360a02a59d25078f227138292c820c266`. Unique Blueprint SHA-256: `d6b23672850b8b69098320025d51d6b88a1bbe64692696e0d6f3e295bbb93a0d`. Synthetic dataset SHA-256: `1a116070afc94a6211f1e57ba5433c231389ab337d14b8ba020e2239380725d5`; rows=54. Replacement register SHA-256: `91ff9e9a07293aa77dfaf2afece6edfbe9e4dd21c83c3b8d08df557283295552`. Technical QA SHA-256: `701499851c911c14b2d345ebb8ec7a0dadb65b34fd14b2403a99ef8c262f258d`. Visual QA SHA-256: `c1a25b876228bdd973993a3350112abdb8f97fcea97e3cf8e79cabf491c9b04c`.

## Official source packet
# SOURCE_PACKET_0112_I18-E21_R01

**State:** SOURCE_PREPARED / CANDIDATE. This packet asserts no real association result, printed checkbox serial, or formal acceptance.

## Binding

- Project: TTQS_ONE.
- Document ID: 0112.
- Official requirement ID in the current 129-to-142 crosswalk: I18-E21.
- Crosswalk deliverable title: 輔導考照及學員回訓率追蹤分析表.
- Official printed checkbox serial: UNKNOWN_NOT_ASSERTED. The two intermediate CSV fields are not a printed serial.
- Source snapshot: PR #92 branch work/ttqs-one-document-quality-contract-20261016 at commit 5916ea3896c1d8caec4d3e8c8eae9a00ea0bf9ed.

## Authoritative source evidence

1. 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》, page 7, indicator 18, four-point evidence examples:
   - Exact wording: 「輔導考照及學員回訓率持續提高。」
   - Source path: docs/ttqs-quality-20261016/quality-review/0037_R07/inputs/official_source.pdf
   - Current PDF SHA-256: 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
   - Git blob SHA-1: 9c7621decdad585b743bf2b3d949ee5518b7bee0
2. Current crosswalk:
   - Path: docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv
   - Raw SHA-256: 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679
   - Git blob SHA-1: 1ac4a8419088d947947031b758e29c35a3606514
   - Exact row: I18-E21,1,0,0112,輔導考照及學員回訓率追蹤分析表
   - This row binds doc_id and title; it does not prove the printed checkbox serial.
3. 157-checkbox Blueprint contract:
   - Path: docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md
   - Raw SHA-256: ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216
   - Git blob SHA-1: 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63
   - A targeted check found no I18-E21 or 0112-specific entry in this contract. The unique Blueprint below is newly prepared for this document.

## Scope and evidence boundary

- The official example requires both certification-coaching outcomes and learner retraining rate to increase. Keep these as separate measures, with comparable periods, explicit eligibility, denominators, source references, and trend calculations.
- The official wording does not prescribe a universal numerator, denominator, follow-up window, target, retention period, or causal test. Any proposed operational definitions and targets in a sample must be marked SAMPLE/SYNTHETIC and must not be represented as an association-approved policy.
- No authorized real learner roster, coaching record, certificate result, retraining log, or approval was found in the inspected source packet. REAL evidence status is UNKNOWN/HOLD.
- Do not publish personal identifiers, certificate images, signatures, member data, or protected originals. Keep any real source in its authorized system and record only permitted reference IDs in a future register.
- Adjacent-document separation:
  - 0104 / I18-E11 concerns certificate acquisition-rate analysis; it is not automatically the same coaching cohort or denominator.
  - 0110 / I18-E19 collects learner/client perceptions and after-course action plans; survey answers do not prove credentials or completed retraining.
  - 0111 / I18-E20 concerns special/social outcomes; it is not a substitute for either I18-E21 measure.
- No 0112 candidate or source-preparation directory was present locally or in the PR tree before this stage.

## Ready-to-build prerequisites

Before a DOCX build, the worked example must include separate cohort data for coaching/certification and retraining, every numerator and denominator, a Python-recomputed trend table, missing/duplicate/withdrawal rules, a fact-level SAMPLE register, an explicit hold/reject path, and visible SAMPLE/SYNTHETIC notices. Do not build from a title-only outline.

## Unique Blueprint
# UNIQUE_BLUEPRINT_0112_I18-E21_R01

## Exact binding and purpose

- Project: TTQS_ONE.
- Document ID: 0112.
- Official requirement ID: I18-E21.
- Official printed checkbox serial: UNKNOWN_NOT_ASSERTED.
- Crosswalk title: 輔導考照及學員回訓率追蹤分析表.
- Official source: current official PDF, page 7, indicator 18, four-point example: 「輔導考照及學員回訓率持續提高。」
- Unique purpose: a practical cohort tracker and trend-analysis tool showing separately whether documented certification coaching and learner retraining increase over comparable periods, with traceable evidence and follow-up actions.
- This is not the 0104 certificate acquisition report, 0110 perception survey, or 0111 special/social outcome register.

## Intended user and association fit

A small volunteer association training administrator can maintain this tool with role codes and a simple paper or spreadsheet register. Suggested roles are 行政承辦、課程聯絡人、覆核者; these are recommendations, not evidence of appointment or legal authority. Do not assume an HR department, employed learners, a standing committee, or a particular certification body.

## Required document anatomy

1. Cover and quick-use panel: purpose, user role, update timing, reporting window, output, SAMPLE/REAL status, and stop conditions.
2. Definitions and eligibility: distinguish coaching offered, coaching received, exam eligibility, retraining eligibility, invitation, exam attempt, verified credential, completed retraining, and matured follow-up window.
3. Cohort register: cohort ID, coded learner ID, eligibility reason, coaching date/type, exam plan/window, retraining eligibility/due window, consent/privacy state, source locator, status, and follow-up owner role. No names or identity numbers in the public sample.
4. Certification coaching follow-up: eligible learners, coaching received, exam attempted, verified credential earned in the stated window, pending proof, withdrawal, and ineligible cases.
5. Retraining follow-up: eligible learners, invited, completed within the stated window, not completed, declined, unreachable, withdrawn, and missing evidence. Invitations never count as completion.
6. Separate trend analysis: show cohort size, numerator, denominator, rate, percentage-point change, comparable-period decision, and missing-data count for each measure. Do not pool measures or double-count a learner within one cohort.
7. Completed SAMPLE case: use only SYN-0112-CASE-01 and synthetic period codes SYN-P1, SYN-P2, SYN-P3. Invented data must be conspicuously labeled SAMPLE/SYNTHETIC and must not claim association outcomes.
8. Action and review log: each gap links to an action, responsible role code, due date, evidence to collect, follow-up date, status, and disposition CONTINUE / REVISE / HOLD / CLOSE. A rising rate does not clear missing-evidence cases.
9. Coding and calculation rules: define duplicate, ineligible, pending, not-yet-due, withdrawn, missing proof, declined, and zero-denominator handling. Do not silently remove unfavourable cases.
10. Evidence and privacy controls: evidence reference, source type, date/window, custodian role, consent/legal-basis state, permitted summary use, verification status, retention-policy reference, and redaction state. Unknown policy or permission means HOLD.
11. Requirement traceability and replacement register: official clause → field/metric → source reference → calculation → conclusion → follow-up action; fact-level register marks every sample datum and replacement instructions.
12. Real-data replacement and version control: replace sample values only with authorized source records, recompute, preserve prior hashes, and keep protected originals out of public repositories unless explicitly authorized.

## Operational definitions for the sample tool

The official source does not define denominators. These proposed definitions are for demonstration and require association approval before REAL use:

- Certification coaching completion rate = eligible coached learners with a verified credential earned within the stated window / all eligible coached learners whose exam follow-up window matured × 100.
- Retraining completion rate = eligible learners with verified completed retraining within the stated window / all retraining-eligible learners whose retraining window matured × 100.
- Report invitations, attempts, pending results, withdrawals, not-yet-matured windows, and missing proof separately. Do not convert self-report to verified completion.

## Complete illustrative data and calculations

SAMPLE/SYNTHETIC ONLY, case SYN-0112-CASE-01:

| Period | Certification numerator/denominator | Rate | Retraining numerator/denominator | Rate |
|---|---:|---:|---:|---:|
| SYN-P1 | 3/8 | 37.5% | 4/10 | 40.0% |
| SYN-P2 | 4/8 | 50.0% | 6/10 | 60.0% |
| SYN-P3 | 5/8 | 62.5% | 7/10 | 70.0% |

- Certification change: P1→P2 +12.5 percentage points; P2→P3 +12.5 points; P1→P3 +25.0 points.
- Retraining change: P1→P2 +20.0 points; P2→P3 +10.0 points; P1→P3 +30.0 points.
- These are separate descriptive sample trends. They do not establish REAL performance, statistical significance, or causality. Period comparability and matured windows must be shown before interpreting a trend.

## Mandatory reject / hold conditions

- HOLD if the cohort or eligibility rule, follow-up maturity, numerator, denominator, source, consent/privacy basis, or custodian is missing or inconsistent.
- HOLD if credential or retraining completion is self-reported without the required authorized verification.
- HOLD a window that has not matured; do not code it as a success or failure.
- Reject duplicates, duplicate credentials, unapproved reclassification, mixed cohort definitions, invitation-count denominators, untracked withdrawals/unreachable cases, or unsupported improvement claims.
- HOLD if an actual target or retention policy lacks authorization; never invent association thresholds or retention periods.
- SAMPLE_ONLY when all values are synthetic; never silently promote them to REAL.

## Nearest-document distinction

- 0104 / I18-E11: certificate acquisition-rate analysis. 0112 follows the coached cohort and retraining lineage; do not copy its denominator or treat the outcomes as interchangeable.
- 0110 / I18-E19: perception questionnaires and an after-course action plan. Perceptions do not verify credentials or retraining completion.
- 0111 / I18-E20: special/social performance register. Do not substitute its claims for certification or retraining measures.

## Build and review entry gate

A DOCX candidate is ready only after a fact-level synthetic dataset and independent Python recomputation prove every row, denominator, rate, percentage-point change, and disposition; all forms are usable; the replacement register is complete; and every sample fact is visibly labeled. Independent review must bind the final exact DOCX SHA and cover official mapping, genre, usability, math, adjacent-document separation, SAMPLE/REAL boundary, and rendered pages. Technical success alone is not acceptance.

## Independently recomputed synthetic cohort summary
| Period | Measure | Eligible | Coached/invited | Verified earned/completed | Matured |
|---|---|---:|---:|---:|---:|
| SYN-P1 | CERTIFICATION_AFTER_COACHING | 8 | 8 | 3 | 8 |
| SYN-P1 | RETRAINING_COMPLETION | 10 | 10 | 4 | 10 |
| SYN-P2 | CERTIFICATION_AFTER_COACHING | 8 | 8 | 4 | 8 |
| SYN-P2 | RETRAINING_COMPLETION | 10 | 10 | 6 | 10 |
| SYN-P3 | CERTIFICATION_AFTER_COACHING | 8 | 8 | 5 | 8 |
| SYN-P3 | RETRAINING_COMPLETION | 10 | 10 | 7 | 10 |

## Synthetic replacement register
fact_id,period,measure,synthetic_values,replacement_source_needed,real_state
SYN-0112-F001,SYN-P1,CERTIFICATION_AFTER_COACHING,verified credential 3/8; exam attempted 7/8,authorized cohort eligibility and coaching records plus independently verifiable credential outcome,UNKNOWN_HOLD
SYN-0112-F002,SYN-P1,RETRAINING_COMPLETION,verified completed retraining 4/10; all 10 eligible and invited,"authorized learner eligibility, invitation/completion records, and independently verifiable retraining source",UNKNOWN_HOLD
SYN-0112-F003,SYN-P2,CERTIFICATION_AFTER_COACHING,verified credential 4/8; exam attempted 7/8,authorized cohort eligibility and coaching records plus independently verifiable credential outcome,UNKNOWN_HOLD
SYN-0112-F004,SYN-P2,RETRAINING_COMPLETION,verified completed retraining 6/10; all 10 eligible and invited,"authorized learner eligibility, invitation/completion records, and independently verifiable retraining source",UNKNOWN_HOLD
SYN-0112-F005,SYN-P3,CERTIFICATION_AFTER_COACHING,verified credential 5/8; exam attempted 7/8,authorized cohort eligibility and coaching records plus independently verifiable credential outcome,UNKNOWN_HOLD
SYN-0112-F006,SYN-P3,RETRAINING_COMPLETION,verified completed retraining 7/10; all 10 eligible and invited,"authorized learner eligibility, invitation/completion records, and independently verifiable retraining source",UNKNOWN_HOLD

## QA scope summaries
DOCX SHA `9944DB848D4554E56FE7E11092E6E7D059C880E1C927783C1A772FFAA85DC6E5`; zip integrity PASS; 17 tables; body/table font floors 10.5/9.5pt; failed checks []; formal acceptance NOT_GRANTED.
DOCX SHA `9944DB848D4554E56FE7E11092E6E7D059C880E1C927783C1A772FFAA85DC6E5`; 8 Word-native pages; all_pages_inspected=True; clipping/overlap=none observed; result=PASS_LAYOUT_SCOPE_ONLY; layout-only, not semantic.
## Full DOCX text with paragraph/table locators
[P001] 輔導考照及學員回訓率追蹤分析表
[P002] 供訓練行政人員分別追蹤考照輔導與學員回訓，並以一致口徑檢視各期變化
[P005] 1　30 秒使用指引
[P006] 本表把兩種不同的後續結果分開追蹤：受輔導且具考照資格者的證照結果，以及具回訓資格者的回訓完成情形。每個追蹤期各自留名冊、核對來源、計算分子與分母，再記錄待處理缺口。不得將兩種比率合併成一個總分。
[P009] 2　官方要求、用途及範圍界線
[P010] 官方資料在訓練機構版第 7 頁、指標 18 的四分範例列出「輔導考照及學員回訓率持續提高。」本表據此設計兩條獨立追蹤線，呈現可核對的資格、證據、分母、分子、各期比率與後續處理。官方文字沒有指定統一分母、觀察窗口、目標值、保存期間或因果分析方法。
[P012] 2.1　關鍵定義
[P014] 3　分開計算與判讀
[P015] 3.1　輔導考照追蹤率
[P016] 建議公式：輔導考照追蹤率 = 窗口成熟且查證於窗口內取得證照的受輔導合格人數 ÷ 窗口成熟且符合考照資格的受輔導人數 × 100%。正式分母及窗口需依實際授權程序核定。
[P017] 分母按人數計，不按輔導次數或考試次數計。同一個人在同一群組、期間、指標下只計一次。
[P018] 符合資格且窗口成熟但尚未取得可驗證證照者，依本建議口徑留在分母、不得計入分子；若資格或窗口資料缺失，先 HOLD。
[P019] 只在有授權的來源驗證結果；來源位置保持私有，只記允許公開的來源代碼或定位。
[P020] 3.2　學員回訓完成率
[P021] 建議公式：學員回訓完成率 = 窗口成熟且查證完成回訓的人數 ÷ 窗口成熟且符合回訓資格的人數 × 100%。邀請、送達或報名不等於完成回訓。
[P022] 具回訓資格、窗口成熟但未完成者，不得從分母中默默剔除；依經核定口徑處理並保留狀態。
[P023] 窗口未成熟、資格不明或完成證據未能查驗，依下表標示 PENDING/HOLD，不把未知轉成成功或失敗。
[P024] 考照率與回訓率分別呈現；不相加、不加權，也不彼此替代。
[P025] 4　逐人追蹤名冊與資料保護表單
[P026] 每項指標、每一期間均以逐人一列方式建立工作名冊。下列空白欄位是供授權取得真實資料後使用的表單；下方兩筆已填示範可供承辦人對照。示範值均為合成資料，不是實際學員或佐證。
[P027] 4.1　名冊輸入欄位
[P029] 4.2　已填樣本列
[P032] 5　合成案例與可重算趨勢
[P033] 案例 SYN-0112-CASE-01 使用 SYN-P1、SYN-P2、SYN-P3 三個合成期間。兩項指標各自有分母、分子及事實代碼；期間標籤不是日曆日期。比率以分子÷分母×100 計算，期差以後一期比率減前一期比率計算，單位為百分點（pp）。
[P034] 5.1　輔導考照
[P036] 樣本描述：三個合成期間的考照追蹤率逐期上升；這只描述輸入資料，不能證明實際協會的考照輔導成效，也不說明上升原因。
[P037] 5.2　學員回訓
[P039] 樣本描述：三個合成期間的回訓完成率逐期上升；不與考照率合併，不解讀為因果效果。
[P041] 6　資料品質與 HOLD / REJECT 規則
[P042] 下列分類是供內部核定的建議控制方式。若組織尚未確認資格、窗口或資料授權，先暫停受影響個案，不用推測填補。
[P044] 7　改善行動與覆核紀錄
[P045] 下表五筆是供演練流程的 SAMPLE/SYNTHETIC 情境代碼，不是原始點協會曾發生的事件。DUE 與 NEXT_FOLLOW_UP 未有授權期程時填 UNKNOWN/HOLD。角色碼只是建議職能，不代表已任命的人員。
[P047] 7.1　空白真實行動記錄欄位
[P048] 每筆 REAL 缺口至少填：case_id、缺口類型、原始證據私有定位、採用處置、預期證據、負責角色代碼、授權 DUE、下次追蹤日、目前狀態、複核者代碼、結案依據與更正版本。欄位未知時填 UNKNOWN/HOLD 並記錄待補來源；不得留下沒有原因的空白，也不得虛構簽名或完成紀錄。
[P049] 8　合成事實替換清冊
[P050] 所有代碼均為本文件 SAMPLE/SYNTHETIC。替換成真實資料時須逐項取自獲授權來源、重新核算、保留私有來源定位與變更版本；合成值不能複製成 REAL。
[P052] 9　相關文件的用途區隔
[P054] 10　投入真實作業前的核對步驟
[P055] 確認官方表單版本與對應欄位；印刷勾選序號目前 UNKNOWN，不以內部索引或 crosswalk 欄位代替。
[P056] 由實際授權程序確認分母、資格、觀察窗口、目標（如需）、保存與隱私規則；未確認前資料維持 HOLD。
[P057] 取得授權來源後，以去識別碼建立逐人名冊，逐筆記錄資格、來源定位、查驗狀態、窗口成熟與覆核角色。
[P058] 以同一口徑分別重算兩項比率及百分點差，核對重複、缺漏、零分母、未成熟窗口及退出個案。
[P059] 只對允許公開的摘要進行外部呈現；簽章、原件與個資留在有權限的來源，不在本候選文件中偽造或替代。
[P060] 保存來源版本、計算結果、差異、修訂理由及審查記錄；只有真實來源和正式授權完成後，才可申請由 SAMPLE 轉 REAL。

[TABLE 01; rows=1; cols=1]
[T01R001] SAMPLE / SYNTHETIC ONLY　下列期間、代碼、分子分母、示範情境皆為合成資料，不代表原始點協會實際學員、成效、核准或處置。

[TABLE 02; rows=7; cols=2]
[T02R001] 文件識別 | 本文件資訊
[T02R002] 文件編號 / doc_id | 0112
[T02R003] 官方需求對應 | I18-E21（依專案 crosswalk；不同於 157 方框流水號）
[T02R004] 官方佐證目的 | 指標18四分範例：「輔導考照及學員回訓率持續提高。」
[T02R005] 官方檢核表印刷序號 | UNKNOWN_NOT_ASSERTED；請依使用時有效的官方表單查對
[T02R006] 文件狀態 | CANDIDATE；SAMPLE/SYNTHETIC only；REAL 證據與正式接受均未建立
[T02R007] 尚未取得的組織規則 | 授權程序/核定權責人、追蹤窗口、目標、保存期限均 UNKNOWN；未確認前不得當成既定制度

[TABLE 03; rows=6; cols=3]
[T03R001] 順序 | 承辦人要做的事 | 可繼續計算的條件；否則如何處理
[T03R002] 1　界定 | 記錄同一報告期、群組、資格理由與窗口定義。 | 資格、期間或窗口未經授權確認：HOLD，不要自行補日期或排除個案。
[T03R003] 2　逐人登錄 | 每位學員每項指標、每期一列；使用去識別代碼。 | 姓名、身分證、證書影像留在獲授權的原始系統，不放入公開表。
[T03R004] 3　核對證據 | 記錄來源種類、私有定位、查證狀態、保管角色與遮罩狀態。 | 只有口頭自述或無可驗證來源：不能列入成功分子；若資格/窗口也不明，整案 HOLD。
[T03R005] 4　分開計算 | 成熟期滿且符合建議納入條件後，分別計算考照率及回訓率。 | 每個期間採同一資格及分母規則；零分母寫 N/A，說明原因。
[T03R006] 5　判讀與追蹤 | 比較各期百分點變化，將缺口連到行動紀錄。 | 期別不具可比性、資料缺漏或驗證未完成：限制結論或 HOLD；不推論因果。

[TABLE 04; rows=1; cols=1]
[T04R001] 以下計算口徑是供討論與演練的建議方案，不是官方強制規定，也不代表協會已核准。REAL 使用前需依實際授權程序確認；核定權責與期限目前 UNKNOWN。

[TABLE 05; rows=4; cols=3]
[T05R001] 工作項目 | 本表採用的建議口徑 | 未確認時的安全處理
[T05R002] 考照輔導 | 追蹤確有受輔導且具考照資格的個案；成功分子需有可授權查驗的證照結果。 | 輔導事實、資格、窗口或來源不明：HOLD，不把自述當成查證成功。
[T05R003] 學員回訓 | 追蹤具回訓資格個案；只有查證完成回訓者列入成功分子。 | 邀請或報名不等於完成；資格、完成紀錄、窗口不明：HOLD。
[T05R004] 報告判讀 | 只在期間口徑和群組可比時描述增加或減少的百分點。 | 不宣稱統計顯著，不推論輔導造成結果，不把樣本數字說成協會績效。

[TABLE 06; rows=7; cols=2]
[T06R001] 名詞 | 作業定義；實際口徑需經授權確認
[T06R002] 受輔導 | 有可追溯的輔導事實；提供資源與實際接受輔導分開記錄。
[T06R003] 考照資格 | 依考照資格來源或已核定規則判定；資格理由及來源定位須留痕。
[T06R004] 回訓資格 | 依可查證的前期資格或已核定規則判定；不能只因收到邀請而推定符合。
[T06R005] 窗口成熟 | 已達經授權設定的觀察截止點。窗口尚未定義或尚未到期，不列入本期計算，標註 WINDOW=UNKNOWN/HOLD 或 PENDING。
[T06R006] 查證成功 | 取得允許使用且可核對的來源，並完成覆核；未查證的口頭聲稱不得計入分子。
[T06R007] 同一個案 | 以去識別學員碼、指標、群組與期間組合檢查重複；更正需保留原值與原因。

[TABLE 07; rows=7; cols=3]
[T07R001] 欄位群 | 逐人必填欄位 | 填寫與保密規則
[T07R002] 識別與資格 | case_id、cohort/period、去識別 learner_code、measure、eligibility 狀態、eligibility_reason_ref。 | 同一人以穩定的去識別代碼比對；姓名與身份資料不放本表。資格來源缺失即 HOLD。
[T07R003] 考照輔導 | coaching_received、coaching_type、coaching_date、exam_eligible、exam_attempted、exam_outcome。 | 只記來源支持的事實；不存在或未知日期填 UNKNOWN，不推測。
[T07R004] 回訓追蹤 | retraining_eligible、retraining_due_window、invited/delivery、completed 狀態及完成來源。 | 邀請狀態和完成狀態分欄；窗口未核定或未成熟不得結算。
[T07R005] 窗口與佐證 | window_start/end 或核定規則代碼、maturity_status、evidence_type、private_source_locator、verification_status。 | 原始文件、證書、出勤表存於授權系統；本表只保留可用的私有定位代碼。
[T07R006] 隱私與責任 | consent/other_authority_state、custodian_role、permitted_summary、redaction_state、retention_policy_ref。 | 權限、保管者、公開範圍或保存政策未知：HOLD；角色代碼僅為建議分工，不代表實際任命。
[T07R007] 追蹤與版控 | source_checked_date、next_action、due_date、follow_up_date、owner_role、status、disposition、revision_note。 | 日期及負責人依實際授權程序填寫；未知期限標 UNKNOWN/HOLD；更正保留理由與版本。

[TABLE 08; rows=8; cols=3]
[T08R001] 欄位 | SAMPLE 考照列 | SAMPLE 回訓列
[T08R002] 案件 / 期別 / 學員碼 | SYN-0112-CASE-01 / SYN-P1 / SYN-L-1-01 | SYN-0112-CASE-01 / SYN-P1 / SYN-R-1-01
[T08R003] 指標 / 合格狀態 | CERTIFICATION_AFTER_COACHING / ELIGIBLE=YES | RETRAINING_COMPLETION / RETRAINING_ELIGIBLE=YES
[T08R004] 過程狀態 | COACHING_RECEIVED=YES; EXAM_ATTEMPTED=YES | RETRAINING_INVITED=YES; RETRAINING_COMPLETED=YES
[T08R005] 窗口 / 結果 | WINDOW_MATURED=YES; VERIFIED_CREDENTIAL=YES | WINDOW_MATURED=YES; VERIFIED_COMPLETION=YES
[T08R006] 事實代碼 / 來源 | SYN-0112-F001; SAMPLE_SYNTHETIC_ONLY | SYN-0112-F002; SAMPLE_SYNTHETIC_ONLY
[T08R007] 同意、保管、公開與遮罩 | REAL 欄位不適用於合成資料；真實個資授權 UNKNOWN/HOLD；ROLE-ADMIN 僅為示範角色碼；不得公開真實來源定位。 | REAL 欄位不適用於合成資料；真實個資授權 UNKNOWN/HOLD；ROLE-ADMIN 僅為示範角色碼；不得公開真實來源定位。
[T08R008] 日期 / 後續 | 合成列未提供日期；REAL 日期=UNKNOWN；無真實行動紀錄。 | 合成列未提供日期；REAL 日期=UNKNOWN；無真實行動紀錄。

[TABLE 09; rows=1; cols=1]
[T09R001] 合成列中的 VERIFIED 只表示示範資料欄位設定為 YES；不是任何真實證照、出勤紀錄或第三方原件已經過本協會查驗。

[TABLE 10; rows=4; cols=6]
[T10R001] 期間 | 成功 / 分母 | 計算率 | 較前期 | 較基期 | 事實代碼
[T10R002] SYN-P1 | 3 / 8 | 3÷8×100=37.5% | 基期 | 基期 | SYN-0112-F001
[T10R003] SYN-P2 | 4 / 8 | 4÷8×100=50.0% | 50.0−37.5=+12.5 pp | +12.5 pp | SYN-0112-F003
[T10R004] SYN-P3 | 5 / 8 | 5÷8×100=62.5% | 62.5−50.0=+12.5 pp | 62.5−37.5=+25.0 pp | SYN-0112-F005

[TABLE 11; rows=4; cols=6]
[T11R001] 期間 | 完成 / 分母 | 計算率 | 較前期 | 較基期 | 事實代碼
[T11R002] SYN-P1 | 4 / 10 | 4÷10×100=40.0% | 基期 | 基期 | SYN-0112-F002
[T11R003] SYN-P2 | 6 / 10 | 6÷10×100=60.0% | 60.0−40.0=+20.0 pp | +20.0 pp | SYN-0112-F004
[T11R004] SYN-P3 | 7 / 10 | 7÷10×100=70.0% | 70.0−60.0=+10.0 pp | 70.0−40.0=+30.0 pp | SYN-0112-F006

[TABLE 12; rows=1; cols=1]
[T12R001] 數值稽核：考照率為 37.5%、50.0%、62.5%；差值為 +12.5、+12.5、+25.0 pp。回訓率為 40.0%、60.0%、70.0%；差值為 +20.0、+10.0、+30.0 pp。統計顯著性未評估；不支持因果結論。

[TABLE 13; rows=11; cols=3]
[T13R001] 情況 | 計算處置 | 記錄與解除條件
[T13R002] 資格符合且窗口成熟；成功來源已查證 | 按核定口徑進入分母；查證完成者才可能進分子。 | 記錄 source type、私有 locator、查驗狀態、查驗日期與覆核角色。
[T13R003] 資格或資格理由缺失 | HOLD；未釐清前不列入本期分子或分母。 | 取得授權資格來源、補完整理紀錄，保留原登錄與更正理由。
[T13R004] 窗口未定義或尚未成熟 | HOLD / PENDING；不作當期成功或失敗判定。 | 只有實際授權規則與截止狀態可解除；不得自行創造期限。
[T13R005] 合格成熟但未成功 / 未完成 | 依經授權分母口徑留存；成功分子為 0。 | 記錄為未完成、未嘗試或明確失敗；不刪除不利個案。
[T13R006] 只有口頭自述、來源不存在或未授權 | 不得計入成功分子；資格與窗口已確定時保留相應分母，其他情況 HOLD。 | 由有權覆核者查驗允許的原始來源；逾期規則須先經授權確認。
[T13R007] 同一人重複紀錄 | 同一指標、群組、期間只採一個有效結果；修正時留痕。 | 先查明重複原因，不以刪除不利結果方式改變比率。
[T13R008] 拒絕、失聯或退出 | 是否列分母依先行核定的資格與成熟規則；不得事後因結果不好而排除。 | 記錄狀態與來源；未核定如何處理時標 UNKNOWN/HOLD。
[T13R009] 分母為 0 | 比率填 N/A，不填 0%。 | 說明沒有合格成熟對象的可查原因，並保留計算期間。
[T13R010] 個資授權、保存、公開範圍未知 | HOLD 真實資料處理；不複製原件到公開檔案。 | 確認授權依據、保管責任、允許摘要、遮罩及保存政策後再使用。
[T13R011] 跨期資料不可比 | 不宣稱趨勢上升或下降。 | 先對齊資格、群組、窗口、來源與期間口徑；完成覆核後再比較。

[TABLE 14; rows=6; cols=4]
[T14R001] 示範代碼 / 缺口 | 行動與預期證據 | 角色 / 日期 / 狀態 | 判定與關閉條件
[T14R002] ACT-SYN-01 / 考照證明尚未查驗 | 向授權保管端確認允許使用的證明定位；完成覆核前不計入成功分子。 / 預期：可驗證來源參照與覆核結果。 | ROLE-ADMIN 建議碼 / DUE=UNKNOWN/HOLD / NEXT=UNKNOWN/HOLD / STATUS=HOLD | HOLD；來源有效且完成覆核後，依核定規則更新。
[T14R003] ACT-SYN-02 / 窗口或資格資料缺項 | 核對授權資格規則及該個案窗口；不可補造日期。 / 預期：資格來源、核定窗口代碼、成熟判定。 | ROLE-COURSE_CONTACT 建議碼 / DUE=UNKNOWN/HOLD / NEXT=UNKNOWN/HOLD / STATUS=OPEN_SAMPLE | HOLD；資料充分且資格/窗口符合後才結算。
[T14R004] ACT-SYN-03 / 回訓未完成 | 依已核定課程安排確認可用的後續學習機會；不假定協會已提供補課。 / 預期：完成紀錄或明確未完成狀態。 | ROLE-COURSE_CONTACT 建議碼 / DUE=UNKNOWN/HOLD / NEXT=UNKNOWN/HOLD / STATUS=REVISE_SAMPLE | REVISE；取得來源後重算，不把邀請當完成。
[T14R005] ACT-SYN-04 / 資料可能重複 | 以去識別代碼、指標、群組、期間檢查重複並保留修訂軌跡。 / 預期：去重理由及更正前後紀錄。 | ROLE-ADMIN 建議碼 / DUE=UNKNOWN/HOLD / NEXT=UNKNOWN/HOLD / STATUS=OPEN_SAMPLE | HOLD；由覆核角色確認唯一採計結果後結案。
[T14R006] ACT-SYN-05 / 趨勢不具可比性 | 檢查各期資格、分母、窗口與來源是否一致；必要時拆開呈現。 / 預期：可比性檢查及受限結論。 | ROLE-REVIEWER 建議碼 / DUE=UNKNOWN/HOLD / NEXT=UNKNOWN/HOLD / STATUS=OPEN_SAMPLE | HOLD；可比性成立才報趨勢，否則標示不可比較。

[TABLE 15; rows=11; cols=3]
[T15R001] 合成代碼 | 目前示範值 / 用途 | REAL 替換所需來源或狀態
[T15R002] SYN-0112-CASE-01 / SYN-P1/P2/P3 | 合成追蹤案例及三個非日曆期間。 | 改用具授權且可追溯的實際 cohort/period；目前 REAL=UNKNOWN/HOLD。
[T15R003] SYN-0112-F001 | P1 輔導考照 3/8=37.5%。 | 受輔導與考照資格名冊、窗口成熟狀態、經授權驗證結果。
[T15R004] SYN-0112-F003 | P2 輔導考照 4/8=50.0%。 | 同上，並確認與其他期間同一口徑。
[T15R005] SYN-0112-F005 | P3 輔導考照 5/8=62.5%。 | 同上，保留來源及核算。
[T15R006] SYN-0112-F002 | P1 學員回訓 4/10=40.0%。 | 回訓資格、邀請/參與及完成紀錄與授權查驗來源。
[T15R007] SYN-0112-F004 | P2 學員回訓 6/10=60.0%。 | 同上，並確認期間與資格口徑可比。
[T15R008] SYN-0112-F006 | P3 學員回訓 7/10=70.0%。 | 同上，保留來源及核算。
[T15R009] ACT-SYN-01..05 | 五種表單演練情境；不是實際事件。 | 替換為有來源的真實缺口及實際行動；不得保留虛構日期、處置或簽名。
[T15R010] ROLE-ADMIN / ROLE-COURSE_CONTACT / ROLE-REVIEWER | 中立的建議角色代碼。 | 只有實際授權的職務分工確認後才能替換；現有人選/任命 UNKNOWN。
[T15R011] WINDOW / APPROVER / RETENTION_POLICY | 官方未定義的窗口、核定權責、保存政策。 | 取得實際核定規則與來源；未取得時保持 UNKNOWN/HOLD，不填自創期限。

[TABLE 16; rows=5; cols=3]
[T16R001] 文件 / 需求 | 主要證據用途 | 不可替代的界線
[T16R002] 0104 / I18-E11 | 證照取得率分析。 | 不能直接當成受輔導 cohort 的相同資格或分母。
[T16R003] 0110 / I18-E19 | 學員/客戶知覺調查與行動計畫。 | 知覺或滿意度不等於證照驗證或回訓完成。
[T16R004] 0111 / I18-E20 | 特殊或社會效益登錄。 | 外部或社會效益不能代替 I18-E21 的兩項追蹤率。
[T16R005] 0112 / I18-E21 | 分別追蹤輔導考照與學員回訓。 | 只有具授權共用來源且範圍相符時，才可引用其他文件的資料；不能只因 ID 相近而搬用。

[TABLE 17; rows=1; cols=1]
[T17R001] 目前狀態：未提供真實學員名冊、證照原件、回訓紀錄或組織核定規則。這份文件是可供檢視和修改的候選工具，不能作為已執行的協會紀錄或正式評核證據。
