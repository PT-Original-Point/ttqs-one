# 0142 / I19-E32 — R08 candidate status

- Candidate SHA-256: $candidate
- Status: CANDIDATE; formal acceptance NOT GRANTED; REAL evidence UNKNOWN/HOLD.
- Deterministic technical QA: PASS; native Word render: PASS; 14/14 rendered pages visually inspected: PASS.
- Independent semantic review: BLOCKED. One exact-SHA OpenCode v2 attempt used opencode/deepseek-v4.1-flash-free; native session returned provider FreeUsageLimitError HTTP 429 after reporting 39,599 input / 0 output / 32,000 reasoning tokens. No review text was returned; CLI exit code is UNKNOWN. OpenCode reported cost 0, which is not an account invoice.
- No fallback model, Computer Use, or paid provider was used. Do not infer that other free endpoints are currently available from a model catalog.
- Provider retry-after: 71,252,000 ms. The same model/input is not to be retried before that window; the current candidate remains unaccepted pending an authorized, actually usable independent reviewer route.
- This reviewer failure does not invalidate the DOCX technical or visual receipts and does not block other independent READY document work.
