# 0135 Unique Blueprint R01｜I19-E25

## Identity and evidence boundary
- Deliverable: DOCX 0135, 「目標市場與顧客價值具體提升成效分析報告」.
- Official requirement: I19-E25, indicator 19「訓練系統的市場功能—目標市場及顧客的價值創造」; official source PDF pages 7–8. The printed checkbox serial is UNKNOWN; do not substitute document ID 0135 or 157 index 140 for that serial.
- Project evidence mapping: 03_157_CHECKBOX_BLUEPRINTS item 140「市場顧客價值量化：期間/分母/改善幅度」. Items 141 (individual training performance) and 142 (market competition/revenue/process/cost/complaints) are distinct; they are excluded as primary evidence here.
- Genre: quantified market-and-customer-value outcome analysis report. It is not a membership/dues trend report, course-count report, satisfaction-only report, or scoring sheet.
- All supplied metrics and case rows are SAMPLE/SYNTHETIC. No actual association market reach, customers, outcomes, approvals, or third-party facts are asserted.

## Exclusive purpose
Demonstrate how a training institution identifies a target market and measures whether both target-market reach and customer value improved over defined periods. The report must separate reach from value, state denominators and calculation rules, show period-to-period changes, explain decisions, and disclose measurement limits.

## Required report structure
1. Cover, document identity, version, reporting period, SAMPLE/SYNTHETIC notice.
2. Executive finding: two outcome lanes (target-market reach; customer value), periods, denominators, changes, and limitations; no self-awarded TTQS score.
3. Requirement-to-measurement map: official wording, operational definition, evidence location, owner/retention, and missing REAL source.
4. Target-market definition: nonprofit volunteer-organization administrators needing reliable monthly service records; eligibility, exclusions, de-duplication, source frame, and stability checks.
5. Multi-year market reach table for 2023–2025: eligible frame 80 each year; served organizations 20/24/28; rates 25%/30%/35%; changes +5.0 percentage points each year; relative changes +20.0% and +16.7%. Label this frame synthetic and not an external market-size estimate.
6. Customer-value measurement design: matched 2025 organizations, pre-course baseline and 90-day follow-up; response numerator/denominator; administration time and on-time completion measures; collection dates, item wording, missing-data rules, and bias limits.
7. Complete paired SAMPLE table: 15 synthetic case rows from SAMPLE_PAIRED_MEASUREMENT_DATA.csv. Median monthly-record time falls 120→90 minutes (25% reduction). On-time completion rises 8/15 (53.3%)→12/15 (80.0%), +26.7 percentage points. Matched response rate is 15/28 (53.6%) of served organizations. Show formulas and rounding.
8. Analysis: interpret reach and value independently; avoid causal claims because no control group or independent source is supplied. Identify nonresponse, frame stability, attribution, and small-sample limitations.
9. Management decision and action register: what to continue/change, accountable role, due date, evidence to review, and stop/hold trigger. These are proposed SAMPLE decisions only, not association approvals.
10. Cross-document evidence links: 0133/I19-E22 supports training sessions/person-times; 0134/I19-E23 supports membership/dues trends; neither supplies 0135 target-market/customer-value outcomes. Use separate case_id and do not reuse their counts or imply a shared real case.
11. REAL replacement register: list each synthetic field, acceptable primary source, owner, source locator, privacy minimization, reconciliation procedure, and release gate.
12. Evaluator-use checklist and explicit HOLD/REJECT conditions.

## Core formulas
- Annual reach rate (%) = unique served eligible organizations ÷ eligible target-market frame × 100.
- Change (percentage points) = current reach rate − prior reach rate.
- Relative change (%) = (current rate − prior rate) ÷ prior rate × 100.
- Time reduction (%) = (baseline paired median − 90-day paired median) ÷ baseline paired median × 100.
- On-time rate (%) = on-time organizations ÷ matched organizations × 100.
- Response rate (%) = matched follow-up organizations ÷ organizations served in the period × 100.

## HOLD / REJECT conditions
HOLD if target frame criteria or denominators vary without reconciliation; if numerator counts duplicates; if pre/post measurement windows differ; if follow-up or nonresponse denominator is missing; if evidence links cannot be located; if private participant details are exposed; or if a result relies only on satisfaction without market/value measures. REJECT any unlabeled synthetic values presented as REAL, unsupported causal claims, invented customer testimony/approval, undefined market size, or use of 0133/0134 facts as this report’s results. Do not claim level 3 or 4 from the sample.
