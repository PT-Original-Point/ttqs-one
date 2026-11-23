# 0142 / I19-E32 — R08 semantic review and scope adjudication

- Candidate DOCX SHA-256: `7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78` (unchanged).
- Antigravity CLI was explicitly called with requested model `gemini-3.8-flash-high`; native output did not expose the served model ID, so actual model identity is **UNKNOWN**. Do not call this a verified Gemini-model PASS.
- CLI exit: 0; elapsed: 49.344 s; reported usage: input 19,022 / output 7,157 / thinking 5,073 / total 26,179. Cost/account billing: UNKNOWN. No Computer Use or fallback was requested/used.
- Raw response verdict: `PASS`, bound to the exact candidate SHA. Raw output SHA-256: `f47a82834d2e41d8cb39dccf671971b63361447ae0fe48de20dd0c8c6107dd2c`.
- Codex scope adjudication: **PARTIAL; not promotable**. The reviewer was explicitly given text only, not the lineage annex/JSON or the companion CSV. Its F1 “RESOLVED” and register-wide assertions therefore exceed the supplied evidence scope.
- Local follow-up: the 19-row CSV and F15 locator were verified; the lineage annex now contains a per-stage inventory with local hashes/byte counts and mtime explicitly distinguished from build date. The R01 original DOCX bytes and build date remain UNKNOWN, so F1 stays PARTIAL.
- F2–F6 are supported by the body and, where applicable, local register rows; they are not promoted as an independent clean PASS because the review request omitted companion artifacts.
- Existing technical QA remains PASS on the exact SHA. Existing Word-native visual receipt remains 14/14 pages PASS; this reviewer did not perform visual inspection.
- Candidate remains CANDIDATE, formal acceptance NOT_GRANTED, REAL UNKNOWN/HOLD, official score NOT_ASSIGNED. No DOCX bytes changed.
