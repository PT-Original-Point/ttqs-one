# HOTFIX8 — OpenCode 429 Detector Narrow Fix — 2026-10-04

Concrete defect:
The OpenCode worker misclassified a successful Muse review as provider HTTP 429 because it scanned ordinary response/body text for the token "429". In the successful 0076 attempt, CLI exit=0, session export attested Muse Spark 1.3 Free, and review JSON passed; the body merely contained "429" as normal content/identifier.

## Invariant
Provider backpressure MUST be determined only from transport/runtime evidence, never arbitrary model/document text.

Valid 429 evidence:
- explicit HTTP status_code == 429 from structured transport metadata;
- structured provider error object/code identifying rate_limit / quota / 429;
- CLI/runtime non-success with machine-readable provider-rate-limit classification.

Invalid 429 evidence:
- substring "429" in model output;
- document content;
- fact IDs;
- line numbers;
- filenames;
- review JSON body text.

## Recovery
- Salvage the successful 0076 exact-SHA review result; do not re-run model and do not change DOCX.
- Reconcile/cancel any cooldown that was created solely by the false-positive detector.
- Re-evaluate recent OpenCode attempts that were classified 429 by text scanning; if transport evidence shows success, salvage exact results.
- Do not broadly re-review or rebuild documents.

## Deadline behavior
After this detector fix, control-plane freeze resumes. Continue production immediately.
