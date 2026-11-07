# Independent Semantic Review — 0033 I07-E01 R07

**Verdict: PASS** (text-scope semantic review only; all material tests pass; minor non-blocking observations listed at the end).

Candidate SHA-256 and packet SHA values are recorded as given; per scope I make no independent re-hashing, no visual/font verification, no official-acceptance claim, and no REAL-evidence claim.

---

## 1. Requirement and genre match — PASS

- Blueprint row: genre 策略／計畫文件「訓練課程計畫配合客戶及受訓者需求、職能需求的_可直接使用成品」, requirement I07-E01「訓練課程計畫配合客戶及受訓者需求、職能需求的調查規劃的證明。」
- Official page-2 locator: 「訓練課程計畫配合客戶 及受訓者需求、職能需求的調查規劃的證明。」is the first bullet under 設計／指標7 的「常見參考佐證資料」欄。Spacing differences are PDF-extraction artifacts; the wording matches the blueprint's `official_requirement_text` verbatim.
- Candidate **P006** cites《TTQS 查核佐證文件資料表》第2頁、指標7, quoting the same sentence — exact match. Requirement ID mapping (I07-E01→指標7 first bullet) is correct.
- Genre execution: the body is a directly usable strategy/plan deliverable (P000–P002 title statement, P003 30-second usage block, blank issuance-ready survey at 表5, blank record forms at 表19/表20). The `title_blind_test` holds: body-specific mechanisms (needs survey + course-objective mapping + explicit rejection of neighbor work-products) do not transfer to other requirements without modification.

## 2. Usable survey and worked SAMPLE — PASS

- **表5 (TABLE 6)**: 18 questions, each with explicit options/answer mode (single/multi/capped at 2/open). **P025** defines both scales: 重要度量尺 "1目前不重要、2較低、3中等、4重要、5非常重要"; 自評把握度 scale with “無經驗不列入平均。” Matches register F0033_SCALE_IMPORTANCE / F0033_SCALE_SELF exactly, and both are correctly marked PROPOSED_SCALE (not official).
- Worked SAMPLE: case ID SYN-0033-PLAN-01, 示範期間 2026/08/03–2026/08/14 (P033; register F0033_CASE/START/END), full per-fact register rows, and a complete 18-question fill (表18/TABLE 21, R01: R01_Q01–Q18 in register) — no blanks or future-tense placeholders presented as completion.

## 3. Question mechanics and Q07 SAMPLE verification — PASS (explicitly requested)

Q07 (表5): 「最需要改善哪種情境？最多2項」 options: 不確定責任者；需求交接遺漏；說明服務範圍困難；流程不清；紀錄過多／過少；其他。

Q07 SAMPLE trace:
| Source | Value | Match |
|---|---|---|
| Document 表18 (TABLE 21) Q07 | 需求交接遺漏；其他：工作界線不清。 | — |
| Candidate (same table) | 需求交接遺漏；其他：工作界線不清。 | identical |
| Register F0033_R01_Q07 | 需求交接遺漏；其他：工作界線不清。 | identical |

Both selections are valid against the option list; 2 items respect the “最多2項” cap; the “其他” free-text is used correctly. **Document, candidate, and register agree exactly.**

Full SAMPLE option-consistency spot-check of SYN-R01 (R01_Q01–Q18 all in register, all in 表18): every selected option exists in 表5's option list (e.g., Q02 three valid selections on a 可複選 item; Q03/Q08 two selections respecting caps; Q10 = 資料交接; Q13 = 3–4小時; Q15 = 紙本；休息安排). Density cross-check: Q04 (甲5；乙4；丙4；丁4) matches 表8 row SYN-R01 (5,4,4,4) and F0033_SYN-R01_*_IMP; Q05 (甲3；乙3；丙4；丁2) matches 表9 row SYN-R01 (3,3,4,2) and *_SELF. All agree.

## 4. Denominators and formula accuracy — PASS (all recomputed)

Table 7 (TABLE 8) internal arithmetic: 4+4+4=12 invited; 3+3+4=10 returned; 3+3+3=9 valid ✓. Group ratios: 3/4=75.0% (×2), 4/4=100.0%, valid 3/4=75.0% ✓. Totals: 10/12=83.3%, 9/12=75.0%, 9/10=90.0% (P036) ✓, all consistent with register F0033_RATE_* and F0033_GROUP_*.

Narrative↔table↔register consistency: 任務角色代表 4 returned / 3 valid ↔ SYN-R10 Q04-matrix exclusion (P033, F0033_SYN_R10_EXCLUSION, per the pre-declared valid rule in P031) ✓; two nonresponses (SYN-R11 合作窗口， SYN-R12 預定受訓者) ↔ 12−10=2 (F0033_NONRESPONSE) ✓.

Table 10 (TABLE 11): importance sums 41/38/35/39 recomputed from 表8 rows ✓; self sums 24/25/27/21 from 表9 rows ✓; means 4.56/4.22/3.89/4.33 and 2.67/2.78/3.00/2.33 at ÷9 valid N ✓; gaps 1.89/1.44/0.89/2.00 on unrounded values per P044 ✓. Priority rule (P045): ≥4.00 且 ≥1.20 → 丁(2.00)第1、甲(1.89)第2、乙(1.44)第3；丙(3.89/0.89) retained with risk check — matches 表11 and F0033_PRIORITY_RULE.

Weighted comparison (表14): weights 40+30+20+10=100% ✓; 甲 5×.4+5×.3+4×.2+5×.1=4.80; 乙 4.00; 丙 3×.4+3×.3+5×.2+4×.1=3.50 — matches P056 逐步重算 and register TOTAL rows ✓. Hours: 90+90+120+60=360 min = 6小時 (P061, F0033_TOTAL_HOURS) ✓. Rounding rules stated (P036 1 decimal for rates; P044 2 decimals for means, unrounded intermediates) ✓ — no conflict between the two conventions.

72 rating values (P041): register contains GROUP + 8 rating rows × 9 respondents = 72 fact rows; spot-checked cells (e.g., R03 丁_IMP 5 ↔ 表8； R09 丁_SELF 2 ↔ 表9) agree.

## 5. SAMPLE/REAL boundary — PASS

- P002 global SAMPLE/SYNTHETIC banner; P012 UNKNOWN declaration for activities/courses/participants; 表2 clocks the four source classes (official requirement REAL, legal name REAL readback, historical manual HISTORICAL_CONTEXT_ONLY dated 2026-10-05, all survey/answer/score/plan data SAMPLE/SYNTHETIC); P088 reiterates status. No synthetic value is presented as institutional fact; P015/P092 forbid pre-filling authorization.
- Blueprint `prohibited_fabrication` respected: no fabricated approvals, signatures, third-party originals; P088 and 表21/TABLE 24 (正式採用及實施 row) route required originals to lawful acquisition paths only.

## 6. Register coverage — PASS

Every synthetic element used in the body has at least one register row with value, type, section/table anchor, replacement source, owner, and reviewer placeholder: denominators (12/10/9), per-group counts, rates, nonresponse/exclusion cases, all 72 rating cells, all means/gaps, threshold rule, weights, anchor rubric, plan scores/total, direction labels, decision, capacity 12, 4 modules (title/objective/assessment/minutes), total hours, 4-week cycle, and the complete SYN-R01 extraction. All three register groupings internally reconcile with 表7 (no orphan facts found).

## 7. Required tables/figures vs Blueprint — PASS

| Blueprint requirement | Locator | Status |
|---|---|---|
| 欄位—定義—來源—填寫者—驗證規則 | 附表 (TABLE 26) | exactly the 5 required columns |
| 完整合成填寫列及欄位解說 | 表18 (SYN-R01) + 表19/表20 blanks | met |
| 問題／例外—修正—覆核及追蹤 | 表16 (TABLE 19): 觸發問題｜立即修正｜覆核方式｜追蹤 | met |
| 官方要求—表單欄位—附件定位追溯表 | 表17 (TABLE 20): facets→專用欄位→判定→正文定位， anchored by P006 | met (observation below) |

Required fields (合成資料識別碼 / 日期+合成標示 / 角色代碼 / 來源與附件定位 / 判定-理由-覆核-後續) each trace to P033, P002/P005, P063+表15, 表20, 表15+表16. All 12 `required_sections` trace to document sections 一–十五 plus 附表； the twelve linked acceptance tests are each addressable (questionnaire+scale, SOP-free genre appropriately replaced by survey mechanics, worked sample, replacement ledger, recomputable formulas, neighbor rejection, 30-second cover, executable rows, sampling floor 6/2, hold criteria, no plagiarism claims).

## 8. Rejection/hold criteria — PASS

P071 lists seven concrete 退件條件 (empty-only questionnaires; missing denominators; purposive→market overreach; self-rating→capability claim; need not linked to task/objective/assessment; unauthorized formal decision; synthetic not marked/registered) that directly operationalize the blueprint's own acceptance conditions; 表16 handles live exceptions; 表15 enforces hold-before-authorization. No missing-content case is passed off as complete.

## 9. Distinctions from 0032 and 0034 — PASS

表1 (TABLE 2) and P005 explicitly exclude both neighbors: 0032/I06-E03 辦訓能力 not scored here; 0034/I07-E02 個人盤點 not replaced, self-rating confined to a planning signal (P025, P041, 表16, 行20). The body rejects both wrong neighbors via checkable differential fields — satisfying the negative-neighbor test — with no cross-document fact duplication (register `cross_document_refs` consistently "無共用案例事實").

## 10. Minor observations (non-blocking, with locators)

1. **Register granularity for two REAL-sourced citation details** — 表2 row 2 carries 「113年度法登他字第000069號」 and 「2024-06-24公告」/「2026-10-05讀回」， but F0033_LEGAL_NAME registers only the 法定名稱 value. Strictly the synthetic rule applies to SYNTHETIC items, so this is bookkeeping polish, not a violation.
2. **Two uncaptioned tables** — the 評分錨點 table (P051/TABLE 13) and 方案理由 table (P057/TABLE 15) lack 表 numbers, so register anchors F0033_SCORING_ANCHORS ("表12計分規則”) and F0033_方案*_RATIONALE ("方案理由”) describe rather than number them; doc's 表12 is the weighted-comparison table (TABLE 14). Minor locator drift; content agreement itself is verified.
3. **Register page fields (2–10)** cannot be confirmed from the text-level extraction provided (no page markers in the candidate dump) — recorded as unverifiable, not contradicted.
4. 表19 caption says「每項需求一列」while its structure is a field-list blank — cosmetic.
5. Style inconsistency: F0033_PRIORITY_RULE uses 「第八節」 vs 「第7節」 elsewhere in the register; engineering IDs (0033/I07-E01 etc.) appear in 表1/表2 — justified by the mandated neighbor-rejection test, but noting the “無內部術語” clause is only partially relaxed by necessity.

None of these affects arithmetic, requirement mapping, boundary control, or usability.

---

## Scope statement

This review covers text-semantic consistency only, within the supplied packet. It does **not** independently verify: the candidate or packet SHA-256 values, DOCX hashing, visual layout, font sizes (10.5/9.5pt), official acceptance of the PDF, or any REAL evidence status. The SAMPLE/REAL boundary claims above describe what the text itself declares and how consistently it does so; no REAL status is affirmed by this review.

**Final: PASS** — requirement/genre match exact (P006 ↔ page-2 指標7 bullet); all survey, SAMPLE, and Q07 mechanics verified; every formula recomputed correctly; synthetic facts comprehensively registered; all four required Blueprint table types present; hold criteria and both neighbor distinctions textually enforced. The five observations above are polish items, not defects requiring hold.