# Independent Semantic Review — 0133 / I19-E22 / R03 (text scope only)

## Verdict: **PARTIAL**

All arithmetic, counting rules, cross-year handling, exclusion of the canceled class, neighbor rejection, and SAMPLE/REAL controls check out exactly against the Blueprint and official page-8 text. Two localized blueprint-conformance defects in exception-table completeness (D1) and replacement-register coverage (D2) prevent PASS.

Scope note: I did not hash the DOCX, perform visual/font inspection, confirm official acceptance, or verify real association records. The Candidate SHA-256 `2b0f7a8d0c886f5a1b0cc09447b33e386c7328e376d6e36516ce30dacf5db68c` and page-8 SHA are taken as given, not recomputed. Every finding below is based solely on text comparison of the three exhibits in the packet.

---

## Check-by-check results

| # | Check | Result | Locators |
|---|-------|--------|----------|
| 1 | Document-specific purpose (dual series, per-adjacent-year, no substitution) | PASS | Blueprint §2 ↔ Candidate P005, P010, P017, P021, TABLE 9 rows 4–5, TABLE 17 row 3. Official sentence demands both 班次 and 人次 growth; candidate treats them as independent series throughout and forbids enrollment/seat-count/day-count/unique-person substitutions at P017. |
| 2 | Official quote and position | PASS | Page 8 excerpt places 「每年訓練班次、人次均持續成長。」in the 3分 常見參考佐證 list; P008 and Blueprint §1 both cite it as the 3分 item. No misattribution to 2分 or 4分 lists. |
| 3 | 24 classes / 317 person-times | PASS | TABLE 5: 2023 = SYN-23-01…06 (6), 2024 = SYN-24-01…08 (8), 2025 = SYN-25-01…10 (10) → 24. Person-times: 12×6=72; 13×8=104; 2025 sum 12+13+14+14+14+14+15+15+15+15=141. 72+104+141=**317** ✓ (stated at P030, TABLE 15 SYN-DERIVED-01). |
| 4 | Yearly counts & growth arithmetic | PASS | TABLE 6/7/8 vs Blueprint §3.3: (8−6)÷6=33.3%; (10−8)÷8=25.0%; (104−72)÷72=44.4%; (141−104)÷104=35.6% (37/104=35.5769→35.6, correct unrounded-then-1dp order per P021/P039); first-last 66.7% (4/6) and 95.8% (69/72=95.8333) correctly shown as supplement at P039, explicitly barred from replacing yearly judgment. 2023 base rows correctly N/A. |
| 5 | Cross-year rule & SYN-EX-05 | PASS | P013 mirrors Blueprint §3.1 (attribution to year of last substantive teaching activity; no splitting one class across two years; HOLD on conflicting REAL policy). TABLE 10 row SYN-EX-05: SYN-24-08 last teaching 2024-12-14 → 2024, closing year 2025, "測例不重複計入總數；SAMPLE 仍為 6/72、8/104、10/141" — no double counting, totals unchanged. Register row present at TABLE 15 (last row) with correct document locations (§2.1/§8). |
| 6 | No double counting | PASS | P015 (same cohort multi-day = 1 class), P017 (班次ID × 去識別學員ID dedup), P045 (SYN-LEARNER-014 two days = 1, second class = +1, labeled 人次 not unique persons), TABLE 4 steps 3–4, TABLE 9 rows 1–2, SYN-EX-01 (20→11) at TABLE 10/P048. Internally consistent — P048's 20→11 matches TABLE 10 SYN-EX-01. |
| 7 | Canceled classes | PASS | SYN-25-X01 (TABLE 5 last row): 取消, 0 (zero is a status marker, excluded from 141 since the 2025 sum already excludes it), kept in roster with source key SYN-PLAN-25-X01 (PLAN-only key — consistent: no ATT/CLOSE exists for a canceled class). P030, TABLE 10 SYN-EX-02 all agree. |
| 8 | Denominator & HOLD/REJECT rules | PASS with defect D1 | TABLE 2 (0/missing denominator → N/A, no ÷0), TABLE 6/7 (2023 N/A), P013 (policy conflict → HOLD), P018 (no policy → no formal conclusion), P021/P065 (no fabricated official threshold), TABLE 16 READY/HOLD/REJECT. Defect D1 below. |
| 9 | All synthetic dates & amounts registered | PASS with defect D2 | TABLE 15 registers all 24 held classes + X01 with date/status/person-times/source keys, plus SYN-DERIVED-01 (6/72, 8/104, 10/141, 24, 317), SYN-RATE-01 (all six percentages), SYN-ROLE-01, SYN-EX-01, SYN-EX-05. All 25 dates are valid calendar dates and match Blueprint §4 row-for-row (2023: 02-11/04-15/06-10/08-12/10-14/12-09; 2024: 02-17/03-23/05-18/06-22/08-17/09-21/11-16/12-14; 2025: 01-18/02-22/04-12/05-17/06-21/07-19/08-23/09-20/10-18/12-06; cancel 11-22). Defect D2 below. |
| 10 | SAMPLE vs REAL | PASS | P002, P005 ("只驗證本表可用及可重算"), P028, P030 ("全為 SYNTHETIC"), TABLE 1 (SAMPLE/SYNTHETIC, REAL_EVIDENCE=UNKNOWN, 官方印刷方框序號 UNKNOWN), P059 ("不得直接將 SYNTHETIC 數值換標籤"), TABLE 16 REJECT row includes "SAMPLE 被冒充 REAL". Consistent throughout; no REAL claim anywhere. |
| 11 | Rejection of 0132 and 0134 | PASS | P010 and TABLE 17: 0132/I19-E21 excluded via no product/defect/受檢單位/不良率分子分母; 0134/I19-E23 excluded via no 會員名冊/會費/收入. Consistent with Blueprint §2. The candidate's own data set (classes, person-times, growth rates) contains nothing from either neighbor's domain; title-blind identification survives via per-class run IDs, dual annual series, and adjacent-year recomputation. |

---

## Defects (with exact locators)

**D1 — TABLE 10 (§8, P047) covers only 5 of the 9 exception scenarios enumerated in Blueprint §5 item 8; 漏結案 has no HOLD/REJECT treatment anywhere.**
- Blueprint §5 item 8 mandates the exception judgment table for: 取消、延期、零出席、跨年、缺名冊、同班多日重複計算、重複 ID、漏結案、政策改變。
- TABLE 10 has dedicated rows only for: 同班多日重複 (SYN-EX-01), 取消 (SYN-EX-02), 缺名冊/名冊簽到不一致 (SYN-EX-03), 政策改變 (SYN-EX-04), 跨年 (SYN-EX-05).
- 延期 and 零出席 appear only in prose/SOP (P015; TABLE 4 step 2; TABLE 9 row 4; TABLE 16) — not as exception-判定 rows. 重複 ID appears only in TABLE 4 step 3. **漏結案** (a class with mismatching or missing closing instructional record) appears nowhere as a named HOLD/REJECT trigger: P015 requires tracing to 結案 or equivalent attendance data, but TABLE 16's HOLD list (“只有報名或彙總；缺年度或來源；名冊與簽到不一致；…”) never addresses it. This leaves a real-world data condition — the missing class-closing record — without an explicit disposition. Reasoning: this is a direct enumeration deviation from Blueprint §5 item 8, and a genuine gap in the BLOCK hold/reject rules (relevant to review check #8), not merely stylistic.

**D2 — TABLE 15 (§10) omits register rows for synthetic keys introduced at P045 and P048.**
- P045 introduces SYN-LEARNER-014, SYN-CLASS-A, SYN-CLASS-B (dedup example, and note their class-ID format differs from the SYN-23-01 series) and P048 introduces the correction record key SYN-0133-CORR-01 with roles SYN-ROLE-REG/SYN-ROLE-REV and the 20→11 figure.
- The register (Blueprint §5 item 11 requires per-fact replacement location for “…來源 ID…角色與更正”) registers the 20→11 correction *principle* via SYN-EX-01 and the role replacement via SYN-ROLE-01, but never itemizes SYN-0133-CORR-01, SYN-LEARNER-014, or SYN-CLASS-A/B. These are correctly marked SYNTHETIC in text (so the §7 prohibition is satisfied), but the workbook is not fully per-fact for them. Severity: minor; no numeric totals are affected.

**Non-defect cross-checks (verified, no action):** SYN-EX-05's document locations (§2.1; §8) match actual content (P013, TABLE 10); TABLE 15's 24 class rows match TABLE 5 row-for-row; the P048 correction example does not conflict with TABLE 10 SYN-EX-01; the three near-neighbor IDs (I19-E21/E22/E23) are consistently mapped across P001, P010, TABLE 17, and Blueprint §2.

---

## Summary

- **PASS** items: purposes and official quote placement (1, 2), all totals and every growth percentage recomputed exactly (3, 4), cross-year/SYN-EX-05 semantics (5), dedup (6), cancellation (7), registration of all material synthetic facts (9, with D2 as gap), SAMPLE/REAL discipline (10), neighbor exclusion (11).
- **PARTIAL driver:** D1 (TABLE 10 missing 延期/零出席/重複 ID rows; 漏結案 unaddressed in any HOLD/REJECT rule) — a concrete deviation from Blueprint §5 item 8 and a usability/hold-rule gap; D2 register omissions are secondary.

**Recommended disposition for the Builder:** add four exception rows (延期、零出席、重複 ID、漏結案) to TABLE 10 with HOLD/REJECT judgments and leave-trail operations, add an explicit HOLD trigger for 漏結案 to TABLE 16, and extend TABLE 15 with rows for SYN-0133-CORR-01 and the P045 dedup-example keys. These are additive text edits; no totals, formulas, or SAMPLE/REAL statements need to change.

Items outside this review's text scope, per instructions and honestly unverified: DOCX hashing, ≥10.5pt/≥9.5pt visual acceptance (Blueprint §7 final items), official acceptance, and real-association evidence.