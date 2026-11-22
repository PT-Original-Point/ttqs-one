# 0045 R03｜訓練資源採購與甄選管理辦法

- Requirement I10-E01；官方方框 047（不是 DOCX 0047）。
- Exact candidate SHA-256：2ea8937143c5360e03d3db74cf531b8ddffccaecaf4058c89bb3df2ede06d031。
- Base：R02 SHA-256 099c10e7039b370ca39066e9baf15267a5f8122aab1aad59ae90a0b4440885fb；R02 PARTIAL remains immutable.
- R03 repairs the price-score contradiction, adds the internal-instructor path, replaces unverifiable table-number references, and distinguishes checkbox 047 from DOCX 0047.
- Technical QA PASS；visual layout PASS (13/13 pages inspected). See evidence receipts.
- Semantic review is pending fresh OpenCode CLI v2 review on this exact SHA.
- SAMPLE/SYNTHETIC only; no actual Association procurement or approval is represented.
- Promotion remains NOT_PROMOTED.


## R03 exact-SHA 語意審查

- DOCX SHA-256：2ea8937143c5360e03d3db74cf531b8ddffccaecaf4058c89bb3df2ede06d031；維持未變。
- OpenCode CLI v2.0.29 獨立審查：PASS（僅 SAMPLE/SYNTHETIC 候選）；0 項阻擋、6 項非阻擋觀察。
- 審查原文與原始 CLI bytes、session、exit code、模型身分限制及封包 SHA 見 review/opencode_v2_review_R03/。
- 真實協會核准／採購履約未證實；不代表 Human 正式接受或升格。
- 目前只待同一 GitHub 分支同步與 exact-byte readback；不得因 metadata 重建 DOCX。

## GitHub raw-byte readback (2026-11-23T06:34:08+08:00)

- PR #92 branch HEAD `e7c384ed1565e9e9f20f42d04bcf43426faa359a` raw-read `candidate/0045_R03.docx`: 58,417 bytes; SHA-256 `2ea8937143c5360e03d3db74cf531b8ddffccaecaf4058c89bb3df2ede06d031`; Git blob SHA-1 `83be15925195cfd1a633394a1f9e55e3ba048517`; exact byte match.
- Same-SHA static QA PASS; Word visual PASS across 13 pages; OpenCode semantic PASS for declared SAMPLE scope, zero blocking findings and six nonblocking findings. Requested route `opencode/deepseek-v4.1-flash-free`; served model identity UNKNOWN. Five stale sidecar entries in the old manifest were refreshed from the pinned checkout; candidate bytes unchanged.
- Receipt `evidence/qa_original/github_raw_byte_readback_r03_current_head_20261123.json`. Candidate remains SAMPLE/SYNTHETIC CANDIDATE; formal acceptance NOT_GRANTED; REAL evidence NOT_ESTABLISHED.
