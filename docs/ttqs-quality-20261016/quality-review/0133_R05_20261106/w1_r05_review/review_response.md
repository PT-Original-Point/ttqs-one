# Independent Semantic Review — TTQS 0133 / I19-E22 / R05

## Verdict: **PASS** (text-scope semantic review)

All in-scope semantic checks against page 8, the unique Blueprint, and the extracted candidate pass. Defects found: none blocking. Two unverifiable-outside-scope items and one minor observation are listed at the end.

**Scope declaration (per instructions):** This review is text-only. I do **not** claim independent hashing of any file, visual inspection, font/point-size verification, official acceptance status, or association-side evidence. The candidate SHA-256 value in the prompt (`7f9cf468…78eb6e`) was compared as a string against the packet header (`full_semantic_packet.md`, line 1) — **the two strings match exactly (text comparison only, not a computed hash)**. The page-8 excerpt SHA is as stated in the packet header and was not recomputed.

---

## 1. Document-specific purpose ✓
- Official sentence confirmed verbatim in the page-8 excerpt, and confirmed as sitting under **「3 分之常見參考佐證資料」** — matches Blueprint §1 and candidate P008.
- Purpose correctly narrowed to the dual annual series (classes + person-times) with adjacent-year comparison: P004, P005, P010, TABLE 1 row 本件文類.
- Blind-test condition (Blueprint §2 “移除標題後仍可辨認”)： the body independently identifies the item via per-class IDs (TABLE 5), status field, class×learner dedup rule (P017, P045, TABLE 9), dual annual series (TABLE 6/7), and adjacent-year recomputation (TABLE 8). ✓

## 2. Negative neighbors 0132 / 0134 ✓
- Boundary statement P010; exclusion table TABLE 17 (0132/I19-E21: no product/defect/inspection denominators; 0134/I19-E23: no member rosters, fee ledgers, or income figures); register §12/P066–P068. Matches Blueprint §2. No neighbor content leaked into TABLE 5 or the totals.

## 3. Complete, usable sample — 24 classes / 317 person-times ✓
Arithmetic recomputed row-by-row from **TABLE 5**:
- 2023: 6 rows × 12 = **72** ✓ (matches P030, TABLE 7)
- 2024: 8 rows × 13 = **104** ✓
- 2025: 12+13+14+14+14+14+15+15+15+15 = **141** ✓
- Classes: 6+8+10 = **24 已辦** ✓; totals 72+104+141 = **317** ✓ (P030, SYN-DERIVED-01 in TABLE 15)
- Canceled row SYN-25-X01 (取消， 0 人次) present but excluded from both totals ✓, consistent with P030, TABLE 9 row 4, and SYN-EX-02 (TABLE 10).
- Usable-as-demo requirement (Blueprint §5 item 10 "at least one fully filled demonstration") is met by TABLE 5 + TABLE 6/7/8; the §9 templates are intentionally blank/HOLD with explicit warning P051 — correct behavior, not a defect.

## 4. Yearly counts and growth arithmetic ✓ (recomputed independently)
| Check | Recomputed | Stated | Locator |
|---|---|---|---|
| (8−6)÷6 | 33.33→33.3% | 33.3% | TABLE 6, TABLE 8, P039 |
| (104−72)÷72 | 44.44→44.4% | 44.4% | TABLE 7, TABLE 8, P039 |
| (10−8)÷8 | 25.0% | 25.0% | TABLE 6, TABLE 8, P039 |
| (141−104)÷104 | 35.577→**35.6%** | 35.6% | TABLE 7, TABLE 8, P039 |
| 首尾 (10−6)÷6 | 66.67→66.7% | 66.7% | P039, TABLE 15 SYN-RATE-01 |
| 首尾 (141−72)÷72 | 95.833→95.8% | 95.8% | P039, TABLE 15 SYN-RATE-01 |

Net increments (+2/+32/+2/+37) all correct in TABLE 6/7. Unrounded-then-1-decimal rule (Blueprint §3.3) stated at P021 and honored. Crucially, P039 correctly labels first–last as supplementary only, and TABLE 9 row 5 rejects first–last-only substitution.

## 5. Cross-year rule and SYN-EX-05 ✓
- Rule (assign to year of last substantive teaching activity; never split one class across two years): Blueprint §3.1 = P013 verbatim-consistent.
- SYN-EX-05 (TABLE 10, registered TABLE 15): SYN-24-08 last teaching day 2024-12-14, closure year 2025 → default 2024, HOLD if REAL policy differs, and explicitly **“不重複計入總數；SAMPLE 仍為 6/72、8/104、10/141”** — no double count, totals invariant. Date 2024-12-14 in TABLE 5 matches. Exemplar discipline correct.

## 6. No double count ✓
- Class-level dedup: P015 (same cohort multi-day = one class), TABLE 9 row 1, TABLE 3 班次 ID row.
- Person-level dedup: P017 (班次 ID × 去識別學員 ID， ≥1 attendance = 1 人次)， TABLE 9 row 2, §4 example SYN-LEARNER-014/SYN-CLASS-A/B (P045, registered TABLE 15).
- SYN-EX-01's 20→11 correction is explicitly **“示例不併年度數”** (TABLE 15) and P030 totals are decoupled — no contamination of 317.

## 7. Canceled classes ✓
- Definition and exclusion: P015, TABLE 9 row 4, TABLE 4 step 1–2, SYN-EX-02 (TABLE 10), the X01 row itself. Exclusion ledger with reason requirement present. Blue criterion “取消班未算” satisfied.

## 8. Denominator and HOLD/REJECT rules ✓
- TABLE 2: N/A on zero/missing prior-year denominator, no division by zero — matches Blueprint §3.3; echoed P021, TABLE 4 step 6.
- HOLD/REJECT/READY conditions in TABLE 16 match Blueprint §6 item-for-item, including REJECT triggers (course-days as classes, daily sign-in sums as person-times, cancellations counted, first–last masking an interim decline, formula inconsistency, stripped SAMPLE tags) and the no-invented-threshold rule (P021, P065).

## 9. Synthetic dates/amounts fully registered ✓
- TABLE 15 registers all 25 class rows with their fact groups (date, ID, course name, status, count, source keys), plus SYN-DERIVED-01 (totals), SYN-RATE-01 (exact rate list including both first–last figures — matches P039), SYN-ROLE-01, SYN-EX-01, SYN-EX-05, student/class demo keys, SYN-0133-CORR-01, SYN-0133-CASE-01. All dates in TABLE 5 fall within their stated years; no date omission found.
- Every synthetic value in P005/P030/P039 has a register entry. No unregistered synthetic fact found.

## 10. SAMPLE versus REAL separation ✓
- P002, TABLE 1 本版狀態 (REAL_EVIDENCE=UNKNOWN), P005 (“不是原始點協會的實績…”), P018 (counting method is a demo definition, not policy), P028, P030, P038, P042, P059 (no relabeling SYNTHETIC→REAL), P065. No claim of actual association performance, policy approval, or acceptance anywhere in the candidate. Blueprint §7 禁止事項 honored.

## 11. 0132/0134 rejection — see §2 above ✓

---

## Out-of-scope items (flagged as **not assessable**, not defects)
1. **TABLE 15 page locators** (§5/p4, /p5, §10/p9–p10, §6/p6, §3/p3, §2.1, §8/p8): the extraction is P-indexed with no page markers, so pagination cannot be confirmed in text scope. Internal section references (§2.1, §5, §8, §10) do map to the correct candidate sections.
2. **Blueprint acceptance items requiring visual/Word checks** (正文≥10.5pt、表格≥9.5pt、全頁視覺驗收) and **independent exact-SHA verification**: outside this review's declared text scope and therefore neither credited nor debited.
3. Minor observation (non-blocking): P048/TABLE 10 SYN-EX-01 states “20 筆日簽到去重為 11” without the day-by-day split. The result is arithmetically feasible (e.g., 10+10 daily counts with 9 common learners → 11 distinct) and the example is explicitly excluded from annual totals, but a reader cannot independently recompute 11 from the stated facts alone. Registering the daily split would make the demo airtight; this does not affect the verdict.

**Final: PASS — no semantic defects located against the Blueprint's text-verifiable acceptance criteria.**