# UNIQUE BLUEPRINT｜DOCX 0124｜I19-E12｜R01

## A. Authority and exact identity
- Project: TTQS_ONE
- Deliverable: DOCX 0124 — 結訓學員雇用與雇主回饋佐證表
- Official requirement: I19-E12, page 8: 「企業主雇用結訓後學員，肯定機構訓練的成效。」
- Source snapshot: PR #92 branch `work/ttqs-one-document-quality-contract-20261016`, HEAD `0e377a92599b16d438c62819e299b6d7579f6490`.
- Unique row authority: remote `BLUEPRINT_CURRENT.jsonl` blob `cab446ede479001334289d18062e6b8bb2340dc3`; local identical Git blob from the verified 142-ID crosswalk source.
- Official PDF SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; exact PDF Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`; page-8 text SHA-256 `c34ead45cad406150de5622e157f44727157776ce5c6abf5343c7db5dca42520`.
- Print checkbox serial: UNKNOWN_NOT_ASSERTED; never infer it from DOCX 0124.

## B. Document-specific purpose and non-substitution
This is an operational evidence record for a particular trained graduate whom an employer hired after course completion, plus the employer's own feedback about the training. It must let an authorized association worker verify the training-to-hire sequence, identify a genuine employer-issued hiring source, capture feedback from an employer owner or authorized respondent, and state what the feedback supports and does not support.

Title-blind identification: after hiding the file name, title, document ID and requirement ID, the job-start-after-completion check, employer source/authority fields, employer feedback questions and two-part evidence decision must still identify this work product.

Negative neighbors:
- 0123 / I19-E11: member business achievement after training. It is not a job-hire/employer-feedback record.
- 0125 / I19-E13: learner uses skills in a job. It is not evidence that an employer hired the graduate or affirmed the institution's training.
- Do not copy either neighbor's case facts, performance data or conclusion.

## C. Required content architecture
1. First-page quick-use card: user, time to use, required outputs, state = SAMPLE/SYNTHETIC example plus reusable form; no REAL evidence supplied.
2. Exact requirement and bounded evidence path.
3. Roles and step sequence: intake → consent/scope → course completion check → claimed hire → employer-source authentication → authorized employer response → cross-check → evidence disposition → controlled filing.
4. Inclusion/exclusion rules and decision matrix. A post-course offer alone is not proof of a hire; self-report alone is a claim, not employer confirmation; a learner skill-use report alone belongs to a different requirement.
5. Field dictionary with definition, source, recorder and validation rule.
6. A usable blank case register and employer questionnaire with response choices, non-response/decline handling, observation period and specific example prompts.
7. A fully completed SAMPLE/SYNTHETIC case with dates, course completion, hire start, issuer/respondent role, source locator marked explicitly simulated, item answers, limitations and decision.
8. A small synthetic cohort reconciliation to demonstrate denominators, coverage and exclusions. Do not call it an employment rate or association performance result.
9. Arithmetic with stated numerator, denominator, unit, period, rounding and N/A treatment. Do not average ordinal questions into a causal effect score.
10. Exceptions, contradictory evidence, correction history and HOLD/reopen criteria.
11. Per-fact synthetic replacement register and real-evidence checklist.
12. Cross-reference, attachment index, version and custody controls; no invented retention period or authority.

## D. Required operational forms and fields
### D1. Case and source register
One row per learner/employer case: synthetic or real case ID; learner code; course ID; course end/completion date and record locator; employer code/name (or controlled protected locator); asserted hire start; source issuer/type/ID/date; employer contact obtained from an independently checked channel where appropriate; verification date/method/operator; employer respondent and authority; consent/use scope; response date; observation period; response status; issue/HOLD reason; evidence locator; reviewer outcome and next action.

### D2. Employer feedback instrument
Use neutral, non-leading questions. Each 1–5 rating must define anchors: 1=not demonstrated/strongly disagree, 2=limited, 3=partly or mixed, 4=mostly/agree, 5=consistently/strongly agree. Provide `NOT OBSERVED`, `NOT APPLICABLE`, `DECLINED`, and `UNKNOWN` as separate states, not as zero. Questions:
- Confirm respondent's employer role/authority and observation period.
- Confirm whether the employer hired the graduate and the verified start date.
- Which course-related skill was relevant to the actual role? Record the task and basis.
- What observable work example supports the answer? Include date/period and a permissible source locator, not a fabricated quotation.
- Rate relevance, observed application, work quality/readiness separately; allow N/A.
- Ask whether the employer considers the training useful for job readiness, with YES / PARTLY / NO / INSUFFICIENT OBSERVATION plus reasons.
- Record other influences (onboarding, supervision, prior experience, tools, team process) and any limits on attributing change.
- Confirm whether the employer permits the response to be retained/used for this evaluation; record scope and source of consent.

### D3. Two-part case decision
`HIRE_VERIFIED` requires a real, lawful source supporting an employer-employee hire after verified course completion; `EMPLOYER_AFFIRMATION_VERIFIED` requires an authorized employer respondent's authentic response, an explicit positive statement tied to training, and a source/permission record. Both must be true to label a REAL case as directly responsive. Otherwise use `HIRE_ONLY`, `FEEDBACK_ONLY`, `HOLD`, `NOT_ELIGIBLE` or `SYNTHETIC_ONLY`. The synthetic worked example may demonstrate a positive path but can never be counted as a REAL result.

## E. Calculations and limits
Use separate descriptive indicators; each denominator is explicit:
- Hire-source verification coverage = verified hire claims ÷ all hire claims submitted for checking. It does not equal an employment rate.
- Employer response rate = complete employer responses ÷ eligible feedback invitations sent. Report counts and non-responses.
- Explicit positive employer affirmation proportion = valid, authorized employer responses meeting the documented positive rule ÷ valid, authorized complete employer responses. State the observation window and exclusions.
- A cohort employment rate is NOT_CALCULATED unless every eligible graduate's employment status is determined with one consistent denominator and observation point. Do not treat missing status as unemployed or silently exclude it.
- Ratings are ordinal item-level observations. Do not average them into an official TTQS score or claim training caused the hire or outcome.
- Synthetic worked values: 3 hire claims, 2 verified records, 2 feedback invitations, 2 complete responses, 1 explicit positive response. Therefore 2/3=66.7% verification coverage among claims; 2/2=100% response among invitations; 1/2=50% explicit-positive proportion among responses. These are synthetic arithmetic examples only, not association results.

## F. SAMPLE/REAL and replacement rules
- Every synthetic code, date, cohort count, hire count, response, rating, example, source locator, decision and percentage must be identified by a unique `SAMPLE-KEY-*` and registered at its document location.
- Sample locator must say `SAMPLE-ONLY—NO REAL FILE`; do not use a plausible actual company name, realistic employer letter number or signature.
- No fabricated employer original, contract, signature, consent, training attendance, employment event, respondent authority or association approval.
- Real evidence fields stay `NOT_PROVIDED` or `UNKNOWN` until an authorized original is examined. Redactions and access controls must preserve a permitted audit path.
- Formal association acceptance remains a separate Human Gate.

## G. Required tables/figures
1. Eligibility and two-part decision table.
2. Field dictionary.
3. Case register / evidence-location form.
4. Employer feedback instrument.
5. Fully completed synthetic case table and evidence inventory.
6. Synthetic cohort arithmetic reconciliation with separate denominators.
7. Exception / correction / HOLD decision table.
8. Synthetic replacement register and real-evidence checklist.
9. Crosswalk and attachment index.

## H. Independent acceptance tests
- Exact official wording is reproduced and identified as page 8; no derived threshold is misrepresented as official.
- Title-blind test identifies employer hiring after course completion and employer training feedback.
- Does not substitute for 0123/I19-E11 business achievement or 0125/I19-E13 skill-use evidence; names concrete differing fields.
- Forms can be used in practice: neutral questions, scale anchors, separate N/A/decline/unknown, authority/consent, date/period, original-source and verification fields, next action and HOLD path.
- At least one complete synthetic case is internally coherent and all facts are in the replacement register; no blank form is offered as the only completed example.
- Hiring occurs after a verified synthetic completion date in the example, but is not represented as real.
- Each calculation recomputes exactly; no cohort employment rate with unknown denominator/status; no misleading Likert average or causal statement.
- Source chain, evidence levels, employer authority, third-party originals, consent, privacy, replacement, custody and correction controls are explicit.
- Body fonts >=10.5pt; table fonts >=9.5pt; Word-rendered PDF pages all visually readable, with no clipping, split rows that break meaning, orphan headings or dense microprint.
- Independent semantic verdict must bind the final exact DOCX SHA. Builder or local technical checks are not independent acceptance. Formal acceptance remains NOT_GRANTED absent human decision.
