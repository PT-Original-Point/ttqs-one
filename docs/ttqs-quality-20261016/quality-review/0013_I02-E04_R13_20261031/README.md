# 0013 / I02-E04 — R13 candidate

Status: `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`. This artifact is not association-approved, formally accepted, or evidence of real publication.

## Provenance

- Requirement: I02-E04, public annual training-course listing evidence record.
- Unique Blueprint SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`.
- Unique Blueprint row SHA-256: `b529f3c13e964b6edbec124158d3559df988b401ce3b97fd1984e90b0582d35b`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Source packet `source_packet_R01.json` SHA-256: `b87440b249ec78c6bbe69ff001fe9d7dbb5060d65f27fe61d21ec48cdb5bfa63`.
- R12 source candidate SHA-256: `978672ae999bbcb1a71137739428ae6d37ce475b96eb59abc8d939d3cbcdc260`.
- R13 candidate DOCX SHA-256: `bf13360703574a7e310864135dcb667314387462678ab8db12d63a0fe79ae31d`.

## R13 scoped changes

- Corrected the visible revision label and version table from R11 to R13; set the draft date to 2026-10-31.
- Moved the unchanged closing paragraph of section 11.2 across the existing landscape-to-portrait section break so it flows before section 12. The near-empty landscape page was removed; no other package part changed.

## Verification

- DOCX package integrity and Python DOCX open: PASS.
- Package delta: only `word/document.xml` differs from R12; explicit body/table font minima remain 10.5/9.5 pt.
- Microsoft Word native export: 24 pages; PDF SHA-256 `937982bb2930257f901e5594236656605338cbdc2736cd6c1d9504e2c4f579d8`.
- All 24 rendered pages directly inspected at 120 dpi. The corrected page 17 now contains the section 11.2 conclusion and section 12 in portrait layout; no clipping or overlap was observed.
- SAMPLE arithmetic shown in the document: 4 courses × 9 required fields = 36; 35/36 rounds to 97.2%; 36/36 = 100%; four sample registration links remain unusable, so availability is 0/4 and release remains HOLD; planned hours total 30 and planned seats total 74.
- Independent semantic review of the exact R13 SHA: PENDING. Therefore this is not counted as a quality-accepted or formally accepted Word.

The R12 OpenCode review attempt ended with HTTP 429 and has no verdict; it is not a review of R13. Do not reuse it as R13 acceptance.
