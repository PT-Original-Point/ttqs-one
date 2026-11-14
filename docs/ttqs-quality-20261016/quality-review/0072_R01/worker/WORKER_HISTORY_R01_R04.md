# DOCX 0072 OpenCode V2 Writer and repair history

Binding: `0072 / I16-E03 / official checkbox 078`; official wording is 訓練的內外稽核流程與紀錄。 The outputs below are candidate material only. All worked facts remain `SAMPLE/SYNTHETIC`; real association audit activity, approvals, identities, and external evidence remain `UNKNOWN/HOLD`.

## Attempts and repairs

- **R01** — requested `opencode/deepseek-v4.1-flash-free`, OpenCode CLI v2.0.29; timed out at the 300-second wrapper limit after 21 tool calls, primarily reading neighboring 0070 material. No body was produced, stderr was empty, and the available diagnostic did not show a provider error. The run was stopped to prevent further context churn. This is not counted as three provider failures; the OpenCode route remains enabled.
- **R02** — isolated source-bound Writer, exit 0, stderr empty; produced a 30,261-byte body (`8472e6617f971fb041beef47ac2468bae00605d8b21f45b9ac983c67449e4e3d`). Its prompt and redacted full CLI transcript are preserved.
- **R03** — isolated targeted repair, exit 0, stderr empty; produced a 52,901-byte body (`429198331a3c81d586d5c08c01ffc279d99bd710329bed528004e7b8ee6c2331`). It repaired identified process/evidence gaps; source-bound patch packet and redacted transcript are preserved.
- **R04** — isolated targeted repair, exit 0, stderr empty; produced a 68,892-byte body (`a485f656da9e111a7a10b2b287ec6afbee5980a4e2d1c2c37a305f8ef461bff9`). A deterministic local register/consistency repair then produced the 73,156-byte build source `0072_R01_body_R04_QA.md` (`e76818aa55c14e49eff843f80aacbb3cc0cea1b9110526bd38e5a004590ac2e0`); original R04 source remains preserved unchanged.

## Final candidate and checks

- DOCX SHA-256: `3327fdc5200770dde695fc822eca3653feed0f562b156d4529e89cdecbdf052e` (79,100 bytes); official-source mapping and exact body/build hashes are in `evidence/build_receipt_R01.json`.
- Independent exact-SHA review: requested OpenCode CLI v2.0.29 model `opencode/beam-free`; initial SHA `94005e3b…` was `PARTIAL` only for 14 10-pt inline labels. A typography-only repair raised body minimum to 10.5 pt; extracted semantic text SHA remained `16aeaae9e4055b22585bed0aacf2228f44b53896a6fe293de18a89cc54115788`. The independent follow-up returned `PASS` for final SHA `3327fdc…`; full responses, invocation records, and logs are preserved. Provider model identity was not separately attested.
- Technical QA: DOCX ZIP readable; 228 paragraphs, 49 tables, no empty tables; body minimum 10.5 pt and table minimum 9.5 pt; 40-page Word PDF and all page images produced.
- Visual scope: all 40 pages inspected in contact sheets; pages 1, 2, 16, 17, 18, 20, 27, 33, 36, 38, 39, and 40 inspected full-size. No clipping, orphan heading, missing page number, or blank page was observed. The independent reviewer confirmed the supplied visual receipt but did not directly inspect all page images; visual inspection is recorded separately.
- Formal acceptance is not granted. Candidate remains `SAMPLE/SYNTHETIC`; REAL audit records and policy inputs are still `UNKNOWN/HOLD`.

R02/R03/R04 packets, all body revisions, redacted CLI transcripts, exact-SHA reviews, and technical/visual evidence are retained alongside this history. Transient CLI session/message identifiers are redacted from public transcripts; raw local logs remain preserved and their hashes are recorded in `worker/worker_history_redaction_manifest.json`.
