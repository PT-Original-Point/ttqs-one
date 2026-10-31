## Independent semantic review of DOCX 0083 R03

Reviewer: OpenCode v2 CLI 2.0.29; model opencode/deepseek-v4.1-flash-free.
CLI exit: 0. A distinct CLI run from the Writer; session ID was not emitted in captured output.

**Exact DOCX SHA-256 (recomputed):** `60c18ccbb6f5b723de7cd69efca28c4c14774617c13d90784604427895ab8b07`
**Extraction SHA-256 (recomputed):** `3e662affd562099b51fd1e537d2643191b62809fc8a21721bb96bc6af6860879`
**Verdict: PASS**

Both target hashes were independently recomputed and match the prompt exactly.

## Actual scope read

- File: `docs/ttqs-quality-20261016/quality-review/0083_R01/candidate/0083_R03.docx` (92,861 bytes; build receipt `evidence/build_receipt_R03.json`).
- Read in full: §1–§15 plus Appendices A–E, including **both** 81-row replacement registers (§8.8 and Appendix E).
- Independent raw extraction of `word/document.xml`: 231 text paragraphs, 63 tables, 873 content lines. Attached `docx_extracted_R03.md` matches the on-disk evidence file (SHA above).
- Compared against `candidate/0083_R02_body.md`, `inputs/SOURCE_PACKET_0083_R01.md`, and `inputs/UNIQUE_BLUEPRINT_0083_R03.md`.

## Key semantic findings (with locators)

- **Identity lock correct** — §1.1 (文件控制) and §12.1: `DOCX 0083 = I17C-E02 = checkbox 089`; 文類 = 學員行動計畫追蹤紀錄; core columns 目標／實際／阻礙／協助／成效. Genres 0082/088 and 090 are kept separate (§13.1; §2.1).
- **DOCX == R02 body** — normalized line diff of the DOCX content vs the R02 body: **0 body lines missing**; the only extra lines are the builder-added `目錄` heading and TOC placeholder field. No content, field, value, or table differs.
- **Field ID integrity** — G1-01…G1-14 (§4), T1-01…T1-17 (§5), A1-00…A1-07 (§6), E1-01…E1-07 (§7) all present with definitions, options, and 缺漏處理; no reordered/inserted IDs.
- **Math (§5.4, §8.3, §8.5, §9.4)** — T1 `3÷4=75.0%` / `3÷12=25.0%`; T2 `4÷4=100.0%` / `7÷12=58.3%`; T3 `3÷4=75.0%` / `10÷12=83.3%`; 累計差 `−1, −1, −2`; 計畫累計 `4,8,12`; 實際累計 `3,7,10`; 本期增量 `4,4,4` / `3,4,3`. All recompute correctly. No forbidden wrong values (`T2 本期 83.3%`, `T3 本期 80%`, `250%`) appear except as prohibited negative-test items (§13.2 #18, #19, #22).
- **Dates (§8.2, §9.6)** — T0 `2026-03-06`; T1 `2026-04-03` (+28); T2 `2026-05-01` (+56); T3 `2026-05-29` (+84); baseline `2026-02-06`–`2026-03-05` (28 days inclusive); 建立 G1 `2026-03-09` (+3); next-date `2026-06-26` > T3. All strictly increasing; no inversions.
- **Decision table (§11.2)** — 21 triggers present; **all 21** carry `PROPOSED SAMPLE ONLY`, with `PENDING` where undetermined (4 rows). §12.3 matrix claims "21 觸發" — consistent.
- **Negative tests (§13.2)** — exactly **28** numbered items.
- **Register coverage** — 81 rows in §8.8 + 81 rows in Appendix E; `REG_ID` continuous `R-001…R-081`, no gaps, no duplicates; each row is a single atomic fact. `SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv` has 82 lines (header + 81) and **0 mismatches** against the body register (all 6 columns, all 81 rows).
- **Cross-document boundaries (§13.1)** — 0082/I17C-E01/088 = upstream, `REAL=UNKNOWN/HOLD`; 0083 = 本件, `NOT EXECUTED`; 090 = `SEPARATE`; 0073/0074 = `NOT_LINKED`. §2.3 and §13.1 explicitly deny that SYN-0083-B01 is an 0082 interviewee/referral.
- **Actions (§11.1/§11.2/§11.3)** — HOLD/RETURN/REJECT/REVERIFY/REVISE defined with release conditions; used consistently (e.g. 合成值當真人紀錄 → REJECT; 數值達標但證據未授權 → REVERIFY/PARTIAL).
- **Appendix A SHA table** — independently verified: all eight local SHA-256 values match exactly, and all five local files' Git blob IDs match `git hash-object` (`SRC-157 8c2bbe7c…`, `SRC-MIS 538bedb9…`, `SRC-GEN 4ff863d9…`, `SRC-0082C a113eaee…`, `SRC-0082B 3679bfa4…`). `SRC-083BP` `21f76376…` and `SRC-083PKT` `2c2f2947…` match the on-disk inputs.

## Math / date / register result

**PASS.** Every quotient, difference, and D+n recomputes; dates are monotonic and span exactly 84 elapsed days (T0→T3) across three 28-day intervals; the register is 81 consecutive unique atomic rows and is byte-consistent with the accompanying CSV and the R02 body.

## Mapping result

**PASS.** Identity mapping `DOCX 0083 = I17C-E02 = checkbox 089` holds. DOCX-extraction → R02 body mapping is an exact content match (only builder TOC lines added). Register mapping: body §8.8 = Appendix E = CSV (81/81/81, 0 diffs).

## Sample boundary result

**PASS.** `REAL = UNKNOWN/HOLD` and `FORMAL_ACCEPTANCE = NOT_GRANTED` appear in §1.1, §12.1, §12.2, Appendix D, and the results layers. `ALL_DEMO = SAMPLE/SYNTHETIC/PROPOSED/NOT_EXECUTED`; the case is explicitly a fully synthetic "模擬志工服務站" with a disclaimer that no site/process/hire/approval is claimed (§8, §13.1). Numeric layer 83.3% is explicitly *not* success; sample-execution = `PARTIAL`, real-evidence = `HOLD/REVERIFY`. No person names/IDs/contacts/health/family data; no signatures; third-party evidence (EVID-05) is authorization-`PENDING`; no approval/`已核准`/`已生效`/`PASS-SAMPLE`/`ACHIEVED` assertions — those strings occur only in definitions, disclaimers, or the negative-test list. Independent scan of `word/document.xml` found **no** PII-like patterns. Header/watermark "SAMPLE / SYNTHETIC" and the watermark shape are present; footer carries 頁 field.

## Limitations

- Semantic review only — **not** visual-layout QA and **not** formal acceptance. Font/spacing, table page-breaks, TOC field population, and PDF rendering were not judged here.
- Two immaterial, non-blocking observations (carried from the Blueprint, no effect on correctness or safety): (1) register rows R-079–R-081 cite locator "§7.4", whereas the corresponding narrative sits in §8.6/§8.7 of this body — the reference points to the Blueprint's §7.4 and is reproduced verbatim; (2) Appendix D still frames itself as the "R02 候選 … PENDING" text candidate with "DOCX 建置狀態 PENDING（未建置）", which predates the R03 word render; it matches the reviewed R02 body and does not alter the identity or boundary locks.
- Remote-side items in Appendix A (`SRC-BR` commit `719ac6a9…`, remote blobs for the two 0083 inputs) were not re-fetched; local SHA-256 and Git blob checks passed for every file present in the workspace.
