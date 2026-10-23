# 0115 I19-E02 candidate R06 audit package

## Current state

R06 is a synthetic, unaccepted candidate for document 0115 / official requirement I19-E02. It is not an association approval, an execution record, a real effectiveness result, or a TTQS acceptance. Real evidence remains UNKNOWN/HOLD; official checkbox serial remains UNKNOWN_NOT_ASSERTED.

Final candidate DOCX SHA-256: `ec4e48258dca756eaad81d899d8195285308fa5e08edb99b31e2f2e9856ff707` (67,054 bytes).

R06 supersedes local R05 only after two exact text corrections identified by the R05 independent review: the document identity now labels the candidate R06 while identifying the adopted manuscript as R03, and table T10R06 corrects `否者` to `否則`. The attached patch receipt records the two-line-only diff; no other body changes were made.

## Verification

- Technical QA: `PASS_TECHNICAL_PRE_RENDER`, bound to the R06 DOCX SHA. It checks package CRC, requirement mapping, candidate status, SAMPLE/REAL boundary, blank-use forms, HOLD/REJECT rules, dataset and A/B case consistency, denominators, percentages, elapsed statistics, and table-font minimum.
- Native Word export: PASS, 24 pages. PDF SHA-256: `1736ab156ca4dd38d133554e93c1d238bcdc3dcd6fc75b30ad3795c551d52a06`.
- Visual QA: changed pages 1 and 17 were directly inspected. They show no clipping or table damage. R06 PNGs for the other 22 pages are pixel-identical to R05; R05's page coverage is retained by exact image hashes. The full 24-page hash manifest is included.
- Independent semantic delta review: PASS for the R06 identity and corrected instruction. The unchanged body retains the R05 full semantic PASS only because the patch receipt proves exactly two string changes. The reviewer did not inspect binary files or images and actual OpenCode serving model, fallback, and billing are UNKNOWN.

R05 remains included as historical evidence, not as the current candidate. Nonblocking whitespace observations from prior visual review remain historical and do not represent new R06 defects. Formal acceptance has not been granted.

## Worker provenance

The initial manuscript was produced through OpenCode CLI v2; requested model was `opencode/deepseek-v4.1-flash-free`, exit code 0, 222.278 seconds. Actual provider model and billing remain UNKNOWN. The R06 reviewer used OpenCode CLI v2, requested `opencode/glm-5.3-flash-free`, exit code 0, 16.322 seconds; raw response contains no tool-call events. Actual serving model, fallback, and billing remain UNKNOWN. No Antigravity run is claimed for this candidate.

## Package map

`candidate/` contains R05 (historical) and R06 (current). `source/` contains the official requirement packet, unique Blueprint, and synthetic dataset. `evidence/` contains the replacement register, change receipt, technical/visual receipts, current candidate status, and package manifest. `review/` preserves the original R05 full-review output and the exact R06 delta-review request/output/receipt. `render/` contains native Word PDFs, renderer receipts, page-hash manifests, and the two R06 changed-page images. `writer/` preserves the original OpenCode manuscript response and dispatch receipt.
