# R04 HOTFIX3 — AUTOMATED CODEX↔OPENCODE REVIEW BUS — 2026-10-03

## Purpose
Remove Human from routine progress relay. ChatGPT Web is not part of the per-document runtime loop.
Codex remains the only canonical builder/promotion owner. OpenCode becomes a headless independent reviewer invoked automatically on the same Win10 host.

## Runtime topology
- Codex runtime: E:\TTQS\TTQS_ONE_CODEX_RUNTIME
- OpenCode review workspace: E:\TTQS\TTQS_ONE_OPENCODE_REVIEW
- Agent bus: E:\TTQS\TTQS_ONE_AGENT_BUS

Required bus directories:
- INBOX\
- REVIEWS\
- REPAIR_SPECS\
- CORPUS_FINDINGS\
- PROCESSED\
- DEADLETTER\
- LOGS\
- LOCKS\

## Authority / ownership
Codex owns:
- canonical DOCX build/repair
- BUILD_QUEUE / SUPERVISOR_STATE
- central synthetic/replacement register
- CURRENT promotion/demotion
- checkpoints

OpenCode owns only:
- exact-SHA independent review artifacts under its review workspace / bus outputs

OpenCode MUST NOT modify canonical runtime/shared state or candidate DOCX bytes.

## Headless OpenCode preflight
Codex must first verify the real local automation surface:
1. Get-Command opencode
2. opencode --version
3. opencode models (or an equivalent authenticated smoke read)
4. one harmless non-interactive smoke call using `opencode run`
5. verify the call can run with no visible console/focus stealing when spawned by Python with Windows CREATE_NO_WINDOW / redirected stdio.

Do not assume the Desktop UI implies the CLI is installed/authenticated.
If CLI/auth is unavailable, this is a one-time local prerequisite. Do not fall back to GUI automation.

OpenCode supports non-interactive `opencode run`. If startup latency is material and a verified local server route is available, Codex may use a long-lived OpenCode server and attach review calls to it. No visible launcher is allowed.

## Review request contract
After a candidate is stable and Codex static gates pass, Codex atomically writes:
AGENT_BUS\INBOX\<deliverable_id>__<candidate_sha256>.json

Required fields:
- request_id
- deliverable_id
- candidate_path
- candidate_sha256
- requirement_id
- document_family
- blueprint_row_hash
- source_anchor_hash
- review_contract_hash
- created_at

Use temp-write + atomic rename. A request is immutable after publication.

Idempotency key:
deliverable_id + candidate_sha256 + review_contract_hash

Do not enqueue duplicate reviews for the same key.

## OpenCode review worker
Codex supervisor starts/manages one hidden local OpenCode review worker. Do not create another visible recurring Scheduled Task.

Worker behavior:
1. claim one unprocessed request using an atomic claim/lock;
2. recompute candidate SHA;
3. if SHA differs -> write STALE_REVIEW_REQUEST and process next request;
4. invoke OpenCode in non-interactive mode with the frozen independent-review prompt;
5. require OpenCode to write structured exact-SHA review output;
6. validate output schema and SHA binding;
7. atomically publish result;
8. move request to PROCESSED;
9. continue automatically.

One review worker maximum on this home PC.

## Reviewer contract
Every promotion review must cover:
- exact requirement fit
- correct document genre mechanics
- title-blind identification
- negative-neighbor rejection
- substantive cross-document duplication
- middle-school 30-second comprehension
- association/operator direct usability
- evaluator-facing professionalism
- SAMPLE/REAL truth boundary
- third-party fabrication check
- internal engineering-language pollution
- unreasonable document inflation
- blank/sparse/orphan page evidence when reliably available

Verdict only:
- PASS
- FAIL_REPAIRABLE
- FAIL_SYSTEMIC

FAIL must provide exact locators and minimum repair requirements.

## Pipeline
Codex BUILD N+1 may run while OpenCode REVIEW N runs.

Stable candidate
-> Codex deterministic/static gate
-> enqueue exact-SHA OpenCode review
-> Codex immediately continues another READY build lane
-> OpenCode PASS => Codex promotion eligibility
-> OpenCode FAIL_REPAIRABLE => exact repair lane
-> OpenCode FAIL_SYSTEMIC => scoped impact scan; unaffected READY lanes continue

A waiting external review blocks only the exact document lane.

## Recovery
On supervisor restart:
- read INBOX/PROCESSED/REVIEWS;
- do not re-dispatch an idempotency key that already has a valid exact-SHA result;
- reclaim only stale worker claims whose process is proven dead;
- no Human relay.

If OpenCode review invocation crashes/times out:
- classify as transient exact-lane failure;
- retry with bounded backoff;
- then DEADLETTER exact request and continue other READY lanes;
- do not promote without the required independent review;
- do not global-stop the project.

## Desktop non-interference
All OpenCode automation is headless.
No visible cmd/PowerShell/Python/OpenCode terminal, no focus stealing, no UI automation.
Use redirected stdio and Windows no-window process creation.
The existing R04 HOTFIX2 no-visible-console policy remains mandatory.

## ChatGPT Web role
ChatGPT Web is NOT a runtime relay and must not be required per document.
It is used only for:
- Human Mission/spec changes;
- bounded audits / acceptance review;
- true Human Gate interpretation;
- final acceptance support.

## Acceptance
Automation is accepted only after:
1. Codex automatically emits one review request;
2. OpenCode headlessly consumes it;
3. result returns exact-SHA bound;
4. Codex consumes the result without Human copy/paste;
5. PASS promotes or FAIL creates repair lane correctly;
6. a second document repeats the full cycle;
7. no visible window appears during the two end-to-end cycles;
8. existing queue/checkpoints remain intact.

Do not start a parallel OpenCode builder lane during this hotfix.
