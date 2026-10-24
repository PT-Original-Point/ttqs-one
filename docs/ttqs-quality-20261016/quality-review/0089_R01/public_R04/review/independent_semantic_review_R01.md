# Independent Semantic Review — TTQS ONE 0089 (R04) — text-only, exact-SHA basis

## Verdict: PASS (candidate-level, SAMPLE/SYNTHETIC)
No material defects found. This verdict covers semantic content only. It is **not** formal association acceptance, not REAL-data verification, and not visual inspection. No tools were used; no files were modified; no fallback was invoked. All SHA values below are packet/receipt-asserted (I cannot recompute binaries in text-only mode); everything marked "recomputed" I verified by hand from the extracted text.

## 1. Exact identity
| Item | Value | Source |
|---|---|---|
| DOCX SHA-256 | `42bebbdfcaba93a753467260d5e1865b93b6bc2fee652a03d39b8fb385ef8476` | both receipts + extraction header (agree) |
| Requirement / deliverable | I17D-E03 / 0089, unique sibling (no co-deliverables) | Blueprint row, §2.1, §10.1 表10-1 |
| Official checkbox (verbatim) | 「品質不良率下降統計表。」 | §2.1 表; official p.6 extract |
| Official source | PDF `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`, 查核佐證文件資料表（訓練機構版）p.6, item 17d 成果評估 | packet + §13 附錄參照 |
| Unique Blueprint row | `fee9687e…19ad9a` (historical blueprint `2aa1d342…`, historical body use PROHIBITED) | packet |
| Checkbox serial | UNKNOWN — correctly **not** inferred anywhere in the body (no serial claimed; citations use page/item/ID only) | §2.1, §10.1 |

Checkbox uniqueness check (recomputed): 「品質不良率下降統計表。」 appears exactly once on the official p.6 extract, under 17d — the requirement→checkbox mapping is unambiguous, and the document's page-6/17d citation is unaltered (no historical-draft rewrite).

## 2. Title-blind genre check — PASS
Masking title, filename, and number, the body still resolves to a 品質不良率下降統計表 via专属 mechanism: defect definition (§3.5 缺陷檢核清單, DEF-01/02/03), rate formula with explicit numerator/denominator (§6.1), step-by-step two-period calculation (§6.2 表6-1), and result sentence "不良率由基準期 20.0%（8/40）降至追蹤期 5.0%（2/40）" (§6.5). The official quote is restated verbatim at §2.1 表. It cannot be moved unmodified to another requirement: unit of analysis is a record, not a person (§2.3 表2-1), and §2.3 explicitly refuses 0088 and 0090.

## 3. Neighbor / requirement-family comparison — PASS
- **I17C (17c 行為評估, p.6)**: 17c tracks client post-training action-plan execution (訓後動態調查表、行動計畫表追蹤紀錄、神秘客稽核). This document contains none of that — no trainee/client-level rows, no action-plan follow-up — so it cannot substitute for 17c, and 17c evidence could not satisfy this checkbox. Note (observation O2 below): 17c/17d scoring language is nearly identical ("有機制並能展現…紀錄" / "相關紀錄能展現具體成效"), so genre anchoring matters; §3.5 and §6.1–6.2 anchor firmly to a defect-rate statistic, which appears only in 17d's list.
- **I17D-E02 (0088, 就業及考照追蹤紀錄) and I17D-E04 (0090, 主管對參訓學員學習成效評估表)**: §2.3 表2-1 rejects both with checkable differentiators (analysis unit: record vs individual; observed value: record defect rate vs employment/certification status vs supervisor rating; case keys R001–R080 exclusive to this file). §10.2 forbids copying neighbor text or sharing case numbers.
- **17d scoring posture**: the artifact evidences a mechanism plus records (consistent with 17d's "有機制並能展現…紀錄" level) and deliberately does **not** claim 具體成效 for the association (§6.5, §8.1, SYN-CON-003) — correct given zero REAL data, and consistent with the packet's instruction not to claim a real improvement.

## 4. Arithmetic and case consistency — recomputed, PASS
| Quantity | Recomputed | Match |
|---|---|---|
| Baseline numerator | R001, R005, R010, R014, R019, R025, R031, R038 = 8 | ✓ §5.2 表5-3, §6.2 步驟1, SYN-CNT-002 |
| Baseline denominator / rate | 40 (R001–R040); 8÷40 = 20.0% | ✓ §6.2 步驟2–3 |
| Follow-up numerator / denominator / rate | R042, R067 = 2; 40 (R041–R080); 2÷40 = 5.0% | ✓ §5.3 表5-4, §6.2 步驟4–6 |
| Category reconciliation | 3+2+3=8; 0+1+1=2; totals 3/3/4 = 10 | ✓ §6.3 表6-2, SYN-CNT-010…015 |
| Complements | 32+8=40; 38+2=40; no-defect total 70 | ✓ §6.4 表6-3 #2, §7.1, SYN-DEC-003 |
| Change | 20.0−5.0 = 15.0 pp; (15.0/20.0)×100 = 75.0% | ✓ §6.2 步驟7–8 (receipt sign convention −15.0/−75.0 is equivalent) |
| Correction log | exactly 10 defect cases, baseline corrected 2026-06-07, follow-up 2026-06-24, review 2026-06-26; first-round numerator not retro-edited (8 and 2 retained) | ✓ §7.1 表7-1, §3.5, SYN-DEC-002 |
| Periods | 5 days each (06-01→06-05; 06-15→06-19), training day 06-08 sits between periods; checklist version SYN-CK-0089-V1 both periods | ✓ §3.2 表3-1, §6.4 #7–8 |
| Register reconciliation | 10 dates + 13 IDs + 80 records + 15 counts + 6 formulas + 3 conclusions + 3 categories + 10 decisions = **140 rows**, matching receipt; keys R001–R080 unique; all evidence_state=NOT_PROVIDED; third_party_original_required=NO throughout | ✓ matches receipt `synthetic_register_rows: 140` |
| Table count | I independently enumerated exactly **30 tables** in the extraction | ✓ matches receipt `docx_table_count: 30` |

## 5. SAMPLE/SYNTHETIC vs REAL boundary — PASS
Prominent marking at the head ("文件狀態：SAMPLE／SYNTHETIC（合成示範）版"), quick panel ("現在的數字是真的嗎？不是…不代表協會不良率曾經下降"), hard-boundary table (§8.1, document is "全部左欄"), seven REAL prerequisites all 未提供/NOT_PROVIDED (§8.2 表8-1), 12-item upgrade checklist (§8.4 表8-2), per-fact replacement register (§11.1, 140 rows, one fact per row, with locator, required source, replacement action, verifier role), and UNKNOWN/NOT_PROVIDED institutional status (§6.5, SYN-CON-003). Receipt `candidate_state: SAMPLE_SYNTHETIC_CANDIDATE_NOT_FORMALLY_ACCEPTED` and `formal_acceptance: NOT_GRANTED` agree. No REAL claim, no approval/signature/attendance/outcome assertion, no third-party original asserted (§8.3, correctly NO). §4.2 and §12 blank forms are explicitly labeled reusable blanks and are **not** used as the finished product — the finished content is the fully filled §5–§7 example, satisfying the "no empty-form completion" test.

## 6. Substantive usability — PASS
All 12 Blueprint `required_sections` present (§1–§13, including §12 blank forms); all 4 required table types present (§4.1 表4-1 欄位—定義—來源—填寫者—驗證規則; §5.2/5.3 filled records + §5.4 status codes; §7.1 表7-1 + §7.3 表7-2 exceptions/correction/verifier; §10.1 表10-1 traceability). Role separation enforced (§1.2 表1-1: A/B/C/D, no self-review), data minimization (§1.3), HOLD rules (§3.4), acceptance/reject/reopen rules (§7.3), retention/access (§9), rounding rule (§6.1), 30-second first-page panel with purpose/reader/timing/output/status (quick panel), and no internal build hashes in the body (§13). Font claims (11pt body / 9.5pt table) are receipt-asserted only.

## 7. Findings
**Material findings: none.**

Non-blocking observations (all located):
1. **O1 (low) Version-label divergence** — body self-identifies as `SAMPLE-R01` / `candidate/0089_R01_body.md` (§13 表13-1「正文」列; §11.1; register `document_locator` column) while receipts declare DOCX revision R04, and §13 states "任何修改升版號". The R03/R04 changes are receipt-described as pagination-only, so this reads as content-version vs build-revision, but an explicit mapping would prevent miscitation.
2. **O2 (low) No explicit 17c carve-out** — §2.3 表2-1 names only I17D-E02/E04 per Blueprint `negative_choice_neighbors`; given 17c's near-identical 2分/3分 wording on the same page 6, one explicit 17c 行為評估 refusal line would harden the boundary. Title-blind test passes regardless.
3. **O3 (cosmetic) Wording** — §6.1 "有至少一項合格缺陷之記錄筆數" reads awkwardly; "至少一項缺陷成立之記錄數" would be clearer.
4. **O4 (scope note) Metric choice** — 品質不良率 is operationalized as documentation-quality defects in activity service records (§3.5 DEF-01/02/03). Defensible (official text defines no metric, per §2.1; coherent with the synthetic course subject, §5.1 表5-1), but for REAL 17d 具體成效 evidence the association should confirm this metric matches its approved quality scope — already gated by §8.2.
5. **O5 (very low) Register granularity** — the narrative cells 情境／測量單位 in §5.1 表5-1 have no dedicated register keys; every Blueprint-enumerated fact class (dates, roles, numbers, ratios, paths, results, decisions) is covered.
6. **O6 (verification boundary)** — font sizes, 35-page count, landscape sections, pixel-identity claims, zip integrity, and all SHA values are receipt-asserted; this review confirms only what is verifiable in text (including the independent 30-table and 140-row reconciliations above).

## 8. Scope statement
Text-only review of the exact-SHA candidate `42bebbdf…8476` against official p.6 (PDF `805386b7…4709`) and the current unique Blueprint row `fee9687e…9ad9a`. No visual inspection is claimed or implied; the visual receipt's page-level assertions are treated as unverified inputs. No REAL-data verification is performed or implied. **Formal association acceptance: NOT_GRANTED** — this verdict is a semantic recommendation only.