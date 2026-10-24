# Independent exact-SHA semantic review — TTQS ONE 0088 R07

**DOCX SHA-256 (echoed exactly):** `83ff96699e8c3e01852524047c822f912323207b2c22eb7e6fdb2cc561a5b5dc`
**Body SHA-256:** `04bc085c8a843dda41ce3c7ec87d40bd8a589650e8d087ff9874b9d89518814e`
**Verdict: PASS** (semantic, text-only, bound to this SHA). Real-evidence status: **UNKNOWN**. Official serial: **UNKNOWN**. DOCX binary/fonts/pagination/layout: **NOT INSPECTED** — no claims made. This PASS is not formal acceptance; state remains `SAMPLE_SYNTHETIC_CANDIDATE_NOT_FORMALLY_ACCEPTED`.

## 1. R05 blocker — RESOLVED

R05 blocker: no real stop/close vocabulary; §11/§12.1 forced a false `—SAMPLE` label; `STOP` produced no clean primary disposition.

R07 fixes verified:
- §11 defines five real dispositions: `OPEN_ACTION`／`HOLD`／`CLOSED`／`CLOSED—NO_RESPONSE`／`STOPPED/WITHDRAWN`, and states the two `—SAMPLE` labels "僅為 §9 合成案件的展示標籤…不得在真實個案中選用."
- §12.1 `主處置狀態` now offers exactly the five real labels and bars sample labels in real cases.
- §3.3: "`STOP` 僅為本節的聯絡閘門判定，不是案件主處置；…對應的案件主處置為 `STOPPED/WITHDRAWN`…結果維持 `UNKNOWN`." §7.2, §11 table row ("未授權聯絡或學員要求停止 | 閘門 `STOP` → 主處置 `STOPPED/WITHDRAWN`"), §11 可停止, and §11.1.3 all agree. The R05 hybrid-label defect is gone.

All three R04-era resolutions show no regression: C01/C07 remain `OPEN_ACTION` with independent exam `HOLD` (§9.2, §9.3 "獨立重疊計數，不併入主處置"); C09 remains `HOLD` with result date `UNKNOWN` ("2026-08-01 為目標期限，非結果日期", §6.3/§9.2/register `SYN-C09-EXAM-RESULT-DATE`); §3.2 chronology keeps 7/29 as attempt 1 only for C11/C12, with no-response closure only after attempts 2–3 through 2026-08-12.

## 2. Independent recomputation

| Metric | Recomputed | Displayed | Match |
|---|---|---|---|
| Response rate | 10÷12=0.8333…→83.3% | 83.3% | ✓ |
| Employment (respondents) | 6÷10=60.0% | 60.0% | ✓ |
| Cohort share | 6÷12=50.0% | 50.0% | ✓ |
| Exam self-reported pass | 3÷4=75.0% | 75.0% | ✓ |
| Verification coverage | 0÷3=0.0% | 0.0% | ✓ |

Dates: 2026-04-30 +90 = 2026-07-29 ✓. All five exam targets (6/20, 7/10, 7/20, 8/1, 7/25) precede the 2026-08-12 cutoff ✓. Gate expiry 2026-09-30 postdates all contact dates ✓. Handoff/due/next dates (8/13–14, 9/12–13, 8/26–27) all postdate the cutoff, matching §9.4's statement. Counts reconcile: 6+2+1+1+2=12 responses; 5 exam-due + 7 N/A = 12; dispositions 6+2+2+2=12; exam HOLD=4 (C01,C02,C07,C09) overlapping, not merged. §9.4's six OPEN_ACTION rows equal §9.3's six. Employment start months (2026-05/06/07) all follow completion ✓.

## 3. Mapping, purpose, safeguards — PASS

Control binding (doc_id 0088, I17D-E02, page-6 text `就業及考照追蹤紀錄。`, serial UNKNOWN) matches the official packet; no serial inferred. §2.2 and §14.2 separate E01 (survey) and E03 (quality-defect rates) and forbid sharing samples/denominators. Title-blind reading (§1.1, §5.1, §6.1, §9.2) still points to individual employment/exam tracking. SAMPLE/REAL boundary is strong: cover banner, `—SAMPLE` labels, §11 bar on sample labels in real cases, blank forms "狀態一律 HOLD", register `SYNTHETIC_NOT_REAL`/`NOT_PROVIDED` with `third_party_original_required=YES`, zero originals, no signatures/approvals/certificates, "不得解讀為實際無人通過" (§9.3), "明確未發生任何服務、轉介送出" (§9.4). Roles (§3.1 incl. dual-role disclosure), gate (§3.2 eight fields, 缺一即 HOLD), reopen (§11 table, §11.1.5 with recalculation) are internally consistent. Register matches the Blueprint §H schema exactly and covers 12 case IDs, contacts, metrics 1–18, 5 ratios, 9 gate facts, 6 handoffs, 4 evidence IDs, cohort 15=12+3, originals=0. Small-association operability is adequate: §1.3 quick start, §4 eight steps, neutral scripts (§7.3), §12.1–§12.5 blank forms, §11 escalation order.

## 4. Non-blocking items

- C02/C09 (primary `HOLD`) have no named owner or review date in the sample (§9.4 covers only OPEN_ACTION); §12.1's `覆核期限` exists only as a blank field.
- Register: no aggregate rows for disposition counts (6/2/2/2) or skill-relation N/A; §9.3 lacks a skill-relation N/A row.
- Copy-paste note in all seven `SYN-C##-EXAM-NA` rows ("C11 also has no employment response…") is C11-specific text on C03–C10 rows.
- Locator imprecision: `SYN-C01/C02/C07-STATE` cite §13.1 (no state rows there); `SYN-C11/C12-SUPPORT` cite §5.3 (no C11/C12 rows in §5.3).
- §12.2 still lacks an explicit evidence-grade (E0–E3) field; §12.4 still places case_id as a data row.
- §9.4's "覆核 RV-SYN-01、主管 SV-SYN-01" is terse; improved but could explicitly say "指派，未發生".
- Associations lacking pre-approved eligibility rules or contact basis are correctly held (§12.1 未知即 HOLD) but the packet offers no turnkey path to obtain them.

## 5. UNKNOWNs

Official 157-item serial; DOCX binary/fonts/pagination/layout (not inspected); real rosters, eligibility rules, consent/basis, responses, employment/exam originals, approvals and reviews; legal sufficiency of the data-use basis.

**Final: PASS** — the sole R05 blocker is resolved; arithmetic, dates, 12-case reconciliation, three-track states, register, gate, SAMPLE/REAL boundary and cross-section consistency hold under independent recomputation. Candidate remains unaccepted pending serial resolution and separate technical/visual receipts.
