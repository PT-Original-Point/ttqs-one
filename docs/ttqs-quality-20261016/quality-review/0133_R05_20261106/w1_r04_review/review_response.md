# Independent Semantic Review — TTQS 0133｜I19-E22｜R04

**Scope discipline honored:** text-only review of the provided packet (official page-8 extract, Blueprint, extracted candidate text, register). I verified no hash, performed no visual inspection, and claim no official acceptance or association evidence. SHA values on both sides are taken as stated identifiers, not independently computed.

---

## VERDICT: **PASS**

All arithmetic, counting-rule, SAMPLE/REAL discipline, and neighbor-exclusion checks pass on text scope. One minor, non-blocking traceability deviation is noted below.

---

## 1. Document-specific purpose

| Check | Locator | Result |
|---|---|---|
| Official sentence correctly identified | Candidate P008 = 「每年訓練班次、人次均持續成長。」, attributed to PDF p.8, 3分常見參考佐證 | ✅ Matches official extract verbatim (page 8, 3分 column: 「每年訓練班次、人次均持續成 長。」) |
| Dual-series purpose (班次 AND 人次, not one substituting the other) | P004, P010, §2.2/§2.3 (P015/P017), TABLE 1 row 5 | ✅ Both indicators defined separately; P010 explicitly forbids substituting one for the other |
| No collateral metrics imported | P010 (excludes 證照/就業/會費/產品 data), TABLE 17 | ✅ Matches Blueprint §2 prohibition |
| Official numbering discipline | TABLE 1: 0133 = internal doc_id, I19-E22 = crosswalk ID, official box serial = UNKNOWN; index 146 not used as official serial | ✅ Complies with Blueprint §1/§7 |
| Blind title test | Title P000; body carries per-class run keys (SYN-23-01…SYN-25-X01), 狀態 column, 班次×學員 dedup rule (P017, TABLE 9 row 2), dual year series (TABLE 6/TABLE 7), adjacent-year formulas (TABLE 8) | ✅ Passes |

## 2. Complete, usable sample — 24 classes, 317 person-times

**Row-by-row recount of TABLE 5 (25 data rows = 24 已辦 + 1 取消):**
- 2023: rows SYN-23-01…06, 6 classes, person-times 12×6 = **72** ✅
- 2024: rows SYN-24-01…08, 8 classes, person-times 13×8 = **104** ✅
- 2025 已辦: rows SYN-25-01…10, 10 classes; person-times 12+13+14+14+14+14+15+15+15+15 = **141** ✅
- Totals: 6+8+10 = **24 已辦班次** ✅; 72+104+141 = **317 人次** ✅
- Totals asserted consistently at P030 and register SYN-DERIVED-01 (§6/p6; §10/p10) ✅
- All dates fall inside their stated calendar year (earliest 2023-02-11, latest 已辦 2025-12-06; cancel case 2025-11-22) ✅

## 3. Yearly counts and growth arithmetic (independently recomputed)

| Check | Recomputed | Candidate | Locator | Result |
|---|---|---|---|---|
| 2024 vs 2023 班次 | (8−6)÷6×100 = 33.33…% | 33.3% | TABLE 6 row 2024; TABLE 8 row 1; P005; P039 | ✅ |
| 2025 vs 2024 班次 | (10−8)÷8×100 = 25.0% | 25.0% | TABLE 6 row 2025; TABLE 8 row 2 | ✅ |
| 2024 vs 2023 人次 | (104−72)÷72×100 = 44.44…% | 44.4% | TABLE 7 row 2024; TABLE 8 row 3 | ✅ |
| 2025 vs 2024 人次 | (141−104)÷104×100 = 35.576…% | 35.6% | TABLE 7 row 2025; TABLE 8 row 4 | ✅ |
| Net increments listed separately | +2/+2 classes; +32/+37 person-times | matches | TABLE 6, TABLE 7 (淨增量 column) | ✅ Blueprint §3.3 requirement met |
| First–last supplementary | (10−6)÷6 = 66.7%; (141−72)÷72 = 95.833…% | 66.7% / 95.8% | P039 | ✅ Correctly labeled as non-substitutable for year-by-year (same row and P021) |
| Denominator/zero rule | 前年 0 或缺漏 → N/A, no division by zero | implemented | TABLE 2; TABLE 6/7 row 2023 (N/A); TABLE 4 step 6 | ✅ |
| Rounding discipline | unrounded computation, 1-decimal display, integers for counts | stated and observed | P021; P039 | ✅ |
| No invented official threshold | repeated twice | — | P021; P065 | ✅ Blueprint §6 prohibition met |

## 4. Cross-year rule and SYN-EX-05

- Rule stated: assignment to the last year with substantive teaching activity; no splitting one class across two years — P013, matching Blueprint §3.1.
- **SYN-EX-05 consistency check:** TABLE 5 places SYN-24-08 at 2024-12-14 within year 2024; TABLE 10 SYN-EX-05 and TABLE 15 SYN-EX-05 state closing year 2025, default assignment 2024, HOLD trigger if a conflicting REAL policy exists, and “SAMPLE 仍為 6/72、8/104、10/141." ✅ Internally coherent, no reclassification, totals unchanged.
- Anti-gaming clause “規則固定後不得為製造成長而改變" present at P013. ✅

## 5. No double counting; canceled class

- Canceled class SYN-25-X01: status 取消, 0 person-times, explicitly excluded from totals — TABLE 5 last row; P030; TABLE 10 SYN-EX-02; register SYN-25-X01 (§5/p5; §8/p8; §10/p10). ✅ (6/72, 8/104, 10/141 confirm exclusion.)
- Per-class per-person dedup: 班次 ID × 去識別學員 ID, multi-day = 1 人次 — P017, TABLE 3 row 6, TABLE 4 step 4, TABLE 9 row 2; worked example P045 (SYN-LEARNER-014/SYN-CLASS-A/B, declared “不併入前述年度總計"). ✅
- Error-scenario integrity: SYN-EX-01 (20 daily sign-ins → 11 dedup associations) is fenced off as a demonstration ("示例不併年度數," TABLE 15; P048), consistent with the 317 total. ✅ No leakage into totals found anywhere.

## 6. Denominator and HOLD/REJECT rules

- TABLE 6/7 include explicit 前年 and N/A rows for base year 2023. ✅
- HOLD triggers enumerated (roster/sign-in mismatch, status ambiguity, missing closing, registration-only counts, unremoved duplicates): TABLE 16 HOLD row; P023; P051; SYN-EX-03/EX-04; 規則：延期/零出席/重複 ID/漏結案 rows of TABLE 10. ✅
- REJECT triggers (days-as-classes, daily sign-ins as person-times, registrations as person-times, canceled counted, first-last masking, formula mismatch, SAMPLE-as-REAL): TABLE 16 REJECT row; TABLE 9; P049 (no untraceable overwrites). ✅
- Corrupt-value correction loop demonstrated with full audit fields (P048, P049; SYN-0133-CORR-01). ✅

## 7. All synthetic dates and amounts registered

TABLE 15 covers all 24 held classes + SYN-25-X01 (25 rows, each with year/ID/date/course/status/person-times/source-key fact-set and REAL replacement source type), plus derived totals (SYN-DERIVED-01), rates (SYN-RATE-01, all six percentages enumerated), roles (SYN-ROLE-01), both exercised exceptions (SYN-EX-01; SYN-EX-05), learner/class keys, and correction key. Register locator page attributions (§5/p4–p5, §10/p9–p10) are internally consistent with the row-block structure. ✅ **Complete.**

## 8. SAMPLE vs REAL discipline

- Synthetic status declared at P002, P005, P028, P030 ("全為 SYNTHETIC"), P065 ("REAL…皆為 UNKNOWN"). ✅
- REAL replacement area explicitly unfilled and blank templates marked 待補/UNKNOWN/HOLD, not construed as completion: P051, P059, TABLES 11–14. ✅
- No statement anywhere claims association performance, approved policy (P018 disclaims), official threshold, or evaluation outcome (P008, P038, P042 disclaim). ✅
- No invented signatures; P048/P049 and TABLE 15 SYN-ROLE-01 forbid fabricated sign-offs. ✅

## 9. Rejection of 0132 and 0134

- Boundary statement P010; neighbor table TABLE 17 with per-neighbor exclusion mechanisms; 0133 row ties mechanism to doc-specific features (逐班狀態、班次去重、班次×學員去重、雙序列、相鄰年度計算). ✅ matches Blueprint §7 acceptance item.

---

## DEFECT (minor, 1 item)

**D-1 — Missing case identifier `SYN-0133-CASE-01`.**
- Locator: Candidate §5 (P027–P030) and §10 TABLE 15 — the identifier appears nowhere in the candidate text (only SYN-0133-CORR-01 exists, at P048 and TABLE 15 last block).
- Blueprint §4 specifies 「案例 ID：`SYN-0133-CASE-01`」 as the named synthetic case package.
- Reasoning: the case content itself (years, totals, cancel exception, table) is fully implemented; only the designated package label is absent, reducing cross-reference traceability between the Blueprint spec and the candidate. It does not affect any total, rate, dedup outcome, or misstatement risk, and it is not among the Blueprint §7 acceptance items — hence non-blocking.

## Observations (not defects)

1. **Table-to-flow placement:** the packet extraction lists TABLE 1–18 as a block after P068, so exact physical table positions (e.g., TABLE 9 relative to the §6/§7 boundary at P043) cannot be pinned from text scope; register §-locators were used where available. This is an extraction limitation, not a content error.
2. **字級/視覺驗收 (Blueprint §7: 正文≥10.5pt、表格≥9.5pt、全頁視覺)：** unverifiable in text scope — excluded from this verdict, not certified.
3. **版本/附件來源** (Blueprint §5 item 12): covered via TABLE 18 (sources), TABLE 12 (口径版次), P049 (lock/versioning); adequate, though no single explicit "attachment version" field exists.

---

**Summary:** Document-specific purpose ✅, complete usable sample (24/317, row-verified) ✅, all six growth computations independently reproduced ✅, cross-year rule + SYN-EX-05 coherent ✅, no double counting ✅, canceled class excluded ✅, denominator/HOLD/REJECT rules ✅, register complete ✅, SAMPLE/REAL discipline ✅, 0132/0134 excluded ✅. **PASS**, subject to minor defect D-1.