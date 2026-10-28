# 0121 / I19-E09 — R04 candidate evidence

- Candidate DOCX SHA-256: `a80535a46b457404c8c1bf93404b124ce6d74c53f653cf0b3dfa128ec82c6e89`
- Independent OpenCode v2 semantic review: **PASS** on the exact candidate and body-extract SHA. The reviewer recorded one LOW and four INFO findings; these are disclosed and non-blocking for the reported PASS. Details and disposition are in `SEMANTIC_REVIEW_STATUS_R04.json`.
- Technical/layout QA: **34/34 PASS**. Microsoft Word native export: **24 pages**; post-exit process readback settled successfully. Manual visual inspection covered pages 1 and 16–24; pages 2–15 were pixel-identical to previously reviewed R03 renders.
- OpenCode session export reports `opencode/glm-5.3-flash-free`, cost 0, 39,372 input and 3,559 output tokens. This is CLI session metadata, not independent upstream provider attestation.
- R03 was preserved unchanged. This is a CANDIDATE only; formal association acceptance is `NOT_GRANTED`, real evidence remains `UNKNOWN/HOLD`, and official score is `NOT_ASSIGNED`.
- Sample distribution: 80 complete responses; rating counts 1–5 = 0, 0, 10, 47, 23; percentages = 0.00%, 0.00%, 12.50%, 58.75%, 28.75%. Partial P09 is excluded from the complete-case distribution.

The DOCX and PDF are directly openable artifacts. Receipts, original reviewer response, sanitized session metadata, and the exact review packet provide traceability.
