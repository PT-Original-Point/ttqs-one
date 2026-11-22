# 0027 / I05-E01 — R02 candidate evidence

Status: **CANDIDATE**. This package does not claim formal acceptance.

- Candidate DOCX: `0027_I05-E01_CANDIDATE_R02.docx`
- Candidate SHA-256: `A9321C8E5D90DCD19B150B97358A325B93C644308775006283F68DEDF598D62D`
- Candidate size: 77,165 bytes
- Deterministic technical QA: PASS, exact SHA; 24 pages, 26 tables; body minimum 11.5 pt, table minimum 9.5 pt; synthetic register 95/95 unique and populated; budget calculations and LaTeX-residue checks PASS.
- Full-page visual QA: PASS, all 24 pages across six contact sheets; pages 1 and 23 additionally inspected full size; no findings.
- Independent W2 semantic/usability review: PASS on the same candidate and extracted-text SHA. Two ADVISORY findings are retained in the raw receipt; zero blocking findings. They do not trigger a rewrite.
- W2 request: Antigravity CLI 1.5.12, requested `gemini-3.8-flash-high`; provider-served model remains UNKNOWN. Native terminal receipt records PID, exit 0, response hashes and zero tool calls.
- The previous W2 R01 pipe failure and UNKNOWN submission state are retained separately. R02 used a changed, previously successful `stream-json` stdin transport.
- Source-lineage reconciliation: the candidate's embedded SOURCE_PACKET and UNIQUE_BLUEPRINT SHA-256 values match the exact GitHub raw bytes at the readback ref (1,625 and 3,591 bytes); recomputed Git blob SHA-1 values also match. The earlier mismatch came from CRLF serialization in the local working copy; LF-normalized bytes match the candidate identifiers. See the supplemental reconciliation receipt.

## GitHub exact raw-byte readback

- Status: PASS_RAW_BYTE_READBACK at immutable PR branch commit 5addbce1a417ebdfd16dbb7ad45af2fe7a8965bb.
- DOCX bytes: 77165; SHA-256: A9321C8E5D90DCD19B150B97358A325B93C644308775006283F68DEDF598D62D; Git blob SHA-1: 6fa32ac25dce95fb6cb568aea38ab096be1c7269.
- Receipt: docs/ttqs-quality-20261016/quality-review/0027_R122_WORKER_DELIVERY_20261119/R02_candidate/qa/GITHUB_RAW_BYTE_READBACK_20261122.json.
- Exact-SHA technical, all-24-page visual, and independent W2 semantic PASS receipts are unchanged. Candidate remains CANDIDATE; formal acceptance is NOT_GRANTED and REAL evidence is NOT_ESTABLISHED.
- Source-lineage status: `SOURCE_LINEAGE_RAW_HASH_RECONCILED` by GitHub raw-byte and Git blob readback; the earlier local CRLF receipt remains unchanged as historical evidence.
