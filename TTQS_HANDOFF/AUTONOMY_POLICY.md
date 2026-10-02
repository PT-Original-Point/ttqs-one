# Autonomy policy

Default loop:
BUILD 10 -> STATIC HARD GATES -> FRESH REVIEW -> PUBLISH PASSING DOCS TO CURRENT -> DELTA CHECKPOINT -> CONTINUE.

Human is not workflow heartbeat.
Every 10 docs may emit a concise NON-BLOCKING status. Continue automatically if gates pass.

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
