# 0011 / I02-E02 — R09 candidate package

## Status

This is a **CANDIDATE / SAMPLE-SYNTHETIC draft**, not a formally approved association policy, not an actual product-market decision, and not evidence that any course or service was delivered. The package does not fabricate an approval, signature, real learner, or third-party source. Independent semantic review is **PENDING** because the OpenCode route is in a documented HTTP 429 cooldown; formal acceptance remains **UNKNOWN**.

## Requirement and sources

- `doc_id`: 0011
- Official requirement: `I02-E02` — 「與訓練政策有關之訓練產品與市場定位。」
- Official checklist PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` (page 1, exact text match)
- Unique Blueprint file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`
- Unique Blueprint raw-row SHA-256: `115b34f20b7f8106f5aa45d06da39ecae99a85a75f5276b79970911b428b32ec`; exact row included in `source/blueprint_unique_row.jsonl`.

## Artifact and QA

- Candidate DOCX: `candidate/0011_I02-E02_R09.docx`
- DOCX SHA-256: `b2e96abedac44af5ad343eaa4576d5819ee8e7373145f65d5a7258274481e2c9`
- Technical QA: `evidence/technical_qa_R09.json` — technical checks pass: OOXML ZIP integrity; Word/Python DOCX open; 27 tables, 988 cells, no empty cells; body minimum 10.5 pt and table minimum 9.5 pt; F001–F083 present; recomputed 5+4+3=12, ratios 75.0/66.7/58.3%, weights 100%, weighted scores 68/86/76, and 240-minute course total. This is not semantic acceptance.
- Word-native PDF: `evidence/0011_I02-E02_R09_WORD_NATIVE.pdf`, SHA-256 `bcbb5c0582b5ce9a89aae17012287c11e1413de0c741e06770959f533f5f2c38`, 28 pages.
- Visual QA: `evidence/visual_qa_R09.json` — all 28 Word-rendered pages inspected. The R09 page-8/9 HOLD-table split and page-10/11 Table 7-5 caption/table split are resolved; no observed clipping/overlap. The receipt is limited to layout/readability.
- Every rendered page PNG and its SHA-256 is under `evidence/render/` and listed in the visual receipt.

## Writer and integration provenance

- Original text writer output: `source/luna_subagent_draft_R01.md`, SHA-256 `27e695922bd2b2e0e844f0edca32c28f967ceb252a075225a3b3e5f7a98e1d82`.
- Its original receipt is included. That receipt marks it `TEXT_DRAFT_ONLY_NOT_QA`; the model/provider identity is not established in that receipt and is therefore UNKNOWN.
- Integrated source: `source/integrated_draft_R07.md`, SHA-256 `a35e2edbf446d3e9be3f319800063f0df88c54e45dd9e33f75758a20e33ec370`, plus its integration receipt.
- The R09 build receipt and build script are preserved. R09 applies narrowly scoped pagination/layout changes; substantive content remains based on the integrated draft.

## State boundaries

The deterministic technical and visual results apply only to the exact DOCX SHA above. Neither result establishes an independent semantic PASS. Do not combine receipts from other revisions or treat this candidate as `CURRENT`, `REAL`, `APPROVED`, or `FORMAL_ACCEPTED`.
