# 0118 R05 change and evidence log

- Document: 0118, mapped to I19-E05 (internal Blueprint index 129). Official printed checkbox serial is not asserted.
- Candidate SHA-256: aa6ee02e2b3ae7c0ef06e74cad6333f2ddcc3bc306651f4e3e5694ecf5838707.
- Status: candidate only; formal acceptance remains NOT_GRANTED.
- Real original: none supplied. Names, third-party signatures, approvals, receipts and association decisions are not represented as real. Demonstrations/data are synthetic and replacement-listed.

## R05 delta

R05 was a minimal repair of the stable R04 candidate, not a fresh rewrite. It aligns the OOXML grid widths with the actual widths in table 2 and restarts the I19-E05 §7.1 routing sequence at (1)–(4). The Word file is fixed at the R05 SHA above.

## Evidence history

- R01 had a partial review and a Word export failure; sanitized receipts are retained under history/.
- R02 had its own semantic and visual results. Those results are historical and do not establish R05 quality.
- R03/R04 layout repairs are retained as history only. The R05 visual receipt identifies the prior defects that remain resolved.
- R05 technical, visual, and semantic receipts each bind to the same final DOCX SHA. The OpenCode final answer was recovered from the same completed session after a UTF-8 console capture issue; the model was not rerun. The private session export, internal reasoning, and corrupted raw stream are excluded from this public package.

## R05 verification

- Technical package/text/layout controls: PASS, see qa/technical_recheck_R05.json.
- Microsoft Word native PDF output: 11 pages; all 11 page images inspected, PASS, see qa/visual_findings_R05.json.
- Independent semantic review by a separate OpenCode v2 CLI plan-agent session: PASS on supplied R05 packet. The reviewer did not independently recompute the DOCX SHA and did not inspect images; upstream serving identity and provider billing are UNKNOWN.
- Candidate state remains CANDIDATE; real-original processing and formal association acceptance remain pending actual authorized evidence.
