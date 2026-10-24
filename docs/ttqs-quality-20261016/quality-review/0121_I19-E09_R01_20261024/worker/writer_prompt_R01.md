# TTQS ONE 0121 / I19-E09 — bounded text-only writer task

WORK_ID=TTQS_ONE_0121_I19-E09_WRITER_R01
DOC_ID=0121
REQUIREMENT_ID=I19-E09
TASK=WRITE_COMPLETE_EVALUATOR_READY_SYNTHETIC_MANUSCRIPT
REQUESTED_MODEL=gemini-3.8-flash-high

Produce the complete body manuscript for the exact document in the included current Source Packet and Unique Blueprint. This is a single bounded writing task. Return the complete Markdown manuscript only; do not return a plan or commentary. The response must be substantive enough to assemble into an approximately 10–14 page landscape Word report.

HARD ROUTING AND SAFETY
- Text only. Use only the requested gemini-3.8-flash-high model. Do not switch, fallback, invoke tools, browse, use Computer Use, access files, or claim a different actual model. If unable, return an explicit error.
- Do not create or imply any REAL association course, participant, survey, assessment, attendance, approval, result, signature, certificate, or third-party evidence. All worked case facts must be labeled SAMPLE/SYNTHETIC and assigned replacement-register keys.
- Use a clearly hypothetical volunteer-association training case, not a claim about actual 原始點協會 activity. Use participant IDs only, not names. Do not make clinical or medical claims.
- Correctly map `doc_id=0121` to `requirement_id=I19-E09`. Printed checkbox serial remains UNKNOWN_NOT_ASSERTED. Do not confuse these identifiers.
- Keep 0120/I19-E08 and 0122/I19-E10 distinct. Do not reuse 0120 sample values, course, cohort, scores, conclusions, or case ID. Do not imply a shared cohort or cross-document linkage.

REQUIRED OUTPUT CONTENT
- Follow every section, form, calculation, table, boundary and acceptance requirement in the Unique Blueprint. Include actual filled synthetic examples, not empty templates or future tense.
- Use 10 invited sample participants P01–P10; 9 return a satisfaction form, 8 complete at least 8/10 items and are included in overall composite, one partial form has 6/10 and is excluded from composite but its answered items may count in item-level summaries, and one invitee does not respond. Make all response counts reconcile.
- Provide the full 10-item instrument with precise wording, 1–5 anchors and N/A rule; full row-level responses for the 8 complete sample forms plus the partial form; and item-level n, missing, mean, 4–5 positive numerator and positive rate. Never count missing/N/A as zero.
- Provide 5 measurable skill tasks with observable 0/10/20 anchors and 100-point total; state the pass threshold as an illustrative SAMPLE rule pending association approval. Provide post-test results for 8 participant IDs, paired pre/post item scores for at least 6 IDs, and calculate post pass rate, paired n, means and mean change from the rows.
- Include at least 3 distinct synthetic reflection excerpts, explain satisfaction vs demonstrated learning, discuss response/missingness and small-sample limits, and do not infer causality or organizational impact.
- Include a decision/action table with supporting row keys, priority, synthetic role, SAMPLE target date, measure, hold/reopen trigger and closure evidence. Keep all future actions visibly SAMPLE/planned, not completed REAL actions.
- Include a fact-level replacement register keyed to every sample participant/response/score/test/reflection/date/threshold/action and an exact real replacement source needed.
- Output one complete human-readable report; no unsupported association facts, fake names, signatures or approvals. Ensure all displayed sums/means/rates can be recomputed from the included tables.

CURRENT SOURCE PACKET
# 0121 / I19-E09 Source Packet R01

## Mapping and authority
- Project: TTQS_ONE; doc_id `0121`; requirement_id `I19-E09`; title `學員滿意度與學習評量報告`.
- Current PR #92 branch source read: `90a5152fe65abecb62088e1d49df5a3e8b866889` (`work/ttqs-one-document-quality-contract-20261016`).
- Exact current requirement wording in the official source: `提出學員滿意度、考試測驗或心得報告（學習技能面）。`
- Official source: `WORK/QUALITY_REBUILD_20261016/official_source_0108_r11.pdf`, p.8, PDF SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; page image SHA-256 `907176e44c4ccb42d86c84566baf9f1b3b6494e6c67d5a8e899decaebb065f9a`; extracted text SHA-256 `c34ead45cad406150de5622e157f44727157776ce5c6abf5343c7db5dca42520`. The printed page shows the relevant checkbox but does not print an individual serial; record `UNKNOWN_NOT_ASSERTED`.
- 129-to-142 crosswalk row: one deliverable, zero split extras, `I19-E09 -> 0121`; crosswalk SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`. The 142 seed confirms the title but has blank document-specific design fields; seed SHA-256 `280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0`.
- The preserved `BLUEPRINT_CURRENT.jsonl` 0121 row SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; exact source row SHA-256 `ca96f525ed9d36688efaeb3ce653e860f254fb94f035e0fb7fb46520ee00b14e`; local mtime `2026-10-02T14:23:06`. It is lineage only. The source requirement map SHA-256 `405b987797d1558ecac182cea8e1adfbd1aead7754c880db32db43c235d5024e` contains no I19-E09 row, so it is not used to invent a different requirement.

## Current human-policy source identities
The R11 prompt target and current branch policies are recorded below by GitHub path, Git blob OID and SHA-256. These identify the current input revision without reloading unchanged long prose:
- `AGENTS.md` blob `2e8d4eddd68c650f38db8cb48d421b838e693ecb` SHA-256 `60f945a5c863ce654f3229ea999745bc06f34e4ef6d0c9120890a6553b0a6008` (10975 bytes).
- `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md` blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` SHA-256 `07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8` (13960 bytes).
- `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md` blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886` SHA-256 `7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa` (16215 bytes).
- `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md` blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` SHA-256 `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216` (36868 bytes).
- `docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md` blob `65e7fd5a406877e875174402a0d3ddc68b6111a1` SHA-256 `830eea1fec05298a02b4ed76af1a7227b7139dd98f93511109cbf7660188350b` (11922 bytes).
- `docs/ttqs-quality-20261016/05_HOURLY_NATIVE_WAKE_RESUME.md` blob `dbdb2e567e8e5c2b7eb0632f060a45a7ae371a49` SHA-256 `4c003c1727dba665cd8f2b7128c18219fa40d8fe453f5b1b3377153589b744bb` (27171 bytes).
- `docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` blob `b566c5c71d1a88e012eca2eeac90c8a3e4ecc06c` SHA-256 `effda772f2e7e1ce2d4f8c3730c4cfdb811a132f84739664ab5aab5bbd0dc863` (68264 bytes).

## Scope and next stage
No 0121 current R01 work directory or live writer was present when this packet was created; historical 0121 DOCX files are not reused as body templates. The exact requirement and crosswalk agree, and a current requirement-specific Blueprint has now been prepared. Derived next legal stage: a bounded text-only writer task for 0121 using this packet and the Unique Blueprint; complete synthetic case only, no real association-performance claims. Writer output must be recovered from its original stdout/artifact, reviewed against this source before DOCX assembly, then carried to native Word and exact-SHA independent QA.

## Adjacent requirements (non-substitution)
- 0120 / I19-E08: separate preliminary training-outcome evidence/assessment form. Do not copy its synthetic case or scores.
- 0122 / I19-E10: separate post-course follow-up/certification analysis. Do not assert its follow-up or certification results here.

## Real-evidence boundary
No authorized real participant survey, test, reflection, approval or performance record was supplied for this packet. The future document must visibly label every worked example `SAMPLE/SYNTHETIC`, retain blank/held REAL fields, and itemize replacement keys. Never fabricate signatures, attendance, results, certificates, approvals or third-party records.


CURRENT DOCUMENT-SPECIFIC UNIQUE BLUEPRINT
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

