# DOCX 0141 R04 candidate status

Observed locally: 2026-10-27T21:44:14+08:00

## Identity and evidence state

- doc_id=0141; official requirement I19-E31; 157-item Blueprint index 155; printed checkbox serial UNKNOWN.
- Candidate DOCX SHA-256: de111911a549a0be0bd6381a6b22ed694881ba6b3f83528d2b4a4e153002142b.
- Candidate state: CANDIDATE; Human formal acceptance: NOT_GRANTED.
- All included response data and worked examples are SAMPLE/SYNTHETIC; real association data and execution evidence remain UNKNOWN/HOLD.

## Verified changes

- R04 makes one targeted pagination change from R03: adds pageBreakBefore to synthetic row SYN-0141-2025-010; the patch receipt states word/document.xml is the only changed package part and visible text is unchanged.
- Native Microsoft Word rendered 28 pages without modifying the DOCX. The full page manifest hashes all 28 rendered pages; pages 23-24 were directly inspected and the other 26 raster hashes match R03. Page 23 has rows 006-009; page 24 has rows 010-012.
- Deterministic R04 QA: PASS. It checks DOCX integrity/structure, source and Blueprint hashes, SAMPLE/REAL boundary, 36 CSV records, 44 replacement-register rows, row-level traceability, appendix-to-CSV equality, recomputed yearly aggregates, Q2 strict >75% threshold, Q5 descriptive-only threshold, body font floor 10.5 pt and table floor 9.5 pt.
- Visual/layout QA: PASS for the stated scope.
- Independent semantic review: BLOCKED / NO REVIEW RESPONSE. No semantic PASS is claimed.

## Reviewer route evidence

- OpenCode v2.1.4, model opencode/glm-5.3-flash-free, was explicitly requested for one hidden, noninteractive, read-only run on the R04 packet. It exited 1 with provider free-limit HTTP 429, no review response, no model identity and token usage UNKNOWN. Raw stdout/stderr and process receipt are included.
- The earlier R03 DeepSeek free-limit 429 and Antigravity R03 attempts are preserved in the raw route archive. Antigravity had three CLI argument failures followed by an empty response and a headless RunCommand permission denial. Actual served model remained UNKNOWN; Computer Use and dangerous permission bypass were not used. That review lane remains paused.
- The current GLM retry interval ends at 2026-10-28T08:00:00.379+08:00. Do not retry before fresh route availability evidence.

## Authority and remaining work

Official source, unique Blueprint, neighbor crosswalk, R02 source packet, synthetic data, manuscript and exact-SHA QA are included in the package. Next legal action is a fresh, bounded exact-SHA semantic review only after an available permitted reviewer route is evidenced; otherwise keep this document waiting for semantic QA and continue unrelated READY work. No production submission or real-world acceptance is implied.
## Additional bounded OpenCode Mimo attempt — 2026-10-27 22:07 TPE

A single hidden, noninteractive exact-SHA review was requested from `opencode/mimo-v2.6-flash-free` under a deny-all-tools project configuration. The provider returned HTTP 429 `provider.free-limit` before inference. No semantic response or token usage was produced; actual model is UNKNOWN. Retry estimate: `2026-10-28T07:59:59.875000+08:00`. The R04 DOCX remained SHA-256 `de111911a549a0be0bd6381a6b22ed694881ba6b3f83528d2b4a4e153002142b` and was not modified. This does not prove every OpenCode model is unavailable; it blocks this free-model review route until fresh availability evidence. See `R04_SEMANTIC_REVIEW_ROUTE_DISPOSITION_R02_20261027.json` and the preserved worker receipt folder.
