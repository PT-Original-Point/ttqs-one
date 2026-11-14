# Independent exact-SHA semantic review packet — DOCX 0060 R08

## Immutable identity and source hashes
- Project: TTQS_ONE
- Document ID: 0060
- Official requirement: I14-E01; official checkbox 065
- Genre in formal mapping: analysis_report
- Candidate DOCX: `E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0060_R01\candidate\0060_R08.docx`
- Candidate SHA-256: `92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3`
- Word-export PDF SHA-256: `B9850431F0A002E788EC21B4432F47A4F8309E067759C3A7FAB6D95AD3B43BAB`
- Unique Blueprint SHA-256: `166B9D45E439ACD979A59B1ED95F343BC8153D3BC8A7C8E3FF65BD966AD1CA74`
- Official source table PDF SHA-256: `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`
- Formal mapping JSON SHA-256: `4004B7C2F574606BE520E016ACE7377AEFDE3A978003ADDA303CC9A05326440D`
- R08 deterministic technical receipt SHA-256: `4AFC0184037C8C67DBC07488D41082EB32D9C34CF822C1E1A2DC97E7A1870D32`
- R08 render manifest SHA-256: `A0ECBA0F448429ECC53E6396C16C94ADBBBAE2F960CDD9347FA120ADBD3E7989`; 26 pages and 26 rendered PNGs.
- R08 visual receipt SHA-256: `52831748FAED75C63B0C02DCF635B4FC9BCF14970A30DF7F6C1CFE787C9755C0`; coordinator directly inspected full-resolution changed pages 18, 19, 20, 23; 22 unchanged page images match R07 byte-for-byte.
- R08 repair receipt SHA-256: `63D06EDADEDE584FC058914FCF41CA79984F767706CBD214F748E012EF826DB2`
- R08 synthetic replacement register SHA-256: `ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B`

## Review instructions

Return an explicit PASS, PARTIAL, or FAIL for this exact SHA. Independently inspect the attached original DOCX, rendered PDF, official source PDF and mapping JSON. Do not inherit a prior verdict, treat deterministic checks as acceptance, or assume the repair receipt is correct. Compare the entire artifact to the official requirement and this unique Blueprint. Cite exact section/table/row/page locations for each finding. Separate semantic adequacy, mathematical consistency, evidence boundary, and visual usability. The R07 findings below are repair targets to verify, not conclusions about R08. Do not claim direct inspection of an image page unless you inspect it.

Specifically verify:

1. DOCX 0060 maps to I14-E01 / checkbox 065 and is correctly an analysis report, distinct from adjacent system, record-building, retrieval and retrieval-speed requirements.
2. The work is a usable small-association record-classification and coding analysis report, not just a generic manual. Check whether an administrator can classify a record, record source and locator, decide accept/correct/HOLD/reject, explain the decision and obtain a second-person check.
3. Full Blueprint coverage: 12 record types/PDDRO, code grammar and segment restrictions, 11 metadata fields, role-based procedures, workflow/exception branches, full worked table rows, metric definitions, calculations, correction trail, hold/reject criteria, real-source replacement process and conclusion.
4. Independently trace all 12 paired Table 9-1 / Table 9-2 items. Check code, title, date, phase/type, access/retention, source/locator, formation, SAMPLE marker, conclusion, and cross-reference. Verify RSC05->03/04, ATT06->03, DLG07->03/04, ASM08->attendance06, FDB09->attendance06, FUP10->03/06, EXC11->05/06/07, and IMP12->09/10/11.
5. Verify the four R07 correction-trail findings: RSC duplicate 004->005; ATT label INT->RST; DLG locator LOC-REC-2026-0815B; ASM08 must not claim a separate label correction. Confirm row 11 states distinct baselines 11/12, 10/12, 11/12 and fixed results 12/12.
6. Verify Table 15's final example code includes the required `-V01` version segment. Verify Chapter 13 says a zero denominator/no applicable data is N/A with scope stated and never 100%.
7. Recompute the shown sample counts and percentages. Confirm denominators agree with cohorts and evidence links. Report arithmetic correctness separately from presence of numeric strings.
8. Inspect the 66-row sidecar replacement register and verify it is explicitly SAMPLE, all fact IDs are unique, and facts 055-066 match the current R08 Table 12 data rows exactly.
9. Distinguish SAMPLE/SYNTHETIC from REAL everywhere. Flag any implied actual association decision, approval, staffing, training, record, system, policy, legal retention rule, third-party proof, or signature not supported by evidence. Do not treat sample material as actual TTQS evidence.
10. Review layout/readability in the PDF, particularly changed pages 18, 19, 20, 23 and tables spanning pages. Report any clipping, overlap, difficult-to-use table, or page-flow defect with locator. The coordinator receipt is context only.
11. Return: (a) exact candidate SHA actually received; (b) explicit PASS/PARTIAL/FAIL; (c) findings with severity and exact locator; (d) positive evidence; (e) limitations. If any point is unverified, say so.

## R07 findings and repair context

The R07 independent reviewer returned PARTIAL. Its raw response and coordinator adjudication are reproduced below for traceability. Reassess R08 from the attached artifact; do not reuse or rubber-stamp the prior verdict.

### Full R07 independent reviewer response

I'll perform the independent review. First, verifying the candidate SHA and inspecting the actual DOCX.

SHAs verified. Now extracting the full DOCX content for independent inspection.

The console redirect mangled the encoding. Let me re-dump directly to a UTF-8 file.

Full text extracted. Now running targeted verification: the repaired cell, code uniqueness, defect-trail cross-consistency, headers, and forbidden literals.

Core verification is done. Now let me map tables to page numbers via the PDF text layer (programmatic, not visual), and check a few remaining items.

Let me hash the remaining packet-declared inputs (hashing doesn't require PDF content reading) and locate the receipt/manifest/register files.

The register hash doesn't match the packet's receipt claim. Let me investigate where the QA register lives.

Register hash resolved: it matches `sidecar/0060_R04_SYNTHETIC_REPLACEMENT_REGISTER.csv` (8355A495…). Now confirming the worksheet output code in the rendered PDF (page 23) and the register contents.

All verification complete. Both PDF files attached to this session could not be opened as file inputs by this model (PDF input unsupported) — informed as required; I worked around this by hashing them and extracting their text layer programmatically (pypdf), but I did **not** view page images.

---

# Independent exact-SHA semantic review — DOCX 0060 R07

## (a) Candidate DOCX SHA-256 actually received

**`044645199B2D704760D3F8729593641EBE54EBF58CB583ABDC026FA355A69286`** — recomputed by me from `E:\…\quality-review\0060_R01\candidate\0060_R07.docx`, 71,444 bytes. Matches the packet exactly. Other packet-declared hashes I recomputed and confirmed: Word-export PDF `BDEC349D…` ✅, mapping JSON `4004B7C2…` ✅, Blueprint `0060_UNIQUE_BLUEPRINT_R01.md` = `166B9D45…` ✅, official source PDF `805386B7…` ✅ (hash only), technical receipt `FF4CC733…` ✅, render manifest `EE4CFFEA…` ✅, coordinator visual receipt `visual_review_R07.md` = `483A6950…` ✅, register `8355A495…` = `sidecar\0060_R04_SYNTHETIC_REPLACEMENT_REGISTER.csv` ✅ (66 rows, all doc_id 0060, all SAMPLE, unique fact_ids).

## (b) Explicit verdict: **PARTIAL**

The authorized R07 repair is **fully verified** — the exact defect that caused the R06 PARTIAL is gone, in both the DOCX and the rendered PDF. A fresh, blind full-document review nonetheless found two locatable semantic defects (one Major, one Moderate) plus one minor Blueprint gap that preclude PASS. No hard-fail conditions exist, so this is not FAIL.

## (c) Findings with severity and exact locators

| # | Severity | Locator (table = Word table index; page = 26-pp Word-export PDF) | Finding |
|---|----------|------|---------|
| 0 | **Verified OK** | Table 12 (表9-2), data row 12, “形成方式（SYNTHETIC）” cell; PDF p.20 | **Targeted repair confirmed.** Cell reads exactly `綜合09回饋、10追蹤及11三項桌面演練缺失，提出改善追蹤樣張；未核准、未執行。` — no `12 IMP | ` prefix. `document.xml` contains exactly one `12 IMP` (the item cell). Rendered PDF p.20 shows the same clean cell. |
| 1 | **Major** | Table 12 (表9-2) rows 05, 06, 07, 08 — “本報告示範檢核結論” column, PDF pp.18–19 — **vs** Ch.10 narrative PDF p.20 + Table 14 (表10-2) PDF p.21 | **Correction-trail contradiction at row level.** Ch.10/表10-2 locate the three deliberate defects as: duplicate SEQ = record 005 (RSC), missing locator = record 007 (DLG), wrong label = record 006 (ATT). But 表9-2 states: row 05 “初始**定位缺漏**已修正” (locator belonged to 007); row 06 “初始**重複碼**已修正” (duplicate belonged to 005); row 07 — the actual locator-defect record — only “必填欄合規”, no correction note; row 08 “初始**標籤不符**已修正” although record 008 never had a defect. An evaluator spot-checking any of these four rows against Ch.10/表10-2 gets conflicting answers about which record was defective and what was fixed. This is exactly the per-row “tabletop check conclusion” cross-verification required by review criteria 3 and 4. |
| 2 | **Moderate** | Table 15 (表11-1), “綜合輸出成果” row, final cell, PDF p.23 | Filled, directly-reusable worksheet emits **8-segment** code `產出代碼：TT-2026-SYN60A-DO-ATT-RST-S3-006`, missing the mandatory 9th `V[NN]` segment required by the document’s own grammar (Ch.6 P46, Table 7/表6-1) and used by all 12 registered codes. Confirmed identical in the rendered PDF. A reader copying this tool outputs a non-conforming code. |
| 3 | **Minor** | Ch.10 P85 / Table 13 (表10-1), PDF pp.20–21 (document-wide absence) | Blueprint formula rule “無範圍內資料時分母為0，標示N/A並不得報100%” is not implemented anywhere (programmatic scan: no `N/A`, no zero-denominator rule). Rounding and numerator/denominator rules are present and correct. |
| 4 | **Observation** | Table 12 (表9-2) row 11 conclusion, PDF p.19 | “示範資料已由10/12修正達12/12一致” compresses three metrics into one baseline (completeness started 10/12; uniqueness and label started 11/12). Full correct figures do appear in Ch.10/表10-1/表10-2, so this is imprecise wording, not an arithmetic error. |
| 5 | **Observation (sidecar, not DOCX)** | `sidecar\0060_R04_SYNTHETIC_REPLACEMENT_REGISTER.csv` facts SYN-0060-FACT-059…062 vs Table 12 rows 05–08 | Register still carries pre-R06 wording (“…待核”) where the body now reads “尚未確認”; the receipt’s `table9_2_values_match: true` therefore holds only under normalization. Also, the register faithfully registers the row-level misattribution of Finding 1 (both versions of the defect locations are registered as synthetic facts). Register integrity itself (hash/rows/SAMPLE/unique IDs) is fine. |

**Not found (checked):** forbidden placeholders (`待填|待核|空白表|保持空白|會後填寫` — zero hits in body), internal paths/SHA/CLI strings in body (zero hits), REAL-boundary breaches, arithmetic errors, code duplicates, requirement drift.

## (d) Relevant positive evidence

- **Authority (criterion 1):** 0060 = I14-E01 = checkbox 065 verified from SHA-verified mapping JSON; official text quoted verbatim in Ch.2 P12; page 5 confirmed. Adjacent 0061–0064 official checkbox texts match the document’s boundary descriptions in Ch.2 P13, Table 3 (表2-1) and Table 18 (表12-1) — no drift, no scope creep (0061 archive system / 0062 filing & locating / 0063 query / 0064 retrieval speed correctly excluded).
- **Targeted repair (criterion on R07):** exact cell text matches the repair receipt `new_cell_text` byte-for-byte; no other artifact needed — confirmed in `document.xml` and PDF p.20.
- **Genre & usability (criterion 2):** title-blind identifiable — Ch.1 (P4–P8, PDF pp.1–2) states purpose, four-pillar mechanics, SAMPLE boundary, navigation. A volunteer administrator can classify (Table 5/表4-1 12-type dictionary with inclusion/exclusion/errors; Table 15/表11-1 filled worksheet), decide accept/correct/return/HOLD/reject (Table 4/表3-1 five branches; Table 16/表11-2: HLD-001/REJ-002/HLD-003/REJ-004 with stated reasons), and obtain the second-person check (Table 10/表8-1 procedures 1–6; “no self-review” rule in P8, P64, P66).
- **Operational completeness (criterion 3):** all present and populated — 12 types (Table 5, PDF p.5), PDDRO matrix (Table 6, p.8), 9-segment grammar + 3 parsed examples (Tables 7–8, pp.9–10), 11 metadata fields (Table 9, p.12), 4-role/6-procedure SOP (Table 10, p.14), 12 paired worked examples (Tables 11–12, pp.15–20), decision/hold/reject flow (p.4, p.24), correction trail (Table 14, p.21), metrics (Table 13, p.21), real-data replacement checklist (Table 17, p.24, 7 steps).
- **Row-level lineage (criterion 4):** all 8 specified repaired links verified *in both* 表9-1 and 表9-2 row-by-row: RSC05→依附003、004; ATT06→依附003; DLG07→依附003、004; ASM08 denominator explicitly checked against 06 (“10人評量母體與06簽到的10人到課數相符”) + 依附003、004、006; FDB09 10-issued-forms tied to 06 + 依附003、006; FUP10 10-person cohort tied to 06 + 依附003、006; EXC11→依附005、006、007 (duplicate/label/locator); IMP12 formation “綜合09…11…” + 依附009、010、011 (Table 12 row 12, p.20).
- **Arithmetic (criterion 5, independently recomputed):** all correct — 10/12=83.3%, 8/9=88.9%, 8/9=88.9%, 8/10=80.0%, 6/8=75.0%, 11/12=91.7%, 10/12=83.3%, 11/12=91.7%, 12/12=100.0%. Denominators match described cohorts (assessment uses valid 9 of 10 attendees — never all 12; feedback uses 9 valid forms; record metrics use all 12). 12 codes occur exactly once (SEQ 001–012, each of 12 TYPEs exactly once, all 9-segment).
- **Evidence boundary (criterion 6):** Table 1 declaration (p.1) covers SAMPLE/SYNTHETIC, UNKNOWN org state, PUB/INT/RST as admin labels only, S3 unapproved, HOLD-mandatory; all 12 表9-2 rows “SAMPLE／桌面演練，未生效”; header/footer marker “候選工作稿｜SAMPLE/SYNTHETIC示範｜非本會核定或實績” present in header1.xml/footer1.xml and on rendered pages; P14 UNKNOWN statement; P88 self-report limitation; Ch.12 pre-adoption checklist. No prohibited real-operations/approval/personnel/legal claims found.

## (e) Scope limitations

1. **No direct visual inspection.** This model cannot ingest PDF or page images (the two attached PDFs errored accordingly — flagged per instructions). Page locators come from programmatic text-layer extraction (pypdf) of the 26-page Word-export PDF, not from viewing page images. Layout, font-size floors (10.5/9.5 pt), table overflow and visual readability were **not** assessed by me; the coordinator visual receipt (SHA verified) is layout-only and I did not treat it as semantic evidence.
2. **Official source PDF content unread directly** — SHA `805386B7…` verified by hashing only; official checkbox text and adjacent checkboxes verified via the SHA-verified mapping JSON plus the document’s own quotations.
3. **No re-render:** I relied on the render manifest (SHA verified) binding candidate SHA `04464519…` to PDF `BDEC349D…`, 26/26 pages.
4. Blueprint trace was mechanic-by-mechanic against every Blueprint-mandated section/table, not a literal sentence-by-sentence diff of all Blueprint prose.
5. Sidecar registers examined for hash/row/status integrity and spot-checks, not fully re-audited.
6. Page numbers are text-layer derived; treat ±1-page uncertainty for tables spanning page breaks.

**Bottom line for the coordinator:** R07’s authorized repair is correct and verified, but fresh review found a Major row-level contradiction (表9-2 rows 05/06/07/08 vs Ch.10/表10-2, PDF pp.18–21) and a Moderate grammar violation in 表11-1’s output code (PDF p.23). Both are narrowly repairable in a single new revision (4 cells + append `-V01`), which would require a fresh exact-SHA review.


### Full R07 coordinator adjudication

# Coordinator adjudication — DOCX 0060 R07

## Exact-SHA review binding

- Candidate SHA-256: `044645199B2D704760D3F8729593641EBE54EBF58CB583ABDC026FA355A69286`
- Review packet SHA-256: `C51E7A9E0D9ED8EF137F12CE84EC9CD3C4505384ACF2537652E43C4B13A13584`
- Reviewer: requested `opencode/mimo-v2.6-flash-free` through OpenCode v2 `opencode v2.0.29`; no Computer Use.
- Attempt 03: provider internal/Nvidia HTTP 503 upstream overload, exit 1; original stdout retained.
- Attempt 04: exit 0, duration 709.257 sec, stdout SHA-256 `BAA7D52E6C9BC8C3C7983926AAD1DAE295681FD8B7E125C0E784E29AA259A3FE`, stderr empty; candidate SHA before/after unchanged.
- Independent reviewer verdict: **PARTIAL**.

## Coordinator verification of findings

I verified the reviewer’s R07 findings against the DOCX, official Blueprint, Table 14 correction trail, and synthetic register:

1. **Major, confirmed:** Table 12 rows 05–08 contradict the fixed defect ownership recorded in Table 14: RSC 005 had the duplicate sequence; DLG 007 had the missing locator; ATT 006 had the wrong INT/RST label; ASM 008 had no corresponding repair. Table 12 currently assigns the defects to RSC 005 (locator), ATT 006 (duplicate), and ASM 008 (label), while omitting the DLG correction. This is a real row-level cross-reference defect.
2. **Moderate, confirmed:** Table 15, final row, emits `TT-2026-SYN60A-DO-ATT-RST-S3-006`, which is missing the required ninth version segment `-V01`; the document’s code grammar and 12 paired examples include that segment.
3. **Minor Blueprint gap, confirmed:** Unique Blueprint R01 SHA-256 `166B9D45E439ACD979A59B1ED95F343BC8153D3BC8A7C8E3FF65BD966AD1CA74`, line 65, requires zero-denominator/no-in-scope data to show `N/A` and never report 100%. R07 has no N/A or zero-denominator rule in the body.
4. **Register mismatch, confirmed:** `SYN-0060-FACT-055` through `-066` values are not exact copies of R07 Table 12 rows; the synthetic register still uses old wording. Its previous technical check compared against the R04 content JSON rather than the current DOCX, so that PASS did not establish current body/register parity.
5. **Minor wording, confirmed:** Table 12 row 11 compresses three separate baselines into “10/12”; Table 14 and Table 13 show unique-code 11/12, complete fields 10/12, label match 11/12.

R07’s targeted repair removing the `12 IMP | ` prefix is verified correct. The independent R07 reviewer could not directly inspect images, but coordinator visual review independently inspected page 20 and the inherited page-coverage chain. This scope limitation does not invalidate the semantic findings above.

## Disposition and narrow repair

**Coordinator disposition: PARTIAL / R07 not accepted.** The independent response’s positive findings are preserved, but the three semantic/Blueprint gaps and register mismatch prevent semantic acceptance.

R08 will correct only the four Table 12 defect-conclusion cells, clarify the row 11 baseline, append `-V01` to the filled worksheet output code, add the zero-denominator N/A rule to the metric procedure, and synchronize the 12 affected synthetic register values to the exact DOCX rows. No real evidence, association approval, signature, or official acceptance will be added. The exact R08 SHA requires new technical, full render/visual delta, and independent semantic QA.


## R08 targeted repair receipt

```json
{
  "doc_id": "0060",
  "requirement_id": "I14-E01",
  "official_checkbox": "065",
  "source_revision": "R07",
  "candidate_revision": "R08",
  "source_sha256": "044645199B2D704760D3F8729593641EBE54EBF58CB583ABDC026FA355A69286",
  "candidate_sha256": "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3",
  "candidate_bytes": 71613,
  "changed_ooxml_parts": [
    "word/document.xml"
  ],
  "other_package_parts_byte_identical": true,
  "zip_testzip_error": null,
  "python_docx_opened": true,
  "targeted_text_changes": [
    {
      "locator": "Table12 row05 conclusion",
      "old": "本報告內合成桌面檢核：初始定位缺漏已修正，欄位齊備。核對資源項對應04配置；實體場地與設備可用性尚未確認。",
      "new": "本報告內合成桌面檢核：初始重複碼已修正，RSC樣張代碼流水號由004更正為005；12筆代碼均唯一。核對資源項對應03與04；實體場地與設備可用性尚未確認。"
    },
    {
      "locator": "Table12 row06 conclusion",
      "old": "本報告內合成桌面檢核：初始重複碼已修正，標記唯一。核對人數邏輯閉合；RST僅為樣本處理標籤無真實個資，真實名冊來源、處理權限及實際簽到資料均未確認。",
      "new": "本報告內合成桌面檢核：簽到名冊情境原先誤標INT，已更正為RST；12報名、10到課、2缺席數量閉合。RST僅為樣本處理標籤，不含真實個資；真實名冊來源、處理權限及實際簽到資料均未確認。"
    },
    {
      "locator": "Table12 row07 conclusion",
      "old": "本報告內合成桌面檢核：日誌節點完整對應03與04進度，必填欄合規。核對節次相符；非真實紀錄，實際授課、紀錄來源與負責角色均未確認。",
      "new": "本報告內合成桌面檢核：初始缺少來源存放定位，已補入LOC-REC-2026-0815B；日誌節點對應03與04。非真實授課紀錄，實際授課、紀錄來源與負責角色均未確認。"
    },
    {
      "locator": "Table12 row08 conclusion",
      "old": "本報告內合成桌面檢核：初始標籤不符已修正，與03課程計畫及04評量安排一致。核對10人評量母體與06簽到的10人到課數相符；RST僅為樣本處理標籤無真實個資，真實成效尚未確認。",
      "new": "本報告內合成桌面檢核：10名到課中9份有效評量、8人達標、1人未達標；與03課程計畫、04評量安排及06簽到10人母體相符。本列未另設缺陷修正；RST僅為樣本處理標籤，真實成效尚未確認。"
    },
    {
      "locator": "Table12 row11 conclusion",
      "old": "本報告內合成桌面檢核：記錄三項演練缺失修正歷程，示範資料已由10/12修正達12/12一致；非真實錯誤，實體稽核尚未確認。",
      "new": "本報告內合成桌面檢核：初始代碼唯一性11/12、必填欄位完整有效10/12、處理標籤相符11/12；更正後三項均為12/12。此為SAMPLE桌面演練設計，非真實錯誤；實體稽核尚未確認。"
    },
    {
      "locator": "Table15 final output-code cell",
      "old": "產出代碼：TT-2026-SYN60A-DO-ATT-RST-S3-006",
      "new": "產出代碼：TT-2026-SYN60A-DO-ATT-RST-S3-006-V01"
    },
    {
      "locator": "Chapter13 metric procedure paragraph",
      "old": "所有指標均依數學公式嚴格定義分子與分母，計算結果採四捨五入至小數點後第一位。各項比率之定義如下：代碼唯一性比率為「無重複之唯一代碼筆數 / 總登錄筆數」；中繼資料完整有效率為「各項必填欄位完整且格式合規之筆數 / 總登錄筆數」；處理標籤相符率為「處理標籤與文件機敏性質完全相符之筆數 / 總登錄筆數」。在演練初始階段，代碼唯一性為 11/12 = 91.7%，欄位完整有效率為 10/12 = 83.3%（第005筆因重碼未生效、第007筆缺漏定位），處理標籤相符率為 11/12 = 91.7%。經獨立第二人覆核提報缺失並填寫 EXC 表單更正後，三項指標均提升至 12/12 = 100.0%。",
      "new": "所有指標均依數學公式嚴格定義分子與分母，計算結果採四捨五入至小數點後第一位。各項比率之定義如下：代碼唯一性比率為「無重複之唯一代碼筆數 / 總登錄筆數」；中繼資料完整有效率為「各項必填欄位完整且格式合規之筆數 / 總登錄筆數」；處理標籤相符率為「處理標籤與文件機敏性質完全相符之筆數 / 總登錄筆數」。在演練初始階段，代碼唯一性為 11/12 = 91.7%，欄位完整有效率為 10/12 = 83.3%（第005筆因重碼未生效、第007筆缺漏定位），處理標籤相符率為 11/12 = 91.7%。經獨立第二人覆核提報缺失並填寫 EXC 表單更正後，三項指標均提升至 12/12 = 100.0%。若特定期間或範圍內沒有任何適用資料、分母為0，結果標示 N/A（不適用）並說明資料範圍；不得報100%。"
    }
  ],
  "forbidden_literals_remaining_in_docx_body": [],
  "register": {
    "source_register_sha256": "8355A495471E34CFF95CE57BE32CD65FC3EDEE18446DFEE76344000F6757D2C6",
    "candidate_register_path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\sidecar\\0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv",
    "candidate_register_sha256": "ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B",
    "previous_interrupted_register_sha256": "41638683BB6A71D668BBA388283B71CC4FEFBDC3D71E1D9B17A795CEEA850A14",
    "rows": 66,
    "unique_fact_ids": true,
    "all_doc_id_0060": true,
    "all_sample": true,
    "facts_055_066_exactly_match_R08_Table12": true,
    "forbidden_literal_hits": 0
  }
}
```

## R08 deterministic technical receipt

```json
{
  "doc_id": "0060",
  "requirement": "I14-E01",
  "checkbox": "065",
  "candidate_sha256": "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3",
  "candidate_bytes": 71613,
  "docx_sha_unchanged_during_check": true,
  "zip_testzip_error": null,
  "python_docx_opened": true,
  "heading_1_count": 12,
  "title_style_present": true,
  "content_sections": 12,
  "content_data_tables": 17,
  "content_data_rows": 129,
  "rendered_body_tables": 17,
  "table9_1_rows": 12,
  "table9_2_rows": 12,
  "table12_row_widths_valid": true,
  "table12_imp_formation_cell": "綜合09回饋、10追蹤及11三項桌面演練缺失，提出改善追蹤樣張；未核准、未執行。",
  "table12_imp_formation_cell_clean": true,
  "R07_semantic_findings_repaired": {
    "RSC05_duplicate_code_corrected_004_to_005": true,
    "ATT06_INT_to_RST_label_correction": true,
    "DLG07_source_locator_added": true,
    "ASM08_no_false_label_correction_claim": true,
    "EXC11_three_baselines_and_fixed_results": true,
    "Table15_version_segment_V01": true,
    "zero_denominator_NA_rule": true
  },
  "all_R07_semantic_findings_repaired": true,
  "all_12_codes_exactly_once": true,
  "table9_1_row_widths_valid": true,
  "table9_2_row_widths_valid": true,
  "lineage_checks": {
    "RSC_05_source_plan_and_lesson_03_04": true,
    "ATT_06_source_plan_03": true,
    "DLG_07_source_plan_and_lesson_03_04": true,
    "ASM_08_denominator_traces_to_attendance_06": true,
    "FDB_09_ten_forms_traces_to_attendance_06": true,
    "FUP_10_ten_person_cohort_traces_to_attendance_06": true,
    "EXC_11_links_duplicate_05_label_06_locator_07": true,
    "IMP_12_formation_and_source_links_09_10_11": true
  },
  "all_lineage_checks_pass": true,
  "register_sha256": "ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B",
  "register_rows": 66,
  "register_checks": {
    "all_doc_id_0060": true,
    "all_sample": true,
    "unique_fact_ids": true,
    "table9_2_values_match": true
  },
  "all_register_checks_pass": true,
  "recomputed_percentages": {
    "attendance_10_of_12": 83.3,
    "assessment_8_of_9": 88.9,
    "feedback_8_of_9": 88.9,
    "followup_8_of_10": 80.0,
    "self_report_6_of_8": 75.0,
    "unique_11_of_12": 91.7,
    "complete_10_of_12": 83.3,
    "label_11_of_12": 91.7
  },
  "recomputed_strings_all_present": true,
  "repository_hard_rule_literal_hits": [],
  "render_manifest": {
    "candidate_sha256": "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3",
    "candidate_unchanged": true,
    "pdf_sha256": "B9850431F0A002E788EC21B4432F47A4F8309E067759C3A7FAB6D95AD3B43BAB",
    "pdf_bytes": 872318,
    "page_count": 26,
    "rendered_png_count": 26,
    "pages": [
      {
        "page": 1,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-01.png",
        "sha256": "21AFC7A208D1AC79FE8FDE67E9AD9D1669890ADC332963475A4C6158C58475D8",
        "bytes": 424344,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1178,
        "blank": false
      },
      {
        "page": 2,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-02.png",
        "sha256": "8A5FF1217AAC94817A2DB8602A75A9D3C941BE309BC221C2CA589DA7F7752705",
        "bytes": 358280,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1094,
        "blank": false
      },
      {
        "page": 3,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-03.png",
        "sha256": "0F396E19200F5D1A40EDF3C7955E86ABD627C585FD41CF65E6F474F6E80F9597",
        "bytes": 302585,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 966,
        "blank": false
      },
      {
        "page": 4,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-04.png",
        "sha256": "D3BBB82C435F334947E3DC3AB336ACB7E30022F89EDB64D7784FE9E60FE8B93D",
        "bytes": 398677,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1098,
        "blank": false
      },
      {
        "page": 5,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-05.png",
        "sha256": "4EE8BD6A63B079C440C0893762BFEF71D620AC9CAF7D84BA53E94BB581C049FD",
        "bytes": 325497,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 954,
        "blank": false
      },
      {
        "page": 6,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-06.png",
        "sha256": "7A89A07B3C228E22B2F5502B87B18C8434E881E9D4C8C9E8A20E14175E084F18",
        "bytes": 253268,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 901,
        "blank": false
      },
      {
        "page": 7,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-07.png",
        "sha256": "9C0FB7B26F4BF3F767EA472A8B23509648F7F43EDB56AEADD661422E526C959C",
        "bytes": 281719,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 942,
        "blank": false
      },
      {
        "page": 8,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-08.png",
        "sha256": "A33A07AE97D926731BDF1F8A99FAE81F4A6935FDC33C0FCE35BDFD919947172F",
        "bytes": 320735,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1014,
        "blank": false
      },
      {
        "page": 9,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-09.png",
        "sha256": "F53ABD1A1CA0BFFC376D58D242F14F2B8FEFEF962AEDD4C02C9D3AAF180687AD",
        "bytes": 307840,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1027,
        "blank": false
      },
      {
        "page": 10,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-10.png",
        "sha256": "1623D66BBD4B91F398BDAD5088A0958A50AABD6193654869352ECDA963CACB97",
        "bytes": 209207,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 950,
        "blank": false
      },
      {
        "page": 11,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-11.png",
        "sha256": "BB07EE63499FA86FEA67BA3F438A7CED60200CEC7BA16647C6EEEA8D340395D9",
        "bytes": 272695,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 944,
        "blank": false
      },
      {
        "page": 12,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-12.png",
        "sha256": "FA683432DCD864B6212A4888469F7C7594800C8B98AFF67F56201A80E57F6B0A",
        "bytes": 199603,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 876,
        "blank": false
      },
      {
        "page": 13,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-13.png",
        "sha256": "3A7ABAC6B6F14FE3F35159C779A1FA00A042B60C6D26B50DDDADF714EBA030ED",
        "bytes": 346726,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1043,
        "blank": false
      },
      {
        "page": 14,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-14.png",
        "sha256": "0A65E96E551DA61AC66892A40BCF717CE69DFE61ECD7D9E65D5D3EF47E4E6FA2",
        "bytes": 282873,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 867,
        "blank": false
      },
      {
        "page": 15,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-15.png",
        "sha256": "9B936EFA0DE1C889C92C74892703F8D4A8A4377B9B11D5F985E628B4DD4A5774",
        "bytes": 345054,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1318,
        "blank": false
      },
      {
        "page": 16,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-16.png",
        "sha256": "5B71FD159434060435FDBAEB0E72ED8A93866080614480AD7BD48F7F4FA5FEEC",
        "bytes": 214158,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1134,
        "blank": false
      },
      {
        "page": 17,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-17.png",
        "sha256": "BF4F31014F4F93C0D060778C9271442800EA76726D13C93F10D7DFCF6CA8F3A2",
        "bytes": 241850,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 960,
        "blank": false
      },
      {
        "page": 18,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-18.png",
        "sha256": "19C2B3DE434796175361DAFFC4F4D7B1709E7AD6A1F96B297EB720D494F57204",
        "bytes": 228848,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 821,
        "blank": false
      },
      {
        "page": 19,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-19.png",
        "sha256": "EC180CD605E53B6AA4C5079D4EEC6FB5704E84453CB0B8648C7D86A1B3E3CAFD",
        "bytes": 240235,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 894,
        "blank": false
      },
      {
        "page": 20,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-20.png",
        "sha256": "20E0A132BB33CED9253CE0C114E75DA78B58C071D05018D967FA6402586BE78D",
        "bytes": 394738,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1219,
        "blank": false
      },
      {
        "page": 21,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-21.png",
        "sha256": "7D771E897BA6E4F2261681094DD447FADBC09F5DFB5A9C6651A5874240FD2FA9",
        "bytes": 268066,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1078,
        "blank": false
      },
      {
        "page": 22,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-22.png",
        "sha256": "48F1A5AAC35BDD5D6F1CBD808E451666F9551811BAEB93990F6CBC4F8C1FB381",
        "bytes": 352127,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1117,
        "blank": false
      },
      {
        "page": 23,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-23.png",
        "sha256": "DDDE0FA14ADD64958DA92BD9CD43CB7CA30D2ED2DB3CE95B1660A9E8C47108DD",
        "bytes": 225702,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 763,
        "blank": false
      },
      {
        "page": 24,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-24.png",
        "sha256": "E25F668C09FC0491C2360C9A10EB47B5BBCF3BD77CFFB320929DA81849C370BA",
        "bytes": 291670,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1032,
        "blank": false
      },
      {
        "page": 25,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-25.png",
        "sha256": "127C7CE3CFF56FEF489E5DBC25AF5D4AB6E6126CF94C98199C54C322E6C1AF58",
        "bytes": 389867,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 1119,
        "blank": false
      },
      {
        "page": 26,
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\page-26.png",
        "sha256": "D6FCB7D6113C0512D44924E15DFF5B695BCC64644A4D46301C80CCB94E714FDC",
        "bytes": 192467,
        "width": 1013,
        "height": 1432,
        "extracted_chars": 632,
        "blank": false
      }
    ],
    "contact_sheets": [
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-01-04.png",
        "sha256": "50B2418FF202F75874C42B61039530BBD14B553838CE4B457095FCF33861CA09",
        "bytes": 1720201
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-05-08.png",
        "sha256": "B0CDADF70EDF79166F181363FC8A160F3A33F8DB572BF0B0205DD7F186DFE714",
        "bytes": 1366695
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-09-12.png",
        "sha256": "6312DCF993540A0D4F2FFAF417D1C086B802639E032DCCE168B93C0937A0E7FA",
        "bytes": 1187297
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-13-16.png",
        "sha256": "34EA71D314725471450E930BC1B7C7742E9E4111FD8450E13CAAF8195EEF30E0",
        "bytes": 1388190
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-17-20.png",
        "sha256": "4D1EA08EBC70BC04D561D8BDDFDBA1E172B564E6C5B7B91527DCDF4F0D9836ED",
        "bytes": 1237379
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-21-24.png",
        "sha256": "FC2A4AB1225C7A1637AEE9F56DBBF3BDE31A7061495C79B02E3C40F42532FD61",
        "bytes": 1327328
      },
      {
        "path": "E:\\TTQS\\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\\docs\\ttqs-quality-20261016\\quality-review\\0060_R01\\evidence\\render_R08\\contact-25-26.png",
        "sha256": "C2155F5D33F9328D9B2697AFA833CA635F25E1EAEC70DAFF3565A878F5193355",
        "bytes": 690070
      }
    ],
    "renderer": "Microsoft Word COM PDF export + bundled PDFium rasterization",
    "rendered_at_utc": "2026-10-18T00:37:58.581801+00:00"
  },
  "checked_at_utc": "2026-10-18T00:38:34.659185+00:00",
  "scope": "Deterministic structural, exact code, row-level lineage, register, arithmetic-string checks; not independent semantic acceptance."
}
```

## Full document-specific Unique Blueprint

# DOCX 0060 唯一 Blueprint R01

## 身分與官方需求
- 專案：TTQS_ONE。
- DOCX deliverable_id：0060。
- 唯一需求：I14-E01；官方方框流水號：065；《TTQS查核佐證文件資料表—訓練機構版》第5頁。
- 官方原文：「訓練資料與訓練過程及成果的紀錄與分類，均有系統化歸納方法編碼。」
- 既有序列的文類標籤：analysis_report。
- 本件唯一命題：訓練規劃、設計、執行、檢討、成果資料能按一致、可核對的分類字典與編碼規則歸類；分類結果能讓行政志工按來源、課程案例、生命週期、資料種類、處理敏感度及保存規則識別資料，不需要讀者猜碼。
- 讀者任務：行政志工取得一件訓練資料時，能判斷是否屬訓練紀錄、選唯一主類與PDDRO階段、產生不含個資的唯一代碼、填完必要中繼資料、發現例外時停在HOLD並留下處理軌跡。

## 權威來源與精確識別
- Human Mission：01_HUMAN_MISSION_AND_ACCEPTANCE.md SHA-256 CE228E4B8697E6E54AD48733F2AED2BCFD09CFF625D99F1F0AEABB45E440C6E7。
- 逐指標寫作手冊：02_GENRE_WRITING_MANUAL.md SHA-256 0F4183A18E5668260B213B35AE223A7DA334EED56A25B6FEF72E2D6D7E12E649；I14分類編碼要求文件類型、處理敏感度、保存規則及實例。
- 157方框 Blueprint：03_157_CHECKBOX_BLUEPRINTS.md SHA-256 7732C40F25D0803F18836725D1634EBE72A156925444F3EA9915B6168CC1A70A；I14第065格要求分類/編碼多種類別、敏感級別、保存年限，含核心正文/示範、決策/結果與事實連結。
- 正式需求對照：quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json SHA-256 4004B7C2F574606BE520E016ACE7377AEFDE3A978003ADDA303CC9A05326440D；0060＝I14-E01、analysis_report、官方表第5頁。
- 官方佐證資料表來源 PDF：quality-review/0058_R01/review/opencode_v2_semantic_R05/inputs/official/official_evidence_table_source.pdf SHA-256 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709；第5頁該格原文及相鄰格已擷取在同目錄 official_evidence_table_fulltext.txt 第440–444行。
- 歷史142序列表：送審資料/05_填表建議_方法示範不等於實績/142份文件逐項檢查與填表建議.csv SHA-256 166EB3CD3D8026206E88F06CB083AA162D2DDD464D53883A3CE5AC411ADCEA6A；0060列明「先不要勾為完整紀錄」、正文尚有主要紀錄待補、未確認完整實際證據、本次未逐頁核對。
- 對照的唯一歷史文件：送審資料/02_既有整套文件_歷史版本未重新驗收/1599_0060__I14-E01__01__訓練資料與訓練過程及成果的紀錄與分類，均有系_可直接使用成品.docx SHA-256 2742D42A9C3FE09E5B94674B89276EADD1646E445330015C149A0C0AA5C7799E；本地核對為22個正文段落、14個表格，含多處「待核/待實測/待填」；只用作歷史缺陷證據，不得複製或改標題重用。
- 協會歷史訓練品質手冊：送審資料/屏東縣原始點關懷協會_訓練品質管理系統手冊_評核說明版.docx SHA-256 0BC88451F964C7F96497D036B9713DD7CE547823A70F5A2A06924C558F406EFF；來源頁標註2026-10-05且明確區分已知現況/建議做法/虛擬填寫示例。僅供情境定位，不能據以宣稱2026-10-18現況或法定事實。本文採低維護、角色而非虛構人名的設計。

## 文類及邊界
- 文件角色按映射為analysis_report；用「訓練資料分類與編碼方法、完整SAMPLE操作案例及落地檢核報告」完成。
- 0061＝I14-E02檔案管理系統（索引、權限、檢索、備援）；0062＝I14-E03需求到成果文件建檔資料及真實定位；0063＝I14-E04查詢功能及持續改善；0064＝I14-E05系統化程度/檢索速度。只用一小段說明界線，不把它們的交付物併入0060。
- 本件不聲稱已有協會採用制度、資料庫/ERP、已配置權限、已備份、已做檢索測試、已核准保存年限或已辦訓。
- 所有課程、角色、日期、代碼、數據、例外與決策均為SAMPLE/SYNTHETIC；使用虛構角色稱謂與代碼，不用真實姓名、學員個資、外部講師證明、簽名或協會核定語氣。
- 協會現行法人/人力/權責及訓練資料現況未以本件來源確認，保持UNKNOWN。章節中提供候選操作設計，不預填正式核准人/生效日。
- 敏感度代碼是本案示範的行政處理標籤，非法律等級、個資法定類別或公開許可。保存碼S3僅為SAMPLE中的假設，不是法令規定/本會保存決定；實際採用前依適用法規、補助/契約、同意、原始來源與有權決議核實；無法確定者用HOLD並不得銷毀。

## 唯一案例與固定數據
- case_id=SYN-0060-2026-A01；課程示範名稱「社區志工接待與資源轉介界線」；僅為合成情境，不代表協會已開課。
- 示範課程日2026-08-15；30日追蹤日2026-09-14；合成樣本報名12人、到課10人、缺席2人；出席率10/12=83.3%。
- 到課10人中9人完成有效評量、8人達標、1人未達標；有效評量通過率8/9=88.9%；不得以全體報名者為分母替代。
- 到課10人發出回饋表10份、取得9份有效表；其中8/9將清楚度評4或5分=88.9%。
- 追蹤對象10人、回覆8人、其中6人自述使用一項課程工具；回覆率8/10=80.0%；僅回覆者中的自述比例6/8=75.0%，不能宣稱已證實行為或組織成效。
- 樣本資料集共12筆；初始檢核：唯一代碼11/12=91.7%、全部必要欄位有效10/12=83.3%；發現1組重複碼、1筆缺來源定位、1筆敏感度標籤不符。修正後：12/12唯一、12/12必要欄完整、12/12處理標籤相符，均100%。這是刻意設計的SAMPLE桌面演練，不是實際稽核或系統運行結果。
- SAMPLE保存規則S3：假設課程結束後3年，示例日期2029-08-15；不可當成真實保存期限或法令意見。

## 專屬分類字典與編碼語法
- 代碼語法：TT-[YYYY]-[CASE]-[PHASE]-[TYPE]-[ACCESS]-[RET]-[SEQ]-V[NN]。
- TT訓練紀錄識別；YYYY為文件建立年；CASE為不含身分的課程/案件代碼；PHASE僅P/D/DO/R/O；TYPE由受控字典選；ACCESS僅PUB/INT/RST行政處理標籤；RET為已核對的保存規則識別，示例S3/HOLD；SEQ為同一案例中流水號；VNN為版本序號。禁止將姓名、生日、電話、身分證、疾病/病歷置入任何代碼。
- TYPE字典：NEE需求來源、NAN需求分析、PLN課程計畫、LSN教學設計、RSC資源確認、ATT出缺席、DLG教學過程、ASM學習評量、FDB學習者回饋、FUP訓後追蹤、EXC分類/編碼異常、IMP改善追蹤。每一碼有唯一中文名稱、納入例、排除例與常見錯分。
- ACCESS：PUB=已核實可公開的去識別版本；INT=一般內部管理資料；RST=包含識別資料或其他需限制接觸的資料。任何代碼不授予存取權。示範資料雖使用RST也不含真實個資。
- RET：實際使用前先判定適用來源與起算事件、複核者/決議依據及合法處置；來源不明用HOLD，不得猜年限或刪除。S3僅sample。
- 12筆案例碼按上列語法、TYPE與資料敏感性產生；其中個別名冊/評量資料RST，其餘去識別摘要INT。
- 必要中繼資料至少10項：record_code、case_id、title、phase、type、created_date、source_origin、access_code、retention_rule_id、status、source_locator、version/relation（可拆欄但須齊全）。以「欄位完整且值有效的筆數/範圍內紀錄數」計算完整率。

## 正文專屬大綱與必備內容
1. 第一頁30秒導讀：對準I14-E01/方框065，這份報告的唯一用途、如何照做、合成與真實界線、正文快速導航。
2. 適用範圍及WHAT/NOT：分類編碼的管理目的；不知道現況的地方明確標UNKNOWN；與相鄰四格的職責界線。
3. 分類判斷流程：先定範圍和來源→判PDDRO階段→選唯一主類與型別→判處理敏感度→找有來源的保存規則→生成並唯一性檢核→覆核/記錄；異常分支含類別不明、來源/授權不明、個資/敏感資料、缺保存依據、重複碼/版次錯誤。
4. 完整分類字典：至少12個TYPE代碼、納入/排除邊界、PDDRO對應及一項易錯案例；另有PDDRO五階段矩陣和分類多軸決策表。
5. 編碼語法與欄位字典：每段格式、長度/字元限制、唯一性範圍、日期/序號/版次、改版保留、個資禁止；逐欄解釋必要中繼資料。
6. 角色與日常程序：小型志工組織角色稱謂模板，不捏造現任職員；逐步寫清入口、處理時間點、執行、第二人覆核、輸出、記錄、例外與退回條件。
7. 12筆完整SAMPLE資料：上列12種檔案各提供日期、完整示範編碼、題名、來源/形成方式、PDDRO、類別、ACCESS、RET、狀態、檢核結論與交叉引用。逐列實際對應同一case_id並清楚標SYNTHETIC。
8. 數值與異常案例：重複碼、缺source_locator、敏感度錯標的發現、最小修正、改前/改後清冊；按固定分母重算唯一率/完整率/適當標籤率，解釋限制。
9. 使用者可直接抄用的實務表格：分類編碼登錄列樣本（完整填好）、單件分類決策記錄樣本、HOLD/退件條件與處置表、真實替換核對清單。不得只給空白表，完整示範為主。
10. 落地採用界線：需真實核對的資料與權責、核定前可做的安全準備、正式使用禁止事項；不把樣本編碼寫回正式原件。
11. 實質結論：本案展示的方法如何覆蓋訓練資料/過程/成果，哪些項目仍是候選/示範，下一個可逆行動及不能宣稱的結果。

## 公式、退件門檻及獨立檢核
- 唯一代碼率=範圍內不同有效現用代碼數/範圍內紀錄總數*100%；同一碼有兩筆即至少一筆未唯一。
- 必要欄位完整率=完整有效必填欄位紀錄筆數/範圍內紀錄總數*100%。
- 標籤相符率=敏感度/ACCESS判定與資料實際內容相符的筆數/範圍內紀錄總數*100%。
- 無範圍內資料時分母為0，標示N/A並不得報100%；百分比保留一位且寫分子分母。
- 任一個案碼帶出個資、同一筆重複現用碼、來源無法說明、保存規則無依據卻可刪除、已作廢/範例標作現行正式、SAMPLE誤稱真實均為拒收。
- 成品必須讓標題盲測者能辨認這是分類/編碼方法與示範報告；不能誤判為0061檔案管理系統、0062原件清冊、0063查詢改善、0064檢索速度報告。
- 保留一張明確標為SAMPLE的完整登錄表；另附可供實際抄用的空白新紀錄行只有在完整SAMPLE示例同時存在時才可出現。所有訓練案例事實須建立Synthetic Register。

## 輸出與隔離
- 唯一Writer：Antigravity CLI；只請求gemini-3.8-flash-high，禁止Computer Use/UI/瀏覽器、禁止--dangerously-skip-permissions、禁止網路新資料、禁止讀寫其他文件包。
- 交付：candidate/0060_R01.docx、sidecar/0060_R01_SYNTHETIC_REPLACEMENT_REGISTER.csv、worker/antigravity/0060_R01_build.py與worker/antigravity/0060_R01_builder_receipt.md；原生stdout/stderr/exit另存於worker目錄。
- DOCX本體使用台灣繁中；A4直式、11pt內文、表格至少9.5pt；標題/章節黑色，表格標題列清晰，重複跨頁表頭與足夠內距，頁尾頁碼。可用Python python-docx，執行本機bundled Python絕對路徑。
- DOCX正文不得出現內部路徑、工程SHA/Blueprint鍵值/CLI紀錄。頁眉/頁尾持續標示「候選工作稿｜SAMPLE/SYNTHETIC示範｜非本會核定或實績」。
- 生成後不自評PASS。交給Codex確定性技術檢查、實際render與頁面目視，再交不同Writer之OpenCode v2 free SKU做exact-SHA獨立語意審查；錯誤只精確修復該件。


## Full text extracted from exact R08 DOCX

Every non-empty paragraph and every table row below is extracted from the exact SHA identified above. Verify against the attached DOCX/PDF.

訓練紀錄與成果分類編碼系統化歸納方法分析報告
TTQS 訓練機構版 I14-E01（佐證表方框 065）草案規劃與示範作業分析
第一章 30秒導讀與系統化歸納編碼總覽
本報告旨在為人力與資源精簡之志工團體與小型辦訓機構，研提一套兼顧實務操作性、稽核追溯性且完全不含個人機敏資訊之訓練紀錄分類與編碼草案體系。透過一致的分類字典與結構化編碼規則，協助第一線執行人員對各階段訓練表單進行型別判斷、代碼賦予及中繼資料記載，確保每筆訓練資料均能連結至特定專案與 PDDRO 訓練流程。
本草案架構由「PDDRO 五階段架構」、「十二種文件型別字典」、「九段式語法編碼」以及「十一項中繼資料欄位」共同構成。為具體展示實務運作，本報告採用示範專案 SYN-0060-2026-A01 作為桌面演練案例，提供自需求分析、課程設計、執行簽到至成效追蹤之完整 12 筆示範樣本，並納入三項刻意設計之桌面演練作業缺失，具體呈現覆核查驗與指標修正軌跡。
指標定位：本文件對應 TTQS 訓練機構版 I14-E01（方框 065），聚焦於分類歸納方法與不含個資識別代碼之建立，屬於候選規劃草案。
個資防護：嚴禁將學員姓名、身分證字號、電話、生日等個人直接識別資訊編入代碼，涉及個別名冊或評量之文件一律標記 RST 行政處理標籤。
審查機制：規劃由登錄人員進行初編，再由另一人員進行第二人獨立核對；兩人功能可由現有人力調配兼任，但不得自行核對自身經辦之紀錄。
表 1-1：系統化歸納與編碼草案核心要素速查表
第二章 官方需求、指標邊界與未知現狀界定
依據勞動部勞動力發展署 TTQS 訓練機構版評核指標 I14-E01（佐證表方框 065）之官方規定，評核重點為「訓練資料與訓練過程及成果的紀錄與分類，均有系統化歸納方法編碼」。此項指標之目的，在於檢視機構是否具備一致且具邏輯追溯性之分類歸納方法與識別代碼，以利訓練歷程之整理與管理。
為維持指標佐證界限之嚴謹性，本文件在此明確劃定本報告（0060）與相鄰四項指標（0061 至 0064）之官方職掌範圍：0061 對應 I14-E02（檔案管理系統），負責建立整體檔案管理架構；0062 對應 I14-E03（完整文件建檔資料及真實定位），負責完整訓練文件建檔、來源憑據與實質定位證據，非僅限於實體檔案櫃；0063 對應 I14-E04（查詢功能與持續改善），負責建立查詢功能與檢索作業之改善機制；0064 對應 I14-E05（系統化程度及檢索速度），負責評定系統化程度與調卷檢索之響應速度。本報告不涉及未經官方界定之伺服器架構、資料庫行為或特定倉儲設備。
本報告明確陳述：本會目前之法人治理編制、專職人力現況、歷史訓練卷宗總量、資訊系統現況及正式檔案保存期限，目前皆處於未知（UNKNOWN）狀態。本報告僅為建議性分析草案，不代表本會已完成建置，亦不取代正式決策核定程序。
官方指標定位：DOCX 0060 專責對應 I14-E01（方框 065），文類屬於包含分類編碼規則與示範案例之分析報告（analysis_report）。
負向邊界隔離：本文件不撰寫檔案系統使用手冊（0061）、不建構全機構建檔總清冊（0062）、不開發查詢介面（0063），亦不執行調卷速度測驗（0064）。
現狀客觀隔離：不預設組織已採購特定資訊軟體或具備完備法規，所有演練均以紙本或基礎試算表皆可運作之最小可行模型進行規劃。
表 2-1：TTQS I14 系列指標官方範疇與本案邊界界定表
第三章 分類編碼作業流程決策樹與退件/凍結分支
為使小型志工組織在有限人力下能有序執行分類編碼，本章提出標準作業決策路徑。當收到各類訓練表單時，依序進行下列檢驗：表單來源與形式完整性查驗 -> 機敏個資檢驗與去識別化 -> PDDRO 訓練階段與型別判定 -> 結構化編碼賦予 -> 中繼資料清冊登錄 -> 獨立第二人覆核確認。任一關卡若發現未符標準，立即啟動退件補正或暫緩凍結（HOLD）程序。
決策流程包含三項核心分支路徑：第一分支為「機敏個資防護分支」，凡表單載有未經授權之學員身分證號、病歷或私人聯絡資料，應退回原辦理人員進行去識別化，若屬必要簽到或評分名冊，則必須標註為 RST 行政處理標籤，代碼中嚴禁置入個資；第二分支為「型別歸屬爭議分支」，若單一表單兼具多種性質，應按實質主要產出標的歸類或拆分為獨立表單賦碼，不得創設複合型別；第三分支為「保存年限未明分支」，若文件之法定或合約保存期尚無法證實，保存欄位一律填記 HOLD，嚴禁銷毀，直至查明適用法規依據並由權責單位正式決議後始得變更。
入口查驗：確認表單為訓練過程中實際產生之紀錄，空白或未完成填寫之表單逕行退回補正。
個資隔離：文件代碼及中繼資料嚴禁包含個人身分資料，涉及個人識別細目或個別評量結果之表單以 RST 標籤管制。
補正原則：登錄或覆核時發現格式、代碼或中繼資料有誤，退回原處理人更正後再行覆核。
HOLD 凍結原則：法定或合約保存年限未經查實前，一律標定為 HOLD 並禁止銷毀，不得擅自依經驗推定處置。
表 3-1：分類編碼作業異常情境、決策分支與處置原則表
第四章 十二種訓練文件型別定義字典
為避免不同人員因認知差異造成分類混淆，本體系規劃涵蓋訓練全歷程之「十二種標準文件型別字典」。每一型別均訂定三碼大寫英文字母代碼、中文名稱、對應之 PDDRO 階段、明確納入範圍、排除範圍，以及常見之錯分防範要點。
實務作業時應嚴格依據文件之「實質內涵」進行歸類，而非僅憑文件表面名稱。例如課堂當日助教填寫之過程記錄為 DLG（教學過程紀錄），不得誤編為 LSN（教學設計）或 ASM（學習評量）；結訓當下學員填寫之主觀心得問卷為 FDB（反應回饋），課後隔一段期間之實務行為調查則為 FUP（成效追蹤），兩者層次不同，不得混淆。任何分類疑義均以本字典之納入與排除標準為準。
型別單一原則：一份獨立紀錄僅配賦一個型別代碼，不使用複合代碼或斜線代碼。
實質重於形式：依文件記載之實質內涵判定型別，若名為「綜合報告」但實為簽到退資料，應歸入 ATT。
異常獨立登錄：分類錯誤、重碼更正及退件修正之紀錄，統一歸入 EXC 型別留存軌跡。
表 4-1：十二種標準訓練文件型別定義字典
第五章 PDDRO 訓練五階段分類矩陣
TTQS 體系以 Plan（規劃）、Design（設計）、Do（執行）、Review（查核）及 Outcome（成果）五大階段為管理骨幹。為使各項訓練紀錄具備明確之生命週期定位，本章研擬 PDDRO 訓練五階段分類矩陣，說明各階段之核心目標、所屬文件型別、生命週期觸發時點及查核重點。
五大階段依序銜接且互為勾稽：規劃階段（P）確立培訓需求與目標；設計階段（D）將目標轉化為計畫、教材並確認教學資源；執行階段（DO）記錄授課現場之出缺勤與互動歷程；查核階段（R）評估學員學習成效與滿意反應，並針對行政與代碼異常進行排錯；成果階段（O）則延伸至課後實務應用追蹤與制度面持續改善。藉由此矩陣，經辦人員得依表單產出之時點與目的，精確指定其所屬階段代碼。
階段代碼縮寫：規劃期為 P、設計期為 D、執行期固定使用 DO（以避免與 Design 之 D 混淆）、查核期為 R、成果期為 O。
流程銜接性：查核階段發現之缺失或未達標項目，應於成果階段之 IMP 型別中研擬具體改善方向，形成閉環管理。
分工原則：各階段紀錄依產出功能由相關人員經辦，並依規範實施覆核，避免球員兼裁判。
表 5-1：PDDRO 訓練階段與文件型別映射矩陣
第六章 代碼語法結構、逐段解析與編碼實例
本體系之文件識別碼採用九段式結構化字串，標準語法公式統一定義為：TT-[YYYY]-[CASE]-[PHASE]-[TYPE]-[ACCESS]-[RET]-[SEQ]-V[NN]。此語法設計目的在於使檢閱者不需依賴特定專用軟體，單從代碼字串即可辨識建立年份、所屬專案、流程階段、型別、行政處理標籤、保存假設、唯一序號及版本。
代碼嚴格禁止置入個人直接識別資料（如姓名、身分證號、電話、生日）。專案代碼（CASE）採用去識別之英數代號（示範案號 SYN60A），流水號（SEQ）依專案內文件產出順序以三位數字（001 至 999）賦予且不得重複。每一區段均設有嚴格取值規範（如表 6-1 所示）。
字元集規範：僅限使用半形大寫英文字母（A-Z）、半形阿拉伯數字（0-9）及半形連字號（-），不使用空格、底線或特殊字元。
長度控制：YYYY 為 4 位西元年；CASE 為 6 碼去識別代號；SEQ 為 3 位數字；NN 為 2 位數字版本號（如 V01）。
序號唯一性：在同一專案內，三位流水號 [SEQ] 具備唯一性，不得重複配賦。
表 6-1：九段式編碼結構逐段定義與規則限制字典
表 6-2：典型訓練紀錄編碼逐段解析示範表
第七章 十一項核心中繼資料欄位字典
文件編碼完成後，必須同步登錄至少「十一項核心中繼資料（Metadata）」。此十一項欄位構建出完整的索引骨架，使管理人員與外部評核人員無需逐頁調閱實體或電子全卷，即可掌握文件的所屬專案、流程階段、來源管道、行政處理標記及關聯版本。
中繼資料之登錄必須遵循內部一致性：代碼（doc_code）中各段取值與中繼資料欄位（如 case_id, phase, doc_type）必須完全呼應，不得有字面矛盾。此外，「來源定位與關聯版本」欄位應記載原生表單之示範存放編號（如 LOC-REC 編號）及其所依附之上游文件序號，以利建立可查考之關聯脈絡。
必填性規範：前十項核心欄位均為強制必填，任一欄位空白即屬無效登錄；第十一項關聯欄位視文件特性明確記載。
格式一致性：日期格式一律使用標準半形西元格式（YYYY-MM-DD），避免使用「開課日」等不確定文字。
前後呼應：中繼資料所載之階段與型別，必須與編碼字串之對應區段保持 100% 一致。
表 7-1：十一項核心中繼資料欄位定義與查驗標準字典
第八章 角色式日常分類編碼標準作業程序（SOP）
為確保分類編碼作業於平日運作中維持規範性，本章研訂具備功能分工之標準作業程序（SOP）。作業程序劃分四種建議功能角色：負責第一線收件與初審登錄之「訓練經辦功能」、負責教學內容確認之「教學主責功能」、負責代碼唯一性與中繼資料獨立核對之「品質覆核功能」，以及負責法規依據確認與爭議列管之「檔案督導功能」。在人力精簡之組織中，上述功能得由現有人員相互兼任，但嚴格遵循「一人不得獨立審查自身經辦紀錄」之防錯原則。
日常 SOP 包含六項作業程序：第一程序「入口收件查驗」，確認表單形式完整；第二程序「個資檢核與標註」，確保無個資洩漏風險並標記處理標籤；第三程序「代碼指派與登錄」，依字典產生代碼並填寫中繼資料清冊；第四程序「獨立第二人覆核」，針對代碼唯一性、中繼資料完整性及處理標籤相符性進行核對；第五程序「受控歸檔與移轉」，通過覆核之紀錄移交後續檔案管理程序；第六程序「異常更正處置」，若覆核發現重碼、漏填或標籤不符，登錄 EXC 表單辦理更正。
功能兼任限制：各項功能得由現有幹部兼任，但初編登錄人員不得擔任同一份文件之獨立覆核人員。
紀錄登記要求：各作業階段之流轉與確認，以登錄表單之註記日期與角色名稱為憑，不作繁複簽章要求。
爭議即時列管：凡發現法令依據未明、契約條款衝突或個資疑義，一律標定為 HOLD 並禁止銷毀，靜待釐清。
表 8-1：日常分類編碼作業標準作業程序（SOP）功能分工與查驗表
第九章 合成案例完整十二筆登錄清冊
為具體展示本體系之可操作性，本章提供示範專案 SYN-0060-2026-A01（課程名稱：「社區志工接待與資源轉介界線」）之 12 筆示範訓練紀錄登錄清冊。本示範案例模擬小型志工團體辦理訓練之流程，完整涵蓋規劃（P）、設計（D）、執行（DO）、查核（R）與成果（O）五大階段，且精準對應第四章定義之 12 種標準文件型別。
清冊中之每筆紀錄均載明結構化代碼、示範日期、虛擬形成方式、階段型別、行政處理標籤、示範保存假設（S3）及示範定位標籤（LOC-REC）。12 筆紀錄之示範時序自 2026-07-20 模擬需求通報起，經課前籌備、2026-08-15 模擬授課與簽到評量，迄至 2026-09-14 模擬成效追蹤與檢討改善。清冊所列為非真實執行之桌面演練示範資料，非本會實際核定、生效或已完成之會務紀錄。
為使每筆示範紀錄的形成方式、狀態、桌面檢核結果及依附關係可逐項查讀，表9-2依表9-1的項次一對一補列；兩表均屬同一合成案例。表內「檢核通過」只表示本報告中的SAMPLE桌面一致性檢核完成，不代表本會真實資料、實際作業、系統測試、正式稽核或核准結果。
示範母體勾稽：06出缺席名冊提供10名到課者；08評量、09回饋與10追蹤所列的10人母體均以06為SAMPLE共同基數。此對照僅在合成案例內成立；真實名冊或追蹤對象不同時，必須依可核對原始來源重新計算，不得套用本例分母。
代碼嚴格對應：每筆代碼之 PHASE 與 TYPE 與中繼資料欄位完全一致，無任何邏輯矛盾。
機敏處理標記：第 006 筆簽到名冊及第 008 筆評量總表因規劃載有學員個人身分識別或個別成績細目，處理標籤明確標註為 RST。
示範數據限制：本清冊所有內容僅供評核佐證之方法論展示，不作為組織已推動該項業務之證明。
表 9-1：合成案例 SYN-0060-2026-A01 完整十二筆示範訓練紀錄中繼資料總清冊
表9-2：12筆SAMPLE紀錄形成方式、狀態與示範檢核結論
第十章 檢核指標、三項刻意演練缺失與修正軌跡
為展示如何檢核人為初編作業瑕疵，本報告於示範資料集中特別設計三項代表性缺失進行桌面演練。此三項預先設計之缺失包含：缺失一為「編碼流水號重複」，經辦功能在模擬產出第 005 筆資源確認查核表（RSC）時誤用第 004 號流水碼；缺失二為「中繼資料定位欄位遺漏」，第 007 筆教學實施日誌之來源存放定位欄位空白未填；缺失三為「行政處理標籤不相符」，第 006 筆簽到名冊設定包含模擬學員個資，初編時被誤標為 INT，未依規則標註為 RST。
所有指標均依數學公式嚴格定義分子與分母，計算結果採四捨五入至小數點後第一位。各項比率之定義如下：代碼唯一性比率為「無重複之唯一代碼筆數 / 總登錄筆數」；中繼資料完整有效率為「各項必填欄位完整且格式合規之筆數 / 總登錄筆數」；處理標籤相符率為「處理標籤與文件機敏性質完全相符之筆數 / 總登錄筆數」。在演練初始階段，代碼唯一性為 11/12 = 91.7%，欄位完整有效率為 10/12 = 83.3%（第005筆因重碼未生效、第007筆缺漏定位），處理標籤相符率為 11/12 = 91.7%。經獨立第二人覆核提報缺失並填寫 EXC 表單更正後，三項指標均提升至 12/12 = 100.0%。若特定期間或範圍內沒有任何適用資料、分母為0，結果標示 N/A（不適用）並說明資料範圍；不得報100%。
示範數據口徑：報名 12 人、實到 10 人、缺席 2 人，出席率為 10/12 = 83.3%。
評量與回饋口徑：到課 10 人中有效受評 9 人、達標 8 人、未達標 1 人，評量通過率為 8/9 = 88.9%；問卷發出 10 份、有效 9 份、評定 4 或 5 分者 8 份，滿意反應正向率為 8/9 = 88.9%。
追蹤與自述限制：追蹤對象 10 人、回覆 8 人，追蹤回覆率為 8/10 = 80.0%；回覆者中自述有應用工具者 6 人，自述應用比例為 6/8 = 75.0%。此僅為個人主觀自述，不代表經組織客觀驗證之行為轉移或營運成果。本文件不設定任何未經核定之合格門檻。
表 10-1：示範課程運作數據與檢核指標計算說明表
表 10-2：三項刻意演練缺失、覆核處置與修正前後對照表
第十一章 實作示範工具與真實替換清單
為利小型志工組織在有限資源下推動作業，本章研擬三項實作示範工具表格：第一項為「填妥示範之分類型別判定工作單」，引導人員依序判定表單性質；第二項為「爭議案卷暫緩處理與退件決策表（HOLD / REJECT）」，規範疑義案卷之處理機制；第三項為「REAL 真實資料上線替換檢核清單」，指導未來承辦人員如何將文內之示範性 SAMPLE 數據替換為真實開課營運資料。
在此特別強調：未來若正式採納本制度並將示範資料替換為真實資料時，必須依循實質檢核程序，逐項抽換專案代碼、真實日期、實際出席名冊及評量成績。替換過程必須落實個資保護審查，嚴禁未經去識別化之資料外洩，未經權責單位核定前不得對外宣稱完成建置。
判定邏輯清晰：型別判定表採階段與實質內涵雙重檢驗，協助人員完成型別歸屬。
爭議暫緩列管：凡法規依據不明或契約條款存疑者，律定標記 HOLD 並禁止銷毀，靜待權責單位決議。
真實資料替換：清冊詳細列出真實資料之來源依據與專責查驗角色，防止直接複製示範數值。
表 11-1：實作工具一：已填妥示範之分類型別判定工作單（示範案例：課堂簽到表）
表 11-2：實作工具二：爭議案卷暫緩處理與退件決策表 (HOLD / REJECT Decision Table)
表 11-3：實作工具三：REAL 真實資料上線替換查核與權責清單
第十二章 制度採用前查核要點與相鄰文件界限
在將本分析報告轉化為正式制度前，管理階層必須依程序完成六項「制度採用前查核要點」：第一，查證本會組織規章，確認訓練紀錄管理之正式業務職掌；第二，檢視受訓對象之個資蒐集告知事項範本，確保符合個人資料保護法規範；第三，清查涉及外部補助或委辦之專案契約，彙整特定保存年限要求；第四，辦理執行人員之代碼編撰與去識別化作業講習，確保落實獨立第二人覆核作業；第五，檢驗與相鄰文件（0061 至 0064）之介面銜接順暢；第六，本作業草案須循內部法制程序提報審議通過後，始得正式發布施行。
最後，本報告再次重申與 0061 至 0064 相鄰文件之官方界限：本報告（0060）專注於分類歸納字典、編碼語法與中繼資料欄位之方法論研提；0061（檔案管理系統）專責建立檔案收納管理體系架構；0062（完整文件建檔資料及真實定位）專責訓練文件建檔、來源憑據與實質定位證據；0063（查詢功能與持續改善）專責查詢功能與改善機制；0064（系統化程度及檢索速度）專責系統化程度與調卷檢索速度之測試。五項指標各自獨立又循序呼應，共同建構完整之 TTQS 訓練品質佐證體系。
程序法定化：未經正式授權與法規查核前，本文件僅具示範草案性質，不得對外宣稱為已正式實施之制度。
介面一致性：本報告研提之 doc_code 作為各項訓練紀錄之唯一識別碼，供後續檔案管理與查詢程序引用。
持續檢討精進：未來正式施行後，應定期檢討 EXC 異常紀錄，持續優化分類字典與作業流程。
表 12-1：TTQS I14 系列相鄰文件官方職掌與本案關聯對照表

[TABLE 1]
【重要聲明與示範邊界】本文件為落實 TTQS 評核標準「訓練資料與訓練過程及成果的紀錄與分類，均有系統化歸納方法編碼」（方框 065）之候選草案分析報告，目前僅具建議與規劃性質，非本會已正式核定、生效或實施之規章辦法。 文內所引述之所有課程名稱、專案代碼、示範日期、統計數據、審查判定、功能角色、編碼字串、流程處置及三年保存期（S3），全數屬於示範性合成數據（SAMPLE / SYNTHETIC DATA）。本會目前之組織架構、現行人力職掌、既有檔案現狀、實體與數位系統環境以及法定檔案保存年限，現階段均標定為未確定（UNKNOWN）。文中所列之職務角色稱謂僅為示範功能分工，不代表實際人事任命；在人力精簡之組織中各項功能得由人員兼任，但一人不得獨立審查自身登錄之紀錄。 文內使用之 PUB、INT、RST 僅為內部行政處理標記，不代表法定機密等級或對外授權；代碼本身不具備授權或開通存取之功能。保存標記 S3 僅為未經核定之三年示範假設，非法律或主管機關規定；若真實保存依據未獲確認，一律標定為 HOLD 並禁止銷毀，直到查明適用法規依據並由權責單位正式決議為止。本報告不提供任何法律或法規結論。

[TABLE 2]
體系構面 | 規範核心 | 草案規劃內容 | 實務作業重點
階段劃分 | PDDRO 五大階段 | 涵蓋 Plan (P)、Design (D)、Do (DO)、Review (R)、Outcome (O) | 確保紀錄覆蓋完整訓練流程，各階段均有對應表單
型別字典 | 12 種標準型別 | NEE、NAN、PLN、LSN、RSC、ATT、DLG、ASM、FDB、FUP、EXC、IMP | 界定清楚納入與排除標準，避免表單混淆歸類
代碼語法 | 九段式結構碼 | TT-[年]-[案號]-[階段]-[型別]-[標籤]-[保存]-[序號]-V[版次] | 具邏輯可解析性，純英數結構，禁止置入個人機敏資料
中繼資料 | 11 項核心欄位 | 代碼、案號、標題、階段、型別、日期、來源、標籤、保存、狀態、定位關聯 | 提供完整追溯線索，作為後續索引與管理依據
覆核機制 | 獨立雙人核對 | 登錄功能負責初編填寫，第二人獨立查核代碼唯一性與中繼資料 | 若發現疑義或依據未明，立即標記退件或 HOLD 禁止銷毀

[TABLE 3]
指標項目 | 對應編號 | 官方指標規範重點 | 本報告（0060）範疇 | 相鄰文件專屬範疇（排除事項）
I14-E01 | DOCX 0060 | 分類歸納方法與系統化編碼 | 研擬分類字典、編碼語法、中繼資料、作業SOP及示範清冊 | 排除檔案系統架構、查詢工具及速度測試等實作
I14-E02 | DOCX 0061 | 檔案管理系統之建立 | 提供標準編碼與型別代碼作為其輸入依據 | 由 0061 專責規劃整體檔案管理系統之運作架構
I14-E03 | DOCX 0062 | 完整文件建檔資料及真實定位 | 提供示範來源定位標籤（LOC-REC）供範例引用 | 由 0062 專責建立完整建檔資料、來源憑據與真實定位證據
I14-E04 | DOCX 0063 | 查詢功能與持續改善機制 | 提供 11 項中繼資料欄位作為查詢欄位規劃之參考 | 由 0063 專責建立查詢介面、檢索功能與持續改善機制
I14-E05 | DOCX 0064 | 系統化程度及檢索速度測試 | 提供示範樣本資料作為後續演練之參考輸入 | 由 0064 專責執行系統化程度評定與檢索調卷速度之測試

[TABLE 4]
作業階段 | 檢核條件 | 演練情境說明 | 建議處置與決策分支 | 處置原則與責任功能
入口收件 | 表單必填欄位完整性 | 實施計畫未附經費規劃或必要欄位註記不全 | 退件分支：退回辦理人補齊內容 | 未補正前不得賦碼；由訓練經辦功能把關
個資檢驗 | 是否涉及自然人機敏個資 | 簽到名冊載有學員身分證號或個人直接識別細目 | 去識別化分支：名冊標記為 RST 標籤管制 | 代碼中嚴禁置入個資；由訓練經辦功能執行
型別判定 | 文件產出內容單一性 | 檢討紀錄同時包含學員滿意度與後續改善計畫 | 拆分分支：滿意度歸 FDB，改善對策歸 IMP | 依實質內容分開賦碼；由教學主責功能釐清
覆核抽檢 | 代碼唯一性與語法合規性 | 同專案內兩份表單使用相同三位流水號 | 退件分支：更正重複碼並配賦唯一序號 | 註銷重複碼並補登紀錄；由品質覆核功能把關
保存查核 | 正式法規或契約保存依據 | 外部專案紀錄無明確法規保存依據 | 凍結分支：標記為 HOLD 並禁止銷毀 | 未查清依據前禁止銷毀；由檔案督導功能列管

[TABLE 5]
型別代碼 | 中文名稱 | 所屬階段 | 納入範圍（應歸入） | 排除範圍（不應歸入） | 常見錯分樣態與防範原則
NEE | 需求來源依據 | P (Plan) | 外部法規要求、社區訪談紀錄、受訓需求通報、組織策略方針 | 統計彙整後之職能落差分析報告（屬 NAN） | 易將第一手需求通報誤編為 NAN；防範：未經量化分析之原始資料歸 NEE
NAN | 需求分析報告 | P (Plan) | 職能缺口分析表、訓練需求調查統計、優先受訓對象評估報告 | 個別人員之原始報名或受訓申請單（屬 NEE） | 易將個別需求彙整誤當分析；防範：具備統計彙整或建議結論者始為 NAN
PLN | 訓練實施計畫 | D (Design) | 訓練專案實施計畫書、開課草案、預算編列與課程綱要表 | 授課講師自行編排之個別教案（屬 LSN） | 易將講師個人講義大綱當作實施計畫；防範：涉行政與經費規劃者為 PLN
LSN | 教學設計教案 | D (Design) | 講師教學教案、單元講義大綱、教學活動引導手冊、演練題目設計 | 整體訓練實施計畫書（屬 PLN）或公開出版講義 | 易與實施計畫混淆；防範：針對課堂授課進度與教材引導設計者歸 LSN
RSC | 資源確認紀錄 | D (Design) | 教學資源確認查核表、設備器材清點單、助教排班確認單 | 課堂當日教學日誌（屬 DLG）或實施計畫書（屬 PLN） | 易與課堂日誌混淆；防範：課前準備期針對軟硬體物資之查核確認始為 RSC
ATT | 出缺席簽到紀錄 | DO (Do) | 課堂簽到退名冊、學員出缺席紀錄表、請假單據彙整 | 隨堂測驗卷、演練評分表（屬 ASM） | 易將附帶成績之簽到表混編；防範：簽到表與成績評量必須分開歸檔
DLG | 教學實施日誌 | DO (Do) | 助教巡堂觀察日誌、講師課堂實施摘記、課堂突發事件紀錄 | 課前設計之教案（屬 LSN）或學員滿意度問卷（屬 FDB） | 易將課前教案誤當課堂日誌；防範：記錄授課現場互動與狀況者始為 DLG
ASM | 學習評量紀錄 | R (Review) | 課堂情境演練評分表、隨堂測驗卷、技能檢定評核表、成績總冊 | 學員對課程滿意度之問卷（屬 FDB） | 最常將滿意度問卷誤作評量；防範：檢驗學習吸收與技能成效者為 ASM
FDB | 反應回饋調查 | R (Review) | 結訓滿意度問卷、教材設施回饋表、學員意見反應統計表 | 學員隨堂測驗（屬 ASM）或課後一段時間之行為追蹤（屬 FUP） | 易將即時反應與長期成效混淆；防範：結訓當下對教學與環境之評價屬 FDB
FUP | 成效追蹤紀錄 | O (Outcome) | 訓後一段期間志工服務追蹤紀錄、電訪回覆表、個案轉介應用統計 | 結訓當日填寫之滿意度問卷（屬 FDB） | 易將課後心得誤為長期追蹤；防範：具時間間隔且追蹤實務應用者始為 FUP
EXC | 編碼異常紀錄 | R (Review) | 流水號重碼註銷單、中繼資料漏填更正表、處理標籤更正對照表 | 一般行政公文之發文改版紀錄 | 易被當一般雜件忽略；防範：凡涉本系統代碼修訂與退件補正者統一收錄
IMP | 持續改善行動 | O (Outcome) | 培訓檢討會議改善追蹤表、課程規劃修正對照表、改善建議方案 | 例行行政會議未涉改善對策之一般紀錄 | 易將純檢討紀錄誤編；防範：載明改善具體方案與追蹤規劃者始為 IMP

[TABLE 6]
階段代碼 | 階段名稱 | 階段核心目標 | 主要納入型別 | 生命週期觸發時點 | 階段品質查核重點
P | 規劃階段 (Plan) | 掌握志工職能缺口與受訓需求，確立辦訓合理性 | NEE (需求來源) NAN (需求分析) | 收到外部反映、幹部訪談或年度規劃啟動時 | 查核需求是否具體客觀，避免無依據開課
D | 設計階段 (Design) | 將需求轉化為實施計畫、教學教案並備妥教學資源 | PLN (實施計畫) LSN (教學設計) RSC (資源確認) | 開課前規劃籌備期間逐步產出 | 查核計畫項目、教案大綱及軟硬體資源是否完備
DO | 執行階段 (Do) | 記錄教學現場實際出缺勤與師生課堂互動狀況 | ATT (出缺席紀錄) DLG (教學實施日誌) | 開課當天教學現場作業時產生 | 查核簽到表單欄位填寫完整無缺漏、日誌符合記載規範
R | 查核階段 (Review) | 評量學員學習成果、滿意回饋並排解行政異常 | ASM (學習評量) FDB (反應回饋) EXC (異常紀錄) | 課程結訓當下至結訓後彙整期間產出 | 查核評量閱卷客觀性、回饋統計確實性及代碼正確性
O | 成果階段 (Outcome) | 評估學員課後行為應用情形，研擬後續持續改善方案 | FUP (成效追蹤) IMP (持續改善行動) | 結訓後追蹤期間及召開檢討會議時產生 | 檢視追蹤數據真實性及改善對策之實質可行性

[TABLE 7]
段號 | 區段標籤 | 格式長度 | 合法取值範圍 | 區段語意說明 | 規則與限制事項
第1段 | TT | 2 字元 | 固定為「TT」 | 代表 Training & Talent 體系識別碼 | 固定常數，不可更動
第2段 | YYYY | 4 數字 | 半形西元年（如 2026） | 代表文件立項或建立之西元紀年 | 不得使用民國年或2位簡寫
第3段 | CASE | 6 字元 | 專案代碼（如 SYN60A） | 特定訓練專案識別代碼，非個資代號 | 嚴禁使用個人識別資訊編碼
第4段 | PHASE | 1-2 字元 | P, D, DO, R, O | 所屬 PDDRO 訓練流程階段代碼 | 執行階段固定使用 DO
第5段 | TYPE | 3 字母 | 第四章定義之 12 種代碼 | 文件標準型別代碼（如 NEE, LSN 等） | 限用字典定義之 12 種合法代碼
第6段 | ACCESS | 3 字母 | PUB, INT, RST | 內部行政處理標記（非法律密級） | 含名冊或個別成績者標記 RST
第7段 | RET | 2-4 字元 | S3, HOLD | 保存期限標籤（S3示範三年；HOLD暫緩） | 依據未查實前一律標記 HOLD
第8段 | SEQ | 3 數字 | 001 至 999 之流水號 | 專案內文件產出之唯一時序流水號 | 同一專案內唯一，不可重複
第9段 | V[NN] | 3 字元 | V01 至 V99 之版本碼 | 文件修訂版次代碼，初版為 V01 | 實質內容變更應遞增版本號

[TABLE 8]
解析維度 | 範例一：教學設計教案 (LSN) | 範例二：學員簽到名冊 (ATT) | 範例三：成效追蹤紀錄 (FUP)
完整結構代碼 | TT-2026-SYN60A-D-LSN-INT-S3-004-V01 | TT-2026-SYN60A-DO-ATT-RST-S3-006-V01 | TT-2026-SYN60A-O-FUP-INT-S3-010-V01
第1段 [體系碼] | TT（訓練文件體系） | TT（訓練文件體系） | TT（訓練文件體系）
第2段 [建立年份] | 2026（2026年示範立項） | 2026（2026年示範課堂產生） | 2026（2026年示範追蹤彙整）
第3段 [專案案號] | SYN60A（接待與轉介界線示範專案） | SYN60A（接待與轉介界線示範專案） | SYN60A（接待與轉介界線示範專案）
第4段 [PDDRO階段] | D（Design，訓練設計階段） | DO（Do，訓練執行階段） | O（Outcome，訓練成效階段）
第5段 [文件型別] | LSN（教學設計教案大綱） | ATT（出缺席簽到紀錄名冊） | FUP（訓後成效追蹤紀錄）
第6段 [處理標籤] | INT（內部處理標記） | RST（限制處理標記，含個資名冊） | INT（內部處理標記）
第7段 [保存參照] | S3（示範假設三年） | S3（示範假設三年） | S3（示範假設三年）
第8段 [時序流水號] | 004（專案內第4件文件） | 006（專案內第6件文件） | 010（專案內第10件文件）
第9段 [修訂版次] | V01（初版） | V01（初版） | V01（初版）

[TABLE 9]
項次 | 欄位名稱 | 英文識別標籤 | 資料型態與屬性 | 格式範例 | 實質定義與查驗重點
01 | 文件完整編碼 | doc_code | 文字 (32-38字元)，必填 | TT-2026-SYN60A-D-LSN-INT-S3-004-V01 | 依第六章語法生成之唯一代碼，作為體系主鍵
02 | 專案案號 | case_id | 文字 (6-16字元)，必填 | SYN-0060-2026-A01 或 SYN60A | 標定文件所屬訓練專案代碼，不得混入無關專案
03 | 文件中文標題 | doc_title | 文字 (4-50字元)，必填 | 社區志工接待與資源轉介界線實施計畫 | 精確簡述表單內容，包含主題與型別意義
04 | PDDRO 階段 | phase | 文字 (1-2字元)，必填 | P, D, DO, R, O | 與代碼中 PHASE 一致，反映流程生命週期
05 | 文件型別代碼 | doc_type | 文字 (3字元)，必填 | NEE, NAN, PLN, LSN, RSC, ATT 等 | 與代碼中 TYPE 一致，符合第四章字典定義
06 | 文件形成日期 | create_date | 日期 (10字元)，必填 | 2026-08-15 (YYYY-MM-DD) | 紀錄實際作成或產出之日期，不得倒填
07 | 來源管道方式 | source_origin | 文字 (4-30字元)，必填 | 需求通報單、線上問卷、課堂簽到表 | 註明資料原始形成來源，確保可查考性
08 | 行政處理標籤 | access_level | 文字 (3字元)，必填 | PUB, INT, RST | 內部行政管理標記；含個資名冊強制標 RST
09 | 保存參照年限 | retention_rule | 文字 (2-10字元)，必填 | S3 (示範三年), HOLD (暫緩銷毀) | 標註保存假設；依據未查實前標記 HOLD
10 | 生命週期狀態 | status | 文字 (4-10字元)，必填 | 草擬中、已生效、待覆核、已歸檔 | 反映文件行政狀態，未經確認不可標已生效
11 | 來源定位關聯 | source_locator_ver | 文字 (6-60字元)，必填 | LOC-REC-2026-0810 / 依附003號 / V01 | 註記示範存放編號及與上下游文件之關聯

[TABLE 10]
步驟編號 | 程序名稱 | 建議執行功能 | 查核功能 | 作業輸入與防錯要點 | 產出紀錄與表單
程序 1 | 入口收件查驗 | 訓練經辦功能 | 教學主責功能 | 查驗訓練表單是否填寫完整，未完成者退件 | 經收件初驗之原始表單
程序 2 | 個資檢核標註 | 訓練經辦功能 | 品質覆核功能 | 檢視是否含自然人個資；名冊類標記 RST 標籤 | 去識別化表單或 RST 標記表單
程序 3 | 代碼指派登錄 | 訓練經辦功能 | 無（自行初編） | 依字典賦予唯一代碼，填入 11 項中繼資料 | 已賦碼之中繼資料清冊初稿
程序 4 | 獨立第二人覆核 | 品質覆核功能 | 檔案督導功能 | 獨立核對代碼唯一性、欄位完整性及標籤相符性 | 覆核確認註記與覆核清冊
程序 5 | 受控歸檔移轉 | 訓練經辦功能 | 檔案督導功能 | 覆核合格之紀錄移交後續檔案管理程序 | 已確認之中繼資料登錄總冊
程序 6 | 異常更正處置 | 品質覆核功能 | 檔案督導功能 | 發現重碼、漏填時登錄 EXC 表單，補正後重新覆核 | EXC 編碼異常更正紀錄表

[TABLE 11]
項次 | 完整文件識別編碼 | 文件中文標題 | 示範日期 | 階段 / 型別 / 標籤 / 保存 | 示範來源與定位關聯
01 | TT-2026-SYN60A-P-NEE-INT-S3-001-V01 | 社區長者接待與轉介需求通報摘記 | 2026-07-20 | P / NEE / INT / S3 (2029-08-15) | 需求通報表單樣張 / LOC-REC-2026-0720 / V01
02 | TT-2026-SYN60A-P-NAN-INT-S3-002-V01 | 第一線志工服務界線與職能缺口分析報告 | 2026-07-31 | P / NAN / INT / S3 (2029-08-15) | 需求統計表 / LOC-REC-2026-0731 / 依附001
03 | TT-2026-SYN60A-D-PLN-INT-S3-003-V01 | 社區志工接待與資源轉介界線實施計畫書 | 2026-08-05 | D / PLN / INT / S3 (2029-08-15) | 實施計畫草案建檔 / LOC-REC-2026-0805 / 依附002
04 | TT-2026-SYN60A-D-LSN-INT-S3-004-V01 | 接待應對規範與轉介作業教學教案大綱 | 2026-08-10 | D / LSN / INT / S3 (2029-08-15) | 講師編撰教案 / LOC-REC-2026-0810 / 依附003
05 | TT-2026-SYN60A-D-RSC-INT-S3-005-V01 | 研習教室教學資源與設備器材確認查核表 | 2026-08-12 | D / RSC / INT / S3 (2029-08-15) | 資源查檢表單樣張 / LOC-REC-2026-0812 / 依附003、004
06 | TT-2026-SYN60A-DO-ATT-RST-S3-006-V01 | 課堂學員出缺席簽到退紀錄名冊 | 2026-08-15 | DO / ATT / RST / S3 (2029-08-15) | 簽到名冊情境樣張 / LOC-REC-2026-0815A / 名冊類型示範標記（本件不含個資、姓名或簽名）/ 同案計畫關聯依附003
07 | TT-2026-SYN60A-DO-DLG-INT-S3-007-V01 | 課堂教學實施日誌與課堂互動摘記 | 2026-08-15 | DO / DLG / INT / S3 (2029-08-15) | 助教巡堂摘記 / LOC-REC-2026-0815B / 依附003、004
08 | TT-2026-SYN60A-R-ASM-RST-S3-008-V01 | 志工情境模擬應對實務演練個別評分總表 | 2026-08-15 | R / ASM / RST / S3 (2029-08-15) | 講師演練評分 / LOC-REC-2026-0815C / 含成績 / 依附003、004、006
09 | TT-2026-SYN60A-R-FDB-INT-S3-009-V01 | 結訓學員滿意度與反應回饋不記名統計表 | 2026-08-20 | R / FDB / INT / S3 (2029-08-15) | 問卷不記名統計 / LOC-REC-2026-0820 / 依附003、006
10 | TT-2026-SYN60A-O-FUP-INT-S3-010-V01 | 課後三十日轉介工具實際應用追蹤彙整表 | 2026-09-14 | O / FUP / INT / S3 (2029-08-15) | 電訪調查回覆 / LOC-REC-2026-0914 / 依附003、006
11 | TT-2026-SYN60A-R-EXC-INT-S3-011-V01 | 編碼重碼與標籤誤標異常更正處置紀錄表 | 2026-09-15 | R / EXC / INT / S3 (2029-08-15) | 覆核異常提報 / LOC-REC-2026-0915 / 異常更正 / 依附005、006、007
12 | TT-2026-SYN60A-O-IMP-INT-S3-012-V01 | 志工轉介培訓檢討與持續改善行動方案 | 2026-09-20 | O / IMP / INT / S3 (2029-08-15) | 改善方案草案樣張 / LOC-REC-2026-0920 / 依附009、010、011

[TABLE 12]
項次 | 形成方式（SYNTHETIC） | 紀錄狀態 | 本報告示範檢核結論 | 交叉引用／依附
01 NEE | 由本文件合成課程題設編寫需求來源樣張；非真實需求通報、訪談或問卷。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：代碼唯一且題設欄位完整。核對需求來源格式與題設相符；真實組織需求與簽核權限均未確認。 | 案例起點，無上游項
02 NAN | 由01合成輸入形成需求分析演示；非真實統計分析。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：分析架構由01推導，必填項完整。核對分析維度邏輯銜接；非真實統計推論，正式決策依據尚未確認。 | 依附01
03 PLN | 由02演示需求形成課程實施計畫樣張；未核准、未開課。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：計畫編號唯一且時序接續02。核對開課架構符合規範；未核准且未開課，適用規範與權限尚未確認。 | 依附02
04 LSN | 由03規劃展開教案大綱樣張；非真實講師教案。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：單元大綱與03時數目標對齊，欄位完整。核對教學配置吻合；非真實教案，若實際使用教材，來源與適用使用權限另行核對；此樣張不表示已取得授權。 | 依附03
05 RSC | 依04假設教學安排列資源確認項；非實際場地/設備盤點。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：初始重複碼已修正，RSC樣張代碼流水號由004更正為005；12筆代碼均唯一。核對資源項對應03與04；實體場地與設備可用性尚未確認。 | 依附03、04
06 ATT | 依合成12報名、10到課、2缺席形成簽到樣張；不含姓名/簽章/可識別個資。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：簽到名冊情境原先誤標INT，已更正為RST；12報名、10到課、2缺席數量閉合。RST僅為樣本處理標籤，不含真實個資；真實名冊來源、處理權限及實際簽到資料均未確認。 | 依附03
07 DLG | 依03及04合成教學腳本形成授課日誌樣張；非真實授課紀錄。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：初始缺少來源存放定位，已補入LOC-REC-2026-0815B；日誌節點對應03與04。非真實授課紀錄，實際授課、紀錄來源與負責角色均未確認。 | 依附03、04
08 ASM | 依合成10到課、9有效評量、8達標、1未達標形成評量彙整；不含個別個資。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：10名到課中9份有效評量、8人達標、1人未達標；與03課程計畫、04評量安排及06簽到10人母體相符。本列未另設缺陷修正；RST僅為樣本處理標籤，真實成效尚未確認。 | 依附03、04、06
09 FDB | 依合成10份發出、9份有效、8份評4或5形成回饋彙整；非真實問卷原表。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：有效份數與評分級距邏輯相符。核對10份發放母體與06簽到的10人到課數一致；非真實問卷原表，真實滿意度尚未確認。 | 依附03、06
10 FUP | 依合成追蹤10人、回覆8人、6人自述形成追蹤彙整；只示範自述、不證明實際行為。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：追蹤回覆與自述數量銜接正確；核對10人追蹤母體與06簽到的10人到課數一致。自述欄位完整；僅示範自述不證明實際行為，長期成效尚未確認。 | 依附03、06
11 EXC | 依本案預設重複碼、定位缺漏、標籤不符三項桌面演練形成異常紀錄；非協會真實錯誤。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：初始代碼唯一性11/12、必填欄位完整有效10/12、處理標籤相符11/12；更正後三項均為12/12。此為SAMPLE桌面演練設計，非真實錯誤；實體稽核尚未確認。 | 依附05、06、07
12 IMP | 綜合09回饋、10追蹤及11三項桌面演練缺失，提出改善追蹤樣張；未核准、未執行。 | SAMPLE／桌面演練，未生效 | 本報告內合成桌面檢核：改善對策完整對應11之演練缺失，因果關聯清晰。樣張未核准且未執行，管理層決策尚未確認。 | 依附09、10、11

[TABLE 13]
指標構面 | 數學計算公式 | 示範分子說明 | 示範分母說明 | 示範數值結果
學員出席率 | 出席人數 / 報名總人數 × 100% | 實際到課學員 10 人 | 核定報名總人數 12 人 | 10 / 12 = 83.3%
評量通過率 | 評量達標人數 / 有效受評人數 × 100% | 演練評量達標者 8 人 | 有效接受評量者 9 人 | 8 / 9 = 88.9%
滿意反應正向率 | 評4或5分人數 / 有效問卷總數 × 100% | 滿意度評高分者 8 人 | 回收有效問卷數 9 份 | 8 / 9 = 88.9%
追蹤回覆率 | 實際回覆人數 / 追蹤對象總人數 × 100% | 完成電話訪查者 8 人 | 追蹤對象總人數 10 人 | 8 / 10 = 80.0%
工具自述應用率 | 自述使用工具人數 / 實際回覆人數 × 100% | 自述使用工具志工 6 人 | 完成電話訪查者 8 人 | 6 / 8 = 75.0% (自述比例)
代碼唯一性比率 | 無重複代碼筆數 / 總登錄筆數 × 100% | 初期 11 筆 / 修正後 12 筆 | 總登錄筆數 12 筆 | 演練前 91.7% -> 修正後 100.0%
欄位完整有效率 | 必填項完整筆數 / 總登錄筆數 × 100% | 初期 10 筆 / 修正後 12 筆 | 總登錄筆數 12 筆 | 演練前 83.3% -> 修正後 100.0%
處理標籤相符率 | 標籤完全相符筆數 / 總登錄筆數 × 100% | 初期 11 筆 / 修正後 12 筆 | 總登錄筆數 12 筆 | 演練前 91.7% -> 修正後 100.0%

[TABLE 14]
演練項目 | 演練缺陷一：代碼流水號重複 | 演練缺陷二：存放定位欄位遺漏 | 演練缺陷三：處理標籤不相符
發生環節 | 初編登錄環節（流水號指派） | 初編登錄環節（中繼資料填寫） | 個資檢驗環節（處理標籤初判）
缺陷具體現象 | 第005筆資源確認查核表（RSC）誤植為第004號代碼 | 第007筆教學實施日誌之來源存放定位欄位空白留白 | 第006筆簽到名冊載有學員個資，卻被標註為 INT
違反之規範 | 違反流水號唯一性與防重碼原則 | 違反必填中繼資料欄位完整性原則 | 違反名冊強制標註 RST 限制處理標籤之規定
覆核查驗軌跡 | 獨立第二人覆核比對發現重碼，退件經辦功能 | 覆核人員檢核欄位完整度發現空值，要求補件 | 覆核功能檢核表單樣張載有個人身分識別細目，判定標籤不合規
具體糾正措施 | 註銷重複碼，將資源確認查核表更正為序號 005 | 經辦補填示範存放編號 LOC-REC-2026-0815B | 將標籤由 INT 抽換更正為 RST，加註管制註記
修正前演練數據 | 代碼唯一性：11 / 12 = 91.7% | 欄位完整有效率：10 / 12 = 83.3% | 處理標籤相符率：11 / 12 = 91.7%
修正後演練數據 | 代碼唯一性：12 / 12 = 100.0% | 欄位完整有效率：12 / 12 = 100.0% | 處理標籤相符率：12 / 12 = 100.0%
演練結論說明 | 示範如何透過覆核比對攔截重複序號並重新配賦，純屬虛擬情境演練，不代表本會實際開課或真實代碼運作成效 | 示範如何透過必填檢核阻斷定位缺漏並落實補正登記，純屬桌面流程測試，不代表本會真實檔案管理或調卷實績 | 示範如何依防護原則更正處理標籤並落實名冊管制，純屬示範檢核機制，不代表本會真實個資審查或營運成果

[TABLE 15]
查核問題步驟 | 檢核重點與選項 | 示範案例檢核結果 | 判定輸出與指引
步驟 1：流程時點檢驗 | 該文件於培訓活動何時產生？ 課前籌備 / 課堂現場 / 結訓查核 / 長期追蹤 | 課堂現場授課時產生 | 鎖定流程階段為 DO 執行階段
步驟 2：內容實質檢驗 | 文件記載之核心內涵為何？ 教學教案 / 出缺席名冊 / 測驗卷 / 滿意度問卷 | 名冊如含個人識別細目或個別出缺席資訊，依示範規則使用 RST。 | 確認文件型別為 ATT（出缺席紀錄）
步驟 3：個資機敏檢驗 | 文件是否包含自然人個人身分識別資料？ 完全無個資 / 僅職務稱謂 / 含學員個人識別細目 | 包含學員個人身分識別細目 | 確認行政處理標籤為 RST 限制標記
步驟 4：保存依據查核 | 是否有明確法規或合約保存期？ 法規明定 / 依示範暫標 S3 / 依據未明需列管 | 示範案例暫標 S3；若未明標記 HOLD | 暫標 S3 (示範假設)；未明者標 HOLD
綜合輸出成果 | 指派完整分類標籤與代碼 | 階段: DO / 型別: ATT / 標籤: RST | 產出代碼：TT-2026-SYN60A-DO-ATT-RST-S3-006-V01

[TABLE 16]
案件列管編號 | 表單送審原由 | 爭議瑕疵現象 | 建議處置判定 | 處置原則與程序說明
HLD-2026-001 | 保存依據未確認之樣張 | 適用保存依據、起算點及有權決定來源尚未取得或核實；本示範不設定年限 | 判定：HOLD（保存依據未確認） | 暫不指派正式保存碼，不得銷毀；由有權角色核對適用來源並留存依據與決定紀錄。
REJ-2026-002 | 志工研習出缺席紀錄樣張 | 表單來源憑證未註記開課場次編號且缺少存放定位標籤 | 判定：REJECT（退件） | 退回登錄功能補正來源場次資訊與定位標記，補齊前不得配賦代碼
HLD-2026-003 | 個人識別資料未確認樣張 | 資料型態包含可能識別欄位，處理標籤與核准接觸角色尚未核實；本示範未附任何個人資料 | 判定：HOLD（標籤、權限未確認） | 暫停一般流通，限由實際有權角色核對最少必要處理方式；不得推定事件、申訴或調查已發生。
REJ-2026-004 | 來源及定位欄位缺漏樣張 | 資料來源及形成方式欄位空白，且缺少可核對之來源定位 | 判定：REJECT（退件補正） | 退回補齊來源、形成方式與定位資訊；補齊前不賦正式代碼，也不推定涉及第三方權利。

[TABLE 17]
查驗步驟 | 替換查驗構面 | 示範內容 (SAMPLE) | 真實資料替換要求 (REAL) | 真實資料驗證依據
第 1 步 | 專案案號替換 | SYN-0060-2026-A01 / SYN60A | 替換為本會正式開課專案案號 | 年度訓練實施計畫核定文件
第 2 步 | 課程主題日期 | 社區志工接待與資源轉介界線 / 2026-08-15 | 替換為經正式核定之開課名稱與實際舉辦日期 | 正式核定之開課計畫或年度行事曆
第 3 步 | 出缺席簽到紀錄 | 報名12人、實到10人、缺席2人 | 替換為實際開課之簽到退正本（依規標記 RST） | 真實出缺席簽到名冊正本
第 4 步 | 學習評量數據 | 有效9人、達標8人、未達標1人 | 替換為學員真實測驗卷或演練評分總表 | 講師評定成績之評分總表正本
第 5 步 | 反應回饋問卷 | 發出10份、有效9份、滿意8份 | 替換為學員真實填寫之實體或線上問卷統計 | 結訓滿意度問卷統計原始表
第 6 步 | 成效追蹤資料 | 追蹤10人、回覆8人、自述應用6人 | 替換為實際追蹤紀錄（註記僅為自述比例） | 訓後追蹤訪談紀錄表正本
第 7 步 | 正式保存依據 | S3（示範三年，至 2029-08-15） | 查明適用法規或契約年限；未明前標記 HOLD | 法規評估紀錄或契約條款依據

[TABLE 18]
文件編號 | 官方指標名稱 | 官方規範重點 | 本報告（0060）定位 | 與本報告之銜接關聯說明
0060 (本案) | 分類歸納方法與編碼 | 系統化歸納方法與不含個資識別代碼 | 研討分類字典、編碼規則、中繼資料與SOP草案 | 體系基礎：研訂分類字典與結構代碼供後續引用
0061 | 檔案管理系統之建立 | 建置合宜之訓練檔案管理系統架構 | 提供標準代碼作為檔案管理體系之輸入識別 | 承接本案代碼作為檔案收納與架構建立之標籤
0062 | 完整文件建檔與真實定位 | 完整訓練文件建檔、來源憑據與實質定位證據 | 提供示範來源定位標籤（LOC-REC）供範例引用 | 將本案示範定位轉化為完整建檔資料與真實定位憑據
0063 | 查詢功能與持續改善 | 建立訓練紀錄查詢功能與持續改善機制 | 提供 11 項中繼資料欄位供查詢功能規劃之參考 | 利用本案中繼資料欄位作為查詢功能設計之依據
0064 | 系統化程度及檢索速度 | 評定檔案系統化程度並測試調卷檢索速度 | 提供示範樣本資料作為演練輸入參考 | 驗證依本案編碼邏輯歸納之文件其調卷檢索速度
