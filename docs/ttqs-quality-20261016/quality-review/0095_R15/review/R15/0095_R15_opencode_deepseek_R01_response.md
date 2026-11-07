**Verdict: PASS** — bounded R14 F-01 closure review only, bound to the packet-declared DOCX SHA `c70521d50fbec6cdc3b53ce3dc35fa2613069e60c58625b7eb2f96a5a6fd3658`.

**Blocking count: 0**  
**R14 F-01: CLOSED**

| Check | Result | Evidence |
|---|---|---|
| (1) CSV row points to §9.5 row 3 at p.39 | **PASS** | `qa/0095_R15_synthetic_replacement_register.csv`, key `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE`: `§4.1 Tool-A blank REAL date fields; §4.2 Tool-B blank REAL date fields; §9.5 row 3；PDF pp. 11, 15, 39` |
| (2) Actual page 39 and manuscript map agree | **PASS** | Loaded `qa/render_0095_R15_final/page-39.png`: §9.5 table, row 3, target key, footer `第 39 頁`; manuscript §1.4 maps §9.5 → pp.39–42 and §9.5 states row 3 is on p.39 |
| (3) DOCX binds the R15 CSV SHA | **PASS** | `writer/0095_R15_CANDIDATE.docx` → `word/document.xml` contains `163796fb365509ddda1d03fe2db7f795feb4f45fba30cbb138fd50857eafd1c9` twice; R15 manifest declares the same `current_csv_sha256` and DOCX SHA `c70521…` |
| (4) Only this register locator changed vs R14 | **PASS** | Direct read-only comparison of R14/R15 CSVs: 211 rows, identical keys/order, exactly **one** changed cell — `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE.document_location`, `p.38` → `p.39`. Manuscript R14→R15 differences are version/SHA relabeling; no factual values changed |
| (5) No REAL fact, approval, signature, or execution inferred | **PASS** | §9.5 row 3 status remains `未提供；UNKNOWN`; REAL date fields remain blank; no approval/signature/execution claim introduced |

**Exact key/page:** `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE` — §9.5 row 3 — R15 PDF **p.39**.

**New finding:** None blocking. Scope note only: the DOCX necessarily carries R14→R15 version/SHA relabeling beyond the single CSV cell; this is bookkeeping, not a substantive change.

**Model identity:** UNKNOWN as native attestation. Harness label only: `opencode` / `deepseek-v4.1-flash-free` (DeepSeek V4.1 Flash Free); not treated as provider attestation.

**Limits:** This is not a full unchanged-content review and does not assert formal acceptance. No direct byte hashing was performed; SHA bindings above are read from the packet, R15 DOCX text, and R15 manifest, not independently recomputed.
