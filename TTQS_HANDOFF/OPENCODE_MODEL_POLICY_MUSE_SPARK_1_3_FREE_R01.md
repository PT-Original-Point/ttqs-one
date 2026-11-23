# OpenCode Model Pin — Muse Spark 1.3 Free — R01

Human explicit model policy:
OpenCode may use ONLY the model displayed as "Muse Spark 1.3 Free".

## Hard allowlist
ALLOWED_DISPLAY_MODEL = Muse Spark 1.3 Free
FALLBACK_MODELS = NONE

Forbidden examples include every other discovered OpenCode model, including:
- ling-3.1-flash-free
- mimo-v2.6-flash-free
- nemotron-3.5-lightning-free
and any other model not proven to be the exact CLI identity corresponding to "Muse Spark 1.3 Free".

## Headless execution
Do not trust Desktop UI selection alone.
Before first headless dispatch, resolve the exact CLI model identifier corresponding to display label "Muse Spark 1.3 Free" from local OpenCode configuration/model metadata. Do not guess the slug.

Persist:
- allowed_display_model
- resolved_cli_model_id
- resolution_evidence
- resolved_at

Every OpenCode BUILD/REVIEW/REPAIR invocation must explicitly pin that resolved CLI model identifier.

If the exact CLI identity cannot be proven:
- OPENCODE_MODEL_ROUTE_BLOCKED
- do not substitute another model
- Codex READY lanes continue
- this is not a Human Gate unless interactive authentication is actually required.

## 429 policy
If Muse Spark 1.3 Free returns 429:
- classify PROVIDER_BACKPRESSURE
- honor Retry-After when available
- otherwise bounded exponential backoff
- do not switch to another model
- do not modify DOCX
- do not count as content/repair failure
- Codex continues other READY work

## Result acceptance
Every OpenCode result must record the actual model identity used.
If actual model != resolved allowed Muse Spark model:
MODEL_POLICY_VIOLATION
The result is invalid for promotion and must not be reused.


## Preferred official client route
For Muse Spark 1.3 Free, route priority is:
1. OpenCode Desktop-owned local server / opencode-cli sidecar session via official OpenCode client/SDK.
2. An official session attached to that same server, if needed.
3. Standalone `opencode run` is disabled by default for deadline production because repeated 429s were observed on that route.

Do not use another model. If the Desktop-sidecar route also receives 429, classify provider backpressure.
