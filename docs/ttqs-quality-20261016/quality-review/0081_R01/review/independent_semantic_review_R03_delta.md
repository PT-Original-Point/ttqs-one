# R03 exact-SHA delta review result

- Observed DOCX SHA-256: `afad7608a1e85dd479eb655724cc2ce42cf5f91f0f9bb59d6f601b3b31b56201`
- Expected DOCX SHA-256: `afad7608a1e85dd479eb655724cc2ce42cf5f91f0f9bb59d6f601b3b31b56201`
- Identity result: PASS
- Delta verdict: PASS

## Six checks

1. (a) DOCX SHA identity: PASS. Observed equals expected.
2. (b) Three corrections present, no stale R01 candidate/register label: PASS.
   - DOCX `word/document.xml`, paragraph 3 (cover status line): review wording now says review state is governed by exact-SHA receipts; `CANDIDATE_ONLY` and `NOT_GRANTED` retained.
   - DOCX `word/document.xml`, paragraph 20 (status table): candidate label is `R03`.
   - DOCX `word/document.xml`, paragraph 524 (section 11.1): register filename is `SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv`.
   - Body markdown line 4, line 32, and line 372 contain the same three corrections.
   - No stale `0081_R01` candidate/register label remains. Only legitimate upstream references remain: `0080_R01/candidate/0080_R05_body.md` and the branch `(R01 observation point)` note in Appendix A.
3. (c) Substantive text/tables/numbers unchanged from R02 except the three metadata corrections: PASS.
   - DOCX XML skeleton is identical between R02 and R03; both have 20 tables.
   - The only document text differences are the three intended label/status/register changes.
   - Body markdown differs only on line 4, line 32, and line 372.
   - Scenario facts, scores, counts, thresholds, and tables remain unchanged.
4. (d) Register: PASS.
   - Register SHA-256: `4e76c3f7e7dc818e94b1551e81b5d3e83d1dd4361c5aaaa3cf8eea139be7e074`
   - Data rows: 23 (`SYN-0081-001` through `SYN-0081-023`).
   - Every `source_path` points to `.../candidate/0081_R03_body.md`.
   - Every `real_status` is `REAL=UNKNOWN/HOLD`; no REAL promotion.
5. (e) PDF pages 1, 2, and 11: PASS for readability/layout based on available evidence.
   - PDF SHA-256: `8d433014ccf8137c4cdafa1f4df5e7c01e6670efded5089ce55044dfeb13fdf0`
   - Page count: 13.
   - Extracted text confirms page 1 cover shows the R03 exact-SHA-receipts status wording, page 2 shows the `R03` candidate label, and page 11 shows `SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv`.
   - Recorded visual review reports all 13 pages inspected with no clipping, overlap, broken table, unreadable text, or missing glyph.
6. (f) Prior R02 semantic PASS applicability: PASS.
   - The R02 semantic PASS at SHA `5b77683da206a9973f132c2222775aa22d96ffb7b24042cdb6230d6875db04e3` still applies to the unchanged substantive content.
   - R03 only resolves the three non-blocking administrative references noted in the R02 review; it does not change substantive document content or claim formal acceptance.

## Final status

- `REAL=UNKNOWN/HOLD`
- `formal_acceptance=NOT_GRANTED`
