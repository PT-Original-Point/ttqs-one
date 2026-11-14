VERDICT: PASS

Review bound to candidate DOCX SHA-256 `faafe2dc117cacaabd7d9dde5b71adec7efd6eb55d1a32efe924e0ed781f3b5b` (79799 bytes, 34-page Word-export PDF, sample/CANDIDATE). All statements below concern only that exact SHA. Evidence basis: the packet's complete page-numbered PDF text; the visual receipt is treated as context only — no visual or font-size inspection is inferred or claimed.

## Prior findings N1–N12 (re-adjudicated)

| ID | Status | Locator in candidate |
|---|---|---|
| N1 core Q1–Q5 mandatory rule empty stub | Fixed | §5.2, pp. 11–12, items 1–4 (Q0 gate; Q1 authorization/calculation; Q1–Q5 blank-count rule "空白達 2 題…不完整資料"; Q6/Q7 rules) |
| N2 trainee code missing/mismatch → HOLD/pre-fill/codebook | Fixed | p. 4 Table 1 row 受訓人員代碼 (預填／缺漏或不符即 HOLD); p. 6 基本觀察背景; p. 3 §2.2-3; p. 19 §8.1 item 2 |
| N3 who completes schedule/attendance/use fields; authorization constrains respondent | Fixed | p. 7 Q1 工作人員預核欄 (a,b)／受訪者本人 (d)／工作人員計算欄 (c,e,f); p. 8 行政代碼; p. 11 §5.1; p. 12 §6.1-3 |
| N4 unrounded banding vs display rounding | Fixed | p. 7 Q1 ("先以未四捨五入的 f 分帶，再…小數一位"); p. 11 §5.1; p. 30 FACT-37 |
| N5 HOLD closure and denominators | Fixed | p. 19 §8.1 items 10 + HOLD 結案 paragraph; p. 18 §7.2 identity N_returned=N_valid+N_excluded+N_stopped+N_hold, N_corecomplete ⊂ N_valid; p. 20 "HOLD 卷不進有效分母" |
| N6 Q0 reason-code map | Fixed | p. 7 Q0 (01/02/03/04); p. 15 Table 2 row Q0 否原因代碼 |
| N7 Q0=2 exclusion regardless of reason | Fixed | p. 2 §2.2-1; p. 7 Q0 note; p. 15 Table 2; p. 19 §8.1-2; p. 34 checklist |
| N8 Q0=1 with Q1=99-A contradiction | Fixed | p. 12 §5.2-2; p. 19 §8.1 item 7; p. 20 §8.1-3 ("Q0=1 與 99-A 矛盾…HOLD") |
| N9 Q4 only within comparable metric subgroups | Fixed | p. 11 §5.1 (指標、單位、判讀方向、期間窗口相同子群內呈現，不得合併平均); p. 21–22 Table 3 Q4 rows |
| N10 artifact-only observers | Fixed | p. 2 §2.2-2 (只看成果物 → 本人選 Q0=3 或留白 → HOLD，不得推定); p. 7 Q0 instruction |
| N11 Table 1 crosswalk/construct mapping | Fixed | pp. 4–5 Table 1 (題目—構面—作答方式—跳題／計算—用途); §3 構面 A–D; p. 32–33 Table 5 traceability |
| N12 FACT-10/12/35 date references | Fixed | p. 26 FACT-10 (↔FACT-35); p. 27 FACT-12; p. 29 FACT-35 (↔FACT-10); dates internally consistent (see below) |

Carried checks all hold: Q10 collects no contact data and 99 is administrative only (pp. 10, 13 §6.2, p. 17 Table 2); Table 3 contains both Q5 and Q10 paths (pp. 21–22); the 5–8 minute figure is explicitly "未經真人試測的粗估" (pp. 1, 13, 23); no fabricated pilot, approval, respondents, signatures, or third-party records (p. 24 §10.2 declares pilot status UNKNOWN).

## New findings (minor only; no new material defect)

1. **Minor — literal escape artifact.** p. 34, 發放前快速確認, 2nd→3rd checkbox: literal `\n-` appears in the text ("…缺漏或不符時 HOLD。`\n`- ☐ Q0 只有本人明確選 2…"), breaking bullet style. Smallest repair: replace `\n- ` with a real paragraph break and the same `• ☐` bullet.
2. **Minor — reason-code wording tension.** p. 7 Q0 option 2 says 原因代碼「擇一」while p. 2 §2.2-1 permits 原因碼「留白」. The exclusion rule itself is unambiguous ("不論原因碼…或留白"), so this is wording only. Smallest repair: on p. 7 write 「原因代碼擇一（可留白；不影響 Q0=2 判定）」.
3. **Minor — Blueprint cross-reference IDs absent from body.** The doc cites 官方佐證資料表第 6 頁 (p. 32 Table 5) but nowhere states 文件編號 0093／需求 I17D-E07, nor neighbor IDs I17D-E06 / I18-E01. Smallest repair: one line in §12 preface logging 0093 / I17D-E07 and the two adjacent requirement IDs.

## Independent recalculations and verifications

- **Q1 recalculation:** a=5 d/wk, b=27, d=18 → c=b÷a=5.4 wk; e=d÷c=18÷5.4=3.3333… d/wk; f=e÷a=d÷b=18÷27=0.666666… = 66.666…%; display 66.7%; unrounded value falls in 60%≤f<100% → band **4**. Matches candidate (p. 7 computation, p. 13–14 demo, p. 16 Table 2, p. 30 FACT-37). Guards a>0, b>0, 0≤d≤b all satisfied; b=0 no-division rule present (pp. 7, 12).
- **Q0/Q1 logic:** only personal Q0=2 excludes regardless of reason; Q0=3/blank → HOLD (never presumed "no"); Q0=1 with 99-A, a≤0, b=0, or d>b → stop and HOLD (pp. 2, 12, 19–20). 99-A/B/C counted separately, excluded from means (pp. 8, 11, 16, 19). No contradiction found.
- **Dates:** 結訓 2026-08-10 + 30 d = 2026-09-09 ✓; + 66 d = 2026-10-15 ✓ (FACT-11 "訓後第 66 日" ✓); pre-baseline 2026-07-13→08-09 ends before 開訓 08-10 ✓; baseline 07-13→08-09 identical across p. 13–14, FACT-29/30 ✓.
- **Denominators:** 2=1+1+0+0 ✓; 回收率 2÷2=100.0%; 有效占回收 1÷2=50.0% ✓; Q3 mean 4÷1=4.0 (n=1) ✓; Q4 N_valid=0 → no mean, no 0/3 conversion ✓; HOLD excluded from N_valid/N_corecomplete ✓.
- **SAMPLE/REAL boundary:** per-page SAMPLE/CANDIDATE headers; FACT-01…37 all UNKNOWN／不得替換或宣稱 REAL (pp. 26–30); §11.2 replacement register complete; no REAL claims, no fabricated pilot/approval/records ✓.
- **Neighbor usage (0092 / I17D-E06 感謝函; 0094 / I18-E01 口述滿意):** p. 1 §1.1 "不是學員滿意度問卷、雇主感謝函"; p. 32 Table 5 "與感謝函工具、滿意度調查的用途不同" — both error neighbors explicitly rejected, difference stated by genre and section; no neighbor facts absorbed. (Neighborhood rejection satisfied; ID citation gap logged as minor finding 3.)
- **Not verified in this review:** font sizes (≥10.5pt body / ≥9.5pt tables) and layout/rendering — text-only evidence; no inference drawn from the visual receipt.

Model/provider identity: MiMo-V2.6-Flash Free (provider: opencode, model ID mimo-v2.6-flash-free) — natively exposed.

This is an independent candidate review of the stated SHA only, not formal TTQS acceptance or certification of any official checkbox.