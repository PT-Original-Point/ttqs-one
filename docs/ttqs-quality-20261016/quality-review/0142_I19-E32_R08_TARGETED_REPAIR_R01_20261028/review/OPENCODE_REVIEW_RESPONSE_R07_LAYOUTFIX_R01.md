**Reviewed candidate SHA-256:** `ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f`  
**Candidate size:** 50,156 bytes (as stated; not independently measured)  
**Body extraction:** claimed `41f5562d9200188a1f76b1964c5c6c6c6b72ba4228a67c1c43c95752036f127c`  
**doc_id:** 0142  
**requirement_id:** I19-E32 (157 index 156; printed serial UNKNOWN)  
**Verdict:** **PARTIAL**

All conclusions below are bound only to candidate `ac6f28…84f`. No R06 verdict is transferred, and this review does not accept the candidate formally.

### Covered scope

Reviewed the supplied candidate body in document order, Tables 1–16, the companion 19-row CSV, the R01 snapshot, the official requirement/crosswalk rows, the lineage extension, and the render/visual receipt metadata. Checked requirement match, genre, operational fields, source register, account classification, reconciliations, formulas, exception/release conditions, math and rounding, SAMPLE/REAL boundary, lineage, title-blind identification, negative-neighbor separation, usability, date/version uncertainty, and the prior R06 findings.

Positive results:
- Official source identity matches: filename, SHA `805386…4709`, 9 pages, citation p9/9, requirement text and index 156.
- Crosswalk title matches: 組織近三年營業額與收入趨勢核對報告.
- Sample arithmetic is correct:
  - 2024: `120,000 / 1,200,000 = 10.00%`
  - 2025: `132,000 / 1,320,000 = 10.00%`
  - 2023–2025 operating cumulative: `252,000 / 1,200,000 = 21.00%`
  - 2023–2025 total-income cumulative: `272,000 / 1,480,000 = 18.378…% → 18.38%`
  - All three total-income additions are correct.
- SAMPLE/SYNTHETIC and REAL are strongly separated; synthetic roles are labeled and no association names, signatures, approvals, or results are fabricated.
- 0139/I19-E29, 0140/I19-E30, and 0141/I19-E31 are expressly excluded.
- Explicit rounding is stated at P31: amounts retained at source value; percentages calculated from unrounded numerator/denominator and displayed to two decimals with no intermediate rounding.
- Denominator ≤0, accounting-basis differences, refunds/allowances/write-offs, unclassified donations/subsidies/membership fees/agency receipts, and one-time income have stop/HOLD conditions.
- P48 states a five-part conjunctive REAL acceptance rule.

### Findings

| # | Severity | Locator | Evidence | Impact | Minimal correction |
|---|---|---|---|---|---|
| F1 | **Medium** | P12; lineage extension fields `parent_lineage_path`, `parent_lineage_sha256` `26649…39bc`, `parent_candidate_sha256` `35f7e3c…44cd`, `candidate_sha256` `ac6f28…84f` | P12 says the R01 source packet is retained only as a historical snapshot and refers to a quality sidecar. The extension asserts inheritance through the “exact parent lineage,” but the parent lineage file is not supplied and there is no entry for R01 baseline `59f9b500…34a6` or R06 `60563d4a…4f0e6`. | The exact R01→R06→R07→R07-layoutfix chain and the “only one empty paragraph removed” claim are asserted, not fully evidenced. Prior finding #1 is only partially repaired. | Add a lineage annex/table listing every stage: SHA-256, bytes, version, date, change type, and verifier, including `59f9b500…34a6`, `60563d4a…4f0e6`, `35f7e3c…44cd`, and `ac6f28…84f`. Include or attach the parent lineage JSON and state the layout-only diff explicitly. |
| F2 | **Medium** | P5; P64; Table 16 F19 | Internal control says “版本：1.2／R07,” while the filename/lineage identify `R07_LAYOUTFIX_R01` and parent R07 SHA `35f7e3c…44cd`. No “LF01” or parent SHA appears in the document control block. | The byte-changing layoutfix candidate is not distinguishable from its parent by the document’s own version label. Retrieval and version-control risk remains. | Add “R07-LF01（版面修正；非空段落與表格文字未變）” and the parent SHA/revision note in P5/P64/F19, or explicitly define “1.2/R07” as the content version and “R07-LF01” as the build label. A changed control block requires a new candidate SHA and re-review. |
| F3 | **Medium** | Table 12 header and R2–R4 | The register combines “整理角色／核准狀態” in one column; values say “合成整理角色；無真人調閱或簽核.” The “幣別／單位／帳務基礎” value says “新臺幣元；完整曆年；同一示例口徑假設,” without stating accrual, cash, or “unspecified.” The blueprint requires “擷取與覆核職務” and “會計基礎.” | The per-year source register does not show a separate independent reviewer or a determinate accounting basis. Real replacement could omit both, weakening auditability. | Split into “整理角色” and “獨立覆核角色／日期”; keep approval status separate. Populate the SAMPLE basis as “示例假設（未指定權責/現金基礎）” or require the actual basis for REAL. |
| F4 | **Low** | Table 15 header and R2–R11; Table 16 R14–R17 (F13–F16) | Table 15’s “重算日期（SAMPLE／REAL分開）” only says “本示範未解除該REAL例外；REAL未重算／無重算日”; no SAMPLE recalculation date is entered. Table 16 F13–F16 says “UNKNOWN/HOLD / 未覆核；未替換” without a date or explicit N/A. | The sample recalculation and replacement-date audit trail is incomplete. | Add “SAMPLE重算日：2026-10-28” or “SAMPLE：不適用” in Table 15; fill Table 16’s date cells with “N/A（未替換）” or an actual date. |
| F5 | **Low** | CSV F15 `document_locator`; Table 8 R1 | CSV F15 locates the cumulative conclusion at “Table 7 cumulative operating-revenue row; Section 4.1 example conclusion.” The actual conclusion is Table 8 R1. | Minor retrieval ambiguity for the sample conclusion. | Change the locator to “Table 7 R4; Table 8 R1.” |
| F6 | **Low** | Tables 12–16; P86; P64 | All registers are populated with SAMPLE values. The document says to replace them, but does not expressly say “preserve the SAMPLE rows and create a separate REAL version.” P64 refers to a “修訂版” but provides no blank REAL worksheet. | Staff could overwrite SAMPLE cells in place, destroying the sample audit trail or mixing SAMPLE/REAL values. | Add one instruction: “另存 REAL 版本；保留本 SAMPLE 列不覆寫；逐列狀態以 CSV 為準,” or add a blank REAL annex/worksheet. |

There is no FAIL-level finding on the core requirement method or sample arithmetic. The three Medium findings are material to PASS because they affect exact-SHA lineage, version identity, and source-register completeness.

### Prior R06 findings

| Prior finding | Status on `ac6f28…84f` | Locator |
|---|---|---|
| 1. R01 baseline/version lineage not reconciled | **Partially resolved** — R01 is called a historical snapshot and parent R07 SHA is supplied, but the full R01→R06→R07→R07-layoutfix chain and parent lineage file are absent. | P12; lineage extension |
| 2. First-page status needed distinct REAL UNKNOWN/HOLD, NOT_ASSIGNED, NOT_GRANTED | **Resolved** — P5 lists CANDIDATE; SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD; official score=NOT_ASSIGNED; formal acceptance=NOT_GRANTED; not effective. | P5; Table 1 R6 |
| 3. Companion CSV absent | **Resolved in supplied packet** — 19 rows F01–F19, matching Table 16’s 19 data rows and values. CSV SHA was not independently computed against `replacement_register_sha256`. | CSV; Table 16 |
| 4. Denominator ≤0 needed N/A/HOLD and basis/refund stop conditions | **Resolved** — base ≤0, accounting-basis differences, and refunds/allowances/write-offs are covered. | Table 3 R7; Table 15 R4, R10, R11; P48 |
| 5. T12/T13/T14/T15 needed separate difference, decision basis, adjustment/source location, recalculation date | **Substantially resolved** — T12 separates SAMPLE/REAL differences; T13 has classification basis; T14 has adjustment and REAL source location; T15 has a recalculation-date column. Residual: T15 sample date empty; T12 reviewer/basis gap. | Tables 12–15 |
| 6. Explicit rounding rule | **Resolved** — P31 states source amounts retained, percentages from unrounded values, two decimals, no intermediate rounding. | P31 |
| 7. Distinguish 0139/0140/0141 | **Resolved** — explicit exclusion of exam/employment, training-system usage, and satisfaction data/periods/samples/conclusions/scores. | P15; P63; Table 11 R4 |
| 8. Record source filename/version and date uncertainty | **Resolved** — official filename, SHA, pages, p9/9, version/publication/download UNKNOWN, file mtime and PDF metadata distinguished. | Table 2; Table 12 |
| 9. Conjunctive REAL acceptance rule | **Resolved** — five conditions must all hold; any failure keeps REAL UNKNOWN/HOLD and bars inference from sample arithmetic. | P48 |

### Visual/render receipt assessment

The render receipt (`706c2ae1…85de6`) reports 12 pages and unchanged DOCX bytes; the page-image manifest (`d21b2624…2b71`) also reports 12 pages; the visual QA receipt (`428e9608…dabe`) reports PASS. The counts are mutually consistent, and the body extraction’s gap before P50 is consistent with the stated removal of an empty page break before Section 5.

However, these are builder-supplied artifacts. I did not open the DOCX/PDF or inspect page images or pixels, so I cannot independently confirm the absence of clipping, overlap, table overflow, font substitution, or other visual defects. The visual PASS is therefore accepted only as supplied metadata, not as an independently verified result.

### Remaining limitations

- No independent binary verification: I did not compute SHA-256, byte counts, or the body-extraction hash; those values are taken as stated.
- Page-level locators are not determinable from the supplied text; the 12-page count is receipt-reported. Findings therefore use section/table/row/field locators.
- The parent lineage file and the “quality sidecar” referenced by P12/extension are not supplied in full; the exact chain relies partly on assertions.
- The companion CSV is present and content-consistent, but its SHA was not independently verified against `replacement_register_sha256`.
- The layout-only change claim was not independently diffed; the non-empty body text appears unchanged, but the exact binary difference was not verified.
- No REAL association financial statements, revenue detail/general ledger, account mapping, authorization, approvals, or review dates were provided. REAL evidence remains unknown; the sample arithmetic cannot establish association performance.
- Practical usability is generally good, but the sample-populated registers create a residual overwrite risk (F6).

**Candidate/sample quality:** substantially complete and arithmetically correct; **PARTIAL** overall because of the lineage/version-control and register-completeness findings above.

**formal_acceptance:** NOT_GRANTED  
**real_evidence:** UNKNOWN/HOLD  
**official_score:** NOT_ASSIGNED

No files were modified; no tools were used.
