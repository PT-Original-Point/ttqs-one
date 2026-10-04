# TTQS_ONE Deadline Execution Override — 2026-10-04

Human priority: maximize evaluator-ready verified DOCX output before 2026-10-05 morning while preserving anti-garbage quality.

This is delete-first steering. It removes blocking conditions that are control-policy artifacts rather than document defects.

## 1. No global Canary blockade
A failing/pending Canary blocks only its exact lane or proven affected document family.
Unrelated READY production may proceed.
For an unproven family, the first READY deliverable acts as that family's local canary; if it passes deterministic + semantic review, that family continues.

## 2. OpenCode Muse is preferred, not a global availability gate
OpenCode may still use ONLY Muse Spark 1.3 Free.
No other OpenCode model is allowed.

For each candidate:
- preferred semantic review route: OpenCode Muse exact-SHA;
- if Muse returns provider 429/backpressure, immediately use a fresh isolated Codex reviewer process for that candidate;
- the fallback reviewer must be read-only, exact-SHA bound, and separated from the builder context;
- Muse catch-up review remains queued and may later invalidate only that exact document if it finds a concrete artifact defect.

No other OpenCode model is used.

## 3. Policy changes are not retroactive artifact defects
A new model-attestation field, queue field, review metadata field, control revision, or policy revision does not invalidate an earlier exact-SHA PASS by itself.
Previously accepted unchanged artifacts remain accepted unless there is a concrete source/artifact defect with an exact locator.
Therefore, do not demote CURRENT solely because an older review lacks requested_model_id/actual_model_id.

## 4. Control-plane freeze
Until evaluation handoff, do not refactor the supervisor/control architecture unless a concrete control failure blocks all READY production.
Use the existing proven hidden supervisor.
Control work must be narrowly scoped and must not delay READY document production.

## 5. Anti-churn
After two transient timeouts/retries on one logical lane with no new artifact/source defect:
- park that lane;
- move to queue tail;
- continue another READY lane;
- do not start a third identical repair/root-cause attempt immediately.

## 6. Production priority
P0: concrete known evaluator-facing defects and remaining canaries, without blocking unrelated work.
P1: named non-Other requirement coverage.
P2: remaining 1:N support documents.

Quality gates remain:
exact requirement/genre, title-blind, negative-neighbor, substantive duplication, evaluator readability, SAMPLE/REAL, no third-party fabrication, lightweight layout, no engineering pollution.
