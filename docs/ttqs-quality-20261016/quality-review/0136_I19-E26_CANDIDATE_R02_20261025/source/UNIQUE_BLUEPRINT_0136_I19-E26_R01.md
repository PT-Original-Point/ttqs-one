# UNIQUE BLUEPRINT — DOCX 0136 / I19-E26 / R01

## Source-derived identity

| Field | Verified value |
|---|---|
| Project | TTQS_ONE |
| Document ID | 0136 |
| 142 crosswalk requirement | I19-E26 |
| Official deliverable title | 公益活動、獎項與學校合作原件驗證登錄表 |
| Document genre | Original-evidence verification register / operational evidence log |
| Official evidence-table source | Current official PDF, printed pages 8–9 |
| Project 157 content index | 150 — 公益/表揚/產學/研發社會影響：原件與來源 |
| Official printed checkbox serial | UNKNOWN |
| Current source commit | 03d73cb900e28d7cd8ea02ec0c43c4564b521e33 |

Do not conflate the document ID, internal requirement ID, project 157 index, or printed checkbox serial.

## Purpose and evidence role

Provide one controlled register for an association administrator to receive, preserve, verify, classify, retrieve, and review evidence offered for the official indicator-19 reference example concerning social-benefit participation, public/private awards, and school-linked industry-academia or R&D social impact. The register records claims and source verification; it is not a third-party original, award certificate, activity record, approval, or proof of an actual social result.

The register must be useful when there are zero verified REAL entries. It must show the missing-source path and a fully populated synthetic walkthrough while preventing that walkthrough from counting as association performance.

## Scope and negative neighbors

- In scope: source provenance, authenticity and relevance checks, participation/contribution, separate outcome support, confidentiality/access, status, reviewer trace, follow-up, and retrieval.
- Out of scope: market/customer value analysis (DOCX 0135 / I19-E25); positive media coverage as the primary evidence item (DOCX 0137 / I19-E27); training-class/person-time totals (DOCX 0133 / I19-E22); member/dues ledgers (DOCX 0134 / I19-E23).
- A media clipping may be a locator or corroborating source but does not become the underlying award, participation, partnership, or R&D original.
- Do not self-assign an official TTQS rating or claim that all three evidence categories are present.

## Required user-facing sections

1. Quick use and scope: intake owner, when to create a row, review before filing, status key, and the rule that a logged claim is not verified evidence.
2. Official-source mapping: exact p8–9 wording, source location, document/requirement/index identities, printed checkbox serial UNKNOWN, and no self-scoring.
3. Intake and preservation SOP: immutable record ID, received date/custodian, read-only original preservation, SHA-256, format/version/page locator, restricted source storage, sanitized public metadata, and chain-of-custody log.
4. Three verification paths: separate steps and acceptable sources for (a) social-benefit activity, (b) awards, and (c) school/industry-academia/R&D social impact. Each separates proof of event/award/project, association role, and claimed outcome.
5. Operational register: complete field definitions and instructions, not just an empty form.
6. Decision/exception rules: VERIFIED_PRIMARY / VERIFIED_SECONDARY / PENDING_SOURCE / HOLD_PRIVACY / REJECTED / SAMPLE_ONLY; decision authority, evidence sufficiency, escalation, correction, and non-counting rules.
7. Worked examples: one completed SAMPLE/SYNTHETIC row per category. Each says no actual original is attached, no real association activity/award/partnership is asserted, and the row is not countable evidence.
8. Cross-evidence/non-duplication control: common event/project key, avoid double counting, and keep media, customer value, participation, and outcome claims in their proper document lanes.
9. Privacy/access/retention/disclosure: minimum personal data, consent/legal basis, role access, redaction, retention and review date, public/private split, incident response.
10. Decision summary and improvement follow-up: unresolved-source queue, owner/target date, retrieval test, recurring defects, next review; no invented association decision or performance conclusion.
11. SAMPLE-to-REAL replacement register: one row per synthetic fact/field/role/date/issuer/outcome/status/source locator and exact real source required.
12. Version, verification, and handoff: reviewer/date/source revision, unresolved issues, and stop/go checklist.

## Required record fields

Each row must include:

- Immutable record_id; evidence class; shared event_project_key; DOCX 0136; I19-E26; project index 150; printed checkbox serial UNKNOWN.
- Neutral claim; issuer/organizer/school category; association role or NOT ESTABLISHED; event/project/award date/period; source-record date; custodian.
- Original evidence type; authority; source title; restricted original locator; safe public locator if any; page/section/item locator; format/version; exact-original SHA-256; capture date; custody transfers.
- Verification method/source endpoint; date and verifier role; result/checkpoint; party identity; actual participation/recipient/contribution; separate social outcome and denominator if numeric.
- Relevance rationale; evidence status; primary/secondary class; limitations; duplicate group; consent/legal basis; data class/access group; retention review date.
- Decision, reason, reviewer role/date, correction note, owner/due date, safe retrieval instruction.

Use NOT_APPLICABLE only with a reason and UNKNOWN when unknown. Blank must not imply verified.

## Category-specific verification

### A. Social-benefit activity
Verify organizer and event directly; separately verify the association's participation (organizer acknowledgement, source-backed attendance/role record, or controlled log corroborated by organizer). Record actual contribution. Beneficiary count, donations, hours, reach, and impact each require their own source, unit, period, and denominator. A registration form, photo, or publicity post alone is insufficient for delivery/outcome.

### B. Award or recognition
Verify issuing body, exact award/title/category/date, recipient identity, criteria/period, and public award registry or issuer confirmation. Nomination, application, participation certificate, self-written summary, or unverified image is not proof of receiving an award. Protect personal data and obtain lawful disclosure consent.

### C. School partnership, industry-academia, or R&D social impact
Verify the school/unit and project using an agreement/project record; identify actual association contribution and deliverable; verify acceptance/public output with the school or authorized first-party source; then separately substantiate social impact. An MOU or meeting proves neither completion nor outcome. R&D claims identify the output, use/context, and source of social benefit; do not imply commercialization/community effect without evidence.

## Status and hard decision rules

- VERIFIED_PRIMARY: lawful original/first-party digital source obtained, exact bytes hashed, authority and party/role verified, relevance recorded, privacy cleared.
- VERIFIED_SECONDARY: authentic attributable public/third-party source supports only the limited recorded claim; original not held, limitation visible, never described as original-verified.
- PENDING_SOURCE: source absent or issuer/participant/outcome not checked; claim not countable.
- HOLD_PRIVACY: consent, legal basis, redaction, access, or publication unresolved; do not publish or count.
- REJECTED: fabricated, unverifiable after bounded checks, unrelated, contradictory, altered without provenance, duplicate-counted, or fails to prove role/outcome; preserve audit note without exposing source.
- SAMPLE_ONLY: demonstration data; never eligible for association performance or score.
- Never infer numeric impact or causation from attendance, partnership title, award, or media alone. Do not self-score TTQS.

## Required tables and working controls

- T1 Evidence register: full fields, one row per discrete claim/source.
- T2 Original inventory and custody: hash, bytes, format/version, page, receipt/transfer, storage tier, access, disclosure.
- T3 Verification checklist: authority, integrity, party identity, role, outcome, relevance, privacy, duplicate check, reviewer decision.
- T4 Hold/reject/correction log: record, failed check, action, owner, due date, recheck.
- T5 Claim-to-source matrix: public claim to exact original/page or official URL/hash/status/allowed wording.
- T6 Synthetic replacement register: each synthetic fact and exact real source required, with locator.
- No fabricated certificates, letters, MOU, school acceptance, attendance logs, award registries, signatures, real names, beneficiary counts, or association decisions.

## Acceptance criteria

1. Exact official p8–9 wording is present and described as a reference example, not association result.
2. Header/crosswalk bind DOCX 0136 ↔ I19-E26; index 150 is separate; printed serial remains UNKNOWN.
3. Usable operationally with zero REAL sources.
4. Three separate verification workflows distinguish source authenticity, association role, and outcome.
5. Required fields, statuses, decision thresholds, rejection/HOLD, privacy and custody controls are usable.
6. Three complete SAMPLE/SYNTHETIC examples are unmistakably non-real and have no counterfeit originals; every synthetic assertion is registered.
7. Neighbors 0135/0137 cannot be mistaken for this requirement.
8. Numbers/claims attributable; unsupported impact UNKNOWN; no TTQS self-score.
9. Reviewer can retrieve a verified source and repeat checks.
10. Word native render, visual QA, technical checks, and independent semantic review bind to final exact DOCX SHA. This Blueprint is not a DOCX/acceptance receipt.

## Source identities

- Crosswalk: I19-E26,1,0,0136,公益活動、獎項與學校合作原件驗證登錄表.
- Seed: 0136,I19-E26,0136__公益活動、獎項與學校合作原件驗證登錄表.docx.
- Project 157 index 150: current branch file quality-review/0133_R01_20261024/source/PROJECT_157_BLUEPRINT_INDEX144_146_EXCERPT.md.
- Official source: printed page 8 continues onto page 9; see included extract and source manifest.
- Source commit: 03d73cb900e28d7cd8ea02ec0c43c4564b521e33.
