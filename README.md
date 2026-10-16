# TTQS ONE

TTQS ONE is the controlled TEST runtime for the 2026-08-13 consultant demonstration.

## v0.6.3 adversarial-audit hardening

Acceptance path:

Real Google Forms SAMPLE submission -> immutable raw event identity -> Apps Script -> TEST core database -> EventJobLedger -> controlled failure -> bounded automatic retry -> raw-root exact reconciliation -> runtime EvidenceMaster registration -> automatic 19-indicator consultant evidence index.

Hard gates:

- TEST only for the 8/13 runtime acceptance path; PROD remains untouched.
- `ENABLE_REAL_WRITES=false` and `PII_VAULT_READY=false` are fail-closed code controls.
- `ttqsBootstrapTest()` requires consent for all explicit manifest scopes before any lock, health check, ledger write, Form creation, or trigger creation; Health also exposes current FULL authorization status.
- Google Forms expose only controlled SAMPLE choices; no arbitrary respondent text field is created.
- Each real Form response is assigned a persisted `TTQS_EVENT_ID` before JobLedger processing. `FORM_SUITE` identity uses Form ID + this immutable event ID; row number is only a locator.
- Retry handles due `FAILED` jobs and stale `RUNNING` jobs after a bounded lease, under a ScriptLock, and resolves the raw response again by immutable source reference.
- Reconciliation starts from the raw `RUNTIME_*_RESPONSES` rows, so a response whose installable trigger never created a JobLedger row is a mismatch rather than a false PASS.
- Reconciliation requires exact component counts and validates job/survey/party/evidence cross-links before `MATCHED_EXACTLY_ONCE`.
- Runtime EvidenceMaster rows are `TEST` / `SAMPLE`, carry raw/provider/job linkage, and are explicitly `NOT_FORMAL`; they do not prove formal TTQS outcomes.
- Managed trigger validation checks handler cardinality plus event type, trigger source, and the TEST core spreadsheet source ID for `onFormSubmit`.
- Runtime Forms must read back as published and expose a non-empty responder URL; real accessibility is still a Google provider runtime gate.
- Indicators 17-19 remain `FORMAL_BLOCKED_NEEDS_REAL` until genuine REAL outcome evidence exists.
- `FormResponse.submit()` is not used for runtime acceptance; submissions must use the real Google Forms UI.
- `clasp` push scope remains exactly `appsscript.json` plus 13 root-level `.gs` files.
- The release manifest verifier requires exact coverage of git-tracked regular files, excluding only the manifest and its separate self-hash file.
- GitHub Actions `checkout` and `setup-node` references are pinned to immutable commit SHAs rather than mutable major-version tags.

Evidence boundary:

- Source/CI PASS does not mean Google runtime PASS.
- Unit/contract/behavior tests do not prove Google OAuth, trigger scheduling, responder accessibility, or provider-side execution.
- Google provider runtime acceptance must independently verify identity ownership, remote source readback, real Form UI submission, Apps Script Executions evidence, exact reconciliation, and the 17-19 formal REAL gate.

Known non-blocking post-demo hardening:

- Remove CI-time `npx --yes` supply-chain dependence by locking the clasp tool graph.
- Re-evaluate TypeScript and a transactional database / Cloud Run architecture before REAL or scaled production use.

## Main TEST entrypoints

- `ttqsBootstrapTest()`
- `ttqsHealthCheck()`
- `ttqsInjectNextRegistrationFailure()`
- `ttqsCreateFaultProbe()`
- `ttqsRetryFailedJobs()`
- `ttqsReconcile()`
- `ttqsRefreshConsultView()`
