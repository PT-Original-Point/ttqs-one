I now have everything I need: the DOCX SHA matches exactly, and my independent re-extraction of the DOCX body reproduced the packet's extraction hash (`82f91c4e…3f24`) with 17 tables and sections 1–16. Cross-document facts (0060, 0061) also check out. Here is the standalone report.

---

# TTQS ONE 0063 R02 — Independent Semantic Review Report

**Review type:** independent semantic content review only (no visual/page review)
**Reviewer role:** independent semantic reviewer; not the writer, not the deterministic builder
**Files not modified:** no file was edited, rebuilt, or regenerated during this review

## 0. Binding identity (exact-candidate binding)

| Item | Value | Reviewer check |
|---|---|---|
| Candidate DOCX | `docs/ttqs-quality-20261016/quality-review/0063_R01/candidate/0063_R02.docx` | present |
| DOCX SHA-256 | `b1e8210b57d00813596d343403526787f065da51afcf5df4434868f0c96279f5` | **recomputed locally — matches exactly** |
| Official requirement | I14-E04 | bound |
| Official checkbox (box serial) | 068 (distinct from DOCX ID 0068) | bound |
| Official source | WDA TTQS《查核佐證文件資料表—訓練機構版》p.5, text 「是否提供查詢功能，並具持續改善機制。」 | bound |
| Unique Blueprint SHA-256 | `9c5e91155a18ccb5aae2a21f7bba40f35d8c483b973436873f08e2fde925dd34` | bound |
| Extracted body text SHA-256 | `82f91c4ee1c3ce29ab1673822cc2f67bdf7a2a5f5eaa955c47d23f7f7b1a3f24` | **reproduced independently from the DOCX** |
| Replacement register SHA-256 | `4f70d73b7ab7103d20e4ff6944a1442c506d28e40c916d6c38ccdba1968f0d0f` | bound |

**Method.** I reviewed the supplied packet (identity/hashes, official mapping, cross-document facts, full Unique Blueprint B1–B9, the synthetic replacement register SYN-063-001…020, and the complete extracted body) and cross-checked it against a fresh local extraction of the exact R02 DOCX. My extraction reproduced 87 non-empty paragraphs and 17 tables and yielded the identical body-text SHA-256, confirming the packet's "complete extracted body" is faithful and complete for the bound candidate. **Verdict is bound to the R02 candidate hash; R01 output was not used as this verdict.**

## 1. Overall verdict (semantic content only)

# ✅ PASS

The R02 candidate is a correct-genre, operationally complete, internally consistent, SAMPLE/REAL-bounded query-service procedure with a full query-failure/continuous-improvement work case. All mandated "check especially" facts are present and consistent. No hard rejection condition is triggered.

## 2. Category verdicts

| # | Category | Verdict |
|---|---|---|
| 1 | Official-purpose and three-code mapping (0063 / I14-E04 / box 068) | **PASS** |
| 2 | Correct document genre | **PASS** |
| 3 | Operational maturity/usability for a small volunteer association | **PASS** |
| 4 | Complete forms/tables/workflow/decision and HOLD/REJECT criteria | **PASS** |
| 5 | SAMPLE/REAL and authority boundary | **PASS** |
| 6 | Cross-document facts and no extra 0061 index entry | **PASS** |
| 7 | Arithmetic/date consistency | **PASS** |
| 8 | Title-blind identification and negative-neighbor separation (0060/0061/0062/0064) | **PASS** |
| 9 | Evidence replacement readiness | **PASS** |

No category is PARTIAL or FAIL. Section 5 lists non-blocking cosmetic observations only.

## 3. Evidence detail

### 3.1 Official-purpose and three-code mapping — PASS
- §1 control table (body rows 5–11): `文件編號 | 0063`, `對應要求 | I14-E04`, `官方方框 | 068`, `官方定位 | …p.5`, `原文重點 | 「是否提供查詢功能，並具持續改善機制。」`.
- The three codes are co-labelled and never merged: box serial `068` is kept distinct from file ID `0063` and never confused with DOCX ID 0068. §2 out-of-scope list also correctly cites neighbours by `I14-Exx` + file ID.
- Purpose matches the official double question: §2 states the document models operational query handling **and** the improvement mechanism (受理→查詢→回應→記錄→矯正→重測→追蹤).

### 3.2 Correct document genre — PASS
Genre = 查詢服務作業程序 ＋ 完整查詢失敗/改善合成案例 ＋ 可用表單. Confirmed by §4 (10-step process), §6 (decision table), §7 (response templates), §8/§14 (reusable + sample forms), §9–§13 (baseline matrix, 3 failure records, correction plan, retest, KPI). This is not a single query-application form and not a generic heading shell — it carries the real functional mechanics required by checkbox 068 (查詢案例、失敗紀錄、改善).

### 3.3 Operational usability for a small volunteer association — PASS
- §4 gives every step with explicit 輸入/動作/輸出.
- §5 role matrix gives five functional roles with duty-separation boundaries and `UNKNOWN／待協會確認` for actual appointment.
- §6 decision table, §7 response scripts, §8.1/§14.1 blank reusable forms, §13 reproducible KPI formulas — all directly operable by a small training-administration function without specialist staff. Language is plain and the responsibility split (受理 ≠ 權限複核; 改善登錄 ≠ 唯一複核) is explicitly stated in the §5 note.

### 3.4 Complete forms / workflow / decision and HOLD-REJECT — PASS
- §6 covers all required decision rows: 唯一命中, 無結果(零結果), 結果模糊, 範圍過寬, 來源/定位不完整, 權限保留/拒絕, 隱私風險, 重複/系統性失敗 — each with 動作, 紀錄 and 結案/停止條件.
- §16 states HOLD conditions (source index unconfirmed, permission unassigned, privacy risk, missing purpose/minimal scope), REJECT conditions (over-broad + refusal to supply, unlawful/improper purpose, request to disclose protected personal data, request to bypass permission by a hit), and the stop branch.
- §8.1 and §14.1 are complete reusable blanks (TEMPLATE/未填); §8.2 and §14.2 are completed synthetic instances.

### 3.5 SAMPLE/REAL and authority boundary — PASS
- §1 declares candidate status: "候選示範文件（草案），非協會已核定制度…也未證明協會現有查詢服務已經實際運作"; personnel/approval/signature are `UNKNOWN`.
- Every synthetic value is tagged `SAMPLE／SYNTHETIC` (case number, dates, roles, results, KPIs); blanks are tagged `TEMPLATE／未填`.
- No fabricated approval, signature, certificate, government letter, or third-party evidence; no real personal names or sensitive data (the only "role" fields are functional, and §8.2 uses "內部訓練行政（合成）").
- §15 + register SYN-063-001…020 define exactly what real records are needed before any value may be relabelled REAL; §15 closing line: "未取得上列證據前，維持標示 SAMPLE/SYNTHETIC，不得改寫為真實。"

### 3.6 Cross-document facts and no extra 0061 index entry — PASS
- §8.3 卡 A and §9 rows 1–4,8 cite the 0060 synthetic facts and these match the 0060 source I checked: case `SYN-0060-2026-A01`, course 「社區志工接待與資源轉介界線」, date `2026-08-15`, 報名 12／到課 10／缺席 2, source code `TT-2026-SYN60A-DO-ATT-RST-S3-006-V01`.
- §8.3 卡 B cites exactly `F-0061-2026-0001` (source doc_id 0060) and states "引用 0061 R03 唯一一筆 SAMPLE 索引；本測試卡只是查詢演練標籤，**不是新增 0061 索引列**"; the closing note repeats "並非兩筆 0061 索引紀錄". 0061's own register records this as "演練唯一 file_id（本件僅 1 筆）" — consistent. **No second 0061 index entry is created or implied.**
- §2 keeps 0062 (正本盤點), 0060 (缺口總登錄), 0064 (速度/效能) firmly out of scope; §1/§2/§5 keep 0061's index/permission design out of scope.

### 3.7 Arithmetic / date consistency — PASS
Verified against §9, §12, §13:

| Fact | Location | Check |
|---|---|---|
| 8 baseline tasks | §9 table rows 1–8 | 8 rows |
| baseline 成功 5 (1–4,8) | §9 closing line | 5+1+2 = 8 ✓ |
| baseline 零結果 1 (5) | §9 row 5 | ✓ (報到表) |
| baseline 需澄清 2 (6,7) | §9 rows 6–7 | ✓ |
| 5/8 = 62.5%, 1/8 = 12.5%, 2/8 = 25.0% | §13 rows 1–3 | 62.5+12.5+25.0 = 100% ✓ |
| 8 retest tasks, 首次成功 6 (1–5,8) | §12 rows + closing | 6+2 = 8 ✓ |
| 6/8 = 75.0%, 8/8 = 100.0% | §13 rows 4–5 | ✓ |
| improvement 75.0% − 62.5% = +12.5 pp | §13 row 6, §11/§5 | ✓ (percentage points, not %) |
| zero-result after alias fix 0÷8 = 0.0% | §13 row 7 | ✓ |
| Date order: 受理/基準 2026-10-26 → 矯正 2026-10-27 → 重測/結案 2026-10-28 → 追蹤 2026-11-25 | §8.2, §9–§12, §11/§14.2 | strictly increasing ✓ |
| Follow-up interval anchor | §11 「30 天追蹤」 + §8.2 受理日 2026-10-26 | 2026-10-26 + 30 日 = **2026-11-25** exactly ✓ (explicit anchor: the intake/baseline date stated at §8.2) |

Fixed denominator (8) is stated consistently in §13 ("分母規則：恆為 8；一筆查詢任務＝一筆觀測"), and all results are rounded to one decimal, matching §13's statement.

### 3.8 Title-blind identification and negative-neighbor separation — PASS
Title-blind: from content alone (查询/受理/權限/失敗/矯正/重測 + identity table 0063/I14-E04/068) the document is unmistakably the I14-E04 query-service + continuous-improvement artifact; no other universe document would fit.

Negative-neighbor separation (all four boundaries explicit):

| Neighbour | Boundary evidence in the candidate | Separation |
|---|---|---|
| 0060 / I14-E01 / 065 | §2 lists 缺口與改善事項之總登錄 as out-of-scope (0060); §8.3 uses `SYN-0060-2026-A01` only as a source-data card, never as 0063's own improvement record | clean |
| 0061 / I14-E02 / 066 | §2 excludes index field design & access/调阅 permission flow; §8.3 states the test card is "不是新增 0061 索引列"; §6 note "權限被拒不是搜尋失敗" | clean |
| 0062 / I14-E03 / 067 | §2 excludes 證據檔案清單與正本存放位置之盤點 (0062); no list/original-location inventory reproduced | clean |
| 0064 / I14-E05 / 069 | §2 excludes 檢索速度、回應時間、效能基準 (0064); §1 forbids reporting speed; §16 routes speed/performance issues to 0064 | clean |

### 3.9 Evidence replacement readiness — PASS
§15 gives a per-item "欲取代項 → 需取得之實際紀錄 → 查證功能角色" table (no real names), and the register carries 20 rows SYN-063-001…020 with `sample_or_synthetic`, `source_relation`, `replacement_or_validation`, and `evidence_required`, including the cross-document inherited SAMPLE items (SYN-063-007 for 0060, SYN-063-008 for the single 0061 index). This is sufficient to define exactly what must be obtained before any REAL promotion.

## 4. Mandated "check especially" items — all satisfied

| Required check | Result |
|---|---|
| 8 baseline + 8 retest tasks | present (§9, §12) |
| baseline 5/8, 1/8, 2/8 | present and arithmetically correct |
| retest 6/8, 8/8 within one clarification | present and correct |
| +12.5 percentage points | §13 row 6 — present, correct |
| zero result 0/8 | §13 row 7 (0÷8 = 0.0%) |
| no speed claims | none; speed/response-time/performance appear only as out-of-scope declarations (§2), prohibition (§1), stop-branch routing (§16), and checklist (§16). `秒` appears 0 times |
| permission denial ≠ search failure | stated §6 note and §13 分母規則 |
| 0061 remains one sample index entry | §8.3 卡 B + notes; no second entry |
| all actors and dates synthetic/proposed | roles `UNKNOWN／待協會確認`; every case/date/result tagged SAMPLE/SYNTHETIC |
| 2026-11-25 follow-up has an explicit valid anchor | §11 「30 天追蹤」 anchored to explicit intake/baseline date 2026-10-26 → exactly +30 days |

## 5. Minor, non-blocking observations (not PARTIAL/FAIL)

These are cosmetic/robustness suggestions; they do not affect the semantic verdict and require no rebuild to stay PASS.

1. **Follow-up anchor phrasing (optional strengthening).** §11 states "30 天追蹤。合成追蹤日 2026-11-25" but does not spell out the anchor date in prose. The value is valid against the explicit 受理/基準日 2026-10-26, but because the preceding sentence references 結案 on 2026-10-28, a reader could momentarily anchor to the closure date. Optional minimum improvement: add one clause such as "自受理/基準日 2026-10-26 起算 30 日". **Non-blocking — the anchor exists and the arithmetic is exact.**
2. **KPI formula column (§13).** The 公式 column repeats the generic "分子÷分母" and relies on the 代入 column (5÷8, 1÷8, …) for the concrete formula. Fully decodable and reproducible, just slightly condensed versus Blueprint B6's per-metric formula layout. Cosmetic.
3. **Retest label abbreviation (§12 row 3).** Task 3 is labelled "課程名稱" while §9 row 3 spells out the full course name. Same task, identical classification — labelling brevity only.
4. **Intake-no suffix (§8.2).** `SYN-0063-QI-2026-01-R6` adds an unexplained `-R6`. Harmless test-row tag; the case number `SYN-0063-QI-2026-01` is used consistently elsewhere.

Because none of these is a content, genre, boundary, or arithmetic defect, none changes the verdict.

## 6. Hard rejection conditions

**None present.** All B8/§16 hard-rejection triggers (over-broad request refusing supplementation, unlawful/improper purpose, request to disclose protected personal data, request to bypass permission by a search hit) are correctly defined as **document content** (the artifact's REJECT criteria) and none is committed by the candidate document itself. There is no fabricated third-party original, signature, certificate, government letter, or bank/accounting evidence; no fabricated approval or real-world operating claim; no extra 0061 index entry; no speed/performance claim; and no hard-fail placeholder ("待填/待核/空白表/保持空白/會後填寫") outside an explicitly labelled TEMPLATE or REAL-replacement area.

## 7. Visual review exclusion

Visual/page-layout review was **not part of my input and is outside this semantic verdict**. This report makes no claim about pagination, fonts, table rendering, orphan/widow control, or image quality. The packet's `PASS_LAYOUT` visual receipt (`evidence/render_R05/visual_review_R05.json`) is a separate, non-semantic signal and was not relied upon to reach any semantic conclusion here. Topic/text-level review only.

---

## 8. Terminal verdict

**Overall: PASS (semantic content only)** for candidate `0063_R02.docx`, bound to DOCX SHA-256 `b1e8210b57d00813596d343403526787f065da51afcf5df4434868f0c96279f5`, official requirement I14-E04 / checkbox 068, and Unique Blueprint SHA-256 `9c5e91155a18ccb5aae2a21f7bba40f35d8c483b973436873f08e2fde925dd34`. No hard rejection condition exists. All nine category verdicts are PASS; observations in §5 are non-blocking and require no rebuild. **VISUAL REVIEW OUT OF SCOPE — this verdict does not attest page/layout rendering.**

**TERMINAL VERDICT: PASS — 0063_R02 (I14-E04 / box 068), bound to DOCX SHA-256 b1e8210b57d00813596d343403526787f065da51afcf5df4434868f0c96279f5; semantic content only; visual review outside this verdict; no hard rejection condition.**