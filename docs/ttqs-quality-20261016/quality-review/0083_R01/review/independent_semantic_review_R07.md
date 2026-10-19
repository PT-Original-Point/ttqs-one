# Independent semantic review — DOCX 0083 R07 (exact-SHA)

## Verdict

**PASS**

- **DOCX SHA-256 (recomputed by me):** `63699ceb8dee08bea7c6ea437ae811670e15d021264b0f253b61ae2bdc4d1d61` — **exact match** to the required value.
- **Extraction SHA-256 (recomputed by me):** `4b4da6fb6002e423b3d181ba0dbb0b41360c96838216f9a3784786ad6947c4cd` for `evidence/docx_extracted_R07.md` — **exact match** to the expected extracted-text SHA.
- Build state as stated in the candidate: `NOT EXECUTED`; `REAL = UNKNOWN/HOLD`; `FORMAL_ACCEPTANCE = NOT_GRANTED`. Candidate quality review only; this verdict is not formal acceptance and not visual-layout QA.

## Actual scope read and counts

| Item | Result |
|---|---|
| Candidate inspected | `quality-review/0083_R01/candidate/0083_R07.docx` (92,974 bytes) + `0083_R07_body.md` (74,373 bytes) |
| Independent DOCX re-extraction | Parsed `word/document.xml` myself: **307 top-level paragraphs, 63 tables** (63 total `w:tbl`, no nested extras); 3,047 discrete text units |
| Attached extraction verified | Line-by-line coverage check of my extraction against `docx_extracted_R07.md`: **3,046 / 3,047 text units present** (see Limitations for the single exception) |
| Sections read | All of 1–15 (§1 file identity/30-second guide … §15 blank copyable forms) and Appendices A–E |
| Registers read | Both 81-row registers (§8.8 and Appendix E) = **162 register rows**, plus all 81 CSV rows of `SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv` |
| Blueprint/source read | `UNIQUE_BLUEPRINT_0083_R03.md` (all 13 sections), `SOURCE_PACKET_0083_R01.md`, R04 continuation receipts for cross-doc identity |

## Source / Blueprint mapping

- **Identity lock verified in body (§1.1, §12.1, §13.1):** DOCX `0083` = requirement `I17C-E02` = official checkbox `089` = genre 學員行動計畫追蹤紀錄 (individual learner post-training action plan design, follow-up, outcome decision). Document ID, requirement ID, and checkbox serial are consistently distinguished; no substitution anywhere.
- **17c/157 mapping (§1.1, §2.1):** correctly cites official evidence table printed p.6, 17c row, reference evidence 「參訓學員的學習成果實施行動計畫表追蹤紀錄」 and 157 blueprint item 089 「學員行動計畫追蹤：目標/實際/阻礙/協助/成效」; the other four 17c works (dynamic survey, supervisor rubric, knowledge community, mystery guest) are explicitly excluded and marked SEPARATE.
- **Sibling scopes:** 0082 / I17C-E01 / 088 correctly characterized as the upstream post-training behavior-transfer questionnaire (20 mentions, all boundary-setting; SYN-0083-B01 explicitly not a 0082 respondent/referral — §8 intro, §13.1, negative tests 4–5). 090 supervisor evaluation kept separate (§2.1, §11.2 trigger, §13.1) — consistent with the 0084 / I17C-E03 / 090 mapping in the workspace continuation receipts; no wrong-item substitution, and 0084's scope is never claimed.
- **Appendix A sources recomputed locally and all match:** SRC-157 `ad03323d…d216`, SRC-P6 `b7bd4c09…a1d1`, SRC-MIS `07c4b0be…1dd8`, SRC-GEN `7fc23191…f49aa`, SRC-083BP `21f76376…d0178`, SRC-083PKT `2c2f2947…50783` — each equals my `Get-FileHash` of the local file. Git blobs listed match the Blueprint's table. Dynamic PR #92 head is correctly *not* embedded (receipt-controlled).

## Semantic findings (section / table / field located)

- **Forms (§4–§7):** G1-01…G1-14 (14/14), T1-01…T1-17 (17/17), A1-00…A1-07 (8/8), E1-01…E1-07 (7/7) each present with definition, format/options, and missing-field handling; blank copies in §4.3/§5.3/§6.3/§7.3 and again in §15.1–§15.4; Appendix C matrices have exactly 14/17/8/7 rows matching the field sets. Form usability for a training administrator is mature: 30-second decision guide (§1.2), lifecycle (§3.1), role codes with prohibitions (§3.2), date/sequence rules (§3.3), SMART check (§4.4), calculation rules with explicit divide-by-zero → N/A handling (§5.4, §9.5), status codes (§5.5, all 10: ACHIEVED…PASS-SAMPLE), AID append-only rules (§6.1), evidence-location rules forbidding 「見附件」 (§7.5), SOP and gates (§10.1–§10.2), decision table (§11.2) with **21 triggers**, every processing window labeled `PROPOSED SAMPLE ONLY` or `PENDING`, each with release condition; §11.3 forbids overwriting originals.
- **Status/hold semantics:** HOLD/RETURN/REJECT/REVERIFY/REVISE defined with concrete operational triggers and release criteria (§11.1–§11.2) and mirrored per-field in Appendix C — requirement satisfied.
- **Negative tests (§13.2):** exactly **28 rows**, numbered 1–28, all with FAIL verdicts and corrective actions; covers 0082/088 confusion, 17c merge, PASS-SAMPLE overreach, range-style register IDs, extension-as-approved, unsourced deadlines, missing PENDING, etc.
- **Wrong-value sweep:** the strings "250%", "T2 本期 83.3%", "T3 本期 80%", "實績提升" occur **only inside negative-test rows 3, 18, 22** as prohibited examples — no erroneous value survives in any working table.
- **Forbidden-authorization wording:** 簽核/核准/核定 appear only in (a) negative-test rows 21/17/26 as banned wording, (b) register row R-009 「真實核定目標」 (替換來源 column, verbatim CSV/Blueprint-locked), and (c) 「非延期核准」 which explicitly negates approval. No claim of signature, approval, execution, third-party records, or formal acceptance anywhere.
- **Cross-document facts (§13.1):** 0082/088 REAL=UNKNOWN/HOLD upstream, 090 SEPARATE, 0073/0074 NOT_LINKED — all consistent with the source packet.

## Math / date result — all recomputed, all correct

- T0 2026-03-06; T1 2026-04-03 = **D+28** ✓; T2 2026-05-01 = **D+56** ✓; T3 2026-05-29 = **D+84** ✓; strictly increasing; G1-08 (2026-05-29) > T0 ✓; next date 2026-06-26 > T3 ✓ and repeatedly labeled SAMPLE 待追蹤／非延期 (§6.4, §8.4, §8.7, R-060).
- Baseline 2026-02-06→2026-03-05 inclusive = **28 days** ✓ (matches §8.1/§12.2 lock); elapsed-day vs inclusive-day distinction stated correctly (§8.2, §9.6).
- AID-01: requested 2026-04-03 (T1), provided 2026-04-13 — falls between T1 and T2 ✓, status PROVIDED ✓; AID-02 REQUESTED with A1-04/A1-05 PENDING ✓.
- Arithmetic: cumulative diffs **−1 / −1 / −2** ✓; current increments 3/4/3 against planned 4/4/4 ✓; current rates **75.0% / 100.0% / 75.0%** ✓; cumulative rates 3÷12=**25.0%**, 7÷12=**58.3%**, 10÷12=**83.3%** ✓ (rounding correct). Cumulative denominator is G1-07=12, never the latest planned 4 (negative test 22 guards this) ✓.
- Conclusion layering (§8.6–§8.7): numeric 83.3% passes only the PROPOSED ≥80% cumulative screen; sample-execution layer = **PARTIAL** (not PASS-SAMPLE) because AID-01 was unprovided at T1, AID-02 open, EVID-04/05 unauthorized; real-evidence layer = **HOLD/REVERIFY**; no causal or effectiveness claim. Internally consistent across §8.3, §8.6, §8.7, §9.4, §12.2.

## Register result — PASS

- Both 81-row registers (§8.8 and Appendix E) contain exactly **R-001…R-081**, continuous, no gaps, no duplicates within a block, no range-style IDs (each REG_ID appears exactly twice in the document — once per block — as designed).
- **Block vs. block:** 0 mismatches across all 6 columns.
- **Both blocks vs. CSV:** 0 mismatches across all 81×6 cells (REG_ID, 欄位定位, 值, 類別, 替換來源/條件, 狀態). R-016 correctly carries `PROPOSED`; all other rows `NOT_EXECUTED`. Every register value agrees with the case tables in §8.1–§8.7.
- Appendix D states the candidate DOCX SHA is receipt-recorded and deliberately not self-embedded — correct practice for exact-SHA verification.

## Real-vs-sample boundary — clean

- Every demo value is inside SAMPLE/SYNTHETIC/PROPOSED/NOT_EXECUTED framing; header1.xml carries `TTQS ONE｜DOCX 0083｜SAMPLE / SYNTHETIC` stamp. `REAL=UNKNOWN/HOLD`, `FORMAL_ACCEPTANCE=NOT_GRANTED` locked in §1.1, §12.1, Appendix D.
- No fabricated people: only role codes (ROLE-LEARNER/TRACKER/COORD/PEER/AUDIT) and synthetic IDs (LRN-B01, SYN-0083-B01, SYN-COURSE-0083-B). No phone/ID/email patterns detected. No real association action, site, approval, or signature asserted; the 模擬志工服務站 is disclaimed as fully synthetic (§8 intro, §12.1, negative test 17). E1-03/E1-05/E1-06 left PENDING rather than invented (§7.4 preamble states this explicitly). Evidence stays HOLD/UNKNOWN throughout; PASS-SAMPLE never used as an outcome (all 6 occurrences are definition, prohibition, or "not PASS-SAMPLE" statements).
- §12.5 isolation rules present including the no-unregistered-SAMPLE-value → REJECT rule; §15.5 replacement procedure requires clean blank copies, recomputation, and unchanged REAL=UNKNOWN/HOLD until authorized originals exist.

## Limitations

1. **Extraction completeness (non-material):** my independent extraction found exactly one text unit absent from the attached `docx_extracted_R07.md`: the string `開啟 Word 後更新目錄欄位` — the placeholder inside the `TOC \o "1-3" \h \z \u` field (`w:fldSimple`). This is dynamic field content Word regenerates on field update, not substantive body content; all 307 paragraphs and all 63 tables (every header and data cell) are otherwise fully represented. The extraction SHA matches the required value as-is.
2. Header/footer text (document number, page field, SAMPLE stamp) lives outside `document.xml` and was inspected separately rather than being part of the extracted-text SHA scope.
3. This is semantic review of the DOCX package and text only; rendered PDF/PNG evidence (`render_R07_final`) was not re-inspected — visual-layout QA is out of scope per the prompt.
4. Remote GitHub blob states (VERIFIED_REMOTE / readback receipts) were accepted as documented in Appendix A; I recomputed all *local* SHA-256 values (all matched) but performed no network calls, so remote byte-identity is receipt-attested, not re-verified by me.
5. No reliance was placed on the R01/R02/R03 review verdicts in `review/`; findings above are from my own extraction and recomputation.

## Actionable findings (non-blocking)

1. **Stale intra-document pointer in register rows R-079/R-080/R-081 (minor):** the 欄位定位 cells read `§7.4 數值層 / §7.4 樣本狀態層 / §7.4 真實證據層`, reflecting the *Blueprint's* section numbering (case = §7), while in the DOCX the result layers live at §8.6–§8.7 (as §8.2's `Blueprint §7.2 控制日期` note and §12.2's correct `第 8.6、8.7、9.4 節` mapping acknowledge). I assess this as **not material** because (a) row values are correct, (b) the layer names are unambiguous, and (c) the DOCX explicitly requires these rows to stay cell-identical to the CSV (`§15.5`), which the register does. If a future revision renumbers, fix it in the Blueprint/CSV first, then rebuild the register — do not diverge the DOCX register from the CSV.
2. Optional clarity improvement: prefix the three register pointers with "Blueprint" (as §8.2 already does) in a future Blueprint-synchronized revision, so Blueprint-numbering references cannot be misread as DOCX section numbers.

**Bottom line:** exact DOCX SHA confirmed; identity, genre, math, dates, both registers vs. each other and the CSV, field completeness for G1/T1/A1/E1, decision/negative-test coverage, cross-document boundaries, and the SAMPLE/REAL boundary all verify independently. **PASS** — no material semantic defect remains. `REAL` remains `UNKNOWN/HOLD`; `FORMAL_ACCEPTANCE` remains `NOT_GRANTED`.