# UNIQUE_BLUEPRINT_0110_I18-E19_R01

## A. Identity and source lock

- Project: TTQS ONE
- Deliverable: doc_id=0110
- Official requirement: I18-E19
- Official checkbox serial: UNKNOWN pending an exact source mapping; never substitute doc_id or requirement ID for the serial.
- Canonical crosswalk name: 問卷調查及課後行動計畫評估表等顯示目標客戶及_可直接使用成品
- Human-facing title proposed for the document: **訓練對組織績效改善與提升之學員及目標客戶問卷暨課後行動計畫評估工具**
- Genre: directly usable dual-respondent survey instrument plus post-course action-plan/follow-up form.
- Official text, verbatim: 「問卷調查及課後行動計畫評估表等顯示目標客戶及學員認為訓練對組織績效的改善及提升均有顯著的效果。」
- Official source: labor agency TTQS training-institution evidence table, PDF page 7, indicator 18; PDF bytes SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709; Git blob 9c7621decdad585b743bf2b3d949ee5518b7bee0.
- Crosswalk blob: 1ac4a8419088d947947031b758e29c35a3606514; R07 BLUEPRINT_CURRENT.jsonl blob cab446ede479001334289d18062e6b8bb2340dc3; source commit db0cd977151dd8623ca6055acdc55dd9c852aa08.
- No actual association responses or outcomes are in this source packet. All demonstrated information must remain SAMPLE / SYNTHETIC; REAL status remains UNKNOWN / HOLD.

## B. Exclusive purpose and ownership

This document gives administrators two ready-to-use instruments for capturing (1) learners’ perceived learning transfer and organizational-performance change and (2) target clients’/service partners’ observations, then connects those answers to an action plan and follow-up. It does not assert that training occurred or produced results.

Adjacent-document separation:
- 0109 / I18-E17: social knowledge-platform use frequency; do not copy its platform/account/activity measures or results.
- 0111 / I18-E20: special-performance/social-impact evidence register; do not substitute this survey or claim exceptional impact.
- This document owns survey questions, response coding, action planning and follow-up linkage for I18-E19 only. It may cite an authorized common case source later, but the current synthetic case is independent and must be labelled as such.

Title-blind test: after hiding the title/file name, a reader should still identify (a) separate learner and target-client survey forms, (b) the performance-change questions, and (c) the connected post-course action-plan follow-up record. A generic satisfaction survey fails.

## C. User and use sequence

Primary user: a small-association training administrator; respondents: learners and target clients/service partners who are eligible to observe the relevant work. No employment relationship is assumed.

Workflow:
1. Define the intended organizational outcome and eligible observers before distributing forms.
2. Record baseline source and period; avoid collecting unnecessary identity data.
3. Obtain voluntary consent and explain purpose, access, retention, and withdrawal.
4. Administer the learner form after training; administer the client/partner form only to observers with a defined observation window.
5. Validate completeness, duplicates, eligibility, and N/A reasons.
6. Code answers using stated denominators; keep groups separate.
7. Connect lower-scoring/barrier items to the action plan.
8. At the specified follow-up point, record evidence and decide CONTINUE, REVISE, HOLD, or CLOSE.
9. Report perception, operational measurement and causal confidence separately.

## D. Required document structure and usable artifacts

1. Cover/quick-use panel: purpose, respondent groups, when to use, approximate time, output, SAMPLE/REAL state.
2. Eligibility, consent, privacy and administration instructions; no compulsory personal identifiers.
3. Construct dictionary: learning gained, transfer/application, perceived organizational outcome, evidence source, alternative cause.
4. Learner form: complete questions and response options.
5. Target-client/service-partner form: complete questions and response options.
6. After-course action-plan/follow-up form.
7. Coding dictionary, denominator/missing/N/A/duplicate rules and descriptive calculations.
8. Completed synthetic case and response dataset; include coherent period, cohort, item answers, computed results and limitations.
9. Evidence-quality and decision rules, including rejection/hold triggers.
10. Requirement traceability table: official clause → respondent/form/item → field/source → decision/output.
11. Fact-level synthetic replacement register / companion-register instructions.
12. Real-data substitution checklist and version/retention instructions.

No blank template alone. Every form must include instructions and meaningful choices; the worked example must be complete enough to demonstrate how staff use it.

## E. Instrument design requirements

### E1. Learner questionnaire
Use at least 10 substantive items, grouped and numbered, including:
- learning confidence/ability for the target work before/after training (make the recall method explicit);
- ability to apply each key skill;
- whether and how often the skill was used during a defined period;
- observed change in quality, completeness, time, coverage or coordination;
- the respondent’s basis of knowledge;
- other changes that could explain the result;
- one open-ended barrier and one improvement suggestion.
Scale: 1 非常不同意 / 明顯變差, 2 不同意 / 稍差, 3 普通 / 無明確變化, 4 同意 / 有改善, 5 非常同意 / 明顯改善; 0 未觀察／不適用 is not a score; blank means no answer. Do not combine these states. Provide a separate frequency scale where needed.

### E2. Client/service-partner questionnaire
Use at least 8 substantive items, including:
- whether the respondent directly observed the defined service/work outcome;
- observed quality/completeness/coordination/timeliness change in a named comparison period;
- whether the respondent can identify the particular trained practice;
- evidence basis and observation frequency;
- alternative causes and uncertainty;
- permission to use an anonymized summary;
- open-ended impact and remaining issue.
Do not ask the client to assess internal learning or training attendance. Use the same 1–5 anchors for comparative items plus 0 未觀察／不適用.

### E3. Action plan and follow-up record
Fields must include: case/form ID; outcome and scope; baseline definition/source/period; target and due date; action steps; role code (not a fictional name); measure and formula; evidence location; privacy/consent state; expected application; follow-up date; actual answer/source; barrier; disposition; reviewer role/date; correction/audit trail. Include a fully completed synthetic example and show an HOLD path when evidence is absent.

## F. Synthetic demonstration, calculations and interpretation

Use only the fictional SYN-0110-CASE-01, separated from any real association claim. Demonstrate respondent groups separately: 8 synthetic learner codes L01–L08 and 6 synthetic client/partner codes C01–C06. If using dates, prefix them as synthetic.

Minimum calculations:
- return rate = eligible valid responses / invitations actually sent;
- valid-item denominator = count of answers 1–5; exclude 0, blank, invalid and duplicate answers and report each exclusion;
- favorable proportion = number of answers 4–5 / valid-item denominator; show numerator, denominator, arithmetic and percentage;
- mean = sum of valid 1–5 scores / valid-item denominator, only if the scale is suitable and distribution/denominator are shown;
- operational completeness = complete records / records sampled; percentage-point change = post percentage − baseline percentage.
Keep learner and client outcomes separate. Do not calculate a pooled impact score that masks differing populations. Do not claim inferential/statistical significance from the sample. A before/after difference is descriptive only and is not causal attribution.

## G. Interpretation and rejection/hold criteria

Use explicit state labels:
- SAMPLE_ONLY: all answers/data invented for training the administrator.
- PERCEPTION_ONLY: real, eligible respondent answers exist, but no independent operational corroboration.
- CORROBORATED_DESCRIPTIVE: real answer sets and comparable operational records are independently traceable; this still does not prove causality.
- INCONCLUSIVE / HOLD: insufficient respondents, missing denominator, no observation window, group contradiction, unverified source, privacy/consent failure, or unexplained data inconsistency.
- REAL: may only be assigned after lawful original records and authorized reviewer verify actual source and handling. This instrument itself never grants REAL status.

The document must not convert the official word 「顯著」 into a statistical-significance claim. Statistical inference requires a suitable sampling and analysis plan and evidence; it is outside this questionnaire’s sample demonstration.

At minimum reject/hold when:
- respondent is ineligible or did not observe the outcome but provides a guessed score;
- baseline/post periods or definitions differ;
- missing/invalid/N/A values are silently counted as positive or negative;
- denominator is absent or does not reconcile;
- only learner opinion is presented as target-client evidence;
- target-client perception is presented as a measured operational outcome;
- a performance change is attributed solely to training without considering alternatives;
- consent/access/retention requirements are not met;
- synthetic case facts are represented as actual association activity.

## H. Cross-document facts and no-fabrication controls

The packet states only the official example, mapping and evidence gap. It does not assert actual training, survey, respondents, customers, service outcomes, approval or performance at 原始點協會. No signatures, names, employer data or third-party originals. Any future sharing of an actual client's response requires authorization and minimized, anonymized data.

The sample case is independent from 0109 and 0111; do not reuse their fictional dates, metrics, actors, case IDs or narrative. Any future common real course evidence must be cited to the verified source; do not duplicate it as a second source of truth.

## I. Required machine-readable checks before Word build

- Exact binding: doc_id=0110, requirement_id=I18-E19, exact quoted requirement, official source page 7.
- Questionnaire contains separately labelled learner and client/partner forms, unique item IDs, complete answer options and the non-score 0 code.
- Action plan includes baseline, target, method, owner-role, deadline, evidence, follow-up and disposition.
- Synthetic case has explicit labels and no real-person names.
- All shown arithmetic can be independently recomputed; denominators and exclusions reconcile.
- All synthetic values/records can be enumerated into a replacement register.
- No statement of actual association result, approval, official score or statistical significance.
- DOCX body excludes engineering paths, commits, hashes, PIDs and review control metadata.
- Builder output remains candidate until independent exact-SHA semantic review and page-level Word visual QA complete.