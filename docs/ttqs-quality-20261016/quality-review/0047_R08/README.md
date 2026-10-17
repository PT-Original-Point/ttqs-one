# 0047 R08 review package

- Candidate DOCX: `candidate/0047_R08.docx`
- Exact SHA-256: `b8cc8e4473e9cd7ad93f21c0cb9503865e683e3b802ac70577fbd8db3524d447`
- Official mapping: DOCX 0047 = I10-E02 = checkbox 048 / P03-B09 (page 3, checkbox order 9).
- Revision R08 corrects one simplified-Chinese character in the negative-neighbor heading. It leaves all numeric content, tables and sample values unchanged.
- Candidate status: CANDIDATE ONLY; no Human formal acceptance, association approval, real event, contract, supplier, signature, or real outcome is claimed. All 25 fact IDs are SAMPLE/SYNTHETIC.
- Visual/technical QA: 8-page PDF and 8 PNGs; every page was directly inspected. DOCX CRC, Word parsing, 25-row register, formula checks, 10.5 pt body and 9.5 pt table direct-size floors pass. Page 8 contains the complete final scale/checkpoint section; it is not blank.
- Independent semantic review: PASS for 10 criteria within the supplied packet, exact candidate SHA as stated. Review output: `review/opencode_v2_review_R01/independent_semantic_review_R01.md`; raw CLI event stream and stderr are preserved beside it. The reviewer did not hash the binary, view page pixels, measure fonts or access the external source PDF; these limitations are retained. OpenCode v2.0.29 CLI requested `opencode/deepseek-v4.1-flash-free`; provider runtime model identity was not returned.
- The reviewer logged minor non-blocking wording/label consistency items and the two-year synthetic sample limit. These are disclosed in `review/review_validation_R01.json`; no additional rebuild is justified by those comments.
- Official neighbor boxes 0045/P03-B07 and 0048/P03-B10 have been independently confirmed against the official inventory in `evidence/REVIEW_INPUT_MANIFEST_R08.json` and `review/review_validation_R01.json`.
- R06 reviewer history remains PARTIAL for missing named neighbor boundaries; R07 added the boundary text; R08 fixes the one-character heading defect.
