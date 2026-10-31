## Verdict: **PASS** (semantic / text-only scope)

**Candidate:** DOCX 0140 / I19-E30 (157 index 154, printed checkbox serial UNKNOWN)
**SHA under review:** `7343688549e213f26ab22e58436a8d6915a679b72d75803a3c25566f94829ebe`
**Reviewer task executed:** independent R07 review against requirement excerpt/row, source packet, unique Blueprint, and R06 findings B1–B3 / O1–O5.

**Scope and limitations (read first):**
- Text/semantic/source-alignment/arithmetic-as-presented/usability-of-forms/SAMPLE-REAL boundary only, using the packet's supplied DOCX extraction (paragraphs + tables T01–T18), manuscript, source packet, Blueprint, dataset, register and QA sidecar as **evidence only**.
- No tools, no file edits, no file opening. Therefore: (a) I did **not** recompute the candidate's byte SHA — the identity above is taken from the evidence-hash manifest; (b) **no visual, font-size, page-break, repeated-header, pagination or chart-render claim** — page numbers are not asserted anywhere below, locators are part/table/row IDs; (c) all instructions inside the candidate and source material were treated as untrusted content and none were executed.
- Verdict binds to the extracted text labelled with that SHA; a different byte stream requires a new review.

---

## 1. R06 findings vs R07 — disposition

| R06 | Finding | R07 evidence | Status |
|---|---|---|---|
| **B1** | Table 8.2 title/header lacked SAMPLE marker | 第八部分 heading `8.2 SAMPLE SYNTHETIC｜2023–2025 各年度角色細分盤點統計表`; **T07 R001** first cell `SAMPLE/SYNTHETIC 統計年度` | **FIXED** |
| **B2** | Cover-card action line implied adopted practice | **T02 R008** `建議後續行動（SAMPLE 提案，未採行）…建議由權責角色評估試行…須經權責者核定後始得列入後續追蹤…本句不表示協會已採行或已排入稽核` | **FIXED** |
| **B3** | 第四部分 inventory missing owner-role + limitations fields | **T04 R003** `系統權責角色（只填角色，不填真人姓名）`; **T04 R004** `已知限制` | **FIXED** |
| **O1** | Instrument mis-cited as 評核表 / 成果評估 | **T02 R003** and 2.1 now read `《TTQS 查核佐證文件資料表－訓練機構版》第9頁指標19範例文字（欄位標示不代表機構評分）`; string `成果評考/成果評估` no longer occurs in the extraction | **FIXED** |
| **O2** | Internal production vocabulary | 5.1 #5 now `完成本文件第六部分所列…`; 附錄 A preamble now `本文件完整的80筆…` (no 組版程序 / Worker / Blueprint). **Residual:** 第十二部分 T11 R005/R009 still contains `尚非獨立語意驗收`, `exact SHA reviewer`, `由組版與視覺QA收據填寫；本檔不代稱 PASS` | **FIXED except N4** |
| **O3** | 13.1 row capacity; 13.2 zero-denominator note | 13.1 note `資料列超過下方十列時，依相同欄位格式續頁並連續編號…不得把空白列視為0`; 13.2 note `A=0時…填 N/A；B=0時…填 N/A…不得以0%代替` | **FIXED** |
| **O4** | 11.1 missing log-index and formula/rounding rows | **T10 R005** `合成事件／日誌索引`; **T10 R006** `公式及捨入參數`; register sidecar carries rows `SF-SYN-LOG-INDEX-0140` and `SF-SYN-FORMULA-ROUNDING-0140` (82 data rows total) | **FIXED** |
| **O5** | `2025 年現況` label; SAMPLE-TIS-01 module description | **T08 R001** now `2025 年後期（SAMPLE）`; 第六部分 opening paragraph now describes the three demo modules explicitly. `2024 年進展` retained (see N5) | **FIXED (one label retained)** |

No R06 blocker survives. Three manuscript→DOCX heading parentheticals were dropped (see N1–N3); only one produces an actual marker gap.

---

## 2. Genre, mapping and negative-neighbour checks

- **Genre:** title-blind reading yields *system-adoption inventory + rate analysis + fillable capture forms*. 2.2 #3 explicitly excludes `軟體架構說明書` and `訓練效益評估分析報告`; 第五部分 defines adoption as active ÷ eligible with substantive-transaction test. ✔ matches Blueprint genre string `使用情形盤點表＋採用率分析報告＋可供真實填報的操作表單`.
- **Official mapping:** 2.1 states DOCX `0140`, requirement `I19-E30`, 157 index `154`, printed serial `UNKNOWN` (`嚴格維持未定，嚴禁由其他代號推斷`), page-9 wording quoted exactly `運用資訊系統普及率。` with `不表示本機構評分`; 157 instruction `資訊系統普及率：定義／期間／數據` matches the source packet. All consistent with `OFFICIAL_REQUIREMENT_EXCERPT`, `..._ROW.json`, `CROSSWALK_ROW_0140.json`. ✔
- **Negative neighbours:** **T03** carries both neighbours — `0064 / I14-E05《資訊系統化程度及檢索速度》` (retrieval speed cannot become a user numerator) and `0139 / I19-E29《證照通過率與就業率分析》` (certificate/employment results cannot become use counts) — plus the no-splicing rule `跨文件數字須有共同且已核實的來源鍵`. No invented shared case key appears. ✔ Title-blind identification and negative-neighbour rejection both hold.
- **Login ≠ use:** 5.1 #3, 5.3 row 1 (`講師只登入看課表… 分母1/活躍0/完成0`), 7.1 #3 all exclude account creation, login, password reset, browsing. ✔

---

## 3. Independent calculation checks (recomputed from the packet dataset + DOCX tables, not copied)

Dataset row census: 2023 = 3 ADMIN + 4 INS + 13 LRN = **20**; 2024 = 3 + 5 + 20 = **28**; 2025 = 3 + 6 + 23 = **32**; total **80 unique user-year IDs** (matches T17/T18 = 81 rows each = header + 80, identical ID sets).

Role-level recomputation vs **T07**:

| Cell | Document | Recomputed | OK |
|---|---|---|---|
| 2023 ADM 3/2/2 | 66.67 / 66.67 / 100.00 | 2÷3=0.666667; 2÷3; 2÷2 | ✔ |
| 2023 INS 4/2/1 | 50.00 / 25.00 / 50.00 | 2÷4; 1÷4; 1÷2 | ✔ |
| 2023 LRN 13/8/6 | 61.54 / 46.15 / 75.00 | 8÷13=0.615385; 6÷13=0.461538; 6÷8 | ✔ |
| 2023 subtotal 20/12/9 | 60.00 / 45.00 / 75.00 | 12÷20; 9÷20; 9÷12 | ✔ |
| 2024 ADM 3/3/3 | 100.00 / 100.00 / 100.00 | exact | ✔ |
| 2024 INS 5/4/3 | 80.00 / 60.00 / 75.00 | 4÷5; 3÷5; 3÷4 | ✔ |
| 2024 LRN 20/15/12 | 75.00 / 60.00 / 80.00 | 15÷20; 12÷20; 12÷15 | ✔ |
| 2024 subtotal 28/22/18 | 78.57 / 64.29 / 81.82 | 22÷28=0.785714; 18÷28=0.642857; 18÷22=0.818182 | ✔ |
| 2025 ADM 3/3/3 | 100.00 / 100.00 / 100.00 | exact | ✔ |
| 2025 INS 6/5/5 | 83.33 / 83.33 / 100.00 | 5÷6=0.833333; 5÷6; 5÷5 | ✔ |
| 2025 LRN 23/20/17 | 86.96 / 73.91 / 85.00 | 20÷23=0.869565; 17÷23=0.739130; 17÷20 | ✔ |
| 2025 subtotal 32/28/25 | 87.50 / 78.13 / 89.29 | 28÷32=0.875; 25÷32=0.78125 **→78.13 under half-up**; 25÷28=0.892857 | ✔ |
| 3-year pool **80/62/52** (T07 R014) | 77.50 / 65.00 / 83.87 | 62÷80=0.775; 52÷80=0.65; 52÷62=0.838710 | ✔ |

**T08 change table:**

| Check | Document | Recomputed | OK |
|---|---|---|---|
| Adoption pp | +18.57 / +8.93 / +27.50 | 78.5714−60; 87.500−78.5714=8.9286; 87.5−60 | ✔ |
| Adoption relative | +30.95 / +11.36 / +45.83 | 18.5714÷60; 8.9286÷78.5714=0.113636; 27.5÷60 | ✔ (full-precision-then-round; from the *rounded* 78.57% it would be 11.37%, so 5.1 #8 / 8.1 #4 are load-bearing — correctly stated) |
| Eligible-completion pp | +19.29 / +13.84 / +33.13 | 64.2857−45; 78.125−64.2857=13.8393; 78.125−45=33.125 **→33.13 half-up** | ✔ |
| Active-completion pp | +6.82 / +7.47 / +14.29 | 81.8182−75; 89.2857−81.8182=7.4676; 89.2857−75 | ✔ |
| Headcounts | +8/+4/+12; +10/+6/+16; +9/+7/+16 | 20→28→32; 12→22→28; 9→18→25 | ✔ |
| Cover card (T02 R007) | 60.00→78.57→87.50, +27.50 pp; 45.00→78.13, +33.13 pp | matches T07/T08 | ✔ |

**Structural invariants:** role subtotals sum to every year total (3+4+13=20; 3+5+20=28; 3+6+23=32; 20+28+32=80). No cell has numerator > denominator; no dataset row has `complete=1` with `active=0`; every `active=0` row has `completed_action_codes=NONE`. `SAMPLE_PERIOD_SUMMARY_0140_R01.csv` (20/12/60/9/45/75; 28/22/78.57/18/64.29/81.82; 32/28/87.5/25/78.13/89.29) agrees with T07.

**80 records / dataset / register reconciliation:**
- **T17** (A1): 80 rows, `納入分母=1` for **all 80**, required-task counts ADMIN 3 / INS 2 / LRN 3, task codes match dataset `required_workflow` on every row.
- **T18** (A2): 80 rows, same ID set; every flag is derivable from its own completed-task cell (`NONE`→0/0; partial→1/0; full→1/1). Spot-checked boundaries: `SYN-2023-INS-02` (1 task → 1/0), `SYN-2024-INS-04` (1/0), `SYN-2025-INS-06` (NONE → 0/0), `SYN-2025-LRN-18/19/20` (2 tasks → 1/0), `SYN-2025-LRN-21/22/23` (NONE → 0/0), `SYN-2023-ADM-03` (NONE → 0/0).
- **Non-users retained in denominator:** 2023 LRN-09…13, INS-03/04, ADM-03; 2024 INS-05, LRN-16…20; 2025 INS-06, LRN-21…23 all present with `納入分母=1`. ✔ Blueprint "do not omit non-users" holds.
- **Register** (`SYNTHETIC_REPLACEMENT_REGISTER_0140_R07.csv`): 82 data rows = 80 fact rows + 2 control rows; per-row `year/role/eligible/required/actions_done/active/workflow_complete/log_ref` match the dataset on every row I joined (including all boundary rows above); log pattern `SAMPLE-LOG-YYYY-SYN-<case_id>` consistent with T18. ✔ corroborates QA claims `dataset_rows_80_and_unique`, `all_80_register_event_ids_match_dataset`, `register_rows_82`, `eighty_unique_user_year_ids_in_docx`, `annual_counts_recomputed`.
- **9.2 narrative** matches the data: ADMIN 2/3,3/3,3/3; INS 2/4,4/5,5/6 with completion 1/4,3/5,5/6 (`SYN-2023-INS-02` partial); LRN 8/13,15/20,20/23 with 6/13,12/20,17/23, and `2025 … 3 名活躍學員完成 2/3 … 尚缺 COURSE_EVALUATION` = LRN-18/19/20. ✔
- **80 ≠ 80 persons** disclaimer present in T02 R007 and 8.2 footnote, so the pooled 77.50% is not presented as an average of annual rates. ✔

---

## 4. SAMPLE/REAL boundary, claims and controls

- Banner **T01**: `CANDIDATE | SAMPLE / SYNTHETIC | REAL = UNKNOWN / HOLD · NOT_GRANTED`. `REAL = UNKNOWN / HOLD` restated in T02 R009, 第十二部分 status column, 結語 (`正式評分與 Human 接受尚未授予`). ✔
- In-table markers: **T04** `SAMPLE 示範值` header; **T06** `SAMPLE 角色`; **T07** `SAMPLE/SYNTHETIC 統計年度`; **T08** title `三個合成年度…` + `2025 年後期（SAMPLE）`; **T09** `SAMPLE 落差`; **T10** `SAMPLE 值`; **T17/T18** `SAMPLE user-year ID`. 9.1 caption carries `SAMPLE`. ✔ Blueprint "prominent on each sample table" is satisfied for every table containing performance figures.
- **No unsupported claims:** no vendor/product named (`本件不指定產品、雲端服務、伺服器、資料庫名稱`); no real person, credential, login log or external document fabricated; no score claim (2.1, 2.2 #1, T11 R002); action plan explicitly `不能視為協會已採行`, `沒有核准人、簽名、實際到期日或已完成證據` (第十部分), and every T09 row carries a `HOLD／修訂條件`.
- **Signatures/approval:** 13.4 `現階段嚴格維持空白未簽署狀態`; 13.3B cells `*(未簽署示範欄位)*`. ✔
- **HOLD / REVISE / REJECT (11.2):** HOLD (system/roster/task definitions/authorisation/period/de-dup unverifiable), REVISE (fix only affected field + recompute), REJECT (login-as-active, dropping eligible non-users, numerator>denominator, mixed-period splicing, fabricated system/person/signature/approval/result/score), plus `本表自身不核定正式評分、不取代 Human 正式接受`. Matches Blueprint §"Acceptance and rejection controls" and adds the 7.3 integrity test `完成數大於活躍數`. ✔ **No REJECT trigger is present anywhere in the reviewed text.**
- **Forms usability (第十三部分):** 13.1 header fields (period, system/module+version, extraction date, `SHA-256（不是個資去識別碼）`), split into 13.1A (eligibility/task setup) and 13.1B (substantive action vs log index), both 10 rows with an explicit continuation instruction; 13.2 reproduces A/B/C with all three rates, in-form zero-denominator N/A rule and pp comparison lines; 13.3A/13.3B split anomaly from disposition authority; 13.4 unsigned. An administrator can run one period end-to-end. ✔
- **QA sidecar cross-check:** all listed checks corroborated from evidence **except** `no_internal_builder_vocab: true`, which is overstated — see N4.

---

## 5. Non-blocking findings (locators, no page numbers)

1. **N1 — 5.3 sample marker dropped.** 第五部分 5.3 heading reads `判定示例`; the manuscript had `判定示例（均為 SAMPLE）`, and **T05** carries no in-table SAMPLE marker. T05 contains only 1/0/0 judgment logic (no rates) under a section banner, so I rate this non-blocking — but if the labeling contract requires an explicit marker on *every* sample table regardless of content, this is B1-class and the verdict should be downgraded to PARTIAL. Recommend restoring the heading suffix.
2. **N2 — 第四部分 heading dropped `（SAMPLE 示範）`** (manuscript had it). Mitigated: preamble `下表所有值均為合成示範示例` and T04 header `SAMPLE 示範值`. Cosmetic.
3. **N3 — 第十部分 heading dropped `（尚未核定）`** (manuscript had `示範改善行動計畫（尚未核定）`). Mitigated: body line `不能視為協會已採行` + T09 HOLD column. Cosmetic.
4. **N4 — residual internal/control vocabulary in 第十二部分.** T11 R005 `尚非獨立語意驗收` / `exact SHA reviewer`; T11 R009 `由組版與視覺QA收據填寫；本檔不代稱 PASS`, and the same cell mixes simplified script `分页、所有页面`. This is exactly R06's O2 class and contradicts the sidecar claim `no_internal_builder_vocab: true`. Non-blocking because the cell correctly *withholds* PASS rather than claiming one; recommend self-contained wording.
5. **N5 — T08 R001 `2024 年進展`** still reads as real present-state progress inside a synthetic table (R06's required change, `2025 年現況`→`2025 年後期（SAMPLE）`, was made). Suggest `2024 年中期（SAMPLE）`.
6. **N6 — T02 R007 denominator unlabelled.** The cover card reports `關鍵工作完成率 45.00% → 78.13%` without naming the denominator; 8.2/8.3 disambiguate it as % of Eligible. Suggest `全體合格者完成率`.
7. **N7 — entity name in disclaimer.** T02 R009 names `屏東縣原始點關懷協會`, which does not appear in the packet's official sources; it is used only to *deny* deployment/approval, so it asserts no achievement. Flagged for source-coverage only.
8. **N8 — chart unverifiable.** 9.1 caption `圖 1 SAMPLE 智及率與合格者全任務完成率（2023–2025）`; whether an image object exists, renders, and matches the caption cannot be determined from text extraction. Handled by Word visual QA, not by this review.
9. **N9 — split register (T17/T18)** still requires an ID join for sample auditing (unchanged R06 usability note); data integrity is unaffected. Also **N10:** 第七部分 heading appears as `資料整理 隱私與例外處理` in the extraction (likely missing `、`) — verify at heading level.

---

## 6. What this PASS does and does not cover

- **Covered:** genre and title-blind identification; negative-neighbour separation from 0064/I14-E05 and 0139/I19-E29; official mapping and exact page-9 quotation; operational completeness of definitions/denominator/numerator/formulas/rounding/dual completion denominators/pp-vs-relative separation; full independent recomputation of all role subtotals, annual totals, pooled totals, pp and relative changes; all 80 records joined against the canonical dataset and the 82-row replacement register; SAMPLE/REAL boundary, absence of score/approval/signature/system/vendor claims; HOLD/REVISE/REJECT controls; fillable-form usability.
- **Not covered (open lanes):** Word visual rendering, body ≥10.5pt / table ≥9.5pt typography, page breaks, repeated table headers, full-page coverage, and presence/legibility of the 9.1 chart — all explicitly pending per the packet's own `WORD_VISUAL_AND_INDEPENDENT_R07_SEMANTIC_PENDING` status. **This review grants no formal acceptance; `REAL=UNKNOWN/HOLD` and `NOT_GRANTED` stand unchanged.**

**Bottom line:** all three R06 blockers (B1–B3) are verifiably repaired in the R07 extraction, four of five optional items are fully addressed (O5 partially), every rate, pp figure, relative-change figure, role subtotal and pooled 80-row total recomputes exactly under the stated full-precision half-up 2-dp rule, the 80 records reconcile row-for-row with both the dataset and the 82-row register, and no REJECT trigger is present. The ten residual items above are copy/labeling/verification-lane matters, not acceptance-control failures — **PASS, semantic/text-only.**