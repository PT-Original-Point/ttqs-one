# Independent semantic review — DOCX 0082 R05

## Verdict

**PASS — candidate quality only.**  
Exact candidate DOCX SHA-256: `20fba40c9ef7f0e09f5b9cd6ea94b754c0be23a3d1b9c64167505a8bc8c4aa5d`  
Candidate body SHA-256: `583fa20e9c6f1a3b0ba7071b8dc542f3224720617b73b1dbdd62cf24803b094b`

This verdict covers **semantic/internal consistency of the candidate only**. It does **not** grant formal acceptance, and it does not establish any real association activity, real response, real observation, decision, execution, or approval.

---

## Requirement mapping

- DOCX `0082` = requirement `I17C-E01` = official checkbox serial `088` (body §1 Table 1; §14 Table 20).
- Distinct from `0083` = `I17C-E02` = checkbox `089`, which is only pointed to, not asserted to exist or be completed (body §1; §4.4; §11.4; §14 Table 20).
- Source: official TTQS evidence table p. 6, indicator 17c; 157 blueprint section I17c, item 088 (body §1; technical review receipt).

---

## Findings — PASS

1. **Identity and boundary** — PASS  
   - Locators: body §1 Table 1; §2 Table 2 (N-01–N-09); §14 Table 20.  
   - The document repeatedly binds itself to `0082 / I17C-E01 / 088` and distinguishes `0083 / I17C-E02 / 089` as a separate follow-up pointer only.

2. **Correct genre and usable content** — PASS  
   - Locators: body §0; §6; §7; §8; §9; §11; Tables 11–16.  
   - Contains a respondent-facing reusable blank questionnaire, a complete worked synthetic example, cohort return matrix, calculations, interpretation, and HOLD/RETURN/REJECT rules. It is not framed as a reaction survey, closure report, appraisal, or action-plan tracker.

3. **B1–B6 wording now aligns with Blueprint R02 §6.1; C1 measures the corresponding behavior** — PASS  
   - Locators: body Table 9; §5.3; §6; §7.3; Table 12.  
   - B1–B6 are service-record completeness, closed-loop handoff, explicit consent before sensitive information, fact/inference distinction, pre-handoff required-field verification, and error-correction trace update. C1 asks past-30-day execution of “交接閉環,” matching B2. This closes the prior R04 alignment gap.

4. **Frequency/opportunity and response-state distinctions are operational** — PASS  
   - Locators: body §5.1–§5.4; Tables 6–10; Appendix A.  
   - `N/O`, score `0`, and blank/nonresponse are defined and handled separately. `N/O` and blanks are excluded from denominators and are not treated as zero.

5. **Follow-up interval, dates, reminders, and statuses are coherent** — PASS  
   - Locators: body §4.1–§4.4; Tables 4–5; §5.4.  
   - Demonstrated chain: A3 `2026-08-15` → A5 `2026-09-14` = exactly 30 days for `INT-30`; due date `2026-09-21`; reminders `2026-09-17` and `2026-09-20`; response date `2026-09-15` is within due date. Statuses, skip logic, and completeness rules are stated and internally consistent.

6. **Cohort counts, denominators, means, and changes independently verified** — PASS  
   - Locators: body §9.1–§9.3; Tables 13–15; Appendix B; data/QA receipt.  
   - Issued 12; returned 10; valid 9; invalid 1 (`BTR-10`, EX-1); not returned 2 (`BTR-11`, `BTR-12`).  
   - Item denominators: B1 9, B2 8, B3 7, B4 9, B5 8, B6 5; total 46.  
   - `N/O` counts: 0, 1, 2, 0, 1, 3 = 7; missing = 1; `46 + 7 + 1 = 54 = 6 × 9`.  
   - Pre sum 69; current sum 133; means 1.500 and 2.891; change +1.391.  
   - Opportunity rates: 100.00%, 88.89%, 77.78%, 100.00%, 88.89%, 55.56%.

7. **Proposed gate and HOLD result are correctly applied** — PASS  
   - Locators: body §10; Table 16.  
   - Gate: opportunity ≥ 60%, current mean ≥ 3.0, change ≥ +1.0. Only B3 passes. B6 fails on opportunity rate (`55.56%`). Result: `1/6 = 16.67%`, therefore `HOLD/REVERIFY` with referral to `0083/089` as a pointer only.

8. **Synthetic boundary is preserved** — PASS  
   - Locators: body §7.7; §11; §12; §14; Table 20.  
   - `BTR` respondents are not mapped to `0073` `S01–S16` or `0074` `P01–P16`. `0073 R08` is treated as reaction-only, `0074 R01` as proposed, and `0083/089` as a separate follow-up pointer. No real association course, response, observation, decision, execution, or approval is implied.

9. **Privacy, consent, minimization, proxy, replacement register, and hold/reject criteria are usable** — PASS  
   - Locators: body §9; §10; §12; §13; Table 19.  
   - De-identification, consent scope, minimization, proxy marking, replacement-register schema, real-source replacement requirements, and explicit hold/reject conditions are present. Current retention/consent/withdrawal regulations are explicitly marked `REAL=UNKNOWN/HOLD`, not claimed as available.

10. **Rendered usability** — PASS with minor nonblocking whitespace only  
    - Locators: visual review receipt; rendered PDF pp. 6, 10, 13, and 17.  
    - The visual review reports all 17 pages inspected, no clipping, no table overflow, no header/footer overlap, and legible tables. Sparse pages are recorded as a nonblocking layout limitation.

---

## Findings — PARTIAL / nonblocking alignment notes

1. **Verdict vocabulary differs from Blueprint R02 §8.1** — low severity  
   - Locators: body §11.1 Table 17; blueprint §8.1.  
   - Body uses `DEMO_MEETS`; blueprint uses `PASS-SAMPLE`. Definitions are equivalent. No arithmetic, identity, or denominator effect.

2. **Negative-test table is shorter than Blueprint R02 §3.2** — low severity  
   - Locators: body Table 2; blueprint §3.2 (N-10, N-11).  
   - The substance of N-10 (do not present thresholds as policy) and N-11 (do not map synthetic respondents to real persons) appears in body §10 and §7.1, but those two rows are not listed in the negative-test table.

3. **Reminder schedule wording differs from Blueprint R02 §5.3** — low severity / blueprint appears internally inconsistent  
   - Locators: body Table 5; blueprint §5.3.  
   - Body uses reminders at +3 and +6 days with due date at +7 days, which is internally coherent and QA-validated. Blueprint text says +7 and +14 days, which is not operationally usable with the same +7-day due date. The candidate’s schedule is the more coherent implementation.

4. **A8 composite label is not one of the listed role options** — minor  
   - Locators: body Table 11 (A8 `服務紀錄／交接執行`); §5.3 (A8 options).  
   - The demonstrated value combines two role categories. This does not affect calculations or identity.

---

## Findings — FAIL

None identified.

---

## Evidence boundary

The evidence supports **candidate review only**. It does **not** support real or formal acceptance. `REAL=UNKNOWN/HOLD` and `formal acceptance NOT_GRANTED` remain in force. The synthetic self-report, selected evidence-source labels, proposed thresholds, and demonstrated cohort must not be treated as independent observation, causation, verified workplace performance, or association approval.

---

## Scope limitations

- No local DOCX file was available in the review workspace; review relied on the provided extracted DOCX text projection, source packet, blueprint, locked synthetic dataset, data/QA receipt, technical receipt, and visual receipt.
- Direct PDF rendering was not independently inspectable by this model; the visual-review receipt was used for page-count, dimension, clipping, table, and whitespace findings.
- Exact section-to-page mapping beyond the visual receipt’s reported whitespace pages was not independently reconstructed.
