# Independent semantic review request — DOCX 0101 / I18-E08 / final9

This is a fresh exact-SHA, read-only semantic review. You are independent from the OpenCode Writer session and deterministic DOCX builder. Do not edit files, run tools, make external calls, or infer facts beyond supplied sources. Review the current final9 content, not any earlier candidate. Return one JSON object followed by a short note. Verdicts must be PASS, PARTIAL or FAIL by criterion and overall. Cite page/section/table locators from the page-labeled Word-native PDF text. Echo the exact candidate SHA. Formal acceptance must remain NOT_GRANTED. Do not treat builder QA as your independent conclusion; it only verifies artifact identity and supplies technical facts.

## Exact artifact identity
- DOC_ID: 0101
- Official requirement: I18-E08
- Official printed checkbox serial: UNKNOWN
- Exact candidate DOCX SHA-256: 56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68
- Word-native PDF SHA-256: 27002fa5e60ba712be1e38952f04bd12ba64d04661fa34101f1e09462c3ce4b2
- Candidate state: SAMPLE / SYNTHETIC candidate; NOT formally accepted
- Paired 0100 remote-readback SHA-256: debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2
- Official purpose per source packet: learner pre/post self-assessment and perceived-change radar analysis.
- Unique Blueprint SHA-256: 51b5a85d08c85550fa18de656ab7e9cdb3923831f4584ea7e9bf4da3ce35e8ce
- Source packet SHA-256: 81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886

## Review criteria
A. Correct I18-E08 purpose and genre; distinguish 0101 aggregate radar analysis from 0100 data-capture instrument and 0097/I18-E05, 0098/I18-E06, 0099/I18-E07.
B. Verify source lineage and pairing/version/date rules; distinguish doc_id from official printed checkbox serial UNKNOWN.
C. Independently recompute 8×5×2=80 raw values, row totals/deltas, dimension totals/means/differences, overall means, denominator, percentages, chart and table duplicates.
D. Check administrative usability, steps, roles, inclusion/exclusion, HOLD/REJECT rules, and replacement register.
E. Check SAMPLE/REAL boundary, no fabricated decision/signature/records, no unsupported causal/significance/competence claims, and no imported 0099 pass threshold.
F. Check cautious interpretation and recommendations.
G. Title-blind classification against adjacent requirements.
H. Re-check prior exact-final8 PARTIAL items on final9: (1) nonexistent §8.4 reference, (2) two A4 portrait-only checklist claims despite 12 landscape pages, (3) residual “four-digit code” phrase for A01-A08. Determine whether each is resolved in current final9. Look for new contradictions caused by the edits.
I. Human usability and readable self-contained content. Do not assess visual pixels; a separate direct visual receipt is supplied.

## Required JSON schema
{"doc_id":"0101","requirement_id":"I18-E08","docx_sha256":"...","overall":"PASS|PARTIAL|FAIL","criteria":{"A":{"status":"PASS|PARTIAL|FAIL","locators":[],"finding":"..."}}, "arithmetic":{"status":"PASS|FAIL","checks":[]},"blocking_defects":[],"nonblocking_notes":[],"review_scope_limitations":[],"formal_acceptance":"NOT_GRANTED"}

## Previous exact-final8 independent review (historical; not verdict for final9)
```json
{
  "doc_id": "0101",
  "requirement_id": "I18-E08",
  "docx_sha256": "92edebeff1703104c30486e18cf568f6666310a20ae8a945ab9d03789ec21fdb",
  "overall": "PARTIAL",
  "criteria": {
    "A": {
      "status": "PASS",
      "locators": [
        "p.1 §1.1 報告目的",
        "p.1–2 §1.2 文件識別與版本",
        "p.3 §1.3 使用情境",
        "p.5 §3.1 分析鏈",
        "p.5–6 表3-1",
        "p.29 表11-1",
        "p.29 §11 盲測順序"
      ],
      "finding": "Correct genre and purpose: a descriptive aggregate report on eight synthetic pre/post self-rating pairs, not the data-capture instrument. §1.1 limits the report to four questions (80-cell completeness/range; pre/post totals, means and dimension differences; fixed 0–4 radar specification; REAL replacement/HOLD-REJECT conditions) and expressly refuses effectiveness, competence gain, pass/fail, comparative and validity claims. §3.1 and 表3-1 separate 0100 (form) from 0101 (aggregate); 表11-1/§11 distinguish 0097 perception, 0098 satisfaction and 0099 rubric-based skill evidence, so the neighbouring requirements are not conflated."
    },
    "B": {
      "status": "PASS",
      "locators": [
        "p.1–2 §1.2 配套表單、配套狀態、示範施測日期",
        "p.2 版本註記",
        "p.5–6 表3-1 來源與版本綁定",
        "p.6–7 表3-2 樣本與課程基本資料",
        "p.7 §4.1 納入條件",
        "p.20–21 表10-2 S-01–S-06",
        "p.30 §12.1 A",
        "p.31 §12.3",
        "p.32 §12.4"
      ],
      "finding": "Identity and pairing are clear: DOC_ID 0101 / I18-E08, official printed serial UNKNOWN in §1.2 and §12.1 A, and no internal index is used as a serial. The companion is 0100 R09 candidate, inner version R09a, questionnaire SR-0100-v1.0-SAMPLE, with same course/session, post date not earlier than pre and same-version rules (§1.2, §3.2, 表3-2, §4.1, 表10-2 S-01–S-06, §12.3). The supplied 0100 table matches the 80 cells exactly. The exact 0100 SHA is not printed in final8; byte-level binding is external (packet/receipt), so version/date lineage is document-level and exact-SHA lineage is packet-level."
    },
    "C": {
      "status": "PASS",
      "locators": [
        "p.4 表2-1、表2-2",
        "p.10 表5-1",
        "p.11 表6-1、表6-2",
        "p.11–12 §6.3 交叉驗算",
        "p.12 表7-1",
        "p.14 圖1 替代文字",
        "p.15 表8-1",
        "p.22–26 §10.5 定位表",
        "p.26–27 表10-3",
        "p.27 表10-4",
        "p.27–28 表10-5"
      ],
      "finding": "All arithmetic recomputes and all duplicates agree. The 80 cells, row totals/deltas, dimension totals/means/deltas, overall means and 160-denominator percentages match 表2-1/2-2, 表5-1, 表6-1/6-2, 表7-1, 表8-1, 表10-3/10-4/10-5, 圖1 alt text and §12.3. The locator map has exactly 80 unique rows and matches 表5-1 cell-for-cell; A05/前E=2 is present on p.24, confirming the prior 79-row report was an extraction artifact."
    },
    "D": {
      "status": "PASS",
      "locators": [
        "p.7–8 §4.1–4.2 表4-1",
        "p.8–9 §4.3 表4-2、表4-3",
        "p.16–18 §9.1–9.2",
        "p.18 表10-1",
        "p.19 §10.2 替換檢查清單",
        "p.20–21 表10-2",
        "p.21–22 §10.4 定位與核對代碼",
        "p.22–26 §10.5",
        "p.26–28 表10-3–10-5"
      ],
      "finding": "Usable administrative machinery: eight inclusion conditions, explicit denominators, no-imputation, 表4-1/表10-1 error rules, V1–V7/H1–H4 codes, a 17-item REAL replacement checklist, eight recommended roles and a nine-step trigger/stop workflow, plus 表10-2 S-01–S-15 with replacement source, verification and HOLD action for every SAMPLE field class. Escalation from unresolved HOLD to REJECT/H3 is stated (§10.4–§10.5). A reader can execute this without the review packet."
    },
    "E": {
      "status": "PASS",
      "locators": [
        "p.1 SAMPLE／SYNTHETIC 邊界警告",
        "全篇頁首／頁尾標記",
        "p.2 §1.2 資料性質",
        "p.3 §1.3–1.4",
        "p.5 §2.3",
        "p.6 §3.3 五點邊界",
        "p.14 §7.4",
        "p.15–16 §8.2–8.3",
        "p.31 §12.3"
      ],
      "finding": "SAMPLE/SYNTHETIC boundaries hold throughout: front-page warning and every page header/footer; 資料性質 in §1.2; blank approval fields in §1.4; no names, signatures, association decisions, real course results or validated-scale claims. 0099 reuse is fenced by five statements (§3.3), and 14/20 appears only in exclusion/boundary contexts (§3.3 item 4, §7.4, §8.3, 表11-1). No causal, significance, pass-rate or competence claims are made; §8.2–8.3 explicitly disclaim them."
    },
    "F": {
      "status": "PASS",
      "locators": [
        "p.4 表2-2 後段",
        "p.15 表8-1",
        "p.15 §8.2",
        "p.16 §8.3",
        "p.16–17 §9.1–9.3",
        "p.30–31 §12.1 D"
      ],
      "finding": "Interpretation is arithmetic only: D +1.250 largest, E +0.875 smallest, A/B +1.000, C +1.125, with explicit denial of significance, effect size, causality, ranking and population inference; §8.1 warns that a 3.125 group mean does not mean every learner scored 3+. Follow-up items in §9 are labelled '建議程序，不是已完成的事實' and keep any objective task, consent, rubric and dataset separate. No recommendation is presented as completed."
    },
    "G": {
      "status": "PASS",
      "locators": [
        "p.29 表11-1 盲標題邊界",
        "p.29 §11 五步盲測順序",
        "p.5 §3.1 分析鏈",
        "p.1–2 §1.1–1.2"
      ],
      "finding": "Title-blind identification works: the body alone reveals n=8, 80 cells, 75/117/+42, five dimension means, a fixed 0–4 radar with legend/denominator disclosure and a companion 0100. 表11-1 and §11's five tests distinguish 0100 (blank ticks, pre/post pages, five items/version field), 0099 (rater, rubric, 14/20), 0098 (satisfaction) and 0097 (perception), so the artifact is identifiable without DOC_ID or filename."
    },
    "H": {
      "status": "PARTIAL",
      "locators": [
        "p.3 §1.5 閱讀路徑",
        "p.24 §10.5 A05 前E",
        "p.20 表10-2 S-01–S-06",
        "p.18 表10-1",
        "p.1、p.7 合成日期說明",
        "p.19 §10.2",
        "p.6–7 表3-2",
        "p.30–31 §12.1 A、E",
        "p.32 §12.4"
      ],
      "finding": "Prior findings are resolved on the exact final8 text: (i) §10.5 has exactly 80 unique locator rows; A05/前E=2 appears on p.24 and in the DOCX table, with no missing/extra rows; (ii) 表10-2 S-01 now cites §3.4 表3-2 and S-02–S-06 cite §1.2/§3.4 表3-2 (p.20), matching the actual field locations; (iii) 表10-1 now reads '僅在本人可安全確認時' (p.18), typo fixed; (iv) the 2026-11-02 sample date is expressly labelled a synthetic placeholder on p.1 and p.7, so no session is implied; (v) §10.2 (p.19) now says '不得在報告公開原始配對碼' without the four-digit mismatch, and 表3-2 calls A01–A08 synthetic non-official codes; (vi) 表10-2 S-01–S-15 are fully populated. Remaining internal-consistency slips: §1.5 (p.3) points readers to '第 8.4 節', but §8 has only 8.1–8.3 (likely §8.3); and §12.1 E/§10.2 say 'A4 直向' while the technical receipt records 12 landscape pages (10, 18–28) for wide tables. Neither affects a number or evidence claim."
    },
    "I": {
      "status": "PASS",
      "locators": [
        "p.1–3 封面、使用範圍、閱讀路徑",
        "p.4–12 表格與算式",
        "p.18–28 HOLD／REJECT、替換登錄與定位表",
        "p.30–32 最終檢核與聲明"
      ],
      "finding": "Phrasing is readable Traditional Chinese and tables/instructions are self-contained: units, denominators, totals, means, differences and HOLD/REJECT actions are defined where used, and the 80-row locator table can be followed row by row. The only usability drags are the dangling §8.4 pointer and the very dense landscape register/locator pages (p.20–28); no dependence on this review packet is required."
    }
  },
  "arithmetic": {
    "status": "PASS",
    "checks": [
      {
        "check": "Cell count, range and 0100 source match",
        "recomputed": "8 pairs × 5 dimensions × 2 phases = 80 integer cells; all values are 1–4 (within 0–4); cell-for-cell equal to the supplied paired 0100 table; 80 unique locator rows.",
        "result": "PASS"
      },
      {
        "check": "Row sums, pre",
        "recomputed": "A01–A08: 8, 10, 11, 9, 12, 7, 10, 8 = 75.",
        "result": "PASS"
      },
      {
        "check": "Row sums, post",
        "recomputed": "A01–A08: 15, 16, 14, 13, 18, 12, 15, 14 = 117.",
        "result": "PASS"
      },
      {
        "check": "Row differences",
        "recomputed": "+7, +6, +3, +4, +6, +5, +5, +6 = +42; all positive as stated.",
        "result": "PASS"
      },
      {
        "check": "Dimension pre sums",
        "recomputed": "A 17, B 16, C 13, D 14, E 15 = 75.",
        "result": "PASS"
      },
      {
        "check": "Dimension post sums",
        "recomputed": "A 25, B 24, C 22, D 24, E 22 = 117.",
        "result": "PASS"
      },
      {
        "check": "Dimension means and deltas",
        "recomputed": "A 2.125→3.125 (+1.000); B 2.000→3.000 (+1.000); C 1.625→2.750 (+1.125); D 1.750→3.000 (+1.250); E 1.875→2.750 (+0.875); delta sum 5.250.",
        "result": "PASS"
      },
      {
        "check": "Overall means",
        "recomputed": "75 ÷ 8 = 9.375/20; 117 ÷ 8 = 14.625/20; difference 5.25/20 = 42 ÷ 8.",
        "result": "PASS"
      },
      {
        "check": "Normalization and denominators",
        "recomputed": "75 ÷ 160 = 46.875%; 117 ÷ 160 = 73.125%; 73.125 − 46.875 = 26.25 percentage points; 160 = 8 × 20.",
        "result": "PASS"
      },
      {
        "check": "Range and ranking statements",
        "recomputed": "Max dimension delta +1.250 (D), min +0.875 (E); post mean A highest 3.125; pre mean C lowest 1.625; post C/E 2.750 below 3.000 — all as stated.",
        "result": "PASS"
      },
      {
        "check": "Chart/text/table duplicate consistency",
        "recomputed": "§7.2 series, 圖1 alt text, 表7-1, 表10-4/10-5 equal 表6-1/6-2 and 表2-2 on a fixed 0–4 axis with n=8 and two SAMPLE series; no contradictory plotted summary.",
        "result": "PASS"
      },
      {
        "check": "Locator and derived-map counts",
        "recomputed": "§10.5 exactly 80 unique T5-1/A01–A08/前後A–E rows, including A05/前E=2 on p.24; 表10-3 has 8 × 3 = 24 values; 表10-4 has 5 × 5 = 25 values; 表10-5 values are consistent.",
        "result": "PASS"
      },
      {
        "check": "No imported 0099 threshold",
        "recomputed": "No 14/20 pass line, pass rate, rubric application or skill-threshold import in any 0101 table, figure or calculation; 14/20 appears only in exclusion/boundary statements.",
        "result": "PASS"
      }
    ]
  },
  "blocking_defects": [],
  "nonblocking_notes": [
    "p.3 §1.5 points readers to '第 8.4 節', but §8 has only 8.1–8.3; the intended target appears to be §8.3 (self-assessment/implementation boundary). Fix the section number.",
    "§12.1 E and the §10.2 checklist say 'A4 直向', while the technical receipt records 12 landscape pages (10, 18–28) for wide tables. Align the checklist wording with the actual wide-table layout; visual layout itself is outside this semantic review.",
    "The exact 0100 SHA debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2 is not printed anywhere in final8. If in-artifact byte binding is required, add it to a controlled annex; if final8 deliberately keeps hashes out of the human-facing body, record that decision.",
    "The future-dated 2026-11-02 sample date is now expressly disclaimed on p.1 and p.7; a non-date placeholder would still read more safely.",
    "表3-2 still says A01–A08 are 'not official four-digit codes'; §10.2 no longer imposes four-digit codes, so this is residual wording rather than a rule conflict.",
    "表11-1 names 0099's own 14/20 only inside its boundary/bypass column; this is consistent with §3.3/§7.4/§8.3, but it must never migrate into 0101 figures or the radar.",
    "The external 95-row replacement register mentioned in the technical receipt was not supplied for semantic review; only the in-document 表10-2 (S-01–S-15) was assessed."
  ],
  "review_scope_limitations": [
    "This was a read-only, no-tool review; the DOCX and PDF SHA-256 values are taken as supplied and were not independently recomputed.",
    "Review is bound to the supplied DOCX-table extract and page-labeled Word-native PDF text; the actual DOCX/PDF bytes were not opened.",
    "Radar-chart pixels, axis-label legibility, legend placement, fonts, orientation and pagination were not independently inspected; visual QA is a separate gate. The technical receipt's landscape-page record is used only as scope/consistency evidence.",
    "The paired 0100 content was checked against the supplied 0100 table (it matches all 80 cells), not by opening the 0100 DOCX; the in-body exact SHA is absent.",
    "The 0097/0098/0099 source documents were not supplied; neighbour boundaries were assessed from 0101's own text and the packet.",
    "The official printed checkbox serial remains UNKNOWN; no external verification was performed."
  ],
  "formal_acceptance": "NOT_GRANTED"
}
```

The exact final8 SHA is bound above. Direct inspection confirms §10.5 has exactly 80 unique locator rows, including `T5-1/A05/前E = 2` on p.24, so the prior 79-row finding was an extraction artifact, and all prior locator, typo, date, privacy-wording and register-field findings are resolved. All 80 cells, row and dimension totals/deltas, means, percentages and chart/table duplicates recompute cleanly and match the supplied paired 0100 table. No blocking defect remains; overall is PARTIAL only for the H-level editorial consistency slips (§1.5's nonexistent §8.4 and the "A4 直向" checklist wording versus 12 landscape table pages). Chart pixels were not independently inspected, and formal acceptance remains NOT_GRANTED.

## Final9 wording-only correction receipt
{
  "receipt_id": "TTQS-I18E08-DOC0101-R09-SEMANTIC-MINOR-CORRECTION-FINAL8-TO-FINAL9-20261021",
  "doc_id": "0101",
  "requirement_id": "I18-E08",
  "previous_candidate_sha256": "92edebeff1703104c30486e18cf568f6666310a20ae8a945ab9d03789ec21fdb",
  "previous_candidate_backup": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09_0101\\history\\0101_I18-E08_R09_final8_92edebeff1703104c30486e18cf568f6666310a20ae8a945ab9d03789ec21fdb.docx",
  "previous_backup_sha256": "92edebeff1703104c30486e18cf568f6666310a20ae8a945ab9d03789ec21fdb",
  "current_candidate_sha256": "56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68",
  "change_count": 4,
  "changes": [
    {
      "field": "§1.5 cross-reference",
      "old": "第 8.4 節",
      "new": "第 8.3 節"
    },
    {
      "field": "§10.2 visual checklist",
      "old": "A4 直向",
      "new": "A4 混合頁面方向（正文直向、寬表橫向）"
    },
    {
      "field": "§12.1 E final checklist",
      "old": "A4 直向",
      "new": "A4 混合頁面方向（正文直向、寬表橫向）"
    },
    {
      "field": "Table 3-2 pairing-code boundary",
      "old": "合成識別碼；不是正式四位數字代碼",
      "new": "合成識別碼；正式使用應採可安全配對的去識別代碼"
    }
  ],
  "numeric_fixture_changed": false,
  "change_scope": "Four deterministic wording-only corrections. No scores, tables of numeric results, formulas, dates, SAMPLE data, source bindings, or candidate state changed.",
  "verified_after_save": true,
  "formal_acceptance": "NOT_GRANTED",
  "changed_at_local": "2026-10-21T21:49:33.074736+08:00"
}

## Paired 0100 raw score table from exact downloaded bytes
| 代碼 | 前A | 前B | 前C | 前D | 前E | 前總分 | 後A | 後B | 後C | 後D | 後E | 後總分 | 變化 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 2 | 2 | 1 | 2 | 1 | 8 | 3 | 3 | 3 | 3 | 3 | 15 | +7 |
| A02 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 4 | 16 | +6 |
| A03 | 3 | 2 | 2 | 2 | 2 | 11 | 3 | 3 | 3 | 3 | 2 | 14 | +3 |
| A04 | 2 | 2 | 1 | 2 | 2 | 9 | 3 | 3 | 2 | 3 | 2 | 13 | +4 |
| A05 | 3 | 3 | 2 | 2 | 2 | 12 | 4 | 4 | 3 | 3 | 4 | 18 | +6 |
| A06 | 1 | 2 | 1 | 1 | 2 | 7 | 3 | 2 | 2 | 3 | 2 | 12 | +5 |
| A07 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 3 | 15 | +5 |
| A08 | 2 | 1 | 2 | 1 | 2 | 8 | 3 | 3 | 3 | 3 | 2 | 14 | +6 |

## Full official source packet
# I18-E08 來源包 R09｜0100 自評表 + 0101 雷達分析報告

## 權威綁定（依目前 GitHub PR #92 live head）

- Repository/PR/branch: `PT-Original-Point/ttqs-one` / `#92` / `work/ttqs-one-document-quality-contract-20261016`
- Source commit observed: `ea43984228f70b99b7003f8cb70fdad67f3e20ba`
- GOAL contract `04_CODEX_GOAL_24X7_EXECUTION.md`, blob `4ee893218791ec9460e824fc559933c276414738`.
- 120-minute wake contract `05_HOURLY_NATIVE_WAKE_RESUME.md`, blob `35d3081c7e7fb979466c3a58a1e77b42f0d1441a`; its ACTIVE 2026-10-21 override supersedes old 60-minute terms.
- Worker/acceptance contract `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md`, blob `4c7eff55748ff265b1e5a7d1122852b0d101acbd`; relevant §5.2–5.4 and §6.6–6.8.
- Official TTQS training-institution evidence PDF, p.7, indicator 18; Windows source SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709` (9 pages). Requirement: learner pre/post self-assessment and radar analysis that presents perceived change.
- 157-item writing contract `03_157_CHECKBOX_BLUEPRINTS.md`, blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; project internal index 109 for I18-E08. This is not the official printed checkbox serial; that serial remains `UNKNOWN` unless read from the original form.
- 129-to-142 crosswalk blob `1ac4a8419088d947947031b758e29c35a3606514`: `I18-E08 -> 0100 | 0101`, names: learner pre/post self-assessment form; perceived-growth radar analysis report.

## Current Human override and scope

The live 04/05 documents direct the I18-E08 worked example to use an 8-person × 5-dimension × 2-phase synthetic fixture (80 original score cells), with pre sum 75, post sum 117, net +42, mean net +5.25. The prior local R08 source packet/blueprints and 0101 R08A candidate were based on 1 person × 6 dimensions. Those artifacts are preserved as historical, but are stale against the live 04/05 override and must not be treated as current acceptance evidence. Do not reuse R08A/R08B/R08C body as a template.

The common numeric fixture below is intentionally reused from 0099 R17 solely as an explicit, synthetic cross-document demonstration fixture, as permitted by live 04/05. It does not establish that 0099 rubric scores and I18-E08 self-reports are the same measurement, do not show agreement/correlation, and are not independent empirical evidence. In I18-E08 these values are only synthetic learner self-ratings. State this limitation plainly in both documents. Do not import the 0099 skill-rubric pass threshold or conclusions into the self-rating report.

## Shared synthetic fixture (authoritative within this sample package)

All A01–A08 codes and values are synthetic. Dimensions A–E are: A source facts/context; B record completeness/traceability; C task-to-output application; D data minimization/privacy awareness; E follow-up planning. Self-rating anchors are 0–4 and belong to this illustrative form only; no association-approved scale is asserted.

|Code|Pre A/B/C/D/E|Pre total|Post A/B/C/D/E|Post total|Change|
|---|---|---:|---|---:|---:|
|A01|2/2/1/2/1|8|3/3/3/3/3|15|+7|
|A02|2/2/2/2/2|10|3/3/3/3/4|16|+6|
|A03|3/2/2/2/2|11|3/3/3/3/2|14|+3|
|A04|2/2/1/2/2|9|3/3/2/3/2|13|+4|
|A05|3/3/2/2/2|12|4/4/3/3/4|18|+6|
|A06|1/2/1/1/2|7|3/2/2/3/2|12|+5|
|A07|2/2/2/2/2|10|3/3/3/3/3|15|+5|
|A08|2/1/2/1/2|8|3/3/3/3/2|14|+6|

Formula checks: 80 values; all 0–4; pre total 75; post total 117; total change 42; n=8; mean total 9.375 -> 14.625; mean change 5.25/20. Per dimension A pre17/post25 (2.125 -> 3.125; +1.000), B 16/24 (2.000 -> 3.000; +1.000), C 13/22 (1.625 -> 2.750; +1.125), D 14/24 (1.750 -> 3.000; +1.250), E 15/22 (1.875 -> 2.750; +0.875). The total score range is 0–20. All values are SAMPLE/SYNTHETIC, not training results.

## Companion artifacts and state

- 0099 R17 source sample DOCX SHA-256: `293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b`; its own requirement is I18-E07. Do not modify or formally reclassify it.
- Existing 0100 R08 candidate SHA-256 `f7f3addfed3bfe46aba1a3f282e22b7f92d36de8a1b1c8252e4a77bad1e270d1` is 1-person/6-dimension and is not the live 8×5 sample; preserve as historical.
- 0101 R08A `0f9e0713a8d98c0c28b2b33234c8a4bbd4548c21d17be209f1696965984932a1`, R08B `320e12bcd5c749ffcfd80f59853e9b784321fda6bb1f0eb7fe39fd1ca62a8a0e`, and R08C `7b779684bab9d050c4e160daefe62a15348a906cdb594a65fed496812b3980f6` are historical revisions of the stale 1×6 draft. R08B/R08C corrected font and pagination only; they are not current acceptance candidates.
- 0100 R09 and 0101 R09 are new candidate work and must each receive their own source mapping, Blueprint, SAMPLE replacement register, deterministic QA, Word visual review, and independent exact-SHA semantic review. No REAL input/original or formal acceptance is present.

## Current READY derivation

`READY_SOURCE_PACKET=VERIFIED` (this versioned packet now binds current contracts/source and fixture); `READY_BLUEPRINT=READY` for both 0100 and 0101 (separate files below); `READY_WRITER=0100` because no matching live writer was found and its output is a usable filled self-assessment instrument, not a blank title shell. 0101 becomes `READY_WRITER` only after a stable 0100 R09 candidate and its exact SHA exist.


## Full unique Blueprint 0101
# Unique Blueprint 0101 R09｜學員自我評量統計與能力雷達圖分析報告

## Authority and document type
- Requirement: I18-E08; project internal index 109; official checkbox printed serial UNKNOWN.
- Official source: TTQS training-institution evidence PDF p.7 requests learner pre/post self-assessment and radar analysis presenting perceived change.
- Crosswalk: companion 0100 is the fillable and completed self-assessment instrument; 0101 aggregates, checks, calculates, charts and interprets those responses. This is a perceived-growth statistical report, not an objective skill assessment, satisfaction report or 0099 skills evidence.
- Current Human override: use the eight-pair, five-dimension, 80-cell synthetic fixture in the R09 source packet; do not carry forward the stale one-pair/six-dimension R08 draft. Preserve 0099 R17 itself.

## Distinctive content required
1. Front-page report identity, who can use it, decision limits, exact SAMPLE/SYNTHETIC notice and companion form.
2. Data lineage: 0100 R09 exact source SHA to be inserted only after stable; matching pair codes, same version and exact phase dates; identify the shared synthetic fixture as a demonstration-only reuse permitted by current contract. Explicitly state this is not empirical agreement with 0099 and no real respondent or course exists.
3. Inclusion/exclusion table and denominator rules: complete same-code pair, same questionnaire version, score range 0–4; missing/duplicate/mismatched data held and excluded without imputation.
4. Individual table with all A01–A08 pre/post five-dimension values, sums and difference; values copied from source packet.
5. Five-dimension summary table with pre/post sum, n=8 mean, difference and interpretation; exact fixed values from packet.
6. Five-axis radar chart using dimension means, fixed 0–4 scale, pre and post series, readable Traditional Chinese labels, legend, n=8 and SAMPLE; retain table values beside it.
7. Descriptive calculations: total sums 75 and 117, means 9.375/20 and 14.625/20, mean difference +5.25/20, optional normalized percentages 46.875% and 73.125% (+26.25 points) with denominator shown. No use of the 0099 skill-rubric 14/20 or B/D pass threshold; no pass rate from a self-rating scale.
8. Per-dimension interpretation: A +1.000, B +1.000, C +1.125, D +1.250, E +0.875. Present as synthetic self-report differences only. The repeated numeric fixture does not prove agreement/correlation or objective competence.
9. Cautious conclusions and practical next steps (e.g. validate form comprehension, pair matching and follow-up objective practice only with real authorized evidence). No claim of causal effect, significance, association performance or validated scale.
10. Exact hold/reject rules, SAMPLE-to-REAL replacement checklist and a locator-level replacement register for every synthetic datum and derived statistic.
11. Blind-title boundary table contrasting 0097 I18-E05 perception survey, 0098 I18-E06 satisfaction, 0099 I18-E07 skill work/rubric, 0100 I18-E08 form, and this 0101 I18-E08 aggregate self-rating report.

## Exact fixture and calculations
Use only the R09 source packet's A01–A08, 5 dimensions, pre/post values. 80 original score cells. Pre total=75; post total=117; change=42; n=8; pre mean total=9.375/20; post mean=14.625/20; mean change=5.25/20. Dimension sums/means/deltas: A 17/8=2.125 to 25/8=3.125 (+1.000); B 16/8=2.000 to 24/8=3.000 (+1.000); C 13/8=1.625 to 22/8=2.750 (+1.125); D 14/8=1.750 to 24/8=3.000 (+1.250); E 15/8=1.875 to 22/8=2.750 (+0.875). Recompute independently. Round only display values; never change source cells.

## Layout / accessibility
A4 portrait, clear page hierarchy, body >=10.5 pt and table text >=9.5 pt, reasonable row heights, repeated headers if tables split. No blank page, tiny table text, split figure legend, English-only axes, clipping or lonely paragraph. Word-render every final page and inspect at readable zoom.

## Reject / hold if
- 0101 is based on 1×6 or otherwise differs from the current 8×5 live override.
- It uses 0099 objective skill pass thresholds, describes synthetic self-ratings as actual participant results, or equates self-report with skill performance.
- Scores/totals/denominators/plot labels disagree, a blank/missing value is silently replaced, or the radar omits the 0–4 axis/legend/n.
- It lacks the source-bound 0100 relationship, concrete interpretation, limits, actionable next steps, or replacement/rejection procedure.
- The document uses an unauthorized official decision, real-person record, signature, approval or institutional result.


## Current exact DOCX extracted paragraphs and every table
0101 學員自我評量統計與能力雷達圖分析報告

Learner Self-Assessment Statistics and Perceived-Growth Radar Analysis Report

R09 候選 DOCX｜DOC_ID 0101｜需求 I18-E08｜2026-10-21

SAMPLE／SYNTHETIC 邊界警告（先讀）  本報告中的 A01–A08、課程、機構、代碼、日期、80 個分數格及所有衍生統計，全部是 SAMPLE／SYNTHETIC 合成示範資料。它們不代表任何真實學員、真實課程、真實訓練辦理、真實參與、真實簽署、真實核准、協會核定、認證或訓練成效。  本稿是候選 DOCX，不是正式驗收版本；配套的 0100 R09 亦為候選文件，尚未正式接受。除明確標示的來源與版本資訊外，本報告不得作為對外績效、招生、補助、認證、及格或能力證明。  示範日期 2026-11-02 為合成占位日期；即使晚於本稿日期，也不代表已排定、預定或已辦理任何課程或施測。

1. 封面與文件識別

1.1 報告目的

本報告的目的，是把 0100 R09 配套表單中的 8 對合成前後測自評資料，整理成可追溯的描述性統計、五維度摘要與雷達圖資料，並明確揭露分母、排除規則、圖表尺度與使用限制。

本報告要回答的問題只有四項：

這 8 對合成資料的 80 個原始分數是否完整、是否落在 0–4 範圍？

前測與後測的總分、平均、五維度合計與差異分別是多少？

以固定 0–4 尺度呈現時，五軸雷達圖的資料與圖說應該如何標示？

若未來要換成真實資料，必須替換哪些欄位、重算哪些數值、在什麼條件下 HOLD 或 REJECT？

本報告不回答「訓練是否有效」、「學員能力是否提升」、「學員是否達標」、「課程是否優於其他課程」或「本量表是否具有信效度」等問題。

1.2 文件識別與版本

版本註記：配套問卷內頁標示 R09a；本報告引用問卷版本 SR-0100-v1.0-SAMPLE。正式填答前應確認前測與後測使用同一問卷版本；如換版，分開分析並記錄版本。

1.3 誰可以使用、可以做什麼

本稿可以由內部讀者用來檢查「表格是否完整、數值是否算對、圖表是否標示清楚、替換登錄是否可執行」。任何真實決策，都必須等到真實資料替換、重算、獨立審查與機構授權完成後，才可能進行。

1.4 準備、審查與核准欄位

上述欄位刻意留空。未實際完成的人員、日期、簽署或核准，不得以職稱、角色、系統名稱或推定方式補寫。

1.5 閱讀路徑

決策者宜先讀第 2 節與第 8.3 節，掌握結果與不可推論的界線；資料處理者宜讀第 4 節、第 10 節與附錄式定位表；文件審查者宜讀第 11 節與第 12 節。第 5 節及第 10.5 節保留所有原始分數的可核對位置。

2. 執行結果與界線結論

2.1 主要結果

本報告依 0100 R09 的 8 對合成示例重算。所有原始值保持 0–4 整數；下列平均與百分比僅為顯示用衍生值。

表 2-1｜SAMPLE／SYNTHETIC：主要統計結果（n=8）

八對的總分變化均為正，但這只是此組合成分數的算術事實，不代表每位學員在每個維度都上升，也不代表真實訓練會產生相同結果。

2.2 五維度結果摘要

表 2-2｜SAMPLE／SYNTHETIC：五維度前後平均與差異（n=8）

五個維度的後測平均都高於前測平均。數值差異最大的是 D（+1.250），最小的是 E（+0.875）；A 與 B 同為 +1.000，C 為 +1.125。這些排序只是這組合成資料的算術結果，不是效果大小、能力排名或訓練優先順序的證明。

2.3 界線結論

可報告的結論  在這組 8 對 SAMPLE 資料的算術範圍內，後測總分為 117、前測總分為 75，淨差為 +42；平均總分由 9.375／20 變為 14.625／20，平均每人差為 +5.25／20。五維度後測平均均高於前測平均。  不可報告的結論  不得寫成「訓練有效」、「能力已提升」、「學員已達標」、「課程造成改變」、「與 0099 技能評分一致」、「具統計顯著性」、「可推廣到母體」或「可作為協會認證成果」。本稿沒有真實資料、沒有對照組、沒有推論設計，且 0–4 分數是自評而非客觀技能測量。

3. 資料血緣、範圍與版本

3.1 分析鏈

本報告只聚合 0100 R09 已完成之合成示例，不重製 0100 的空白表單，也不把 0100 的個別填答頁當成彙總報告。

官方證據需求：I18-E08；PDF p.7、indicator 18
                    │
                    ▼
0100 R09 候選表單與完成示例
8 對 × 5 維度 × 2 階段 = 80 個原始分數格
                    │
                    │ 配對、版本、範圍、日期、隱私與分母檢核
                    ▼
0101 R09 本報告
描述統計、五維度摘要、固定 0–4 雷達圖資料與替換登錄

129-to-142 對照將 I18-E08 指向 0100 | 0101：0100 是學員前後自我評量表，0101 是自覺成長雷達分析報告。兩者是同一需求下的不同產物層級，不可互相代替。

3.2 來源綁定

表 3-1｜來源與版本綁定（非 SAMPLE 數值）

本示範使用 SR-0100-v1.0-SAMPLE。正式分析時，前測與後測須使用相同問卷版本；若題目或評分錨點不同，應分版整理，不得直接合併配對。

3.3 與 0099 R17 的合成重用邊界

本報告 A01–A08 的 80 格數值，是依現行契約自 0099 R17 共用同一組合成數值，僅作為跨文件格式、欄位對應與算術一致性的 SAMPLE／SYNTHETIC demonstration fixture。必須明確區分以下五點：

1. 不是同一種測量。 0099 是技能工作／評分規準文件，數值在該文件中的角色是技能評分示範；在本報告中則只是學員自評值。兩者的構念、評分者、單位與用途不同。

2. 不是一致性或相關證據。 即使兩份文件使用同一組數字，也不能說自評與技能評分「一致」、「相關」、「互相驗證」或「可互換」。

3. 不是獨立實證資料。 共用 fixture 是示範重用，不是第二次獨立觀察，不能增加樣本或提供額外證據。

4. 不得引入 0099 的技能門檻。 0099 的 14/20 或任何技能通過標準，均不得套用到本報告；本報告不設及格線、不計算通過率、不呈現技能達標人數。

5. 不是真實機構或課程結果。 本報告沒有真實學員、真實課程、真實訓練辦理、真實協會核定或真實成效。所有 SAMPLE 欄位都必須在真實使用前替換。

0099 R17 本身不被本報告修改、重新分類或重新認證。其原需求 I18-E07 與文件定位保持不變。

3.4 分析範圍與樣本基本資料

表 3-2｜SAMPLE／SYNTHETIC：樣本與課程基本資料

表 3-2 的日期是 0100 的 SAMPLE fixture，不代表課程已辦理或學員已出席。稿件日期 2026-10-21 也不是施測日期；不得以時間順序推定真實事件。

3.5 分析單位、分母與版本控制

本報告的分析單位是「一對同配對代碼的前測與後測」，不是單一問卷、單一題目或單一分數格。有效分母為完成配對且通過檢核的對數；本合成 fixture 的 n=8。

原始分數格分母：80 格（8 × 5 × 2），只用於完整性與範圍檢查。

維度平均分母：每個維度每階段 8 個值。

總分平均分母：8 對。

正規化群體分母：160（8 × 20），僅為顯示用。

不得以 80 格當成人數分母，也不得把格數混稱為樣本數。

不得加權、不得用部分平均替代缺漏、不得變更分母而不揭露。

版本控制上，現行契約是 8 人 × 5 維度 × 2 階段。先前 1 人 × 6 維度的 R08 系列（包含 0100 R08 與 0101 R08A／R08B／R08C）均為歷史稿，與現行 8×5 fixture 不一致，不得作為本稿模板、現行接受依據或數值來源。R09 與 R08 系列不得混用。

4. 納入、排除與處理紀錄

4.1 納入條件

一對資料必須同時符合下列條件，才可進入本報告的有效分母：

1. 前測與後測具有相同的配對代碼；本合成示例為 A01–A08，正式使用時則為學員自選且可安全配對的代碼或去識別分析編號。

2. 前測與後測使用完全相同的問卷版本；本示例為 SR-0100-v1.0-SAMPLE。

3. 同一課程代碼或同一辦理場次；不得把不同課程、不同版本或不同場次的資料混配。

4. 每一階段五個維度 A–E 均有值，且每個值都是 0–4 的整數。

5. 後測日期不得早於前測日期。

6. 同一階段不得有未解決的重複配對代碼。

7. 表單不得含姓名、電話、證件號、電子郵件或其他可直接或間接識別個人的欄位。

8. 有效份數、排除份數、留置份數與原因必須可追溯，且分母必須揭露。

4.2 HOLD／REJECT 規則

表 4-1｜缺漏、重複、錯配與版本問題的處理

任何缺漏都不得補值。HOLD 是可補正狀態；REJECT 是排除狀態。兩者都必須留下原因、處理人與日期紀錄，且不得把排除份數隱藏在意見或註腳之外。

4.3 本次合成 fixture 的處理結果

表 4-2｜SAMPLE／SYNTHETIC：本 fixture 的納入與排除計數

本報告所稱「已核對」僅指合成示範資料已完成結構、範圍、配對與算術核對；不是獨立實證驗證、不是正式驗收，也不是對真實表單品質的聲明。

4.4 處理日誌

表 4-3｜SAMPLE／SYNTHETIC：處理與核對日誌

本段記錄撰寫階段的結構與算術核對，並非獨立審查；正式使用前仍須由不同審查者檢查候選版本的內容、計算與 Word 呈現。

5. 全體填答者資料

表 5-1｜SAMPLE／SYNTHETIC：A01–A08 前後測五維度原始值、總分與變化（n=8）

計算定義：

前總分 = 前 A + 前 B + 前 C + 前 D + 前 E。

後總分 = 後 A + 後 B + 後 C + 後 D + 後 E。

變化 = 後總分 − 前總分。

A–E 的十個欄位是 80 個原始分數格；前總分、後總分與變化是計算值，不計入 80 格。

A01–A08 是合成識別碼，不是正式施測代碼，也不得直接轉用為真實學員的公開代碼。

逐列合計覆核（詳值見表 5-1）：A01 8→15（+7）；A02 10→16（+6）；A03 11→14（+3）；A04 9→13（+4）；A05 12→18（+6）；A06 7→12（+5）；A07 10→15（+5）；A08 8→14（+6）。各維度與全體三種算法的交叉驗算見第 6.3 節。

6. 五維度統計與整體核算

6.1 維度統計

表 6-1｜SAMPLE／SYNTHETIC：五維度合計、平均與差異（每維 n=8）

維度平均的單位是該維度的 0–4 分，不是 0–20 總分。最後一列的「整體總分／平均」是 8 人總分的合計與平均，不與前五列的維度平均相加混淆。

6.2 整體總分與正規化顯示

表 6-2｜SAMPLE／SYNTHETIC：整體總分、平均與正規化

正規化只是把總分線性換算成百分比，方便閱讀：

9.375 ÷ 20 = 46.875%；14.625 ÷ 20 = 73.125%。

群體層級：75 ÷ 160 = 46.875%；117 ÷ 160 = 73.125%。

差值為 26.25 個百分點，不是「進步 26.25%」，也不是效果量、通過率或常模分數。

6.3 交叉驗算

維度層級：

前測：17 + 16 + 13 + 14 + 15 = 75。

後測：25 + 24 + 22 + 24 + 22 = 117。

差異：117 − 75 = 42。

配對層級：

前測：8 + 10 + 11 + 9 + 12 + 7 + 10 + 8 = 75。

後測：15 + 16 + 14 + 13 + 18 + 12 + 15 + 14 = 117。

變化：+7 + 6 + 3 + 4 + 6 + 5 + 5 + 6 = 42。

平均層級：

平均每人變化：42 ÷ 8 = 5.25。

維度平均差合計：+1.000 + 1.000 + 1.125 + 1.250 + 0.875 = +5.250。

前後平均總分差：14.625 − 9.375 = 5.25。

三種算法結果一致：前 75、後 117、差 +42、平均差 +5.25。

6.4 顯示精度與平均方法

所有原始值均維持整數，不因顯示而改變。維度平均以「維度合計 ÷ 8」計算，顯示至三位小數；整體平均以「總分 ÷ 8」計算。1.000、3.000 等尾零是顯示精度，不代表比原始整數多出有效位數。

本報告對 0–4 整數採算術平均，只是描述性彙總約定，不主張此量表是等距量表，也不主張具有常模、信度、效度或可加權的潛在能力分數。合計與平均不得被解讀為客觀能力總量。

7. 雷達圖資料規格與替代表格

7.1 圖表資料

表 7-1｜SAMPLE／SYNTHETIC：五軸雷達圖資料（n=8；固定 0–4）

此表就是雷達圖的數值來源。圖形只畫五個維度的前後平均，不畫 80 個個別分數格，也不把維度合計直接畫在同一軸上。

7.2 原生 Word 圖表規格

7.3 圖說與可及性替代文字

圖 1｜SAMPLE／SYNTHETIC：學員五維度訓練前後自評平均雷達圖（n=8；0–4 分；描述性）

圖例：前測自評平均（SAMPLE）；後測自評平均（SAMPLE）。

替代文字：

五軸雷達圖，n=8，固定 0–4 分。前測平均依 A 至 E 為 2.125、2.000、1.625、1.750、1.875；後測平均為 3.125、3.000、2.750、3.000、2.750；差異為 +1.000、+1.000、+1.125、+1.250、+0.875。圖形只呈現合成自評平均，不呈現個別學員、客觀技能或統計顯著性。

可及性表格替代：表 7-1 已列出每個軸的前測、後測與差異；即使圖形未顯示或讀者無法辨識顏色，仍可從表格取得完整數值。

7.4 圖形解讀邊界

五軸的徑向尺度固定為 0–4；不可因資料範圍縮放而改變軸的意義。

雷達圖多邊形面積不是效果量、不是能力總分、不是進步幅度，也不是統計檢定結果。

五個軸是不同構念，沒有共同單位與權重；軸的排列順序會改變多邊形形狀與面積，因此面積不可比較。

前後系列的平均差只能用來看這組合成資料的數值位置；不能說「面積變大代表能力提升」。

圖形不得省略 n=8、SAMPLE 標記、圖例或 0–4 刻度。

不得把 0099 的技能門檻畫成同一張圖的參考線，也不得把 14/20 轉成此圖的通過區。

8. 維度解讀與自評邊界

8.1 逐維度數值解讀

表 8-1｜SAMPLE／SYNTHETIC：五維度算術觀察

所有數值都是 0–4 自評分的群體平均。平均 3.125 不代表每位學員都是 3 或 4；平均差 +1.250 也不代表每個人都增加 1.250。

8.2 最大與最小變化

在五個維度中，D 的算術平均差最大（+1.250），E 的算術平均差最小（+0.875）。A 與 B 同為 +1.000，C 為 +1.125。這個排序只描述本合成 fixture 的數字：

不是統計顯著性排序。

不是效果量或實務重要性排序。

不是因果推論，不能說訓練造成 D 的變化最大。

不是能力優劣排序，不能說 D 比其他維度「更重要」或「更成功」。

不代表真實學員、真實課程或母體會出現相同模式。

n=8、無對照組、無隨機分派、無抽樣架構、無信效度資料，且數值為合成自評值，因此本報告不做檢定、不計算信賴區間、不宣稱顯著或因果。

8.3 自評與實作能力的區隔

本報告所稱的「自評」是學員依 0–4 錨點，對自己在某一時刻「主觀上能做到多少」的判斷。它不等於：

受過訓練的評分者對實際作品或任務表現的評分。

客觀測驗、技能檢定、工作樣本或通關門檻。

講師觀察、同儕評分或管理者績效考核。

學習遷移、行為改變或組織績效。

即使真實前後測平均上升，也可能受題意理解、作答風格、期待、記憶、社會讚許、重複施測或課程期待影響；本報告沒有設計可排除這些替代解釋。0–4 錨點文字是填答提示，不是已驗證的行為觀察規準。

若未來要討論「實作能力」，必須另以獲授權的客觀任務、明確評分規準、合格評分者與可追溯紀錄進行；該客觀資料不得直接併入本報告的自評分數，也不得借用 0099 的 14/20 或任何技能通過門檻。

9. 建議後續工作流程

以下流程是建議程序，不是已完成的事實。角色名稱是一般性建議，不代表已被指派、已同意或已存在；任何實際決定仍須由適用機構依其程序授權。

9.1 建議角色

9.2 流程、觸發條件與責任

9.3 未來真實資料的比較原則

未來若取得真實且合法的前後配對資料，報告至少應揭露：納入對數、排除對數與原因、每維度分母、前後分布、平均差、缺漏處理與圖表尺度。不得只報總分或只報漂亮的百分比。

若考慮推論統計，必須在分析前指定方法、檢查假設、處理配對結構並報告不確定性；不得因為看到數字上升就事後選擇檢定。以目前 n=8 的合成 fixture，不進行顯著性檢定，也不提供母體推論。

若另行執行客觀實作任務，應使用獨立同意、獨立規準與獨立資料檔；可與自評結果並列討論，但不得把兩者合併成一個未定義的「能力分數」，也不得把 0099 的技能門檻移入本報告。

10. 留置／退件準則、SAMPLE 替換與定位登錄

10.1 精確 HOLD／REJECT 準則

表 10-1｜使用前與分析前的留置／退件判定

核心原則：不補值、不代選、不挑份、不隱藏分母。HOLD 與 REJECT 的份數、原因和處理日期都必須與有效份數一起揭露。

10.2 真實資料替換檢查清單

以下為正式使用前的必要步驟；本候選稿尚未執行，不得預先勾選為完成。

☐ 確認真實資料的使用目的、權限、告知與隱私程序已由適用機構核准。

☐ 凍結實際使用的 0100 問卷版次與版本號；如前測、後測版本不同，分開統計並更新配對與重算紀錄。

☐ 確認分析對象是已完成、已檢核的真實前後測表單，不是空白表、草稿或合成資料。

☐ 登錄收到、納入、排除、HOLD 與 REJECT 的份數及原因，確認有效分母。

☐ 以去識別分析編號取代 A01–A08；不得在報告公開原始配對碼；A01–A08 僅為合成代碼，對照資訊由單一窗口分開保管。

☐ 以真實表單替換全部 80 個原始分數格；任一格缺漏先 HOLD，不以 0、平均或前測值補值。

☐ 核對每對的前後代碼、版本、課程、日期、五題完整性與 0–4 範圍。

☐ 重算每一對的前總分、後總分與變化；不得手動改寫衍生值。

☐ 重算五維度前後合計、平均、差異、整體總分、平均與正規化顯示。

☐ 重新產生表 7-1 與圖 1；確認五軸中文標籤、固定 0–4、圖例、n 與 SAMPLE 標記（若尚未替換）正確。

☐ 更新所有分母、排除說明與限制段落；不得只改表格數字而不改敘述。

☐ 由第二人獨立重算並比對；差異未解釋前不得釋出。

☐ 完成 DOCX 的 Word 視覺檢查：A4 混合頁面方向（正文直向、寬表橫向）、正文至少 10.5 pt、表格至少 9.5 pt、無裁切、無空白頁、表格跨頁有重複表頭、圖說不與圖分離。

☐ 由獨立審查者依本報告所示版次完成語意、算術與 Word 呈現檢查；未完成前維持 HOLD。

☐ 只有在真實替換、重算、審查與機構授權都完成後，才可移除 SAMPLE／SYNTHETIC 標記；限制聲明仍須保留「自評、描述性、非客觀技能」的性質。

☐ 準備、審查、核准欄僅在實際完成時填寫；不得以角色、職稱或推定補簽。

☐ 封存替換登錄、排除清單、重算紀錄及來源版本紀錄；不得將可識別個資留在報告或公開資料夾。

10.3 合成欄位替換登錄

以下右欄是未來替換要求，不是已完成事項。所有 SAMPLE 欄位在真實使用前都必須處理。

表 10-2｜SAMPLE 欄位、位置、替換來源、驗證與 HOLD 動作

10.4 定位代碼與核對代碼

為使每一格可追溯，本報告使用下列定位規則：

T5-1/A01/前A 表示表 5-1 中 A01 的前測 A 維度格；其他原始格依此類推。

T6-1/A/前合計 表示表 6-1 中 A 維度的前測合計。

T7-1/A/前平均 表示表 7-1 中 A 軸的前測平均。

FIG1 表示第 7.3 節的圖 1；其數值只讀取 T7-1，不另存一份數值。

T2-1、T6-2 分別表示第 2 節與第 6.2 節的整體統計表。

核對代碼：

V1：官方來源、問卷版本與本報告使用界線一致。

V2：前後配對代碼、課程／場次一致。

V3：五個維度齊全，分數為 0–4 整數。

V4：階段、日期順序與重複代碼檢查完成。

V5：由原始值重新計算總分、差異、平均與百分比。

V6：已完成去識別，無直接個資。

V7：第二人獨立核對／視覺檢查。

HOLD 代碼：

H1：該對 HOLD，暫不納入。

H2：報告 HOLD，暫不釋出。

H3：該對 REJECT，排除於有效分母。

H4：所有引用該值的表格、圖形與摘要一併 HOLD。

替換來源代碼：

SRC-A01-P：將取代 A01 的真實前測表單（同一版本、同一課程、已完成檢核、去識別處理）。

SRC-A01-Q：將取代 A01 的真實後測表單。

其他配對依此類推。候選稿不列出任何真實代碼或可識別資訊。

10.5 80 個原始分數格的定位

SAMPLE／SYNTHETIC 80 格定位（不是真實資料）

下列每一列皆為一個原始分數格；value 是目前合成值。驗證失敗時，先依 H1／H4 留置該對及引用表圖；若無法補正，轉 H3。

10.6 配對總分與變化的定位

表 10-3｜SAMPLE／SYNTHETIC：8 對總分與變化的定位映射

這 24 個值全部由表 5-1 的原始格重算；驗證代碼 V5，失敗時 H2／H4。不得以人工方式只替換總分而不替換原始格。

10.7 五維度統計的定位

表 10-4｜SAMPLE／SYNTHETIC：維度合計、平均與差異的定位映射

雷達圖的 10 個系列值直接等於上表的前平均與後平均，不另存獨立數值：

FIG1 只讀取 T7-1；若維度值變動，必須同時重繪圖 1、更新圖說與替代文字。所有維度值驗證代碼 V5，失敗時 H2／H4。

10.8 整體統計與正規化的定位

表 10-5｜SAMPLE／SYNTHETIC：整體與正規化值的定位映射

所有整體與正規化值都必須由替換後的原始值重算，不得沿用本稿的合成數字，也不得只改百分比而保留舊總分。

11. 盲標題邊界矩陣

盲標題測試不能只看檔名。至少要用五個線索判定：需求編號、產物類型、分析單位、輸出型態、來源綁定。以下矩陣用來避免把 0097、0098、0099、0100 與 0101 互相替換。

表 11-1｜五份文件的盲標題邊界

盲測時可依下列順序判定：

1. 若看到空白勾選欄、前後測頁、五題與版本欄，先判定為 0100，不是 0101。

2. 若看到 8 對、80 格、75／117／+42、五軸雷達圖與分母揭露，判定為 0101。

3. 若看到評分者、rubric、作品評分或 14/20，判定為 0099；不得把該門檻移入 0101。

4. 若主體是滿意度，判定為 0098；若是知覺或看法調查，判定為 0097。

5. 0100 與 0101 雖同為 I18-E08，但前者是表單與資料蒐集，後者是聚合報告；同一需求不代表可互相代替。

12. 使用前檢核與來源／範圍聲明

12.1 最終使用前檢核表

以下檢核項供正式釋出前逐項核對。候選版次、技術、視覺與獨立語意品質檢查應另行留存；本文件不代替權責人員的核准，未由權責人員依證據核對的項目不得勾選。

A. 識別與來源

☐ 文件標題、DOC_ID 0101、需求 I18-E08、R09 候選版次與稿件日期正確。

☐ 官方印刷序號維持 UNKNOWN；未以其他清單序號代替。

☐ 配套 0100 表單的名稱、內頁版次及問卷版本一致；該表單仍是候選文件，尚未正式接受。

☐ 官方來源用途、配套表單題目與版本、示範資料範圍及相鄰文件用途已分別核對。

候選文件的檢查狀態須依實際查核結果填寫；本表不得預先勾選。

B. 資料與算術

☐ 納入 8 對、80 個原始分數格；全部為 0–4 整數。

☐ 前總分 75、後總分 117、淨變化 +42，且逐列與維度交叉核對一致。

☐ 前平均 9.375／20、後平均 14.625／20、平均變化 +5.25／20。

☐ 五維度：A 17／25、B 16／24、C 13／22、D 14／24、E 15／22；平均差分別為 +1.000、+1.000、+1.125、+1.250、+0.875。

☐ 正規化 46.875%／73.125%／+26.25 個百分點只作為顯示，且有揭露分母。

☐ 未使用 0099 的 14/20、技能門檻或通過率。

☐ 未以 0、平均數、前測值或其他方式補值。

☐ 有效分母、排除份數與 HOLD／REJECT 原因均已揭露。

C. 圖表與可及性

☐ 雷達圖五軸均為完整繁體中文標籤，固定 0–4，刻度 0、1、2、3、4。

☐ 前測與後測兩系列及圖例清楚，並標示 n=8 與 SAMPLE／SYNTHETIC。

☐ 圖 1 具備 n=8、SAMPLE／SYNTHETIC、前後系列圖例、完整圖說與替代文字；圖說不與圖分離。

☐ 五軸標籤完整可讀，未被裁切、縮成英文縮寫或旋轉到難以辨識。

☐ 徑向軸固定 0–4，刻度為 0、1、2、3、4；未因資料範圍而改動尺度。

☐ 表 7-1 可作為無圖環境的完整表格替代；其數值與表 6-1 一致。

☐ 未以多邊形面積、3D 效果或視覺面積暗示效果量、能力總分、統計顯著性或通過率。

D. 邊界與核准

☐ 全篇未把自評寫成客觀技能、訓練因果、學習成效、通過率、母體推論或機構績效。

☐ 未與 0099 做一致性、相關或門檻比較；未使用其 14/20 或任何技能通過標準。

☐ 未出現真實姓名、簽名、虛構核准、協會核定、真實課程辦理或真實學員結果。

☐ 準備／審查／核准欄仍為空白；僅在實際完成並留有紀錄後，依機構程序填寫。

☐ 盲標題邊界已依第 11 節檢查，0100 與 0101 未被互相代替。

E. 檔案與審查

☐ DOCX 採 A4 混合頁面方向（正文直向、寬表橫向）；正文至少 10.5 pt、表格至少 9.5 pt；無空白頁、裁切、重疊或孤立圖說。

☐ 跨頁表格重複表頭；長表格未出現錯誤斷列或失去欄位標題。

☐ 所有頁面經 Word 視覺檢查；圖例、軸標籤、表格與替代文字均清楚可讀。

☐ 由獨立審查者依本稿版次完成語意、算術與 Word 呈現審查。

☐ 所有 SAMPLE 欄位均已替換，或仍保留在合法的示範版本；不得把殘留合成值當成真實結果。

☐ 替換登錄、排除清單、重算紀錄、來源版本及審查紀錄已妥善保存。

12.2 本稿目前狀態

狀態：SAMPLE／SYNTHETIC 候選 DOCX；未正式接受。

本文件已提供完整報告結構、表格、算術核對、圖表資料規格、HOLD／REJECT 規則、SAMPLE 替換登錄與 80 格定位映射。候選版次及品質檢查結果另行記錄；本稿仍待以下真實條件：

真實 0100 完成表單與真實有效分母；

機構授權、正式核准或協會決定。

因此，本稿不得釋出為正式報告，也不得用於課程成效、學員能力、招生、補助、績效或認證宣告。

12.3 來源、範圍與不主張聲明

本文件是 DOC_ID 0101、需求 I18-E08 的 R09 SAMPLE／SYNTHETIC 候選報告，依據 TTQS 訓練機構版證據資料表第 7 頁指標 18 編製，並以配套 0100 學員前後自評表作為同一示範案例的輸入。0100 內頁標示 R09a，問卷版本為 SR-0100-v1.0-SAMPLE；該表單仍為候選，尚未正式接受。

正式使用時，應以表單內頁版次及問卷版本辨識配套文件，確認前測與後測題目及評分錨點一致；本節所有數值仍為 SAMPLE／SYNTHETIC。

此 0100 文件為候選，不是正式接受版本。本報告的 8 對、5 維度、2 階段、80 個原始分數格，全部是 SAMPLE／SYNTHETIC。與 0099 R17 共用數值僅是契約允許的跨文件示範 fixture；不是同一構念、不是獨立實證資料、不是一致性或相關分析，也不代表真實課程、學員、機構或協會結果。

本報告只提供描述性算術與圖表規格：

前測總分 75；

後測總分 117；

淨變化 +42；

前測平均 9.375／20；

後測平均 14.625／20；

平均每人變化 +5.25／20；

五維平均差為 A +1.000、B +1.000、C +1.125、D +1.250、E +0.875。

上述數值只描述這組合成自評資料。本報告不主張統計顯著性、因果效果、效果量、信效度、常模、通過率、能力認證、訓練成效或母體推論。雷達圖面積不具效果量或能力總分意義；0–4 分數不是客觀技能分數。

本報告不含任何真實姓名、參與者紀錄、簽名、核准、協會決定或實際訓練成果。未來若要以真實資料使用，必須完成第 10 節的替換、重算、分母揭露、隱私檢核、獨立審查與機構授權；在此之前，所有 SAMPLE 欄位與限制文字均須保留。

12.4 版本與歷史邊界

報告結束。

[DOCX TABLE 1]
| 欄位 | 內容 |
| --- | --- |
| 文件名稱 | 學員自我評量統計與能力雷達圖分析報告 |
| 英文名稱 | Learner Self-Assessment Statistics and Perceived-Growth Radar Analysis Report |
| DOC_ID | 0101 |
| 需求編號 | I18-E08 |
| 報告識別說明 | DOC_ID 0101、需求 I18-E08；官方印刷序號另以 UNKNOWN 標示。 |
| 官方表單印刷序號 | UNKNOWN（未取得官方原始表單印刷序號） |
| 本稿版次 | R09（候選 DOCX） |
| 稿件日期 | 2026-10-21 |
| 配套表單 | 0100 學員訓練前後自我評量表，R09 候選稿；文件內頁版次標示為 R09a；問卷版本為 SR-0100-v1.0-SAMPLE |
| 配套表單用途 | 0100 用於蒐集學員個別前後自評；本報告負責彙整與描述性分析。 |
| 配套狀態 | 候選文件，尚未正式接受；本報告不宣稱 0100 已完成驗收 |
| 示範資料範圍 | 8 對 A01–A08 合成配對、5 個維度、前後測共 80 格；不代表真實學員或課程。 |
| 分析範圍 | 描述性自評整理；不推論客觀技能、因果效果或機構績效。 |
| 官方來源 | TTQS 訓練機構證據資料表第 7 頁、指標 18；要求學員訓練前後自我評量及自覺改變雷達分析。 |
| 官方要求內容 | 學員訓練前後自我評量，以及呈現自覺改變之雷達分析 |
| 資料性質 | 8 對 A01–A08 的 SAMPLE／SYNTHETIC 自評資料 |
| 樣本規模 | n=8 對；5 個維度；前測／後測 2 階段；共 80 個原始分數格 |
| 量表 | 每維度 0–4 分；單一階段總分 0–20 分；僅為本示範表使用，非協會核定或信效度驗證量表 |
| 示範課程代碼 | SAMPLE-CRS-0100 |
| 示範課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 |
| 示範施測日期 | 前測 SAMPLE 2026-11-02；後測 SAMPLE 2026-11-02（課後同日） |
| 報告狀態 | SAMPLE／SYNTHETIC 候選 DOCX；沒有真實資料或正式核准，不得作為實際成效證明。 |
| 文件狀態 | R09 SAMPLE／SYNTHETIC 候選；尚未正式接受，亦未替代真實資料或正式核准。 |

[DOCX TABLE 2]
| 使用情境 | 是否可用 | 條件與限制 |
| --- | --- | --- |
| 文件作者與內部方法審查者檢查格式、算術、圖表規格 | 可用 | 必須保留全篇 SAMPLE／SYNTHETIC 標記與限制說明 |
| 未來獲授權的課程承辦窗口、資料管理者與分析者做替換演練 | 可用 | 只能使用經檢核的真實 0100 表單，不得把合成值當真實值 |
| 對外呈現課程成效、招生、績效、補助或認證 | 不可用 | 本稿沒有真實資料、對照設計、統計推論或機構核准 |
| 判斷學員能力、及格、通過、聘用或升遷 | 不可用 | 自評分數不是客觀技能評分，也沒有通過門檻 |
| 與 0099 技能評分做一致性、相關或門檻比較 | 不可用 | 兩者構念、單位與用途不同；合成重用不構成實證關係 |
| 學術推論、母體估計、統計顯著性宣稱 | 不可用 | n=8、無抽樣架構、無對照組、無推論設計 |

[DOCX TABLE 3]
| 欄位 | 狀態 |
| --- | --- |
| 準備／撰寫 | 未填寫 |
| 資料檢核 | 未填寫；不表示已完成獨立復核 |
| 獨立審查 | 未填寫；候選稿尚待獨立審查。 |
| 核准／核定 | 未填寫；未核准、未核定 |
| 機構／協會決定 | 無；本稿不主張任何核定、認證、背書或正式驗收 |

[DOCX TABLE 4]
| 指標 | 結果 | 說明 |
| --- | --- | --- |
| 納入分析 | 8 對 | 僅限本合成 fixture |
| 排除 | 0 對 | 僅限本合成 fixture；不代表真實資料品質 |
| 原始分數格 | 80 格 | 8 × 5 維度 × 2 階段 |
| 分數範圍檢查 | 全部 0–4 | 80 格均為整數且在範圍內 |
| 前測總分 | 75 | 8 人前測總分合計 |
| 後測總分 | 117 | 8 人後測總分合計 |
| 淨變化 | +42 | 117 − 75 |
| 前測平均總分 | 9.375／20 | 75 ÷ 8 |
| 後測平均總分 | 14.625／20 | 117 ÷ 8 |
| 平均每人變化 | +5.25／20 | 42 ÷ 8；亦等於 14.625 − 9.375 |
| 正規化顯示 | 46.875% → 73.125% | 9.375 ÷ 20 與 14.625 ÷ 20；群體為 75 ÷ 160、117 ÷ 160 |
| 正規化差異 | +26.25 個百分點 | 僅為線性顯示，不是效果量、門檻或通過率 |
| 五維平均差範圍 | 最小 +0.875；最大 +1.250 | E 最小、D 最大；只有算術描述意義 |

[DOCX TABLE 5]
| 維度 | 前測平均 | 後測平均 | 平均差 |
| --- | --- | --- | --- |
| A 來源事實與情境 | 2.125 | 3.125 | +1.000 |
| B 紀錄完整性與可追溯 | 2.000 | 3.000 | +1.000 |
| C 任務與產出對應 | 1.625 | 2.750 | +1.125 |
| D 資料最小化與隱私意識 | 1.750 | 3.000 | +1.250 |
| E 後續行動規劃 | 1.875 | 2.750 | +0.875 |

[DOCX TABLE 6]
| 資料／文件 | 可查定位 | 用途與限制 |
| --- | --- | --- |
| 官方證據來源 | TTQS 訓練機構版證據資料表，第 7 頁、指標 18 | 要求學員訓練前後自我評量，並呈現自覺改變的雷達分析。 |
| 配套文件 0100 | 學員訓練前後自我評量表 R09a；SR-0100-v1.0-SAMPLE | 個別學員資料蒐集表；候選文件，尚未正式接受。 |
| 0097／I18-E05 | 知覺／看法調查 | 分析對象的知覺或意見；不能代替前後自評配對。 |
| 0098／I18-E06 | 滿意度調查 | 評估課程或服務感受；不能證明學習或技能提升。 |
| 0099／I18-E07 | 技能工作與評分規準 | 評估任務表現；本報告不引用其技能門檻或結果。 |
| 本報告 0101／I18-E08 | 聚合描述性自評報告 | 8 對合成配對的示範分析；不是表單、技能評分或因果證據。 |

[DOCX TABLE 7]
| 欄位 | 目前示範值 | 邊界 |
| --- | --- | --- |
| 辦理單位 | SAMPLE 示範訓練機構 | 非真實機構 |
| 課程代碼 | SAMPLE-CRS-0100 | 非正式課程代碼 |
| 課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 | 非真實課程 |
| 前測日期 | SAMPLE 2026-11-02 | 非真實施測紀錄 |
| 後測日期 | SAMPLE 2026-11-02（課後同日） | 非真實施測紀錄；後測不得早於前測 |
| 問卷版本 | SR-0100-v1.0-SAMPLE | 前後測必須相同 |
| 配對識別 | A01–A08 | 合成識別碼；正式使用應採可安全配對的去識別代碼 |
| 量表 | 每維 0–4；單階段總分 0–20 | 示範用；非協會核定、非信效度驗證 |
| 納入分析 | 8 對 | 僅限本合成 fixture |
| 原始分數格 | 80 格 | 8 × 5 × 2 |

[DOCX TABLE 8]
| 情況 | 判定 | 處理方式 | 分母效果 |
| --- | --- | --- | --- |
| 任一維度缺漏，或同一題多選 | HOLD | 請本人補正或重選；不得以 0、平均數、前測值或其他替代值填入 | 未補正前不納入 |
| 分數不是整數或超出 0–4 | HOLD | 核對原表；不得截斷、四捨五入或代填；無法確認時整對 REJECT | 未解決前不納入 |
| 同階段出現兩份以上相同代碼 | HOLD | 該代碼全部表單先 HOLD；不得挑選較完整或分數較高的一份 | 未確認前全部不納入 |
| 重複代碼經本人確認仍無法安全歸屬 | REJECT | 全部相關表單排除，不得勉強配對 | 排除該等對數並揭露 |
| 前後測代碼不一致 | HOLD | 未經本人當場確認不得配對；確認後更正並留註記 | 未確認前不納入 |
| 前後測版本或課程代碼不一致 | REJECT | 該對不得併入分析 | 排除該對並揭露 |
| 後測日期早於前測 | REJECT | 時序錯誤；查明後重填，不得倒填日期 | 排除該對並揭露 |
| 表單含姓名、電話、證件號等 | HOLD | 立即遮蔽或換碼；未完成去識別前不得分析 | 未完成前不納入 |
| 承辦人代填、代選或代改分數 | REJECT | 該份作廢，記錄程序違失 | 排除並揭露 |
| 問卷版次、前後配對條件或來源資料無法確認 | HOLD | 停止整批分析，重新綁定來源 | 全部暫不納入 |
| 未揭露有效分母或排除份數 | HOLD | 不得產出最終 0101 分析或對外版本 | 報告不得釋出 |

[DOCX TABLE 9]
| 項目 | 數量 | 說明 |
| --- | --- | --- |
| 納入配對 | 8 | A01–A08 |
| 納入原始分數格 | 80 | 全部在 0–4 |
| 排除配對 | 0 | 僅限本合成 fixture |
| 留置配對 | 0 | 僅限本合成 fixture |
| 重複代碼 | 0 | 合成識別碼唯一 |
| 缺漏維度 | 0 | 每對每階段五維俱備 |
| 超範圍值 | 0 | 無 5、負數、空白或非整數 |
| 補值 | 0 | 未使用 0、平均數或前測值代入 |
| 有效分母 | 8 | 本報告 n=8 |

[DOCX TABLE 10]
| 步驟 | 檢查 | 本 fixture 結果 |
| --- | --- | --- |
| 1. 來源綁定 | 核對 0100 問卷版次、題目與評分錨點；確認前測、後測使用相同版本並保存來源表單。 | 已記錄；0100 仍為候選 |
| 2. 結構完整性 | 8 對 × 5 維度 × 2 階段 | 80 格齊全 |
| 3. 數值範圍 | 每格為 0–4 整數 | 全部符合 |
| 4. 配對與版本 | A01–A08 唯一、前後版本相同、課程代碼相同、日期順序合理 | 符合 |
| 5. 列算術 | 每列前總分、後總分、變化 | 八列均重算相符 |
| 6. 維度交叉合計 | A–E 前合計、後合計與整體總分 | 前 75、後 117、差 +42 |
| 7. 圖表資料 | 五維度平均、固定 0–4、前後兩系列 | 與表 6-1、表 7-1 一致 |
| 8. 隱私與去識別 | 僅有合成識別碼；無姓名、電話或證件欄 | 符合；真實使用時仍須重新檢核 |

[DOCX TABLE 11]
| 代碼 | 前 A | 前 B | 前 C | 前 D | 前 E | 前總分 | 後 A | 後 B | 後 C | 後 D | 後 E | 後總分 | 變化 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 2 | 2 | 1 | 2 | 1 | 8 | 3 | 3 | 3 | 3 | 3 | 15 | +7 |
| A02 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 4 | 16 | +6 |
| A03 | 3 | 2 | 2 | 2 | 2 | 11 | 3 | 3 | 3 | 3 | 2 | 14 | +3 |
| A04 | 2 | 2 | 1 | 2 | 2 | 9 | 3 | 3 | 2 | 3 | 2 | 13 | +4 |
| A05 | 3 | 3 | 2 | 2 | 2 | 12 | 4 | 4 | 3 | 3 | 4 | 18 | +6 |
| A06 | 1 | 2 | 1 | 1 | 2 | 7 | 3 | 2 | 2 | 3 | 2 | 12 | +5 |
| A07 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 3 | 15 | +5 |
| A08 | 2 | 1 | 2 | 1 | 2 | 8 | 3 | 3 | 3 | 3 | 2 | 14 | +6 |

[DOCX TABLE 12]
| 維度 | 前測合計 | 前測平均 | 後測合計 | 後測平均 | 平均變化 |
| --- | --- | --- | --- | --- | --- |
| A 來源事實與情境 | 17 | 2.125 | 25 | 3.125 | +1.000 |
| B 紀錄完整性與可追溯 | 16 | 2.000 | 24 | 3.000 | +1.000 |
| C 任務與產出對應 | 13 | 1.625 | 22 | 2.750 | +1.125 |
| D 資料最小化與隱私意識 | 14 | 1.750 | 24 | 3.000 | +1.250 |
| E 後續行動規劃 | 15 | 1.875 | 22 | 2.750 | +0.875 |
| 整體總分／平均 | 75 | 9.375／20 | 117 | 14.625／20 | +5.25／20 |

[DOCX TABLE 13]
| 指標 | 前測 | 後測 | 變化 |
| --- | --- | --- | --- |
| 總分 | 75 | 117 | +42 |
| 平均總分（÷8） | 9.375／20 | 14.625／20 | +5.25／20 |
| 正規化顯示（÷20；群體÷160） | 46.875% | 73.125% | +26.25 個百分點 |

[DOCX TABLE 14]
| 軸／維度 | 前測平均 | 後測平均 | 差異 |
| --- | --- | --- | --- |
| A 來源事實與情境 | 2.125 | 3.125 | +1.000 |
| B 紀錄完整性與可追溯 | 2.000 | 3.000 | +1.000 |
| C 任務與產出對應 | 1.625 | 2.750 | +1.125 |
| D 資料最小化與隱私意識 | 1.750 | 3.000 | +1.250 |
| E 後續行動規劃 | 1.875 | 2.750 | +0.875 |

[DOCX TABLE 15]
| 屬性 | 設定 |
| --- | --- |
| 圖表類型 | 雷達圖（radar chart），含資料標記；不使用 3D、透視或立體效果 |
| 類別順序 | A → B → C → D → E，順時針排列，A 置於上方起始位置 |
| 軸標籤 | 五個完整繁體中文標籤：來源事實與情境、紀錄完整性與可追溯、任務與產出對應、資料最小化與隱私意識、後續行動規劃 |
| 系列 1 | 前測自評平均（SAMPLE） |
| 系列 2 | 後測自評平均（SAMPLE） |
| 數值 | 前測：2.125、2.000、1.625、1.750、1.875；後測：3.125、3.000、2.750、3.000、2.750 |
| 徑向軸 | 最小值 0、最大值 4、主要刻度間隔 1；刻度為 0、1、2、3、4 |
| 網格 | 淺色、低對比；不得遮住線條或標籤 |
| 圖例 | 置於圖下方或右側空白區，完整顯示兩個系列；不得與圖說分離 |
| 標記 | 前後系列使用不同形狀與線型，不能只靠顏色區分 |
| 資料標籤 | 預設關閉以免擁擠；若顯示，固定三位小數，且不得取代表 7-1 |
| 標題 | SAMPLE／SYNTHETIC：五維度前後自評平均（n=8；0–4 分） |
| 圖說 | 見 7.3；圖說與圖不得跨頁分離 |
| 來源註 | 「來源：0100 R09 合成 fixture；所有數值為 SAMPLE／SYNTHETIC；n=8；描述性統計。」 |
| 可讀性 | 圖內文字至少 9.5 pt；軸標籤不得裁切、旋轉到難以閱讀或只剩英文縮寫 |

[DOCX TABLE 16]
| 維度 | 前測平均 | 後測平均 | 平均差 | 數字層級的解讀 |
| --- | --- | --- | --- | --- |
| A 來源事實與情境 | 2.125 | 3.125 | +1.000 | 後測平均為五維最高（3.125）；與 B 同為 +1.000。這是群體平均，不能推論每位學員都達到 3 分以上。 |
| B 紀錄完整性與可追溯 | 2.000 | 3.000 | +1.000 | 合成平均由 2.000 到 3.000；數值上增加 1.000。不得寫成「紀錄能力已達標」。 |
| C 任務與產出對應 | 1.625 | 2.750 | +1.125 | 前測平均為五維最低（1.625）；後測平均 2.750，仍低於 3.000。這個位置只是此組合成分數的算術事實。 |
| D 資料最小化與隱私意識 | 1.750 | 3.000 | +1.250 | 平均差 +1.250，為五維最大；但不能解讀為「隱私能力進步最多」或訓練效果最大。 |
| E 後續行動規劃 | 1.875 | 2.750 | +0.875 | 平均差 +0.875，為五維最小；不能解讀為「後續規劃最無效」或「訓練沒有幫助」。 |

[DOCX TABLE 17]
| 建議角色 | 建議責任 | 不可做的事 |
| --- | --- | --- |
| 文件持有人／課程承辦窗口 | 確認實際使用的 0100 問卷版次及版本號，保管來源表單，維持配對代碼控制並確認場次。 | 不得代填、代選代碼或修改分數 |
| 表單／題項審查者 | 檢查題意、錨點、版本與填答說明是否一致 | 不得把理解測試當成訓練成效證據 |
| 資料管理者 | 去識別收件、權限控管、分開保管對照資訊 | 不得把姓名、電話或名冊併入分析檔 |
| 表單檢核者 | 逐份檢查完整性、配對、版本、日期與 HOLD／REJECT | 不得替任何缺漏補值 |
| 分析者 | 重算 80 格、總分、維度統計、分母與圖表資料 | 不得直接手改衍生值或挑選有利結果 |
| 第二核算者 | 獨立重算與比對差異 | 不得與分析者共用未揭露的暫存值 |
| 獨立審查者 | 按本報告版次完成語意、算術與 Word 呈現審查。 | 不得在未審查時簽署或背書 |
| 機構權責主管 | 在機構程序允許時授權真實資料使用與釋出 | 不得以本候選稿代替正式核定 |

[DOCX TABLE 18]
| 步驟 | 建議角色 | 觸發條件 | 建議工作與產出 | 停止／HOLD 條件 |
| --- | --- | --- | --- | --- |
| 1. 凍結表單版本 | 文件持有人 | 準備使用 0100 前 | 確認問卷版次、題目與評分錨點一致，並記錄使用版本。 | 版本或題目不一致時分開分析，不得直接合併。 |
| 2. 驗證題意理解 | 題項審查者、承辦窗口 | 第一次真實施測前 | 以獲授權的小型認知訪談或說明測試檢查五題與 0–4 錨點是否被理解；記錄修訂需求 | 無授權、無隱私安排或題意仍不清楚時，不得開始正式蒐集 |
| 3. 真實施測與配對控制 | 承辦窗口、資料管理者 | 機構核准辦理且隱私流程就緒 | 前後測使用同版本、同配對代碼；名冊與分數分開保管；當場檢查完整性 | 缺漏、重複代碼、版本不符或個資外洩風險即 HOLD |
| 4. 收回與檢核 | 表單檢核者、資料管理者 | 表單收回後 | 逐份檢核真實回應、登錄納入／排除／留置份數與原因 | 未揭露分母、未解決重複或無法配對時，不得進入分析 |
| 5. 建檔與獨立重算 | 分析者、第二核算者 | 檢核完成且資料集凍結 | 建立去識別資料集；重算每列總分、維度合計、整體統計與圖表值 | 任一加總或分母不一致即整批 HOLD |
| 6. 產出統計與圖表 | 分析者 | 資料集通過檢核 | 依表 6-1、表 6-2、表 7-1 產生報告與固定 0–4 雷達圖 | n、排除數、圖例或軸標籤不完整即不得釋出 |
| 7. 視需要進行客觀實作任務 | 課程權責人、合格評分者 | 另有書面授權且具獨立評分規準 | 以獨立任務觀察實際表現；另立資料集與分析，不併入 0100 自評分數 | 未授權、無規準、無評分者訓練時不得執行或宣稱 |
| 8. 日後比較真實紀錄 | 分析者、獨立審查者 | 有足夠且合法的真實配對資料，並事先指定分析計畫 | 分開報告樣本、排除、前後分布與不確定性；必要時才使用推論方法 | 設計不足或資料品質不明時，只做描述，不做因果或顯著性宣稱 |
| 9. 審查與釋出 | 獨立審查者、機構權責主管 | 文件與資料凍結 | 依報告版次完成語意、算術與 Word 呈現審查；依程序填寫審查與核准欄。 | 未完成審查、未經授權或仍有 SAMPLE 殘留時，維持 HOLD |

[DOCX TABLE 19]
| 條件 | 判定 | 必要處理 | 是否可補正 |
| --- | --- | --- | --- |
| 前測或後測缺少其中一份 | HOLD | 尋找同一配對代碼的另一份；不得以其他學員或平均數替代 | 可，限本人補件 |
| 任一維度空白 | HOLD | 請本人補填；不得以 0、平均、前測值或推估值代入 | 可，限本人補正 |
| 同一題勾選兩個以上分數 | HOLD | 請本人重選一個；承辦人不得代選 | 可，限本人重選 |
| 分數超出 0–4 或非整數 | HOLD | 核對原表並更正；不得截斷或四捨五入 | 可，限有原始依據 |
| 同階段出現重複配對代碼 | HOLD | 同代碼全部表單留置；不得挑一份計分 | 僅在本人可安全確認時 |
| 重複代碼無法安全確認歸屬 | REJECT | 全部相關表單排除，揭露於分母 | 不可 |
| 前後測代碼不一致 | HOLD | 未經本人確認不得配對；確認後更正並留註記 | 可，限本人確認 |
| 前後測版本不一致 | REJECT | 該對不得併入分析 | 不可 |
| 前後測課程代碼或場次不一致 | REJECT | 不得跨課程配對 | 不可 |
| 後測日期早於前測 | REJECT | 查明後重填；不得倒填日期 | 不可 |
| 表單含姓名、電話、證件號或其他直接識別 | HOLD | 立即遮蔽或換碼；必要時重填 | 可，完成去識別後 |
| 承辦人代填、代選或代改分數 | REJECT | 該份作廢並記錄程序違失 | 不可 |
| 0100 問卷版本或前後配對來源無法確認 | HOLD | 停止整批分析並重新綁定 | 可，完成來源確認後 |
| 未揭露有效分母或排除份數 | HOLD | 不得釋出最終報告 | 可，補齊揭露後 |

[DOCX TABLE 20]
| ID | 目前 SAMPLE 欄位／值 | 文件／表／圖位置 | 真實替換來源 | 必要驗證 | HOLD 動作 |
| --- | --- | --- | --- | --- | --- |
| S-01 | 辦理單位：SAMPLE 示範訓練機構 | §3.4 表 3-2 | 經授權的機構名稱與課程主檔 | 與核准課程紀錄一致；不得自行推定 | 未確認前 HOLD 報告 |
| S-02 | 課程代碼：SAMPLE-CRS-0100 | §1.2、§3.4 表 3-2 | 機構正式課程代碼 | 與場次、表單預印代碼一致 | 不一致則 HOLD／REJECT 受影響配對 |
| S-03 | 課程名稱：SAMPLE「資料紀錄與隱私基礎示範課」 | §1.2、§3.4 表 3-2 | 正式課程名稱 | 與課程主檔及表單一致 | 未確認前 HOLD |
| S-04 | 前測日期：2026-11-02 | §1.2、§3.4 表 3-2 | 真實前測日期紀錄 | 與表單及場次紀錄一致 | 缺漏或矛盾則 HOLD |
| S-05 | 後測日期：2026-11-02 | §1.2、§3.4 表 3-2 | 真實後測日期紀錄 | 不得早於前測；與場次一致 | 早於前測則 REJECT |
| S-06 | 問卷版本：SR-0100-v1.0-SAMPLE | §1.2、§3.4 表 3-2、§4.1 | 機構核定之問卷版本 | 前後測完全相同；與實際表單一致 | 不一致則 REJECT 該對 |
| S-07 | 配對識別：A01–A08 | §5 表 5-1、§10.5 | 去識別分析編號；原始配對代碼另由單一窗口保管 | 唯一、可配對、不得含個資 | 重複或無法配對則 HOLD；未解 REJECT |
| S-08 | 80 個原始分數格 | §5 表 5-1、§10.5 | 8 對已完成且檢核通過的真實 0100 前後表單 | V1–V4、V6；每格不得補值 | 任一格失敗則 H1／H4；未解 H3 |
| S-09 | 8 對前總分、後總分、變化（24 個值） | §5 表 5-1、§10.6 | 不得人工替換；由 S-08 以固定公式重算 | V5；逐列核對 | H2／H4 |
| S-10 | 五維度合計、平均、差異（25 個值） | §6 表 6-1、§7 表 7-1、圖 1、§10.7 | 由 S-08 重算，不由舊稿沿用 | V5；維度交叉合計 | H2／H4 |
| S-11 | 整體總分、平均、淨變化 | §2 表 2-1、§6 表 6-2、§10.8 | 由 S-08／S-09 重算 | V5；三種算法交叉核對 | H2 |
| S-12 | 正規化 46.875%／73.125%／+26.25 個百分點 | §2、§6.2、§10.8 | 由真實總分除以 20（群體除以 160）重算 | V5；不得沿用合成百分比 | H2 |
| S-13 | 雷達圖資料與圖說（前後系列、n=8、SAMPLE） | §7 表 7-1、圖 1、§10.8 | 由 S-10 的真實維度平均重新產生 | V5、V7；軸、圖例、尺度、標籤 | H2／H4 |
| S-14 | SAMPLE 邊界文字、限制與警告 | 全篇、§1、§12 | 真實審查後改為正式版本文字，但保留「自評、描述性、非客觀技能」限制 | V7；不得刪除核心限制 | 未完成替換前 HOLD 全篇 |
| S-15 | 準備／審查／核准空白欄 | §1.4、§12.1 | 實際完成的人員、日期與機構紀錄 | 僅依真實簽核資料填寫 | 無紀錄則保持空白並 HOLD 釋出 |

[DOCX TABLE 21]
| locator | value | source | verify | hold |
| --- | --- | --- | --- | --- |
| T5-1/A01/前A | 2 | SRC-A01-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/前B | 2 | SRC-A01-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/前C | 1 | SRC-A01-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/前D | 2 | SRC-A01-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/前E | 1 | SRC-A01-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/後A | 3 | SRC-A01-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/後B | 3 | SRC-A01-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/後C | 3 | SRC-A01-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/後D | 3 | SRC-A01-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A01/後E | 3 | SRC-A01-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/前A | 2 | SRC-A02-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/前B | 2 | SRC-A02-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/前C | 2 | SRC-A02-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/前D | 2 | SRC-A02-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/前E | 2 | SRC-A02-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/後A | 3 | SRC-A02-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/後B | 3 | SRC-A02-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/後C | 3 | SRC-A02-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/後D | 3 | SRC-A02-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A02/後E | 4 | SRC-A02-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/前A | 3 | SRC-A03-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/前B | 2 | SRC-A03-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/前C | 2 | SRC-A03-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/前D | 2 | SRC-A03-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/前E | 2 | SRC-A03-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/後A | 3 | SRC-A03-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/後B | 3 | SRC-A03-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/後C | 3 | SRC-A03-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/後D | 3 | SRC-A03-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A03/後E | 2 | SRC-A03-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/前A | 2 | SRC-A04-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/前B | 2 | SRC-A04-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/前C | 1 | SRC-A04-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/前D | 2 | SRC-A04-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/前E | 2 | SRC-A04-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/後A | 3 | SRC-A04-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/後B | 3 | SRC-A04-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/後C | 2 | SRC-A04-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/後D | 3 | SRC-A04-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A04/後E | 2 | SRC-A04-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/前A | 3 | SRC-A05-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/前B | 3 | SRC-A05-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/前C | 2 | SRC-A05-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/前D | 2 | SRC-A05-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/前E | 2 | SRC-A05-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/後A | 4 | SRC-A05-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/後B | 4 | SRC-A05-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/後C | 3 | SRC-A05-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/後D | 3 | SRC-A05-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A05/後E | 4 | SRC-A05-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/前A | 1 | SRC-A06-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/前B | 2 | SRC-A06-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/前C | 1 | SRC-A06-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/前D | 1 | SRC-A06-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/前E | 2 | SRC-A06-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/後A | 3 | SRC-A06-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/後B | 2 | SRC-A06-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/後C | 2 | SRC-A06-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/後D | 3 | SRC-A06-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A06/後E | 2 | SRC-A06-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/前A | 2 | SRC-A07-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/前B | 2 | SRC-A07-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/前C | 2 | SRC-A07-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/前D | 2 | SRC-A07-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/前E | 2 | SRC-A07-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/後A | 3 | SRC-A07-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/後B | 3 | SRC-A07-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/後C | 3 | SRC-A07-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/後D | 3 | SRC-A07-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A07/後E | 3 | SRC-A07-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/前A | 2 | SRC-A08-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/前B | 1 | SRC-A08-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/前C | 2 | SRC-A08-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/前D | 1 | SRC-A08-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/前E | 2 | SRC-A08-P | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/後A | 3 | SRC-A08-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/後B | 3 | SRC-A08-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/後C | 3 | SRC-A08-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/後D | 3 | SRC-A08-Q | V1/V2/V3/V4/V6 | H1/H4 |
| T5-1/A08/後E | 2 | SRC-A08-Q | V1/V2/V3/V4/V6 | H1/H4 |

[DOCX TABLE 22]
| 配對 | 前總分定位＝值 | 後總分定位＝值 | 變化定位＝值 |
| --- | --- | --- | --- |
| A01 | T5-1/A01/前總分＝8 | T5-1/A01/後總分＝15 | T5-1/A01/變化＝+7 |
| A02 | T5-1/A02/前總分＝10 | T5-1/A02/後總分＝16 | T5-1/A02/變化＝+6 |
| A03 | T5-1/A03/前總分＝11 | T5-1/A03/後總分＝14 | T5-1/A03/變化＝+3 |
| A04 | T5-1/A04/前總分＝9 | T5-1/A04/後總分＝13 | T5-1/A04/變化＝+4 |
| A05 | T5-1/A05/前總分＝12 | T5-1/A05/後總分＝18 | T5-1/A05/變化＝+6 |
| A06 | T5-1/A06/前總分＝7 | T5-1/A06/後總分＝12 | T5-1/A06/變化＝+5 |
| A07 | T5-1/A07/前總分＝10 | T5-1/A07/後總分＝15 | T5-1/A07/變化＝+5 |
| A08 | T5-1/A08/前總分＝8 | T5-1/A08/後總分＝14 | T5-1/A08/變化＝+6 |

[DOCX TABLE 23]
| 維度 | 前合計 | 前平均 | 後合計 | 後平均 | 差異 |
| --- | --- | --- | --- | --- | --- |
| A | T6-1/A/前合計＝17 | T6-1/A/前平均＝2.125 | T6-1/A/後合計＝25 | T6-1/A/後平均＝3.125 | T6-1/A/差＝+1.000 |
| B | T6-1/B/前合計＝16 | T6-1/B/前平均＝2.000 | T6-1/B/後合計＝24 | T6-1/B/後平均＝3.000 | T6-1/B/差＝+1.000 |
| C | T6-1/C/前合計＝13 | T6-1/C/前平均＝1.625 | T6-1/C/後合計＝22 | T6-1/C/後平均＝2.750 | T6-1/C/差＝+1.125 |
| D | T6-1/D/前合計＝14 | T6-1/D/前平均＝1.750 | T6-1/D/後合計＝24 | T6-1/D/後平均＝3.000 | T6-1/D/差＝+1.250 |
| E | T6-1/E/前合計＝15 | T6-1/E/前平均＝1.875 | T6-1/E/後合計＝22 | T6-1/E/後平均＝2.750 | T6-1/E/差＝+0.875 |

[DOCX TABLE 24]
| 圖表資料 | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| T7-1/前平均 | 2.125 | 2.000 | 1.625 | 1.750 | 1.875 |
| T7-1/後平均 | 3.125 | 3.000 | 2.750 | 3.000 | 2.750 |

[DOCX TABLE 25]
| 指標 | 定位＝值 | 重算依據 | HOLD |
| --- | --- | --- | --- |
| 前總分 | T2-1；T6-2/前總分＝75 | 八對前總分合計 | H2 |
| 後總分 | T2-1；T6-2/後總分＝117 | 八對後總分合計 | H2 |
| 淨變化 | T2-1；T6-2/淨變化＝+42 | 117 − 75 | H2 |
| 前平均 | T2-1/前平均＝9.375／20 | 75 ÷ 8 | H2 |
| 後平均 | T2-1/後平均＝14.625／20 | 117 ÷ 8 | H2 |
| 平均每人變化 | T2-1/平均變化＝+5.25／20 | 42 ÷ 8；或 14.625 − 9.375 | H2 |
| 正規化前 | T2-1；T6-2/正規化前＝46.875% | 9.375 ÷ 20；群體 75 ÷ 160 | H2 |
| 正規化後 | T2-1；T6-2/正規化後＝73.125% | 14.625 ÷ 20；群體 117 ÷ 160 | H2 |
| 正規化差 | T2-1；T6-2/正規化差＝+26.25 個百分點 | 73.125 − 46.875 | H2 |
| n | T2-1/n＝8 | 納入配對數 | H2 |
| 原始格數 | T2-1/原始格數＝80 | 8 × 5 × 2 | H2 |
| 圖 1 系列 | FIG1／T7-1/前平均、FIG1／T7-1/後平均 | 直接等於表 10-4 的平均 | H2／H4 |

[DOCX TABLE 26]
| 文件／需求 | 產物類型 | 分析單位 | 核心構念 | 主要輸出 | 盲測辨識指紋 | 不可回答的問題 |
| --- | --- | --- | --- | --- | --- | --- |
| 0097／I18-E05 | 知覺／看法調查 | 填答者對某對象的知覺 | 知覺、意見或看法 | 知覺結果彙總 | 以知覺題為主；沒有前後自評配對、沒有技能規準、沒有五軸成長雷達 | 不能當成 0100 的前後自評、不能當成技能評分或滿意度 |
| 0098／I18-E06 | 滿意度調查 | 對課程或服務的滿意感受 | 滿意度 | 滿意度統計與回饋 | 滿意度題項；不是能力自評、不是技能評分、不是前後雷達 | 不能證明學習、能力提升或訓練成效 |
| 0099／I18-E07 | 技能工作／評分規準 | 作品或任務表現 | 以其規準定義的技能表現 | 技能評分、評分規準與其自身門檻（含 14/20） | 有評分者、rubric、作品或任務；有技能通過概念 | 不能把 0101 的自評分數混入；不能宣稱一致性、相關或互換 |
| 0100／I18-E08 | 可填寫表單／資料蒐集工具 | 每位學員的前後配對 | 五維度自覺能力（0–4） | 空白題頁、配對欄位、80 格原始資料 | 有勾選欄、前測／後測頁、五題與版本欄；是表單不是彙總報告 | 不是聚合分析、不是雷達圖結論、不是技能證據 |
| 0101／I18-E08 | 聚合描述性報告 | 8 對合成配對（本稿） | 自覺改變的群體描述 | 75／117／+42、五維平均、固定 0–4 雷達圖與替換登錄 | 有 n、分母、80 格映射及雷達圖；是聚合報告，不是配套表單。 | 不是技能評分、不是因果效果、不是 0099 的替代品 |

[DOCX TABLE 27]
| 版本／文件 | 狀態 | 邊界 |
| --- | --- | --- |
| 0101 R09（本稿） | 現行候選 DOCX | 使用 8 對 × 5 維度 × 2 階段、80 格合成 fixture |
| 0101 R08A／R08B／R08C | 歷史稿 | 均為 1 人 × 6 維度之舊版；不得作為現行模板、接受依據或數值來源 |
| 0100 R08 | 歷史稿 | 1 人 × 6 維度，與現行 8×5 契約不一致 |
| 0100 R09（內頁 R09a） | 現行配套候選 | 候選文件；尚未正式接受。 |
| 0099 R17 | 另一需求 I18-E07 的文件 | 僅作為合成 fixture 重用來源；不修改、不重新分類、不引入其技能門檻 |

## Current Word-native PDF text by page
===== WORD PDF PAGE 1 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 1 頁
0101 學員自我評量統計與能力雷達圖分析報告
Learner Self-Assessment Statistics and Perceived-Growth Radar Analysis Report
R09 候選 DOCX｜DOC_ID 0101｜需求 I18-E08｜2026-10-21
SAMPLE／SYNTHETIC 邊界警告（先讀） 本報告中的 A01–A08、課程、機構、代碼、日期、80 個分
數格及所有衍生統計，全部是 SAMPLE／SYNTHETIC 合成示範資料。它們不代表任何真實學員、真
實課程、真實訓練辦理、真實參與、真實簽署、真實核准、協會核定、認證或訓練成效。 本稿是候
選 DOCX，不是正式驗收版本；配套的 0100 R09 亦為候選文件，尚未正式接受。除明確標示的來源
與版本資訊外，本報告不得作為對外績效、招生、補助、認證、及格或能力證明。 示範日期 2026-
11-02 為合成占位日期；即使晚於本稿日期，也不代表已排定、預定或已辦理任何課程或施測。
1. 封面與文件識別
1.1 報告目的
本報告的目的，是把 0100 R09 配套表單中的 8 對合成前後測自評資料，整理成可追溯的描述性統計、五
維度摘要與雷達圖資料，並明確揭露分母、排除規則、圖表尺度與使用限制。
本報告要回答的問題只有四項：
1. 這 8 對合成資料的 80 個原始分數是否完整、是否落在 0–4 範圍？
2. 前測與後測的總分、平均、五維度合計與差異分別是多少？
3. 以固定 0–4 尺度呈現時，五軸雷達圖的資料與圖說應該如何標示？
4. 若未來要換成真實資料，必須替換哪些欄位、重算哪些數值、在什麼條件下 HOLD 或 REJECT？
本報告不回答「訓練是否有效」、「學員能力是否提升」、「學員是否達標」、「課程是否優於其他課程」
或「本量表是否具有信效度」等問題。
1.2 文件識別與版本
欄位 內容
文件名稱 學員自我評量統計與能力雷達圖分析報告
英文名稱 Learner Self-Assessment Statistics and Perceived￾Growth Radar Analysis Report
DOC_ID 0101
需求編號 I18-E08
報告識別說明
DOC_ID 0101、需求 I18-E08；官方印刷序號另以
UNKNOWN 標示。
官方表單印刷序號 UNKNOWN（未取得官方原始表單印刷序號）

===== WORD PDF PAGE 2 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 2 頁
欄位 內容
本稿版次 R09（候選 DOCX）
稿件日期 2026-10-21
配套表單
0100 學員訓練前後自我評量表，R09 候選稿；文件
內頁版次標示為 R09a；問卷版本為 SR-0100-v1.0-
SAMPLE
配套表單用途
0100 用於蒐集學員個別前後自評；本報告負責彙整與
描述性分析。
配套狀態 候選文件，尚未正式接受；本報告不宣稱 0100 已完成
驗收
示範資料範圍
8 對 A01–A08 合成配對、5 個維度、前後測共 80 
格；不代表真實學員或課程。
分析範圍
描述性自評整理；不推論客觀技能、因果效果或機構績
效。
官方來源
TTQS 訓練機構證據資料表第 7 頁、指標 18；要求
學員訓練前後自我評量及自覺改變雷達分析。
官方要求內容 學員訓練前後自我評量，以及呈現自覺改變之雷達分析
資料性質 8 對 A01–A08 的 SAMPLE／SYNTHETIC 自評資料
樣本規模
n=8 對；5 個維度；前測／後測 2 階段；共 80 個原始分
數格
量表
每維度 0–4 分；單一階段總分 0–20 分；僅為本示範表使
用，非協會核定或信效度驗證量表
示範課程代碼 SAMPLE-CRS-0100
示範課程名稱 SAMPLE「資料紀錄與隱私基礎示範課」
示範施測日期
前測 SAMPLE 2026-11-02；後測 SAMPLE 2026-11-02
（課後同日）
報告狀態
SAMPLE／SYNTHETIC 候選 DOCX；沒有真實資料
或正式核准，不得作為實際成效證明。
文件狀態 R09 SAMPLE／SYNTHETIC 候選；尚未正式接受，
亦未替代真實資料或正式核准。
版本註記：配套問卷內頁標示 R09a；本報告引用問卷版本 SR-0100-v1.0-SAMPLE。正式填答前應確
認前測與後測使用同一問卷版本；如換版，分開分析並記錄版本。

===== WORD PDF PAGE 3 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 3 頁
1.3 誰可以使用、可以做什麼
使用情境 是否可用 條件與限制
文件作者與內部方法審查者檢查格式、算術、圖
表規格
可用
必須保留全篇 SAMPLE／SYNTHETIC 標記與限制
說明
未來獲授權的課程承辦窗口、資料管理者與分析
者做替換演練
可用
只能使用經檢核的真實 0100 表單，不得把合成
值當真實值
對外呈現課程成效、招生、績效、補助或認證 不可用
本稿沒有真實資料、對照設計、統計推論或機構
核准
判斷學員能力、及格、通過、聘用或升遷 不可用 自評分數不是客觀技能評分，也沒有通過門檻
與 0099 技能評分做一致性、相關或門檻比較 不可用
兩者構念、單位與用途不同；合成重用不構成實
證關係
學術推論、母體估計、統計顯著性宣稱 不可用 n=8、無抽樣架構、無對照組、無推論設計
本稿可以由內部讀者用來檢查「表格是否完整、數值是否算對、圖表是否標示清楚、替換登錄是否可執
行」。任何真實決策，都必須等到真實資料替換、重算、獨立審查與機構授權完成後，才可能進行。
1.4 準備、審查與核准欄位
欄位 狀態
準備／撰寫 未填寫
資料檢核 未填寫；不表示已完成獨立復核
獨立審查 未填寫；候選稿尚待獨立審查。
核准／核定 未填寫；未核准、未核定
機構／協會決定 無；本稿不主張任何核定、認證、背書或正式驗收
上述欄位刻意留空。未實際完成的人員、日期、簽署或核准，不得以職稱、角色、系統名稱或推定方式補
寫。
1.5 閱讀路徑
決策者宜先讀第 2 節與第 8.3 節，掌握結果與不可推論的界線；資料處理者宜讀第 4 節、第 10 節與附錄
式定位表；文件審查者宜讀第 11 節與第 12 節。第 5 節及第 10.5 節保留所有原始分數的可核對位置。
2. 執行結果與界線結論
2.1 主要結果
本報告依 0100 R09 的 8 對合成示例重算。所有原始值保持 0–4 整數；下列平均與百分比僅為顯示用衍生
值。

===== WORD PDF PAGE 4 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 4 頁
表 2-1｜SAMPLE／SYNTHETIC：主要統計結果（n=8）
指標 結果 說明
納入分析 8 對 僅限本合成 fixture
排除 0 對 僅限本合成 fixture；不代表真實資料品質
原始分數格 80 格 8 × 5 維度 × 2 階段
分數範圍檢查 全部 0–4 80 格均為整數且在範圍內
前測總分 75 8 人前測總分合計
後測總分 117 8 人後測總分合計
淨變化 +42 117 − 75
前測平均總分 9.375／20 75 ÷ 8
後測平均總分 14.625／20 117 ÷ 8
平均每人變化 +5.25／20 42 ÷ 8；亦等於 14.625 − 9.375
正規化顯示 46.875% → 73.125% 9.375 ÷ 20 與 14.625 ÷ 20；群體為 75 ÷ 160、
117 ÷ 160
正規化差異 +26.25 個百分點 僅為線性顯示，不是效果量、門檻或通過率
五維平均差範圍 最小 +0.875；最大 +1.250 E 最小、D 最大；只有算術描述意義
八對的總分變化均為正，但這只是此組合成分數的算術事實，不代表每位學員在每個維度都上升，也不代
表真實訓練會產生相同結果。
2.2 五維度結果摘要
表 2-2｜SAMPLE／SYNTHETIC：五維度前後平均與差異（n=8）
維度 前測平均 後測平均 平均差
A 來源事實與情境 2.125 3.125 +1.000
B 紀錄完整性與可追溯 2.000 3.000 +1.000
C 任務與產出對應 1.625 2.750 +1.125
D 資料最小化與隱私意識 1.750 3.000 +1.250
E 後續行動規劃 1.875 2.750 +0.875
五個維度的後測平均都高於前測平均。數值差異最大的是 D（+1.250），最小的是 E（+0.875）；A 與 B 
同為 +1.000，C 為 +1.125。這些排序只是這組合成資料的算術結果，不是效果大小、能力排名或訓練優
先順序的證明。

===== WORD PDF PAGE 5 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 5 頁
2.3 界線結論
可報告的結論 在這組 8 對 SAMPLE 資料的算術範圍內，後測總分為 117、前測總分為 75，淨差為
+42；平均總分由 9.375／20 變為 14.625／20，平均每人差為 +5.25／20。五維度後測平均均高於前
測平均。 不可報告的結論 不得寫成「訓練有效」、「能力已提升」、「學員已達標」、「課程造成
改變」、「與 0099 技能評分一致」、「具統計顯著性」、「可推廣到母體」或「可作為協會認證成
果」。本稿沒有真實資料、沒有對照組、沒有推論設計，且 0–4 分數是自評而非客觀技能測量。
3. 資料血緣、範圍與版本
3.1 分析鏈
本報告只聚合 0100 R09 已完成之合成示例，不重製 0100 的空白表單，也不把 0100 的個別填答頁當成彙
總報告。
官方證據需求：I18-E08；PDF p.7、indicator 18
 │
 ▼
0100 R09 候選表單與完成示例
8 對 × 5 維度 × 2 階段 = 80 個原始分數格
 │
 │ 配對、版本、範圍、日期、隱私與分母檢核
 ▼
0101 R09 本報告
描述統計、五維度摘要、固定 0–4 雷達圖資料與替換登錄
129-to-142 對照將 I18-E08 指向 0100 | 0101：0100 是學員前後自我評量表，0101 是自覺成長雷達分析
報告。兩者是同一需求下的不同產物層級，不可互相代替。
3.2 來源綁定
表 3-1｜來源與版本綁定（非 SAMPLE 數值）
資料／文件 可查定位 用途與限制
官方證據來源
TTQS 訓練機構版證據資料表，第 7 
頁、指標 18
要求學員訓練前後自我評量，並呈現自
覺改變的雷達分析。
配套文件 0100 學員訓練前後自我評量表 R09a；SR￾0100-v1.0-SAMPLE
個別學員資料蒐集表；候選文件，尚未
正式接受。
0097／I18-E05 知覺／看法調查
分析對象的知覺或意見；不能代替前後
自評配對。
0098／I18-E06 滿意度調查
評估課程或服務感受；不能證明學習或
技能提升。

===== WORD PDF PAGE 6 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 6 頁
資料／文件 可查定位 用途與限制
0099／I18-E07 技能工作與評分規準
評估任務表現；本報告不引用其技能門
檻或結果。
本報告 0101／I18-E08 聚合描述性自評報告
8 對合成配對的示範分析；不是表
單、技能評分或因果證據。
本示範使用 SR-0100-v1.0-SAMPLE。正式分析時，前測與後測須使用相同問卷版本；若題目或評分錨點不
同，應分版整理，不得直接合併配對。
3.3 與 0099 R17 的合成重用邊界
本報告 A01–A08 的 80 格數值，是依現行契約自 0099 R17 共用同一組合成數值，僅作為跨文件格式、欄
位對應與算術一致性的 SAMPLE／SYNTHETIC demonstration fixture。必須明確區分以下五點：
1. 不是同一種測量。 0099 是技能工作／評分規準文件，數值在該文件中的角色是技能評分示範；在本報
告中則只是學員自評值。兩者的構念、評分者、單位與用途不同。
2. 不是一致性或相關證據。 即使兩份文件使用同一組數字，也不能說自評與技能評分「一致」、「相
關」、「互相驗證」或「可互換」。
3. 不是獨立實證資料。 共用 fixture 是示範重用，不是第二次獨立觀察，不能增加樣本或提供額外證據。
4. 不得引入 0099 的技能門檻。 0099 的 14/20 或任何技能通過標準，均不得套用到本報告；本報告不設及
格線、不計算通過率、不呈現技能達標人數。
5. 不是真實機構或課程結果。 本報告沒有真實學員、真實課程、真實訓練辦理、真實協會核定或真實成
效。所有 SAMPLE 欄位都必須在真實使用前替換。
0099 R17 本身不被本報告修改、重新分類或重新認證。其原需求 I18-E07 與文件定位保持不變。
3.4 分析範圍與樣本基本資料
表 3-2｜SAMPLE／SYNTHETIC：樣本與課程基本資料
欄位 目前示範值 邊界
辦理單位 SAMPLE 示範訓練機構 非真實機構
課程代碼 SAMPLE-CRS-0100 非正式課程代碼
課程名稱 SAMPLE「資料紀錄與隱私基礎示範課」 非真實課程
前測日期 SAMPLE 2026-11-02 非真實施測紀錄
後測日期 SAMPLE 2026-11-02（課後同日） 非真實施測紀錄；後測不得早於前測
問卷版本 SR-0100-v1.0-SAMPLE 前後測必須相同
配對識別 A01–A08
合成識別碼；正式使用應採可安全配對
的去識別代碼

===== WORD PDF PAGE 7 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 7 頁
欄位 目前示範值 邊界
量表 每維 0–4；單階段總分 0–20 示範用；非協會核定、非信效度驗證
納入分析 8 對 僅限本合成 fixture
原始分數格 80 格 8 × 5 × 2
表 3-2 的日期是 0100 的 SAMPLE fixture，不代表課程已辦理或學員已出席。稿件日期 2026-10-21 也
不是施測日期；不得以時間順序推定真實事件。
3.5 分析單位、分母與版本控制
本報告的分析單位是「一對同配對代碼的前測與後測」，不是單一問卷、單一題目或單一分數格。有效分
母為完成配對且通過檢核的對數；本合成 fixture 的 n=8。
• 原始分數格分母：80 格（8 × 5 × 2），只用於完整性與範圍檢查。
• 維度平均分母：每個維度每階段 8 個值。
• 總分平均分母：8 對。
• 正規化群體分母：160（8 × 20），僅為顯示用。
• 不得以 80 格當成人數分母，也不得把格數混稱為樣本數。
• 不得加權、不得用部分平均替代缺漏、不得變更分母而不揭露。
版本控制上，現行契約是 8 人 × 5 維度 × 2 階段。先前 1 人 × 6 維度的 R08 系列（包含 0100 R08 與 0101 
R08A／R08B／R08C）均為歷史稿，與現行 8×5 fixture 不一致，不得作為本稿模板、現行接受依據或數值
來源。R09 與 R08 系列不得混用。
4. 納入、排除與處理紀錄
4.1 納入條件
一對資料必須同時符合下列條件，才可進入本報告的有效分母：
1. 前測與後測具有相同的配對代碼；本合成示例為 A01–A08，正式使用時則為學員自選且可安全配對的代
碼或去識別分析編號。
2. 前測與後測使用完全相同的問卷版本；本示例為 SR-0100-v1.0-SAMPLE。
3. 同一課程代碼或同一辦理場次；不得把不同課程、不同版本或不同場次的資料混配。
4. 每一階段五個維度 A–E 均有值，且每個值都是 0–4 的整數。
5. 後測日期不得早於前測日期。
6. 同一階段不得有未解決的重複配對代碼。
7. 表單不得含姓名、電話、證件號、電子郵件或其他可直接或間接識別個人的欄位。

===== WORD PDF PAGE 8 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 8 頁
8. 有效份數、排除份數、留置份數與原因必須可追溯，且分母必須揭露。
4.2 HOLD／REJECT 規則
表 4-1｜缺漏、重複、錯配與版本問題的處理
情況 判定 處理方式 分母效果
任一維度缺漏，或同一題多選 HOLD
請本人補正或重選；不得以 0、平均
數、前測值或其他替代值填入
未補正前不納入
分數不是整數或超出 0–4 HOLD
核對原表；不得截斷、四捨五入或代
填；無法確認時整對 REJECT
未解決前不納入
同階段出現兩份以上相同代碼 HOLD
該代碼全部表單先 HOLD；不得挑選較
完整或分數較高的一份
未確認前全部不納
入
重複代碼經本人確認仍無法安全歸
屬
REJECT 全部相關表單排除，不得勉強配對
排除該等對數並揭
露
前後測代碼不一致 HOLD
未經本人當場確認不得配對；確認後更
正並留註記
未確認前不納入
前後測版本或課程代碼不一致 REJECT 該對不得併入分析 排除該對並揭露
後測日期早於前測 REJECT 時序錯誤；查明後重填，不得倒填日期 排除該對並揭露
表單含姓名、電話、證件號等 HOLD
立即遮蔽或換碼；未完成去識別前不得
分析
未完成前不納入
承辦人代填、代選或代改分數 REJECT 該份作廢，記錄程序違失 排除並揭露
問卷版次、前後配對條件或來源資
料無法確認
HOLD 停止整批分析，重新綁定來源 全部暫不納入
未揭露有效分母或排除份數 HOLD 不得產出最終 0101 分析或對外版本 報告不得釋出
任何缺漏都不得補值。HOLD 是可補正狀態；REJECT 是排除狀態。兩者都必須留下原因、處理人與
日期紀錄，且不得把排除份數隱藏在意見或註腳之外。
4.3 本次合成 fixture 的處理結果
表 4-2｜SAMPLE／SYNTHETIC：本 fixture 的納入與排除計數
項目 數量 說明
納入配對 8 A01–A08
納入原始分數格 80 全部在 0–4
排除配對 0 僅限本合成 fixture
留置配對 0 僅限本合成 fixture
重複代碼 0 合成識別碼唯一
缺漏維度 0 每對每階段五維俱備

===== WORD PDF PAGE 9 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 9 頁
項目 數量 說明
超範圍值 0 無 5、負數、空白或非整數
補值 0 未使用 0、平均數或前測值代入
有效分母 8 本報告 n=8
本報告所稱「已核對」僅指合成示範資料已完成結構、範圍、配對與算術核對；不是獨立實證驗證、不是
正式驗收，也不是對真實表單品質的聲明。
4.4 處理日誌
表 4-3｜SAMPLE／SYNTHETIC：處理與核對日誌
步驟 檢查 本 fixture 結果
1. 來源綁定
核對 0100 問卷版次、題目與評分錨點；確認前
測、後測使用相同版本並保存來源表單。
已記錄；0100 仍為候選
2. 結構完整性 8 對 × 5 維度 × 2 階段 80 格齊全
3. 數值範圍 每格為 0–4 整數 全部符合
4. 配對與版本
A01–A08 唯一、前後版本相同、課程代碼相同、
日期順序合理
符合
5. 列算術 每列前總分、後總分、變化 八列均重算相符
6. 維度交叉合計 A–E 前合計、後合計與整體總分 前 75、後 117、差 +42
7. 圖表資料 五維度平均、固定 0–4、前後兩系列 與表 6-1、表 7-1 一致
8. 隱私與去識別 僅有合成識別碼；無姓名、電話或證件欄 符合；真實使用時仍須重新檢核
本段記錄撰寫階段的結構與算術核對，並非獨立審查；正式使用前仍須由不同審查者檢查候選版本的內容、
計算與 Word 呈現。

===== WORD PDF PAGE 10 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 10 頁
5. 全體填答者資料
表 5-1｜SAMPLE／SYNTHETIC：A01–A08 前後測五維度原始值、總分與變化（n=8）
代碼 前 A 前 B 前 C 前 D 前 E 前總分 後 A 後 B 後 C 後 D 後 E 後總分 變化
A01 2 2 1 2 1 8 3 3 3 3 3 15 +7
A02 2 2 2 2 2 10 3 3 3 3 4 16 +6
A03 3 2 2 2 2 11 3 3 3 3 2 14 +3
A04 2 2 1 2 2 9 3 3 2 3 2 13 +4
A05 3 3 2 2 2 12 4 4 3 3 4 18 +6
A06 1 2 1 1 2 7 3 2 2 3 2 12 +5
A07 2 2 2 2 2 10 3 3 3 3 3 15 +5
A08 2 1 2 1 2 8 3 3 3 3 2 14 +6
計算定義：
• 前總分 = 前 A + 前 B + 前 C + 前 D + 前 E。
• 後總分 = 後 A + 後 B + 後 C + 後 D + 後 E。
• 變化 = 後總分 − 前總分。
• A–E 的十個欄位是 80 個原始分數格；前總分、後總分與變化是計算值，不計入 80 格。
• A01–A08 是合成識別碼，不是正式施測代碼，也不得直接轉用為真實學員的公開代碼。
逐列合計覆核（詳值見表 5-1）：A01 8→15（+7）；A02 10→16（+6）；A03 11→14（+3）；A04 9→13（+4）；A05 12→18（+6）；A06 7→12（+5）；A07 10→15
（+5）；A08 8→14（+6）。各維度與全體三種算法的交叉驗算見第 6.3 節。

===== WORD PDF PAGE 11 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 11 頁
6. 五維度統計與整體核算
6.1 維度統計
表 6-1｜SAMPLE／SYNTHETIC：五維度合計、平均與差異（每維 n=8）
維度 前測合計 前測平均 後測合計 後測平均 平均變化
A 來源事實與情境 17 2.125 25 3.125 +1.000
B 紀錄完整性與可追溯 16 2.000 24 3.000 +1.000
C 任務與產出對應 13 1.625 22 2.750 +1.125
D 資料最小化與隱私意
識
14 1.750 24 3.000 +1.250
E 後續行動規劃 15 1.875 22 2.750 +0.875
整體總分／平均 75 9.375／20 117 14.625／20 +5.25／20
維度平均的單位是該維度的 0–4 分，不是 0–20 總分。最後一列的「整體總分／平均」是 8 人總分的合計
與平均，不與前五列的維度平均相加混淆。
6.2 整體總分與正規化顯示
表 6-2｜SAMPLE／SYNTHETIC：整體總分、平均與正規化
指標 前測 後測 變化
總分 75 117 +42
平均總分（÷8） 9.375／20 14.625／20 +5.25／20
正規化顯示（÷20；群體÷160） 46.875% 73.125% +26.25 個百分點
正規化只是把總分線性換算成百分比，方便閱讀：
• 9.375 ÷ 20 = 46.875%；14.625 ÷ 20 = 73.125%。
• 群體層級：75 ÷ 160 = 46.875%；117 ÷ 160 = 73.125%。
• 差值為 26.25 個百分點，不是「進步 26.25%」，也不是效果量、通過率或常模分數。
6.3 交叉驗算
維度層級：
• 前測：17 + 16 + 13 + 14 + 15 = 75。
• 後測：25 + 24 + 22 + 24 + 22 = 117。
• 差異：117 − 75 = 42。
配對層級：

===== WORD PDF PAGE 12 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 12 頁
• 前測：8 + 10 + 11 + 9 + 12 + 7 + 10 + 8 = 75。
• 後測：15 + 16 + 14 + 13 + 18 + 12 + 15 + 14 = 117。
• 變化：+7 + 6 + 3 + 4 + 6 + 5 + 5 + 6 = 42。
平均層級：
• 平均每人變化：42 ÷ 8 = 5.25。
• 維度平均差合計：+1.000 + 1.000 + 1.125 + 1.250 + 0.875 = +5.250。
• 前後平均總分差：14.625 − 9.375 = 5.25。
三種算法結果一致：前 75、後 117、差 +42、平均差 +5.25。
6.4 顯示精度與平均方法
所有原始值均維持整數，不因顯示而改變。維度平均以「維度合計 ÷ 8」計算，顯示至三位小數；整體平
均以「總分 ÷ 8」計算。1.000、3.000 等尾零是顯示精度，不代表比原始整數多出有效位數。
本報告對 0–4 整數採算術平均，只是描述性彙總約定，不主張此量表是等距量表，也不主張具有常模、信
度、效度或可加權的潛在能力分數。合計與平均不得被解讀為客觀能力總量。
7. 雷達圖資料規格與替代表格
7.1 圖表資料
表 7-1｜SAMPLE／SYNTHETIC：五軸雷達圖資料（n=8；固定 0–4）
軸／維度 前測平均 後測平均 差異
A 來源事實與情境 2.125 3.125 +1.000
B 紀錄完整性與可追溯 2.000 3.000 +1.000
C 任務與產出對應 1.625 2.750 +1.125
D 資料最小化與隱私意識 1.750 3.000 +1.250
E 後續行動規劃 1.875 2.750 +0.875
此表就是雷達圖的數值來源。圖形只畫五個維度的前後平均，不畫 80 個個別分數格，也不把維度合計直
接畫在同一軸上。
7.2 原生 Word 圖表規格
屬性 設定
圖表類型 雷達圖（radar chart），含資料標記；不使用 3D、透視或立體效果
類別順序 A → B → C → D → E，順時針排列，A 置於上方起始位置

===== WORD PDF PAGE 13 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 13 頁
屬性 設定
軸標籤
五個完整繁體中文標籤：來源事實與情境、紀錄完整性與可追溯、任務與產出對應、
資料最小化與隱私意識、後續行動規劃
系列 1 前測自評平均（SAMPLE）
系列 2 後測自評平均（SAMPLE）
數值 前測：2.125、2.000、1.625、1.750、1.875；後測：3.125、3.000、2.750、3.000、
2.750
徑向軸 最小值 0、最大值 4、主要刻度間隔 1；刻度為 0、1、2、3、4
網格 淺色、低對比；不得遮住線條或標籤
圖例 置於圖下方或右側空白區，完整顯示兩個系列；不得與圖說分離
標記 前後系列使用不同形狀與線型，不能只靠顏色區分
資料標籤 預設關閉以免擁擠；若顯示，固定三位小數，且不得取代表 7-1
標題 SAMPLE／SYNTHETIC：五維度前後自評平均（n=8；0–4 分）
圖說 見 7.3；圖說與圖不得跨頁分離
來源註
「來源：0100 R09 合成 fixture；所有數值為 SAMPLE／SYNTHETIC；n=8；描述性統
計。」
可讀性 圖內文字至少 9.5 pt；軸標籤不得裁切、旋轉到難以閱讀或只剩英文縮寫

===== WORD PDF PAGE 14 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 14 頁
7.3 圖說與可及性替代文字
圖 1｜SAMPLE／SYNTHETIC：學員五維度訓練前後自評平均雷達圖（n=8；0–4 分；描述性）
圖例：前測自評平均（SAMPLE）；後測自評平均（SAMPLE）。
替代文字：
五軸雷達圖，n=8，固定 0–4 分。前測平均依 A 至 E 為 2.125、2.000、1.625、1.750、1.875；後測平
均為 3.125、3.000、2.750、3.000、2.750；差異為 +1.000、+1.000、+1.125、+1.250、+0.875。圖
形只呈現合成自評平均，不呈現個別學員、客觀技能或統計顯著性。
可及性表格替代：表 7-1 已列出每個軸的前測、後測與差異；即使圖形未顯示或讀者無法辨識顏色，仍可
從表格取得完整數值。
7.4 圖形解讀邊界
• 五軸的徑向尺度固定為 0–4；不可因資料範圍縮放而改變軸的意義。
• 雷達圖多邊形面積不是效果量、不是能力總分、不是進步幅度，也不是統計檢定結果。
• 五個軸是不同構念，沒有共同單位與權重；軸的排列順序會改變多邊形形狀與面積，因此面積不可比
較。
• 前後系列的平均差只能用來看這組合成資料的數值位置；不能說「面積變大代表能力提升」。
• 圖形不得省略 n=8、SAMPLE 標記、圖例或 0–4 刻度。
• 不得把 0099 的技能門檻畫成同一張圖的參考線，也不得把 14/20 轉成此圖的通過區。

===== WORD PDF PAGE 15 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 15 頁
8. 維度解讀與自評邊界
8.1 逐維度數值解讀
表 8-1｜SAMPLE／SYNTHETIC：五維度算術觀察
維度 前測平均 後測平均 平均差 數字層級的解讀
A 來源事實與情境 2.125 3.125 +1.000
後測平均為五維最高（3.125）；與 B 
同為 +1.000。這是群體平均，不能推論
每位學員都達到 3 分以上。
B 紀錄完整性與可追溯 2.000 3.000 +1.000
合成平均由 2.000 到 3.000；數值上增
加 1.000。不得寫成「紀錄能力已達
標」。
C 任務與產出對應 1.625 2.750 +1.125
前測平均為五維最低（1.625）；後測
平均 2.750，仍低於 3.000。這個位置只
是此組合成分數的算術事實。
D 資料最小化與隱私意識 1.750 3.000 +1.250
平均差 +1.250，為五維最大；但不能解
讀為「隱私能力進步最多」或訓練效果
最大。
E 後續行動規劃 1.875 2.750 +0.875
平均差 +0.875，為五維最小；不能解讀
為「後續規劃最無效」或「訓練沒有幫
助」。
所有數值都是 0–4 自評分的群體平均。平均 3.125 不代表每位學員都是 3 或 4；平均差 +1.250 也不代表每
個人都增加 1.250。
8.2 最大與最小變化
在五個維度中，D 的算術平均差最大（+1.250），E 的算術平均差最小（+0.875）。A 與 B 同為 +1.000，
C 為 +1.125。這個排序只描述本合成 fixture 的數字：
• 不是統計顯著性排序。
• 不是效果量或實務重要性排序。
• 不是因果推論，不能說訓練造成 D 的變化最大。
• 不是能力優劣排序，不能說 D 比其他維度「更重要」或「更成功」。
• 不代表真實學員、真實課程或母體會出現相同模式。
n=8、無對照組、無隨機分派、無抽樣架構、無信效度資料，且數值為合成自評值，因此本報告不做檢定、
不計算信賴區間、不宣稱顯著或因果。
8.3 自評與實作能力的區隔
本報告所稱的「自評」是學員依 0–4 錨點，對自己在某一時刻「主觀上能做到多少」的判斷。它不等於：

===== WORD PDF PAGE 16 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 16 頁
• 受過訓練的評分者對實際作品或任務表現的評分。
• 客觀測驗、技能檢定、工作樣本或通關門檻。
• 講師觀察、同儕評分或管理者績效考核。
• 學習遷移、行為改變或組織績效。
即使真實前後測平均上升，也可能受題意理解、作答風格、期待、記憶、社會讚許、重複施測或課程期待
影響；本報告沒有設計可排除這些替代解釋。0–4 錨點文字是填答提示，不是已驗證的行為觀察規準。
若未來要討論「實作能力」，必須另以獲授權的客觀任務、明確評分規準、合格評分者與可追溯紀錄進行；
該客觀資料不得直接併入本報告的自評分數，也不得借用 0099 的 14/20 或任何技能通過門檻。
9. 建議後續工作流程
以下流程是建議程序，不是已完成的事實。角色名稱是一般性建議，不代表已被指派、已同意或已存在；
任何實際決定仍須由適用機構依其程序授權。
9.1 建議角色
建議角色 建議責任 不可做的事
文件持有人／課程承辦窗口
確認實際使用的 0100 問卷版次及版本號，保
管來源表單，維持配對代碼控制並確認場次。
不得代填、代選代碼或修改分數
表單／題項審查者 檢查題意、錨點、版本與填答說明是否一致 不得把理解測試當成訓練成效證據
資料管理者 去識別收件、權限控管、分開保管對照資訊
不得把姓名、電話或名冊併入分析
檔
表單檢核者
逐份檢查完整性、配對、版本、日期與 HOLD
／REJECT
不得替任何缺漏補值
分析者
重算 80 格、總分、維度統計、分母與圖表資
料
不得直接手改衍生值或挑選有利結
果
第二核算者 獨立重算與比對差異 不得與分析者共用未揭露的暫存值
獨立審查者
按本報告版次完成語意、算術與 Word 呈現審
查。
不得在未審查時簽署或背書
機構權責主管 在機構程序允許時授權真實資料使用與釋出 不得以本候選稿代替正式核定
9.2 流程、觸發條件與責任
步驟 建議角色 觸發條件 建議工作與產出 停止／HOLD 條件
1. 凍結表單版本 文件持有人 準備使用 0100 前
確認問卷版次、題目與評
分錨點一致，並記錄使用
版本。
版本或題目不一致時分開
分析，不得直接合併。

===== WORD PDF PAGE 17 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 17 頁
步驟 建議角色 觸發條件 建議工作與產出 停止／HOLD 條件
2. 驗證題意理解
題項審查者、
承辦窗口
第一次真實施測前
以獲授權的小型認知訪談
或說明測試檢查五題與
0–4 錨點是否被理解；記
錄修訂需求
無授權、無隱私安排或題
意仍不清楚時，不得開始
正式蒐集
3. 真實施測與配
對控制
承辦窗口、資
料管理者
機構核准辦理且隱私流
程就緒
前後測使用同版本、同配
對代碼；名冊與分數分開
保管；當場檢查完整性
缺漏、重複代碼、版本不
符或個資外洩風險即
HOLD
4. 收回與檢核
表單檢核者、
資料管理者
表單收回後
逐份檢核真實回應、登錄
納入／排除／留置份數與
原因
未揭露分母、未解決重複
或無法配對時，不得進入
分析
5. 建檔與獨立重
算
分析者、第二
核算者
檢核完成且資料集凍結
建立去識別資料集；重算
每列總分、維度合計、整
體統計與圖表值
任一加總或分母不一致即
整批 HOLD
6. 產出統計與圖
表
分析者 資料集通過檢核
依表 6-1、表 6-2、表 7-1 
產生報告與固定 0–4 雷達
圖
n、排除數、圖例或軸標
籤不完整即不得釋出
7. 視需要進行客
觀實作任務
課程權責人、
合格評分者
另有書面授權且具獨立
評分規準
以獨立任務觀察實際表
現；另立資料集與分析，
不併入 0100 自評分數
未授權、無規準、無評分
者訓練時不得執行或宣稱
8. 日後比較真實
紀錄
分析者、獨立
審查者
有足夠且合法的真實配
對資料，並事先指定分
析計畫
分開報告樣本、排除、前
後分布與不確定性；必要
時才使用推論方法
設計不足或資料品質不明
時，只做描述，不做因果
或顯著性宣稱
9. 審查與釋出
獨立審查者、
機構權責主管
文件與資料凍結
依報告版次完成語意、算
術與 Word 呈現審查；依
程序填寫審查與核准欄。
未完成審查、未經授權或
仍有 SAMPLE 殘留時，維
持 HOLD
9.3 未來真實資料的比較原則
未來若取得真實且合法的前後配對資料，報告至少應揭露：納入對數、排除對數與原因、每維度分母、前
後分布、平均差、缺漏處理與圖表尺度。不得只報總分或只報漂亮的百分比。
若考慮推論統計，必須在分析前指定方法、檢查假設、處理配對結構並報告不確定性；不得因為看到數字
上升就事後選擇檢定。以目前 n=8 的合成 fixture，不進行顯著性檢定，也不提供母體推論。
若另行執行客觀實作任務，應使用獨立同意、獨立規準與獨立資料檔；可與自評結果並列討論，但不得把
兩者合併成一個未定義的「能力分數」，也不得把 0099 的技能門檻移入本報告。

===== WORD PDF PAGE 18 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 18 頁
10. 留置／退件準則、SAMPLE 替換與定位登錄
10.1 精確 HOLD／REJECT 準則
表 10-1｜使用前與分析前的留置／退件判定
條件 判定 必要處理 是否可補正
前測或後測缺少其中一份 HOLD
尋找同一配對代碼的另一份；不得以其他學員或平均數替
代
可，限本人補件
任一維度空白 HOLD 請本人補填；不得以 0、平均、前測值或推估值代入 可，限本人補正
同一題勾選兩個以上分數 HOLD 請本人重選一個；承辦人不得代選 可，限本人重選
分數超出 0–4 或非整數 HOLD 核對原表並更正；不得截斷或四捨五入 可，限有原始依據
同階段出現重複配對代碼 HOLD 同代碼全部表單留置；不得挑一份計分 僅在本人可安全確認時
重複代碼無法安全確認歸屬 REJECT 全部相關表單排除，揭露於分母 不可
前後測代碼不一致 HOLD 未經本人確認不得配對；確認後更正並留註記 可，限本人確認
前後測版本不一致 REJECT 該對不得併入分析 不可
前後測課程代碼或場次不一致 REJECT 不得跨課程配對 不可
後測日期早於前測 REJECT 查明後重填；不得倒填日期 不可
表單含姓名、電話、證件號或其他直接識別 HOLD 立即遮蔽或換碼；必要時重填 可，完成去識別後
承辦人代填、代選或代改分數 REJECT 該份作廢並記錄程序違失 不可
0100 問卷版本或前後配對來源無法確認 HOLD 停止整批分析並重新綁定 可，完成來源確認後
未揭露有效分母或排除份數 HOLD 不得釋出最終報告 可，補齊揭露後
核心原則：不補值、不代選、不挑份、不隱藏分母。HOLD 與 REJECT 的份數、原因和處理日期都必須與有效份數一起揭露。

===== WORD PDF PAGE 19 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 19 頁
10.2 真實資料替換檢查清單
以下為正式使用前的必要步驟；本候選稿尚未執行，不得預先勾選為完成。
• ☐ 確認真實資料的使用目的、權限、告知與隱私程序已由適用機構核准。
• ☐ 凍結實際使用的 0100 問卷版次與版本號；如前測、後測版本不同，分開統計並更新配對與重算紀錄。
• ☐ 確認分析對象是已完成、已檢核的真實前後測表單，不是空白表、草稿或合成資料。
• ☐ 登錄收到、納入、排除、HOLD 與 REJECT 的份數及原因，確認有效分母。
• ☐ 以去識別分析編號取代 A01–A08；不得在報告公開原始配對碼；A01–A08 僅為合成代碼，對照資訊由單一窗口分開保管。
• ☐ 以真實表單替換全部 80 個原始分數格；任一格缺漏先 HOLD，不以 0、平均或前測值補值。
• ☐ 核對每對的前後代碼、版本、課程、日期、五題完整性與 0–4 範圍。
• ☐ 重算每一對的前總分、後總分與變化；不得手動改寫衍生值。
• ☐ 重算五維度前後合計、平均、差異、整體總分、平均與正規化顯示。
• ☐ 重新產生表 7-1 與圖 1；確認五軸中文標籤、固定 0–4、圖例、n 與 SAMPLE 標記（若尚未替換）正確。
• ☐ 更新所有分母、排除說明與限制段落；不得只改表格數字而不改敘述。
• ☐ 由第二人獨立重算並比對；差異未解釋前不得釋出。
• ☐ 完成 DOCX 的 Word 視覺檢查：A4 混合頁面方向（正文直向、寬表橫向）、正文至少 10.5 pt、表格至少 9.5 pt、無裁切、無空白頁、表格跨頁有重複表頭、圖
說不與圖分離。
• ☐ 由獨立審查者依本報告所示版次完成語意、算術與 Word 呈現檢查；未完成前維持 HOLD。
• ☐ 只有在真實替換、重算、審查與機構授權都完成後，才可移除 SAMPLE／SYNTHETIC 標記；限制聲明仍須保留「自評、描述性、非客觀技能」的性質。
• ☐ 準備、審查、核准欄僅在實際完成時填寫；不得以角色、職稱或推定補簽。
• ☐ 封存替換登錄、排除清單、重算紀錄及來源版本紀錄；不得將可識別個資留在報告或公開資料夾。
10.3 合成欄位替換登錄
以下右欄是未來替換要求，不是已完成事項。所有 SAMPLE 欄位在真實使用前都必須處理。

===== WORD PDF PAGE 20 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 20 頁
表 10-2｜SAMPLE 欄位、位置、替換來源、驗證與 HOLD 動作
ID 目前 SAMPLE 欄位／值 文件／表／圖位置 真實替換來源 必要驗證 HOLD 動作
S-01 辦理單位：SAMPLE 示範訓練機構 §3.4 表 3-2 經授權的機構名稱與課程主檔
與核准課程紀錄一致；不
得自行推定
未確認前 HOLD 報告
S-02 課程代碼：SAMPLE-CRS-0100 §1.2、§3.4 表 3-2 機構正式課程代碼
與場次、表單預印代碼一
致
不一致則 HOLD／REJECT 受影響
配對
S-03
課程名稱：SAMPLE「資料紀錄與
隱私基礎示範課」
§1.2、§3.4 表 3-2 正式課程名稱 與課程主檔及表單一致 未確認前 HOLD
S-04 前測日期：2026-11-02 §1.2、§3.4 表 3-2 真實前測日期紀錄 與表單及場次紀錄一致 缺漏或矛盾則 HOLD
S-05 後測日期：2026-11-02 §1.2、§3.4 表 3-2 真實後測日期紀錄
不得早於前測；與場次一
致
早於前測則 REJECT
S-06 問卷版本：SR-0100-v1.0-
SAMPLE
§1.2、§3.4 表 3-2、§4.1 機構核定之問卷版本
前後測完全相同；與實際
表單一致
不一致則 REJECT 該對
S-07 配對識別：A01–A08 §5 表 5-1、§10.5
去識別分析編號；原始配對代碼另
由單一窗口保管
唯一、可配對、不得含個
資
重複或無法配對則 HOLD；未解
REJECT
S-08 80 個原始分數格 §5 表 5-1、§10.5
8 對已完成且檢核通過的真實 0100 
前後表單
V1–V4、V6；每格不得補
值
任一格失敗則 H1／H4；未解 H3
S-09
8 對前總分、後總分、變化（24 個
值）
§5 表 5-1、§10.6
不得人工替換；由 S-08 以固定公
式重算
V5；逐列核對 H2／H4
S-10
五維度合計、平均、差異（25 個
值）
§6 表 6-1、§7 表 7-1、圖 1、§10.7 由 S-08 重算，不由舊稿沿用 V5；維度交叉合計 H2／H4
S-11 整體總分、平均、淨變化 §2 表 2-1、§6 表 6-2、§10.8 由 S-08／S-09 重算 V5；三種算法交叉核對 H2
S-12
正規化 46.875%／73.125%／
+26.25 個百分點
§2、§6.2、§10.8
由真實總分除以 20（群體除以
160）重算
V5；不得沿用合成百分比 H2

===== WORD PDF PAGE 21 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 21 頁
ID 目前 SAMPLE 欄位／值 文件／表／圖位置 真實替換來源 必要驗證 HOLD 動作
S-13
雷達圖資料與圖說（前後系列、
n=8、SAMPLE）
§7 表 7-1、圖 1、§10.8 由 S-10 的真實維度平均重新產生
V5、V7；軸、圖例、尺
度、標籤
H2／H4
S-14 SAMPLE 邊界文字、限制與警告 全篇、§1、§12
真實審查後改為正式版本文字，但
保留「自評、描述性、非客觀技
能」限制
V7；不得刪除核心限制 未完成替換前 HOLD 全篇
S-15 準備／審查／核准空白欄 §1.4、§12.1 實際完成的人員、日期與機構紀錄 僅依真實簽核資料填寫 無紀錄則保持空白並 HOLD 釋出
10.4 定位代碼與核對代碼
為使每一格可追溯，本報告使用下列定位規則：
• T5-1/A01/前 A 表示表 5-1 中 A01 的前測 A 維度格；其他原始格依此類推。
• T6-1/A/前合計 表示表 6-1 中 A 維度的前測合計。
• T7-1/A/前平均 表示表 7-1 中 A 軸的前測平均。
• FIG1 表示第 7.3 節的圖 1；其數值只讀取 T7-1，不另存一份數值。
• T2-1、T6-2 分別表示第 2 節與第 6.2 節的整體統計表。
核對代碼：
• V1：官方來源、問卷版本與本報告使用界線一致。
• V2：前後配對代碼、課程／場次一致。
• V3：五個維度齊全，分數為 0–4 整數。
• V4：階段、日期順序與重複代碼檢查完成。
• V5：由原始值重新計算總分、差異、平均與百分比。
• V6：已完成去識別，無直接個資。

===== WORD PDF PAGE 22 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 22 頁
• V7：第二人獨立核對／視覺檢查。
HOLD 代碼：
• H1：該對 HOLD，暫不納入。
• H2：報告 HOLD，暫不釋出。
• H3：該對 REJECT，排除於有效分母。
• H4：所有引用該值的表格、圖形與摘要一併 HOLD。
替換來源代碼：
• SRC-A01-P：將取代 A01 的真實前測表單（同一版本、同一課程、已完成檢核、去識別處理）。
• SRC-A01-Q：將取代 A01 的真實後測表單。
• 其他配對依此類推。候選稿不列出任何真實代碼或可識別資訊。
10.5 80 個原始分數格的定位
SAMPLE／SYNTHETIC 80 格定位（不是真實資料）
下列每一列皆為一個原始分數格；value 是目前合成值。驗證失敗時，先依 H1／H4 留置該對及引用表圖；若無法補正，轉 H3。
locator value source verify hold
T5-1/A01/前 A 2 SRC-A01-P V1/V2/V3/V4/V6 H1/H4
T5-1/A01/前 B 2 SRC-A01-P V1/V2/V3/V4/V6 H1/H4
T5-1/A01/前 C 1 SRC-A01-P V1/V2/V3/V4/V6 H1/H4
T5-1/A01/前 D 2 SRC-A01-P V1/V2/V3/V4/V6 H1/H4
T5-1/A01/前 E 1 SRC-A01-P V1/V2/V3/V4/V6 H1/H4
T5-1/A01/後 A 3 SRC-A01-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A01/後 B 3 SRC-A01-Q V1/V2/V3/V4/V6 H1/H4

===== WORD PDF PAGE 23 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 23 頁
locator value source verify hold
T5-1/A01/後 C 3 SRC-A01-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A01/後 D 3 SRC-A01-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A01/後 E 3 SRC-A01-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A02/前 A 2 SRC-A02-P V1/V2/V3/V4/V6 H1/H4
T5-1/A02/前 B 2 SRC-A02-P V1/V2/V3/V4/V6 H1/H4
T5-1/A02/前 C 2 SRC-A02-P V1/V2/V3/V4/V6 H1/H4
T5-1/A02/前 D 2 SRC-A02-P V1/V2/V3/V4/V6 H1/H4
T5-1/A02/前 E 2 SRC-A02-P V1/V2/V3/V4/V6 H1/H4
T5-1/A02/後 A 3 SRC-A02-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A02/後 B 3 SRC-A02-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A02/後 C 3 SRC-A02-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A02/後 D 3 SRC-A02-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A02/後 E 4 SRC-A02-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A03/前 A 3 SRC-A03-P V1/V2/V3/V4/V6 H1/H4
T5-1/A03/前 B 2 SRC-A03-P V1/V2/V3/V4/V6 H1/H4
T5-1/A03/前 C 2 SRC-A03-P V1/V2/V3/V4/V6 H1/H4
T5-1/A03/前 D 2 SRC-A03-P V1/V2/V3/V4/V6 H1/H4
T5-1/A03/前 E 2 SRC-A03-P V1/V2/V3/V4/V6 H1/H4
T5-1/A03/後 A 3 SRC-A03-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A03/後 B 3 SRC-A03-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A03/後 C 3 SRC-A03-Q V1/V2/V3/V4/V6 H1/H4

===== WORD PDF PAGE 24 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 24 頁
locator value source verify hold
T5-1/A03/後 D 3 SRC-A03-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A03/後 E 2 SRC-A03-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A04/前 A 2 SRC-A04-P V1/V2/V3/V4/V6 H1/H4
T5-1/A04/前 B 2 SRC-A04-P V1/V2/V3/V4/V6 H1/H4
T5-1/A04/前 C 1 SRC-A04-P V1/V2/V3/V4/V6 H1/H4
T5-1/A04/前 D 2 SRC-A04-P V1/V2/V3/V4/V6 H1/H4
T5-1/A04/前 E 2 SRC-A04-P V1/V2/V3/V4/V6 H1/H4
T5-1/A04/後 A 3 SRC-A04-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A04/後 B 3 SRC-A04-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A04/後 C 2 SRC-A04-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A04/後 D 3 SRC-A04-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A04/後 E 2 SRC-A04-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A05/前 A 3 SRC-A05-P V1/V2/V3/V4/V6 H1/H4
T5-1/A05/前 B 3 SRC-A05-P V1/V2/V3/V4/V6 H1/H4
T5-1/A05/前 C 2 SRC-A05-P V1/V2/V3/V4/V6 H1/H4
T5-1/A05/前 D 2 SRC-A05-P V1/V2/V3/V4/V6 H1/H4
T5-1/A05/前 E 2 SRC-A05-P V1/V2/V3/V4/V6 H1/H4
T5-1/A05/後 A 4 SRC-A05-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A05/後 B 4 SRC-A05-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A05/後 C 3 SRC-A05-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A05/後 D 3 SRC-A05-Q V1/V2/V3/V4/V6 H1/H4

===== WORD PDF PAGE 25 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 25 頁
locator value source verify hold
T5-1/A05/後 E 4 SRC-A05-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A06/前 A 1 SRC-A06-P V1/V2/V3/V4/V6 H1/H4
T5-1/A06/前 B 2 SRC-A06-P V1/V2/V3/V4/V6 H1/H4
T5-1/A06/前 C 1 SRC-A06-P V1/V2/V3/V4/V6 H1/H4
T5-1/A06/前 D 1 SRC-A06-P V1/V2/V3/V4/V6 H1/H4
T5-1/A06/前 E 2 SRC-A06-P V1/V2/V3/V4/V6 H1/H4
T5-1/A06/後 A 3 SRC-A06-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A06/後 B 2 SRC-A06-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A06/後 C 2 SRC-A06-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A06/後 D 3 SRC-A06-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A06/後 E 2 SRC-A06-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A07/前 A 2 SRC-A07-P V1/V2/V3/V4/V6 H1/H4
T5-1/A07/前 B 2 SRC-A07-P V1/V2/V3/V4/V6 H1/H4
T5-1/A07/前 C 2 SRC-A07-P V1/V2/V3/V4/V6 H1/H4
T5-1/A07/前 D 2 SRC-A07-P V1/V2/V3/V4/V6 H1/H4
T5-1/A07/前 E 2 SRC-A07-P V1/V2/V3/V4/V6 H1/H4
T5-1/A07/後 A 3 SRC-A07-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A07/後 B 3 SRC-A07-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A07/後 C 3 SRC-A07-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A07/後 D 3 SRC-A07-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A07/後 E 3 SRC-A07-Q V1/V2/V3/V4/V6 H1/H4

===== WORD PDF PAGE 26 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 26 頁
locator value source verify hold
T5-1/A08/前 A 2 SRC-A08-P V1/V2/V3/V4/V6 H1/H4
T5-1/A08/前 B 1 SRC-A08-P V1/V2/V3/V4/V6 H1/H4
T5-1/A08/前 C 2 SRC-A08-P V1/V2/V3/V4/V6 H1/H4
T5-1/A08/前 D 1 SRC-A08-P V1/V2/V3/V4/V6 H1/H4
T5-1/A08/前 E 2 SRC-A08-P V1/V2/V3/V4/V6 H1/H4
T5-1/A08/後 A 3 SRC-A08-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A08/後 B 3 SRC-A08-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A08/後 C 3 SRC-A08-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A08/後 D 3 SRC-A08-Q V1/V2/V3/V4/V6 H1/H4
T5-1/A08/後 E 2 SRC-A08-Q V1/V2/V3/V4/V6 H1/H4
10.6 配對總分與變化的定位
表 10-3｜SAMPLE／SYNTHETIC：8 對總分與變化的定位映射
配對 前總分定位＝值 後總分定位＝值 變化定位＝值
A01 T5-1/A01/前總分＝8 T5-1/A01/後總分＝15 T5-1/A01/變化＝+7
A02 T5-1/A02/前總分＝10 T5-1/A02/後總分＝16 T5-1/A02/變化＝+6
A03 T5-1/A03/前總分＝11 T5-1/A03/後總分＝14 T5-1/A03/變化＝+3
A04 T5-1/A04/前總分＝9 T5-1/A04/後總分＝13 T5-1/A04/變化＝+4
A05 T5-1/A05/前總分＝12 T5-1/A05/後總分＝18 T5-1/A05/變化＝+6
A06 T5-1/A06/前總分＝7 T5-1/A06/後總分＝12 T5-1/A06/變化＝+5

===== WORD PDF PAGE 27 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 27 頁
配對 前總分定位＝值 後總分定位＝值 變化定位＝值
A07 T5-1/A07/前總分＝10 T5-1/A07/後總分＝15 T5-1/A07/變化＝+5
A08 T5-1/A08/前總分＝8 T5-1/A08/後總分＝14 T5-1/A08/變化＝+6
這 24 個值全部由表 5-1 的原始格重算；驗證代碼 V5，失敗時 H2／H4。不得以人工方式只替換總分而不替換原始格。
10.7 五維度統計的定位
表 10-4｜SAMPLE／SYNTHETIC：維度合計、平均與差異的定位映射
維度 前合計 前平均 後合計 後平均 差異
A T6-1/A/前合計＝17 T6-1/A/前平均＝2.125 T6-1/A/後合計＝25 T6-1/A/後平均＝3.125 T6-1/A/差＝+1.000
B T6-1/B/前合計＝16 T6-1/B/前平均＝2.000 T6-1/B/後合計＝24 T6-1/B/後平均＝3.000 T6-1/B/差＝+1.000
C T6-1/C/前合計＝13 T6-1/C/前平均＝1.625 T6-1/C/後合計＝22 T6-1/C/後平均＝2.750 T6-1/C/差＝+1.125
D T6-1/D/前合計＝14 T6-1/D/前平均＝1.750 T6-1/D/後合計＝24 T6-1/D/後平均＝3.000 T6-1/D/差＝+1.250
E T6-1/E/前合計＝15 T6-1/E/前平均＝1.875 T6-1/E/後合計＝22 T6-1/E/後平均＝2.750 T6-1/E/差＝+0.875
雷達圖的 10 個系列值直接等於上表的前平均與後平均，不另存獨立數值：
圖表資料 A B C D E
T7-1/前平均 2.125 2.000 1.625 1.750 1.875
T7-1/後平均 3.125 3.000 2.750 3.000 2.750
FIG1 只讀取 T7-1；若維度值變動，必須同時重繪圖 1、更新圖說與替代文字。所有維度值驗證代碼 V5，失敗時 H2／H4。

===== WORD PDF PAGE 28 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 28 頁
10.8 整體統計與正規化的定位
表 10-5｜SAMPLE／SYNTHETIC：整體與正規化值的定位映射
指標 定位＝值 重算依據 HOLD
前總分 T2-1；T6-2/前總分＝75 八對前總分合計 H2
後總分 T2-1；T6-2/後總分＝117 八對後總分合計 H2
淨變化 T2-1；T6-2/淨變化＝+42 117 − 75 H2
前平均 T2-1/前平均＝9.375／20 75 ÷ 8 H2
後平均 T2-1/後平均＝14.625／20 117 ÷ 8 H2
平均每人變化 T2-1/平均變化＝+5.25／20 42 ÷ 8；或 14.625 − 9.375 H2
正規化前 T2-1；T6-2/正規化前＝46.875% 9.375 ÷ 20；群體 75 ÷ 160 H2
正規化後 T2-1；T6-2/正規化後＝73.125% 14.625 ÷ 20；群體 117 ÷ 160 H2
正規化差 T2-1；T6-2/正規化差＝+26.25 個百分點 73.125 − 46.875 H2
n T2-1/n＝8 納入配對數 H2
原始格數 T2-1/原始格數＝80 8 × 5 × 2 H2
圖 1 系列 FIG1／T7-1/前平均、FIG1／T7-1/後平均 直接等於表 10-4 的平均 H2／H4
所有整體與正規化值都必須由替換後的原始值重算，不得沿用本稿的合成數字，也不得只改百分比而保留舊總分。

===== WORD PDF PAGE 29 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 29 頁
11. 盲標題邊界矩陣
盲標題測試不能只看檔名。至少要用五個線索判定：需求編號、產物類型、分析單位、輸出型態、來源綁
定。以下矩陣用來避免把 0097、0098、0099、0100 與 0101 互相替換。
表 11-1｜五份文件的盲標題邊界
文件／需求 產物類型 分析單位 核心構念 主要輸出 盲測辨識指紋 不可回答的問題
0097／I18-
E05
知覺／看法
調查
填答者對
某對象的
知覺
知覺、意見
或看法
知覺結果彙總
以知覺題為主；沒
有前後自評配對、
沒有技能規準、沒
有五軸成長雷達
不能當成 0100 的
前後自評、不能當
成技能評分或滿意
度
0098／I18-
E06
滿意度調查
對課程或
服務的滿
意感受
滿意度 滿意度統計與回饋
滿意度題項；不是
能力自評、不是技
能評分、不是前後
雷達
不能證明學習、能
力提升或訓練成效
0099／I18-
E07
技能工作／
評分規準
作品或任
務表現
以其規準定
義的技能表
現
技能評分、評分規
準與其自身門檻
（含 14/20）
有評分者、
rubric、作品或任
務；有技能通過概
念
不能把 0101 的自
評分數混入；不能
宣稱一致性、相關
或互換
0100／I18-
E08
可填寫表單
／資料蒐集
工具
每位學員
的前後配
對
五維度自覺
能力（0–
4）
空白題頁、配對欄
位、80 格原始資料
有勾選欄、前測／
後測頁、五題與版
本欄；是表單不是
彙總報告
不是聚合分析、不
是雷達圖結論、不
是技能證據
0101／I18-
E08
聚合描述性
報告
8 對合成配
對（本
稿）
自覺改變的
群體描述
75／117／+42、五
維平均、固定 0–4 
雷達圖與替換登錄
有 n、分母、80 格
映射及雷達圖；是
聚合報告，不是配
套表單。
不是技能評分、不
是因果效果、不是
0099 的替代品
盲測時可依下列順序判定：
1. 若看到空白勾選欄、前後測頁、五題與版本欄，先判定為 0100，不是 0101。
2. 若看到 8 對、80 格、75／117／+42、五軸雷達圖與分母揭露，判定為 0101。
3. 若看到評分者、rubric、作品評分或 14/20，判定為 0099；不得把該門檻移入 0101。
4. 若主體是滿意度，判定為 0098；若是知覺或看法調查，判定為 0097。
5. 0100 與 0101 雖同為 I18-E08，但前者是表單與資料蒐集，後者是聚合報告；同一需求不代表可互相代
替。

===== WORD PDF PAGE 30 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 30 頁
12. 使用前檢核與來源／範圍聲明
12.1 最終使用前檢核表
以下檢核項供正式釋出前逐項核對。候選版次、技術、視覺與獨立語意品質檢查應另行留存；本文件不代
替權責人員的核准，未由權責人員依證據核對的項目不得勾選。
A. 識別與來源
• ☐ 文件標題、DOC_ID 0101、需求 I18-E08、R09 候選版次與稿件日期正確。
• ☐ 官方印刷序號維持 UNKNOWN；未以其他清單序號代替。
• ☐ 配套 0100 表單的名稱、內頁版次及問卷版本一致；該表單仍是候選文件，尚未正式接受。
• ☐ 官方來源用途、配套表單題目與版本、示範資料範圍及相鄰文件用途已分別核對。
• 候選文件的檢查狀態須依實際查核結果填寫；本表不得預先勾選。
B. 資料與算術
• ☐ 納入 8 對、80 個原始分數格；全部為 0–4 整數。
• ☐ 前總分 75、後總分 117、淨變化 +42，且逐列與維度交叉核對一致。
• ☐ 前平均 9.375／20、後平均 14.625／20、平均變化 +5.25／20。
• ☐ 五維度：A 17／25、B 16／24、C 13／22、D 14／24、E 15／22；平均差分別為 +1.000、+1.000、
+1.125、+1.250、+0.875。
• ☐ 正規化 46.875%／73.125%／+26.25 個百分點只作為顯示，且有揭露分母。
• ☐ 未使用 0099 的 14/20、技能門檻或通過率。
• ☐ 未以 0、平均數、前測值或其他方式補值。
• ☐ 有效分母、排除份數與 HOLD／REJECT 原因均已揭露。
C. 圖表與可及性
• ☐ 雷達圖五軸均為完整繁體中文標籤，固定 0–4，刻度 0、1、2、3、4。
• ☐ 前測與後測兩系列及圖例清楚，並標示 n=8 與 SAMPLE／SYNTHETIC。
• ☐ 圖 1 具備 n=8、SAMPLE／SYNTHETIC、前後系列圖例、完整圖說與替代文字；圖說不與圖分離。
• ☐ 五軸標籤完整可讀，未被裁切、縮成英文縮寫或旋轉到難以辨識。
• ☐ 徑向軸固定 0–4，刻度為 0、1、2、3、4；未因資料範圍而改動尺度。
• ☐ 表 7-1 可作為無圖環境的完整表格替代；其數值與表 6-1 一致。
• ☐ 未以多邊形面積、3D 效果或視覺面積暗示效果量、能力總分、統計顯著性或通過率。
D. 邊界與核准
• ☐ 全篇未把自評寫成客觀技能、訓練因果、學習成效、通過率、母體推論或機構績效。
• ☐ 未與 0099 做一致性、相關或門檻比較；未使用其 14/20 或任何技能通過標準。
• ☐ 未出現真實姓名、簽名、虛構核准、協會核定、真實課程辦理或真實學員結果。

===== WORD PDF PAGE 31 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 31 頁
• ☐ 準備／審查／核准欄仍為空白；僅在實際完成並留有紀錄後，依機構程序填寫。
• ☐ 盲標題邊界已依第 11 節檢查，0100 與 0101 未被互相代替。
E. 檔案與審查
• ☐ DOCX 採 A4 混合頁面方向（正文直向、寬表橫向）；正文至少 10.5 pt、表格至少 9.5 pt；無空白頁、
裁切、重疊或孤立圖說。
• ☐ 跨頁表格重複表頭；長表格未出現錯誤斷列或失去欄位標題。
• ☐ 所有頁面經 Word 視覺檢查；圖例、軸標籤、表格與替代文字均清楚可讀。
• ☐ 由獨立審查者依本稿版次完成語意、算術與 Word 呈現審查。
• ☐ 所有 SAMPLE 欄位均已替換，或仍保留在合法的示範版本；不得把殘留合成值當成真實結果。
• ☐ 替換登錄、排除清單、重算紀錄、來源版本及審查紀錄已妥善保存。
12.2 本稿目前狀態
狀態：SAMPLE／SYNTHETIC 候選 DOCX；未正式接受。
本文件已提供完整報告結構、表格、算術核對、圖表資料規格、HOLD／REJECT 規則、SAMPLE 替換登錄
與 80 格定位映射。候選版次及品質檢查結果另行記錄；本稿仍待以下真實條件：
• 真實 0100 完成表單與真實有效分母；
• 機構授權、正式核准或協會決定。
因此，本稿不得釋出為正式報告，也不得用於課程成效、學員能力、招生、補助、績效或認證宣告。
12.3 來源、範圍與不主張聲明
本文件是 DOC_ID 0101、需求 I18-E08 的 R09 SAMPLE／SYNTHETIC 候選報告，依據 TTQS 訓練機構版證
據資料表第 7 頁指標 18 編製，並以配套 0100 學員前後自評表作為同一示範案例的輸入。0100 內頁標示
R09a，問卷版本為 SR-0100-v1.0-SAMPLE；該表單仍為候選，尚未正式接受。
正式使用時，應以表單內頁版次及問卷版本辨識配套文件，確認前測與後測題目及評分錨點一致；本節所
有數值仍為 SAMPLE／SYNTHETIC。
此 0100 文件為候選，不是正式接受版本。本報告的 8 對、5 維度、2 階段、80 個原始分數格，全部是
SAMPLE／SYNTHETIC。與 0099 R17 共用數值僅是契約允許的跨文件示範 fixture；不是同一構念、不是獨
立實證資料、不是一致性或相關分析，也不代表真實課程、學員、機構或協會結果。
本報告只提供描述性算術與圖表規格：
• 前測總分 75；
• 後測總分 117；
• 淨變化 +42；
• 前測平均 9.375／20；

===== WORD PDF PAGE 32 =====
TTQS ONE ｜ 0101 自評統計與雷達圖分析
SAMPLE／SYNTHETIC 候選示範稿 • 0101 • 第 32 頁
• 後測平均 14.625／20；
• 平均每人變化 +5.25／20；
• 五維平均差為 A +1.000、B +1.000、C +1.125、D +1.250、E +0.875。
上述數值只描述這組合成自評資料。本報告不主張統計顯著性、因果效果、效果量、信效度、常模、通過
率、能力認證、訓練成效或母體推論。雷達圖面積不具效果量或能力總分意義；0–4 分數不是客觀技能分
數。
本報告不含任何真實姓名、參與者紀錄、簽名、核准、協會決定或實際訓練成果。未來若要以真實資料使
用，必須完成第 10 節的替換、重算、分母揭露、隱私檢核、獨立審查與機構授權；在此之前，所有
SAMPLE 欄位與限制文字均須保留。
12.4 版本與歷史邊界
版本／文件 狀態 邊界
0101 R09（本稿） 現行候選 DOCX 使用 8 對 × 5 維度 × 2 階段、80 格合成
fixture
0101 R08A／R08B／R08C 歷史稿
均為 1 人 × 6 維度之舊版；不得作為現行
模板、接受依據或數值來源
0100 R08 歷史稿 1 人 × 6 維度，與現行 8×5 契約不一致
0100 R09（內頁 R09a） 現行配套候選 候選文件；尚未正式接受。
0099 R17 另一需求 I18-E07 的文件
僅作為合成 fixture 重用來源；不修改、不
重新分類、不引入其技能門檻
報告結束。

## Technical and direct visual receipts; identity/scope evidence only
Technical:
{
  "receipt_id": "TTQS-I18E08-DOC0101-R09-FINAL9-TECHNICAL-QA-20261021",
  "doc_id": "0101",
  "requirement_id": "I18-E08",
  "official_checkbox_serial": "UNKNOWN",
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "verified_at_local": "2026-10-21T21:52:16.346886+08:00",
  "verification_scope": "Exact final8 DOCX SHA; OOXML integrity; body/table font minima; source and unique Blueprint hashes; 0100 remote candidate byte match; all 80 integer scores, totals, means, percentages and dimensions; all 80 locators; Word-native PDF; 32 rendered page PNG hashes; register schema/records; SAMPLE boundary and internal metadata scan. Does not establish REAL association performance or formal acceptance.",
  "checks": {
    "docx_zip_integrity": true,
    "docx_size_nonzero": true,
    "final9_exact_sha_matches_semantic_correction_receipt": true,
    "semantic_correction_is_wording_only_and_preserves_history": true,
    "word_export_receipt_binds_final9_docx_and_pdf": true,
    "owned_word_process_lifecycle_and_existing_pids_verified": true,
    "render_manifest_binds_final9_docx_and_pdf": true,
    "unique_blueprint_exact_hash": true,
    "source_packet_exact_hash": true,
    "0100_remote_readback_exact_sha_matches_companion": true,
    "human_facing_body_has_no_internal_ids_or_hashes": true,
    "document_identity_and_requirement": true,
    "sample_boundary_and_not_formally_accepted": true,
    "cross_reference_and_mixed_orientation_copy_corrected": true,
    "pairing_code_boundary_copy_corrected": true,
    "no_personal_identifier_columns": true,
    "embedded_radar_image_and_alt_text": true,
    "expected_table_count_27": true,
    "body_text_minimum_10_5pt_excluding_caption_style": true,
    "caption_text_minimum_9_5pt": true,
    "table_text_minimum_9_5pt": true,
    "eight_pairs_80_integer_scores_in_0_to_4": true,
    "all_80_values_match_0100_remote_bytes": true,
    "grand_totals_and_dimension_crossfoot": true,
    "derived_means_and_percentages_are_present": true,
    "80_unique_locator_rows": true,
    "locator_set_exactly_matches_8x5x2": true,
    "word_pdf_and_manifest_both_32_pages": true,
    "all_32_page_pngs_match_manifest": true,
    "no_blank_pdf_pages": true,
    "expected_12_landscape_20_portrait": true,
    "radar_chart_text_on_page_14": true,
    "pdf_contains_all_80_locator_ids": true,
    "replacement_register_95_rows": true,
    "replacement_register_required_columns_present": true,
    "replacement_register_all_required_fields_nonblank": true,
    "replacement_register_unique_fact_ids": true,
    "replacement_register_bound_to_font_register_repair": true
  },
  "details": {
    "minimum_fonts_pt": {
      "body_excluding_caption": 10.5,
      "caption": 9.5,
      "table": 9.5,
      "normal": 10.5
    },
    "locator_missing": [],
    "locator_extra": [],
    "docx_sha256": "56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68",
    "docx_bytes": 166586,
    "pdf_sha256": "27002fa5e60ba712be1e38952f04bd12ba64d04661fa34101f1e09462c3ce4b2",
    "pdf_bytes": 1081073,
    "render_manifest_sha256": "4de6b20e4ec0b3ed421f1a56704082f128bcf9fddd9dee9beb67a7dc3946f237",
    "page_count": 32,
    "landscape_pages": [
      10,
      18,
      19,
      20,
      21,
      22,
      23,
      24,
      25,
      26,
      27,
      28
    ],
    "table_count": 27,
    "scores_0101": {
      "A01": [
        2,
        2,
        1,
        2,
        1,
        3,
        3,
        3,
        3,
        3
      ],
      "A02": [
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        4
      ],
      "A03": [
        3,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        2
      ],
      "A04": [
        2,
        2,
        1,
        2,
        2,
        3,
        3,
        2,
        3,
        2
      ],
      "A05": [
        3,
        3,
        2,
        2,
        2,
        4,
        4,
        3,
        3,
        4
      ],
      "A06": [
        1,
        2,
        1,
        1,
        2,
        3,
        2,
        2,
        3,
        2
      ],
      "A07": [
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3
      ],
      "A08": [
        2,
        1,
        2,
        1,
        2,
        3,
        3,
        3,
        3,
        2
      ]
    },
    "scores_0100_remote_readback": {
      "A01": [
        2,
        2,
        1,
        2,
        1,
        3,
        3,
        3,
        3,
        3
      ],
      "A02": [
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        4
      ],
      "A03": [
        3,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        2
      ],
      "A04": [
        2,
        2,
        1,
        2,
        2,
        3,
        3,
        2,
        3,
        2
      ],
      "A05": [
        3,
        3,
        2,
        2,
        2,
        4,
        4,
        3,
        3,
        4
      ],
      "A06": [
        1,
        2,
        1,
        1,
        2,
        3,
        2,
        2,
        3,
        2
      ],
      "A07": [
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3
      ],
      "A08": [
        2,
        1,
        2,
        1,
        2,
        3,
        3,
        3,
        3,
        2
      ]
    },
    "pre_total": 75,
    "post_total": 117,
    "delta": 42,
    "dimension_pre": [
      17,
      16,
      13,
      14,
      15
    ],
    "dimension_post": [
      25,
      24,
      22,
      24,
      22
    ],
    "locator_rows": 80,
    "replacement_rows": 95,
    "minimum_pdf_page_chars": 580,
    "page_sha256": {
      "1": "3b034638006827f6c182a2218403fbf9acaab4fc2808c8ea163a1b69f1eeae3e",
      "2": "6716f2928be6ac8cc7071f4868c30a5b9b91cc065f746d3c1022d8f4450d9eb9",
      "3": "17a88b1133f16c99927b6305387e6c6b036a3efd3affd56835edc2e656db1af7",
      "4": "18cce6b6c98a7940a63365fcaf86ab0270d3e83e19052ce1d3a6b5bd1ac0c6c5",
      "5": "023434fd54e1923a3d3c176aad64dd75a7b2ec743539f7be066118ab215fcc6f",
      "6": "18dc93510c08b24616344027cd00864eb11b524a4387dece28bebd8db88270ec",
      "7": "5797740248d95f25b0e7aea12d26a89a05c335e6ada92e5d3261a1530dd57de3",
      "8": "a86d74e0ef72d15a3f257336d12403ef8cdcac3ed1104b2586ad74d68466ac3c",
      "9": "2502881739ccf9d54dd1990bd1dab1bd0340a4971c2c2ca8fc92836f6cfb49f9",
      "10": "2bd4828f09bbe9dab23288309dcda1b30653366ffe0c0ebe5bc446bd4d8c0a59",
      "11": "5bc2bbc946bce80df9f0d0ae8f9801302ee72601053cad1595c0e0e3f0a5028a",
      "12": "9ae8896d611065be2cb4b25e104c8be6cc3e06aeadfb7f4bfe938fa2ea59531c",
      "13": "f5dc515c73ee15fb4fb436f45397917a783be0fbf4c958ff5b0f3f8537cff06f",
      "14": "2f9bd22bf568db05b8497ac885c0acc913a50c718e1fed9f7ee9775d599dfa85",
      "15": "0b93871b9f95330d85f883437f0c97cb65594a56e7657c1226a51ddb3c734655",
      "16": "783443d1092e70ae70495ddf725ad9a9d35e861cdb0510c592bb11bb6cd2ae34",
      "17": "e3fce85c735f375e51b2152f60fdb2a26c118b05c5617816236260128ff9dae6",
      "18": "30b23cec34afc034a3adc2c4fc45f112de94371def944e24fcc4ec2c57aed625",
      "19": "b2abebbfdd9eefecd06a54bb6146dd144d6bf7c2d876449d86bae20cdf569797",
      "20": "c52192c1124a7adf5cc2b4dfd1775636063c2455f3fe05447ec8b9700217e0a9",
      "21": "1a2b45376010d61f02919774b2d554663cd6c23715993b0e7cc469169f25764a",
      "22": "6bc4da68dd54c2e26deacf82a86dc3de712bd5288a9bfa2b1628dd22e3e7e3ec",
      "23": "d9b45cfbedbf5706429b3623302079b3c8723283ea359bbfc2ba257157d65297",
      "24": "4f468b10891e441f3a83c9349c76f7ddb42497e11efbf1fa7b725b45abbb5c61",
      "25": "19c6bcee928c56c3e871efc886ba71bce0f5963f68d5963c50c59ee44a16eecd",
      "26": "50be56701617d0b7bfb25d592f6d46d9fb3bab6e79aea87bb18ad48d145b3e4a",
      "27": "ed0d887493b631d87f4b76eededab1d4ffbbef48c69f9ff1f544819bc3e02375",
      "28": "afa140efc51be486ecda1c837c16fd28a3c83314dda5c813f8f40b3d439b9ad8",
      "29": "509c8102701a8dfdb673053fa21ebdcf6f4e438f55d338b4be30a45f77512f4a",
      "30": "1b8031e9a93a2401f369b9c482e5f96f41d043456696daadf525b5f50ca74453",
      "31": "7af487fd2d3b1b9cba16439323ad114531fff3cd0f597d8c36a4552cadbaca33",
      "32": "6c5ce4d56fc0ff3e6af9c7ac8fec5a863437f6ba0efee7721b2d79d09f0ffe4c"
    },
    "source_packet_sha256": "81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886",
    "blueprint_sha256": "51b5a85d08c85550fa18de656ab7e9cdb3923831f4584ea7e9bf4da3ce35e8ce",
    "0100_remote_candidate_sha256": "debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2",
    "register_sha256": "d4375ee82bb872e2a54ba94a5aef45e72befc68760824fe98d2bd82569bfc7fd",
    "repair_receipt_sha256": "9609dda77b4d772479ae9cb8ae3c52d21f190d3e0c4b37e0db0ed76868f72428",
    "semantic_correction_receipt_sha256": "13b1cee87a6cc5b86cc65827191bfb0b4a10da343bf2b9cf45e8f961bae5f546"
  },
  "technical_status": "PASS_TECHNICAL_ONLY",
  "semantic_review": "PENDING_ON_FINAL9_EXACT_SHA",
  "visual_review": "PENDING_FINAL9_VISUAL_RECEIPT",
  "formal_acceptance": "NOT_GRANTED"
}

Visual:
{
  "receipt_id": "TTQS-I18E08-DOC0101-R09-FINAL9-VISUAL-QA-20261021",
  "doc_id": "0101",
  "requirement_id": "I18-E08",
  "official_checkbox_serial": "UNKNOWN",
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "verified_at_local": "2026-10-21T21:52:33.482453+08:00",
  "docx_sha256": "56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68",
  "pdf_sha256": "27002fa5e60ba712be1e38952f04bd12ba64d04661fa34101f1e09462c3ce4b2",
  "render_manifest_sha256": "4de6b20e4ec0b3ed421f1a56704082f128bcf9fddd9dee9beb67a7dc3946f237",
  "page_count": 32,
  "direct_original_resolution_pages": [
    3,
    6,
    7,
    8,
    9,
    19,
    31,
    32
  ],
  "inherited_exact_image_pages": [
    1,
    2,
    4,
    5,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30
  ],
  "changed_pages_from_final8": [
    3,
    6,
    7,
    8,
    9,
    19,
    31,
    32
  ],
  "previous_visual_receipt_sha256": "a9f10c32f524885c79b86e8efc5ef2cc4dc7d807c5b53b5ddb50cf6caa124d64",
  "previous_visual_docx_sha256": "92edebeff1703104c30486e18cf568f6666310a20ae8a945ab9d03789ec21fdb",
  "inspection_method": "Word-native final9 PDF rendered with PDFium at 1.5 scale. All 32 pages covered: eight changed-page images directly inspected at original resolution; the remaining 24 images are byte-identical by SHA to pages covered by the full final8 visual receipt.",
  "findings": [
    "No clipping, overlap, broken tables, missing glyphs, orphaned content, or unreadable text observed on changed pages. All 24 unchanged images retain their final8 review by exact SHA."
  ],
  "visual_status": "PASS_VISUAL_ALL_32_PAGES_EXACT_IMAGE_COVERAGE",
  "reviewer_independence": "Codex visual inspection only; semantic review separate.",
  "page_hashes": [
    {
      "page": 1,
      "png_sha256": "3b034638006827f6c182a2218403fbf9acaab4fc2808c8ea163a1b69f1eeae3e",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 2,
      "png_sha256": "6716f2928be6ac8cc7071f4868c30a5b9b91cc065f746d3c1022d8f4450d9eb9",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 3,
      "png_sha256": "17a88b1133f16c99927b6305387e6c6b036a3efd3affd56835edc2e656db1af7",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 4,
      "png_sha256": "18cce6b6c98a7940a63365fcaf86ab0270d3e83e19052ce1d3a6b5bd1ac0c6c5",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 5,
      "png_sha256": "023434fd54e1923a3d3c176aad64dd75a7b2ec743539f7be066118ab215fcc6f",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 6,
      "png_sha256": "18dc93510c08b24616344027cd00864eb11b524a4387dece28bebd8db88270ec",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 7,
      "png_sha256": "5797740248d95f25b0e7aea12d26a89a05c335e6ada92e5d3261a1530dd57de3",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 8,
      "png_sha256": "a86d74e0ef72d15a3f257336d12403ef8cdcac3ed1104b2586ad74d68466ac3c",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 9,
      "png_sha256": "2502881739ccf9d54dd1990bd1dab1bd0340a4971c2c2ca8fc92836f6cfb49f9",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 10,
      "png_sha256": "2bd4828f09bbe9dab23288309dcda1b30653366ffe0c0ebe5bc446bd4d8c0a59",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 11,
      "png_sha256": "5bc2bbc946bce80df9f0d0ae8f9801302ee72601053cad1595c0e0e3f0a5028a",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 12,
      "png_sha256": "9ae8896d611065be2cb4b25e104c8be6cc3e06aeadfb7f4bfe938fa2ea59531c",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 13,
      "png_sha256": "f5dc515c73ee15fb4fb436f45397917a783be0fbf4c958ff5b0f3f8537cff06f",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 14,
      "png_sha256": "2f9bd22bf568db05b8497ac885c0acc913a50c718e1fed9f7ee9775d599dfa85",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 15,
      "png_sha256": "0b93871b9f95330d85f883437f0c97cb65594a56e7657c1226a51ddb3c734655",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 16,
      "png_sha256": "783443d1092e70ae70495ddf725ad9a9d35e861cdb0510c592bb11bb6cd2ae34",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 17,
      "png_sha256": "e3fce85c735f375e51b2152f60fdb2a26c118b05c5617816236260128ff9dae6",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 18,
      "png_sha256": "30b23cec34afc034a3adc2c4fc45f112de94371def944e24fcc4ec2c57aed625",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 19,
      "png_sha256": "b2abebbfdd9eefecd06a54bb6146dd144d6bf7c2d876449d86bae20cdf569797",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 20,
      "png_sha256": "c52192c1124a7adf5cc2b4dfd1775636063c2455f3fe05447ec8b9700217e0a9",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 21,
      "png_sha256": "1a2b45376010d61f02919774b2d554663cd6c23715993b0e7cc469169f25764a",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 22,
      "png_sha256": "6bc4da68dd54c2e26deacf82a86dc3de712bd5288a9bfa2b1628dd22e3e7e3ec",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 23,
      "png_sha256": "d9b45cfbedbf5706429b3623302079b3c8723283ea359bbfc2ba257157d65297",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 24,
      "png_sha256": "4f468b10891e441f3a83c9349c76f7ddb42497e11efbf1fa7b725b45abbb5c61",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 25,
      "png_sha256": "19c6bcee928c56c3e871efc886ba71bce0f5963f68d5963c50c59ee44a16eecd",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 26,
      "png_sha256": "50be56701617d0b7bfb25d592f6d46d9fb3bab6e79aea87bb18ad48d145b3e4a",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 27,
      "png_sha256": "ed0d887493b631d87f4b76eededab1d4ffbbef48c69f9ff1f544819bc3e02375",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 28,
      "png_sha256": "afa140efc51be486ecda1c837c16fd28a3c83314dda5c813f8f40b3d439b9ad8",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 29,
      "png_sha256": "509c8102701a8dfdb673053fa21ebdcf6f4e438f55d338b4be30a45f77512f4a",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 30,
      "png_sha256": "1b8031e9a93a2401f369b9c482e5f96f41d043456696daadf525b5f50ca74453",
      "coverage": "INHERITED_EXACT_PNG_HASH_FROM_FINAL8_FULL_VISUAL_RECEIPT",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 31,
      "png_sha256": "7af487fd2d3b1b9cba16439323ad114531fff3cd0f597d8c36a4552cadbaca33",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    },
    {
      "page": 32,
      "png_sha256": "6c5ce4d56fc0ff3e6af9c7ac8fec5a863437f6ba0efee7721b2d79d09f0ffe4c",
      "coverage": "DIRECT_ORIGINAL_RESOLUTION_INSPECTION_FINAL9",
      "visual_result": "NO_CLIPPING_OVERLAP_BROKEN_TABLE_OR_UNREADABLE_CONTENT"
    }
  ],
  "limitations": [
    "Visual review does not establish semantic acceptance, REAL performance, or formal association approval.",
    "Official printed checkbox serial remains UNKNOWN."
  ],
  "formal_acceptance": "NOT_GRANTED"
}