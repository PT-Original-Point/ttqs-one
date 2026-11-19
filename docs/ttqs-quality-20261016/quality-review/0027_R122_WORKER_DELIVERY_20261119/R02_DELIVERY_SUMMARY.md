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
- Source-lineage caveat: deterministic QA records `CONTENT_READBACK_PASS_WITH_LEGACY_RAW_HASH_MISMATCH`; content readback is documented, but the legacy raw-hash chain is not certified.

Remote synchronization and raw-byte readback are recorded separately after the GitHub write; no remote delivery is claimed by this local README.
