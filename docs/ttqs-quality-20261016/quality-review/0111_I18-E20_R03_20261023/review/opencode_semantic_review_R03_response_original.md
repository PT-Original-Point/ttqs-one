## Independent semantic review — 0111 / I18-E20 / R03

### Review scope, method, and identity binding

**SHA independently rehashed: YES.** I re-read the candidate bytes with `Get-FileHash` before reviewing:

- `f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50`, 75015 bytes — **matches the asserted SHA and byte count exactly.** This verdict is bound to that SHA.

**Extraction independently reproduced (not trusted on faith):** I re-extracted the DOCX with python-docx 1.2.0 and machine-diffed it against the packet:

- 135 total paragraphs, 113 non-empty → **all 113 packet paragraph claims matched byte-for-byte at their claimed indices** (22 claimed gaps: P013, P033, P041, P046, P054, P058, P060, P063, P066, P072, P076, P077, P080, P085, P088, P089, P092, P113, P118, P127, P130, P133 — all confirmed empty in the DOCX).
- 16 tables, row counts `[7,8,3,5,11,7,9,9,11,3,8,8,6,54,8,7]` and column counts `[3,5,8,5,7,7,8,7,3,7,6,5,6,6,5,5]` → **0 table-row mismatches, 0 missing rows.**
- Manifest cross-checks also rehashed and matched: `technical_qa_0111_R03.json` = `a67eee3e…2f36`, manuscript `…_R03.md` = `66309d7b…cc92` / 38993 bytes, `official_source_page7_text.txt` = `78a60101…d9eb`.

**Not performed / excluded:** Word-native render is BLOCKED for R03 (0 page images), so **no visual, layout, pagination, or font-rendering PASS is claimed or implied**; the technical QA receipt and the export-blocker receipt were read as evidence only and are **not** converted into any semantic finding. No files were edited, no Computer Use, no replacement manuscript generated, no formal association acceptance asserted.

---

### Q1 — Genre and direct answer to the official checkbox

**PASS.** Genre is 分析／評估報告 — 特殊績效及社會面成果證據登錄表, evidenced by decision question §1.3 (P014–P019), operational definition §2.2 (P025), evidence grading §4.1, per-record registry 表7/表8, recomputation 表9, and action/trace tables 表11/表12/表13.

The exact official sentence is quoted **verbatim** at P022: I extracted all three occurrences of the `提出目標客戶及學員對訓練達…` family in `source/official_source_page7_text.txt` and compared codepoints — occurrence at index 383 (the 特殊績效 item) is **character-identical to the candidate's 29-character quote**, including U+6236 `戶` and the full-width punctuation, after whitespace normalization. No rewrite, no abbreviation, no historical-draft variant (P023 correctly says 頁 7, `PDF_TEXT_EXACT_PAGE_MATCH`, and explicitly refuses to equate E-levels with the official 4-point band).

Both required subjects are answered separately: 目標客戶 → 表7/表9 (3/8→6/8) and 學員 → 表8/表9 (6/8), with the three proof elements enumerated at T02-R08 (目標客戶 / 學員 / 社會面·其他).

### Q2 — Unique Blueprint conformance

**PASS.** Every Blueprint `required_sections` item is present and non-empty: §1 摘要·用途·決策問題, §2 官方要求及範圍, §3 資料來源·樣本·納入排除, §4 指標定義·分母·計算, §5 完整示範資料及逐步計算, §6 分群/趨勢/差異, §7 圖表解讀及品質限制, §8 發現·原因·證據強度, §9 例外/歧異/缺件/更正, §10 結論與建議+責任·期限·追蹤, §11 合成聲明+替換清單, §12 附件索引·覆核·版本.

All five `required_tables_or_figures` exist: 字典 (表5), 合成明細+逐步計算 (表7/8/9), 分群比較+差距優先矩陣 (表10/11), 結論—證據—建議—責任—追蹤 (表13), 官方要求追溯 (表2).

All nine `required_fields_or_questions` are addressed (原件第三方出具→T04 E3/F3; 回查出具者·日期·事件→T04-T05/F3; 授權→consent欄+§11; 哪段哪表證明官方句→T02-R08; 現階級+升級缺口→表4+F3/F4; 母數及排除→§3.2/3.3/表3; 口徑與四捨五入→表6; 建議決策及限制→§10/表13/§7; 替換登錄鍵→表14). `required_calculations_or_analysis` (原件取得率=已驗證/應取得) is computed at §5.4 and 表6-T06-R07, and is never called 組織實績. Exception/hold workflow is real and executable: 表12 (trigger → immediate action → role → time limit → release condition) plus the source hierarchy and 辨識→隔離→重算→覆核→升版→通知 correction flow at P114. Replacement register present: 表14, **53 keys, 53 unique, no duplicates**, all `表 N` locators within 1–16, all `§x.y` locators resolve to existing sections.

### Q3 — Sample distinctness, internal completeness, arithmetic (independently recomputed)

**PASS — every number reproduces from the displayed rows.**

| Check | My recomputation from 表7/表8 | Document says | Match |
|---|---|---|---|
| TC T0 positives | TC-01,04,07 → **3/8 = 37.5%** | 3；37.5% (表9-R03) | ✓ |
| TC T1 positives | TC-01,02,04,05,07,08 → **6/8 = 75.0%** | 6；75.0% (表9-R04) | ✓ |
| Change | +3 people; 75.0−37.5 = **+37.5 pp** | +3；+37.5 個百分點 | ✓ |
| Transition split | retained 3, gained 3, lost 0, never-positive 2, T1-negative 2 | 留3/新3/失0/未達2 = 合計8 (表9-R07) | ✓ |
| Per-person contribution | 3 × 12.5 = 37.5 pp | 1/8=12.5 each (P082, P095) | ✓ |
| Learner application | L-01,02,04,05,07,08 → **6/8 = 75.0%** | 6；75.0% (表9-R09) | ✓ |
| Original acquisition | 0 ÷ 2 = **0.0%** | 0/2＝0.0% (§5.4) | ✓ |
| Denominators | TC 8, L 8, all 16 rows `1／1`; response 8/8 = 100.0% both groups | 表3, 表9-R02/R08 | ✓ |
| Denominators kept separate | TC and L never summed to 16 | P043, P029 | ✓ |

Distinctness and register: TC and L are separate populations with separate denominators and a separate construct (表10-R03 explicitly "不同構念、不同分母…不可算"); learner 6/8 is explicitly *not* 考照通過率, *not* 滿意度, *not* a second customer denominator (P029, P083). Language is descriptive throughout: causal statements are affirmatively blocked at P082 ("不能推論訓練造成改變"), P090 (no control, no multi-period, no test), P097–P104 (8 numbered limitations), F1/F2 hedged with explicit alternative explanations (P106–P107). The equal 75.0% coincidence is flagged twice as non-comparable (P090, P102, 表11-R08).

### Q4 — SAMPLE/SYNTHETIC vs REAL separation

**PASS.** All **16/16 table captions** carry `SAMPLE / SYNTHETIC — NOT ASSOCIATION REAL PERFORMANCE` (verified programmatically). Front matter P003/P004 and the closing P135 restate it; 表1 sets REAL evidence = 0 件/E0, external claimable = 無, 正式驗收 = 未授予.

Prohibited-claim scan across all 113 paragraphs + 891 table rows: **0 hits** for 榮獲, 獲獎, 感謝函; 「已達 4 分」 and 「本會訓練使…」 appear **only inside the prohibition** at T01-R05 ("不得寫…"); 核准 (21 hits) and 簽章 (2 hits) all occur in negation/pending form (P004, P051, P052, P059, P111, P121, T14-R10/R26/R44–R47); 原始點 appears only twice, both in explicitly negative constructions (P044 "不代表…實際活動", P111 "並非…已核准 SOP"). No third-party original, consent, approval, award, or real outcome is asserted anywhere. Consent is uniformly qualified as `SAMPLE假設同意：是` with header `示範同意（非實際文件）`, dictionary caveat `示範值不是實際同意` (T05-R10), and register key SYN-0111-026 "16/16…不是實際同意文件". **No ambiguity or over-claim found in consent/control statements.**

### Q5 — Replacement register sufficiency

**Substantially sufficient; three narrow gaps (all nonblocking).** Locators are usable: every `表 N` reference resolves (1–16), every `§x.y` reference resolves to an existing section, and per-record granularity is genuinely per-record for all 16 sample rows (SYN-0111-027…042, each with row-level locator + required real replacement evidence + owner). Every decimal in the document (0.0%, 100.0%, 37.5%, 75.0%) and all dates except one appear in register text.

Uncovered / under-located synthetic facts:

- **表13 第5列** (「75.0% 相等易誤讀」, 期限 2026-07-24, 追蹤指標「圖表檢核缺失 0」) — **no SYN key.** SYN-0111-021/022/023/024 cover 第2/第1/第3/第4列 only.
- **表16-R05 `v1.1 候選 R03 | 2026-10-23`** — **no SYN key**; SYN-0111-012 enumerates only v0.1/v0.2/v1.0 dates and is labelled "本列目前均為虛構示範". It is therefore *ambiguous* whether the R03 row is REAL build metadata or synthetic (the row does say "候選文件修訂日期；不是協會活動、核准或正式接受", which is honest but not a register classification).
- **表16-R07「次回覆核 2026-08-14 排定」** — the date exists in SYN-0111-023, but that key's locator is `表 13 第 3 列` only, so this row has no locator entry.
- Immaterial partials: 表13 第4列 tracking target "樣本決策 1 份" and 第5列 "圖表檢核缺失 0" are not individually registered.

None of these affect any computed value, claim, or integrity statement → **nonblocking**.

### Q6 — Title-blind distinguishability

**PASS.** §2.3 (P027–P030) rejects two wrong neighbours plus the financial object by name and by differing mechanism: 0110/I18-E19 = 題目—選項—行動承諾 (questionnaire/action plan); 0112/I18-E21 = 考照通過與回訓率, denominators = 考生/回訓學員; 財務/薪資/營業額 → separate deliverable. The differentiating instrument is genuinely internal: TC/L 特殊績效登錄, 可及性四面向, E0–E3, K1/K2 取得率, HOLD 規則 — none of which appear in the neighbours' mechanism. Explicitly at P029: 學員 6/8「指定應用」 is not a licensing pass rate, not satisfaction, not a second customer denominator. Title-blind identification works (P030 states the test; the content supports it).

### Q7 — Usability by training staff and an evaluator

**Usable.** Operating sequence P011 resolves (表3 → 表7/8 → 表9+§5.4 → 表4 → 表12 → 表13); all cross-references in P011, 表2 (§2.3/§5.4/表5/表7–8), 表13 (表7/表9/§5.4/§6/§8/表8/表10) and 表15 (§5.4/§9/§10) resolve to real sections/tables. Roles are defined at P119; exception procedure 表12 is actionable (trigger/action/role/SLA/exit condition); replacement procedure P125 is a complete 6-step control with HOLD fallback; thresholds are consistently labelled as 待核准提案 rather than policy (P051, P052, P059, P111, SYN-025, SYN-043–046).

Findings (no blocking):

- **N1 (nonblocking) — unsupported-by-fields coverage claim.** T02-R04 asserts `8 筆虛構陳述涵蓋四面向` as evidence for the 社會面／其他 element, but 表5 has **no 可及性面向 field**, 表7/表8 have **no aspect column**, and there is **no tally**. The substance does check out by reading 表7 T1 (TC-01 資訊可理解; TC-05 動線可到達; TC-02/TC-07 溝通可回應; TC-08 時間可配合), but "8 筆" is unanchored — the document contains 16 TC statements + 8 L statements = 24, and TC-03/TC-06 T1 statements are non-positive. Fix: add an aspect field to 表5/表7 or reword to 「表 7 之 T1 陳述（8 筆）」.
- **N2 (nonblocking) — defined field not instantiated.** 表5-T05-R09 defines `referent（場域、日期、聯絡）` as required, 可回查, and P053 makes 可回查參照 a positive-coding condition, yet 表7/表8 have **no referent column**; values are said to live in D1/D2 (declared 未附 at 表15 A2–A3) and are `示範未驗`. An evaluator therefore cannot inspect per-record referents inside the artifact. This is consistent with E0/HOLD, but the demo-positive rule and the hidden field should be tied together explicitly.
- **N3 (nonblocking) — register gaps** as listed in Q5.
- **N4 (nonblocking) — timeline coherence.** 表13 deadlines (2026-07-24 / 07-31 / 08-14 / 08-28) and 表16「次回覆核 2026-08-14 排定」 all **precede** the document's own current version date 2026-10-23 (表16-R05), with no overdue/replan status. P103 declares all demo dates fictional and 表16-R05 labels itself layout-revision metadata, so this is reconcilable — but the artifact never states that 表13 期限 belong to the demo timeline rather than the R03 revision timeline, so an evaluator may read the plan as stale. (This is *not* a visual/layout matter and is unaffected by the render blocker.)
- **N5 (nonblocking) — denominator readability.** All 16 sample rows are labelled `K1-HOLD／E1` / `K2-HOLD／E1`, while §5.4 (P084) defines 應取得原件 as **2 classes** (K1+K2=2件). A reader could miscount 16 originals against the 0/2 denominator. §5.4 does explain class-level vs per-person and instructs changing the denominator if per-person originals are adopted — recommend a footnote on 表7/表8. Relatedly, rows coded 0 (TC-03, TC-06, L-03, L-06) still carry an evidence-class label for claims they do not make.
- **N6 (nonblocking, informational).** §7 is titled 圖表解讀 but contains **no figure** — only conditional charting rules (P095). No figure is required by the Blueprint's `required_tables_or_figures`, so this is not a gap against the Blueprint.

No unsupported performance claim, no fabricated original, no contradiction in numbers, and no unusable procedure was found.

### Q8 — Verdict

## PASS

**Blocking findings: none.**

**Nonblocking findings (exact anchors):**

1. T02-R04 `8 筆虛構陳述涵蓋四面向` has no aspect field (表5), no aspect column (表7/表8), no tally, and an unanchored count "8" (24 statements exist); substance verified by reading 表7 T1.
2. 表5-T05-R09 `referent` field is defined and made a positive-coding condition (P053) but is not displayed in 表7/表8; per-record referents are external (表15 A2–A3, 未附) and `示範未驗`.
3. Register gaps: 表13 第5列 has no SYN key (SYN-0111-021…024 cover 第1–4列); 表16-R05 `v1.1 候選 R03 / 2026-10-23` has no SYN key and no REAL/SYN classification (SYN-0111-012 covers only v0.1/v0.2/v1.0); 表16-R07 `2026-08-14` is covered only indirectly by SYN-0111-023 whose locator is 表13 第3列; sub-targets「樣本決策 1 份」and「圖表檢核缺失 0」unregistered.
4. 表13 期限 (07-24…08-28) and 表16 次回覆核 (08-14 排定) all precede the current version date 2026-10-23 (表16-R05) with no overdue status; the demo-timeline vs file-revision-timeline distinction is implied but never stated.
5. Per-row `K1-HOLD／K2-HOLD` labels (表7/表8, 16 rows) vs the 2-class original denominator at §5.4 (P084) invite miscounting; no footnote on 表7/表8. Rows coded 0 also carry an evidence-class label.
6. §7 has no actual figure (P095 is conditional guidance only); no Blueprint figure requirement is violated.

**Calculation checks performed (all reproduced independently from displayed rows):** TC T0 3/8=37.5% · TC T1 6/8=75.0% · Δ +3 人 / +37.5 個百分點 · transitions 留3/新3/失0/未達2=8, T1未達2 · 3×12.5=37.5 pp · learner 6/8=75.0% · originals 0/2=0.0% · response 8/8=100.0% both groups · all 16 detail rows `1／1` · TC/L denominators never merged · 75.0−37.5 computed in counts before rounding (P067) · 1-decimal rounding rule stated in 表6.

**Review scope / exclusions:** semantic content only, on the exact-SHA DOCX, using an independently reproduced python-docx extraction that matched the packet with 0 discrepancies; official page-7 text re-hashed and the quoted sentence verified character-identical. **Word-native render BLOCKED for R03 → no visual, layout, pagination, or typography PASS is claimed or implied; no page images were inspected; no R01/R02 visuals were borrowed.** The technical QA receipt and the export-blocker receipt were treated as evidence only and are not the basis of any finding above. No files were created or modified, no Computer Use invoked, no replacement manuscript produced, **no formal association acceptance claimed**, and no assertion of official 4-point attainment or of any real 原始點協會 performance is made or endorsed by this review.