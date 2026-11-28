# 0123 OpenCode writer incident R01

- Work: TTQS_ONE DOCX 0123 / I19-E11, complete case-record manuscript.
- Client: OpenCode CLI v2.0.32, hidden noninteractive process.
- Requested route: opencode/deepseek-v4.1-flash-free (listed by local opencode models immediately before dispatch).
- Session: ses_e9345f1faffenEymkO9Z3ElSrj.
- Result: provider returned FreeUsageLimitError, HTTP 429, "Free usage limit reached". CLI exit 1; 681 bytes of JSONL; no manuscript text and no model token usage receipt. Actual served model is UNKNOWN because the provider rejected the request before a completion.
- Computer Use: not used. Model fallback: not authorized. No subscription or paid route enabled.
- Retry decision: do not resend this unchanged request until a free-quota reset/availability change is evidenced. This is a provider quota blocker for the attempted model request; it does not prove every OpenCode model or the entire document queue is blocked.
- Continued route: keep source packet and Blueprint ready; proceed with locally authored synthetic-only candidate content and deterministic/native Word construction. Independent semantic review remains separate and pending an available reviewer.