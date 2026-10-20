# DOCX 0093 / I17D-E07 — R16 candidate audit package

**State: CANDIDATE.** This package is not formal TTQS acceptance, association approval, a real employer response, or executed survey evidence. Filled records are SAMPLE/SYNTHETIC; all 37 registered facts are listed in `changes/0093_R16_SYNTHETIC_REPLACEMENT_REGISTER.csv`.

## Identity and official mapping
- DOCX ID: `0093`
- Official requirement: `I17D-E07` — 學員訓後雇主問卷調查表
- Unique Blueprint row SHA-256: `482ca2a1ca32e3f6b84625ff8959bc19a97a2f78861bb8194f087716c366bf28`
- Blueprint source SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`
- Official evidence-table PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- Distinct neighbors: DOCX 0092 / I17D-E06; DOCX 0094 / I18-E01. Their sidecar mappings are included.

## Exact candidate and QA
- R16 DOCX: 79,800 bytes; SHA-256 `d12b256f2a0162749ff685235e90665a0d440a0f4c6365da00fbbe1c479707e5`.
- Source Markdown SHA-256: `65507d4d412713304a0214a9073953620218da3a1a341ae5815a337f544d8b6f`.
- Static QA: PASS, exact candidate SHA bound in `qa/0093_R16_STATIC_QA.json`.
- Microsoft Word native PDF export: 34 A4 pages; PDF SHA-256 `9d46f524f68d73a5b21a199328c8ae99c03e5e9b548c802394e75bab5a5eec54`.
- Layout: all page images compared against R15; only pages 7 and 34 changed and were inspected full resolution. Other pages inherit the R15 visual baseline; receipts and changed page images are included.
- Independent OpenCode v2 review: R15 reported PASS with three minor findings. R16 exact-SHA delta review reports PASS, closes the two corrected findings, and accepts the remaining ID-mapping point as sidecar traceability. This is not formal acceptance.

## R15 to R16 repairs
1. Page 7 clarifies the Q0 reason code may be selected or left blank and does not alter explicit Q0=2 exclusion.
2. Page 34 replaces a literal escaped newline with a separate checklist bullet.

No Word bytes were changed for metadata or receipt packaging. This package includes the R15 baseline, R16 DOCX/source, QA and layout receipts, reviewer original responses and bounded CLI outputs, focused source diff, official mapping, Word PDF/pages, and replacement register.

## Source provenance
At package preparation, existing PR #92 branch `work/ttqs-one-document-quality-contract-20261016` was at head `ae1f7dffb89f1218f20c9cf31ae87e4412abaf33`. Applicable command file `docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` blob SHA: `263aaca84891bba8dca087875804343c3670e921`.
