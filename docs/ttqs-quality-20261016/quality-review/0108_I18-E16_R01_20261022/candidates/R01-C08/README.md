# 0108 / I18-E16 — R01-C08 synthetic candidate

**State: CANDIDATE / VISUAL_FAIL (R11 full-page inspection). Formal acceptance: NOT GRANTED. REAL payroll evidence: UNKNOWN / NOT PROVIDED.** This package contains synthetic demonstration data only. It does not establish that the association delivered a course, employed anyone, raised salaries, or approved the sample.

## Official mapping and sources

- Document ID: `0108`; official requirement: `I18-E16`, “提高薪資紀錄”, evidence table page 7. Blueprint registry index 117 is an internal project index, not an official checkbox serial.
- Source packet SHA-256: `f11df2f92edb7c63bc7dbddefe8461188dfdf90c4be9e0c0c4ae284f15457d5f`.
- Unique Blueprint SHA-256: `41713064e2744c12831cb56098cc3ceb5661279048eb16123583f6c26d2f64ab`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Source-stage commit on PR #92 branch before this candidate publication: `75d8f79679e3b3df2a88555e78637404674ff018`. Current §6 contract blob read in this run: `4c7eff55748ff265b1e5a7d1122852b0d101acbd`.

## Candidate and verification

- Markdown SHA-256: `f4bf23b791726256348d3223c6c204d8b88e5a542855b12b2e04c51f3b48179c`.
- DOCX SHA-256: `e4c5b662384d84f6c11d0a1d69860935992216437088febfb791e767075d7f4f` (71,535 bytes).
- Technical OOXML/content QA: PASS; 357 paragraphs, 85 tables, body minimum 10.5 pt, table minimum 9.5 pt; ZIP/structural and internal metadata scans recorded in the receipt.
- OpenCode v2 independent semantic delta review: PASS, text-only, bound to the exact Markdown/DOCX hashes above. It closed C07 findings M1–M3. Reviewer did not inspect DOCX binary, PDF, or page images.
- Historical R09 export attempt: BLOCKED_TIMEOUT after 9.8 minutes. That attempt created no PDF; its owned Word/export processes were stopped, while pre-existing PID 15600 was preserved. This historical failure is retained.
- R11 bounded export: SUCCESS using a newly owned hidden Word COM instance (PID 68868), read-only, without an explicit `Repaginate` call. It produced a 38-page PDF; SHA-256 `b4c8af9d847f3369fabaacdc91a553e99d36eb770f977262f9dfb0d9758de7ea`.
- R11 visual inspection: FAIL on the unchanged DOCX SHA above. All 38 full-page images were inspected. Major findings: Table 2 / SYN-P01 continues from page 6 to page 7 without a repeated header or record identifier; the Table 5 caption is stranded at the bottom of page 11 while its body starts on page 12. Moderate findings: Table 1 / SYN-P03 continues across pages 4–5 without a repeated header; the Section 6 evidence-control table continues from page 12 to page 13 without a repeated header.
- The visual receipt lists all 38 page-image SHA-256 values. The PDF and receipt are stored under `visual/R01-C08_R11/`; selected pages 4–7, 11–13, and 15–16 are included for direct audit. The DOCX bytes were not modified.
- The semantic review remains PASS only for its original text-only scope; the reviewer explicitly did not inspect the DOCX/PDF/images. It is not a visual PASS. Provider-side model serving and billing remain UNKNOWN.

## CLI work and limits

The attached ledger reconciles the available 0108 OpenCode v2 sessions and the two captured failed invocations, with session token counts and saved returns. Session DB local cost is 0.0; provider billing and serving-side model identity remain UNKNOWN. The requested free model is recorded as `opencode/deepseek-v4.1-flash-free`; the session metadata reports that model, but does not prove provider-side serving or billing. The 24-hour TTQS SQLite window records 50 sessions / 48 with activity overall, not 50 CLI launches. Exact repository-wide CLI invocation counts and Antigravity attempts remain UNKNOWN because the OS invocation audit is incomplete.

The C08 DOCX and Markdown are the adopted candidate artifacts. Writer output was returned in three native OpenCode assistant segments, then formatted and locally corrected against review findings. The C08 delta reviewer found no remaining M1–M3 text defect. No real payroll records were available.

## Next action

Repair only the documented table-pagination defects in a new candidate revision. Keep the R01-C08 DOCX and its FAIL receipt as immutable history; do not relabel it. After a layout-only repair, rerun technical QA and hidden native Word export, inspect every page, and obtain an exact-final-SHA semantic receipt. Formal acceptance remains a Human Gate.
