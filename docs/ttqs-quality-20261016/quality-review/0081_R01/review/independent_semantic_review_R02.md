# Independent exact-SHA semantic review — DOCX 0081 R02

**Reviewed artifact:** `docs/ttqs-quality-20261016/quality-review/0081_R01/candidate/0081_R02.docx`  
**Rendered PDF:** `docs/ttqs-quality-20261016/quality-review/0081_R01/qa/0081_R02_word_render.pdf` (13 pages)  
**Controlling sources checked:** Human Mission, genre manual, 157 blueprint row 086, official evidence table PDF page 6/17b, unique blueprint 0081 R01, upstream 0080 R05, replacement register R02.

## Identity verification

| Item | Result |
|---|---|
| `observed_docx_sha256` | `5b77683da206a9973f132c2222775aa22d96ffb7b24042cdb6230d6875db04e3` |
| Expected DOCX SHA | `5b77683da206a9973f132c2222775aa22d96ffb7b24042cdb6230d6875db04e3` |
| Identity | **PASS** |
| Body SHA-256 | `653bc92095889fa0b3c39a3d126bce86245aa902f8649da054119a47ddb71640` (matches expected; body/table content unchanged from R01) |
| Rendered PDF SHA-256 | `f036d375e48907083476e6c3d4df5f06a3e5d09a0a12794bd4e9dd0292dd524b` |
| Unique blueprint SHA-256 | `ea24a5986af99c2c6b8e68075e64c2e1d0a8702ab3c4434d94120191de3fde18` |
| Replacement register SHA-256 | `6ff60cb1e14bc0030562d26e38dc6e2f0061bd8c62fbb846e9478f913a6aab65` (23 data rows) |
| Controlling source SHAs | All match the values recorded in Appendix A (mission, genre manual, 157 blueprint row 086, official PDF, upstream 0080 R05 DOCX/body/blueprint, 0076/0077/0079 chain evidence) |

## Verdict

**PASS — semantic scope.**  
No blocking semantic defect was found. The document is internally consistent with its controlling sources, preserves the required SAMPLE/REAL boundary, and correctly keeps all real A1–A7 progress as `REAL=UNKNOWN/HOLD`.

This verdict is a semantic-review result only. It does **not** modify the file, grant formal acceptance, or change the real-evidence status:

- `REAL=UNKNOWN/HOLD`
- `formal_acceptance=NOT_GRANTED`
- official checkbox 086 = `PARTIAL/HOLD` (textual demonstration only)

## Substantive checks passed

1. **Genre and boundary control (PDF pp. 1–2, 12; body §§1.5, 12.1)**  
   The document is clearly a closeout/action-plan verification record, not 0080 course redesign, 0075 reaction improvement, 0079 individual advice, 0082 behavior transfer, or 0072 full institutional closeout.

2. **Official 17b / checkbox 086 alignment (PDF p. 2; body §2.1; official PDF p. 6)**  
   The 0/1/2/3 grading semantics match the official table, and the document correctly maps itself to “結案報告書、課後訓練機構的課程檢討行動計畫查核紀錄” without claiming any achieved level.

3. **Real A1–A7 ledger (PDF pp. 3–4; body §3.1, table 3)**  
   All seven actions remain `UNKNOWN/HOLD`, with required real evidence listed. No action is overstated as approved, assigned, executed, verified, or passed.

4. **Synthetic scenario isolation (PDF p. 5; body §5)**  
   `SCN-0081-001` and `SYN-0081-2026-B01` are explicitly marked invented/sample/not executed. `VERIFIED-SAMPLE` is confined to the labeled synthetic scenario and is not presented as real execution.

5. **Evidence-quality rules (PDF p. 5; body §5.2–5.3)**  
   EQ3 authorization failure and EQ7 attribution failure correctly force `HOLD`/return. A6 is correctly marked as the failed action; A2 and A4 are correctly reopened rather than reported as improved.

6. **Next-cohort mathematics (PDF pp. 7–8; body §§7.4–7.8, Appendix B)**  
   Verified:
   - C1–C5 = 20, 15, 18, 16, 16 = 85/120 = 70.83%
   - participant totals = 9+8+8+7+7+8+9+6+7+8+5+3 = 85
   - average = 7.08/10
   - pass/hold = 6/12 and 6/12 = 50.00% each
   - critical-error hold = 2/12 = 16.67%
   - academic total = 198/240 = 82.50%
   - Q01 9/12 = 75.00%; Q17 8/12 = 66.67%; Q18 10/12 = 83.33%; Q19 8/12 = 66.67%
   - C2 15/24 = 62.50%; C5 16/24 = 66.67%

7. **Causality boundary (PDF p. 8; body §7.10)**  
   The document correctly states that B01 and A01 are different cohort/people/time, that no causal attribution to A1–A7 is permitted, and that behavior transfer remains in 0082/17c/088.

8. **Cross-document fact linkage (PDF pp. 3, 12; body §§2.4, 12.1)**  
   Case ID, cohort n=16, weak items Q01/Q17/Q18/Q19 = 11/16, 0–2 five-criterion rubric, and proposed 8/10 threshold all match upstream 0080 R05. The document does not reproduce 0079 individual card content.

9. **Replacement register and return conditions (PDF p. 11; body §11)**  
   The 23-row register covers the required groups, all rows remain `REAL=UNKNOWN/HOLD`, and the return/hold conditions include blank-table abuse, false approval, causal overclaim, privacy, and version mismatch.

10. **Data protection (PDF p. 11; body §11.4)**  
    Only de-identified group summaries are used; no names, contact details, IDs, images, or 0079 individual card details appear.

## Page/section locator map used for this review

| PDF page | Main content |
|---|---|
| 1 | Cover, warning, §§1.1–1.2 |
| 2 | §§1.3–1.5, §§2.1–2.2 |
| 3 | §§2.3–2.5, §3.1 (real A1–A7 ledger begins) |
| 4 | §3.2–3.3, §4 (gaps/missing evidence) |
| 5 | §5 (synthetic scenario `SCN-0081-001`, EQ1–EQ7, decisions) |
| 6 | §6 (closeout summary, group-level) |
| 7 | §7.1–7.4 (B01 method, criteria, denominator, threshold) |
| 8 | §7.5–7.7 (item, learner, pass/hold results) |
| 9 | §§7.8–7.10, §8, §9 |
| 10 | §10 (reusable blank form) |
| 11 | §11 (replacement register, return/hold, privacy) |
| 12 | §12 (cross-document positioning and closeout judgment) |
| 13 | Appendix A SHAs, Appendix B calculations, Appendix C glossary |

## Non-blocking observations

1. **Revision-label mismatch (PDF p. 2, §1.3 table; PDF p. 11, §11.1)**  
   The artifact reviewed is `0081_R02.docx`, but the internal candidate label still reads `R01` in the status table, and §11.1 names the register as `SYNTHETIC_REPLACEMENT_REGISTER_0081_R01.csv`. The actual reviewed register is `..._R02.csv`. Because the body/table content is unchanged from R01 and R02 is a layout-only revision, this does not block semantic acceptance, but the next revision should relabel both references to R02.

2. **Document self-description (PDF p. 1)**  
   The DOCX still states it has not undergone independent semantic review. That statement was accurate before this review; this verdict supplies the independent semantic-review result, but it does not itself convert the candidate into an accepted document.

## Final status

- `REAL=UNKNOWN/HOLD`
- `formal_acceptance=NOT_GRANTED`
- Official checkbox 086 = `PARTIAL/HOLD` (textual demonstration only)
- No files were modified, no Computer Use was used, and nothing was published.
