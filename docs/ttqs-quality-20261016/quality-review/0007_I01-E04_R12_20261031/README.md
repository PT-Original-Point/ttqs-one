# 0007 / I01-E04 — R12 candidate evidence

- Official requirement / checkbox: `I01-E04`; document ID: `0007`.
- Unique Blueprint row SHA-256: `4f7f55577ae42d0988e02e2112d73514dda173cb6232690a95d2149ac1851980`.
- Candidate DOCX SHA-256: `7e7509a2687396c4fa32a5bd8d8bf89691d8fb250026c96067eed74173f67f76`.
- Deterministic technical/content checks: PASS within the recorded receipt scope.
- Word render: 11-page PDF and page-image evidence included.
- Visual QA: PASS within scope. Pages 1 and 11 directly inspected; pages 2–10 inherited from R11 only because their page-image hashes matched. The semantic reviewer did not re-inspect pages.
- Independent semantic review: PASS by a separate Codex subagent context, bound to the exact candidate SHA. The original review response and receipt are included. OpenCode's separate attempt received HTTP 429 and produced no review; its public sanitized terminal receipt is in `evidence/W1_OPENCODE_429_TERMINAL_PUBLIC_R01.json`, and it is not counted as a review.
- Synthetic boundary: all 147 registered example facts are `SAMPLE_SYNTHETIC_ONLY`. No association approval, real execution, or third-party evidence is asserted.
- Status: quality candidate evidence; `FORMAL_ACCEPTANCE=NOT_GRANTED`, `REAL_EVIDENCE=NOT_ASSERTED`.

See `inputs/SOURCE_PACKET_0007_I01-E04_R12.json`, the replacement register, and each receipt for exact source and evidence hashes.