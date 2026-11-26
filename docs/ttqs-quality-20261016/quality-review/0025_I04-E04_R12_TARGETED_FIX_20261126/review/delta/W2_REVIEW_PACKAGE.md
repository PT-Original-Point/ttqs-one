# TTQS ONE 0025 R12｜W2 精確 SHA 範圍複核

work_id=TTQS_ONE_0025_I04-E04_R12_W2_SCOPED_DELTA_REVIEW_20261126
doc_id=0025
requirement_id=I04-E04
base_candidate_sha256=7fe989df84e5d4e5b1163617aa2e470e2ba497b7aac7e0414dc1a55dd0625fd3
reviewed_candidate_sha256=2a6eae131aeff27275adc2e6fa851e05b1cdf2b7688b1da96cd79c27a88f3712
requested_model=gemini-3.8-flash-high
actual_served_model=UNKNOWN unless the CLI response itself attests it
role=independent semantic delta reviewer; text-only; no tools, no file access, no edits

## Boundary

The base candidate received a complete independent semantic review at the base SHA below. That review found exactly five blocking defects and no other blockers; it was a FAIL and is not a PASS for this candidate. A later R11 scoped confirmation covered only a prior small B1 delta, so it is not acceptance evidence for the five defects below. The W1 R12 review attempt has no recoverable response or terminal receipt and must not be treated as a verdict. This W2 request is limited to confirming whether the R12 candidate fixes all five baseline blockers without creating contradictions in their cross-references. Do not claim a fresh full-document review.

## Official / Blueprint scope

The candidate is a SAMPLE/SYNTHETIC SOP for I04-E04: training result evaluation, implementation basis, and standardized operating procedure. Formal approval, real institutional facts, real attendance, real outcomes and third-party originals remain UNKNOWN/HOLD. Base full review already checked the rest of the body against the project blueprint; preserve that review as a failed baseline, then assess only the exact repair delta and its cross-references here.

## R12 repair manifest

{
  "repair_scope": [
    "D-06 code-to-authority mapping",
    "E-11 R03/R05 fallback and pause disposition",
    "IB-05 mandatory yes / no N/A",
    "IB-06 N/A meaning and evidence fields",
    "S03 and worked example alignment",
    "revision and synthetic replacement register synchronization"
  ],
  "changed_ooxml_locations": [
    "T3R3C2",
    "T3R5C2",
    "T4R3C6",
    "T10R3C3",
    "T11R6C2",
    "T11R6C4",
    "T12R2C3",
    "T14R5C1",
    "T14R6C1",
    "T15R2C1",
    "T16R6C0",
    "T16R6C1",
    "P37",
    "P39",
    "T20R11C3",
    "T20R11C4",
    "T21R1C2",
    "T21R2C2",
    "T23R3C1",
    "T31R1C2",
    "T32R1C2",
    "T35R44C2",
    "T35R45C2",
    "P1",
    "T39R4C1",
    "T38_APPEND_R12",
    "T35_APPEND_REGISTER_119",
    "P88"
  ],
  "candidate_bytes": 72213,
  "formal_acceptance": "NOT_GRANTED",
  "candidate_state": "SAMPLE_SYNTHETIC_CANDIDATE"
}

## Exact R12 candidate excerpts (from the fixed DOCX text extraction)

[77] | R03 | 訓練品質主管 | 審核實施依據、覆核評估結果、核准例外與矯正；決定 E-11 復行；拒絕核准或收件後 3 個工作日未決時升級 R05。 |
[81] | R05 | 高階主管 | 重大例外與升級案件之最終決策；處理 R03 拒絕或逾期未決之 E-11；目標或門檻變更由 R05 核准。 |
[91] | 步驟群 | R01 | R02 | R03 | R04 | R05 | 分離控制要求 |
| 例外／矯正 | R | C | A | C | A（重大） | 重大例外須 R05 決策；E-11 由 R03 初審復行，拒絕核准或 3 個工作日未決即升級 R05；R01 不得關閉自身登錄之例外。 |
[177] | 步驟 | 輸入 | 責任 | 判斷 | 控制點（CP） | 輸出 | 紀錄 |
| S02 實施依據確認 | F-0025-01 | R01 填寫，R03 核准 | 適用項目全數通過；僅具來源依據且經 R03 記錄核准之 N/A 可排除 | CP-02 | 實施依據確認紀錄 | R-0025-S02 |
[179] | 步驟 | 輸入 | 責任 | 判斷 | 控制點（CP） | 輸出 | 紀錄 |
| S03 開課與執行 | 核准計畫版本／課程資料 | R02 | 按核准版執行；記錄日期、時數、講師、教材版次、出席與偏差。偏差立即暫停受影響部分並登錄 E-11；1 個工作日內送 R03，核准後復行；R03 拒絕或收件後 3 個工作日仍未決時升級 R05；R05 決議前持續暫停。目標或門檻變更須 R05 核准後復行。 | CP-02 | 執行紀錄及偏差紀錄 | R-0025-S03／E-11 |
[213] | D-06 | 例外升級 | E-02~E-07、E-10：發現後 3 個工作日內升級 R03；E-08：3 個工作日內升級 R05；E-01、E-09：1 個工作日內升級 R05；E-11：1 個工作日內送 R03。R03 拒絕 E-11 核准或收件後 3 個工作日仍未決時升級 R05；未決前持續暫停。處置期限另依 §10.1。 | 例外發生日 | 依代碼升級：E-02~E-07、E-10→R03；E-08、E-01、E-09→R05；E-11→R03，R03拒絕或3個工作日未決則R05；目標／門檻變更另交R05。 |
[221] | CP-02 | 實施依據核准 | R03 | F-0025-01 適用項目均為「是」；IB-05 必須為「是」且不得 N/A；IB-06 N/A 僅限 0024 範疇證明無適用參與者類別，並有來源、理由及 R03 核准。 | 不通過不得開課；登錄 E-01 |
[253] 開始：取得評估數據。四項評估指標逐項判定；本段 N/A 僅適用反應、學習、行為、成果四項指標，須有範疇依據、具體理由並經 R03 核准，且不得遮蔽未達的適用指標；F-0025-01 的 IB-01~IB-06 不適用本段 N/A 規則，尤其 IB-05 必須為「是」，不得列 N/A（見 §8.3）。若四項評估指標均為 N/A，記錄「不適用，無法判定符合」，不得宣告通過。反應 ≥ T-REACT？是→記錄通過；否→登錄 E-05 並升級 R03。學習 ≥ T-LEARN？是→記錄通過；否→登錄 E-06 並擬定重訓／修課計畫。行為 ≥ T-BEHAV？是→記錄通過；否→登錄 E-07 並擬定輔導計畫。成果 ≥ T-RESULT？是→記錄通過；否→登錄 E-08 並依層級升級 R05。綜合判定：全部適用指標通過＝符合；1~2項未通過＝部分符合並改善；3~4項未通過＝不符合並升級 R05。
[267] | 項目 | 判定規則 |
| IB-05 與年度計畫連結 | 必須為「是」；不得標示 N/A。否或未填均未通過 CP-02，不得開課。 |
[269] | IB-06 利益關係人已參與（引用 0024 範疇，本程序僅確認有紀錄） | 原則須為「是」。N/A 僅表示依 0024 範疇證據可證明沒有適用的參與者類別，不表示參與者缺席或未參與；須記錄 0024 類別、證據來源、具體理由並經 R03 核准。缺少適用參與者紀錄不得列 N/A。 |
[271] 判定：IB-01~IB-06 均須符合適用條件；適用項目須為「是」。IB-05 為必填，必須為「是」，不得標示 N/A。IB-06 的 N/A 僅表示依 0024 範疇資料可證明「沒有適用的參與者類別」，不表示參與者缺席或未參與；F-0025-01 必須記錄 0024 類別、對應資料、明確理由與來源，並由 R03 核准。缺少應有的參與者紀錄不得列 N/A。任一適用項目為「否」、或 IB-06 N/A 未具體核准，均不得實施；依情形登錄 E-01 或退回補正。
[279] | IB-06 確無適用範疇 | N/A 僅代表 0024 範疇證明沒有適用的參與者類別，不代表參與者缺席或未參與；記錄 0024 類別、證據定位、理由及 R03 核准。應有參與者但缺簽到或紀錄時列為缺件，不得 N/A。 |
[301] | IB-01~IB-06（IB-05不得N/A） | IB-01~IB-04、IB-06：是／否／N/A；IB-05：是／否，不得 N/A | 是 | 判定依據 |
[377] | IB-05 與年度計畫連結 | 是 |
[379] | IB-06 利益關係人已參與 | 是；引用 MR-SMP-2026-001（SAMPLE索引，非真實會議或簽到原件） |
[457] | E-11 | 未依核准訓練計畫執行／重大偏差 | 高 | 立即暫停受影響部分並登錄 E-11；1 個工作日內送 R03，核准後復行。R03 拒絕核准或收件後 3 個工作日仍未決時升級 R05；R05 決議前持續暫停。涉及目標或門檻變更須 R05 核准後復行。 | 升級 R03：1 個工作日；R03 拒絕或收件後 3 個工作日未決→R05；處置：立即暫停，決議前不得復行 |
[463] | Level 1 | R03 訓練品質主管 | E-02~E-07、E-10；E-11 復行核准；R03 拒絕或收件後 3 個工作日未決之 E-11 升級 Level 2 R05；涉及目標或門檻變更另由 R05 核准。 |
[465] | Level 2 | R05 高階主管 | E-01、E-08、E-09、重大例外；E-11 涉目標或門檻變更，或 R03 拒絕／3 個工作日未決。R05 決議前維持暫停；R05 未核准不得復行。 |
[521] | 步驟 | 執行內容（SAMPLE） | 結果（SAMPLE） |
| S02 | R01填F-0025-01，R03於2026-08-07核准（SAMPLE） | 通過CP-02；於開課前5個工作日完成 |
[523] | 步驟 | 執行內容（SAMPLE） | 結果（SAMPLE） |
| S03 | 按 R03 核准計畫版 SMP-PLAN-V1.0 執行；記錄實際日期、時數、講師、教材版次、出席及偏差；偏差立即暫停受影響部分並登錄 E-11，1 個工作日內送 R03；R03 核准後復行，拒絕或收件後 3 個工作日未決升級 R05，R05 決議前持續暫停；目標或門檻變更須 R05 核准後復行。 | 完成R-0025-S03；本例無偏差（SAMPLE） |
[653] | 1 | DOC_VERSION | 0.3（SAMPLE） | 封面、§15.3、§17 | 文件屬性 | 正式版本號與核准紀錄 | R03 |
[689] | 18 | DEADLINE_D06 | 例外期限依§7.2逐代碼列明；E-11於1個工作日送R03，拒絕或收件後3個工作日未決升級R05。 | §7.2 | 期限參數 | 授權之時限規定 | R03 |
[775] | 59 | RECORD_STEP_S03 | R-0025-S03 | §7.1 | 紀錄編號 | 真實紀錄編號與檔案 | R02 |
[807] | 74 | CONTROL_CP02 | CP-02 | §7.3 | 控制點 | 實際稽核結果 | R04 |
[883] | 112 | EXCEPTION_TIMELINE_RULES | D-06：E-02~E-07、E-10於3工作日升級R03；E-08於3工作日升級R05；E-01、E-09於1工作日升級R05；E-11於1工作日送R03，拒絕或3工作日未決升級R05。處置期限另列。 | §7.2、§10.1、§10.2 | 期限規則 | 授權例外處置時限 | R03/R05 |
[885] | 113 | EXCEPTION_E11 | E-11立即暫停受影響部分；1工作日送R03；核准後復行；R03拒絕或3工作日未決轉R05；R05決議前維持暫停；目標／門檻變更須R05核准。 | §7.1、§10.1、§10.2 | 控制規則 | 核准計畫與正式偏差紀錄 | R02/R03/R05 |
[897] | 119 | DOC_REVISION_DATE_0_3 | 2026-11-26（SAMPLE修訂日期） | §15.3、§17 | 版本日期 | 正式版本發行／修訂紀錄 | R01/R03 |
[941] | 0.2 | 2026-11-26（SAMPLE） | R01 | 修正評估分母與個人判準、升級/處置時限、IB-06條件、R04計算覆核、S03偏差控制及替換簿（候選修訂；非正式核准） |
[943] | 0.3 | 2026-11-26（SAMPLE） | R01 | 修正例外升級層級與 E-11 未決處置；明確限定 IB-05 必須為「是」及 IB-06 N/A 的範疇意義；候選修訂，非正式核准。 |

## Prior full-review result on base SHA 7fe989df84e5d4e5b1163617aa2e470e2ba497b7aac7e0414dc1a55dd0625fd3

REVIEWED_CANDIDATE_SHA256=7fe989df84e5d4e5b1163617aa2e470e2ba497b7aac7e0414dc1a55dd0625fd3
VERDICT=FAIL

BLOCKING DEFECTS:

1. §7.2 D-06 upgrade level contradicts §10.2 upgrade path  
   - Location: §7.2 D-06 row ("例外升級" table); §10.2 Level 1/2 escalation table  
   - Original text: D-06 states "一般例外發現後3個工作日；E-01、E-09、E-11依§10.1於1個工作日內升級；處置完成期限另依§10.1 | 例外發生日 | 升級 R05". §10.2 Level 1 (R03) handles E-02~E-07, E-10; Level 2 (R05) handles E-01, E-08, E-09, major exceptions.  
   - Violated requirement: Upgrade authority and timeline must be internally consistent across all tables (§7.2 time limits, §10.2 escalation path). The SOP cannot simultaneously place general exception upgrades under R05 (3-day) and R03 (Level 1) without creating enforcement ambiguity.  
   - Minimal fix: Align D-06 with §10.2 — general exceptions (E-02~E-07, E-10) should upgrade to R03 (Level 1) within 1 work day, with R05 involvement only for E-01, E-08, E-09 and major exceptions per §10.2.

2. §10.1 E-11 upgrade contradicts D-06 upgrade  
   - Location: §10.1 E-11 row; §7.2 D-06 row  
   - Original text: §10.1 E-11 states "升級 R03：1個工作日；處置：立即暫停". D-06 states "升級 R05：1個工作日；處置：立即暫停" (as part of "E-01、E-09、E-11依§10.1於1個工作日內升級").  
   - Violated requirement: Same exception code must specify identical upgrade authority across all referenced tables (exception definition vs. time limits). Contradictory upgrade targets for E-11 create enforcement ambiguity and risk incorrect authority assignment.  
   - Minimal fix: Unify E-11 upgrade authority. If E-11 should upgrade to R03 (as per exception definition in §10.1), update D-06 to reflect R03 upgrade in 1 work day. If R05 is correct per operational reality, update §10.1 E-11 accordingly.

3. §8.2 decision tree allows N/A for IB-05, but §8.3 IB-05 requires "是"  
   - Location: §8.2 decision tree ("四項逐項判定"); §8.3 IB-05 row  
   - Original text: Decision tree states "N/A僅限有範疇依據、具體理由並經 R03 核准者，且不得遮蔽未達的適用指標。若四項均為 N/A，記錄「不適用，無法判定符合」，不得宣告通過." §8.3 IB-05 states "IB-05 與年度計畫連結 | 必須為「是」".  
   - Violated requirement: Decision framework must not permit N/A for requirements explicitly designated "must be Yes" (§8.3 IB-05). Allowing N/A for IB-05 creates an irreconcilable conflict with the "must be Yes" mandate and risks improper N/A marking to circumvent threshold requirements.  
   - Minimal fix: Revise the decision tree to exclude IB-05 from N/A options, or update IB-05 to specify conditions under which N/A may apply (with R03 approval recorded and documented rationale).

4. IB-06 N/A condition ambiguity risks misinterpretation as "non-participation"  
   - Location: §8.3 IB-06 row; §5.2 RACI table role definitions  
   - Original text: IB-06 states "利益關係人已參與（引用 0024 範疇，本程序僅確認有紀錄） | 原則須為「是」；僅當 0024 範疇證明確不適用，且 R03 記錄理由與來源時才可 N/A；缺少適用參與者紀錄不得視為 N/A." Role definitions state "R01 不得自行核准；R03 不得為同一案件之唯一稽核者" without clarifying IB-06 N/A meaning.  
   - Violated requirement: N/A condition for participation (IB-06) must unambiguously distinguish "category inapplicable" from "person did not participate." The current wording risks treating N/A as equivalent to non-participation, violating the intent that IB-06 N/A only applies when 0024 categories prove inapplicable with R03 approval.  
   - Minimal fix: Add explicit documentation that IB-06 N/A = "0024 categories proved inapplicable with R03 approval," not "participant absent." Ensure F-0025-01 IB-06 field guidance distinguishes these meanings and that R03 approval records include the specific 0024 category reference.

5. §7.1 S03 deviation resolution path incomplete  
   - Location: §7.1 S03 row; CP-02 row  
   - Original text: S03 states "偏差停受影響部分、登錄 E-11，R03 核准後復行." CP-02 states "不通過不得開課；登錄 E-01." No specification exists for what occurs if R03 withholds deviation-approval authorization, nor is there a time limit for R03's approval decision.  
   - Violated requirement: Every operational step must have a defined resolution path when the primary authority acts, and time-bound deadlines must exist for approval decisions to prevent process stagnation (§7.1 general requirement for defined control points and dispositions).  
   - Minimal fix: Add to S03 a specification that if R03 does not approve the deviation resolution within 3 work days, the matter escalates to R05 per §10.2 Level 2. Include a default disposition (e.g., suspend affected portion until resolution) if R05 also defers, and document the escalation path in the control point definition.

The complete document, including all tables, SAMPLE values, and the 118-entry SYNTHETIC REPLACEMENT REGISTER (§14.3), has been reviewed. No LOW suggestions are mixed with the blocking findings above. The candidate consistently marks all content as SAMPLE/SYNTHETIC, the replacement register logs every synthetic fact with precise location and replacement requirements, and the cover page clearly states "SAMPLE/SYNTHETIC (非 REAL; 尚未取得可核實原件)." However, the five blocking defects listed must be resolved before this SOP can be accepted for operational use.

FINAL: The packet-required fields (purpose, scope, roles, inputs, steps, thresholds, calculations, cross-references, real data status) are present and generally consistent with the Blueprint. However, the five blocking defects above violate core acceptance requirements and must be corrected.

## Reviewer task

Review only the R12 repair delta against the five exact blockers in the baseline result, using the exact R12 excerpts above and their cross-references. For each blocker (1–5), state RESOLVED / NOT_RESOLVED / UNKNOWN, with exact section/table anchor and a short rationale. Check consistency among D-06, §10.1, §10.2, the S03 procedure/example, IB-05 decision tree/table, IB-06 meaning and forms, plus revision/replacement-register entries. Reject if a repaired table still contradicts another included cross-reference. Keep SAMPLE/REAL and authority limits explicit. Do not invent recommendations or edit files.

End with exactly one verdict: VERDICT=PASS_SCOPED_DELTA only if all five blockers are RESOLVED; otherwise VERDICT=FAIL or PARTIAL. Repeat reviewed_candidate_sha256 exactly. Separate request model from actual model; actual model is UNKNOWN unless independently attested in the returned response.
