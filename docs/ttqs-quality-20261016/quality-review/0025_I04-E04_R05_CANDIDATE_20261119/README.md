# 0025 I04-E04 R05 candidate evidence

This package preserves the exact R05 candidate and its scoped repair, deterministic QA, Word/PDF visual evidence, and W1 OpenCode v2 independent semantic review.

- Candidate: `candidate/0025_I04_E04_R05_CANDIDATE.docx`
- Candidate SHA-256: `B72A65EA05D118C6479747280DBA768AC27ECB0B2A335FDD61C0FA2A32D9FC2D`
- W1 requested route: `opencode/longcat-2.5-free`; served model is UNKNOWN.
- W1 verdict: PASS at the exact candidate SHA; no blocking findings. Four LOW findings are preserved in the raw response and are nonblocking.
- W1 scope limitation: the reviewer process could not find the source packet and manifest in its own environment. The trusted local source packet and blueprint were recovered after the review and their exact hashes are preserved; this does not retroactively claim reviewer access.
- Static QA and full 19-page visual QA are separate receipts bound to the same candidate SHA.
- Status remains CANDIDATE. This package does not assert formal acceptance or REAL evidence.

The full raw OpenCode stdout remains in the local runtime at the path recorded in the W1 terminal receipt; its SHA-256 is recorded there. The bounded final response is preserved byte-for-byte in `evidence/semantic/W1/W1_REVIEW_RESPONSE_R05.json`.
GitHub byte note: `PACKAGE_MANIFEST.json` hashes refer to exact raw Git blob bytes at the recorded readback ref. Windows Git `core.autocrlf=true` normalized text files from CRLF to LF during commit; the DOCX/PDF binaries were not transformed. Worker response and original source hashes in receipts describe their pre-commit source bytes; the package manifest records the stored GitHub copies.