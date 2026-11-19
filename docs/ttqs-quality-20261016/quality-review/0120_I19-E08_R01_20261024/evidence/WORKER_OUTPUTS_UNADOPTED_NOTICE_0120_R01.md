# 0120 R01 worker outputs — unadopted audit records

The files in `worker/raw_unadopted/` preserve the original CLI replies and execution envelopes for audit. They are not source facts, not association records, and not the accepted text of the DOCX.

- OpenCode CLI v2.0.32 was asked for `opencode/glm-5.3-flash-free`; its raw stdout is a 430-byte HTTP 429 `FreeUsageLimitError`. It produced no manuscript. The exit code and actual model identity were not captured.
- Antigravity CLI was requested to use `gemini-3.8-flash-high`, but actual model identity remains UNKNOWN. The first invocation ended when stdin closed. A later first-part response was incomplete and used the wrong document genre/title and incorrect neighboring requirement mapping. The second-part wrapper returned exit 0, while the raw response status was ERROR / stream interrupted. Neither part was adopted. No complete multi-part manuscript or DOCX came from Antigravity.
- The current candidate was assembled locally from the official source mapping, the dedicated I19-E08 Blueprint and explicitly synthetic data. Worker prose was not copied into the candidate.
- The raw outputs are included here only so auditors can inspect what happened. Do not cite them as TTQS evidence or as proof that Gemini was the actual model.
