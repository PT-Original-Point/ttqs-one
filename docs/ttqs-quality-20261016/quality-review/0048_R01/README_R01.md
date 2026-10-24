# DOCX 0048 R01 — candidate evidence package

**Status:** CANDIDATE ONLY. Technical and direct visual QA pass. Independent exact-SHA semantic review: **PARTIAL (F1)**. Formal association acceptance is NOT GRANTED.

## Official requirement binding

- DOCX ID: `0048`
- Requirement ID: `I10-E03`
- Official checkbox sequence: `049` (not the DOCX ID)
- Official source box: `P03-B10`, official evidence table page 3
- Official requirement: 「大型採購均辦理會議通過、師資遴聘後亦經過會議或審查通過並留有紀錄。」
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- Unique Blueprint row SHA-256: `8b258f9125f2b1209629d0356539537e00c322073739ec65d05c58590847ef72`
- Unique Blueprint source SHA-256: `cf27a59f04d59d7b43aa364c3a812715e37337863c756ab513fe0b0661513667`

## Candidate bytes and scope

- File: `candidate/0048_R01.docx`
- SHA-256: `e6bb07cc8f984a8d6d72a64f4498717df6a5116d98431bee75c2f1e2151d28e9`
- Size: 58,156 bytes
- The body is a dedicated meeting/review evidence record. It contains a reusable meeting form, a full synthetic procurement meeting example, a separate synthetic post-selection instructor review, operational decision and hold/return conditions, a source and attachment index, and a 39-row fact replacement register.
- All case events, roles, dates, amounts, votes, scores, decisions, criteria and attachment identifiers are SAMPLE/SYNTHETIC. No actual association meeting, procurement, appointment, approval, signature, or third-party original is represented.

## Technical and visual evidence

- DOCX package integrity: PASS; 19 package parts.
- Document structure: 88 paragraphs and 27 tables.
- Rendered PDF: `evidence/render_final_R01_e6bb07cc/0048_R01.pdf`, 16 pages.
- All 16 rendered pages were directly inspected. No blank page, clipping, overlap, orphan table row, unreadable table, or title rule was observed.
- Arithmetic recomputed: 120,000 − 113,000 = 7,000; utilization 94.2%; weights total 100%; weighted scores 89 and 80; sample completeness ratios 10/10 and 9/9.
- Technical receipt: `evidence/TECHNICAL_VISUAL_QA_R01.json`.
- Full-page images and PDF are included for external review.

## Independent semantic review

An independent review was completed through OpenCode CLI v2 against the full candidate text/tables and this exact SHA. Original reviewer response: `review/opencode_v2_review_result_R01.md`; invocation receipt: `review/opencode_v2_review_receipt_R01.json`. Verdict: **PARTIAL**. Finding F1: §02 field table lacks an explicit `填寫者／責任角色` column required by the unique Blueprint. The reviewer also noted that the required requirement-to-field-to-attachment trace is split across multiple tables; the next revision will make it explicit in one table. No arithmetic, authenticity, or sample-boundary defect was found. The exact R01 bytes remain preserved for audit; the targeted content correction is R02. A later independent R02 review also found the 9.5 pt body-note font-floor issue was already present in R01 (page 1 and page 11); the R01 reviewer's statement that body text met the 10.5 pt floor was inaccurate. See `../0048_R02/review/opencode_v2_review_result_R02.md`. Formal acceptance remains NOT GRANTED.

## Adjacent requirement separation

DOCX 0045 is I10-E01, DOCX 0047 is I10-E02, DOCX 0048 is I10-E03, and DOCX 0049 is I11-E01. This package is bound to DOCX 0048 / I10-E03 / checkbox 049 / P03-B10. Checkbox 049 is not a document number.
