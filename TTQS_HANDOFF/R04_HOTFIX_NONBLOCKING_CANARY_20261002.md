# R04 HOTFIX — NONBLOCKING CANARY / HUMAN-GATE CORRECTION — 2026-10-02

## Root cause
The prior policy incorrectly treated "two repair epochs fail the same substantive issue" as a Human Gate.
That contradicts the Human Mission and NON_BLOCKING_BY_DEFAULT.

## Exact correction
1. Revoke any Human Gate raised solely because deliverable 0003 failed two repair epochs.
2. Set 0003 status to PARKED_ROOT_CAUSE_REPAIR.
3. Re-enable supervisor.
4. Continue all other READY Canary lanes immediately.
5. Publish every passing Canary to E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CURRENT as soon as it passes.
6. Keep production rollout denied until the required Canary set passes, but do not stop the executor while repairable work remains.
7. For 0003, the current review defect is concrete and source-resolvable:
   - the questionnaire rule says Q4 allows up to three needs and requires one concrete work/life scenario for each selected need;
   - the synthetic answer lists three needs but does not supply one concrete scenario for each.
   Repair from source by adding one explicit concrete scenario per selected Q4 need, register any new synthetic facts, run fresh review, and promote only if it passes.
8. If the same defect persists after bounded repair, run root-cause audit of builder/reviewer/validator instructions. Do not ask Human unless there is genuine authority ambiguity or missing external reality information.

## Human Gate definition
Human Gate is reserved for Mission/spec change, genuine SAMPLE/REAL authority ambiguity, legal/signature/identity/OAuth/MFA, missing third-party reality that changes the deliverable, unresolved external side effects after bounded readback, or final package acceptance.
