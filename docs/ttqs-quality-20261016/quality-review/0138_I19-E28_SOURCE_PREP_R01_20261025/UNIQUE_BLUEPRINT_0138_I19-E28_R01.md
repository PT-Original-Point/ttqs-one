# DOCX 0138 / I19-E28 Unique Blueprint R01

## Identity and source binding
- Project TTQS ONE; DOCX ID 0138; official requirement ID I19-E28; 157-item Blueprint index 152. These identifiers are distinct.
- Exact official wording (printed p.9): **「個人績效提升（薪資提升或獎勵升遷之紀錄）。」**
- Unique Blueprint index 152: **「個人升薪/獎勵/升遷證明：取得同意與原件」**; required elements are a specific source locator, complete example, decision/result, and factual links to other documents.
- Crosswalk title: **學員訓後薪資與獎勵升遷第三方驗證表**. Genre: dedicated evidence record; does not replace third-party originals.
- Source baseline: `339c79e7341e35cc77790374655901a6a292d75c`; current 142-row JSONL Git blob `cab446ede479001334289d18062e6b8bb2340dc3`; official PDF Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`; crosswalk Git blob `1ac4a8419088d947947031b758e29c35a3606514`; 157 spec Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; genre manual Git blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886`.

## Purpose and operational boundary
Record and verify one consented individual's post-training salary increase, reward, or promotion from traceable third-party primary evidence. The form itself is not third-party proof. The fact that a change occurred after training does not establish that training caused it. Never merge cohort analysis, media coverage, employment rates, awards or market effects into this record.

## Workflow, roles and gates
1. **Intake:** authorized case handler confirms the I19-E28 claim type (salary, reward, promotion, unchanged, unknown) and creates a pseudonymous case ID. Do not collect identity-key data in the public index.
2. **Consent:** obtain specific, dated, purpose-limited permission before requesting or processing personal salary/employment records. Record fields, recipients, permitted disclosure, retention and withdrawal path. Missing/withdrawn consent means stop collection and `HOLD_PRIVACY`.
3. **Source capture:** record issuer, source document type, identifier, issue/effective date, exact page/field, acquisition channel/time, file integrity/version/hash, authorized storage locator and access class. Missing source locator/hash remains `UNKNOWN`; never invent one.
4. **Independent source check:** verify the issuer through a contact channel obtained independently or a verifiable official/digital signature source. A document's own contact details alone do not authenticate it. Keep request, response and verification notes as separate records.
5. **Claim comparison:** link each claim to exact source page/field. Salary comparisons require same currency, period, wage components and comparable working time; baseline zero or incomparable units means `N/A` with reason. Rewards require source-supported type/date/value; promotions require source-supported old/new position or grade and effective date.
6. **Decision:** `VERIFIED_PRIMARY` only after authentic source, subject linkage, consent/access, exact fact scope and second-person review all pass. Use `VERIFIED_LIMITED` only for narrowly supported facts. Otherwise `HOLD`/`REJECT`/`SAMPLE_ONLY` with reason and next action.
7. **Privacy and storage:** retain originals and any identity key in approved restricted storage, separate from public working files. Public GitHub may contain only the synthetic example and non-identifying control evidence; no real salary originals or private data.
8. **Second review and closure:** an authorized reviewer checks source, consent, scope, calculations and allowed wording. Record role code, date, exact artifact/version reviewed and correction history. No fabricated signatures or approvals.

## Required data model and forms
- Case fields: pseudonymous case ID; relevant course/cohort ID; completion date and source; baseline and outcome periods; claim type; responsible/reviewer role codes; status.
- Consent record: subject confirmation; purpose; field scope; recipients; expiration/retention; withdrawal; status; controlled locator. Consent is permission, not proof of the claim.
- Third-party source index: issuer; issuer role; document class (payroll statement, HR certificate, formal reward decision, promotion notice); record ID; dates; page/field; acquisition method/date/time; raw-file SHA-256; restricted locator; access category; verifier and verification channel.
- Claim matrix: claim ID/text; claim kind; evidence page/field; exact supported wording; unsupported wording; decision; limitation; follow-up.
- Salary comparison: currency; monthly/annual basis; included/excluded components; work-time/FTE comparability; baseline, follow-up, difference and percent; formula, denominator and rounding; N/A/rejection reason.
- Reward/promotion paths: source-supported award/reward type and effective/decision date, or old/new grade/title and effective date; amount only if documented; exact source locator; verification scope and limitation.
- Exception/change log: missing or withdrawn consent, issuer unreachable, date/value mismatch, altered source, duplicate, incomparable periods, privacy hold; corrective action; responsible role; due date; independent recheck result.
- Official traceability map: I19-E28 source wording → section/table/field → source entry → decision/reviewer locator.
- Synthetic replacement register: every invented ID/date/value/issuer label/source description/result, exact page/table/field, real source required, authorized replacement role, completion status.

## Complete synthetic demonstration
Use one consistent cross-document training case from the 0126/I19-E14 Blueprint only as `SAMPLE / SYNTHETIC ONLY`: `SYN-0126-01`, baseline monthly pay NT$32,000, follow-up NT$33,000, difference +NT$1,000, rate `(33,000-32,000)/32,000 × 100 = 3.1250%` (display `3.13%`). This is a synthetic survey value, not a real learner, employer, payroll record or association result. No source bytes or consent exist; therefore source status is `NOT PROVIDED`, verification is `SAMPLE_ONLY`, and any REAL claim remains `UNKNOWN/HOLD`. Do not create a mock payroll slip, signature, issuer reply, fake hash or fabricated locator. The sample illustrates how a genuine source would be indexed and compared, not a completed verification.

## Required sections and evidence tables
1. 30-second user guide: purpose, reader, timing, outputs and SAMPLE/REAL boundary.
2. Exact official requirement, evidence boundary and title-blind purpose.
3. Roles, eligibility, consent, privacy, restricted storage and stop conditions.
4. Field dictionary: definition, source, entry role, verification, sensitivity, missing-value rule.
5. Third-party source intake form and source locator/index.
6. Claim-to-source matrix for salary, reward and promotion; exact supported wording.
7. Completed synthetic case with explicit no-original/no-consent disclaimer and recalculable salary example.
8. Completeness/consent/source validation checklist, exception and correction trail, HOLD/REJECT path.
9. Unsent/unsigned third-party request-letter draft.
10. Official requirement-to-section/table/field traceability map and negative-neighbor test.
11. SAMPLE-to-REAL replacement register and retention/access-control steps.
12. Blank REAL capture fields with decline, unknown and N/A choices; never prefill real values/signatures.

## Cross-document boundaries
- 0137 / I19-E27 is media reporting; reject media claims as evidence of an individual's salary/reward/promotion.
- 0139 / I19-E29 covers qualification/employment rates; aggregate rates cannot prove an individual's compensation record.
- 0126 / I19-E14 is a cohort salary survey/analysis, not a third-party verification record. A synthetic cross-link is allowed only with the same case ID and exact values; no REAL link is established.
- 0125 / I19-E13 is job application of learned skills, not proof of a salary change.
- Reuse of historical body text is **PROHIBITED**; only current official sources and the current row govern.

## Acceptance and rejection gates
- Hide title/file name: reader still identifies this as a third-party verification record for individual post-training salary/reward/promotion.
- Official text/page and ID mapping are exact; DOCX 0138, I19-E28, and 157 index 152 never substitute for each other.
- Each SAMPLE fact is registered; no fictitious employer original, consent signature, issuer response, association approval or REAL outcome appears.
- Formula, amount, units, denominator and rounding recompute; no unsupported training causation.
- Staff can execute the workflow: roles, inputs, source verification, consent, privacy, decision states, exception handling, reviewer, output and follow-up are concrete.
- At least two nearest neighbors are explicitly rejected using distinct evidence fields.
- Body font >=10.5 pt; tables >=9.5 pt; native Word export and every page visually inspected.
- Independent semantic and technical receipts bind the same final DOCX SHA. Candidate status never implies formal acceptance.