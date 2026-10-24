# 0121 / I19-E09 Unique Blueprint R01

**State:** source-derived candidate blueprint; not official approval.
**Artifact:** 0121《學員滿意度與學習評量報告》.
**Official requirement:** 提出學員滿意度、考試測驗或心得報告（學習技能面）。
**Printed checkbox serial:** UNKNOWN_NOT_ASSERTED (the source page does not print a unique serial).
**Official source:** official_source_0108_r11.pdf, p.8; original PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
**Crosswalk:** I19-E09 -> one deliverable, 0 split extras -> doc_id 0121; source SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`. **Do not conflate doc_id, requirement ID, and printed checkbox serial.**

## 1. Purpose and audience
Produce an evaluator-readable working report that an association training administrator and instructor can use to collect, calculate, interpret and act on learner satisfaction and skill-learning evidence. It must contain a completed, internally consistent SAMPLE/SYNTHETIC worked case if no verifiable REAL records are supplied.

## 2. Genre and boundary
This is an analysis/evaluation report with usable embedded instruments and evidence tables, not a policy essay, empty questionnaire shell, course plan, or training-outcome ledger. Its direct evidence role is the I19-E09 learner-satisfaction / test / reflection evidence. It may cite I19-E08 (0120) and I19-E10 (0122) as different adjacent requirements, but must not copy their cases, claim a shared cohort, or substitute their evidence. Use a clearly separate case ID `SAMPLE-0121-C01`; any real cross-document cohort link requires source evidence and Human-provided truth.

## 3. Required sections
1. One-page use card: purpose, reader, timing, inputs, completed outputs, SAMPLE/REAL state, and hold warning.
2. Official requirement mapping and evidence scope; exact source page and record locator.
3. Evaluation design: training objective/skill construct, learner population, invitation/response flow, inclusion/exclusion, anonymous ID, administration time, and limitations. Any synthetic scheduling details must be marked SAMPLE.
4. Data dictionary with variable, definition, scale, numerator/denominator, missing-value rule, source record and replacement key.
5. Complete satisfaction questionnaire with at least 10 specific items, 1–5 anchors (1=非常不同意/不滿意 through 5=非常同意/滿意), N/A rule, optional comment prompts, and a response/validity check. Include distinct dimensions: relevance, objective clarity, instructor explanation, material usability, practice adequacy, environment, assessment fairness, confidence to apply, overall satisfaction, and improvement priority.
6. Full synthetic response data (row-level, anonymous IDs) and response-flow reconciliation; never present the sample as association performance.
7. Learning assessment: at least five measurable skill tasks or test items aligned to stated constructs, scoring rubric with observable 0/partial/full anchors, total score and explicitly illustrative pass threshold; keep the threshold SAMPLE until an association-approved REAL rule is provided.
8. Complete synthetic paired pre/post or equivalent learning evidence, with item-level data and calculations.
9. Results: valid response rate, per-item mean and positive rate, overall distribution, learning-test pass rate, paired change, and a small subgroup/difference analysis only when sample size permits. Explain denominator and missingness for each metric.
10. Interpretation, limitations and attribution: distinguish satisfaction from learning; do not infer causality or organizational impact from self-report or a small sample.
11. Findings-to-action plan with finding, supporting rows, priority, responsible ROLE (synthetic role label only), target date (SAMPLE), action, follow-up measure, hold/reopen trigger, and closure evidence.
12. SAMPLE/REAL boundary, fact-by-fact replacement register, source index and independent review fields.

## 4. Required tables/figures
- requirement-to-report locator and source provenance table;
- evaluation construct / question / score / decision map;
- full response-flow table (invited, responded, valid, excluded, missing; arithmetic reconciles);
- 10+ question instrument and score anchors;
- complete anonymous response-level satisfaction matrix;
- assessment blueprint with at least five tasks, observable scoring anchors and max points;
- complete item-level pre/post synthetic scores plus totals;
- item summary (n, missing, mean, 4–5 positive numerator, positive rate);
- learning summary and paired-change calculation;
- evidence-strength/limitation table;
- recommendation owner/target/monitor/hold table;
- synthetic fact replacement register.

## 5. Calculations and rules
For each statistic show formula, numbers substituted, rounding, unit and denominator. Suggested formulas: response rate = valid respondents / invited learners; satisfaction positive rate = number of valid 4–5 responses / valid responses for that item; item mean = item-score sum / valid answers; assessment pass rate = learners meeting the illustrative threshold / learners with assessable tests; paired mean change = sum(post-pre for matched IDs) / matched IDs. Never divide by invited count when computing item mean; never count N/A as zero; state missing/excluded handling. A sample must pass recomputation from included CSVs.

## 6. Synthetic dataset design
Use a separate cohort of at least 8 synthetic participants, with a disclosed invitation count and at least one non-response or item missingness to demonstrate denominators; include at least 7 valid questionnaires, all item data, at least 6 paired skill assessments, and 3 short distinct synthetic reflections. Choose values that produce at least one actionable low-scoring item and a non-uniform skill result. Keep every date, identity, role, response, score, threshold, conclusion, action, and target date in the replacement register. Do not reuse 0120's sample case or scores.

## 7. Cross-document boundary
0120/I19-E08 is the separate preliminary training-outcome/evidence compilation; 0122/I19-E10 is the separate post-course follow-up/certification analysis. This report may explain why its learner-level satisfaction and assessment records are relevant, but it must not re-label 0120 results as 0121, make up a shared case_id, or claim 0122 follow-up outcomes. The official 157 checkbox summary line is not the same thing as the 142 deliverable ID.

## 8. REAL evidence prerequisites
Before any REAL label, verify authorized source file, actual course/date, participant/response custody and privacy basis, denominator, scoring policy, instructor/assessment evidence, approval where required, and exact location. No REAL source was provided for this source-prep stage. Leave real fields blank/held; never fabricate participants, attendance, signatures, approval, scores, certificates, actual association decisions or third-party records.

## 9. Replacement, hold and rejection criteria
Every synthetic atomic fact gets a register key and locator. HOLD if official mapping/source page is absent; sample and real records are mixed; denominators do not reconcile; N/A/missing are silently treated as zero; rubric or pass threshold is not approved but described as REAL; response or assessment rows do not reproduce summaries; small-sample subgroup inference is overstated; causal/organizational results are asserted from satisfaction; a neighboring requirement's evidence is substituted; actual participant data is exposed without authority; or form fields are incomplete. Reject if the title-blind test cannot identify a learner-satisfaction/learning-assessment report and its direct I19-E09 purpose.

## 10. Acceptance tests
- Exact mapping I19-E09 -> 0121; serial remains UNKNOWN_NOT_ASSERTED.
- Official wording and page 8 source locator preserved.
- All required sections/tables/items and complete sample data present; no empty-template substitution.
- All displayed arithmetic independently recomputes from included line-item data.
- Satisfaction and learning measures are distinct and interpreted within limitations.
- Every SAMPLE fact has a replacement key; REAL evidence remains visibly unavailable/held.
- Negative-neighbor test separates 0120 and 0122.
- Readable native Word rendering, all pages inspected, no clipped cells or undersized text (body >=10.5pt, table >=9.5pt).
- Independent semantic review is bound to final exact DOCX SHA; builder review is not acceptance.
- Formal association acceptance remains NOT_GRANTED until the actual Human Gate.

## 11. Source freshness note
The crosswalk, 142 seed and `CONTROL/BLUEPRINT_CURRENT.jsonl` are local R01/R03 controls last modified 2026-10-02. Crosswalk mapping agrees with the official page-8 requirement; the 142 seed's authoring fields are blank and the 0121 current-blueprint row is preserved verbatim only as lineage. This R01 Unique Blueprint is a fresh, requirement-specific authoring decomposition, not a copy of historical body text or a claim that the old runtime queue is current. The Wave005 source map has no I19-E09 row.
