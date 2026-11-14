PASS

**Artifact SHA and extraction-receipt binding**

- DOCX SHA-256: `885fe403b46144639034a3f6b26c2b74916c22c7b5a5a971628136f376a115f3` — matches the expected SHA exactly.
- Extraction receipt (`docx_extraction_receipt_R01.json`) binds the same DOCX SHA and the extracted file SHA `cdf6aa0ea80110e58a77fd2dff2e52980f9a4d00edf069f4be6977918977a28e`; the extracted file hash matches; receipt reports 31 tables and `COMPLETE`.
- Official evidence-table PDF SHA: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`, matching the blueprint/source packet.

**Requirement / checkbox / Blueprint decision**

- 0076 is correctly mapped as the **exam and practical assessment record** for **I17B-E01 / checkbox 084 / indicator 17b**, not 0073 (17a satisfaction survey), 0074 (17a learning assessment), 0075 (17a improvement plan), or checkboxes 085/086.
- The Unique Blueprint’s four distinct functions for 084 are preserved: 0076 exam/practical record, 0077 reflection, 0078 photo/activity index, 0079 post-training guidance. 0076 does not claim to replace the other three.
- Official 17b levels are recorded as definitions only; the candidate claims no level.

**Findings (with locators)**

1. **SAMPLE/HOLD identity is explicit and consistent** — title block, Table 1, Table 15, and closing status state `SAMPLE/SYNTHETIC`, `CANDIDATE_ONLY`, `REAL=UNKNOWN/HOLD`, `NOT_GRANTED`, and 084 `PARTIAL`. No real participant, score, session, approval, signature, credential, or outcome is asserted.
2. **Usable assessment instrument, not generic narrative** — Table 7 maps all 20 items to OBJ-1–OBJ-4 with the fixed answer key `A,C,B,D,A,C,B,D,C,A,D,B,C,A,D,B,A,C,D,B`; Section 5.2 gives item text, choices, and explanations; Table 16 gives four 0–5 rubric criteria with observable anchors; Table 17 gives a completed P01 example.
3. **Full 16-learner response matrix and scoring are internally consistent** — Tables 12–13 match the supplied CSV row-for-row; every learner’s `correct_items × 5 = written_score` holds; written score equals the retained post-test total for each P01–P16.
4. **Item analysis is arithmetically consistent** — Table 15’s `correct_n` values match an independent recount from Tables 12–13 and the item-analysis CSV; total correct item instances = 253; facility values range from 0.6875 to 0.9375; n = 16 for every item.
5. **Practical assessment is complete and auditable** — Table 18 lists all 16 practical totals from the four criteria; Table 19 recomputes 253 / 15.8125 / 11 of 16 ≥ 15; Table 20 cross-tab and Table 21 per-learner combined decisions are consistent with the computed pass sets.
6. **Linked 0073/0074 facts are preserved with denominator separation** — Table 14 retains pre 870 / 54.375, post 1265 / 79.0625, gain +24.6875, post ≥ 80 = 9/16 = 56.25%; 0073 Q5 = 54/15 = 3.60/5 with 8/15 = 53.33% positive, explicitly using a 15-questionnaire denominator separate from the 16-test denominator.
7. **0075 is correctly treated as non-causal background** — Tables 5 and 28 state Option B is `PROPOSED/PENDING APPROVAL`, not executed or approved, and no causal claim is made from 0075 to 0076 data.
8. **Identity and data boundaries are respected** — Section 4.2 and Table 28 state that 0073 S01–S16 and 0076 P01–P16 have no asserted identity crosswalk; historical candidate 2163 is excluded as a different course/date/sample.
9. **Usability and control rules are actionable** — Sections 6, 9, 12, and 13 define versioning, authorized assessor/tester, timing, denominator rules, missing/invalid/late/duplicate/unclear-answer handling, regrade traceability, privacy/minimal necessary access and retention, and H-1 through H-12 HOLD/rejection triggers; Table 26 is a complete REAL replacement checklist.
10. **Composite boundary is correctly marked unresolved** — Tables 6 and 28 and H-10 state that 084 requires 0076 + 0077 + 0078 + 0079 with authentic source paths; the candidate does not claim 084 completion.
11. **A technical checker false negative is not a semantic defect** — `technical_review_R01_checker_false_negative.json` reports “body missing checkbox 084,” but the body consistently uses the Chinese locator “勾選 084” (Tables 1, 3, 6, 14, and Section 14), so this is a literal-string checker issue, not a content gap.

**Recalculation result**

Independently recomputed from the assessment CSV and extracted DOCX:

| Measure | Result |
|---|---:|
| Pre-test sum / mean (n = 16) | 870 / 54.375 |
| Post-test sum / mean (n = 16) | 1265 / 79.0625 |
| Mean gain | +24.6875 |
| Post-test ≥ 80 | 9 / 16 = 56.25% |
| Written score ≥ 70 | 15 / 16 = 93.75% |
| Practical sum / mean (n = 16) | 253 / 15.8125 |
| Practical ≥ 15 | 11 / 16 = 68.75% |
| Both written and practical pass | 11 / 16 = 68.75% |
| Total item correct instances | 253 = 253 / 320 = 0.790625 |
| Item correct counts | 11,12,12,12,13,12,12,13,13,13,14,14,14,15,15,13,11,11,11,12 |

Per-learner matrices, practical subtotals, cross-tabulation, and combined decisions also match the CSV and extracted Tables 12, 13, 18, 20, and 21. **No arithmetic discrepancy was found.**

**Remaining blockers**

- Checkbox 084 remains **composite and PARTIAL/HOLD**: 0077 learner reflection, 0078 real photo/activity index, and 0079 individual post-training guidance are still required.
- All real evidence remains `REAL=UNKNOWN/HOLD`; the sample thresholds (≥70/100 and ≥15/20) are explicitly sample rules, not approved association policy.
- Formal acceptance remains **NOT_GRANTED**; real source paths, authorized roles, real scores, and real administration evidence are not verified.

**Review basis and limitations**

- Basis: exact DOCX text extraction bound to the expected DOCX SHA; supplied CSVs, blueprint, source packet, upstream snapshots, technical review, visual review JSON, and official PDF identity by SHA.
- The official source’s page-6 17b wording/levels were taken from the supplied blueprint/source packet; the PDF’s font encoding was not independently decoded as usable text in this environment.
- Visual layout was **not independently re-inspected by me**; I relied on `visual_review_R01.json` (PASS, 26 pages) as supplied evidence.
- This is a review-only verdict; no files were edited or rebuilt. A semantic PASS does not mean checkbox 084 is complete, formal acceptance is granted, or real evidence is verified.
