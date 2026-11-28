## RESULT=PASS

**exact candidate SHA:** 8C004FB986747CC7FA5FFF77D720252C708F66BE7EB085AA87D7658A4160E1DE  
**REVIEWED_INPUT_SHA256:** B991859C2A45631813740930515FFCAB2DEBE4D7DCC660CF78636A0EDE999BDF

---

## FINDINGS

| Severity | Section/Table Locator | Chinese Excerpt (≤25 chars) | Issue & Minimal Correction |
|----------|----------------------|----------------------------|----------------------------|
| INFO | Ch.1 役職責任說明 (職能項目矩陣) | `專業訓練人員職能評估` | Document correctly identifies as professional training personnel capability assessment method; no substitution for I06-E01 (third-party experience) or I06-E03 (institution/manager capacity). Negative neighbors (row 029 training/work experience proof, row 031 small-association operational duties, row 032 other, PDF indicator 7 training need analysis) are explicitly rejected. |
| INFO | Ch.3 量規與評估準備 | `量規、角色分數、落差、改善、複評` | All five required mechanism categories present: indicators/observable behaviors, role scores with target/actual comparison, gap calculation rules, improvement actions with responsibility/limit/evidence, re-evaluation with comparable scale. No official score scale claimed; sample 1-4 scale explicitly marked SAMPLE/SYNTHETIC. |
| INFO | Ch.4 完整 SAMPLE/SYNTHETIC 案例 | `SAMPLE/SYNTHETIC 完整操作示例` | Full workflow from initial assessment through improvement actions, re-evaluation, and decision demonstrated. All person codes, roles, scores, dates, gaps, improvement results, re-evaluation, and decisions labelled SAMPLE/SYNTHETIC. No real-person data presented as fact. |
| INFO | Ch.7 事實連結索引 | `事實連結逐項登錄` | Synthetic register contains 82+ entries (SYN-0031-CASE-001 through SYN-0031-RE-AVERAGE-002), each with case_id, doc_id, field, value, assumed basis/reason, and document positioning. Register entries cross-reference each section uniquely; no "data recorded" substitution for individual item verification. |
| INFO | Ch.8 REAL 替換清冊 | `REAL 替換清冊 全項 UNKNOWN` | Per-ID REAL replacement register covers every SAMPLE/SYNTHETIC field (case, person, role, method scale, target, gap, average, action, owner, review, evidence, criterion, re-score, delta, final gap, decision). All 82+ entries explicitly state REAL 狀態: UNKNOWN with precise REAL sourcing requirements and verification dependency notes. No示例 values retained as REAL. |
| INFO | 官方來源定位 | `Official PDF 紙面第 2 頁` | Official source correctly identified: TTQS evidence table R04, p.2, indicator 6 (training institution administrative management capability & training supervisor related functions), rightmost column "common reference evidence data (note source & page)", 2nd checkbox: "專業訓練人員職能評估方法等證明". Matches Blueprint 157 row 030 exactly. |
| INFO | 邊界檢核 | `負向近鄰排除` | Document explicitly rejects: row 029 (training/work experience proof index/acquisition), row 031 (small-association operational duties/division/supplement/permission/operation cases), row 032 (other/BLOCKED_UNTIL_UNIQUE_OTHER_NAMED), and PDF indicator 7 (training need analysis/application). 0031 not a substitute for any negative-neighbor scope. |

---

## SAMPLE/SYNTHETIC FACT REGISTER & REAL REPLACEMENT REGISTER

**Visibility:** Complete — the document contains a synthetic register (Ch.7) with every synthetic value indexed by unique ID, and a per-ID REAL replacement register (Ch.8) mapping each SAMPLE/SYNTHETIC field to its required REAL source, precise positioning requirement, and current UNKNOWN status.

**Completeness:** The REAL replacement register contains 82+ entries (SYN-0031-CASE-001 through SYN-0031-RE-AVERAGE-002, plus all intermediate IDs for scores, gaps, actions, owners, reviews, evidence, criteria, re-scores, deltas, final gaps, and decisions). Every entry has:示例值, REAL replacement source & exact positioning requirement, and REAL 狀態: UNKNOWN with verification responsibility noted. No entry lacks a positioning requirement or has a REAL value substituted without source dependency.

---

## INDEPENDENT RECOMPUTATION OF STATED VALUES

| Stated Value | Computation | Verified |
|---|---|---|
| 課程設計者 初評角色平均 2.5 | (3+2+3+2)/4 = 10/4 = 2.5 | ✓ |
| 授課講師 初評角色平均 2.75 | (3+3+2+3)/4 = 11/4 = 2.75 | ✓ |
| 課程設計者 正落差計數 2 | Gaps: COMP-002 (1), COMP-004 (1); others 0 | ✓ |
| 授課講師 正落差計數 1 | Gap: COMP-003 (1); others 0 | ✓ |
| 複評後 課程設計者 平均 3.0 | All 4 re-evaluation scores = 3; (3+3+3+3)/4 = 3.0 | ✓ |
| 複評後 授課講師 平均 3.0 | All 4 re-evaluation scores = 3; (3+3+3+3)/4 = 3.0 | ✓ |
| 落差公式: 目標 − 實得分數 | Document states: "落差 = 目標分數 - 實得分數" | ✓ (no zero/negative abatement by opposite-positive) |
| 平均數不跨角色合併 | Document states: "不跨角色合併，也不取代逐項判定" | ✓ |

All stated scores, gaps, averages, and reassessment values independently recomputed and consistent with documented formulas.

---

## UNVERIFIABLE REAL-WORLD CLAIMS

All real-world claims (personnel names, actual role assignments, real scores, real evidence files, real assessor authorization, real improvement/completion decisions, real certification/authorization) are explicitly maintained as **UNKNOWN** in the REAL replacement register (Ch.8). The document states: "目前均為 UNKNOWN，除非另有可核驗來源." No real-world claims are inferred or constructed from the SAMPLE/SYNTHETIC demonstration. No real-person names, actual scores, or real authorization details appear as facts.

---

## 0031 SUBSITUTION CHECK

- **I06-E01 (third-party experience originals):** 0031 is explicitly not a training/work experience proof index or third-party acquisition procedure document. Negative-neighbor rejection (row 029) confirmed in both blueprint and document text.
- **I06-E03 (institution/manager capacity):** 0031 is explicitly not a small-association operational duties, division, supplement, permission, or administrative operation cases document. Negative-neighbor rejection (row 031) confirmed. Document scope locked to I06-E02 unique mapping; no "other" files invented (row 032 rejection observed).

**0031 is not a substitute for I06-E01 or I06-E03.**
