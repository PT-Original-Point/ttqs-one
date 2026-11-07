# UNIQUE BLUEPRINT｜0130｜I19-E19｜R01

## 1. 身分與來源鎖定

- `project_id`: TTQS_ONE
- `doc_id`: 0130
- `internal_requirement_id`: I19-E19（internal 142 sequence crosswalk only）
- `project_157_index`: 143，I19-L3，official evidence table p.8
- `printed_official_checkbox_serial`: UNKNOWN; the cited official source shows the checkbox and item wording but no verified printed sequence number. Never call index 143 the printed serial.
- Official item: 「學員訓後創業案例。」
- Unique genre: third-party post-training entrepreneurship case intake, source-provenance verification, training linkage, decision and follow-up record. Not a testimonial, success story, award document, or fabricated business registration.
- Intended reader: small training-association administrative/volunteer staff and an evaluator checking whether a claimed learner entrepreneurship case is authentic, post-training, and traceable.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; p.8.
- Current 157 Blueprint SHA-256: `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216`; internal crosswalk excerpt SHA-256: `556cbc29defe5ac32d2d3f285430c2f43edf4fe19ca1a49a16cea62d0c28a009`.
- Source contract blobs: 01 `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`; 02 `4ff863d9f534b6359fc1c7c1685bd8cce02da886`; 03 `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`.

## 2. Core acceptance purpose

The document must let staff receive a claimed post-training entrepreneurship case, preserve provenance, verify a real third-party source with permission, establish timing and training linkage, decide whether the evidence is sufficient, and record a follow-up or HOLD without overstating causality or association performance. The document itself is a SAMPLE/CANDIDATE tool until genuine authorized evidence is supplied; no sample case can be counted as real TTQS performance.

## 3. Required document body

1. Reader-facing cover/quick guide: exact doc/requirement/index mapping, explicit CANDIDATE and SAMPLE/SYNTHETIC banner, one-paragraph scope, how to use, what the form does not prove.
2. Definitions and decision states: `VERIFIED_FOR_REVIEW`, `HOLD_MISSING_SOURCE`, `HOLD_CONSENT`, `HOLD_LINKAGE`, `NOT_VERIFIED`, `EXCLUDED_DUPLICATE`, and `REAL_SOURCE_PENDING`. Explain the evidence threshold for each and who may change a state.
3. Intake and privacy/authorization form: case ID; masked participant reference; cohort/course; completion date; reported venture name/type and start date; source contact role; consent scope/date/expiry; minimum necessary information; storage/access/deletion fields. Never put government ID, bank/tax credentials or private raw copies in a public package.
4. Training-linkage and chronology table: enrollment/completion source; training end date; claimed launch date; first evidence date; verification date; discrepancy days; relevance of course skills; distinguish participant report from source-confirmed facts; no causal inference solely from timing.
5. Third-party source register: evidence ID, claim tested, issuer/independent source, original-vs-copy, issue/effective date, acquisition channel/URL or retrieval locator, consent/authority, validation action, reviewer/date, redaction, SHA-256 (only for actual authorized source), result, limitation. A screenshot without issuer/date/location is not authentic proof by itself.
6. Claim-to-evidence matrix: claim, required independent corroboration, source ID, exact locator, authenticity checks, training linkage, status, limitation, next action and due date.
7. Complete usable synthetic worked case `SYN-ENT-01`: fictional participant/cohort/course and dates; sample-only self-report and clearly synthetic mock evidence descriptions; step-by-step checks; a filled chronology and evidence matrix; explicit missing authentic third-party source and consent; outcome `HOLD_*`, not verified; no invented actual organization, registry number, signature, interview or real association decision.
8. Decision and review sheet: threshold checklist for identity linkage, post-training chronology, authentic independent source, source validity, consent/privacy, evidence-to-claim match, duplicate check, limitations, reviewer/second-check role, outcome and reason. Any unresolved critical check forces HOLD/NOT_VERIFIED.
9. Follow-up and disposition: owner role, next action, due date, permitted contact script, reminder log, source received/not received, close/reopen criteria, retention and secure deletion. A sample follow-up is labeled synthetic.
10. Summary table: cases received, cases verified, on hold, excluded; denominator rule and reporting window. For SAMPLE data, explicitly label all figures synthetic and prohibit using them as actual institutional rates.
11. Replacement and real-source checklist: every fictional field with its real source required, acceptable custodian, minimum disclosure and verification; list third-party originals that remain unavailable.
12. Negative-neighbor boundary: not 0129 financial performance, not 0131 certificate/employment, and not index 111 thank-you-letter evidence acquisition.

## 4. Minimum sample facts and calculations

Use one wholly synthetic case, `SYN-ENT-01`, and no real personal or organization identifiers. Sample chronology: course completion 2025-05-30; learner-reported venture start 2025-10-01; intake 2025-10-08; intended source verification 2025-10-10. The dates are illustrative only. In the worked exercise, staff can inspect a synthetic-only mock reference and the tool must visibly stop because there is no authentic third-party registry/operation source and no real consent. Decision: `HOLD_MISSING_SOURCE + HOLD_CONSENT`; verified count = 0 of 1 SAMPLE case; the 0/1 calculation is an exercise-only count, not an association rate. Report no verified real case and no performance claim.

## 5. HOLD / reject rules

- No independent source, no original or authorized verification route, source cannot be authenticated, no consent or disclosure authority, or inability to link the case to the training cohort: HOLD; do not count as verified.
- Registration date before training completion: reject as post-training case unless an independently sourced material post-training start event is evidenced; never silently change dates.
- Name/entity mismatch, conflicting dates, duplicate case, expired/inaccessible source, undated screenshot, altered copy, or source that only proves intent rather than actual operation: HOLD or EXCLUDE with a precise reason and route to appeal/reopen.
- Participant self-report alone is not a third-party source. Training completion alone does not prove entrepreneurship. A registration alone does not prove active operation, income, success, or that training caused the outcome.
- Any fabricated third-party artifact, signature, interview, official confirmation or association approval is a hard fail.

## 6. Data integrity and cross-document facts

All Sample facts must use one stable `case_id` and a replacement-register row. Dates must satisfy course completion ≤ claimed post-training start ≤ intake ≤ planned verification, unless the sample explicitly documents a discrepancy and HOLD. The worked-case status, summary counts, timeline, source matrix and conclusion must agree. The sample case cannot be linked to 0129's financial sample or 0131's employment/certificate sample absent a new source-backed shared fact; no such real link is established.

## 7. Visual and semantic acceptance

Body font ≥10.5 pt, table font ≥9.5 pt. Tables must fit and remain readable with repeated header rows as needed. The document must be a functioning case record when title/cover are hidden. Independent exact-SHA semantic review must test every required component, source/Blueprint mapping, negative neighbors, SAMPLE/REAL separation, date and count consistency, evidence threshold and HOLD behavior. Word open/render and actual visual review are separate checks. Candidate never equals REAL or formal acceptance.