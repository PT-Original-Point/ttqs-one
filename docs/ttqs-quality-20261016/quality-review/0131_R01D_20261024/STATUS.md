# 0131 / I19-E20 — candidate R01D evidence package

Original package observation (Asia/Taipei): 2026-10-24T22:17:46.625211+08:00. Current status reconciliation (2026-11-15): see `qa/CURRENT_STATUS_RECONCILIATION_0131_R01D_20261115.json`.

- Official item: p.8 `學員證照通過、就業率高。`; internal crosswalk `I19-E20`; project index 144 / `I19-L3`. Printed official checkbox serial: UNKNOWN.
- Candidate DOCX SHA-256: `1f979e423624e59a63ddf080da5b61354e2526efb68f0d6f8ef1380a57b3f8ba`; bytes: 65841.
- Source body: `0131_I19-E20_BODY_R01C.md`, SHA-256 `1c0fe740375a2fa83010749fb50bf913eb3fbb58cfc2a07463bb3ce1fecf679c`.
- Native Word 365 read-only export PDF SHA-256: `7bcfaa67eaf10e5a3ac168ad77cc52afa2c3cf271270be2593b8855e34cb2487`; 26 pages. The layout correction removed a forced page break before Form 5: the previous candidate had a six-line Form 4 tail isolated on page 26 and Form 5 on page 27. In R01D, Form 4 continuation and the complete blank Form 5 share the final page; no row is orphaned.
- Pages 1–25 are pixel-identical to the previously inspected R01C render; page 26 was inspected directly at original resolution. Full page images and contact sheet are included.
- Deterministic technical/content/layout receipts: PASS for this exact SHA.
- Independent semantic review: `PASS` for text-semantic scope on this exact SHA, via the separate Antigravity CLI W2 review. Requested model `gemini-3.8-flash-high`; actual serving model `UNKNOWN`. Exact extracted-text SHA matches; the reviewer noted a future REAL-version nonresponse-reason field as a nonblocking observation. The earlier OpenCode HTTP 429 records only that route attempt and is superseded as the current semantic status. See `qa/CURRENT_STATUS_RECONCILIATION_0131_R01D_20261115.json`.
- Antigravity writer: requested `gemini-3.8-flash-high`, CLI exit 0 and response returned; actual served model identity UNKNOWN. Reported duration 153.85s and 32,238 tokens are provider response fields, not independently verified billing/account usage. The raw writer response SHA is recorded in `qa/WORKER_DISPOSITION_0131_R01D.json` and preserved in the local work directory; it is not copied into this public package because it contains unadopted unsupported factual and authority claims. The candidate uses a deterministically repaired body, not the worker response verbatim.
- Every example and performance figure is SAMPLE/SYNTHETIC. REAL evidence: UNKNOWN / none supplied. Formal association approval and Human final acceptance: NOT GRANTED.
- Candidate status: `CANDIDATE_TECH_LAYOUT_PASS / SEMANTIC_PASS_TEXT_ONLY`; not formally accepted, not REAL, and not evidence of real association performance.
