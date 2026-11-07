## Independent exact-SHA semantic review — DOCX 0079 R07

### 1. Identity
- Observed SHA-256: `0361cf65557733cb3e1af93d5e59197aa96d307622a840800d008d8c580c66a7`
- Required SHA-256: `0361cf65557733cb3e1af93d5e59197aa96d307622a840800d008d8c580c66a7`
- Identity: **PASS** (exact match; reviewed the actual DOCX bytes via python-docx, not only Markdown).

### 2. Verdict
**PASS** — semantic quality is adequate for candidate review. This is **not** formal acceptance.

### 3. Finding table
| ID | Severity | Locator (printed page / section / table / cell) | Evidence | Required remedy |
|---|---|---|---|---|
| — | — | None identified | No blocking or minor semantic defect requiring remedy was found in the reviewed DOCX bytes, rendered PDF (21 pages), or cross-document mapping table. | None required. |

(Non-substantive note: `docProps/app.xml` reports `Pages=1`, which is stale metadata; the rendered export has 21 pages and `visual_review_R07.json` records `layout_result=PASS`. No semantic impact.)

### 4. Dimension checks
1. **Exact agreement with official requirement 084 / I17B-E01 and correct genre** — PASS. Cover and p.1–4 state `0079 / I17B-E01 / checkbox 084 / 17b`; title “訓後個別職涯與學習規劃建議表”; explicit statement that it is not 0073/0074/0075/0076/0077/0078, not a recommendation letter, aptitude certificate, or admission review. Official p.6 wording “訓後學員職涯規劃建議表” is reproduced (Table 3, p.1–2).
2. **Mature, usable content** — PASS. Realistic workflow (Section 3, 7 steps), choice comparison (each P card options A/B/C with feasibility/limits/reasons), source traceability (Tables 8–17, 31, Appendix A), role boundaries (Table 6), participant confirmation (Table 1), planned follow-up form (Section 7, status dictionary Table 27), objection/withdrawal (Table 26 + Section 4), review/hold/reject/transfer rules (Section 9, Table 32).
3. **P01–P04 synthetic and internally coherent** — PASS. All four cards carry `SAMPLE/SYNTHETIC`, `PROPOSED`, `PLANNED_NOT_EXECUTED`, `REAL=UNKNOWN/HOLD`. Scores match source packet: P01 70/100 & 18/20 PASS_SAMPLE_RULE; P02 75/100 & 15/20 PASS_SAMPLE_RULE; P03 85/100 & 14/20 HOLD_SAMPLE_RULE; P04 80/100 & 16/20 PASS_SAMPLE_RULE. Themes match 0077 (NEEDS_CLARIFICATION, PRIVACY_CONSENT, RECORD_ACCURACY, CLOSED_LOOP_HANDOFF). Planning/action/follow-up dates are sequential after the 2026-08-15 synthetic course date. P03 remains HOLD with supervision/reassessment limits and is not written as passing.
4. **Cross-document fact integrity** — PASS. No real names, meetings, approvals, consent, outcomes, credentials, signatures, or association decisions invented. Uses only synthetic codes (SYN-0073-2026-A01, P01–P04) and placeholders. P01–P04 are not mapped to 0073 S01–S16, 0078 A01–A08, or any real activity/photo. `SAMPLE/SYNTHETIC`, `REAL=UNKNOWN/HOLD`, `NOT_GRANTED`, `084 PARTIAL/HOLD` are stated throughout (cover, Tables 2 and 34, p.21).
5. **Mapping to adjacent DOCX 0080 and 0081** — PASS. Printed p.19, Table 33 rows 9–10 read `0080 / I17B-E02 / checkbox 085` and `0081 / I17B-E03 / checkbox 086`. No remaining collision: the document contains no `0085`/`0086` file-number references; `085`/`086` appear only as official checkbox serials.
6. **Reject wrong-document substitution** — PASS. Even with the title hidden, the body still clearly serves 084: it is individual post-training career/learning planning advice with learner choice, source facts, options, actions, support, and follow-up; it explicitly contrasts itself with course evaluation (085) and closeout/action-plan verification (086) and does not perform either.
7. **Math / numerical separation** — PASS. The only arithmetic is score-vs-threshold comparisons and the 70/100, 15/20 demonstrative rule; these are repeatedly labeled `SAMPLE_RULE` / “僅為示範規則，非本會或官方標準.” No numerical conclusion is presented as an official threshold or as a career-fit claim.
8. **Actual DOCX readability / rendered layout** — PASS. Rendered PDF is 21 pages; independent PDF-text extraction confirms readable tables and the corrected p.19 rows. `visual_review_R07.json` records `layout_result=PASS` with no clipping/overlap/broken borders on changed pages; unchanged pages are hash-identical to inspected prior renders. Header/footer consistently carry identity and `SAMPLE/SYNTHETIC | CANDIDATE ONLY | REAL=UNKNOWN/HOLD`.

### 5. Formal acceptance
`formal_acceptance=NOT_GRANTED`. The document is a candidate/sample artifact only; no real evidence, consultation, consent, approval, or official acceptance is claimed. Checkbox 084 remains `PARTIAL/HOLD` pending the four distinct products (0076/0077/0078/0079) and real source paths.
