# 0117 / I19-E04 source packet — R01

## Binding identity and source provenance
- Document ID: 0117. Official requirement ID: I19-E04. One deliverable maps to this requirement: `學員考照通過率追蹤及分析表`. The exact local 129-to-142 crosswalk and blueprint-seed file SHA-256 values are in `mapping_evidence_0117.json`.
- Current GitHub PR #92 157 Blueprint internal index 128 describes “考照提升口述：分母/追蹤證據未備”. This index is an internal Blueprint locator, not the official printed checkbox serial. Printed serial remains UNKNOWN_NOT_ASSERTED.
- Official checklist source: `official_source_0108_r11.pdf`, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`. The item begins on p.7 and continues on p.8. Exact item text: “學員考照通過率有增加，但未有具體紀錄及評量。” Extracted full source pages and local page images are in this source-preparation folder.
- Current PR #92 source blobs: `03_157_CHECKBOX_BLUEPRINTS.md` 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63; `02_GENRE_WRITING_MANUAL.md` 4ff863d9f534b6359fc1c7c1685bd8cce02da886; `01_HUMAN_MISSION_AND_ACCEPTANCE.md` 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e.

## Document purpose and boundaries
This is a usable certification/exam outcome tracking and analysis form. It records a frozen eligible cohort, exam/certification identity and version, first attempt, retake, 90-day result window, evidence index, missing/non-attempt status, calculations, review, action and recheck. It is not an employment survey, satisfaction form, certificate, or claim that the association actually improved pass rates.

All rows, scores, exam code, dates, cohorts, results, threshold and changes in the supplied dataset are SAMPLE_SYNTHETIC_ONLY. No real learner, issuer, exam, certificate, consent, pass result, association approval or third-party source is supplied. Real pass rate, real increase, and real evidence status remain UNKNOWN/HOLD. Do not publish names or certificate numbers. For REAL operation, keep identity mapping and originals in a restricted repository; the public register holds only a safe evidence reference.

## Reconciled synthetic demonstration
The 70/100 pass threshold is invented for SAMPLE arithmetic and does not assert any issuer's rules. Baseline cohort: 8 eligible, 6 first sittings, 3 first-sit passes, 3 first-sit fails, 2 non-attempts; one failed learner passes a retake inside the 90-day window. Current cohort: 10 eligible, 8 first sittings, 5 first-sit passes, 3 first-sit fails, 2 non-attempts; one failed learner passes a retake inside the 90-day window. Retakes are persons already in the first-sit denominator and never extra people.

- First-sit pass rate: 3/6=50.0% vs 5/8=62.5%; delta +12.5 percentage points.
- Eventual pass within 90 days: 4/6=66.7% vs 6/8=75.0%; delta +8.3 percentage points.
- Eligible pass yield: 4/8=50.0% vs 6/10=60.0%; delta +10.0 percentage points.
- First-sit participation: 6/8=75.0% vs 8/10=80.0%; delta +5.0 percentage points.

Small synthetic cohorts demonstrate record structure and arithmetic only; they do not establish association performance, causality, statistical significance, or an actual increase. Missing issuer results are UNKNOWN/HOLD, not failures. Non-attempts remain visible in the eligible denominator, but not in the valid first-sit denominator. Retakes are tracked separately.

## Cross-document boundaries
0116 / I19-E03 concerns post-training employment status; 0117 / I19-E04 concerns certification-exam outcomes. They have distinct synthetic cohorts and denominators and cannot borrow rows or claim a shared REAL cohort. 0115 / I19-E02 is knowledge-sharing evidence, not an exam record. Any future shared real fact requires authorized source references proving the same cohort, period and provenance.
