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
## Additional bounded OpenCode DeepSeek attempt — 2026-10-28T08:44:27.706033+08:00

A single hidden, noninteractive exact-SHA semantic review requested `opencode/deepseek-v4.1-flash-free` (OpenCode CLI v2.1.4; PID 77092) against the R04 packet. The provider returned `provider.free-limit`, HTTP 429, before model inference. No review response was produced; actual model identity was NOT REACHED and token usage was not returned. Provider retry estimate: `2026-10-29T07:59:59.706+08:00`. Candidate SHA-256 remains `de111911a549a0be0bd6381a6b22ed694881ba6b3f83528d2b4a4e153002142b` before and after; no DOCX rebuild or mutation occurred. The OpenCode free semantic-review lane remains blocked until fresh route availability; unrelated READY work remains eligible. Public session ID is redacted; the full local stdout/stderr and exact hashes remain in the local worker record.

## Current status reconciliation — 2026-10-29

This addendum supersedes the earlier `Independent semantic review: BLOCKED / NO REVIEW RESPONSE` and the associated next-action statement above. Those statements remain preserved as historical status at their recorded observation time.

- Candidate: DOCX 0141 / I19-E31 / Blueprint index 155; SHA-256 `de111911a549a0be0bd6381a6b22ed694881ba6b3f83528d2b4a4e153002142b`. Candidate bytes remain unchanged.
- Independent semantic review: PASS on the exact DOCX and extracted-text SHA. Scope covers the complete extracted text and the listed requirement mapping, genre/usability, SAMPLE/REAL boundary, mathematics, cross-document identity and negative-neighbor checks. The reviewer reported zero major and zero minor findings, and five residual limitations.
- Reviewer route: Antigravity CLI 1.4.9; requested and CLI-selected `gemini-3.8-flash-high`; exit code 0; no tool calls or file modifications reported. The provider did not attest the served model, so actual model identity remains UNKNOWN; this is not a provider-verified Gemini PASS.
- Existing technical QA and Word-native visual QA remain PASS for their recorded exact-SHA scopes. The review does not replace those scopes.
- Residual limitations remain: printed checkbox serial UNKNOWN; real-data retention/privacy authority and responsible custodian UNKNOWN/HOLD; synthetic Q8 contains no real qualitative responses; Human formal acceptance NOT_GRANTED and official score NOT_ASSIGNED. Real personal data must not be collected without association authorization and applicable policy.
- Candidate state remains CANDIDATE_ONLY. No DOCX rebuild, Human acceptance, real evidence, or formal score is claimed. Do not repeat a same-SHA review solely to update this status; continue the next READY requirement.

Current source evidence at PR #92 HEAD `0b3382f2a03cc709ea6020ef2a32af3fa2f750d3`: `worker_ANTIGRAVITY_R04_GEMINI_HIGH_R01_20261029/PUBLIC_REVIEW_RECEIPT.json` (Git blob `0895e9691d1872d8df46c86b3f3147102cbd18b9`, reviewer response SHA-256 `eba62f86e35c576704b124cdc742f4bf56ce2ce08f9ceb3b057abcbd501b059a`); `QUALITY_STATUS_DELTA.json` (Git blob `f69eca75cc98b5a7f53e415e3a4bbf13196e8f17`).