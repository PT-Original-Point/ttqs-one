# 0122 R02 OpenCode exact-SHA review reconciliation

Observed 2026-11-01 10:02:37 +0000 (Asia/Taipei). This is an additive audit record; no DOCX bytes were changed.

## R02 result

- Official mapping: DOCX 0122 → I19-E10. Candidate SHA-256: `d3a6a1222d0389172dc6ab9737d06c5e46f4b45ed3a661324f3b885b751b7b86`; extracted body SHA-256: `61a732058927a033f268171084db05f3a86cac44fe9e92dd21a7a6f77fcb47ea`. The reviewer response echoes both hashes, and the local candidate/body were independently rehashed for this reconciliation.
- OpenCode v2 requested/observed session route: `opencode/glm-5.3-flash-free`; provider `opencode`; upstream serving identity and invoice are UNKNOWN. No fallback or tool call was recorded. CLI exit 0; 125.547 seconds; reported usage 27,578 input / 2,531 output / 20,556 reasoning tokens; reported cost 0 is not invoice-verified.
- Reviewer verdict: **PARTIAL** (one blocking, one nonblocking finding). The blocker states that R02 records all eight Wave-1 certification attempts on 2026-07-10, after the Wave-1 close on 2026-06-24; the 30-day Q12 pass/fail results therefore contradict the document's own timeline. The nonblocking finding is two escaped percent signs in the declaration.
- Review was text-only and did not inspect the Word binary, layout, pages, or real-world evidence. R02 is not semantically PASS and was not promoted.

## R03 remains a separate revision

- Current later candidate R03 SHA-256: `b55d498e0e3ea8a53c2b5d12a64958c40383f4a015c5f8211789e664762f2c2d`; body SHA-256: `a6f9b879203ab5234d6f5c918c7b3b7b5109c641a66bbbae3d72ebbb9b409991`. Its own OpenCode adjudication is `PASS_TEXT_ONLY_EXACT_SHA` with `0` blockers; its own technical receipt is `PASS_DETERMINISTIC_SCOPE; exact candidate SHA` and visual receipt is `PASS_VISUAL_DELTA_SCOPE; 28 pages, 25 pixel-identical baseline pages, 3 changed pages directly inspected`. The local adjudication records formal acceptance `NOT_GRANTED` and promotion `NOT_PROMOTED`.
- R02's PARTIAL verdict is historical and is not merged with R03's scoped evidence. R03's PASS does not retroactively change R02. The R03 candidate and its receipt hashes are listed in the local record; verify each against its own exact SHA.
- Both R02 and R03 candidate DOCX raw bytes were fetched from GitHub branch head `b09745e38c88966b3a5facf2f06d9fc1ce7f83f1` and matched their local SHA-256 exactly.

## Public evidence files

`REVIEWER_RESPONSE_R02.json` preserves the original reviewer response bytes exactly. `DISPATCH_TERMINAL_R02_PUBLIC.json` and `RAW_STDOUT_R02_REDACTED.jsonl` redact PID/session identifiers; originals remain in the local work package. `INPUT_MANIFEST_R02_PUBLIC.json` contains source, Blueprint, candidate, body, packet, route, and worker-output hashes without local absolute paths.

REAL evidence: not supplied. Human formal acceptance: not granted.
