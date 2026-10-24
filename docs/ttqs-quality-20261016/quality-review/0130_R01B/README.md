# DOCX 0130 — I19-E19 — R01B

## Candidate state

- State: `CANDIDATE`; formal association acceptance is not granted.
- Official evidence purpose: `學員訓後創業案例。`
- Internal crosswalk: `0130` → `I19-E19`; Blueprint index `143` → `I19-L3`.
- Official printed checkbox serial: `UNKNOWN` in the source excerpt; do not substitute the project index.
- Candidate DOCX SHA-256: `ea67d33b6bcca83b9640614b60e0363b2f5186fa2f03a9a196c3a5e59de83c0b`.
- Adopted Markdown SHA-256: `8c9c9f7845d9d63fde9b4007d6ea7a7bf1d819843c904c2f6759bd6905733222`.
- Source packet SHA-256: `2611e44b35aff821d70b4d9ca0ca77cbbdd267057006ec84c02da1a89a1cc1da`.
- Unique Blueprint SHA-256: `1eb6ad3b4e5b4d88c59ec67599b2dd4fe361f4a5bc7c680acf5bba4f7a267ecc`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.

## Verification

- Deterministic OOXML/static checks: PASS; 15 tables, Markdown/DOCX table cells exact, no duplicate numbered paragraphs or incomplete source placeholder; body minimum 10.5 pt and table minimum 9.5 pt.
- Native Microsoft Word export: PASS; 13-page PDF, SHA-256 `a22950c24a52597f4f7c9e8a29e91b292a4dcc7ecfc8b32c46212f37eaf5105d`.
- Visual inspection: PASS for all 13 page images at original 894×1263 raster resolution. The source/claim matrices are five columns and readable. All three hard stops remain together on page 13; no orphan-only page. See `evidence/VISUAL_QA_0130_R01B.json`.
- Independent semantic review: PENDING. One exact-SHA OpenCode v2 review request was rejected with HTTP 429 `FreeUsageLimitError`; no assistant review was returned. Do not treat this as PASS. See `review/opencode_semantic_R01B/`.
- Formal acceptance: NOT GRANTED.

## SAMPLE / REAL boundary

All case identities, dates, course data, claims, and evidence labels are SAMPLE/SYNTHETIC. No real association records were queried or supplied. Authorization to use or externally verify real personal data is UNKNOWN; real case evidence and actual association outcomes remain UNKNOWN. The candidate does not assert that the association received, investigated, verified, signed, or approved a real case.

## Worker provenance

- Antigravity CLI R01 requested `gemini-3.8-flash-high`; native response envelope exited 0 after 146 seconds and produced a manuscript (SHA-256 `b6b4fdf727fcf5aa000cca65e1945104d0a49173b2ea06df0ab8c5d574a8642f`). Serving model identity and provider billing remain UNKNOWN. Sandbox was enabled; Computer Use, file tools, permission bypass and paid upgrade were disabled. CLI stderr warned that `--mode plan` had no effect while slash commands were disabled. The manuscript was adopted only through subsequent deterministic content corrections; exit 0 does not establish model identity or quality.
- OpenCode v2 Writer R01 requested `opencode/deepseek-v4.1-flash-free`; it exited 1 with a 429 free-usage-limit response, 430 bytes and no assistant manuscript. No content was adopted.
- OpenCode v2 semantic review R01B requested `opencode/glm-5.3-flash-free`; it returned 429 before an assistant review. Exact exit code and usage are UNKNOWN. No identical retry was made.

## R01A → R01B corrections

R01B addresses the prior candidate's unsupported authorization wording, overly broad verification/consent assumptions, narrow source and claim tables, and isolated final hard-stop pagination. R01A artifacts remain preserved locally; R01B is a separate candidate revision.