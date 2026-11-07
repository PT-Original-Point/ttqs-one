# 0141 I19-E31 專屬 Blueprint R01

## A. 唯一命題與文件用途
本件只處理「顧客滿意度提升」：用相同服務定義、固定問卷核心題、相同 1–5 量尺、可核對的有效分母與多期統計，呈現訓練服務顧客評價的變化，分析限制，並形成下一輪待核准改善建議。它是調查與分析報告，不是評分表、資訊系統使用報告、考照/就業成效報告或營收證明。

## B. 正式對應
- doc_id 0141
- requirement_id I19-E31
- indicator 19, criterion 「顧客滿意度提升。」, weight 4 points (weight only; never claim score)
- 157 blueprint index 155: 「顧客滿意度上升：多期同量尺統計」
- official source locator: training-institution scoring evidence table, physical PDF page 9, criterion 「顧客滿意度提升。」 The 0141 deliverable title comes from the separate 129-to-142 crosswalk row.
- printed checkbox serial: UNKNOWN.
- Neighbor guard: 0139/I19-E29/index153 = licensing/employment; 0140/I19-E30/index154 = information-system uptake; 0142/I19-E32/index156 = revenue. All are different proof constructs.

## C. Intended reader and use
Training administration prepares, fields, cleans and summarizes surveys; responsible officers review customer groups and draft responses; an authorized association role decides whether any proposed change may be adopted. The document must be usable before launch: the questions, scale, timing, invitation denominator, nonresponse treatment, segment fields, analysis formulas, actions, follow-up and hold criteria are visible. Sample decisions are proposals only.

## D. Document structure and required content
1. Cover and status: document identity, report purpose, period, version; label the whole demonstration SAMPLE/SYNTHETIC and REAL evidence UNKNOWN/HOLD.
2. One-page executive finding: exact three-period sample means, response denominator, observed lowest service dimension, interpretation and limits; distinguish sample arithmetic from association performance.
3. Scope and comparability protocol: customer/participant definition, service cohort, sampling frame, invitation unit, response window, eligibility, segment policy, privacy and small-cell controls.
4. Reusable survey administration protocol: dispatch timing, reminder limit, collection channel, coding, invalid/duplicate exclusion, missing/N/A rules, file custody and audit trail.
5. Complete questionnaire: eight exact questions from the source packet, item type, response options, skip/NA handling, respondent segment and service-period metadata. Keep the seven 1–5 items unchanged across periods; Q8 is qualitative and excluded from numeric means.
6. Results: period-level invitation/valid/response counts; six domain-item means and valid n; separate Q7 overall mean and Top-2 rate; customer segment results if supplied; a multi-period table and readable line chart using the same axis. No cross-SHA or cross-construct metrics.
7. Interpretation: compare 2023→2024, 2024→2025 and baseline→final; identify the weakest item, check for scale/response/composition shifts, and state that a small synthetic sample cannot establish causal impact or represent all customers.
8. SAMPLE improvement loop: two hypothetical actions and measurable follow-up, each tied to the observed synthetic item, proposed responsible role, check date/window, success measure and explicit NOT_ADOPTED/NOT_EXECUTED status. Do not describe a proposal as a meeting decision or actual result.
9. Limitations and next-cycle decision table: continue/change/hold choices with explicit evidence required; if valid n, scale, service definition or denominator changed, mark trend not comparable and hold.
10. Appendices: blank reusable capture form plus filled SAMPLE example; data dictionary; 36 response-level SYNTHETIC records; replacement register; formula sheet; source locator and revision record.

## E. Survey protocol and scoring
- Core scale: 1 very dissatisfied, 2 dissatisfied, 3 neutral, 4 satisfied, 5 very satisfied; N/A/not known excluded per item.
- Six domain items are Q1–Q6. Q7 overall satisfaction is separate. Q8 is open text.
- Return rate = valid completed returns / issued invitations. Sample design: 15 invited and 12 valid per year (80%). This is a fictional teaching dataset, not actual sampling.
- Per-item mean = valid response score total / valid answers for that item.
- Six-item index = sum of valid Q1–Q6 scores / number of valid Q1–Q6 answers; only compute respondent-level index when at least 5 of 6 answered. Report item Ns and do not impute.
- Q7 Top-2 = respondents scoring 4 or 5 / valid Q7 answers.
- Trend = later-period value minus earlier-period value on the same five-point scale, reported in points. Do not call it percent improvement. If customer composition, question wording, channel or service changes materially, compare strata only or mark HOLD.
- No causal claim without a verified intervention log and a design supporting attribution.

## F. Canonical synthetic case and item alignment
Canonical SAMPLE fact ID: FACT-SYN-0141-SAT-TREND-R01. Case IDs SYN-0141-YYYY-NNN; 12 complete respondents/year, 3 years; 36 unique IDs; 15 invitations/year; no real personal information. Q5 admin communication is illustrated as improving after a hypothetical notification redesign; Q2 needs/content fit is illustrated as improving after a hypothetical pre-course clarification step; Q7 overall item rises in the sample. These are deliberately synthetic trajectories and cannot support a claim that the association performed either action.
Use the same data file, item wording, scale, period summary and replacement register in the DOCX and its sidecar receipts.

## G. Shared-fact / cross-document boundary
Cross-reference I19-E29/0139, I19-E30/0140, I19-E32/0142 only to distinguish constructs and prevent substitution. Do not reuse their generated narrative, datasets, rates, respondents or claims. Until a verified shared fact source exists, 0141 uses only its own synthetic fact ID and does not assert that the same actual trainees, years, or cohorts appear in adjacent deliverables.

## H. SAMPLE / REAL and authority restrictions
Every generated respondent, date, score, action and narrative is SAMPLE/SYNTHETIC. Real responses require authorized original forms or exports, auditable period and item mapping, protected identity matching, and permission to analyze. Do not invent actual members, instructors, clients, survey returns, approvals, committee decisions, signatures, causal findings, score attainment or formal acceptance. If real data are absent, the example remains complete but visibly synthetic; the real-performance conclusion is UNKNOWN/HOLD.

## I. Exact reject / hold criteria
Reject or hold if: (1) official IDs are conflated; (2) only a blank survey is supplied; (3) periods use different questions/scales without a comparability warning; (4) denominator or valid n is absent; (5) N/A/blank is treated as zero or imputed; (6) Likert point delta is mislabeled as percent growth; (7) nonrespondents disappear without response-rate handling; (8) customer segments are blended despite composition changes; (9) synthetic figures/actions are presented as real; (10) satisfaction is substituted for learning, employment, licensing, revenue or system-use results; (11) a causal claim lacks evidence; (12) no actionable follow-up, owner role, checkpoint or hold rule is provided; (13) no source locator or exact-SHA QA is attached.

## J. Pre-build acceptance gates
- Confirm the official source, row mapping, index 155 and neighbor guard.
- Recompute all sample aggregates from the canonical CSV; response counts and replacement-register IDs must match exactly.
- Confirm exact questionnaire wording, scale and missing-data rules match across manuscript and DOCX.
- Independent semantic reviewer assesses the exact candidate SHA for requirement fit, usefulness, completeness, claims and negative-neighbor distinction.
- Word-native render and all-page visual inspection are separate from semantic review.
- Candidate remains CANDIDATE until exact-SHA independent semantic PASS and any formal Human acceptance; SAMPLE never converts into REAL by formatting.
