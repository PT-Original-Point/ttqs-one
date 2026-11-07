# DOCX 0091 unique content blueprint

Source: `SOURCE_BOUND_WRITER_PACKET_R01.md`; source SHA-256: bafcd91970cd44e69f5b5b87b848f4e95accc88c7e3356d7be2ae5c87508cb60

## Unique content blueprint

### Purpose and reader

Help a small training association's authorized training administrator safely request, receive, inspect, verify, index, and retrieve learner employment proof when the learner chooses to provide it. The document must be usable by a volunteer administrator with no full-time HR department. It must keep learner self-report, a received document, and issuer verification as distinct evidence grades.

### Required operating sequence

1. Identify the training cohort, follow-up due date, and approved evidence purpose from REAL records before opening a case. Missing source means `HOLD_SOURCE_NOT_CONFIRMED`.
2. Check the applicable privacy notice/consent and scope before contacting a learner or employer. No employer contact without documented, valid authorization and an approved channel. A refusal or withdrawal stops optional contact and is recorded without penalty language.
3. Ask the learner to provide proof voluntarily through the association's authorized channel. Offer a safe alternative if the learner declines employer contact. Do not request unnecessary sensitive fields.
4. Record receipt without exposing personal information in the public evidence package. Keep the original in the authorized restricted store; the public DOCX/register contains only a synthetic locator or a redacted reference, never a real certificate.
5. Check the submitted item's type, issuer, date, subject/cohort linkage, legibility, completeness, and whether it actually supports the stated employment fact. Document what was checked and what was not.
6. If issuer verification is necessary, confirm authority and learner authorization first; use only an authorized channel and record method/date/role. Never imply contact occurred when it did not.
7. Apply an explicit disposition with evidence grade, rationale, reviewer role, due date, correction path, and next action.
8. Reconcile the case register to source population and follow-up window before calculating any aggregate. If the population or denominator is unknown, report no rate.

### Document-specific forms/tables

- Evidence-grade ladder: self-report; original voluntarily supplied but not checked; document inspected for completeness; issuer/authorized source checked; unresolved/invalid. Define precisely what each state proves and does not prove.
- Pre-contact authorization gate with required basis, scope, date, expiry, permitted channel, withdrawal status, checker, and `PASS/HOLD/STOP`; no `PASS` without evidence locator.
- Learner request template (association-to-learner), optional employer-request template (association-to-employer only after authorization), and nonresponse/decline script. Label all as SAMPLE and avoid claiming they were sent.
- Evidence intake and verification register with one row per case: synthetic case ID, cohort/source locator, due window, self-report status, consent status, item type, issuer code, received date, restricted original locator, checks performed, verification method, evidence grade, disposition, reviewer role, hold reason, responsible role, next due date, correction trail.
- Decision table that distinguishes `HOLD_NO_AUTHORIZATION`, `HOLD_NO_ORIGINAL`, `PENDING_AUTHORIZED_CHECK`, `VERIFIED_WITH_SCOPE`, `NOT_SUPPORTED`, `DECLINED`, and `STOP_WITHDRAWN`. Do not use `VERIFIED` in the sample case.
- Complete worked sample with every field filled and a defensible hold decision; explain why an employment self-report is not an employment certificate.
- Synthetic replacement register mapping each invented date, case code, role code, result, and locator to its field and the exact REAL item that must replace it.
- Retrieval/access log and correction/appeal route that does not expose real personal information in a public repository.

### Negative-neighbor separation

- 0090 / I17D-E04 assesses supervisor-observed learning outcomes; it cannot substitute for the learner's employment proof or be presented as employer evidence.
- 0092 / I17D-E06 concerns a thank-you letter request and original tracking; it is not employment proof. Keep the workflows and document outputs separate.
- 0088 / I17D-E02 is broader post-training follow-up. Reference its verified source only if available; do not copy its cases, outcomes, denominators, or claims into this file. If no exact shared case source is confirmed, keep the sample case unique to 0091.

### Required sections and title-blind test

1. Plain-language cover: purpose, user, when to use, what this file records, and `SAMPLE / SYNTHETIC — no association certificate or employment record supplied`.
2. Requirement and boundary: exact checkbox, evidence-grade distinction, and what this record cannot replace.
3. Roles and low-maintenance workflow for a volunteer association; do not invent a department or delegated authority.
4. Authorization and privacy gate.
5. Step-by-step request, intake, inspection, verification and retrieval SOP, including exception branches.
6. Ready-to-use blank forms plus at least one fully completed synthetic hold case and worked decision.
7. Decision rules, correction/review path, retention/access locator fields, and rejection/hold criteria.
8. Synthetic replacement register and REAL replacement checklist.
9. Cross-document links and explicit non-substitution with 0090 and 0092.

If the title is covered, a reader must still recognize this as an association-side employment-proof request/intake/verification workflow. If the body could be relabeled as the supervisor learning-outcome form or thank-you letter log, it fails.
