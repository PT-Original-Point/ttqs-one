# 0102 / I18-E09 / R14 candidate package

**State:** candidate only. Formal acceptance is not granted.

## Identity and source binding

- `doc_id`: 0102; official requirement: I18-E09; current project 157 index: 110.
- The official paper form does not print a checkbox sequence number; `printed_official_checkbox_serial=UNKNOWN`.
- Source packet Git blob at the PR #92 head used for this readback: `41a98e2f0eca92d8ad6be05b396f6a18ceb4ca68` (remote-byte SHA-256 `1C71D7095D32C31DACF450B0069E0C4AB3D7D2B9F296E38827CFFF9976A7F767`).
- Unique Blueprint Git blob: `d20368335369a0680c97a43360d60f120cc37bfe` (remote-byte SHA-256 `6DDF1FB585EB24144DFC544034D74E9FB9E02C742521083150F4087357E8BC8A`).
- These documents distinguish `doc_id=0102`, `I18-E09`, project index 110, and unknown printed serial. The source packet's earlier “no current candidate” status is historical and superseded by this R14 receipt.

## Candidate and content boundary

- DOCX: `../../candidate/0102__技能競賽獲獎證據取得與查核工作紀錄_R14.docx`
- SHA-256: `DFF360BD29772B5CC52FCB7ABE227B7281589949F3744EA06D9C9E91AA83F007`
- The document is SAMPLE/SYNTHETIC and does not assert that the Association has real awards, third-party originals, approvals, or verified outcomes.
- R14 applies local spacing and version-label corrections to R13; no narrative, facts, figures, dates, cases, or workflow rules changed from R13.

## Render and visual inspection

- Word-created PDF: `0102_R14_Word_native_export_20261023.pdf`; 54 pages; SHA-256 `2F30AC7E7779078D73F72642DD7FBE99CDC7A72259AA1C21E0580361F555D67D`.
- All 54 page images were reviewed in six contact sheets; pages 1, 13, 48, 49, and 54 were also inspected at full resolution. Page 13 has a sparse four-row continued table; it is recorded as a nonblocking layout note. No clipping was observed; the final caution remains on page 54.
- See `visual_review_receipt_R14_20261023.json` and `page_image_manifest_R14_20261023.json` for exact hashes and scope.
- Word produced the PDF, but the exporter process hung during COM cleanup after output creation; its exit status is UNKNOWN. The partial export receipt records this and no normal exporter-exit PASS is claimed.

## Remaining gate

- Exact-SHA independent semantic review for R14: PENDING.
- Formal acceptance: NOT_GRANTED.