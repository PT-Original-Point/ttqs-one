## Scope and limitations

**Scope:** text-semantic review of the supplied packet, bound to the exact target SHA, covering the embedded R11 extraction, `SOURCE_PACKET_0084_R01.md` content, complete Unique Blueprint R03, the 0083 §§8.1–8.3 excerpt, the 59-row register CSV, and (as targeted questions only) the historical R09 findings. Technical/visual receipts treated as supplementary, never as semantic acceptance.

**Independent bindings I recomputed myself (read-only, no edits, no Computer Use, no replacement content drafted):**

| Object | Recomputed SHA-256 | Result |
|---|---|---|
| `candidate\0084_R11.docx` | `cf4376b3287db4f3a900fe7a39012e7dc6a49b419e586371b1eb1e0190a245d8` | matches target exactly |
| `inputs\UNIQUE_BLUEPRINT_0084_R03.md` | `49ac3786cdac0547bdab636663a280b5ef015e2b956ee2fefb157d674b66ed7e` | matches packet |
| `inputs\SOURCE_PACKET_0084_R01.md` | `6c2e928a889f0e01fe6aeca2ed0ed5b6a0dca6b3a12f591ba493a969dd4d3f1d` | matches packet |
| `evidence\synthetic_replacement_register_R10.csv` | `3d73cb6302849066c99cdba0916689a397c7f2c2036f3b1e0970dd24d67910cf` | matches packet; 59 rows, 59 unique IDs, statuses 53/5/1 |
| `candidate\0084_R10_body.md` (stated R11 body) | `15261e5613661e547cae4b102e8bd2fdf8402f41affe16f580bf1187ab4ddcd4` | matches receipt `body_sha256` |
| packet file itself | `f07a00034887ef956eb6b398f5e40bbe9ef9dc9088a8284b3f842dab58baee55` | **no cross-check possible** — packet SHA is stated to live in a separate post-generation receipt, which is not in the packet |

I also parsed `word/document.xml` from the exact DOCX directly (not just the embedded extraction) to run the word-token and register scans below, which confirms the embedded extraction is faithful on every point I cite.

**Limitations:** layout/render/watermark/TOC/page-number checks out of scope (visual receipt treated as supplementary); extracted-text SHA `329dadf2…` not independently reproduced (no extraction artifact supplied — I substituted direct XML parsing); no human trial-use; no file modified.

---

## Verdict: PASS

All eight required checks pass on the exact R11 text. Four minor, non-blocking defects are cited at the end; none changes a rule, number, gate, boundary, or cross-document fact.

---

### 1. Genre and requirement identity — PASS

Cover identity block (`0084 / I17C-E03 / 090`, 文類 = 派訓主管學習成效評估：職場觀察量規和回饋); §0.1 three-second table (B1–B4/O0–O3/Form-O → 本件; 學員自填 → 0082/088; 目標次數/實際次數 → 0083/089; 就業率/考照率 → 17d; 知識社群/神秘客 → 17c 其他); §1.1 identity lock plus the explicit 編號混淆禁制 ("090 不得寫成 089 或 088；0084 不得寫成 0090"); §1.2 five-work table with the single ☑ row 0084/090; §1.3 17d exclusion table; §1.4 seven "本件不是什麼" lines; §2.4 "何時不要用本件". **Consequence:** title-blind, the artifact can only be read as a supervisor/observer workplace-behavior observation and feedback instrument, and each of the three nearest wrong documents plus 17d is positively excluded.

### 2. R09 P1 regression (approval token in blank O-01; §5.1 vs §15.2) — PASS

- **Token screen:** I searched the exact DOCX text for `核准 / 核定 / 簽核 / 批准 / 已採納` → **0 hits each** (Blueprint §2.3's ban list). The old offending string `正式授權案號（依機構核定格式填寫）` is gone. (`已採用` appears 3× only inside prohibition sentences: §11.2 不可說 column, §17.4, closing line — no approval is asserted anywhere.)
- **§15.2 O-01 (blank master):** 填寫欄 empty; 格式／選項 = `依單位適用之識別格式`.
- **§5.1 O-01:** `依單位適用之識別格式` — **identical**; both occurrences confirmed in the DOCX (count = 2). The R09 format disagreement is closed.
- Field-by-field §5.1 ↔ §15.2 comparison: O-02…O-17, O-19 identical or compatible (O-10 `文字` vs `路徑／卷宗／頁碼／版本` and O-17 `文字` vs `文字；未回應請標「未回應」` are elaborations of the same rule; the only differing qualifier is O-18 — `文字；連結 AID（若有）` in §5.1 vs `文字；對象＋時間或觸發` in §15.2, both satisfied by §5.2 rule 8).
- Note: the neutral O-01 wording departs from Blueprint §7.1's `SYN-0084-□` in *both* places (consistently), and matches REG-001's REAL requirement `正式案號（授權登記）`; §14.5's decision template still shows `SYN-0084-□` as its sample format. **Consequence:** no literal-word screen can flag the form, and a real user is not handed a synthetic-case ID scheme.

### 3. R09 P2 regression against Blueprint R03 and the 59-row register — PASS

- **Register:** CSV recomputed = 59 rows, 59 unique `REG_ID`, status distribution NOT_EXECUTED 53 / HOLD 5 / SAMPLE-SYNTHETIC 1 (= 59). Candidate Appendix E: `REG-001…REG-059`, no gaps, no duplicates, no range IDs (verified by script on the DOCX-extracted text).
- **Exact coverage — every one of the 59 CSV values appears verbatim in the candidate body (0 missing).**
- The specific R09 gaps are all closed: **O-08 at O0/O1/O2/O3 = REG-047/048/049/050**; **O-16 = REG-051/037/052/053**; **O-17 = REG-054/038/055/056**; **O-18 = REG-057/039/058/059** — each verbatim in §6.5.1–6.5.4. Supporting atoms: O-09 = REG-033–036, levels = REG-012–027, dates = REG-008–011, locators = REG-029–032 (HOLD), N/O reason = REG-028, derived = REG-040–042/044, cross-doc = REG-045 (HOLD) / REG-046 (SAMPLE/SYNTHETIC).
- **Real-source/authorization column is actionable per row**, e.g. REG-002 `真實去識別碼（本人同意）`, REG-006 `真實主管指派（授權）`, REG-029–032 `真實可定位原件（授權）`, REG-045 `補可定位授權原件`, REG-054 `真實學員回應（有來源且去識別）`, REG-059 `ROLE-COORD 追蹤 AID-02 狀態，提供日 PENDING`.
- §16.2 category counts sum correctly (4+22+2+4+16+4+4+2+1 = 59); §16.5 status line = 53/5/1. No 46-row count or R09 verdict carried forward. **Consequence:** a REAL replacement pass driven by REG-001…059 leaves no synthetic case value behind in any O0–O3 record cell.

### 4. R09 P3 regression — §0.4 workflow — PASS

§0.4 (TOC p.8, body) is a single labeled section: 7 steps `建基準 → 確認觀察機會 → 記錄事實與定位 → 對照行為錨點 → 進行事實回饋 → 記錄回應與下一步 → 複核與留狀態`, each row carrying 表單欄位, 操作與通過關卡, and 停止／退回條件 with tokens: step 1 `→ HOLD`, step 2 `→ REVERIFY`, step 3 `→ RETURN／HOLD`, step 4 `→ HOLD`, step 5 `→ RETURN`, step 6 `→ RETURN`, step 7 `→ HOLD；不一致 → REVERIFY；不得由本表自行表示正式接受`. REJECT gates sit in §2.4 and §14.2/Appendix C. **Consequence:** a first-time supervisor now walks the whole cycle from one table instead of assembling it from five sections.

### 5. Practical completeness — PASS

| Element | Citation |
|---|---|
| B1–B4 dictionary | §3.1 task context, §3.2 dictionary (observable signs / acceptable evidence / not-evidence), §3.3 valid-opportunity test, §3.4 fuzzy-language rewrites |
| Behavior anchors | §4.1 generic 0–3 + N/O anchors with prompt-count rules, §4.2 per-indicator anchors, O-09 required-fact table, §4.3 priority, §4.4 three misjudgments, §4.5 calibration |
| Blank Form-O | §15.2 clean master (empty 填寫欄 verified line-by-line, no sample values, no dates, no names), §15.4 continuation, §15.5 print/copy rules, footer row "不代表正式接受" |
| Complete O0–O3 demo | §6.5.1–6.5.4 (all 19 fields each), §6.6 fact→level→locator matrix, §6.7/§6.8 consistency and scale separation |
| Sources/locators | O-010 definition §5.1 + §5.2 rule 6 + §5.4 `見附件 → RETURN`; `OBS-NOTE-0084-B01-O0–O3` all marked 合成定位／PENDING |
| N/O & disagreement | §9.1 rules, §9.2 worked O0/B4 case, §9.3 five disagreement rows, §9.4 seven-step flow, §9.5 audit fields |
| Feedback / response / next steps | §8.1 four steps, §8.2 dialogue, §8.3 quality contrast, §8.4 learner-disagreement path, §8.5 five next-step gates; O-16/17/18 definitions §5.1, rules §5.2 |
| HOLD/RETURN/REJECT (+REVERIFY) | §14.1 four decisions, §14.2 **18 triggers** (counted, matching Blueprint §15), §14.3 all deadlines `PROPOSED SAMPLE ONLY`/`PENDING`, §14.4 five drills, §14.5 decision template (carries REJECT, which O-19's option list omits), Appendix C 11 rows |
| Arithmetic | §7.1–§7.7 recomputed independently: 4×4=16, N/O=1 (B4@O0), valid=15, paired n=9, B4 denominator 0 → "不計算" (explicitly not 0%), direction 9/0/0 over denominator 9; dates from T0 2026-03-06: −1, +38, +56, +84, strictly increasing, O0 < T0. Prohibitions on ordinal averaging, N/O-as-0, 93.75%, 83.3% carry-over and causation all present (§7.5–7.6, §11.4) |
| Privacy/minimum data | §13.1 permitted/prohibited fields, §13.2 de-identification, §13.3 all `PENDING`, §13.4 `PENDING`/`PROPOSED`, §13.5 "不虛構任何處理單位或期限" |

### 6. Cross-document consistency vs the 0083 §§8.1–8.3 excerpt — PASS

Every shared anchor is verbatim to the excerpt: `SYN-0083-B01` (§6.1 父案例錨點, REG-046), `LRN-B01`, `SYN-COURSE-0083-B`, T0 `2026-03-06`, baseline 4 counts `2026-02-06→2026-03-05` (28 days), target 12, T1 `2026-04-03` 4/3, T2 `2026-05-01` cum 8/7, T3 `2026-05-29` cum 12/10 = 83.3% (§6.2, §11.3, §12.2). AID-01 raised 04-03 / provided **04-13** → O1 = 2026-04-13 with O-08 `AID-01 於本日提供` (5 occurrences in the DOCX) and explicit non-conflation with T1 in §2.2 rule 5, §6.3, §7.4, §12.2, §12.4. AID-02 raised 05-29, still `REQUESTED`, provide date `PENDING` (§6.2, §6.5.4 O-08, REG-050/059). 0083 stays `PARTIAL` with evidence locator/authorization `PENDING` (§12.1, §12.5, REG-045 HOLD). **Synthetic 0084 additions are not represented as 0083 evidence:** §6.1 declaration ("新增的合成示範，不是 0083 已有證據"), §12.3 "用本件合成觀察把 0083 變成 REAL" listed as forbidden, §12.5 `OBS-NOTE-0084-B01-O0–O3` = new synthetic locators. **Consequence:** the timeline is internally coherent and neither document's status can be silently upgraded.

### 7. SAMPLE/SYNTHETIC/PROPOSED vs REAL boundary — PASS

Stamps verified in the DOCX: cover (`CANDIDATE / NOT_EXECUTED`, `REAL=UNKNOWN/HOLD`, `FORMAL_ACCEPTANCE=NOT_GRANTED`, `ALL_DEMO=SAMPLE/SYNTHETIC/PROPOSED`), §6.1, §17.1/17.3/17.4, closing line. Roles are codes only (§2.1 "全文只用角色碼"); no real person, credential, signature, association execution/adoption/approval, official score, or third-party original is claimed anywhere (token scan above; §17.4 不可宣稱清單). Institutional 17c 0–3 is kept in §10 only, marked `UNSCORED`, with five explicit prohibitions (§10.3) and REG-043 `UNSCORED`, separate from the `PROPOSED SAMPLE ONLY` individual rubric (§4 preamble, §4.1/4.2). §13.2's hypothetical names (`王女士`, `小明的媽媽`, `志工阿華`) are examined: they sit in the 原始描述（不可用） teaching column of a de-identification table and assert no real service-user data, person, or record — not a fabrication.

### 8. Title-blind recognizability and rule completeness — PASS

With the title hidden, §0.1 plus the B1–B4 / O0–O3 / Form-O / `ROLE-OBS-*` vocabulary and §6 alone identify a supervisor behavior-observation instrument distinct from 0082/0083/17d. Role-based entry points exist for all five users (§0.3: 派訓主管 / 受指派觀察者 / 訓練行政 / 內部複核者 / 評估委員); pre-use gate §2.3, fill order §5.3, opportunity test §3.3, N/O vs 0 vs HOLD §9.1, dual-observer REVERIFY §9.3–9.4, 18 return/reject triggers §14.2, blanks §15, replacement procedure §16.4, glossary Appendix B, missing-field matrix Appendix C. The one apparent rule gap — O-19's option list excludes `REJECT` — is covered by §14.5's decision template (決策 = HOLD／RETURN／REJECT／REVERIFY). **Consequence:** a volunteer-association training administrator and evaluator can run the instrument end to end without inventing a rule.

---

## Findings (minor, non-blocking)

**F1 — Stale build-input provenance inside the SHA appendix (accuracy).**
§12.4 closing line: "上列勾選是建置者依 **Blueprint R02** 與來源包所做的靜態對齊"; Appendix A preamble: "與 SOURCE_PACKET_0084_R01.md 及 **Blueprint R02** 的來源矩陣比對". I confirmed **2 occurrences of "Blueprint R02" inside the actual DOCX XML** — not a packet artifact. These contradict the cover ("R01（依唯一 **Blueprint R03** 建置）"), Appendix A's 施工輸入 SHA row (`UNIQUE_BLUEPRINT_0084_R03.md` = `49ac3786…` `MATCH`, which I recomputed and it matches), and Appendix D (藍圖版本 `R03`). *Consequence:* the prose provenance in a SHA-bound deliverable is self-contradictory — a reviewer cannot tell from the text which blueprint validated the six-source matrix. No rule, number, register row, or verdict depends on it (§12.4's eight checklist items are identical in R02 and R03, and the body is 59-row everywhere); correcting two labels resolves it. Related hygiene note: the cover's `版本 R01` vs. artifact/receipt `R11` is ambiguous (plausibly the document-series version) and worth normalizing.

**F2 — §6.7 self-check location claim is incomplete (accuracy).**
§6.7 row: "事件計數未當行為分數 | `3/4、7/8、10/12` **僅在 §6.2、§12** | 對齊". The literal strings also occur in **§6.8** ("0083 的 3/4、7/8、10/12、83.3%") and the equivalent values appear in **§11.2 / §11.3** (4/3, 8/7, 12/10) and §7.5 (83.3%). *Consequence:* the location assertion is false as written, so a literal reviewer scan would flag the self-check table itself; the substantive claim it certifies — event counts are never converted into behavior levels — I verified independently as **true** (no conversion anywhere in the DOCX). Non-material, but the row should be corrected.

**F3 — §15.3 introduces stricter, unstamped filling thresholds (spec).**
"O-10 …須列出筆記代碼、卷宗、頁碼中的**至少兩項**" and "O-09 **至少記三點**" are not in Blueprint §7 and are not marked `PROPOSED SAMPLE ONLY`, while the operative RETURN trigger (§14.2, Appendix C, Blueprint §15) fires only on "只寫「見附件」". *Consequence:* an evaluator could treat a single precise locator (e.g. one full path) as deficient even though no decision rule rejects it — a risk of over-returning valid records. The binding rules remain §5.2 rule 6 and §14.2, so no record's fate actually changes; adding a `PROPOSED` stamp or aligning the hint removes the ambiguity.

**F4 — One register cell is registered as a substring, not whole-cell (very minor, echo of P2's rule).**
§6.5.1 O-15 cell = `B4：當日無異常或衝突情境，無有效觀察機會`; REG-028's value = `當日無異常或衝突情境` (contained verbatim, but not the full cell), against §16.1's "整格…整格替換" / "未入冊即洩漏 → 全文比對". *Consequence:* a literal full-text leak tool would flag the label prefix and the glossary-definition suffix (neither is synthetic data), producing a false positive; the replacement pass itself is unaffected. Same class: guidance-only illustrations (§5.4 正確寫法, §8.2's condensed dialogue variant, §9.2 wording) are unregistered SAMPLE-like sentences, but §16.4 directs real use to the clean §15 master, so they sit outside the record-replacement scope. Everything else in the four O0–O3 records is registered whole-cell verbatim.

*Examined and cleared, not findings:* Appendix E's pointer to `evidence/synthetic_replacement_register_R10.csv` — the file exists with that exact name and hashes to `3d73cb63…`, matching the packet, so the pointer is correct, not stale.

---

**Status:** PASS is the semantic verdict for this exact SHA only. Layout/render evidence remains supplementary, the packet's own SHA is not cross-checkable from inside the packet, and the candidate remains `CANDIDATE / NOT_EXECUTED`, `REAL=UNKNOWN/HOLD`, `FORMAL_ACCEPTANCE=NOT_GRANTED` — **not formally accepted**.
