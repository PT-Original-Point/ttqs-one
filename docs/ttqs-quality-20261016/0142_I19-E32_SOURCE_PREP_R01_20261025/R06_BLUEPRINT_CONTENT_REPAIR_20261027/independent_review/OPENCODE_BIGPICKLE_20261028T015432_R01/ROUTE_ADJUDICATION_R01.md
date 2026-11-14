# 0142 R06 OpenCode Big Pickle route adjudication

- Work: `TTQS-0142-I19-E32-R06-W1-OPENCODE-BIG-PICKLE-FREE-EXACT-SHA-SEMANTIC-REVIEW-20261028T015432`
- Local window: 2026-10-28 01:54:32–01:54:42 (Asia/Taipei); CLI PID 79844; OpenCode V2 2.1.4; hidden, noninteractive.
- Requested model: `opencode/big-pickle` (no fallback allowed, no auto-approval, no Computer Use).
- Candidate DOCX SHA-256 before/after: `3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e` (unchanged).
- Result: CLI exit 1; provider returned `provider.free-limit`, HTTP 429, “Free usage limit reached”; no inference reached, no reviewer response, no provider-reported tokens, no observed tool calls. Billing/account ledger remains UNKNOWN.
- Provider `retryAfterMs=21925000`; local retry estimate from the recorded start time is 2026-10-28T07:59:57.0000000+08:00.
- The prior GLM 5.3 Flash Free attempt for this same candidate also received a pre-inference HTTP 429 with retry estimate about 08:00 TPE. This supports a free-usage-limit block across these two requests, but does not by itself prove the quota’s account/model scope.
- The OpenCode status page showed the hosted/free inference service operational during this turn. Its measurement notes exclude requests rejected for account balance, budget, or usage limits from service failure metrics. Thus service health does not contradict this local account/request rejection.
- The official model page lists Big Pickle as Free and notes that data sent during its free period may be used to improve the model. The supplied review packet contains only the synthetic candidate example and source excerpts; no REAL financial originals or personal records were submitted.
- No retry of this same request is authorized before the returned retry time. At/after that time, recheck route state and retry only if a material provider/account change is confirmed; otherwise continue another READY lane.
- Semantic status remains `PENDING_INDEPENDENT_EXACT_SHA_REVIEW`; no PASS is inferred.
