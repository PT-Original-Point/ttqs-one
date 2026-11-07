# 0140 / I19-E30 — R11 exact-SHA semantic delta review packet

## Review contract
Review only the R11 changes against the prior exact-SHA semantic PASS. Bind every conclusion to candidate DOCX SHA-256 `5860d73916e94c221a8cdba6ba39bab7236c1af65be5f569448c06ecdcd6b86d`. This packet is text-only: do not use tools, files, UI, browser, or external services. Do not claim technical or visual review. Return PASS, PARTIAL, or FAIL; identify each finding by the source/review locator and quote only short relevant phrases. If the supplied extracted context is insufficient, say PARTIAL. Do not claim formal acceptance or real association evidence.

## Exact artifact identity
- doc_id 0140; official requirement I19-E30; registry index 154; printed checkbox serial UNKNOWN.
- R11 DOCX SHA-256: `5860d73916e94c221a8cdba6ba39bab7236c1af65be5f569448c06ecdcd6b86d`; 127801 bytes.
- Parent R10 DOCX SHA-256: `de9525e42a391d0ed002d23d54d5a9b9c1e042f7c194b71f00b61bd98ff48c16`.
- R10 semantic review receipt SHA-256: `598aa42ac83f3de9462bcf49f6c33fcf657bd1a1432a748c5cfa91e20c2f3d55`.
- R11 source delta receipt SHA-256: `e929d9079dce51347283a11543dab526e29395acc9963ca558533f95ec02cf6a`.

## Official requirement excerpt
TTQS 查核佐證文件資料表－訓練機構版
官方 PDF 第9頁，指標19的4分佐證例示位置（此處是需求位置，不代表機構已獲評4分）：
「運用資訊系統普及率。」
來源檔：E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf
SHA-256：805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709

authenticity: exact text extracted from PDF page 9; the official wording is short and reproduced only for requirement traceability.


## Official registry row
```json
{
  "requirement_id": "I19-E30",
  "indicator_no": "19",
  "subitem_or_score_tier": "4分",
  "official_checkbox_text": "運用資訊系統普及率。",
  "master_register_text_match": "True",
  "official_evidence_table_pdf": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\INPUTS\\R04\\06_OFFICIAL_SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
  "official_evidence_table_page": "9",
  "pdf_text_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "visually_checked_pages": "",
  "deliverable_ids": "0140",
  "deliverable_titles": "訓練資訊系統使用普及率盤點與分析表",
  "deliverable_count": "1",
  "phase2_blueprint_status": "PHASE2_BLUEPRINT_EXPANDED_PREPRODUCTION",
  "production_mode_candidate": "SYNTHETIC_COMPLETE_DRAFT",
  "phase2_plan_count": "1",
  "phase2_title_alignment": "HISTORICAL_PLAN_NAMES_NOT_AUTHORITATIVE_R04_CROSSWALK_TITLE_USED"
}

```

## Unique Blueprint
# DOCX 0140 / I19-E30 Unique Blueprint R01

## Identity and binding
- Project `TTQS_ONE`; DOCX `0140`; requirement `I19-E30`; 157 list index `154`; printed checkbox serial `UNKNOWN`.
- Official title: `訓練資訊系統使用普及率盤點與分析表`.
- Official source: TTQS training-institution evidence table, page 9; exact relevant phrase `運用資訊系統普及率。`
- Genre: `使用情形盤點表＋採用率分析報告＋可供真實填報的操作表單`.
- The official tier reference is not a score assignment. This document must not claim a rating or achievement.

## Unique purpose, reader and evidence role
Enable an association training administrator to define the people and tasks that should use a training information system, measure actual substantive use over a stated period, find role/workflow gaps, and assign a verifiable improvement action. A reviewer must be able to recalculate the denominator and numerator from the included de-identified SAMPLE dataset and identify what real source would replace each synthetic fact.

This is specifically adoption/penetration of a training information system. It is not the I14-E05 document-management/retrieval-speed study, and it is not the I19-E29 certificate/employment outcome report. Account creation, a login, or a claim that a system exists does not count as substantive use.

## Source of truth and prohibited assumptions
Authority order: latest Human Mission and current 01–03 GitHub contracts; official page 9; 142 crosswalk title/ID; this Blueprint; then verified artifact. No live association system, users, activity logs, outcomes, or approvals were located in the scoped sources. Therefore the entire numeric case is `SAMPLE/SYNTHETIC`; `REAL=UNKNOWN/HOLD`. The generic label `SAMPLE-TIS-01` is invented solely for the demonstration and is not a vendor or association deployment.

## Operational definitions and formulas
1. Measurement window: one stated calendar period (sample: 2023, 2024, 2025); compare periods only with the same eligibility and activity definitions.
2. Eligible unique user: one distinct, pseudonymous person in a defined role (training administrator, instructor, or learner) who was assigned at least one required training task that the system is intended to support during that window. Count a person once per period, even if they attended multiple courses. Include eligible people with no account or no activity in the denominator. Exclude only documented out-of-scope roles/tasks, and record exclusions separately.
3. Active user: eligible unique user with at least one system-recorded substantive training workflow transaction during the window. A provisioned account, password reset, or login without a completed task is not active use.
4. Adoption/usage prevalence = active eligible unique users ÷ eligible unique users × 100%. Report numerator, denominator, period, role breakdown, and rounding.
5. Required-workflow completion rate among eligible users = users completing all role-specific mandatory system tasks ÷ eligible unique users × 100%. Also report completion among active users, but label its denominator separately.
6. Percentage-point change = later adoption rate − earlier adoption rate. Relative change may be reported only as `(later−earlier)/earlier ×100%` when the earlier rate is non-zero. Do not call percentage-point change a percent change.
7. De-duplicate using a protected source key before pseudonymization; no personal names, IDs, phone numbers, emails, or credentials in the public candidate. Logs are an example source locator only, not evidence that such logs exist.

## Fixed synthetic worked dataset
The included CSV contains 80 synthetic unique user-period records. Role totals:
- 2023: administrators 2/3 active and 2/3 complete; instructors 2/4 active and 1/4 complete; learners 8/13 active and 6/13 complete. Total 12/20 active; 9/20 complete.
- 2024: administrators 3/3 active and complete; instructors 4/5 active and 3/5 complete; learners 15/20 active and 12/20 complete. Total 22/28 active; 18/28 complete.
- 2025: administrators 3/3 active and complete; instructors 5/6 active and complete; learners 20/23 active and 17/23 complete. Total 28/32 active; 25/32 complete.
- Overall: 62/80 active; 52/80 complete.
Calculated adoption: 2023 60.00%; 2024 78.57%; 2025 87.50%; changes +18.57pp, +8.93pp, and +27.50pp (2025 versus 2023). The example is internally consistent but has no association-performance meaning.

## Required document sections and tables
1. Cover/first-glance card: purpose, reader, when to use, key result, actions, and clear SAMPLE/REAL status.
2. Official requirement and scope mapping (DOCX ID, requirement ID, 157 index, printed serial UNKNOWN, official page).
3. One-page annual system inventory form: system/module, owner role (not a named actual person), covered courses/tasks, eligible roles, period, data source and exact locator, privacy check, and limitations.
4. Eligibility and substantive-activity rules, with include/exclude examples and decision flow.
5. Full SAMPLE system/workflow description and role-to-required-task matrix.
6. Complete 80-row pseudonymous sample register in the appendix; each row shows period, synthetic ID, role, required workflow, required task count, actions completed, active flag, completion flag, and synthetic log reference. Do not omit non-users.
7. Period-by-role count table and a fully reconciled 3-year summary table; independently recalculate every total and rate from the 80 rows.
8. Trend analysis with adoption and completion kept separate; show numerator/denominator, percentage-point changes, explanation limits, and a role-gap diagnosis.
9. Directly usable form: new period data capture, source reconciliation, exception log, review sign-off fields left as unsigned/unapproved workflow fields (not fabricated signatures).
10. A SAMPLE action plan with owner role, due interval, measurable follow-up, evidence locator expected, and HOLD/REVISE triggers. Do not state that the association adopted or completed it.
11. Fact-level synthetic replacement register; map every synthetic period, ID, count, formula, event reference, action, and conclusion to the real record required and secure replacement method.
12. Evidence locator and reviewer checklist; distinguish existing real evidence from evidence requested/absent.

## Sample workflow tasks
- Administrator: course/roster setup, eligibility confirmation, close-out/evaluation export (3 required tasks).
- Instructor: attendance or assessment recording and post-session instructional close-out (2 required tasks).
- Learner: enrolment confirmation, attendance/learning acknowledgement, post-course evaluation (3 required tasks).
The tasks are generic synthetic examples. Real role duties must be confirmed against the association's approved process before using them.

## Acceptance and rejection controls
- Title-blind reading identifies a training-system adoption inventory/analysis, not records-retention/retrieval speed or training outcomes.
- A user can fill the inventory, derive the denominator, classify activity, calculate rates, reconcile role counts, identify missing evidence, and assign follow-up.
- All 80 sample rows roll exactly to the stated totals; formulas can be recomputed; `active=0` means zero substantive actions; completion implies active.
- Account existence/logins alone are not counted; denominator excludes no eligible non-user.
- `SAMPLE/SYNTHETIC` is prominent on each sample table/page; `REAL=UNKNOWN/HOLD`; no association approval, actual IT product, actual system use, actual score, or actual performance is asserted.
- HOLD if eligibility list, period, event logs, task definitions, data authorization, or denominator cannot be verified. REJECT if login-only metrics, unexplained exclusions, duplicate identities, numerator exceeds denominator, mixed periods/definitions, fabricated records, or the analysis claims an official score.
- Typography: body ≥10.5pt and table text ≥9.5pt, clean page breaks and repeated headers for long register. Include all Word/PDF pages in visual review.

## Cross-document links and negative neighbors
- `0064 / I14-E05`: records classification/retention and retrieval-speed methodology; may provide a control for protecting source logs, but does not establish actual training-system adoption.
- `0139 / I19-E29`: certificate examination and employment follow-up; may share training-period context only if a real linked case ID exists. Its results cannot serve as system-use numerator/denominator.
- Any cross-document case linkage must use a verified shared source key or be labelled synthetic; do not invent one.


## Prior independent R10 semantic review response (baseline only)
# R10 獨立語意審查報告 — DOCX 0140 / I19-E30 / 157 項索引 154

**Verdict: PASS**（僅限文字語意層；非 Human 正式接受）

Boundaries stated up front: 我未使用任何工具、未讀取任何檔案、未重算候選 DOCX 之 binary SHA（該 SHA 由 host 綁定並宣稱），未做 Word 視覺/逐頁檢視，未依賴 R07 舊判定。以下所有數值均由隨附 80 列資料集與替換清冊獨立重算。

---

## 1. 重算結果（half-up，2 位小數）

| 年度 | Eligible | Active | 普及率 | Complete | 合格者完成率 | 活躍者完成率 |
|---|---|---|---|---|---|---|
| 2023 | 3+4+13 = **20** | 2+2+8 = **12** | 12/20 = **60.00%** | 2+1+6 = **9** | 9/20 = **45.00%** | 9/12 = **75.00%** |
| 2024 | 3+5+20 = **28** | 3+4+15 = **22** | 22/28 = 78.571… → **78.57%** | 3+3+12 = **18** | 18/28 = 64.2857… → **64.29%** | 18/22 = 81.818… → **81.82%** |
| 2025 | 3+6+23 = **32** | 3+5+20 = **28** | 28/32 = **87.50%** | 3+5+17 = **25** | 25/32 = 78.125 → **78.13%** (half-up) | 25/28 = 89.2857… → **89.29%** |
| 三年 | **80** | **62** | 62/80 = **77.50%** | **52** | 52/80 = **65.00%** | 52/62 = 83.870… → **83.87%** |

角色細項全部重算一致（抽核全數）：2023 ADMIN 2/3、2/3、2/2；INS 2/4、1/4、1/2；LRN 8/13=61.54%、6/13=46.15%、6/8=75%。2024 ADMIN 3/3 全 100%；INS 4/5=80%、3/5=60%、3/4=75%；LRN 15/20=75%、12/20=60%、12/15=80%。2025 ADMIN 全 100%；INS 5/6=83.33%、5/6=83.33%、5/5=100%；LRN 20/23=86.96%、17/23=73.91%、17/20=85%。與 TABLE 7、P79–P82、P93、P95–P97 全部吻合。

**變動量**：+18.57 pp、+8.93 pp、+27.50 pp；合格者完成率 +19.29 / +13.84 / +33.13 pp；活躍者完成率 +6.82 / +7.47 / +14.29 pp — 全部正確。相對變化以全精度計算為 30.95%、11.3636→**11.36%**、45.83% — 與 TABLE 8 一致（若誤用四捨五入後的 78.57 反而會得 11.37%，文件依 P74 全精度規則正確）。分子/分母增減 +8/+4/+12、+10/+6/+16、+9/+7/+16 亦一致。

**活躍未完成分布**（附錄 A2 逐列核對）：2023 講師 INS-02（1/2）、學員 LRN-07/08（2/3）→ 1 名 + 2 名；2024 講師 INS-04、學員 LRN-13/14/15 → 1 名 + 3 名；2025 講師 0 名（5 名活躍全 2/2）、學員 LRN-18/19/20（2/3，completed codes 顯示確為缺 COURSE_EVALUATION）→ 0 名 + 3 名；ADMIN 三年活躍列全數完成，無未完成活躍列。P95–P97 與資料完全一致。附錄 A1/A2 各 81 列（表頭+80）與 CSV 逐列相符；active=1 ⟺ actions_done>0、complete=1 ⟺ actions_done=required 全資料無違反。

## 2. 替換清冊

供應清冊實算：2023 共 20 列 + 2024 共 28 列 + 2025 共 32 列 = 80 user-year，再加 2 筆 control（LOG-INDEX、FORMULA-ROUNDING）= **82 筆資料列**；含表頭 = **83 物理行** — 與 packet 標示相符。DOCX 本文未宣稱任何衝突的筆數；P148「另列每筆資料、日誌索引及公式參數」恰好對應 80+1+1。抽查 record_id、year/role、actions_done、active、workflow_complete、log_ref 與資料集全數一致，`SYNTHETIC_REPLACE_BEFORE_REAL` 狀態一致。

## 3. 各項評估結論

1. **體裁與對應**：P13/P16 給出官方第 9 頁指標 19 之範例文字定位，5.1 給定義、期間、數據，8 節給計算與結果，Table 9 給行動與 HOLD 條件，Table 3 明確區隔 0064/I14-E05（檢索）與 0139/I19-E29（證照就業）— 滿足 index 154「定義/期間/數據 + 來源定位 + 決策/結果 + 跨文件連結」。無錯件範圍混入。
2. **成熟度/可用性**：盤點表（Table 4）、分母與活躍定義（5.1 第 2–3 點）、五步判定路徑（5.2）、空白擷取/對帳/例外表單（13.1–13.3）、簽章流程欄（13.4 未簽署）、REVISE/REJECT/HOLD 條件（11.2）齊備，行政與評核委員可操作。
3. **合成/真實邊界與假主張風險**：SAMPLE/SYNTHETIC 標示覆蓋每張數據表（P24、P47–48、8.2/8.3 標題、Table 8 各欄「（SAMPLE）」）；合成年度顯式列出；中立免責（P16、P47、P99、P110、P154）到位；REAL=UNKNOWN/HOLD、NOT_GRANTED、評分非本機構 — 未發現捏造系統、人名、簽章、核准或實績。
4. **算術**：如上，全數重算通過，無接受 builder 斷言。
5. **清冊對齊**：通過（見 §2）。
6. **R07 修復確認**：
   - (a) 5.3 標題 P43「判定示範（SAMPLE / SYNTHETIC）」✓；
   - (b) 標題括號全形一致、第 7 節 7.1/7.2/7.3 與項目標點一致 ✓；
   - (c) 完成率雙分母明確分列（P34、8.1 公式 2/3、Table 7 三欄）✓；
   - (d) 合成年度顯式 ✓；(e) 中立協會免責 ✓；
   - (f) 第 12 節 checklist 已非流水線術語（但見下方 F1，僅低度殘留）；(g) 9.2 已涵蓋三年活躍未完成案例 ✓；(h) 清冊筆數由 packet 侧確認 82/83，本文無衝突宣稱 ✓。
7. **單一星號強調**：全文無可見 Markdown 星號（僅有 `•` 項目符號）；P86/P87 以「粗體／斜體」文字描述格式，Table 8 以括號承載相對變化 — 無洩漏的 `**` 或 `*` 標記。粗體/斜體實際渲染屬視覺閘，文字層 UNKNOWN。

## 4. Findings（無阻擋性缺點；以下皆低嚴重度）

| ID | Sev | 位置 | 引文 | 為何重要 | 最小安全修復 |
|---|---|---|---|---|---|
| F1 | LOW | TABLE 11 表頭及末列 | 「本候選狀態」「本示範文件尚待逐頁檢視」 | 第 12 節是操作性覆核清單，仍帶候選/審查流程語彙（R07(f) 的輕微殘留） | 表頭改「本文件狀態」；末格改「正式使用前須逐頁檢視頁碼、表格可讀性與附件」 |
| F2 | LOW | TABLE 9 第 3 欄（3 列） | 「責任角色（待核）」「課程承辦角色（是否存在待核）」 | 內容為實質核實指示、非空白待填，但專案反垃圾規則對 `待核` 字面敏感 | 改為「（真實角色是否存在，須由權責者核實）」 |
| F3 | LOW | P97 | 「2025 三筆資料列示尚缺 COURSE_EVALUATION，其他示範年度的原因未提供」 | 2023/2024 之 A2 亦顯示同為缺 COURSE_EVALUATION；「原因」一詞易被讀成「缺失任務未標示」 | 改為「2023、2024 同樣僅缺 COURSE_EVALUATION；三個年度均未記錄個案原因」 |
| F4 | OBS | P92 圖 1 | 「圖 1 SAMPLE 普及率與…完成率」 | 圖形內容無法由文字層驗證；敘事值（P93）已驗為正確 | 視覺閘時核對圖中三點值 = 60.00/78.57/87.50 與 45.00/64.29/78.13 |

## 5. UNKNOWN / 未涵蓋範圍

- 候選 binary SHA-256：**未重算**，採 host 綁定宣稱。
- Word 原生視覺、分頁、圖像外觀、頁碼：**未檢視**，另屬視覺閘。
- 印鑑勾選序號：維持 **UNKNOWN**（文件正確未推斷）。
- 附錄 A2 逐列索引為合成索引，非真實日誌；真實系統、名冊、核准、簽章一律 **UNKNOWN/HOLD**。

本報告為獨立文字語意審查，**不構成 Human 正式接受**，亦不授予 PASS 之最終驗收權。

## Prior R10 semantic receipt (baseline identity/scope)
```json
{
  "work_id": "TTQS-0140-I19-E30-R10-INDEPENDENT-SEMANTIC-REVIEW",
  "reviewer": "OpenCode CLI v2.1.4",
  "requested_model": "opencode/mimo-v2.6-flash-free",
  "session_reported_model": "mimo-v2.6-flash-free",
  "session_reported_provider": "opencode",
  "model_identity_limit": "Session metadata only; no independent provider-side attestation.",
  "result": "PASS",
  "scope": "Full supplied text manuscript, official requirement and Unique Blueprint mapping, 80-row SAMPLE dataset, replacement register (82 data rows plus header), arithmetic/distributions, usability, genre/neighbor distinction, SAMPLE/REAL boundary, false-claim risk, and Markdown italic leakage.",
  "limitations": [
    "Reviewer did not independently recompute binary DOCX SHA; host packet bound extracted text to the stated candidate SHA.",
    "Reviewer did not inspect Word rendering or page images.",
    "This is not Human formal acceptance."
  ],
  "candidate_docx_sha256": "de9525e42a391d0ed002d23d54d5a9b9c1e042f7c194b71f00b61bd98ff48c16",
  "review_packet_sha256": "e9d5f92c17b9f078f2fc1d7bdd9a5695317eb6f0ca403765b5e91d7801bdd692",
  "original_response_file": "OPENCODE_R10_REVIEW_RESPONSE.md",
  "original_response_sha256": "73400bfceec096a794a211c85347e93a19c0a274e734e7c8882672ea9953c0cd",
  "token_usage_reported_by_session": {
    "input": 43224,
    "output": 2986,
    "reasoning": 9049,
    "cache": {
      "read": 3456,
      "write": 0
    }
  },
  "cost_reported_by_session": 0,
  "token_and_cost_note": "OpenCode session metadata reports tokens and cost; no external billing-meter readback was available.",
  "findings": [
    {
      "locator": "Table 11 header and final row",
      "issue": "Residual candidate/review workflow language remains in operational checklist.",
      "minimal_repair": "Change status header to 本文件狀態; replace final cell with practical page/table/attachment checks.",
      "severity": "LOW",
      "id": "F1"
    },
    {
      "locator": "Table 9 column 3, three rows",
      "issue": "待核 wording may resemble a placeholder.",
      "minimal_repair": "Use explicit wording that the responsible person must verify whether the real role exists.",
      "severity": "LOW",
      "id": "F2"
    },
    {
      "locator": "P97",
      "issue": "2025 COURSE_EVALUATION omission wording omits the same 2023/2024 cases.",
      "minimal_repair": "State that all three synthetic years omit COURSE_EVALUATION; individual causes are not recorded.",
      "severity": "LOW",
      "id": "F3"
    },
    {
      "locator": "Figure 1, P92",
      "issue": "Text-only review cannot verify plotted points.",
      "minimal_repair": "Use the separate 29-page visual receipt; do not infer from text review.",
      "severity": "OBS",
      "id": "F4"
    }
  ],
  "cli_exit_code": "UNKNOWN_WRAPPER_TIMED_OUT_AFTER_240S",
  "terminal_event_reason": "stop",
  "finished_response_captured_after_wrapper_timeout": true,
  "computer_use": "NOT_USED",
  "auto_approve": "NOT_ENABLED",
  "fallback_allowed": false
}
```

## R11 change receipt
```json
{
  "schema": "ttqs-one-evidence-receipt-v1",
  "project_id": "TTQS_ONE",
  "work_id": "TTQS-0140-I19-E30-R11-REVIEW-FINDING-REPAIR",
  "doc_id": "0140",
  "official_requirement_id": "I19-E30",
  "official_registry_index": 154,
  "base_candidate_revision": "R10",
  "base_candidate_sha256": "de9525e42a391d0ed002d23d54d5a9b9c1e042f7c194b71f00b61bd98ff48c16",
  "source_manuscript": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0140_I19-E30_SOURCE_PREP_R03_20261025\\worker\\MANUSCRIPT_0140_R10.md",
  "base_manuscript_sha256": "05a48af62b25273f41019aa6f66d61ca2a1c9c111d51e3e02a37afeac2e4e4d6",
  "new_manuscript": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0140_I19-E30_SOURCE_PREP_R03_20261025\\worker\\MANUSCRIPT_0140_R11.md",
  "new_manuscript_sha256": "8dcd4ec781e21d163a1912ff2397f40272ce357206fc7d81cea3a645116066df",
  "review_receipt_sha256": "598aa42ac83f3de9462bcf49f6c33fcf657bd1a1432a748c5cfa91e20c2f3d55",
  "independent_findings": [
    "F1",
    "F2",
    "F3"
  ],
  "changes": [
    {
      "before": "2025 三筆資料列示尚缺 COURSE_EVALUATION，其他示範年度的原因未提供。",
      "after": "2023、2024 同樣僅缺 COURSE_EVALUATION；三個年度均未記錄個案原因。",
      "occurrences": 1
    },
    {
      "before": "責任角色（待核）",
      "after": "責任角色（真實角色是否存在，須由權責者核實）",
      "occurrences": 1
    },
    {
      "before": "課程承辦角色（是否存在待核）",
      "after": "課程承辦角色（真實角色是否存在，須由權責者核實）",
      "occurrences": 1
    },
    {
      "before": "本候選狀態",
      "after": "本文件狀態",
      "occurrences": 1
    },
    {
      "before": "本示範文件尚待逐頁檢視；正式使用前須由權責人員核定",
      "after": "使用前須逐頁檢視頁碼、表格可讀性與附件，並由權責人員核定",
      "occurrences": 1
    }
  ],
  "unchanged": [
    "SAMPLE dataset",
    "replacement register",
    "calculations",
    "tables except targeted labels/text",
    "REAL=UNKNOWN/HOLD",
    "formal acceptance NOT_GRANTED"
  ],
  "state": "CANDIDATE_TECHNICAL_PASS_PENDING_R11_EXACT_SHA_VISUAL_AND_SEMANTIC_DELTA_REVIEW",
  "observed_at": "2026-10-25T13:24:42.7048426+08:00",
  "candidate_sha256": "5860d73916e94c221a8cdba6ba39bab7236c1af65be5f569448c06ecdcd6b86d",
  "candidate_bytes": 127801,
  "build_receipt_sha256": "39a2c58493b22f8d73373c15879f4d514d60dd96378a1b1a97e0bf07670f47aa",
  "comprehensive_qa_status": "PASS_TECHNICAL",
  "comprehensive_qa_sha256": "bc3655dbe60bebfe4bc7dda65514808ae3ccb50cf85098e4f7fcb059ab5028d2"
}
```

## Actual R11 DOCX extracted paragraph context
P96: • INSTRUCTOR：普及率 2/4、4/5、5/6；合格者全任務完成率 1/4、3/5、5/6。2023 與 2024 示範資料各有 1 名活躍講師只完成 1/2 任務；合成資料未記錄兩年度個案原因。2025 示範資料中 5 名活躍講師均完成 2/2 任務；以上分布不代表真實改善。
P97: • LEARNER：普及率 8/13、15/20、20/23；合格者全任務完成率 6/13、12/20、17/23。2023、2024、2025 示範資料分別有 2、3、3 名活躍學員完成 2/3 任務；2023、2024 同樣僅缺 COURSE_EVALUATION；三個年度均未記錄個案原因。以上分布不代表真實改善。
P98: 9.3 解讀界限

## Actual R11 DOCX table rows matching the changed topics
T11-R1: 覆核點 || 可操作的核對問題 || 本文件狀態 || 真實替換所需證據
T11-R9: Word 與使用前檢查 || 頁碼、表格可讀性與附件是否齊全？ || 使用前須逐頁檢視頁碼、表格可讀性與附件，並由權責人員核定 || 頁碼檢查紀錄、附件清單、權責人員核定紀錄

## Deterministic Builder QA excerpt (context only; not independent semantic evidence)
```json
{
  "targeted_instructor_distribution": {
    "result": "PASS",
    "evidence": "Section 9.2 states all three years without unsupported cause"
  },
  "targeted_learner_distribution": {
    "result": "PASS",
    "evidence": "Section 9.2 states 2023=2, 2024=3, 2025=3"
  },
  "human_facing_status_cells": {
    "result": "PASS",
    "evidence": [
      [
        "官方映射",
        "DOCX 0140 是否仍對 I19-E30、157 index 154、官方第9頁？",
        "官方第9頁出處已核對；本文件為示範，不代表正式評核結果",
        "最新官方來源頁及本文件對照紀錄"
      ],
      [
        "Word 與使用前檢查",
        "頁碼、表格可讀性與附件是否齊全？",
        "使用前須逐頁檢視頁碼、表格可讀性與附件，並由權責人員核定",
        "頁碼檢查紀錄、附件清單、權責人員核定紀錄"
      ]
    ]
  },
  "pipeline_jargon_removed_from_checklist": {
    "result": "PASS",
    "evidence": [
      [
        "官方映射",
        "DOCX 0140 是否仍對 I19-E30、157 index 154、官方第9頁？",
        "官方第9頁出處已核對；本文件為示範，不代表正式評核結果",
        "最新官方來源頁及本文件對照紀錄"
      ],
      [
        "Word 與使用前檢查",
        "頁碼、表格可讀性與附件是否齊全？",
        "使用前須逐頁檢視頁碼、表格可讀性與附件，並由權責人員核定",
        "頁碼檢查紀錄、附件清單、權責人員核定紀錄"
      ]
    ]
  },
  "sample_real_formal_status": {
    "result": "PASS",
    "evidence": {
      "candidate": "CANDIDATE",
      "real": "UNKNOWN/HOLD",
      "formal_acceptance": "NOT_GRANTED"
    }
  }
}
```

## Reviewer questions
1. Does R11 resolve R10 findings F1-F3 in the actual extracted R11 text and table rows, without converting unknown real roles or missing reasons into factual claims?
2. Are the revised statements consistent with the official I19-E30 requirement and the Unique Blueprint?
3. Did the changed wording create any new contradiction, unsupported assertion, or unusable instruction in the reviewed scope?
4. State the verdict and exact scope. Keep visual layout, unchanged body, formal acceptance, REAL evidence, and provider billing outside this text-only review unless the supplied evidence explicitly supports a conclusion.
