# Autonomy policy

Default loop:
BUILD -> STATIC HARD GATES -> FRESH SEMANTIC REVIEW -> PUBLISH PASSING DOCS TO CURRENT -> DELTA CHECKPOINT -> CONTINUE.

Human is not workflow heartbeat.
Every 10 docs may emit a concise NON-BLOCKING status. Continue automatically if gates pass.

## Throughput / anti-churn policy
- One scheduling turn gives each lane at most one build-or-repair attempt. If it does not pass, move that lane to the back of the READY queue; do not retry the same lane immediately while other READY work exists.
- Builder responsibility ends when a stable DOCX + build receipt are written. Builder MUST NOT run duplicate PowerShell/Word/LibreOffice/CUA/PDF self-check pipelines that are already owned by the static gate or reviewer.
- If a builder exits non-zero but leaves a stable new DOCX + valid receipt, salvage that exact candidate: run static gate + fresh review before deciding to rebuild. Never discard a completed candidate merely because builder cleanup/self-check failed.
- Static gate owns deterministic checks: DOCX/OOXML integrity, placeholders, font floors, required markers, arithmetic/source consistency that is machine-checkable, candidate/receipt SHA binding.
- Fresh reviewer owns semantic/usability checks only: exact requirement fit, genre mechanics, title-blind identification, negative-neighbor rejection, middle-school first-glance readability, evaluator-facing professionalism, SAMPLE/REAL truth boundary. Reviewer MUST NOT launch Word COM, CUA, PDF/PNG rendering, or nested Codex probes unless an exact layout anomaly has already been identified.
- Allow at most two active execution units on this home PC: one BUILD lane and one REVIEW lane for a different document. All shared writes (central synthetic register, queue promotion, CURRENT publish, checkpoint) are serialized under one promotion lock.
- Cache authoritative source readback per deliverable by exact source SHA + Blueprint row hash. Reuse only when both hashes are unchanged; do not repeatedly re-read Drive/PDF sources without an evidence delta.
- A timed-out/crashed build or review is TRANSIENT for that exact lane. Return it to queue tail and continue other READY lanes.
- Do not rescan/re-hash the full 142 corpus after every document. Use delta-only verification except at explicit final QA.
- No full-corpus PDF/PNG rendering. Render only an exact document/page when a concrete layout anomaly is detected.
- After two consecutive Canary documents PASS under the same builder/static/reviewer contract, freeze that acceptance contract for the remaining Canary/production run. A later control change may invalidate prior PASS only when tied to a concrete source defect or exact artifact defect with body locators; policy drift alone is not enough.

## Non-blocking failure policy
- A single document failure parks only that document lane.
- A single canary failure parks only that canary lane; continue all other READY canaries.
- Passing canaries are published to CURRENT immediately so Human may inspect them without blocking execution.
- Two failed repair epochs on the same logical defect trigger CHURN_FUSE on that exact lane: stop blind rebuild, perform root-cause audit, fix the builder/reviewer/validator contract or source interpretation, then retry only after a material delta.
- CHURN_FUSE is NOT a Human Gate and NOT a Project blocker.
- Full production rollout still requires the required representative Canary set to pass, but the system must autonomously repair parked canaries while continuing every other legal READY lane.

## Escalate to Human only when
1. Mission/spec or major quality policy must change and the answer cannot be derived from current authority;
2. SAMPLE vs REAL / third-party authority is genuinely ambiguous;
3. legal/signature/identity/OAuth/MFA is required;
4. a missing third-party original or real-world fact materially changes the required deliverable and cannot be obtained automatically;
5. bounded readback/root-cause reconciliation leaves external side effect or authority ambiguity unresolved;
6. final evaluation package needs Human acceptance.

Do NOT escalate merely because:
- one document fails;
- one canary fails;
- two repair attempts fail;
- a local script/validator/parser is defective;
- a reviewer issue can be resolved from official sources.

## Automatic defect handling
- single defect -> rebuild exact doc from source;
- same requirement inconsistency -> rebuild requirement slice;
- same-family anti-pattern -> family impact scan/rebuild;
- cross-family template/old-policy pollution -> taint affected quality epoch;
- forged third-party or SAMPLE represented as REAL -> quarantine affected epoch immediately;
- repeated same defect with no material delta -> park exact lane, root-cause audit, repair contract, continue other READY lanes.

Human may randomly inspect CURRENT anytime. A Human finding outranks automated PASS, but Human is never required to keep the queue moving.

## Anti-garbage rule for efficiency work
Efficiency changes are invalid if they reduce semantic review coverage. No fast path may skip fresh review, reuse peer document bodies as templates, or promote on technical validity alone. Every promotion still requires requirement-specific genre mechanics, title-blind identification, negative-neighbor rejection, substantive-duplication screening, evaluator-facing readability, and SAMPLE/REAL truth-boundary PASS. Caching may reuse source readback, calculations, and shared fact IDs only; not generated prose or document bodies.

## HOTFIX5 delete-first dual-agent pipeline
The stable acceptance path is BUILD -> STATIC/LAYOUT/RECEIPT -> OpenCode exact-SHA independent semantic review -> promotion. Remove duplicate mandatory Codex semantic acceptance from the critical path. Codex may diagnose repairs but cannot self-accept content.
Defect classes are CONTENT_DEFECT, LAYOUT_DEFECT, CONTROL_PLANE_DEFECT, REVIEW_INFRA_DEFECT, TRANSIENT_EXECUTION_DEFECT. Only the first two may mutate DOCX.
NO_CONTENT_OR_LAYOUT_CHANGE => DOCX_SHA_MUST_NOT_CHANGE.
WAITING_OPENCODE_REVIEW != CONTENT_FAIL.
Control/review infrastructure defects repair only their own lane/control surface, never document bytes.
