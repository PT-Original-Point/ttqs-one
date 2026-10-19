# Read-only exact-SHA delta review: DOCX 0081 R03

Review the actual attached DOCX bytes. Do not edit or create files, use Computer Use, publish, or run a broad repeat review. Respond in ASCII-only English so the receipt remains lossless in the Windows CLI encoding.

R02 received an independent semantic PASS at SHA `5b77683da206a9973f132c2222775aa22d96ffb7b24042cdb6230d6875db04e3`. The full R02 review is attached. Its only non-blocking findings were three stale administrative references. R03 is a narrow correction only:
1. Cover no longer says semantic review has not occurred; it says review state is governed by exact-SHA receipts, while retaining CANDIDATE_ONLY and NOT_GRANTED.
2. Status table labels the current candidate R03.
3. Section 11.1 points to register R03; all 23 CSV source paths now point to the R03 body. Every row remains REAL=UNKNOWN/HOLD.

Candidate DOCX path: `docs/ttqs-quality-20261016/quality-review/0081_R01/candidate/0081_R03.docx`
Expected exact SHA-256: `afad7608a1e85dd479eb655724cc2ce42cf5f91f0f9bb59d6f601b3b31b56201`
Expected PDF SHA-256: `8d433014ccf8137c4cdafa1f4df5e7c01e6670efded5089ce55044dfeb13fdf0` (13 pages).

Verify: (a) observed DOCX SHA equals expected; (b) the DOCX contains the three corrections and no stale R01 candidate/register label; (c) substantive text/tables/numbers are unchanged from R02 apart from those three metadata corrections; (d) the register has 23 rows, correct R03 body path, and no REAL promotion; (e) page 1, page 2, and page 11 in the PDF remain readable and correctly laid out; (f) the prior R02 semantic PASS still applies to the unchanged substantive content. If any additional difference or substantive defect is found, identify its exact page/section and do not pass by assumption.

Return observed SHA, identity result, delta verdict PASS/PARTIAL/FAIL, six checks above, exact locators, and state `REAL=UNKNOWN/HOLD`, `formal_acceptance=NOT_GRANTED`. This is only an exact-SHA candidate review.
