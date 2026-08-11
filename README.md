# TTQS ONE

TTQS ONE is the controlled TEST runtime for the 2026-08-13 consultant demonstration.

## v0.6.2 authorization preflight hardening

Acceptance path:

Real Google Forms SAMPLE submission -> Apps Script -> TEST core database -> EventJobLedger -> controlled failure -> bounded automatic retry -> exact-count reconciliation -> runtime EvidenceMaster registration -> automatic 19-indicator consultant evidence index.

Hard gates:

- TEST only for the 8/13 runtime acceptance path; PROD remains untouched.
- `ENABLE_REAL_WRITES=false` and `PII_VAULT_READY=false` are fail-closed code controls.
- `ttqsBootstrapTest()` requires consent for all explicit manifest scopes before any lock, health check, ledger write, Form creation, or trigger creation.
- Google Forms expose only controlled SAMPLE choices; no arbitrary respondent text field is created.
- Indicators 17-19 remain `FORMAL_BLOCKED_NEEDS_REAL` until genuine REAL outcome evidence exists.
- `FormResponse.submit()` is not used for runtime acceptance; submissions must use the real Google Forms UI.
- `clasp` push scope remains exactly `appsscript.json` plus 13 root-level `.gs` files.
- Runtime writes use a ScriptLock, retry provenance is explicit, and reconciliation requires exactly one SurveyResponse, PartyAlias, and runtime EvidenceMaster record.
- Bootstrap is journaled before side effects and can reuse a previously-created Form when a prior run stopped before response-sheet mapping completed.
- CI verifies every `release/MANIFEST.sha256` entry plus the manifest self hash before tests or deployment-scope verification.

## Main TEST entrypoints

- `ttqsBootstrapTest()`
- `ttqsHealthCheck()`
- `ttqsInjectNextRegistrationFailure()`
- `ttqsCreateFaultProbe()`
- `ttqsRetryFailedJobs()`
- `ttqsReconcile()`
- `ttqsRefreshConsultView()`
