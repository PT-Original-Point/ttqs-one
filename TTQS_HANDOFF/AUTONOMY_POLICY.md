# Autonomy policy

Default loop:
BUILD 10 -> STATIC HARD GATES -> FRESH REVIEW -> PUBLISH CURRENT -> DELTA CHECKPOINT -> CONTINUE.

Human is not workflow heartbeat.
Every 10 docs may emit a concise NON-BLOCKING status. Continue automatically if gates pass.

Escalate to Human only when:
1. mission/quality policy must change;
2. two repair epochs fail the same substantive issue;
3. fresh reviewers disagree and sources cannot resolve it;
4. SAMPLE vs REAL / third-party authority is genuinely ambiguous;
5. final evaluation package needs Human acceptance.

Automatic defect handling:
- single defect -> rebuild exact doc from source;
- same requirement inconsistency -> rebuild requirement slice;
- same-family anti-pattern -> family impact scan/rebuild;
- cross-family template/old-policy pollution -> taint affected quality epoch;
- forged third-party or SAMPLE represented as REAL -> quarantine affected epoch immediately.

Human may randomly inspect CURRENT anytime. A Human finding outranks automated PASS, but Human is never required to keep the queue moving.
