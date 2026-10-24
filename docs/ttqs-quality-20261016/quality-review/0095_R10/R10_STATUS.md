# DOCX 0095 R10 candidate and exact-SHA review status

Project: TTQS_ONE  
Document: 0095 — I18-E02 — 建立目標客戶及學員滿意度調查機制（系統及流程面）  
State: CANDIDATE; formal association acceptance is not asserted.

## Candidate and evidence

- DOCX SHA-256: 4c52fe99188b726f1e62754484aec8604abae83d73643c46a263f7e6a7ee3630
- Word-exported PDF SHA-256: de40911be70a852798e285141b7f8536c7ae48c4e2285a715685d5d74bd65b4d; 44 pages
- Technical readback: PASS for this exact DOCX SHA; 383 paragraphs, 29 tables, 19 sections; body font floor 10.5 pt, table floor 9.5 pt.
- Visual QA: PASS_WITH_SCOPE_LIMITS for this exact DOCX/PDF pair; all pages represented in three inspected contact sheets; direct high-resolution inspection on the pages recorded in the receipt.
- Independent semantic review: PARTIAL; 0 blocking and 5 nonblocking findings. The exact response, raw CLI output, packet and receipt are included.
- Reviewer route: OpenCode CLI v2.0.32, requested model opencode/minimax-m3.1-flash-free; session model ID minimax-m3.1-flash-free; provider-model identity UNKNOWN.
- The semantic reviewer examined packet text and supplied receipts only; it did not rehash the DOCX, rerender the PDF, or inspect page images. Its review is not formal TTQS acceptance.

## Required targeted R11 correction

1. Issue a new register/manifest revision bound to the R10/R11 page layout; preserve the original R08 CSV and manifest as history.
2. Correct document_location page anchors for chapter 6 onward. The current R10 export has a one-page shift relative to R08 anchors; the independent review lists the affected ranges and examples.
3. Correct the §1.4 spans to §5.1 pp.20–21, §5.2 p.21, and §9.5 pp.38–41.
4. Correct the §9.5 row-3 self-location from PDF p.39 to the actual page.
5. Correct the 65-character CSV SHA printed in Attachment A; bind it to the actual 64-character SHA.
6. Show both parent-source SHA and page-extract SHA for official page 6 and scoring-form page 4 in the source traceability text.
7. Rebuild once from the targeted manuscript/register revision, render and verify the final pages, then obtain a new independent exact-SHA semantic review.

R10 remains a useful historical candidate and must not be relabelled PASS. No REAL association evidence, approval, signature, or formal adoption is asserted. All example data are SAMPLE/SYNTHETIC; missing real-source classes remain UNKNOWN.
