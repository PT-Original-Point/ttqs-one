# 0120 R01A evidence manifest

- Project: TTQS_ONE; document: 0120; official requirement: I19-E08; official printed source page: 8.
- State: CANDIDATE; formal acceptance: NOT GRANTED.
- Candidate DOCX: `0120__訓練成果初步證據彙整與評量表_R01A.docx`; SHA-256 `d99e4caec0f2ede04ed607d0e7a897065213c06c8e93bcadb83e638e3b54e57a`.
- Input R01 retained unchanged: SHA-256 `7dfc32e23d0be9e5c5749b3e721ae47d7a472dd913d9d247ce76a70eaa8ebaf4`.
- Source packet SHA-256 `2b04bc2bc232b45247b37ab93bf00e25d8d2fff8402366e771b960c8fe096b9d`; unique Blueprint SHA-256 `09a3aec874c14f97d5d6a1bed85d3cd75d617a9cf4bd33871973e5cb27c088ad`; official page-text SHA-256 `C34EAD45CAD406150DE5622E157F44727157776CE5C6ABF5343C7DB5DCA42520`.
- Change: preserved R01 and added 22 row-level SAMPLE/SYNTHETIC replacement mappings for 8 satisfaction records (7 responses, one nonresponse not imputed) and 14 assessment records; added rows map to DOCX table 26 and the sidecar CSV. All such entries remain `PENDING_REAL_SOURCE`.
- Deterministic technical/arithmetic check: PASS for assembly and arithmetic only; 15 prior baseline rows retained, 22 row-level rows added, all 14 assessment totals reconcile to five item scores, satisfaction values recomputed.
- Word render: Microsoft Word COM export, 15-page PDF. Visual QA: `PASS_VISUAL_15_OF_15`, with page images and per-page SHA in `render/visual_qa_receipt_R01A.json`.
- Independent semantic CLI response: PASS, zero findings, exact candidate SHA; response checks full extracted body, official requirement, Blueprint and recalculations. The requested model was `gemini-3.8-flash-high`, but raw CLI response has no model/provider field; actual model identity and fallback status are UNKNOWN. Reviewer did not inspect rendered pages (`visual_scope=NOT_EXAMINED`); visual QA is separate. Cost is UNKNOWN.
- Worker invocation: Antigravity CLI 1.4.7, PID 84684, exit 0, one turn, 67.79 seconds; raw stdout/stderr, prompt and dispatch receipts are preserved under `review/`. This does not prove Gemini model identity and does not restore the separately paused 0110 Writer lane.
- Scope boundary: all newly added records are SAMPLE/SYNTHETIC; no real association results, approvals, signatures or formal acceptance are represented.