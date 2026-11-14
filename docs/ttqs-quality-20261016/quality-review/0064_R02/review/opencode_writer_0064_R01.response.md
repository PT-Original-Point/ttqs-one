The work packet is complete. Below is the manifest.

## Manifest — 0064 R01 (資訊檢索效率測試報告, I14-E05 / 方框 069)

### Created files (this folder only)
| Path | Bytes |
|---|---|
| `UNIQUE_BLUEPRINT_0064_R01.md` | 13,995 |
| `candidate/0064_R01.docx` | 53,445 |
| `build/fixture_0064.py` | 14,281 |
| `build/benchmark_0064.py` | 10,468 |
| `build/make_register_0064.py` | 15,424 |
| `build/build_docx_0064.py` | 43,407 |
| `build/qa_docx_0064.py` | 3,731 |
| `build/render_docx_0064.py` | 2,192 |
| `build/run_all_0064.py` | 3,135 |
| `evidence/fixture/synthetic_index_0064_R01.json` | 10,704 |
| `evidence/benchmark_runs_0064_R01.csv` | 11,752 |
| `evidence/benchmark_summary_0064_R01.json` | 10,414 |
| `evidence/0064_R01_SYNTHETIC_REPLACEMENT_REGISTER.csv` | 92,227 |
| `evidence/technical_qa_0064_R01.json` | 376 |
| `evidence/visual_review_0064_R01.json` | 476 |
| `evidence/0064_R01.pdf` | 622,289 |
| `evidence/pages/page_01..11.png` | — |
| `evidence/build_receipt_0064_R01.json` | 3,079 |
| `evidence/README_BUILD_RUN.md` | 2,318 |

`inputs/` SHAs re-verified and unchanged (`official_source.pdf` `805386…4709`, `0061_UNIQUE_BLUEPRINT_R02.md` `C589…CABB`). No full-disk search performed; nothing outside this folder written.

### Commands run and exit codes (all 0)
`python build\benchmark_0064.py` → 0 (OK runs=200 correct=200 corpus=30 reps=20)
`python build\make_register_0064.py` → 0 (OK register rows=337 blanks=0)
`python build\build_docx_0064.py` → 0
`python build\qa_docx_0064.py` → 0 (checks_passed = true)
`python build\render_docx_0064.py` → 0 (OK pages=11)
`python build\run_all_0064.py` → 0 (all_exit_zero = True)

### Candidate
`candidate/0064_R01.docx`
SHA-256 `D3C6CD6E2B573047CB34F132930F0FFAC07035ADB3195A1D1F051D7FF0B1BBDD`

### Result source (measured, not hand-filled)
- Fixed synthetic index of **30 records** (24–36 range), no personal data.
- **10 query specs × 20 reps = 200 runs**; clock `time.perf_counter_ns` (monotonic).
- **200/200 runs correct; 0 unauthorized leakage**; each type ≥10 runs.
- Percentiles **nearest-rank** (`rank = ceil(p/100 × n)`), stated identically in program, receipt and body. DOCX tables read directly from `benchmark_summary_0064_R01.json`.

### Checks actually performed (and what I do NOT claim)
- Verified: body font ≥10.5 pt (min 10.5), table font ≥9.5 pt (min 9.5), header/footer banner present, no `sha256/json/csv/build//evidence//code-id` leaks in the human body, 11-page render, all 11 pages visually inspected, register 337 rows / 0 blank cells.
- **Not claimed:** I did **not** run an independent reviewer, and the numbers describe only this Windows host's in-memory lookup over a synthetic index. Status remains **CANDIDATE**; `human_acceptance` is not asserted.

### Unresolved / blockers
- Independent **exact-SHA review not performed** → document held at CANDIDATE (cover note added).
- REAL items remain **UNKNOWN** (association's real retrieval system name/version, real user accounts/permissions, real index field spec, association-approved thresholds, real locator/original positions via 0062) — listed in ch. 11.
- Latency figures are run- and host-specific; the blueprint therefore quotes only the deterministic outcome metrics (200/200, 0 leakage, 100% hit) and defers all timing to the measured summary.

Hard boundary respected: this is a retrieval-efficiency **test report** (environment + sample + query + reps + measured result), distinct from 0060 (coding), 0061 (lifecycle/permission/backup), 0062 (inventory/originals) and 0063 (query function/improvement).
