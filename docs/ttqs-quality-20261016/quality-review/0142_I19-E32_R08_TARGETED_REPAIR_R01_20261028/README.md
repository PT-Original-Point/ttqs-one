# 0142 / I19-E32 — R08 targeted repair candidate

- State: CANDIDATE only. Formal acceptance: NOT GRANTED. REAL evidence: UNKNOWN/HOLD. Official score: NOT ASSIGNED.
- Exact candidate DOCX SHA-256: `7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78`.
- Parent R07-LF01 candidate SHA-256: `ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f`.
- Mapping: internal document 0142, official requirement I19-E32, unique Blueprint and official row/crosswalk included; official source is PDF page 9/9. R01 DOCX bytes are now recovered and SHA-256 matched to the historical R01 hash; the actual build date remains UNKNOWN.
- Targeted changes: lineage/version labels; Table 12 role and REAL accounting-basis clarity; dated SAMPLE recalculation; REAL hold criteria; separate REAL-copy instructions; and replacement-register locator/date fields.
- Technical QA: PASS on the exact candidate SHA. Word-native export: 14 pages. Visual QA: PASS, 14/14 page images inspected.
- Independent semantic review R02: `PASS_TEXT_ONLY_EXACT_SHA`, bound to the same candidate SHA. OpenCode v2 CLI session `ses_e7eb7fa15ffeNy82oKA48J6mC8` reports actual model `opencode/glm-5.3-flash-free`; exit 0; 92.813 s; no tool events, no Computer Use, and no fallback observed in the captured session. Session-reported cost was 0; account billing was not independently verified.
- Review scope includes candidate body plus official requirement, source packet, unique Blueprint, SAMPLE replacement register, and lineage records. The semantic reviewer did not inspect rendered pages; the separate 14/14 visual QA receipt covers layout. Review response SHA-256: `65341f80ac0a6205e33d6da74f834db6d1b7bd6fbd5a8ea3362681509533d271`.
- Remaining limitation: R01 bytes and recorded hash are verified; its historical build date remains UNKNOWN, so lineage chronology is partial. R08 remains unchanged and is not rebuilt. The earlier DeepSeek HTTP 429 and Antigravity model-identity-UNKNOWN responses remain preserved as historical attempts.
- Current-head raw-byte recheck for the 13-file R02 review bundle: see `evidence/GITHUB_RAW_READBACK_R02_CURRENT_HEAD.json`. This receipt records the pre-status-update branch HEAD; post-sync readback is separately verified after the status correction is pushed.

Next: preserve the exact DOCX SHA, continue only any independently READY document stage, and keep formal acceptance and REAL evidence as HUMAN/REAL gates.
- R01 byte-reconciliation receipt: evidence/R01_BASELINE_BYTES_RECONCILIATION_20261029.json; it confirms 44,970 bytes and SHA-256 match without changing or re-reviewing R08.
