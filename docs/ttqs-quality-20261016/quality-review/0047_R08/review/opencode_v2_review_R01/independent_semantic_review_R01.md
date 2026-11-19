# Independent Semantic Review — TTQS-0047 (I10-E02), R08

**Candidate DOCX SHA-256 (as supplied, not recomputed):** `b8cc8e4473e9cd7ad93f21c0cb9503865e683e3b802ac70577fbd8db3524d447`
**Rendered PDF SHA-256 (as supplied, not recomputed):** `e828097ba100efba6d67a1937bdf163199566087161e97f2b7ba4079042fb2a5`

## Scope and limits (input-scope statement)
My review covers **only** the supplied packet: the 0047 Blueprint row (and adjacent 0045/0048 rows), the DOCX block-order text, the rendered page-by-page text (pp.1–8), and the 25-entry SAMPLE/SYNTHETIC replacement register. I did **not** recompute the binary SHA-256 of either file, did **not** open the original DOCX, did **not** view a PNG or inspect any pixels/rendering, did **not** measure fonts, and did **not** access the external official source PDF or any runtime SOURCE/CONTROL map. The two hashes above are transcribed from the packet as claims, not verified by me. Font-floor compliance (body ≥10.5 pt / table ≥9.5 pt) is therefore **UNKNOWN**. Statements below separate *supplied-source facts* from *reviewer inference*, which is labeled.

---

## Criterion-by-criterion verdicts

**1. Correct document type and official mapping — PASS**
Blueprint row `document_role = analysis_report`, `document_genre = 分析／評估報告`; body presents as an analytical report (摘要/用途, 官方要求及分析範圍, 資料來源樣本, 指標定義, 完整示範資料及逐步計算, 分群/趨勢/差異, 圖表解讀, 發現/原因/證據強度, 結論與建議, 責任期限追蹤, 合成聲明, 附件索引), matching the `required_sections` list. Official text quoted verbatim: 「相關文件能記錄近年來對於課程之評估、採購、簽約與後續管理作業的檢討及改善。」 (p.1 「本文件對應的查核要求」 and 「官方要求及分析範圍」; p.7 追溯表). Source locator used: 《TTQS查核佐證文件資料表－訓練機構版》指標10 第3頁 and box P03-B09 (p.1, p.2, p.4) — consistent with the packet (page 3, P03-B09, checkbox 048, order 9). Minor: checkbox 048 / order 9 are not restated in the body; not an error. **Fact.**

**2. Mature, usable analysis/report mechanics — PASS**
Contains a real data dictionary with denominator/口径/limits (p.4–5 「資料欄位、定義、分母、來源及限制字典」), formula definitions (p.2 指標定義), a worked multi-criterion table (p.5), weighted-score computation (p.6), a gap-prioritisation matrix (p.6), an N/A rule (「應完成數為零時列不適用並說明」, p.5), rounding rules to 2 dp / 1 dp and a no-averaging-of-percentages rule (p.2), interpretation thresholds (p.3, p.8), and a conclusion→evidence→action→owner→deadline→KPI table (p.7). This is genuinely executable analysis mechanics, not headings-only. **Fact.**

**3. Complete evaluation → procurement → contracting → post-performance → review/improvement chain — PASS (with scope caveat)**
All five links exist as explicit criteria/check items: 選擇前課程需求與評估規準; 資源/選擇理由可重現 (採購比較、核決); 採購、契約及驗收 (契約範圍、簽署、驗收); 履約後評估及改善追蹤; 改善閉環 (檢討發現→責任→期限→複核→結案) in the dictionary (p.4–5), the 判斷依據 table (p.7), and the 履約檢核項目 list (p.8). **Caveat (reviewer inference):** the report interprets 「課程之評估」 primarily as *selection/evidence-quality evaluation of resource acquisition*, and does not present post-course learning/reaction outcome metrics. The requirement is defensible under this reading (課程設計時師資／教材／廠商的評估選擇), so I do not mark it down, but the alternate reading is not separately evidenced.

**4. 0045 (I10-E01) and 0048 (I10-E03) explicitly distinguishable, not falsely claimed — PASS**
p.2 「相鄰要求邊界與負向近鄰拒收規則」 gives one explicit bullet per neighbour with *checkable distinguishing fields*:
- 0045/I10-E01《訓練資源採購與甄選管理辦法》 — distinguishes by procedure fields (啟動條件、輸入來源、角色與覆核、門檻分支、控制點、異常升級、紀錄編號、交接) and states 「本件 0047 不制定或取代這些程序；…若待證的是程序本身或其權責核准，不得以 0047 代替。」
- 0048/I10-E03 — distinguishes by meeting/approval fields (日期、角色代碼、來源／附件定位、判定與理由、覆核及後續行動) and states 0047 pp.5–7 「不是會議紀錄、師資遴聘核准或大型採購通過之原件…必須另取 0048 之真實原件，不得從本報告的合成數據推定。」
This satisfies the "reject at least two erroneous near-neighbours" acceptance test. **Minor / UNKNOWN note:** the body's neighbour box IDs (0045 = P03-B07, 0048 = P03-B10) are *not* corroborated by the supplied rows (only 0047's P03-B09 is given). They are internally plausible (0046 is 0045's I10-E01 sibling; sequential orders 7→9→10 fit 0047's "order 9"), but I cannot verify them from the packet — treat as **UNKNOWN/plausible**, not confirmed.

**5. All 25 synthetic facts have exact locators and actionable replacement guidance — PASS**
Every register entry 0047-FE1-001 … -025 carries a page/table locator that **resolves against the rendered text**, plus a concrete replacement action and a `Source status: SAMPLE/SYNTHETIC`. Spot-verified against rendered pages: FE1-003→p.8 評分量尺; FE1-006→p.3 thresholds sentence + p.8 bullets; FE1-004/011/017→p.5 評分構面與示範分數; FE1-012/018→p.6 履約檢核結果與判讀; FE1-013/019/021→pp.3,6; FE1-020→p.6; FE1-022→p.3 發現/原因/證據強度; FE1-023→p.7 結論表; FE1-024→pp.1,4,7; FE1-025→pp.3,7. All present. **Minor non-blocking:** the report body's 合成資料聲明 (p.4) lists replacement **categories**, not per-fact keys, and does not cite the FE1-xxx keys inside the DOCX; the keys/locators live in the register. Traceability is satisfiable at packet level but not wired into the body text.

**6. Arithmetic and conclusions agree — PASS (independently recomputed)**
See recalculation below. Every displayed figure reproduces exactly, and each judgment follows the report's own stated thresholds.

**7. Title-blind identification — PASS**
With title/filename/ID masked, the body still (a) reproduces the exact official requirement sentence (p.1 「本文件對應的查核要求」/「官方要求及分析範圍」), and (b) carries an I10-E02-specific *mechanism* — a cross-year analysis linking pre-decision criteria → reproducible selection rationale → signed contract/acceptance → post-performance review/improvement, scored per case. It cannot be moved unmodified to 0045 (a procedure/SOP, whose fields it explicitly declines to address) or 0048 (a meeting/approval record, which it explicitly states it is not), per p.2. **Fact + reviewer inference.**

**8. Real-vs-synthetic truth boundary — PASS**
Boundary is enforced at multiple points: document control line 「狀態：示範資料｜非本會實際紀錄…生效日期：未生效」 (p.1), 「示範資料｜非本會實際紀錄」 under the cited requirement (p.1), explicit non-inference statements (「不代表任何機構曾經辦訓、採購、簽約或完成改善」 p.1; 「不代表真實機構有改善趨勢」 p.3; 「證據強度只支持方法演練及表內算術核對；不支持機構實績、核准、簽章、採購合法性或第三方事實」 p.3), and the 資料狀態 column repeated on both case rows (p.6). All 25 register facts are labeled SAMPLE/SYNTHETIC. No passage claims REAL. **Fact.**

**9. Usability for administrators and evaluators — PASS**
First table 「先看這裡」 (p.1) gives 用途/使用人/使用時機/操作方式/最後得到的結果, with a 4-step operation («依資料字典核對原始文件，重算評分與履約檢核率，再按差距表確認改善責任與期限»). The dictionary (p.4–5) names the real originals to check; the p.7 table gives owner/deadline/KPI per gap; the p.7 追溯表 maps official text → result → evidence needed → location → review decision. No evaluation-engineering jargon. **Fact.**

**10. Material omission or misleading statement — PASS (no material defect; minor items logged)**
No statement materially misleads: synthetic values are consistently flagged and conclusions stay inside the source. Minor, **non-material** observations: (i) neighbour source-box IDs (P03-B07/P03-B10) are unverified (see #4); (ii) criterion naming differs between the short labels in the p.5 評分構面 table («需求與事前規準 / 選擇理由可重現 / 契約及驗收 / 履約檢討改善») and the long labels in the p.7 判斷依據 table / register («選擇前課程需求與評估準則 / 資源選擇理由可重現 / 採購、契約及驗收 / 履約後評估及改善追蹤») — mapping is inferable but not explicitly keyed; (iii) terminology varies (履約達成率 / 履約檢核率 / 履約檢核完成率 / 履約率) for the same 3÷4 metric; (iv) the third threshold branch («≥4.00 但檢核未全數完成») is defined but never exercised by either sample case; (v) «近年來» is demonstrated with only two synthetic years. None of these change acceptance.

---

## Arithmetic recalculation (from displayed data)
| Quantity | Report value | My recomputation | Agree |
|---|---|---|---|
| 2024 weighted score | 3.25 | 4·.25+4·.25+3·.25+2·.25 = 1.0+1.0+0.75+0.5 = **3.25** | ✓ |
| 2025 weighted score | 4.00 | 4·.25×4 = **4.00** | ✓ |
| Year-on-year score Δ | +0.75 | 4.00−3.25 = **0.75** | ✓ |
| 2024 履約 rate | 75.0% | 3÷4×100 = **75.0%** | ✓ |
| 2025 履約 rate | 100.0% | 4÷4×100 = **100.0%** | ✓ |
| Rate Δ | +25.0 個百分點 | 100.0−75.0 = **25.0 pp** | ✓ |
| Combined rate | 7/8 = 87.5% | (3+4)÷(4+4) = 7/8 = **87.5%** | ✓ |
| Mean score | 3.625 → 3.63 | (3.25+4.00)÷2 = 3.625 → 四捨五入 2dp = **3.63** | ✓ |
| 2024 judgment | 需改善 | 3.25 <4.00 ⇒ 需改善 | ✓ |
| 2025 judgment | 達示範檢視門檻 | 4.00≥4.00 and 4/4 complete | ✓ |
| Overall | 需改善 | mean 3.63<4.00 and combined 87.5%<full | ✓ |

All formulas are recoverable from the displayed figures; denominators, units, rounding and the N/A condition are stated (p.2, p.5). Weight-sum check: 25%×4 = 100% ✓. No arithmetic or logic contradiction found.

## Negative-neighbour rejection (explicit)
- **0045 / I10-E01 (procedure/manual):** rejected via p.2 bullet — 0047 supplies no procedure (no 啟動條件/控制點/異常升級/紀錄編號/交接); it is an annual-case analysis. Distinguishing, checkable fields cited. ✓
- **0048 / I10-E03 (meeting/approval evidence):** rejected via p.2 bullet — 0047 pp.5–7 are annual scores/rates/gaps, explicitly **not** meeting minutes, instructor-appointment approval, or large-procurement resolutions; the body directs readers to 0048 real originals. Distinguishing, checkable fields cited. ✓
Two neighbours rejected with distinct field sets — meets the "at least two" bar.

## SAMPLE/SYNTHETIC register sweep (25/25)
Keys 0047-FE1-001 through 0047-FE1-025 reviewed individually. All 25 carry: a field path, a stated synthetic value, a page/section/table locator that resolves against the rendered pages, a Basis note, a `Real replacement action`, and `Source status: SAMPLE/SYNTHETIC`. Grouped by scenario: SCALE-AND-REPORT (001–008), CASE-2024-A (009–014), CASE-2025-B (015–020), COMBINED-AND-TREND (021–022), FOLLOW-UP-PLAN (023–025). Register-internal arithmetic quotes (FE1-013/019/021) match my recomputation. **No entry is missing a locator or replacement guidance.** The register documents *labeling and replacement*, not real events — I do **not** treat its existence as evidence any real course, procurement, contract, or improvement occurred.

## Title-blind use identification
Masking title/filename/ID, the text self-identifies as I10-E02 by verbatim official sentence (p.1, p.7) and by a cross-year records-analysis mechanism distinct from I10-E01's procedure and I10-E03's meeting/approval record. It cannot be reused unmodified for a neighbour without losing its own declared function.

## Final overall verdict
**PASS** — the candidate is semantically and content-consistent with requirement I10-E02 (analysis-report genre) **within the supplied packet**, at SAMPLE/SYNTHETIC level. All 10 criteria pass; the only flagged items are minor and non-blocking (unverified neighbour box IDs, criterion-name variant mapping, terminology variance, one unexercised threshold branch, two-year «近年來» sample, register keys not cited in body). This verdict is limited by the input scope above: it does not certify binary SHA-256, the original DOCX, rendered pixels, font floors, or the external official source, and it is a semantic-layer opinion only — promotion remains subject to the canonical BUILD → STATIC/RECEIPT → independent review → CURRENT pipeline.

**Reviewed candidate SHA-256:** `b8cc8e4473e9cd7ad93f21c0cb9503865e683e3b802ac70577fbd8db3524d447`