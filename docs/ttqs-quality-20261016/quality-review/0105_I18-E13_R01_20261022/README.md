# 0105 / I18-E13 — Performance Improvement Survey and Follow-up Kit

**State: CANDIDATE. Formal acceptance: NOT GRANTED. Real association results: UNKNOWN.** This package contains a complete SAMPLE/SYNTHETIC worked example and does not claim real learners, customers, outcomes, approvals, or signatures.

## Source and identity

- `doc_id=0105`; official requirement `I18-E13`; project 157 index 114. The separate official checkbox serial is not asserted.
- Source packet SHA-256: `166338523fad5550511cd5f16fd7b347b28a23ef295fdc9396c21bb8728ae99e`.
- Unique Blueprint SHA-256: `0a457287fcc005e13408ad85763f4e7065dd1915f3f9b11757928c64715cb826`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.

## R04 candidate

- DOCX: `candidate/0105_I18-E13_績效改善調查與課後行動計畫追蹤套件_R04.docx`
- SHA-256: `17f7d680cbb992db93a6f67df84415500050953eecf426b477f675810177b4cb`.
- Deterministic technical QA: **PASS 32/32**, bound to this SHA. The 60-row replacement register identifies every example as SAMPLE/SYNTHETIC and HOLD. The worked response data reconcile: 6 learners/23 positive, 4 customers/17 positive, total 10/40 with 7 positive; overall mean 4.0 and positive rate 70%.
- Independent semantic review: **PASS** on this exact SHA. Antigravity CLI 1.4.4 requested `gemini-3.8-flash-high`, returned CLI exit 0 / `SUCCESS`, and reported 46,557 tokens in one turn. The provider's actual serving model and fallback status are **UNKNOWN**; this is not evidence of Gemini quota or billing. The review covered semantics only, not rendering or technical QA.

## Remaining visual blocker

R04 has **no verified PDF or page images**. Word opened the exact candidate and reported 13 pages. Three bounded output paths then stalled without producing a PDF: whole-document `ExportAsFixedFormat` (~150s), `SaveAs2` on a byte-identical copy (~155s), and page-range export (~154s). The first pre-start attempt also exposed a PowerShell UTF-8 BOM/path issue, which was corrected before the three stalled calls. The 19 pre-existing Word embedding processes were preserved.

The bundled `render_docx.py` requires LibreOffice on Windows; `soffice.exe` was not found on PATH or in the bundled dependency tree. R02/R03 page images are historical and do not satisfy R04 visual review. Accordingly, `VISUAL_QA=BLOCKED`, not PASS. Resume only when a compatible existing renderer is available; do not rebuild R04 solely to add receipts.

## Worker evidence

OpenCode v2 CLI 2.0.32 first selected `deepseek-v4.1-flash-free` and returned zero manuscript tokens (`finish=length`); a bounded second dispatch selected `mimo-v2.6-flash-free` and returned the retained manuscript. The session model identifiers are recorded, but serving identity/fallback and vendor billing are UNKNOWN; local-reported cost was zero. The manuscript and both dispatch records are under `writer/`.

The complete raw Antigravity response, prompt, retry/parser error, requested model, token usage, and exact-SHA semantic receipt are under `evidence/`. Neither Worker directly produced the final DOCX; the DOCX was built and technically checked by the native local pipeline.

## GitHub readback

The candidate and evidence package were pushed to PR #92 at commit `abb10fcb356a533777e0e685eb7ff160ad5482e6`. The branch and PR head matched. The first commit's 84 changed paths had 84/84 matching canonical Git blob IDs; all 6 binary artifacts also matched raw SHA-256, including the R04 DOCX (`17f7d680cbb992db93a6f67df84415500050953eecf426b477f675810177b4cb`). Full path-level evidence is in `evidence/github_readback_receipt_0105_R04.json`.
