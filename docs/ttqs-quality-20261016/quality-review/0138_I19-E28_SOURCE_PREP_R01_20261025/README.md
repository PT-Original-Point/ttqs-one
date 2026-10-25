# DOCX 0138 / I19-E28 source preparation R01

**Preparation baseline (2026-10-25):** `SOURCE_READY` before the later R08 candidate was built; see the current R08 status below. This package binds the current official row, official p.9 text, Unique Blueprint index 152, 142-document crosswalk, genre guidance, and the adjacent 0126 synthetic source contract.

- Source baseline at preparation: PR #92 branch commit `339c79e7341e35cc77790374655901a6a292d75c`.
- DOCX 0138 / I19-E28 / 157 index 152 are distinct identifiers.
- Current source row and raw Git blob comparisons are recorded in `SOURCE_PREP_RECEIPT_0138_R01.json`.
- A legacy 2044 R02 artifact was inspected and rejected as a quality-ready candidate: 1,541 extracted characters, many `[待補]` fields, no complete SAMPLE/SYNTHETIC case. Current Blueprint prohibits historical-body reuse. See `ARCHIVE_TRIAGE_0138_R02.md`.
- No actual participant consent, employer source, salary/reward/promotion record, issuer response, or approval was provided. REAL evidence remains `UNKNOWN/HOLD`.
- Do not upload real payroll/employment originals or identity keys to this public repository.

## Current R08 candidate status (reconciled 2026-10-26)

- Current candidate: DOCX 0138 / I19-E28 / Project 157 index 152, SHA-256 `f06439849ba70d0ad665d760d0a422382d9f4a991ca449b36f05fae39abd5a27`. It was built from the local manuscript by `build_0138_r08.py`; no DOCX rebuild was made for this metadata reconciliation.
- Technical QA: `PASS_SCOPED`. Word-native visual QA: `PASS_VISUAL_SCOPE_ONLY`, 15 pages; PDF SHA-256 `fa28010481f34ddab55fcf071c53db5c72c8868857603e24a58579a6aa997650`.
- Antigravity semantic response: reviewer verdict PASS on the exact candidate SHA; adjudication status `PASS_RECORDED_MODEL_IDENTITY_UNKNOWN`. The adjudication confirms exact-SHA binding and selected cited anchors; it explicitly does not independently verify every semantic proposition. Requested model was `gemini-3.8-flash-high`; actual serving model and usage are UNKNOWN.
- OpenCode v2 review attempt: nonzero exit, no review returned, `adopted=false`.
- Antigravity writer attempt returned 26,482 characters and CLI-reported 31,110 tokens, but `adopted_worker_text=false`; the manuscript and DOCX were built independently from the source packet and Unique Blueprint.
- Existing GitHub readback receipt covers 16 files. Candidate DOCX and Word PDF matched byte-for-byte; text files matched after Git line-ending normalization. Source readback commit: `48b3380af283b8c8f23a954e8c79e1f5816e8851`.
- This remains CANDIDATE only. REAL evidence is UNKNOWN/HOLD; formal acceptance is NOT_GRANTED. See `STATUS_RECONCILIATION_0138_R08_20261026.json`.
