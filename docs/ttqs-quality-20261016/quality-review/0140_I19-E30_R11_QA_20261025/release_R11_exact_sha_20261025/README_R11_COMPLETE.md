# DOCX 0140 / I19-E30 / R11 — candidate evidence package

**State:** CANDIDATE only. Formal acceptance is NOT_GRANTED. REAL association data is UNKNOWN/HOLD. Every learner record, role, system-use rate and task result in this package is SAMPLE/SYNTHETIC.

## Identity and exact candidate

- DOCX ID: 0140; official requirement: I19-E30; project registry index: 154; printed checkbox serial: UNKNOWN.
- Unique Blueprint R01 and official page 9 excerpt are included under `source/`.
- Candidate DOCX SHA-256: `5860d73916e94c221a8cdba6ba39bab7236c1af65be5f569448c06ecdcd6b86d` (127,801 bytes).
- Parent R10 SHA-256: `de9525e42a391d0ed002d23d54d5a9b9c1e042f7c194b71f00b61bd98ff48c16`.
- Word-native 29-page PDF SHA-256: `ed2b1cb66440eb5f4db83023d794587467c8836197fed4ca686fc86de49bc5bc`.

## R11 quality results

- Deterministic technical/content QA: PASS, exact R11 SHA. It checks 80 synthetic user-year rows, 82 replacement-register rows, cross-document math, embedded chart, typography and preservation of unchanged sections.
- Word-native visual QA: PASS_WITH_NONBLOCKING_LAYOUT_NOTE on 29 pages. No clipping, overlap, truncated text or table overflow; pages 6, 10 and 14 have unused whitespace but remain readable. The 29 rendered page images and the Word PDF are included.
- Semantic review: PASS for the R11 text/table delta only. Unchanged content inherits the full semantic PASS attached to R10's exact parent SHA; no claim of a fresh full-body R11 semantic review. Reviewer response and parent R10 candidate/receipt are included. Actual serving-model identity is UNKNOWN.
- F4 chart/data reconciliation: PASS. On exact Word-rendered page 9, the displayed labels match the source dataset and period summary: 2023 adoption 12/20=60.00%, complete 9/20=45.00%; 2024 22/28=78.57%, 18/28=64.29%; 2025 28/32=87.50%, 25/32=78.13%. The chart shows the blue adoption series and orange eligible-user completion series, with SAMPLE/SYNTHETIC labeling.
- The first local chart checker emitted a false FAIL due to its own percent-string/page-field comparison bugs; the candidate did not change. The original failed receipt and correction diagnosis are preserved alongside the corrected PASS receipt.

## Worker and route evidence

- Antigravity CLI requested `gemini-3.8-flash-high`; one bounded text-only delta review returned PASS after two pre-model CLI parse failures. Actual backend/model identity and fallback identity remain UNKNOWN; no Gemini identity PASS is claimed. No Computer Use or file-writing tools were requested.
- OpenCode v2 reviewer returned the provider's free-limit 429 with no review response; it was not used to claim PASS and was not retried.

## Scope and hold conditions

This package does not prove actual association system usage, real users, records, approvals or performance. Replace synthetic fields only with authorized originals, retain sensitive records in their authorized source, and keep unverifiable evidence on HOLD. This candidate has not received Human formal acceptance or an official TTQS score.
