# 0036 R09 layout correction and full-page visual supplement

**Status: CANDIDATE ONLY; not promoted or formally accepted.** This R09 candidate maps DOCX 0036 to official requirement I07-E04 (official checklist checkbox serial 036). DOCX identifiers and checkbox serials are separate namespaces.

## Exact artifacts

- DOCX: `candidate/0036__課程設計進度與訓練規劃_R09.docx`
- DOCX SHA-256: `91d749d00b153227bb3db67a60c552c0e17fa2b5364c799dee7de6bf69117815`
- Word COM PDF: `evidence/render/0036_R09_word_export.pdf`
- PDF SHA-256: `b68da17dd6fae66eb05db8c2c8a6d91bc44abb53487d34880975533a2639b677`
- Render: 19 page PNGs in `evidence/render/` (1191 × 1684 px each)

## Finding and narrow correction

The R08 full-page supplement found that the last row (item 8) of the service-record scoring rubric appeared alone at the top of page 13 without column labels. R09 preserves R08 unchanged and moves only that final row into a two-row continuation table with a visible copy of the four-column heading. An existing spacer paragraph is used for the page break. No prose, sample values, calculations, evidence claims, or decisions changed; the only additional visible text is the duplicated column heading.

The resulting Word COM export remains 19 pages. Page 13 now shows the heading above rubric item 8. The summary table that continues on page 14 also has its column headings visible. Pages 1–11 are pixel-identical to the R08 Word COM render. Pages 12–19 were directly inspected in the R09 render. The page 5 curriculum-design flowchart was directly re-inspected: arrows, both rejection branches, labels, and the release condition are readable. No clipping, overlap, blank page, or footer displacement was observed.

## Review scope and limitations

R08 has an independent Antigravity CLI semantic review bound to R08 SHA `e2d4b3f5e906faaf3d473c7351bd79618a78dcf2c8f91a32a4e952d005ac5eae`, verdict PASS with a declared visual-scope limitation (the reviewer directly inspected only pages 14, 16, 18, and 19). The raw reviewer output and scope statement remain in the sibling `../0036_R08/review/` bundle. This R09 change is limited to OOXML table pagination/heading structure, and a structural text-integrity comparison confirms that all original visible text is unchanged after excluding the one duplicated heading row. **No fresh R09 exact-SHA semantic review is claimed.** R09 has a full direct visual review, but remains a candidate and is not formal association evidence or approval.

R08 source package inputs are preserved here for audit: unique Blueprint, neighboring Blueprint, official text/map, checkbox crosswalk, and the 75-row SAMPLE/SYNTHETIC replacement register. Source identifiers and hashes are in `PROGRESS.json` and `artifact_manifest.json`.

## Render and verification method

The packaged `render_docx.py` was attempted, but this runtime has no bundled `soffice.exe`; its failure is recorded in `review/render_docx_attempt_R01.txt`. No installed LibreOffice was used. R09 was exported and rasterized through Microsoft Word COM, matching the renderer used for R08. Package integrity, exact SHA-256, 19-page count, 19 image count, the one-file OOXML diff, and text equivalence are checked by `review/0036_R09_visual_and_integrity_receipt_R01.json`.

## Boundary

All modeled dates, roles, cases, decisions, values, and outcomes remain SAMPLE/SYNTHETIC. R09 is not a claim that the association held a course, approved a plan, hired a trainer, received actual results, or issued a formal release. Human acceptance and any real-source replacement remain separate.
