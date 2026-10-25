# 0141 R06 closeout (candidate only)

- Work: doc_id 0141 / official requirement I19-E31 / internal 157 index 155.
- Candidate DOCX SHA-256: `e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2`.
- Semantic review: exact-SHA `PASS`, 0 major, 4 minor; text-only. This does not promote or formally accept the document.
- Four remaining minor findings: (1) 36 row register locators should use Chinese appendix/section locations and clarify aggregates use all rows; add R06 source manuscript SHA metadata. (2) Align “7 core items” phrasing with six construct items plus separate Q7. (3) Show Q2/Q5 sample Top-2 baselines and make future success thresholds explicitly baseline-plus-delta SAMPLE parameters. (4) Add a plain ASCII UNKNOWN-sourced locator while keeping the nonbreaking live token.
- All 25 Word pages were rendered and visually inspected in contact sheets; pages 1, 8, 11, 12, 14, 16, 24 and 25 also full-resolution. The initial page 11/12 token split was fixed before the final SHA; no clipping or overlap remained.
- Reproducible math QA passes against all 36 synthetic rows and R01 summary. REAL remains UNKNOWN/HOLD; official score NOT_ASSIGNED; Human acceptance NOT_GRANTED.
- Worker receipt: OpenCode v2 requested `opencode/deepseek-v4.1-flash-free`; actual serving model UNKNOWN. Writer exit 0, no recorded tool errors. Semantic review returned a complete response with stderr 0; its process exit code was not captured. Provider token usage and cost UNKNOWN.
- Render incident: first COM attempt exported a PDF but failed in `Application.Quit(0)` because this local COM binding needs `[ref]`; the call was corrected, re-render passed, DOCX SHA stayed unchanged. Only the exact new hidden Word orphan from that attempt was cleaned up; legacy Word processes were not touched.
- Deterministic QA verifier had two corrected column-key mapping mistakes before final pass; they changed no source or DOCX bytes. Final script and receipt are bound by SHA in `R06_WORKER_CLOSEOUT_RECEIPT.json`.
- R06 is retained as a reviewed historical candidate with 4 minor findings. R07 will address only these findings and receive its own SHA-bound QA.
