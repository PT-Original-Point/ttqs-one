# TTQS ONE 0141 C1.2 — exact-SHA evidence reconciliation and OpenCode 429

- Project / work: TTQS_ONE / TTQS-0141-I19-E31-R07-C1-2-OPENCODE-DELTA-20261028-R01
- Official binding: DOCX 0141 = I19-E31; 157-item index 155; printed checkbox serial UNKNOWN.
- PR branch HEAD read before this record: 3e5b5d0cc5ffe8bd82e30a91f87ebe13ec0bdd2e
- R12 command source blob: 63f26f0708249b211611d51b34a7fb90b4cd26a9
- Candidate state: CANDIDATE; formal acceptance NOT_GRANTED; REAL evidence UNKNOWN/HOLD; official score NOT_ASSIGNED.
- Candidate DOCX SHA-256: b40ea2f5b5c5467cdc31c2e5b1595ac8de4d679b7f4763aa00860727f5d3f1a0 (164,838 bytes). Local candidate matched the GitHub branch object before and after the attempted review; no DOCX bytes changed.
- Current candidate Git blob SHA-1: ba350f5bf8ce2093f533b626162478ef2607b655. Do not confuse this Git blob SHA-1 with the file SHA-256 above.

## Reconciled existing exact-SHA QA

The current PR contains an independent full-body semantic review bound to the same candidate SHA, covering extracted paragraphs P1–P233 and tables 1–18. Reviewer verdict: PASS; findings: none; extraction SHA-256 8410743cf1525aa5a2fd8ddf19b7b1439da4c2f502319a2fb87acd11d19390fa. Current GitHub objects: semantic review blob 0c320d13412808830635d795fda2742bec6a4f3c; adjudication blob bcaa4e7dfefee09d41bccc9f4f371b1df70f8964; public receipt blob 5b23ed156dd59eddf334a64e54313bd2af468cdc.

This corrects the older R11 stage receipt's statement that no fresh C1.2 full-body review was run: the R01 full-body W2 review exists at the current branch and is exact-SHA bound. The review requested gemini-3.8-flash-high and returned PASS, but the serving/backend model identity is UNKNOWN. Therefore this is exact-SHA semantic PASS evidence with a model-provenance limitation; it is not a Gemini-verified PASS and does not grant formal acceptance.

Technical QA is PASS on the same candidate SHA (receipt SHA-256 104662cfc195156b7e6c758170f7059e6b8b7a955c07128a9d8cae6a964835fe). Word-native rendering exported a 26-page PDF (SHA-256 42cb62c989a5b807bf8090f3bab82ab03359f2265aa01cfc6231e19ba3f9c022); all 26 pages were visually inspected. Result: PASS_WITH_NONBLOCKING_LAYOUT_NOTE (receipt SHA-256 57aabcc665da47b600da1d69d06c0adb1a15b72b7c1b0bff29f6c4fca0b17ca8).

## OpenCode v2 dispatch attempt

- CLI: OpenCode v2.1.4, hidden noninteractive process; PID 49684; session ses_e7dfd55a9ffeMy2TLOiVoumywN.
- Requested model: opencode/glm-5.3-flash-free; this ID was present in the local OpenCode model catalog. No alternate model or fallback was requested; --auto was not used.
- Start/end: 2026-10-28 18:16:14.822 +08:00 / 2026-10-28 18:16:16.323 +08:00; exit code 1.
- Provider terminal error: provider.free-limit HTTP 429, message Free usage limit reached; server retryAfterMs=51510000. Approximate retry-after time computed from the server timestamp: 2026-10-29T08:34:46.286+08:00 (Taipei time).
- No review response or adoptable content was returned. Actual serving model identity: UNKNOWN. Token/billing usage: UNKNOWN. Computer Use: NOT_USED; permission bypass: false; automatic approval: false.
- Raw stdout SHA-256: 5ad70325b0e38e905d039a7db6c670704d53d93f57d27dda699561b7791ee6c4 (528 bytes). Raw stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (0 bytes). Raw provider event follows.

{
  "type": "error",
  "timestamp": 1793182576286,
  "sessionID": "ses_e7dfd55a9ffeMy2TLOiVoumywN",
  "error": {
    "type": "provider.free-limit",
    "message": "Free usage limit reached. Connect a provider or subscribe to OpenCode Go to keep going, or switch models.",
    "status": 429,
    "response": {
      "body": "{\"type\":\"error\",\"error\":{\"type\":\"FreeUsageLimitError\",\"message\":\"Free usage limit reached. Free models work in OpenCode (https://opencode.ai); subscribe to OpenCode Go to keep going: https://opencode.ai/go\"}}"
    },
    "retryAfterMs": 51510000
  }
}

## Routing disposition

The exact GLM free-model route is BLOCKED until the server retry-after time or new positive availability evidence. This one 429 does not prove every OpenCode free model is unavailable. No identical retry was made; other model IDs remain UNKNOWN. Keep the candidate's existing exact-SHA reviews and visual QA; do not rebuild or repeat the full-body review. Formal acceptance remains NOT_GRANTED.
