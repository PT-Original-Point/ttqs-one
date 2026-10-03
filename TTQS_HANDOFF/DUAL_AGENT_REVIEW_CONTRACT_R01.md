# TTQS_ONE Dual-Agent Review Contract R01 — 2026-10-03

## Architecture
Single canonical writer + single independent semantic reviewer.

Codex owns BUILD, deterministic/static/layout gates, canonical queue/register/CURRENT/checkpoints.
OpenCode owns independent semantic/usability review only.

Canonical promotion pipeline:
BUILD -> STATIC/LAYOUT/RECEIPT PASS -> WAITING_OPENCODE_REVIEW -> OPENCODE PASS -> PROMOTE CURRENT

There is NO second mandatory Codex semantic acceptance gate. Codex may run diagnostics for repair, but builder/self-review never grants promotion.

## Immutable artifact invariant
CONTROL_PLANE_DEFECT != DOCUMENT_DEFECT.
REVIEW_INFRA_DEFECT != DOCUMENT_DEFECT.
WAITING_OPENCODE_REVIEW != CONTENT_FAIL.
NO_CONTENT_OR_LAYOUT_CHANGE => DOCX_SHA_MUST_NOT_CHANGE.

Control, queue, receipt, review-request, checkpoint, policy, or scheduler changes must be sidecar/control-plane only and must not resave DOCX.

## Defect classes
- CONTENT_DEFECT: exact body/content issue; may authorize targeted DOCX repair.
- LAYOUT_DEFECT: exact pagination/table/font/layout issue; may authorize targeted DOCX repair.
- CONTROL_PLANE_DEFECT: runtime/state/hash/parser/verifier/scheduler bug; repair control only.
- REVIEW_INFRA_DEFECT: OpenCode invocation/auth/timeout/schema/bus issue; repair review infrastructure only.
- TRANSIENT_EXECUTION_DEFECT: crash/timeout/lock/process issue; retry/queue-tail only.

Only CONTENT_DEFECT or LAYOUT_DEFECT may mutate DOCX.

## Review dimensions
OpenCode must independently assess:
1. exact TTQS requirement fit;
2. correct document genre mechanics;
3. title-blind identification;
4. negative-neighbor rejection;
5. substantive cross-document duplication;
6. middle-school 30-second comprehension;
7. association/operator direct usability;
8. evaluator-facing professionalism;
9. SAMPLE/REAL truth boundary;
10. third-party fabrication;
11. internal engineering-language pollution;
12. unreasonable document inflation;
13. blank/sparse/orphan-page evidence when reliably available.

Verdict only:
PASS | FAIL_REPAIRABLE | FAIL_SYSTEMIC

FAIL requires exact locator + minimum repair.
Every verdict binds deliverable_id + exact candidate SHA256 + review_contract_hash.

## Human gate
Human is not runtime relay.
Only Mission/Spec change, real authority/SAMPLE-vs-REAL ambiguity, legal/signature/identity/OAuth/MFA, missing real-world prerequisite that materially changes deliverable, unresolved external side effect, or final acceptance may stop for Human.
