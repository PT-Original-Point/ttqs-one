# Official PDF page 2 text and location check

## Bound source

- File: E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf
- SHA-256: 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709
- Page count: 9
- Source file length: 303044 bytes
- Text readers: pypdf 6.21.4; pdfplumber 0.11.9
- Extraction page: PDF page object index 1 (human page 2); rendered at 160 dpi.
- Rendered original visibly shows printed page number 2.

## Locator checked against the page image

The target is in official table indicator 6 (table row 6) under the vertical group label 「能力」. The row heading is 「6.訓練機構的行政管理能力及訓練主管相關職能」. Within the rightmost column 「常見參考佐證資料（並註明資料來源及頁碼）」, it is checkbox 2 of that row, between the work-experience training proof and the organizational training-capability description.

- Target checkbox, visually read: 專業訓練人員職能評估方法等證明。
- Blueprint mapping: I06 row 030, training-personnel competency evaluation, rubric, role scores, gaps, improvement and reassessment.
- Adjacent item 7 on this same page covers training-needs-related competency analysis and its application; it is outside this personnel evaluation method.

## Text readback comparison

The complete second page was read with two independent extractors. Their unmodified outputs are preserved in OFFICIAL_PAGE2_READBACK_PYPDF.txt and OFFICIAL_PAGE2_READBACK_PDFPLUMBER.txt. pypdf recovers the full checkbox string after layout whitespace is removed:

專業訓練人員職能評估方法等證明。

pdfplumber preserves the target words but its flattened table reading order interleaves text from adjacent cells across line breaks, so its full-page string does not contain the entire checkbox as one uninterrupted normalized substring. This limitation is recorded rather than treating the two extraction results as identical. The page image confirms the exact printed phrase and checkbox location. pypdf maps the checkbox glyph to private-use character U+F070 in its text output; the image shows the printed square.

## Render notes

OFFICIAL_PAGE2_RENDER.png is page 2 rendered from the bound PDF. OFFICIAL_PAGE2_RENDER_LOG.txt preserves renderer output. The renderer emitted missing-display-font warnings for Symbol and ArialUnicode; the target row remains visibly legible and is confirmed against the original page image.
