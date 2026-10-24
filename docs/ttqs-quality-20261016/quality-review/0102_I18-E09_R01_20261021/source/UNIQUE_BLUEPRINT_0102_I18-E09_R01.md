# UNIQUE BLUEPRINT 0102 I18-E09 R01

## Identity

- `project_id`: TTQS_ONE
- `doc_id`: 0102
- `official_requirement_id`: I18-E09
- `indicator`: I18 / 指標 18「訓練系統的一般性功能—目標客戶及學員的評價」
- `project_157_index`: 110 in current `03_157_CHECKBOX_BLUEPRINTS.md`
- `printed_official_checkbox_serial`: UNKNOWN (the source page displays a checkbox, not a printed sequence number)
- `requirement_text`: 指導學員參加技能競賽獲獎。
- `genre`: third-party evidence acquisition, provenance/authenticity verification, training-linkage assessment, and case register; not a fabricated award certificate or a generic success story.
- `reader`: small training-association administrative/volunteer staff and a reviewer checking the evidence.
- `candidate_title`: 技能競賽獲獎證據取得與查核工作紀錄
- `status`: candidate/SAMPLE-SYNTHETIC; no REAL result evidenced.

## Why this file exists

Give an authorized staff member a repeatable, low-overhead way to receive a learner's award claim, obtain and authenticate a real third-party record, connect the result to a specific training activity without overstating causation, protect personal information, decide whether the item is admissible, and locate the source later. A blank checklist alone is insufficient; include a completed synthetic case showing the hold path.

## Source facts and qualification

- Official evidence table PDF p.7, SHA `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`: award coaching is one example in the indicator-18 4-point evidence list.
- Official assessment form PDF p.4, SHA `9d253829410a505c77d8a59fa0203b4c052aa223e2c98d1d509c7c1a57083684`: the 2-point standard concerns target customer/learner belief that training achieved ability improvement. Do not equate a competition award alone with this judgment or with a guaranteed score.
- Project blueprint row 110, I18-L2; local R04 crosswalk maps `I18-E09` and doc 0102, while formal printed sequence remains unknown.
- Real award originals, event results and participant records are not supplied. The sample case is synthetic and must stay explicitly separated from real evidence.

## Negative neighbors

- I18-E08 / project index 109 / docs 0100 and 0101 concern pre/post self-rating and radar analysis. Do not copy their survey/report genre or their case data. Link only when an actual shared case ID and evidence supports it; no shared real case is currently established.
- I18-L2 index 111 concerns a thank-you letter and real-source acquisition. This file must focus on competition award records, not generate a thank-you letter.
- I18-L2 index 112 concerns certificate acquisition rate and denominators. Do not claim an award count or pass rate as a credential-acquisition rate.
- I18-L4 index 122 concerns continued exam coaching and learner return rate. An archived artifact using the prefix 0102 for that different requirement is a known numeric-ID collision and is not source material.

## Document-specific outline

1. Cover and one-minute use guide: exact purpose, official mapping, who should use it, where a user finds the request form, verification form and decision register; prominent `SAMPLE / SYNTHETIC` warning.
2. Evidence boundary: what the award record can support, what it cannot prove, difference between self-report, organizer-issued source, checked original, training linkage and formal scoring.
3. Small-team roles and handoff: requester/records custodian, independent callback verifier where feasible, approver only if real delegation is confirmed; otherwise `authorization status UNKNOWN` and hold external disclosure.
4. End-to-end flow with decision branches: claim received → consent/privacy check → request minimum source → receive original or official public result → authenticity check → verify awardee/competition/date/result → link training objectives → decision → controlled filing / hold / reject → annual review. Include timeout/no-response and suspicious-source branches.
5. Form A, case intake: unique case ID, pseudonymous learner ref, course ID/date and source, competition title/date/organizer, exact claimed result, claim origin, consent scope/date, evidence requested, due date, current evidence state.
6. Form B, participant source request: complete ready-to-send draft with purpose, accepted documents/official links, permitted redaction, deadline, response channel, consent choice, no penalty/no-guarantee language. Clearly marked unissued SAMPLE template.
7. Form C, organizer verification request/script: ready-to-send text and call checklist using independently obtained official contact information; ask only to confirm competition identity, published result, category, date and listed awardee reference; record channel, date/time, handler, reply/source locator. Mark all drafts as not sent.
8. Form D, source authenticity checklist: official domain/document provenance, issuer identity, publication date, event/date/category consistency, name/alias match held privately, original-file integrity/hash, external confirmation, tamper/duplicate check, privacy/consent, evidence locator. Status options: NOT_RECEIVED, RECEIVED_UNVERIFIED, VERIFIED_REAL, HOLD, REJECTED; no PASS without every required predicate.
9. Form E, training-linkage matrix: actual course learning objective → taught skill → practice/assessment record → competition skill/result → temporal sequence → alternative explanations → corroboration → bounded inference. Explicitly separate association, temporal order and causation.
10. Form F, case decision sheet: eligible source? authentic? correct person? award? linked training? consent/authority? disposition and reason; evidence used, missing item, owner role, due date, reviewer and next action. Sample approval language must be `示範判定`; no real approval.
11. Worked synthetic case: two synthetic claims, both without a received/authenticated third-party original; one can be requested but remains pending; the other lacks consent or sufficient identity match and is held. Show completed forms and an explicit zero verified-award result for the sample dataset only.
12. Computation and interpretation: `verified award cases = count(unique case_id with official source checked AND award confirmed AND identity match AND training link documented AND disclosure authority)`; sample count 0. Optional internal process KPI `evidence closure rate = verified cases / claims due for review` with sample numerator 0 and denominator 2 = 0%. State this is a synthetic workflow example, not association performance or TTQS scoring.
13. Case register and evidence/replacement register: one row per claim; sample CSV-like table with source status, verification, training link, privacy authority, decision, locator, synthetic fact IDs, real source required, owner role, deadline and state.
14. Filing, access and retention: keep identity key and source original in an authorized restricted location; public review package receives pseudonym and redacted summary only; access log, version, backup, retention trigger, safe deletion and breach response. Exact retention period is `to be set from current law/consent/association policy`; do not invent a period.
15. Exception and rejection rules; quick-use checklist and version/change record.

## Required tables and usable content

- Case intake table with fillable fields, allowed values and worked sample row.
- Evidence authenticity matrix with at least 8 checks and disposition for pass/fail/unknown.
- Training-linkage matrix with skill, course objective, evidence source and inference limit.
- Decision table mapping missing original, failed issuer confirmation, identity mismatch, no award, duplicate, no consent, missing training link, and confirmed authentic record to HOLD/REJECT/eligible-for-human-review.
- Replacement register with one fact per row, `fact_id`, `case_id`, `doc_id`, location, synthetic value, replacement source required, responsible role, state.
- Two fully populated sample case records; neither may assert an authentic award.
- Request text to the learner and organizer, marked `SAMPLE TEMPLATE - NOT SENT`.

## Sample case fixed boundary and arithmetic

Use `case_id=SYN-0102-CASE-01` and `SYN-0102-CASE-02`. All names/events/claims/dates are invented for workflow demonstration. For both cases, no third-party original has been received, independently checked, or approved for disclosure. Hence `verified_award_count=0`; with two synthetic claims due for review, `closure_rate=0/2=0%`. The calculation only demonstrates a control metric. It is not a real association outcome, award result, or TTQS score. Do not manufacture an award certificate, winner list, organizer reply, signature or real institution name.

## Required rejection / hold conditions

HOLD if source is not received; issuer/channel cannot be independently checked; consent/authority is incomplete; identity or event details conflict; training-to-competition relationship lacks traceable support; third-party reply is pending; original integrity unknown; publication scope not authorized. REJECT the evidence item only when reliable checks show it is false, unrelated, duplicate or not an award; retain reason and reviewer. Never convert a missing source into a zero award result for the association.

## Document acceptance criteria

- Reader can operate the end-to-end workflow without further model interpretation.
- Distinct genre is unmistakable when title is hidden: evidence acquisition + authenticity + training linkage.
- Templates, completed synthetic examples, decision thresholds, formulas and exceptions are all usable.
- 2-point vs 4-point source context is accurately qualified.
- No real association event, winner, certificate, authorization, signature or approval is fabricated.
- No reuse of historical 0102 body or unrelated 0102_122 file.
- Real evidence remains UNKNOWN until a protected authorized source is supplied; formal acceptance remains NOT_GRANTED.