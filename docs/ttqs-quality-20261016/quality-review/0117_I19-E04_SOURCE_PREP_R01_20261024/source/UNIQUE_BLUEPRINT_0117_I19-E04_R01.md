# UNIQUE BLUEPRINT — Document 0117 / I19-E04 — R01

## Exact mapping
- doc_id: `0117`
- official requirement: `I19-E04`
- unique Blueprint internal index: `128`
- internal content direction: `考照提升口述：分母/追蹤證據未備`
- document title: `學員考照通過率追蹤及分析表`
- official printed checkbox serial: `UNKNOWN_NOT_ASSERTED`
- source hashes: see `source_manifest_0117_R01.json`.

## Document genre and reader
Operational examination/certification outcome tracker and analysis sheet for a small association training administrator and a reviewer. It must be directly usable to freeze a cohort, log each eligible participant's first sitting and retake separately, reconcile source evidence, calculate rates, flag missing inputs and record a decision.

## Required original contents
1. Cover/control block: course/cohort, completion date, 90-day window, certification/exam code and version, issuer source, record custodian role, review date, version, SAMPLE/REAL status. Use roles, not invented staff names or approvals.
2. Metric dictionary with exact numerator, denominator, exclusions, unit and interpretation for first-sit pass rate, participation rate, eventual 90-day pass rate and eligible pass yield.
3. Cohort eligibility and freeze form: entry rule, duplicates, withdrawal, no-show, no-attempt, late result, incomplete and missing source handling.
4. Person-level anonymized tracking form with first attempt date/result/score reference, retake date/result, no-attempt reason, evidence index, verification status and protected identity-map location.
5. Attempt-level audit log or equivalent fields so retakes do not inflate person counts.
6. Complete two-cohort SYNTHETIC dataset (8 baseline + 10 current) and a clearly labelled illustrative comparison using the source packet arithmetic. Scores, threshold and all outcomes must remain SAMPLE.
7. Issuer/third-party evidence route: lawful source, original document or approved verification, date, version, custodian, independent verifier, storage/retention/access and redaction rules. Do not fabricate a certificate or issuer confirmation.
8. Analysis worksheet: actual formulas, denominator reconciliation, percentage-point differences, missing/non-attempt sensitivity, comparison comparability, small-n limitations, non-causal wording.
9. Decision/action log: discrepancy, finding, cause hypothesis, action, responsible role, due date, evidence needed, close criteria and recheck date. Sample entries are labeled synthetic and not association decisions.
10. Real-evidence replacement register with required source, acceptance checks, status and hold/reject conditions.

## Synthetic values (must exactly reconcile)
- Baseline: eligible 8; first valid sittings 6; first-sit pass 3; failed-first-sit 3; retake within window 1, one eventual pass; non-attempt 2.
- Current: eligible 10; first valid sittings 8; first-sit pass 5; failed-first-sit 3; retake within window 1, one eventual pass; non-attempt 2.
- First-sit: 50.0% → 62.5%, +12.5 percentage points.
- Eventual 90-day: 66.7% → 75.0%, +8.3 percentage points.
- Eligible pass yield: 50.0% → 60.0%, +10.0 percentage points.
- Participation: 75.0% → 80.0%, +5.0 percentage points.
All values are synthetic demonstrations only. No causal or statistically significant improvement may be claimed.

## Mandatory hold / reject rules
HOLD if cohort source/freeze cannot be verified, exam version or official threshold is unknown, issuer result is missing or permission/source authority is unconfirmed, an identity mapping is unprotected, windows are incomparable, denominator reconciliation fails, consent/privacy policy is unresolved, or a real pass/increase claim cannot be independently verified. Missing result is UNKNOWN, not FAIL.
REJECT an inapplicable/duplicate record, a result outside the approved period, an invalid exam version, a fabricated certificate/issuer statement/approval, a row with exposed personal identity in public evidence, or a calculation that counts attempts as people. Stop publication of the affected statement; do not stop unrelated documents.

## Cross-document no-mix rules
0116/I19-E03 is employment follow-up; 0117/I19-E04 is exam/certification outcomes; 0115/I19-E02 is knowledge sharing. No shared synthetic or real denominator, cohort, outcome, or `fact_id` unless a lawful source manifest explicitly proves identical cohort, period and provenance. Do not use 0117 as an employment survey or claim that an exam pass proves employment.

## Acceptance tests for a future DOCX
- exact doc_id/requirement/internal Blueprint mapping and unknown official printed serial are visible;
- operational tables/forms contain all required fields and decision paths, not placeholder-only pages;
- all 18 synthetic participant records reconcile to cohort totals and formulas above;
- first-sit vs retake vs 90-day eventual outcomes are distinct; no duplicate learner numerator;
- source, permission, verification, privacy and retention controls are usable;
- sample calculations recompute exactly, with no real-performance inference;
- evidence register and hold/reject rules allow the administrator to act;
- cross-document exclusions are explicit;
- Word body font >=10.5pt, table font >=9.5pt; Word-native render visually reviewed on every page;
- independent semantic review is tied to the final exact DOCX SHA; formal acceptance remains separate.
