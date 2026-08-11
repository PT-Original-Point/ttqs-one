# TTQS ONE

TTQS ONE is the controlled TEST runtime for the 2026-08-13 consultant demonstration.

## v0.6.0 acceptance path

Real Google Forms SAMPLE submission -> Apps Script -> 15-table core database -> EventJobLedger -> bounded retry -> reconciliation -> automatic 19-indicator consultant evidence index.

Hard gates:

- TEST/DEV only. No PROD deployment workflow exists.
- `ENABLE_REAL_WRITES=false` and `PII_VAULT_READY=false` are code-level fail-closed controls.
- Demo inputs use SAMPLE aliases only; do not enter real PII or medical information.
- Indicators 17-19 remain `FORMAL_BLOCKED_NEEDS_REAL` until genuine REAL outcome evidence exists.
- `FormResponse.submit()` is not used for runtime acceptance. Submit through the real Google Forms UI.
- `clasp` push scope is fail-closed: `.clasp.json` uses `rootDir=apps-script`, `.claspignore` only admits `appsscript.json` and root-level `*.gs`, and CI verifies `show-file-status --json` before any push.

## Main TEST entrypoints

- `ttqsBootstrapTest()`
- `ttqsHealthCheck()`
- `ttqsInjectNextRegistrationFailure()`
- `ttqsCreateFaultProbe()`
- `ttqsRetryFailedJobs()`
- `ttqsReconcile()`
- `ttqsRefreshConsultView()`
