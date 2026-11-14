## Binding

| Item | Value |
|---|---|
| Project / doc | TTQS_ONE / 0086, revision **R02** |
| Mapping | I17C-E05 / official checkbox 092 — **provisional** (historical 142-sequence source unavailable; §2.3 & 附錄A state this correctly; not scored against body) |
| DOCX SHA-256 | `0beec6684f01101675ad4034e7b9deef4a992b6d6e4a7ce4bf5c55f0cceb645b` — identical string in build, technical and visual receipts (text match only; I did not hash the binary) |
| Body SHA-256 | `0ce826c54a5124596ccec578c3c419f7df1ad33af58e3642f18517be5fd32699` — matches `body_sha256` in build receipt, which binds body→DOCX |
| Register | build receipt `synthetic_register_rows: 53` = actual CSV rows F002–F054 (53) |

`technical_status: PASS`, `visual_status: PASS` and §14.1 編稿自檢 are **not** treated as semantic PASS.

## Dimension verdicts

**1. Official requirement fit & genre — PASS**
§2.1 names the source exactly per packet (《TTQS 查核佐證文件資料表—訓練機構版》印刷第6頁, I17c「行為評估」); §2.2 reproduces official 0/1/2/3 text verbatim with 「不可推論」 column and the boundary line 「兩者不換算、不映射、不替代」; no 0–3 conclusion is drawn anywhere. Genre is method/manual: §0 「不是實際稽核報告…不是正式 TTQS 自評、不是 17c 0–3 評分」; §2.4 lists all non-claims. Mapping limitation honestly disclosed, not a body defect.

**2. Blueprint R02 C1–C15, register pointer & schema — PARTIAL**
C1–C14 all located (§0 no SHA/queue/JSON; §2; §3; §4 Gate 0 前置A–H; §5 母體12/樣本3/25.0%; §6 14 steps; §7.1–7.5; §8–9; §10 表A–H; §11; §12; §13; §14.1 labelled 非QA/非接受). C15 satisfied structurally: **§12.1 in-body pointer** `quality-review/0086_R01/evidence/synthetic_replacement_register_R02.csv`, schema lists all 11 columns incl. `跨文件引用狀態` (CSV header confirms), every row = `NO_LINK`. Practical use is strong (§6「最小可行演練」+ 桌演 fallback; §4.3 建議核准角色). **Why PARTIAL:** §12.1 claims 「所有…角色代碼…逐筆列於」 the register, but `SYN-ROLE-TRN-01`, `SYN-ROLE-MGR-01`, `SYN-ROLE-SITE-01` (§8.6, 表D, 表E, 表F) appear in no row; two row locators are wrong (D-3).

**3. Authorization, independence, safety — PASS**
Prior written authorization (§4.1 incl. mystery-shopper-specific fields; §4.3 「任何一欄缺件即 HOLD」); independence (§4.2, 表B, 獨立性閘門); legal/privacy HOLD gate (前置F, §4.5-1, §6 step 2, §13 row 「法規／契約／政策要求個別事前告知／同意，或無法確認→禁神秘客」); delayed disclosure defined (§1.3, §4.5, 表A/表D); no impersonation/recording/unauthorized data (紅線2, §4.4, 表A 「含身分證號／病歷／電話／地址→拒收」); no legal conclusion (§13 「本文件不作法律結論…一律 HOLD」), demo legal premise explicitly hypothetical (§8.1/§8.2「假設…（SYN）」). No residual pre-disclosure error; no G0–G3 numbering.

**4. Forms A–H — PASS**
All eight are real 4-column Markdown tables (欄位指示｜SYNTHETIC｜REAL空白｜拒收/HOLD規則); my row counts match technical receipt `A15/B11/C13/D13/E12/F11/G13/H12`. REAL column uniformly `（空白）`; rules actionable (表A「用於人事處分→拒收」, 表H「未關閉即結案→REJECT」). **R01 F-5 fixed:** 表D now has 「NA／NE 核准與說明…核准人／日期／參照」 with SYN example `SYN-NA-APPROVAL-03` and rule 「不得事後追認」 (D count 12→13 confirms the added row).

**5. Worked example & cross-section consistency — PARTIAL**
Independent recomputation: S-01 2+2+2+2+1+2+1+0=**12**, ÷16=**75.0%**; S-02 2+2+1+2+2+2+1+1=**13** ÷16=81.25→**81.3%**; S-03 six 2s+1=**13**, 8−1 NA→7×2=**14**, 13÷14=92.8571→**92.9%** — all agree with §8.5/§8.7/§9/表H/F027/F029/F031 and rounding rule §7.4. Dispositions against the sole threshold table §7.5 all correct (S-03 ≥90% still 條件改善 because of one 1). Sample mapping S-01=003(高)/S-02=007(中)/S-03=011(低) consistent in §5.1/§5.2/§5.3/§8.3/表C; 12→3=25.0%. D baseline explicit and calendar-coherent (D=07-22 Wed→07-23 D+1→07-24 D+2, 表D=07-24). Finding IDs `SYN-FND-01/02/03` uniform in body (表D 偏差 row, 表H 發現 row fixed). **Why PARTIAL:** closure unit still disagrees inside 表F (D-1) and the NA approval’s 「樣本凍結前」 sequencing is unsound (D-2).

**6. SAMPLE/SYNTHETIC vs REAL boundary — PASS**
Header 「SAMPLE／SYNTHETIC…未經原始點協會核准；…REAL=UNKNOWN／HOLD」; §8 blockquote; §8.2 「不得用虛構 PASS 宣稱真實 Gate 0 通過」; every signature 「虛構占位」 or `UNSIGNED／DEMO`; §10「簽章不得以打字代替」; §11.3「本文件不產生任何真實原件」; association appears only in negations (§2.4). No fictional fact presented as real approval, audit, signature, result or execution.

**7. Separation from 0082–0085 — PASS**
§12 table + link keys + rule 「任一缺件標 NO_LINK」; all four demo rows `NO_LINK`, 本文 `SAMPLE ONLY`; explicit bans 「不得跨文件合併分數」「不得用 0084 主管評分代替獨立觀察」; register F037 and all 53 rows `NO_LINK`. No invented shared case or score substitution.

**8. Text-reader usability — PARTIAL (rendered NOT_INSPECTED)**
Text side: §1.2 reading order, valid §-cross-references (§4/§5–§7/§10/§11/§13 all exist), uniform HOLD/STOP/REJECT vocabulary, §8.3 sentence now complete — no truncation/duplicate heading. **Rendered-image review: NOT_INSPECTED** — no PDF or page images were attached and none may be opened; coverage limit = **0 of 22 pages** independently verified. `visual_qa_R02.json` binds the same DOCX SHA `0beec668…` (values agree with binding) and asserts 22 pages, Word 16 COM/Poppler 144 dpi, all pages inspected — producer evidence only, not my judgment.

## R01 finding resolution

| ID | Status in R02 (determined from body/register, not builder claims) | Evidence locator |
|---|---|---|
| F-1 truncated §8.3 / duplicate heading | **RESOLVED** | §8.3 single heading; sentence complete: 「抽出 3 件不同匿名案件：S-01＝SYN-CASE-003、S-02＝SYN-CASE-007、S-03＝SYN-CASE-011」 |
| F-2 no register pointer / no cross-doc column | **RESOLVED** | §12.1 pointer + path; CSV header has `跨文件引用狀態`; body lists it; all rows `NO_LINK` |
| F-3 unclear D+2 baseline | **RESOLVED** | §8.1 「D 定義為本案觀察事實完成確認日…D=SYN-2026-07-22…07-23 為 D+1、07-24 為 D+2」; 表A, 表D, 表H, register F053 align; weekday sequence checks out |
| F-4 inconsistent finding IDs | **RESOLVED in body** (表D「偏差／安全事件」and 表H「發現／改善／覆核」now `SYN-FND-*`); register rows F046/F047/F050 still abbreviate → D-4 | 表D, 表H vs register F046/F047/F050 |
| F-5 Form D missing NA/NE approval | **RESOLVED** | 表D row 「NA／NE 核准與說明…S-03／item 4＝NA…SYN-NA-APPROVAL-03 事前核准」 + reject rule 「不得事後追認」 |
| F-6 “3 cases” vs “3 consecutive observations” | **PARTIALLY RESOLVED** | Fixed in §8.6, §8.8, 表E, 表F「完成證據」(all say 3 件不同服務案件, unique case_id/date/evidence); **表F「關閉條件」still 「3 次連續觀察」and「缺第 3 次觀察」** → D-1 |

## Remaining actionable defects

| ID | Sev. | Locator (exact phrase) | Correction | DOCX bytes change? |
|---|---|---|---|---|
| D-1 | Low | 表F rows 「關閉條件」=「3 次連續觀察，無 1／0」 and 「未關閉原因／升級」=「缺第 3 次觀察」 (contradicts same table’s 「完成證據…3 件不同服務案件」 and §8.8「不得將同一案件拆成多次」) | Rewrite as 「連續 3 件不同服務案件（各具唯一 case_id、日期、證據 ID）觀察均無 1／0」/「缺第 3 件不同案件觀察」 | **YES** |
| D-2 | Low | 表D「NA／NE 核准與說明」cell: 「SYN-ROLE-APPR-01 於 SYN-2026-07-13（樣本凍結前）…事前核准」; register F052 repeats 「樣本凍結前」 | Approval names S-03, which per §8.3 exists only 「在清冊凍結後」— sequencing is circular and both events are same-day/unverifiable. Replace with 「樣本凍結後、觀察（07-20）前」 or drop the parenthetical; mirror in F052 | **YES** (表D cell; CSV too) |
| D-3 | Low | Register F010 locator `§3` (field 真實狀態, value REAL=UNKNOWN／HOLD — not in §3); F035 locator `§8.6` (values 「SYN-ACT-01；開始 2026-08-10；提交 2026-09-18；逾期 3 天」 are in 表F) | F010→ document status header/§11.3; F035→ 表F | No (CSV only) |
| D-4 | Low | Register F046 「FND-01／item 5」, F047 「ACT-01」, F050 「F-01／F-02 OPEN；F-03 無證據」 vs body `SYN-FND-01…03` / `SYN-ACT-01` | Align register values to body IDs (row-by-row cross-check currently fails) | No (CSV only) |
| D-5 | Low | §12.1 claim 「所有演示日期、角色代碼…逐筆列於」 vs register: `SYN-ROLE-TRN-01` (§8.6/表E/表F), `SYN-ROLE-MGR-01` (§8.6), `SYN-ROLE-SITE-01` (表D) absent from all 53 rows | Add rows (or extend F032/F046/F047) for the three role codes | No (CSV only); body claim otherwise overstated |

No Critical/Major defects remain. No finding alleges fabricated real facts, privacy/legal violations, score errors, or threshold misapplication. Note: technical receipt `finding_01_unit_consistent: true` does **not** cover 表F’s residual wording (D-1) — technical PASS ≠ semantic PASS.

## Coverage / limits

- Text-only review of the 7 attached artifacts; body, source packet, Blueprint, register CSV, three receipts, prior R01 review. **Rendered PDF/page images: NOT_INSPECTED — 0/22 pages verified by me**; all layout/readability claims are receipt-sourced (visual receipt names the exact DOCX SHA; values agree with binding). The path in §12.1 was not verified to exist (no tools).
- No hashing, tools, shell, network or edits performed; SHA bindings accepted as stated with cross-file string consistency confirmed only. Official page-6 wording verified against the source packet transcription only (official PDF/PNG not attached here).
- Unsupported source/mapping limitation (missing 142-sequence CSV → provisional mapping) is **not** counted as a body defect. No legal determination made or implied.

## Overall verdict

# PARTIAL

**This exact candidate is semantically ready to enter Human review — yes, provided this finding list travels with it.** Dimensions 1, 3, 4, 6, 7 pass on independent reading; all arithmetic, denominators, rounding and threshold dispositions recompute correctly; five of six R01 findings are resolved and F-6 is resolved in substance.

**It is not formally acceptable:** `CANDIDATE_NOT_FORMALLY_ACCEPTED` preserved. D-1 and D-2 require **DOCX byte changes** (表F, 表D cells) — correction yields a new DOCX SHA and mandates re-running build/technical/visual receipts before any re-review or formal acceptance; D-3/D-4/D-5 are register-CSV-only fixes requiring no byte change but must also be closed or waived by Human. Formal acceptance remains behind the Human Gate; nothing above constitutes technical QA, visual QA, or acceptance.