## Independent exact-SHA semantic review — TTQS ONE DOCX 0055 R04

**Overall verdict: PASS**

Candidate `candidate/0055_R04.docx`, exact SHA-256 `0c4abf37856611a8226361cedb9bf58fd7c769a4cec27574920ed5d93ff4687b`, register `evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv`, exact SHA-256 `66f660e24cfe12bd0c1351be577a6e4602f5a5454ba4914c0b736926cf9c0af7`. Both hashes were independently recomputed before review and match the task and patch receipt. This is an exact-SHA candidate review by an independent reviewer, **not** Human formal acceptance, and I claim no technical/visual PASS on behalf of the Builder.

---

### 1. Genre, requirement mapping, intended use, neighbor boundaries — PASS

- Cover (p.1, "講師遴選與聘任流程範例" + official-source line "官方來源定位：訓練品質評核表第 4 頁指標 12c（需求代碼 I12-E03；官方方框 058）：「講師的遴聘依師資遴選標準及流程評選並經訓練管理委員會通過後發給聘書。」") matches the Blueprint identity exactly; the three official mechanics are implemented (§4 rubric/§3 authority → §9 committee decision → §10 appointment-letter handling).
- Neighbor table (p.1–2, §1 "相鄰需求（需求代碼／官方方框）") covers I12-E01/056, I12-E02/057, I12-E05/059, I11-E02/052 and the prose "它不是講師授課後的評估、學員招生，也不是設備或場地檢查" — the full negative-neighbor set from the Blueprint is present; no requirement bleed found.
- Intended users are named (p.1, "本範例供課程需求提出人、遴選承辦人、評審及具有效授權的決策者使用"). All 13 Blueprint sections are present in the required order (verified in OOXML body order, 66 paragraphs / 26 tables).

### 2. Maturity and usability — PASS

This is a specific, worked example, not a generic template: role/authority table with stop-conditions (§3), 7-item authority checklist with HOLD default (§3 end), 0/60/100 observable anchors per criterion (§4), non-compensable gate table (§4), completed three-candidate/three-reviewer scorecards with per-criterion arithmetic (§7), fully marked simulated committee record with quorum/vote/recusal/owner/deadline (§9), 5-step letter issuance gates (§10), and a 52-row replacement register (§12). Body text is 10.5 pt, table text 9.5 pt minimum (OOXML `w:sz` scan: minimum 19 half-points = 9.5 pt), within contract floors.

### 3. SAMPLE/SYNTHETIC vs REAL boundary — PASS

- Cover banner (p.1, "SAMPLE / SYNTHETIC｜未核准、未發聘、不可作為真實任命證明…均為 UNKNOWN") and per-page header/footer ("示範文件，非正式任命紀錄" / "SAMPLE / SYNTHETIC").
- No invented real person, credential, authority, committee, approval, signature, or activity found. Every candidate/reviewer/committee/owner identifier is a code explicitly labeled synthetic (C-01–03, 評審甲乙丙, P-01, M-01–03, S-01, A-01); the letter specimen carries "SAMPLE｜NOT ISSUED｜NOT VALID" (§10) with blank signature lines that state "本樣本未簽發、未送達、未接受"; §11 is explicitly "尚未發生"; §9 decision is "教學用模擬文字，並非協會真實決議". Grep for adoption-style claims ("本會已核定/已通過/已發出/實際授課") returned only negating sentences.
- The new tie-break paragraph itself is labeled "（SAMPLE / SYNTHETIC，提案規則）" and ends "此提案須由具權限者核定後始得正式採用" — it cannot be mistaken for adopted association policy.

### 4. Internal consistency and register alignment — PASS (independently recomputed)

- Weights 25+25+20+20+10 = 100. Panel means and weighted points recompute exactly: C-01 86/82/78/80/90 → 21.5+20.5+15.6+16.0+9.0 = **82.6**; C-02 78/88/75/80/85 → **81.0**; C-03 90/86/88/85/90 → **87.6**. Ranking table (p.7, §7 "排序 | 候選代碼 | 總分") and 排序核對 paragraph agree: C-03 87.6 > C-01 82.6 > C-02 81.0. Thresholds all satisfied (C-02 learner-fit 75.0 exactly at gate; safety 90/85/90 ≥ 80).
- 360 = 90+90+120+60; fee NT$4,800 = 6 h × NT$800/h (§10 letter table) consistent with register FAC-0055-045/046. Dates 2026-11-10 meeting → 2026-11-17 deadline → 2026-12-05 course, no inversion.
- Register: exactly 52 data rows, 12 columns, zero empty fields; byte-level diff vs the R03 register shows **only** line 11 (FAC-0055-010) changed; UTF-8 BOM and LF endings preserved. All score vectors (FAC-018–032), codes, dates, committee facts, fee facts align with the DOCX text.

### 5. Blueprint tie-break sequence — PASS

Inserted paragraph (p.7, §7, immediately after "排序核對：C-03 87.6 > C-01 82.6 > C-02 81.0…"; anchor "同分處理（SAMPLE / SYNTHETIC，提案規則）") implements the sequence in order, and its text is byte-verbatim to the packet's proposed insertion (verified programmatically):
1. 「專業內容正確性」加權點數 — subject-accuracy weighted points ✔
2. 「教學示範與引導」加權點數 — teaching-demonstration weighted points ✔
3. 第二次試教「相同題目、準備時間、時長及量尺…記錄評審觀察與分數」 — identical conditions, observations/scores retained ✔
4. 「若仍同分，或無法核實具權限者與已核定的後續規則，立即 HOLD，依真實章程與授權處理，不另創規則」 — HOLD under real governing authority ✔
5. 「本例三組加權總分互異，未觸發此程序」 — fallback correctly stated untriggered ✔

### 6. Authorized register row change — PASS

Only FAC-0055-010 changed. Locator now reads "第 4 節量尺表「權重」欄；第 7 節排序核對與同分處理。" — both anchors verified to exist in the candidate. The row retains the 25/25/20/20/10 weights, adds the tie-break order and HOLD condition marked as an unapproved synthetic proposal; real_source requires "權責治理單位與正式核定之遴選辦法，以及（如使用）第二次試教評分表"; verifier is "權限經核實後之具權限者／權責單位"; status remains SYNTHETIC; HOLD condition covers both premature use and triggered-but-unverifiable cases. Adequate.

### 7. Change scope and technical evidence

- OOXML ZIP comparison R03 (`747218b1…`) vs R04: **only `word/document.xml` changed**; 18 other members byte-identical, member order preserved — matching the receipt. The full-body text diff shows exactly **one inserted paragraph** and nothing else.
- The inserted `<w:p>` clones the preceding paragraph's pPr/rPr (Microsoft JhengHei, bold, `w:sz 21` = 10.5 pt, same spacing) — consistent styling, no new style definitions.
- Supplied visual evidence is internally coherent: all 11 page-image SHA-256 values and the PDF SHA in `visual_review_R04.json` were recomputed and match; pages 1–6 and 8–11 are pixel-identical to the reviewed R03 render (only page 7 differs), page count stays 11, and my direct inspection of page-01.png and page-07.png confirms the new paragraph sits cleanly after the ranking check with no clipping, overlap, or extra page. No "待填/待核/空白表/會後填寫" placeholder tokens found (single "待核定" is inside the letter's date row describing the synthetic date's real-use requirement, not a blank placeholder).

### Non-blocking findings (carried or new, none affecting the verdict)

1. **Minor / metadata only** — `docProps/core.xml` title still reads "講師遴選與聘任證據包｜DOCX 0055 R02｜SAMPLE/SYNTHETIC" and `app.xml` reports stale stats (Pages 1, Words 0). Inherited from the R02 template and intentionally untouched by the bounded patch; user-visible version control lives in §13. Suggest a future metadata-only sidecar fix (no DOCX byte change required for acceptance per HOTFIX5).
2. **Minor / carried from R03 review** — §9 "出席及法定人數" row still does not explicitly say recorder S-01 has no vote, and "3/3 表決委員出席" remains readable as either attendance or quorum threshold. Denominator is now unambiguous (M-01/02/03 only), so this stays cosmetic.
3. **Minor / partially carried from R02 review** — resume indexes S-C01–03 are now registered (FAC-015/016/017 explicitly note "僅示例索引，本包未附履歷或資格文件"), resolving most of that finding; the §6 12-minute demonstration design itself is still unregistered, which the upstream contract permits as a design artifact.

### Review scope and limitations

Covered: exact-SHA verification of candidate and register; full OOXML/text inspection of the candidate (all 13 sections, 26 tables, header/footer, metadata); exact one-line diff of DOCX body text and CSV bytes vs R03; independent recomputation of every weight, mean, weighted point, total, ranking, fee, and date; tie-break sequence conformance; register row-count/column/empty-field checks and FAC-0055-010 adequacy; direct visual inspection of pages 1 and 7 plus hash/pixel verification of the supplied render set. Not covered: I did not re-render the DOCX myself, did not run a full-corpus cross-document duplication sweep (deferred to final QA per contract), and did not open the external same-case source DOCX files (their SHAs were taken from the Blueprint/receipt bindings).

---

**Conclusion:** Candidate `0055_R04.docx` at SHA-256 `0c4abf37856611a8226361cedb9bf58fd7c769a4cec27574920ed5d93ff4687b` (register `66f660e24cfe12bd0c1351be577a6e4602f5a5454ba4914c0b736926cf9c0af7`) is **PASS** for semantic acceptance at this exact SHA: the R04 change closes the Blueprint's tie-break gap exactly as authorized, the only DOCX and register deltas are the authorized ones, and all SAMPLE/REAL, consistency, and HOLD boundaries hold. Reviewer identity: **OpenCode V2 independent reviewer / opencode/mimo-v2.6-flash-free**. This is an exact-SHA candidate review, not Human formal acceptance; promotion and formal acceptance remain with the dispatcher/Human Gate.