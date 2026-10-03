# TTQS_ONE Dual-Worker Sprint Contract R01 — 2026-10-03

## Goal
Maximize verified DOCX throughput before the 2026-10-05 morning TTQS evaluation without reintroducing template pollution, self-review, shared-state races, or control-plane SHA churn.

## Activation prerequisite
This sprint activates automatically only after HOTFIX5 proves two end-to-end exact-SHA review cycles with:
- HUMAN_RELAY_COUNT=0
- VISIBLE_CONSOLE_COUNT=0
- DOCX_SHA_CHANGED_BY_CONTROL_FIX=0
- duplicate/stale verdict reuse = 0

Until then, DOCX mutation remains frozen except for already-authorized true CONTENT_DEFECT/LAYOUT_DEFECT repairs.

## Two workers, no self-review
Worker identities:
- CODEX_WORKER
- OPENCODE_WORKER

For each deliverable, roles are per-document, not permanently tied to a model:
- one BUILD_OWNER
- the other agent is REVIEW_OWNER
- BUILD_OWNER != REVIEW_OWNER always

Codex remains the only canonical dispatcher/integrator/promoter and the only writer of shared control state.

## Work-stealing loop
Each model worker has one active model task maximum.

Priority:
1. review a ready candidate built by the other worker;
2. repair an exact defect on a document originally built by this worker;
3. build the next READY document assigned by the dispatcher.

This keeps both workers useful instead of leaving OpenCode idle.

## Assignment
Codex dispatcher creates immutable work packets under:
E:\TTQS\TTQS_ONE_AGENT_BUS\BUILD_INBOX\

Packet fields:
- work_id
- deliverable_id
- build_owner
- review_owner
- document_family
- requirement_id
- blueprint_row_hash
- source_anchor_hash
- evidence_bundle_path
- shared_fact_snapshot_path
- shared_fact_snapshot_hash
- shared_fact_groups
- acceptance_contract_hash
- output_staging_path

Atomic claim. One BUILD_OWNER per deliverable.

Do not concurrently build two documents whose declared shared_fact_groups overlap. If dependency groups are unknown, serialize that family.

## Evidence bundle
The dispatcher creates one immutable per-document evidence bundle from authoritative sources before build:
- exact requirement text
- exact Blueprint row
- verified source locators/excerpts
- document-family mechanics requirements
- current shared fact snapshot needed for consistency
- explicit known repair feedback for that same deliverable

No peer DOCX body is included.

Both builder and reviewer use the same source bundle/hash, but the reviewer receives no builder chain-of-thought or prose plan.

## Isolated outputs
Codex-built candidate:
E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CANDIDATES\...

OpenCode-built candidate:
E:\TTQS\TTQS_ONE_OPENCODE_BUILD\CANDIDATES\...

OpenCode may write only its isolated build workspace and task receipts/deltas. It never writes canonical queue, CURRENT, central register, supervisor state, or Codex automation code.

Each build returns:
- stable DOCX
- build receipt
- proposed synthetic-fact delta
- source/evidence hashes
- candidate SHA256

The proposed synthetic delta is not merged centrally until promotion.

## Deterministic integration gate
Codex integration layer runs deterministic gates for candidates from either builder:
- OOXML/open integrity
- required markers / forbidden placeholders
- font floors
- arithmetic checks where machine-verifiable
- engineering-language scan
- blank/sparse/orphan/table overflow lightweight hidden layout check
- candidate/receipt/evidence hash binding
- substantive duplication screen

No full-corpus PDF/PNG.

## Cross-review
If Codex built it -> OpenCode reviews exact SHA.
If OpenCode built it -> a fresh isolated Codex reviewer process reviews exact SHA.

No agent reviews its own artifact.

Review contract is DUAL_AGENT_REVIEW_CONTRACT_R01 plus:
- requirement fit
- genre mechanics
- title-blind
- negative-neighbor
- substantive duplication
- middle-school 30-second comprehension
- association direct usability
- evaluator professionalism
- SAMPLE/REAL boundary
- third-party fabrication
- engineering-language pollution
- unreasonable inflation
- reliable layout evidence

Verdict:
PASS | FAIL_REPAIRABLE | FAIL_SYSTEMIC

## Promotion
Only Codex integrator may promote.
Promotion requires:
- deterministic gate exact-SHA PASS
- independent reviewer exact-SHA PASS
- acceptance_contract_hash match
- synthetic delta validation

Then, under one promotion lock:
1. CAS/fresh-read shared fact groups;
2. merge approved synthetic delta;
3. publish exact reviewed DOCX to CURRENT;
4. update queue/checkpoint/receipts;
5. release lock.

If shared fact snapshot is stale at promotion:
- do not blindly rebuild;
- recompute whether the delta conflicts;
- if no conflict, rebind sidecar and promote without DOCX mutation;
- if content truly conflicts, return exact CONTENT_DEFECT to original builder.

## Throughput rules
- two model workers maximum: one Codex task + one OpenCode task.
- hidden deterministic integration is allowed, but Word COM/layout checks are serialized.
- no second visible scheduler.
- no Human relay.
- checkpoint/report every 10 promotions is non-blocking.
- do not wait for a 10-document batch to finish before starting the next ready work.
- do not reopen clean CURRENT documents for policy-only changes.

## Quality / anti-garbage
Speed may not change acceptance criteria.
No peer-body template reuse.
No generic prose/table/question/SOP body cloning.
SAMPLE must be fully worked and clearly non-REAL.
Internal IDs/registers stay in sidecars.
First page must explain purpose/user/timing/use/output in plain Chinese.
Only exact content/layout defects may mutate DOCX.

## Deadline scheduling
Until 2026-10-05 evaluation handoff:
Priority 0: finish/repair remaining canaries and any evaluator-facing known defects.
Priority 1: maximize named requirement coverage with evaluator-ready documents.
Priority 2: remaining planned 1:N support documents.
Within equal priority, choose READY work with no shared-fact collision and shortest unresolved dependency chain.

The target remains 142/142; prioritization changes order, not scope.
