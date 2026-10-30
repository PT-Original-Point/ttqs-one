## Review return — TTQS_ONE_0142_R06_REVIEW_20261029

**Candidate SHA256 echoed:** `3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e`

**Scope limits applied:** This review used only the supplied extracted text. No tools were run, no files were read, edited, or hashed. No page, layout, font, or Word rendering inspection is claimed. No official score, no formal acceptance, and no promotion authority is exercised here.

**Overall verdict: PARTIAL**

Content quality against I19-E32 is strong and the arithmetic is fully reproducible; the verdict is held back by (a) an unresolved exact-SHA evidence binding inside the packet itself, and (b) several Blueprint-required fields that are absent as fields.

---

### Criterion-by-criterion

**1. Exact I19-E32 purpose, genre, neighbor separation — PASS**

- Purpose statement matches the official wording: "以三個連續完整會計年度的可調回財務原件及可核對帳簿，判斷營業額/營業收入是否逐年增加" (唯一佐證目的 paragraph), and explicitly disclaims: "此文件不是財報、會計簽證、官方評分或協會核准紀錄".
- Three years are enumerated per year in 表 2 "REAL 財務來源登錄清冊（依完整年度逐年列示）", rows `2023` / `2024` / `2025`.
- Genre is correct: a reconciliation report with source registry, account mapping, ledger tie-out, formula table, decision rules, and exception/hold register — not a blank form or questionnaire. Contrast 表 4 heading: "SAMPLE 模擬財報/帳簿勾稽表（算術示範，非真實查核）".
- Neighbor requirements are actively rejected rather than borrowed (表 7, rows `0139 / I19-E29 / 索引 153`, `0140 / I19-E30 / 索引 154`, `0141 / I19-E31 / 索引 155`).

**2. Operational usability (retrieval, roles, mapping, reconciliation, formulas, decision/stop, replacement) — PASS (mechanics present; two minor control-field notes below)**

- Source retrieval/locator: 表 2 columns `完整會計年度 | 應取得來源及版本 | 頁碼/科目列/原件位置 | 幣別、單位、會計基礎 | 核准與角色/日期 | 差異及狀態`.
- Roles are title-based, no invented names: 表 1 rows `資料保管/財務行政職務`, `財務權責職務`, `獨立覆核職務`, `文件控管職務`, each with a "完成證據 / 權限界線" cell, e.g. 文件控管: "不得自行簽核、核准或宣稱正式生效".
- Classification boundaries: 表 3 covers 服務/營業收入, 捐款/指定捐款, 政府/民間補助, 會費/會員收入, 利息及投資收益, 代收款/代付款, 退款/折讓/沖銷/重分類, each with `REAL 分類現況` and `停止狀態`.
- Annual reconciliation: 表 4 `模擬財報列 | 模擬明細/總帳列 | 模擬差額 | 證據解讀`.
- Formulas with numerator/denominator shown in-cell: 表 5, e.g. `120,000 / 1,200,000 × 100 = +10.00%`.
- Decision and stop/release: "真實判定規則" (§5), 表 2 "解除條件", 表 6 (7 trigger rows) with `解除所需證據`.
- Replacement workflow is explicit and countable: 附錄 A / 表 8 "本附錄將 19 個示例/控制資料逐列綁定…" — 12 financial rows + 4 derived-percentage rows + `SYN-0142-CURRENCY-UNIT` + `SYN-0142-ACCOUNT-MAPPING-ASSUMPTION` + `SYN-0142-DOCUMENT-CONTROL-DATE` = 19, consistent with the stated count.
- Numbered execution order 1)–6) under "執行順序與停止點" is operable as a procedure.

**3. Numerical and cross-table consistency; operating vs other vs total income — PASS**

Every figure in the extracted text re-computes exactly, with no cross-table mismatch:

- Year totals: 1,200,000 + 280,000 = 1,480,000; 1,320,000 + 260,000 = 1,580,000; 1,452,000 + 300,000 = 1,752,000 (表 4 rows + "年度總額驗算" paragraph) — all correct.
- 2024 YoY: 120,000 / 1,200,000 = 10.00% — correct.
- 2025 YoY: 132,000 / 1,320,000 = 10.00% — correct.
- Operating cumulative: 252,000 / 1,200,000 = 21.00% — correct, and consistent with 1.10 × 1.10 = 1.21.
- Total-income cumulative: 272,000 / 1,480,000 = 18.378…% → 18.38% — correct, and equal to 1,752,000 / 1,480,000 − 1.
- Denominators are the prior-year/base-year figures, not the later year; base year 1,200,000 > 0; two-decimal display is applied; NTD is declared (表 4 cells "1,200,000 NTD"; `SYN-0142-CURRENCY-UNIT` = 新臺幣（NTD）).
- Category separation holds throughout: "其他收入全程獨立列示，不作營業收入趨勢的替代分子" (§4), 表 5 row `總收入三年累計變化（分開列示）` with "不得替代營業收入趨勢", and §6 "總收入、捐款、補助、會費或一次性收入只作分類後的附帶核對；不能掩蓋營業收入下降". The sample even demonstrates the needed contrast (total growth 18.38% < operating growth 21.00%, because 其他收入 declines 280,000 → 260,000), so the "total income must not mask operating revenue" rule is functionally exercised, not just asserted.

**4. SAMPLE/SYNTHETIC vs REAL, authorization, approval, score, acceptance boundaries — PASS (with one low-severity wording tension)**

- Cover status block: "尚未取得協會授權三年度財報…因此 REAL=UNKNOWN/HOLD，不能據此宣稱本會營業額成長".
- 文件控制卡 row `REAL 證據` = `UNKNOWN/HOLD`; `合成資料` = `SAMPLE/SYNTHETIC；僅驗算`; `核准 / 簽署` = `未主張；無簽核紀錄`; `正式接受` = `NOT GRANTED`; `官方評分` = `NOT ASSIGNED`; `生效狀態` = `NOT ISSUED`.
- §6 keeps three separate registers: "SAMPLE 算術" / "REAL 財務證據：UNKNOWN/HOLD" / "TTQS 評分 / 正式接受：NOT ASSIGNED / NOT GRANTED", and adds "此結果只證明示例公式可重算".
- Every 表 8 row carries `狀態：UNKNOWN/HOLD` and `替換日期：尚未替換；未提供授權 REAL 來源`; the last row is explicitly non-financial: "不適用：控制資料，不是財務事實".
- Privacy/authorization limit is registered: 表 6 row "原件含個資、帳戶資訊或未授權公開內容 → 資料保管/隱私權責職務；停止公開同步".
- Low-severity tension: §3 says "本表把 SAMPLE 算例中的「營業收入」視作一個計算欄位，**不將它映射成協會實際服務收入**", while 表 8 row `SYN-0142-ACCOUNT-MAPPING-ASSUMPTION` says "示例假設：「營業收入」欄位**對應「服務收入」**；非協會分類決定". Both are sample-scoped, so no truth-boundary breach, but the two sentences read as contradictory and should be reworded to one formulation.

**5. Required fields, exception cases, rejection/hold criteria; no fabrication — PARTIAL**

Adequate:
- Exception coverage is broad and correct: 缺件, 映射未確認, 帳表不一致/無憑證調整, 年度不連續/短年度, 分母 ≤ 0 or basis/currency mismatch, 捐款/補助/會費/利息/代收款混入, 個資/未授權公開 (表 6, all 7 rows).
- Denominator ≤ 0 → N/A without estimation: "前期分母小於或等於 0…該比較結果為 N/A；不得換算、推估".
- Rejection-side protections are present: 表 7 blocks neighbor substitution; 表 1 文件控管 "不得自行簽核、核准"; `官方評分 NOT ASSIGNED` plus 獨立覆核 "不得代替官方評分".
- No fabricated people, signatures, certificates, statements, approvals, or results: all persons are job titles (表 1); no signature lines are claimed complete; 表 2 states "各格均明列缺件，不以空白表示完成".

Gaps against the Blueprint's required fields (these are the basis for PARTIAL):
- 例外停審 table is missing the required **期限欄** and **重算日** — 表 6 provides only `觸發條件 | 影響範圍 | 責任/狀態 | 解除所需證據`; Blueprint lists "缺件/差異、受影響年度、待辦責任職務、**期限欄**、解除證據、**重算日**".
- 科目映射 table lacks a dedicated **原帳科目** column (actual booked account code/name) and a **權責確認及版本** column — 表 3 has `科目/收入類型 | SAMPLE 演示處理 | REAL 分類現況 | 真實核實依據 | 停止狀態`, so the "whether included in 營業額" and "basis" elements are present but the booked-account identity and mapping version are not.
- 年度勾稽 table lacks a discrete **調整** column and a per-year **原件位置** pointer — 表 4 has no adjustment column, and original-document location lives only in 表 2; adjustments are referenced only in 表 3's last row and 表 6.
- 趨勢算式 table folds **單位** into cell text rather than a unit column, and **可比性結論** is represented only by `可用範圍` ("SAMPLE 僅；REAL 未核") — acceptable in substance, weaker as a checkable field.
- No anchor to the **three most recent** complete fiscal years. §1 says only "三個連續完整會計年度"; the 表 2/附錄 A window is fixed at 2023–2025, and there is no rule for "if the latest year is not yet closed/attested, step back and re-anchor the window". §6's "不得改選有利期間" mitigates cherry-picking but does not define the anchor. Also 附錄 A hard-codes FY boundaries "2023-01-01 至 2023-12-31" as synthetic values, which is fine for a sample but does not itself establish the association's fiscal year (correctly still UNKNOWN in 表 2 `會計基礎：未知 / HOLD`).

**6. Title-blind identification and negative-neighbor test — PASS (minor note on source_id/fact_id)**

- Title-blind: from title alone ("組織近三年營業額與收入趨勢核對報告") plus §1 and 表 2, a blind reader would identify a three-year operating-revenue trend reconciliation against source financial statements. It cannot be mistaken for a satisfaction survey, system-usage log, or exam/employment-rate table; no such content appears anywhere in the body.
- Negative-neighbor test passes in the required direction: 表 7 states for `0141 / I19-E31 / 索引 155` "不替代營業額趨勢；不得借用其樣本、期間或分數", and §8 adds "沒有共同真實來源，不推定數字、日期或結論相同".
- Minor: Blueprint §10 requires cross-document facts to carry `source_id/fact_id`. §8 names both identifiers, but no `source_id` field exists in 表 2 or 表 8 (表 8 carries only `sample_fact_id`). The mechanism is asserted, not implemented as a field.

**7. Material semantic gaps vs legitimately-held REAL evidence — PARTIAL**

- Legitimately unavailable and correctly held (not defects): audited/attested financial statements, chart of accounts, ledger/income detail, currency and accounting basis, page/account locators, approval status, tie-out differences, mapping decisions, reviewer roles and dates, fiscal-year-end confirmation, and the resulting official score/acceptance. 表 2 states per year: "表帳差異：未能檢查；不得推定為零", and 表 2 does not convert missing data into zeros or estimates.
- Genuine completeness gaps: the four required-field omissions in criterion 5 (表 6 期限/重算日; 表 3 原帳科目/版本; 表 4 調整/原件位置; 表 5 單位) and the unimplemented `source_id` field in criterion 6. These are contract deviations, not arithmetic or boundary failures, and they are repairable without touching the verified sample numbers.
- One additional INFO item: 表 4's `模擬差額 = 0 NTD（演示差額）` cells have no `sample_fact_id` in 附錄 A. They are derived (identical columns), so this is derivable rather than unregistered, but it is the one numeric cell family not explicitly bound to the replacement register.
- Extraction caveat, not a finding: 表 2 cells run text together (e.g. "年度財報：未提供查核/簽證報告：未提供收入明細/總帳：未提供"). This is most likely flattening of in-cell line breaks during text extraction; whether the DOCX genuinely lacks separators is **UNKNOWN** without readback and cannot be decided from extracted text.

---

### Material findings (severity + locator)

| # | Severity | Locator | Finding |
|---|---|---|---|
| F1 | **Blocking (evidence binding)** | Packet header `CANDIDATE_SHA256=3781cb4…` vs source packet §既有候選讀回 ("完全同 SHA-256 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6，44,970 bytes，最後變動 2026-10-04；版本1.0" and "保留此 SHA…不因來源包更新重建 DOCX") | The packet's own readback evidence describes a **different** artifact (v1.0, 2026-10-04, 59f9b5…), while the reviewed body declares `版本 / 狀態 R06 / CANDIDATE` and `候選建置日 2026-10-28`. No byte size, mtime, page count, or recomputed digest is supplied for `3781cb4…`. The mapping from the extracted text to the reviewed SHA is therefore **UNKNOWN**, and the packet's "do not rebuild" instruction conflicts with reviewing a v1.0→R06 rebuild. |
| F2 | Major | 表 6 header row `觸發條件 | 影響範圍 | 責任/狀態 | 解除所需證據` | Missing the Blueprint-required **期限欄** and **重算日**, so exception items have no due-date or recompute-date control. |
| F3 | Major | 表 3 header row `科目/收入類型 | SAMPLE 演示處理 | REAL 分類現況 | 真實核實依據 | 停止狀態` | Missing **原帳科目** (booked account code/name) and **權責確認及版本** columns; mapping version is not recorded anywhere. |
| F4 | Minor–Major | 表 4 header row `年度 | 項目 | 模擬財報列 | 模擬明細/總帳列 | 模擬差額 | 證據解讀` | No discrete **調整** column and no per-year **原件位置** pointer; adjustments appear only as prose in 表 3's last row and 表 6. |
| F5 | Minor | §1 "核對對象限於同一組織三個連續完整會計年度" + 表 2 rows `2023/2024/2025` | No rule anchoring the window to the **three most recent** complete fiscal years, nor to rolling the window back when the latest year is unaudited or incomplete. |
| F6 | Minor | §3 "不將它映射成協會實際服務收入" vs 表 8 row `SYN-0142-ACCOUNT-MAPPING-ASSUMPTION` "示例假設：「營業收入」欄位對應「服務收入」" | Two sample-scoped sentences read as contradictory about whether a mapping has been assumed; no truth-boundary breach, but the wording should be unified. |
| F7 | Minor | §8 "只有共同、授權且可追溯的來源才可用 source_id/fact_id 建立跨文件連結" vs 表 2 / 表 8 fields | `source_id` is named as a control but exists as no field in any table; only `sample_fact_id` is implemented. |
| F8 | Info | 表 4 `0 NTD（演示差額）` cells | Demo differences are not individually listed in 附錄 A's 19-row register (derivable, so low risk). |
| F9 | Info / UNKNOWN | 表 2 cell text ("年度財報：未提供查核/簽證報告：未提供…") | Possible genuine separator loss vs extraction flattening. Cannot be determined from extracted text; no layout or readability claim is made here. |

---

### Is a blocking defect identifiable?

- **Blocking content defect in the body text: none identifiable.** Criterion 1, 2, 3, 4, and 6 pass; all sample arithmetic reproduces exactly; SAMPLE/REAL, approval, score, and acceptance boundaries are stated consistently and are not overstated; no fabricated persons, signatures, statements, approvals, or results appear.
- **Blocking item: F1, evidence binding — UNKNOWN.** The reviewed body cannot be tied to `3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e` from the supplied material, and the packet's readback section describes a different SHA/version. This is a review-infrastructure/provenance defect, **not** a licence to mutate the DOCX: per the governing rules, defect classes of this kind never authorize document mutation by themselves.
- Consequently: **PASS cannot be granted at this gate.** Recommend re-issuing the packet with (i) readback of `3781cb4…` (recomputed digest, byte size, mtime, version, page count), (ii) the four required-field repairs for F2–F4 as a separate, bounded content delta if the field gaps are to be closed before promotion, and (iii) a unified formulation for F5–F7. The verified sample arithmetic and all SAMPLE/REAL boundaries need no rework.

### Explicitly UNKNOWN in this review

- Whether the extracted text corresponds byte-for-byte to `3781cb…`; the actual DOCX digest, size, mtime, version, and page count.
- Whether `SOURCE_PACKET_SHA256=e3e8b3a8…` and `UNIQUE_BLUEPRINT_SHA256=4841161d…` match the supplied text (asserted only).
- Latin/print checkbox serial (declared `UNKNOWN` in both packet and body).
- All layout properties: page count, pagination, table splitting, body ≥10.5 pt / table ≥9.5 pt font floors, header/footer, TOC, visual readability.
- Whether authorized REAL financial originals exist anywhere in the corpus — the packet states "REAL=UNKNOWN/HOLD" and "其他位置是否存在經授權的真實財務原件未全域盤點".

### Authority statement

This is a candidate semantic review only. It assigns no official score, grants no formal acceptance, does not promote to CURRENT, and does not certify the artifact's SHA or layout.