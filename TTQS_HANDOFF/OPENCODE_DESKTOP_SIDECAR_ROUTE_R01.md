# OpenCode Desktop-Sidecar Route R01 — 2026-10-04

Human intent: use the normal official OpenCode Desktop execution path for Muse Spark 1.3 Free instead of relying on repeated standalone `opencode run` invocations.

## Reason
Muse free-tier behavior can differ by client/session path. A provider 429 from standalone headless `opencode run` is not proof of a bot ban, but repeated 429s make that route unsuitable as the primary deadline path.

## Preferred route
1. Detect the already-running OpenCode Desktop local server / opencode-cli sidecar from the live Windows host.
2. Read back its actual localhost endpoint from process/listening-port/config evidence; do not guess a port.
3. Use the official OpenCode client/SDK against that existing local server.
4. Create or reuse a dedicated TTQS_ONE session inside that server context.
5. Pin Muse Spark 1.3 Free using the resolved canonical CLI/model identity.
6. Submit BUILD/REVIEW tasks as normal OpenCode sessions through that server.
7. Read session status/result from the same official server.
8. Persist exact candidate SHA, work_id, session_id, requested_model_id and actual_model_id.

This is not GUI click automation. It uses the same official local server that the Desktop UI uses.

## Route order
PRIMARY = DESKTOP_LOCAL_SERVER_SESSION
SECONDARY = OFFICIAL_TUI/CLI SESSION ATTACHED_TO_SAME_SERVER, only if supported without changing provider/session semantics
DISABLED_BY_DEFAULT = STANDALONE_OPENCODE_RUN for Muse free-tier production work

## Validation
Before using for production, run one harmless prompt in a dedicated test session and prove:
- server is the Desktop-owned local server;
- Muse Spark 1.3 Free is actually selected;
- session completes without 429;
- result is readable through the same server;
- no visible console/focus stealing;
- Desktop UI remains optional.

If Desktop-sidecar route also returns 429, classify as provider/backpressure. Do not switch to another OpenCode model.

## GUI automation
Do not automate mouse/keyboard into the Desktop UI unless the official Desktop local-server/session route is unavailable and Human explicitly authorizes visible UI automation. UI automation is last resort because it is fragile and can steal focus.
