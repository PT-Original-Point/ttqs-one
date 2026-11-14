# 0064 R05 to R06 targeted repair

- R05 DOCX: `54888e13f954478051a49839d8b67ff845992c72811e41e09d90045e512c69e1`; preserved unchanged.
- R06 DOCX: `f83eeda42589da66c23918d522ad983178a252da9b6dd2240b725e9c9cfb50a1`.
- Finding: R05 page 19 stranded the §13.3 24-pair timing-table header at page bottom.
- Fix: `keepNext` on all six header-cell paragraphs; repeated-header marker retained.
- Revision field: R05 -> R06.
- Text delta: version label only; no substantive text/table change.
- OOXML delta: `word/document.xml` only; styles and run font/style signatures unchanged.
- Render remains 28 pages. Page 19 now ends after the SYNTHETIC callout; the table starts with the repeated header and data on the next page.
- Status: technical PASS; visual PASS_LAYOUT; independent exact-SHA semantic review pending; formal acceptance not granted.
