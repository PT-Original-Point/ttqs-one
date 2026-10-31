# UNIQUE_BLUEPRINT_0112_I18-E21_R01

## Exact binding and purpose

- Project: TTQS_ONE.
- Document ID: 0112.
- Official requirement ID: I18-E21.
- Official printed checkbox serial: UNKNOWN_NOT_ASSERTED.
- Crosswalk title: 輔導考照及學員回訓率追蹤分析表.
- Official source: current official PDF, page 7, indicator 18, four-point example: 「輔導考照及學員回訓率持續提高。」
- Unique purpose: a practical cohort tracker and trend-analysis tool showing separately whether documented certification coaching and learner retraining increase over comparable periods, with traceable evidence and follow-up actions.
- This is not the 0104 certificate acquisition report, 0110 perception survey, or 0111 special/social outcome register.

## Intended user and association fit

A small volunteer association training administrator can maintain this tool with role codes and a simple paper or spreadsheet register. Suggested roles are 行政承辦、課程聯絡人、覆核者; these are recommendations, not evidence of appointment or legal authority. Do not assume an HR department, employed learners, a standing committee, or a particular certification body.

## Required document anatomy

1. Cover and quick-use panel: purpose, user role, update timing, reporting window, output, SAMPLE/REAL status, and stop conditions.
2. Definitions and eligibility: distinguish coaching offered, coaching received, exam eligibility, retraining eligibility, invitation, exam attempt, verified credential, completed retraining, and matured follow-up window.
3. Cohort register: cohort ID, coded learner ID, eligibility reason, coaching date/type, exam plan/window, retraining eligibility/due window, consent/privacy state, source locator, status, and follow-up owner role. No names or identity numbers in the public sample.
4. Certification coaching follow-up: eligible learners, coaching received, exam attempted, verified credential earned in the stated window, pending proof, withdrawal, and ineligible cases.
5. Retraining follow-up: eligible learners, invited, completed within the stated window, not completed, declined, unreachable, withdrawn, and missing evidence. Invitations never count as completion.
6. Separate trend analysis: show cohort size, numerator, denominator, rate, percentage-point change, comparable-period decision, and missing-data count for each measure. Do not pool measures or double-count a learner within one cohort.
7. Completed SAMPLE case: use only SYN-0112-CASE-01 and synthetic period codes SYN-P1, SYN-P2, SYN-P3. Invented data must be conspicuously labeled SAMPLE/SYNTHETIC and must not claim association outcomes.
8. Action and review log: each gap links to an action, responsible role code, due date, evidence to collect, follow-up date, status, and disposition CONTINUE / REVISE / HOLD / CLOSE. A rising rate does not clear missing-evidence cases.
9. Coding and calculation rules: define duplicate, ineligible, pending, not-yet-due, withdrawn, missing proof, declined, and zero-denominator handling. Do not silently remove unfavourable cases.
10. Evidence and privacy controls: evidence reference, source type, date/window, custodian role, consent/legal-basis state, permitted summary use, verification status, retention-policy reference, and redaction state. Unknown policy or permission means HOLD.
11. Requirement traceability and replacement register: official clause → field/metric → source reference → calculation → conclusion → follow-up action; fact-level register marks every sample datum and replacement instructions.
12. Real-data replacement and version control: replace sample values only with authorized source records, recompute, preserve prior hashes, and keep protected originals out of public repositories unless explicitly authorized.

## Operational definitions for the sample tool

The official source does not define denominators. These proposed definitions are for demonstration and require association approval before REAL use:

- Certification coaching completion rate = eligible coached learners with a verified credential earned within the stated window / all eligible coached learners whose exam follow-up window matured × 100.
- Retraining completion rate = eligible learners with verified completed retraining within the stated window / all retraining-eligible learners whose retraining window matured × 100.
- Report invitations, attempts, pending results, withdrawals, not-yet-matured windows, and missing proof separately. Do not convert self-report to verified completion.

## Complete illustrative data and calculations

SAMPLE/SYNTHETIC ONLY, case SYN-0112-CASE-01:

| Period | Certification numerator/denominator | Rate | Retraining numerator/denominator | Rate |
|---|---:|---:|---:|---:|
| SYN-P1 | 3/8 | 37.5% | 4/10 | 40.0% |
| SYN-P2 | 4/8 | 50.0% | 6/10 | 60.0% |
| SYN-P3 | 5/8 | 62.5% | 7/10 | 70.0% |

- Certification change: P1→P2 +12.5 percentage points; P2→P3 +12.5 points; P1→P3 +25.0 points.
- Retraining change: P1→P2 +20.0 points; P2→P3 +10.0 points; P1→P3 +30.0 points.
- These are separate descriptive sample trends. They do not establish REAL performance, statistical significance, or causality. Period comparability and matured windows must be shown before interpreting a trend.

## Mandatory reject / hold conditions

- HOLD if the cohort or eligibility rule, follow-up maturity, numerator, denominator, source, consent/privacy basis, or custodian is missing or inconsistent.
- HOLD if credential or retraining completion is self-reported without the required authorized verification.
- HOLD a window that has not matured; do not code it as a success or failure.
- Reject duplicates, duplicate credentials, unapproved reclassification, mixed cohort definitions, invitation-count denominators, untracked withdrawals/unreachable cases, or unsupported improvement claims.
- HOLD if an actual target or retention policy lacks authorization; never invent association thresholds or retention periods.
- SAMPLE_ONLY when all values are synthetic; never silently promote them to REAL.

## Nearest-document distinction

- 0104 / I18-E11: certificate acquisition-rate analysis. 0112 follows the coached cohort and retraining lineage; do not copy its denominator or treat the outcomes as interchangeable.
- 0110 / I18-E19: perception questionnaires and an after-course action plan. Perceptions do not verify credentials or retraining completion.
- 0111 / I18-E20: special/social performance register. Do not substitute its claims for certification or retraining measures.

## Build and review entry gate

A DOCX candidate is ready only after a fact-level synthetic dataset and independent Python recomputation prove every row, denominator, rate, percentage-point change, and disposition; all forms are usable; the replacement register is complete; and every sample fact is visibly labeled. Independent review must bind the final exact DOCX SHA and cover official mapping, genre, usability, math, adjacent-document separation, SAMPLE/REAL boundary, and rendered pages. Technical success alone is not acceptance.
