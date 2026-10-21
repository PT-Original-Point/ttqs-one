# Independent semantic & usability review — DOCX 0104 / I18-E11 / R15

## Verdict: **PARTIAL**

Zero blocking defects remain — all five R14 blockers are **verified fixed in R15 text (not presumed)**, and every number was independently recomputed correct. PARTIAL instead of PASS because (1) one R14 nonblocking finding is verifiably still open (T-13 priority labels), (2) register completeness — an explicit review criterion — is incomplete at three points, (3) three locator defects remain. No residual item changes any figure, denominator, boundary, or conclusion.

### Evidence binding (read-only; no files edited)
- `candidate\0104__證照獲取率_分析報告_R15.docx` recomputed SHA-256 = `9bbb96da74ba9da845ab0e063421d04f035e79496209a02de1f04b0c98ec7eb8`, bytes = **85599** — matches the packet binding exactly.
- In-memory text check of that same file's `word/document.xml`: `<w:tbl>` count = **31** (matches "all 31 tables"); present: `209/384`, `54.427083`, `F-RC-04`, `N/A（P1=0）`, `規範性保留中`, `3 年`; **absent: `54.4358`, `6.94`, `I18-E12`**.
- R14 receipt file re-hashed: bytes 46976, sha `928d17fdf4ddc389c0223a3259060a7eefdc9ce4a34c992f20f6af2728084178` — matches receipt (evidence of prior run only).

---

## 1. R14 → R15 finding-by-finding verification

| # | R14 finding (packet line 6) | Verdict | Exact R15 locator + evidence |
|---|---|---|---|
| B1 | T14 C rate wrongly shown 0.00% (zero denominator) | **FIXED** | §13 表 T-14 (extract [TABLE 16]) row「乘法鏈 = 取證率」, C cell = `N/A（P1=0）`. No standalone `0.00%` cell exists anywhere; C cells in that table are integer counts (`0 ✓`), T-12/T-13 have no C column. |
| B2 | T19 C counts contradicted C=0 | **FIXED** | §18 表 T-19 ([TABLE 22]) column「示例數（A／B／C）」: `8/3/0`, `3/2/0`, `7/5/0`, `2/1/0`, `1/1/0`, `3/1/0`, `0/0/0`, `0/0/0` — every C entry = 0; consistent with T-10 C column P1–P11 all 0 and F-PC-01…11 = 0. |
| B3 | Missing C-4 register key | **FIXED** | §19.4 [TABLE 26] and CSV: `F-RC-04,N/A,簽發查證完成率,§11.3/C-4；T-18 G9,0/0 重算,品保,S` (also confirmed present in the hash-bound DOCX XML). |
| B4 | D-0 hold mixed with executed results; no register key | **FIXED** | §16 preamble:「D-1 至 D-5 的『結果』欄均為『未執行（示範）』。D-0 是規範性發布保留狀態，不代表真實決議或已發生執行。」; T-16 D-0 row 結果 =「規範性保留中（非執行結果）」; keys **F-DS-06** (decision) and **F-RS-01** (result/status split) exist in [TABLE 26] + CSV. |
| B5 | First-page navigation wrong | **FIXED (text level)** | §1「三十秒讀法」→ §7 (21 項; U01–U21 = exactly 21) → 表 T-13 (§12 差距優先排序矩陣 = "哪一段缺口最大" ✓) → 表 T-16 (§16 決策/責任/期限 = "誰在什麼時候做什麼" ✓). All three targets resolve correctly. Physical first-page placement **not verifiable** (no visual evidence) — limitation L1. |
| N1 | Five missing zero-denominator rates in G9 | **FIXED** | §18 T-18 row **G9** 狀態 lists exactly five:「C期申請率、到考率、通過率、簽發查證完成率、已驗證取證率均觸發（示範）」; corroborated at §11.3 C-1…C-5 (all `N/A`), T-14 C cell `N/A（P1=0）`, register **F-RC-01…05** (5 keys). |
| N2 | Derived rate register coverage | **SUBSTANTIALLY FIXED, gaps remain** | Added and counted: F-RAGG-01…06, F-RSPL-01…05, F-RD-01…06, F-GP-01…05. Gaps: see RF-2/RF-3/RF-4 below. |
| N3 | T14 aggregate ratios | **FIXED** | §13 narrative under T-14 gives six: `65/76=85.53%、60/65=92.31%、48/60=80.00%、43/48=89.58%、43/76=56.58%、48/76=63.16%` — all six independently recomputed correct (§4 below); registered F-RAGG-01…06. |
| N4 | Ambiguous relative change vs percentage points | **FIXED** | §8:「相對變化率定義為 (B−A)÷A×100%…百分點差是 B−A，不得與相對變化率混用」; T-12 separates「百分點差」/「相對變化」columns; §12 uses「個百分點」; F-RD-01…06 store「+…pp；+…%」; [TABLE 4] row「計算單位」pre-documents the ±0.01 display rule (material at 簽發查證完成率: exact 5.9441 → `+5.94` although displayed cells subtract to 5.95 — correct as stated). |
| N5 | Priority label collision | **NOT FIXED** | §12 表 T-13 ([TABLE 15]) 排序 column = `1, 1, 2, 3, 3, —` (duplicates) with **no tie rule stated**; label order does not follow descending gap (−5.00 pp row labeled 2 sits below −3.64 pp row labeled 1); register F-GP-02 locator says「T-13 row 2」while that physical row's 排序 label is **1** → label/locator mismatch. See RF-1. |
| N6 | Locators | **MOSTLY FIXED, 3 residual defects** | Fixed: §19 defines定位語法 (`T-10/P5/A`, `§11.1/A-5`, `§16/D-1`); all 121 register rows carry 定位; §24 index ([TABLE 30], 19 rows) all resolve correctly (counts verified: §7=21, T-18=10 gates, T-19=8 exceptions, §21=12 steps, §22=15 items, §8=6 indicators). Residual: RF-5, RF-6, RF-7. |

**Blocking findings: 5/5 verified fixed. Nonblocking: 3/6 fully fixed, 1 substantially fixed with gaps, 2 not fixed/incomplete.**

---

## 2. Disputed arithmetic — independent recomputation (exact)

Dispute: alleged "step 1 = 627/1152 = 54.4358%, +6.94 pp".

- §11.4 step 1 = (33/36)×(29/32)×(22/29)×(19/22). Cancelling (29 and 22): = (11/12)×(19/32) = **209/384** = 0.5442708333… = **54.427083…%** → displayed **54.43%** ✓.
- The allegation's own fraction is *identical*: 627/1152 = (627÷3)/(1152÷3) = 209/384 → **54.427083%**, so the alleged **54.4358% is an arithmetic error**, not a discrepancy with the report.
- Delta vs A: 54.4270833 − 47.50 = **6.927083… pp → +6.93 pp** ✓ (allegation's `+6.94 pp` is wrong).
- The strings `54.4358` and `6.94` do not occur in the hash-bound DOCX (verified) — the report does not carry the error.

**Full independent recomputation (all match the document):**

*Cohort rates* — A ([TABLE 10]/§11.1): 32/40=80.00% ✓; 29/32=0.906250→90.63% ✓; 22/29=0.7586207→75.86% ✓; 19/22=0.8636364→86.36% ✓; 19/40=47.50% ✓; 22/40=55.00% ✓; A-7 chain = 19/40 = 47.50% ✓. B ([TABLE 11]/§11.2): 33/36→91.67% ✓; 31/33→93.94% ✓; 26/31=0.8387097→83.87% ✓; 24/26→92.31% ✓; 24/36→66.67% ✓; 26/36→72.22% ✓; B-7 chain = 24/36 ✓. C ([TABLE 12]): 0/0 → N/A for all five + reason UNKNOWN ✓.

*T-12 ([TABLE 14]) pp and relative* — 申請 11/60=+11.67 pp, 7/48=+14.58% ✓; 到考 35/1056=+3.31 pp, 35/957=+3.66% ✓; 通過 72/899=+8.01 pp, 72/682=+10.56% ✓; 簽發查證 34/572=+5.94 pp, 34/494=+6.88% ✓; 取證 23/120=+19.17 pp, 23/57=+40.35% ✓; 通過產出 31/180=+17.22 pp, 62/198=+31.31% ✓. Threshold judgments (≥85/90/75/90/60) vs A/B values all consistent ✓.

*§11.4 substitution ([TABLE 13])* — cumulative exact: step1 **209/384=54.4270833%**→54.43 ✓; step2 589/1044=56.4176245%→56.42 ✓; step3 494/792=62.3737374%→62.37 ✓; step4 24/36=66.6666667%→66.67 ✓. Increments from exact values: +6.9271→**+6.93**, +1.9905→+1.99, +5.9561→+5.96, +4.2929→+4.29 (sum **+19.17** = 66.67−47.50 ✓). Shares: 36.1413→36.14, 10.3854→10.39, 31.0754→31.08, 22.3979→22.40; displayed sum **100.01%** — correctly labeled 四捨五入差 0.01 ✓. Order-dependence caveat (§11.4) correct ✓.

*T-14 identities ([TABLE 16])* — A: 32+8=40 ✓, 29+3=32 ✓, 22+7=29 ✓, 19+2+1=22 ✓; B: 33+3=36 ✓, 31+2=33 ✓, 26+5=31 ✓, 24+1+1=26 ✓; C: 0=0 ✓; totals 76/65/60/48/43 ✓; 失聯 A 2+1=3, B 1, total 4 ✓ (matches T-10 P11 note and T-19). Chain row A/B ✓, C `N/A（P1=0）` ✓.

*T-13 gaps ([TABLE 15])* — −12.50 pp & 5 人 (24/40 needed, 24−19=5) ✓; −3.64 pp & 1 件 (ceil 19.8=20, 20−19=1) ✓; −5.00 pp & 2 人 (34/40, 34−32=2) ✓; +0.63 (0.90625−0.90=0.625) ✓; +0.86 (0.758621−0.75) ✓.

*Dates* — 2026-06-27 + 90 d = **2026-09-25** ✓; D-1 +14 = 2026-10-09 ✓; D-2 = 10-23 ✓; D-3 = 10-30 ✓; D-4 = 11-06 ✓; D-5 = cutoff+49 = 11-13 ✓ — all match §16 期限計算說明 and F-DT-10…14.

*Aggregate narrative §13* — all six verified ✓ (see N3).

---

## 3. Criterion-by-criterion (with locators)

**Identity & official text — PASS.** Header:「文件編號 0104　評核項目 I18-E11　官方佐證項次 112」matches packet identity, crosswalk row `I18-E11,1,0,0104,證照獲取率_分析報告`, and Blueprint (genre/`final_filename`); [TABLE 31] 文件 row consistent. §2.1 quotes「證照獲取率。」with「列印頁 7」verbatim against SOURCE_PACKET/page-7 extract; correctly frames it inside the 4分 example list (with「指導學員參加技能競賽獲獎。」「感謝函。」), states the list is not achievement evidence, cites 3分「高證照通過率之證明資料。」and the truncated 1分 fragment explicitly marked truncated — no over-claim, no rewritten official text.

**Unique requirement identity vs neighbors — PASS with one limitation.** §20 表 T-20 ([TABLE 27]) rejects three documented neighbors with checkable fields: 0103/**I18-E10** (§8 denominator P1, no letter fields in §19), 0105/**I18-E13** (§8 numerator, §18 G6), 0102/**I18-E09** (five-condition rule); reinforced at §2.2 and §25.1 item 5. ✅ E10. ⚠️ **`I18-E12` does not exist anywhere in the packet or in the hash-bound DOCX** (grep + XML check); the packet's documented neighbors are E10/E13/E09. I therefore did **not** verify against E12 and invent nothing about it — see limitation L2.

**Title-blind identification — PASS.** With title/filename/number masked: §1 opening sentence (報名→到考→通過→簽發查驗 with denominators), §2.1 official phrase+page, §3 P1–P5, §8 formulas, §9 four-segment chain, §11 steps, and T-17 R-6 (evidence locus §8+§11+T-10 P5) uniquely identify a certificate-acquisition-rate analysis; §2.2/T-20 actively refuse re-use for E10/E13/E09 work-products (Blueprint failure condition not triggered).

**Definitions/populations/denominators/formulas — PASS.** T-03 five populations with denominators; [TABLE 7] six formulas each with zero-denominator `N/A` and misuse column; matches SOURCE_PACKET's four required rates (P2/P1, P3/P2, P4/P3, P5/P1) and keeps pass yield separate (P4/P1, §8「不得簡稱取證率」); §3 identity chain + exclusion rules; T-10 P6–P11 and T-19's 8 exception classes show non-applicants, no-shows, failed, uncontactable, pending, missing evidence (缺件/缺漏), unverifiable, overdue separately.

**Five zero-denominator rates — PASS (4 loci consistent):** §11.3 C-1…C-5 all `N/A`; T-14 C `N/A（P1=0）`; T-18 G9 lists all five; F-RC-01…05. No `0.00%` denominator-zero display exists (verified).

**SAMPLE/REAL boundary & no fabrication — PASS.** §7: all 21 U-items `UNKNOWN`, with「尚不可計算」≠「取證率為 0」(unknown never converted to zero); §10 declaration of fictional demonstration; §14 synthetic data excluded from grading, REAL = E0 (also T-17 R-7, §25.1); §16 D-1…D-5 = 未執行（示範）, D-0 hold; all release boxes in §25.2 unchecked `[ ]` → **no approval claimed**; no personal names (T-05 `reviewer` = role code), no certificate numbers (§6.2), no signatures (§6.7, §23, T-17 R-11), provider/exam labeled 示例/虛構 (F-PV-01/02), every synthetic value status `S`. All thresholds carry「所有門檻均為 `SAMPLE—待協會核定`」(§12) + T-12 header「SAMPLE 門檻」+ F-RT-01…05 (替換來源「協會核定」). No causal claim (§15「不行」, §12, §25.3).

**Limitations & operational actions — PASS.** §14 upgrade gaps, §15 T-15, §16 T-16 (roles/dates/tracking), §21 12-step SOP ([TABLE 28]), §22 C01–C15 covering every packet-required REAL item (roster, eligibility decision, enrollment/attendance, result notice, issue/verify sources, reconciliation, privacy, cutoff, exact numerator/denominator, independent verifier + version/third-party/retention), §25.3.

**Register completeness — INCOMPLETE (criterion partially unmet).** DOCX §19 tables and CSV both total **exactly 121 rows** (19.1=14, 19.2=18, 19.3=33, 19.4=56), matching the packet's "121-row register"; all dates, cohorts, roles, provider, sources, all 33 counts, all 23 cohort rates + 5 N/A, 6 deltas, 5 substitution, 5 gaps, 6 aggregates, 5 thresholds, 5 findings, 6 decisions, 1 status key are registered with locators. Gaps: RF-2, RF-3, RF-4.

**Usability (volunteer + TTQS evaluator) — PASS with nits.** §1 30-second path (correct), §24 19-row index (all rows verified true), §21 executable SOP, T-05 dictionary, T-18/T-19 gates and exceptions, plain language, no internal QA/Builder jargon in body (none present). Nits: RF-1, RF-10.

---

## 4. Residual findings (all nonblocking; no files edited)

| ID | Locator | Finding |
|---|---|---|
| RF-1 | §12 表 T-13 排序 column; F-GP-02 | Duplicate priority labels `1,1,2,3,3` with no tie rule; order not by descending gap; register "row N" ≠ 排序 label. **R14 N5 not fixed.** |
| RF-2 | §11.1 A-7, §11.2 B-7 rows; T-14 chain row cites「見 11.1 A-7／11.2 B-7」 | No register key carries locator `§11.1/A-7` or `§11.2/B-7` (values duplicate F-RA-05/F-RB-05). |
| RF-3 | §23 「保存年限…示例建議 3 年」(present in DOCX XML) | Synthetic value/decision has no fact key in §19.1–§19.4. |
| RF-4 | T-12 A/B判定 column (12 cells) | Only 2 keyed (F-FN-01, F-FN-02); 10 unkeyed though derivable from F-RT-01…05; §19.4's own title claims「判定」coverage. |
| RF-5 | §15 T-15 FN-2 證據 = `T-12` | The decision「記錄 8 名未申請」is evidenced in T-10 P8=8, not T-12. |
| RF-6 | §17 T-17 R-1 證據位置 includes「表 T-11」 | T-11 is the cohort/date table; it evidences neither the official phrase nor P5/P1 (§2.1, §11.1–11.2, T-10 do). |
| RF-7 | §26 [TABLE 31] 修改規則「T-10、T-14、T-19 三處」 | Under-specifies value-change propagation (omits T-12, T-13, §11.1–11.3, §13 narrative, §19 register). |
| RF-8 | §25.1 item 4「3 件」 | Equals A-period pending+failed (T-10 A: 2+1) but is unlabeled "A期"; A+B totals are 5 (P6=3, P7=2). D-1/T-15 are A-scoped → wording ambiguous. |
| RF-9 | §10 SRC-C1「未成班控制紀錄（非報名名冊）」 vs F-SR-07「SRC-C1 報名統計（0 筆）」 | Same source code, different document-type label between §10 and §19.2 (reconcilable: statistics ≠ roster). |
| RF-10 | [TABLE 1] 主要輸出「5 個比率（另加簽發查證完成率）」 | Composition of the "five" is ambiguous (implies 通過產出率 is among them, though [TABLE 7] marks it 選用); total 6 agrees with §24「六個指標」. |

---

## 5. Text-only sufficiency, blockers, limitations

- **Text-only evidence IS sufficient for semantic PASS on every packet criterion that is decidable from text** (identity, official-text fidelity, populations/formulas, complete arithmetic, cross-document consistency, zero-denominator handling, register coverage, SAMPLE/REAL boundary, no-fabrication, neighbor rejection, title-blind, navigation, limitations/actions). I did **not** use Builder PASS, deterministic QA, or visual receipts — none was consulted or needed.
- **Unresolved blocking findings: none.** The PARTIAL tier is driven solely by RF-1…RF-4 (one open R14 nonblocking finding + register-coverage gaps), with RF-5…RF-10 as minor corrections. All would move the verdict to PASS.
- **Limitations:** L1 no visual/layout/font verification (≥10.5pt/≥9.5pt, physical first page, rendering) — excluded by instruction, left unverified, not scored as defects; L2 `I18-E12` named in the request has no evidence anywhere in the packet/DOCX, so uniqueness vs E12 could not be checked (no E12 facts asserted); L3 I reviewed the packet's extraction, bound to the artifact by SHA-256/bytes and spot-checked 9 strings + 31-table count — a full extraction diff was not run (run-splitting can fragment phrases); L4 the R14 receipt was verified only as matching file bytes/hash, not its runtime claims; L5 no provenance comparison against historical DOCX bodies was performed; L6 **no REAL association count, certificate, approval, signature, or outcome is asserted — REAL status remains UNKNOWN/E0 (§14, §7, §25.1)**; L7 no formal approval is claimed or implied (§25.2 boxes unchecked, D-0 hold active); L8 no model identity is claimed.

**Final: PARTIAL** — all five R14 blockers corrected and every disputed number independently confirmed correct (report right: 209/384 = 54.427083%, +6.93 pp; allegation wrong), with ten residual nonblocking findings (RF-1…RF-10) enumerated above.