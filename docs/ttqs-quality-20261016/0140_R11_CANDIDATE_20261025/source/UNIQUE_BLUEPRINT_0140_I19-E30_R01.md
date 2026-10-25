# DOCX 0140 / I19-E30 Unique Blueprint R01

## Identity and binding
- Project `TTQS_ONE`; DOCX `0140`; requirement `I19-E30`; 157 list index `154`; printed checkbox serial `UNKNOWN`.
- Official title: `訓練資訊系統使用普及率盤點與分析表`.
- Official source: TTQS training-institution evidence table, page 9; exact relevant phrase `運用資訊系統普及率。`
- Genre: `使用情形盤點表＋採用率分析報告＋可供真實填報的操作表單`.
- The official tier reference is not a score assignment. This document must not claim a rating or achievement.

## Unique purpose, reader and evidence role
Enable an association training administrator to define the people and tasks that should use a training information system, measure actual substantive use over a stated period, find role/workflow gaps, and assign a verifiable improvement action. A reviewer must be able to recalculate the denominator and numerator from the included de-identified SAMPLE dataset and identify what real source would replace each synthetic fact.

This is specifically adoption/penetration of a training information system. It is not the I14-E05 document-management/retrieval-speed study, and it is not the I19-E29 certificate/employment outcome report. Account creation, a login, or a claim that a system exists does not count as substantive use.

## Source of truth and prohibited assumptions
Authority order: latest Human Mission and current 01–03 GitHub contracts; official page 9; 142 crosswalk title/ID; this Blueprint; then verified artifact. No live association system, users, activity logs, outcomes, or approvals were located in the scoped sources. Therefore the entire numeric case is `SAMPLE/SYNTHETIC`; `REAL=UNKNOWN/HOLD`. The generic label `SAMPLE-TIS-01` is invented solely for the demonstration and is not a vendor or association deployment.

## Operational definitions and formulas
1. Measurement window: one stated calendar period (sample: 2023, 2024, 2025); compare periods only with the same eligibility and activity definitions.
2. Eligible unique user: one distinct, pseudonymous person in a defined role (training administrator, instructor, or learner) who was assigned at least one required training task that the system is intended to support during that window. Count a person once per period, even if they attended multiple courses. Include eligible people with no account or no activity in the denominator. Exclude only documented out-of-scope roles/tasks, and record exclusions separately.
3. Active user: eligible unique user with at least one system-recorded substantive training workflow transaction during the window. A provisioned account, password reset, or login without a completed task is not active use.
4. Adoption/usage prevalence = active eligible unique users ÷ eligible unique users × 100%. Report numerator, denominator, period, role breakdown, and rounding.
5. Required-workflow completion rate among eligible users = users completing all role-specific mandatory system tasks ÷ eligible unique users × 100%. Also report completion among active users, but label its denominator separately.
6. Percentage-point change = later adoption rate − earlier adoption rate. Relative change may be reported only as `(later−earlier)/earlier ×100%` when the earlier rate is non-zero. Do not call percentage-point change a percent change.
7. De-duplicate using a protected source key before pseudonymization; no personal names, IDs, phone numbers, emails, or credentials in the public candidate. Logs are an example source locator only, not evidence that such logs exist.

## Fixed synthetic worked dataset
The included CSV contains 80 synthetic unique user-period records. Role totals:
- 2023: administrators 2/3 active and 2/3 complete; instructors 2/4 active and 1/4 complete; learners 8/13 active and 6/13 complete. Total 12/20 active; 9/20 complete.
- 2024: administrators 3/3 active and complete; instructors 4/5 active and 3/5 complete; learners 15/20 active and 12/20 complete. Total 22/28 active; 18/28 complete.
- 2025: administrators 3/3 active and complete; instructors 5/6 active and complete; learners 20/23 active and 17/23 complete. Total 28/32 active; 25/32 complete.
- Overall: 62/80 active; 52/80 complete.
Calculated adoption: 2023 60.00%; 2024 78.57%; 2025 87.50%; changes +18.57pp, +8.93pp, and +27.50pp (2025 versus 2023). The example is internally consistent but has no association-performance meaning.

## Required document sections and tables
1. Cover/first-glance card: purpose, reader, when to use, key result, actions, and clear SAMPLE/REAL status.
2. Official requirement and scope mapping (DOCX ID, requirement ID, 157 index, printed serial UNKNOWN, official page).
3. One-page annual system inventory form: system/module, owner role (not a named actual person), covered courses/tasks, eligible roles, period, data source and exact locator, privacy check, and limitations.
4. Eligibility and substantive-activity rules, with include/exclude examples and decision flow.
5. Full SAMPLE system/workflow description and role-to-required-task matrix.
6. Complete 80-row pseudonymous sample register in the appendix; each row shows period, synthetic ID, role, required workflow, required task count, actions completed, active flag, completion flag, and synthetic log reference. Do not omit non-users.
7. Period-by-role count table and a fully reconciled 3-year summary table; independently recalculate every total and rate from the 80 rows.
8. Trend analysis with adoption and completion kept separate; show numerator/denominator, percentage-point changes, explanation limits, and a role-gap diagnosis.
9. Directly usable form: new period data capture, source reconciliation, exception log, review sign-off fields left as unsigned/unapproved workflow fields (not fabricated signatures).
10. A SAMPLE action plan with owner role, due interval, measurable follow-up, evidence locator expected, and HOLD/REVISE triggers. Do not state that the association adopted or completed it.
11. Fact-level synthetic replacement register; map every synthetic period, ID, count, formula, event reference, action, and conclusion to the real record required and secure replacement method.
12. Evidence locator and reviewer checklist; distinguish existing real evidence from evidence requested/absent.

## Sample workflow tasks
- Administrator: course/roster setup, eligibility confirmation, close-out/evaluation export (3 required tasks).
- Instructor: attendance or assessment recording and post-session instructional close-out (2 required tasks).
- Learner: enrolment confirmation, attendance/learning acknowledgement, post-course evaluation (3 required tasks).
The tasks are generic synthetic examples. Real role duties must be confirmed against the association's approved process before using them.

## Acceptance and rejection controls
- Title-blind reading identifies a training-system adoption inventory/analysis, not records-retention/retrieval speed or training outcomes.
- A user can fill the inventory, derive the denominator, classify activity, calculate rates, reconcile role counts, identify missing evidence, and assign follow-up.
- All 80 sample rows roll exactly to the stated totals; formulas can be recomputed; `active=0` means zero substantive actions; completion implies active.
- Account existence/logins alone are not counted; denominator excludes no eligible non-user.
- `SAMPLE/SYNTHETIC` is prominent on each sample table/page; `REAL=UNKNOWN/HOLD`; no association approval, actual IT product, actual system use, actual score, or actual performance is asserted.
- HOLD if eligibility list, period, event logs, task definitions, data authorization, or denominator cannot be verified. REJECT if login-only metrics, unexplained exclusions, duplicate identities, numerator exceeds denominator, mixed periods/definitions, fabricated records, or the analysis claims an official score.
- Typography: body ≥10.5pt and table text ≥9.5pt, clean page breaks and repeated headers for long register. Include all Word/PDF pages in visual review.

## Cross-document links and negative neighbors
- `0064 / I14-E05`: records classification/retention and retrieval-speed methodology; may provide a control for protecting source logs, but does not establish actual training-system adoption.
- `0139 / I19-E29`: certificate examination and employment follow-up; may share training-period context only if a real linked case ID exists. Its results cannot serve as system-use numerator/denominator.
- Any cross-document case linkage must use a verified shared source key or be labelled synthetic; do not invent one.
