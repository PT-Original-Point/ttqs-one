# TTQS ONE candidate evidence — DOCX 0129 / I19-E18 / R03

- State: **CANDIDATE**. Formal TTQS acceptance is **NOT GRANTED**.
- Candidate DOCX SHA-256: `73c856a6c31b9997e084b443f30bb0eadb1763320d2c7818626e40d431fc848a` (61,464 bytes).
- Official requirement: I19-E18 operating performance (financial dimension); this candidate demonstrates the cost-control sub-area. Adjacent internal crosswalk rows I19-E17→0128 and I19-E19→0130 are included to prevent document-ID confusion.
- Technical/static and independently recalculated sample arithmetic: **PASS_STATIC_AND_MATH_ONLY**. This confirms OOXML integrity, 8 tables, 9 sections, 10.5pt body and 9.5pt table explicit minimums, and recomputation of the 160 SAMPLE rows.
- Independent reviewer: **PASS_TEXT_ONLY** for the exact DOCX SHA above; fresh Antigravity CLI conversation, requested model `gemini-3.8-flash-high`, actual serving model **UNKNOWN**. The raw CLI envelope, exact response and dispatch receipt are retained. Review token counters are provider-reported usage, not an invoice.
- Visual QA: **PASS_VISUAL_QA (20/20 pages)**. Word 16.0 ExportAsFixedFormat produced a 20-page PDF; the exact-SHA visual receipt and PDF are included. No clipping, overlap, missing glyphs, or unreadable tables were observed. Pages 5, 7, 12, and 13 contain intentional transition/form whitespace; no reflow repair was made. The earlier R02/R03 timeout records remain as historical failures; the current export-pass receipt supersedes their blocked status for this unchanged DOCX.
- Visual QA receipt SHA-256: $visHash; Word-native PDF SHA-256: $pdfHash. DOCX remains $((Get-FileHash -Algorithm SHA256 (Join-Path E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0129_I19-E18_SOURCE_PREP_R01_20261024\candidate_R03\github_sync_public 'candidate\0129_I19-E18_R03.docx')).Hash.ToLowerInvariant()).
- REAL association records and performance remain **UNKNOWN_UNTIL_SOURCE**. All supplied data are `SAMPLE/SYNTHETIC`; no approval, signature, execution record, or third-party evidence is represented.
- The final R03 manuscript differs from R01C only by the visible revision-label line. The DOCX was not changed after the independent review.

## Selected exact evidence

- Official PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; official page-8 extract is included.
- Unique Blueprint SHA-256: `c86b2e79c4953a0d12eda4fa0264325ffa0e073016522601ca9c6457c8988046`.
- Source packet SHA-256: `5d6ef2b80872a3ac80c8e72c43d51f2002c138cdf9e8025cf36061dcad9f3e72`.
- Official-to-internal crosswalk source SHA-256: `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`; included excerpt is explicitly internal mapping, not an official checkbox serial.
- Sample math: pre 55/80 = 68.75%, post 66/80 = 82.5%; workdays 400→265; assumed rework consumables NT$200→112; S-B03 adverse first-pass 5/10→4/10 retained. The NT$8/case is a SAMPLE assumption, not actual association cost.
- Reviewer response SHA-256: `132a5735562029662c425c115667df7bdd371370b5b8f4a487a513a3172f10e6`; reviewer raw stdout SHA-256: `db2b51b17ebc38264039fb11c3063b420cfd31eadb63f5767c242da60df2ec94`.
- The package manifest lists SHA-256 for every artifact listed inside it, including this README; the manifest excludes its own hash to avoid recursion. Public copies of receipts remove absolute local paths while preserving the original local receipt hash; raw worker/reviewer output is included where applicable.
