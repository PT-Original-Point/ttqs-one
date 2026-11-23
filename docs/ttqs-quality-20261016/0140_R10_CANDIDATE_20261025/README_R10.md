# DOCX 0140 R10 candidate

- Mapping: DOCX 0140 -> requirement I19-E30 -> official 157-item index 154; printed checkbox serial: UNKNOWN.
- Exact candidate SHA-256: de9525e42a391d0ed002d23d54d5a9b9c1e042f7c194b71f00b61bd98ff48c16.
- R10 changes only Word rendering of paired single-asterisk emphasis; manuscript text, 80-row SAMPLE data, chart inputs and replacement register are unchanged from R09.
- The audit bundle contains the source manuscript, dataset, replacement register, source mapping, build/QA code, receipts, four rendered pages showing changed emphasis, the operational checklist and chart, and original OpenCode review materials. The complete 29-page Word PDF remains in the Windows candidate folder.
- Deterministic technical/content QA: PASS, 21/21 checks.
- Native Microsoft Word render: PASS, 29 pages; PDF SHA-256 03a9e7c8efd30beb81f0882bb6995211bff2bd6a6e487f0c45ff2c28117cfdd5.
- Visual review: PASS, all 29 pages individually inspected; exact page image hashes and R09 pixel-diff results are in receipts/R10_VISUAL_PAGE_DIFF.json.
- Independent OpenCode CLI v2 text semantic review: PASS, bound to the candidate SHA. It reports three LOW wording recommendations and one chart OBS; the chart values were checked in the separate visual review. The three LOW items remain non-blocking and are not represented as repaired.
- Reviewer did not recompute the DOCX binary SHA or inspect page images; host and Word-render receipts separately bind those artifacts.
- Replacement register: 82 data rows (80 SAMPLE user-year rows plus two control rows) and one header = 83 physical lines.
- Status: CANDIDATE only; REAL evidence UNKNOWN/HOLD; formal acceptance NOT_GRANTED.
