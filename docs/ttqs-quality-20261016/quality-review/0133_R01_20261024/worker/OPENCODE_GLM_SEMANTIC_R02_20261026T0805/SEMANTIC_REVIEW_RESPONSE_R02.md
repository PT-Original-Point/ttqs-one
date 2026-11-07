# Independent Semantic Review — TTQS ONE 0133 / I19-E22 (R01)

**Verdict: `PASS`** *(text-only semantic scope; partial scopes excluded below)*

## 1. Identity binding (as supplied; not recomputed in text-only scope)
- Work / project: **TTQS_ONE / TTQS_ONE_0133_I19-E22_R01**
- Candidate DOCX: **0133_I19-E22_CANDIDATE_R01.docx** — supplied DOCX SHA-256: `25116afb8206e0828c8b3a4a763845a9c3e672a4cb49969a64a2a3737d87256b`
- Candidate extracted text: supplied extraction SHA `314c24da92f364dddd4609956b602b4b19dd89bb48562392b752bd79b65bbd5d`; source packet SHA `097dcc766a8c2b0f320cb51e084e46681e85deef23a9476b94890726654b2863`; unique Blueprint SHA `edb8d241b1604790b36daf1622b907a9985ec7901c6d1e0a79f440be5fcb42fd`
- Requirement: **I19-E22** (142-sequence internal crosswalk ID, *not* an official printed serial); official source: evidence-table **p.8**, 3分 common-reference evidence line, exact wording verified character-for-character: 「每年訓練班次、人次均持續成長。」
- Project 157 index: **146** (I19-L3, “年度班次/人次：完整多期數據”); **official printed checkbox serial: UNKNOWN** — correctly left unknown in the document.
- Binding basis: the packet asserts the extraction came from the above DOCX; hashes were not recomputed (no tools, per contract). The supplied extraction itself is **complete and coherent** (30秒摘要 + §§1–12 + Tables 1–18, no truncation; internal cross-references self-consistent, e.g. SYN-25-X01 in §5/§8/§10; totals agree between §5 and §6), so the PARTIAL trigger for incomplete/unbindable text is **not** met.

## 2. Required checks — results and evidence

**C1. Genre & direct fit — PASS.** §1 quotes the official sentence verbatim and locates it at PDF p.8, 3分 reference list; Table 1 R5–R6 types the document as 年度班次與參訓人次登錄表及趨勢分析. Body delivers a dual annual series (classes **and** person-times) with every adjacent year compared (Tables 6–7) plus a step-by-step recomputation table (Table 8), and explicitly demotes first/last comparison to “補充…不可用來遮蔽中間年度下降” (§6 final paragraphs).

**C2. Negative neighbors — PASS.** §1 closing paragraph names 0132/I19-E21 (product defect units / inspected-product denominators) and 0134/I19-E23 (member count / fee income) and bars importing their data. Table 17 R2–R3 gives rejection fields ("不含產品、缺陷、受檢單位或不良率分子分母"; "不含會員名冊、會費帳冊或收入數字"). Full-text scan of Tables 5–15 found zero member/fee/income/product-defect figures — rejection is by body substance, not title only.

**C3. Operational completeness — PASS.** Yearly scope and cross-year no-split rule (§2.1); class definition and exclusion list for cancelled/postponed/zero-attendance/recruit-only cases (§2.2, SOP step 2, Table 3 R6); person-times definition (§2.3); source chain mapping plan→closure→anonymous roster/sign-in→annual roll-up→2nd-person recheck (§3 preamble, Table 3, SOP step 7); 8-step SOP with control points and outputs (Table 4); complete 24+1 filled sample (§5); reusable forms pre-marked UNKNOWN/HOLD so blanks cannot read as done (§9, Tables 11–14); exception demos with correction-and-trace requirements including formal correction-record field list and "不得無痕覆寫" (§8); correction demo SYN-0133-CORR-01 with both roles present; HOLD/REJECT/READY gates (§11, Table 16); per-fact replacement register incl. totals, rates, roles, and the dedup example as registered REAL-replacement targets (§10, Table 15 R2–R30). Minor gaps noted in F1–F4, none blocking.

**C4. Recalculation of all SAMPLE values — PASS (100% agreement).**
| Item | Recomputed from supplied text | Document value | ✓ |
|---|---|---|---|
| 2023 classes / person-times | 6 rows × 12 = **72** | 6 / 72 | ✓ |
| 2024 | 8 rows × 13 = **104** | 8 / 104 | ✓ |
| 2025 (10 held) | 12+13+14+14+14+14+15+15+15+15 = **141** | 10 / 141 | ✓ |
| Cancelled SYN-25-X01 (Table 5 R26) | 0 person-times, excluded | excluded | ✓ |
| 3-year totals | 6+8+10 = **24** classes; 72+104+141 = **317** | 24 / 317 | ✓ |
| 2024/2023 classes | (8−6)÷6 = 33.33→**33.3%** | 33.3% | ✓ |
| 2024/2023 person-times | 32÷72 = 44.44→**44.4%** | 44.4% | ✓ |
| 2025/2024 classes | (10−8)÷8 = **25.0%** | 25.0% | ✓ |
| 2025/2024 person-times | 37÷104 = 35.577→**35.6%** | 35.6% | ✓ |
| Endpoint 2025/2023 (supplementary only) | 4÷6 = 66.7%; 69÷72 = 95.8% | 66.7% / 95.8% | ✓ |

Net increments listed separately (+2/+2; +32/+37, Tables 6–7); base year rendered N/A (Tables 6–7 R2), zero/missing-denominator rule stated (Table 2 R2–R3); percentages computed unrounded and displayed at 1 decimal with classes/person-times integral (§2.4, §6); both metrics ≥ +1 in every adjacent year; no official growth threshold invented (§2.4, §11: 「官方沒有規定最低成長率…本表不創設此類標準」).

**C5. Person-times definition coherence — PASS.** §2.3: one person-time per (班次 ID × 去識別學員 ID) with ≥1 verified attendance; same attendee's multiple days in one class count **once** (no within-class repetition); same learner across two classes counts twice; explicitly *not* sign-up count, quota, daily sign-in sum, or cross-year unique natural persons. Backed by Table 9 R2–R5 and the SYN-LEARNER-014 dedup demo (§7 end: 「這是『人次』而非兩個不同自然人」); mismatch roster-vs-sign-in → HOLD (§2.3, SYN-EX-03).

**C6. SAMPLE discipline / no fabrication — PASS.** Banner "SAMPLE / SYNTHETIC 示範版｜REAL 原件與機構實績：目前 UNKNOWN"; §5 preamble marks all 24+1 rows and SYN-PLAN/ATT/CLOSE keys as fictional; roles are labeled 合成角色代碼 with Table 3 R10 explicitly banning real-signature representation; §6: "只是 SAMPLE 驗算，不是協會實績或官方評定"; §11: all association REAL data/policy/sign-offs/acceptance = UNKNOWN; no approvals, signed originals, or actual-performance claims anywhere.

**C7. Title-blind test — PASS.** With the title removed, the mechanism set (per-class unique IDs, class status column, class×learner dedup, dual annual series, adjacent-year delta checks, replacement register keys referencing 逐班明細) uniquely identifies an annual class/person-time trend evidence file; the body states what evidence proves the claim (closure + anonymous attendance sources, §3/§4) and what cannot yet be concluded (association growth, causal attribution, — §6 趨勢圖讀法, §11 HOLD restrictions).

**C8. Traceability & identity — PASS.** Table 1 R2–R4 separately displays doc_id 0133, internal I19-E22, and 157 index 146, each marked "不是官方方框流水號"; official printed serial stated UNKNOWN (R4). Index 146 appears only as a project locator (Table 1 R4, Table 18 R3), never as a printed serial. Official quote matches p.8 source exactly and is correctly attributed to the 3分 list.

**C9. Scope limits honored.** This review makes no claims about typography, font sizes (10.5pt/9.5pt acceptance item), images, pagination, DOCX rendering, opening behavior, or formal acceptance — reserved for separate technical/visual review.

## 3. Minor findings (non-blocking)
- **F1 (§2.1):** Cross-year attribution wording is "依實際結案規則指定一個年度" (flexible, documented reason + reviewer), diverging slightly from unique Blueprint §3.1's fixed default “最後一個具實質教學活動年度”. Anti-gaming intent ("不得為製造成長而改變") is preserved and the sample contains no cross-year case; align wording before REAL upgrade.
- **F2 (Table 3):** Field dictionary omits the explicit "輸出用途" column listed in unique Blueprint §5 item 7; usage is inferable from §1 outputs and Table 4 outputs column.
- **F3 (§8 Table 10):** Worked exception table demonstrates 4 of the 9 exception types; the remaining types (延期、零出席、跨年、重複 ID、漏結案) are covered in §2.1–2.3, Table 3 R2/R6, and SOP steps 2–3, but not as separate worked rows in one table.
- **F4 (§12 Table 18):** Source index lists positioning but not explicit version/date stamps for the official table readback ("附件來源與版本"); versioning is asserted in the runtime packet, not restated in the document.

## 4. Blocking defects
**none**