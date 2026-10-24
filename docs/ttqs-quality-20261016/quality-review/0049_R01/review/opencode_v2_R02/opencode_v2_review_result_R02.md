I have completed all independent checks. Here is my report.

---

# Independent exact-SHA review — DOCX 0049 R01 repair

**On-disk SHA-256 (`candidate/0049_R01.docx`):** `955f7138951cf9f37863116540159a908c2693ce4b006c5a9bb2914f3b2de291` — **matches** the required hash exactly; size 61,772 bytes. No mismatch, review proceeded.

**Verdict: PARTIAL.** The candidate substantively satisfies official checkbox 051 and is a sound, usable three-source demand→course plan with no fabrication; all three previously-flagged repair targets are corrected. PARTIAL reflects only two remaining **minor, non-material consistency items** (one in the evidence packet, one cosmetic in-DOCX locator), neither of which changes requirement satisfaction.

**Inspected directly:** candidate DOCX (73 paragraphs, 31 tables — matches QA receipt); `SOURCE_MAP_R01.md`; `BUILD_METADATA_R01.json`; 158-row `SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`; `TECHNICAL_VISUAL_QA_R01.json`; official image `source/official_evidence_table_page4.png`; `BLUEPRINT_CURRENT.jsonl` row `0049`; `02_GENRE_WRITING_MANUAL.md` Ind.11; `03_157_CHECKBOX_BLUEPRINTS.md` I11; DOCX 0033 R03 at SHA `fe5f3cfd…b5f4f` and its register `d114f36d…523247` (both recomputed, both matching); and all **15** final page images in `render_R01_955f7138/`.

## 1. Official wording, genre, scope; distinction from 033/049/052 — PASS
Official p.4 image shows indicator 11 whose first checkbox reads exactly 「訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。」 The candidate reproduces it verbatim (rendered p.13 §9 Table row 1; p.1 identification), maps to `I11-E01 / 方框051 / 官方資料表第4頁`. Blueprint row 0049 = `I11-E01`, page 4, confirming mapping. The four identities are kept strictly distinct: 本件 0049/I11-E01/051; 0033/I07-E01/033; 0050/I11-E02/052; 0048/I10-E03/049 (§1.1 table, p.2–3; §9, p.13). Genre is strategy/plan, correct for 051. No wrong-item content.

## 2. Title/file-masked body reads as demand→course plan — PASS
Masking p.1, the body runs §2 (three demand sources) → §3 (denominators + raw matrices) → §4 (gap/priority + option comparison) → §5 (course-level objectives G1–G4) → §6 (content/method/schedule/staffing/resources/environment) → §7 (assessment/timing/scales/thresholds) → §8 (risk/revision) → §9–10 (traceability/replacement). This is unmistakably a demand-to-course plan. Survey instrumentation lives in 0033 (p.4 §intro says so); unit-level lesson detail is expressly deferred to 0050 (§5 intro, p.6); procurement/trainer meetings are only a negative-neighbour distinction (§1.1, p.3). Not a survey-only report, unit plan, or procurement record.

## 3. Recomputed linked data/formulas — PASS
Independently recomputed from rendered §3.1/§3.2 raw matrices:
- Denominators: 合作窗口 4/3/3; 預定受訓者 4/3/3; 任務角色代表 4/4/3; total **12/10/9**; 10÷12=**83.3%**, 9÷12=**75.0%**, 9÷10=**90.0%** ✔ (one respondent excluded for incomplete Q04; two non-returns — matches 0033 R03).
- Importance sums 甲41/乙38/丙35/丁39 → means **4.56/4.22/3.89/4.33** ✔
- Self-rating sums 甲24/乙25/丙27/丁21 → means **2.67/2.78/3.00/2.33** ✔
- Gaps **丁2.00 / 甲1.89 / 乙1.44 / 丙0.89** ✔ (matches ranking 丁1, 甲2, 乙3)
- Option weights 40/30/20/10%: 甲 5·.4+5·.3+4·.2+5·.1=**4.80**; 乙=**4.00**; 丙=**3.50**/5 ✔
- Modules **90+90+120+60 = 360** teaching minutes ✔
Priority rule stated as sample-only (importance ≥4.00/5 AND gap ≥1.20). All internally coherent and traceable to 0033.

## 4. Prior concrete defects corrected; no stale wording — PASS
- **0033 表12 = option-weight comparison:** 0049 §4.1 (p.6) now says weights and scores 「沿用 0033 R03 **表12** 的合成示範」. I independently confirmed 0033 R03's printed labels: 表12 = 「三個候選方向的合成加權比較」. ✔
- **0033 表13 = objectives/module basis:** 0049 §6.1 (p.8) now says module names/behaviour/hours 「沿用 0033 R03 **表13**」. 0033 R03's 表13 = 「優先擬議方向的學習目標與評量」. ✔
- **p.1 quick guide → §4.1:** rendered p.1 「先做什麼」 now reads 「…再看第 **4.1** 節方案比較及第 6 節計畫」. ✔
- **Cohort 12 / room 14:** §1 (p.2) 「12 人為同案示範班級規模」; §6 (p.8) 「示範班級 12 人」 and 學習環境 「12 名學員與 2 名教學人員…建議 **14 席**」; register `F0049_COHORT_SIZE=12`, `F0049_ROOM_SIZE=14`. Matches 0033 R03's 「示範規劃名額12人」. ✔
- **Stale-token sweep** (raw `document.xml` + headers/footers, not just body): 表14 / 表15 / 表16 = 0; 「8 人」= 0; 「10 席」= 0; 「第5節」= 0. ✔ (The remaining 已調查/已開課/已核准/已達標/已聘任 hits are all inside explicit *prohibitions* — e.g. p.1 callout 「不得改寫成「本會已調查／已決定／已開課／已達標」」 — not claims.)

## 5. Register: 158 unique IDs, full coverage, SAMPLE/REAL boundary — PASS
Register = **158 rows, 158 unique `fact_id` (0 duplicates, 0 empty values/fields)**; all `doc_id=0049`, all `case_id=SYN-0033-PLAN-01`, all `verification_status=SAMPLE_ONLY_NOT_VERIFIED_AS_REAL`, every row carries `required_replacement_source`, `owner_role_to_confirm`, and `locator_marker`. 115 rows cross-reference 0033; 43 are synthetic plan/assessment assumptions. Key figures are registered: cohort 12, room 14, 360 min, modules 90/120/60, weights 40/30/20/10%, thresholds 8/10 and 3/4, dates 2026-08-03/08-14, quiz Q1–Q10, rubric R01–R04. No real person/signature/approval/attendance/delivery/learner result/third-party fact exists; the association name appears only inside an explicit non-representation disclaimer (p.1). Boundary repeatedly asserted as UNKNOWN / NOT APPROVED / NOT SCHEDULED / NOT IMPLEMENTED. PASS.

## 6. Practical usability; replacement gates; 0048/0050 separation — PASS
Actionable throughout: observable course-level objectives G1–G4 with criteria (§5); content/method/staffing/resources/environment (§6); two-half-day schedule with per-slot minutes (§6.2); assessment timing/scales/thresholds ≥8/10 and ≥3/4 with explicit failure handling and one re-demonstration then re-assessment (§7); retraining/reopen conditions (§4.1 重開條件; §8 R6 two-failed-retries trigger; 課後14日 review). §10 replacement checklist defines per-source gates and UNKNOWN/NOT-APPROVED/NOT-SCHEDULED/NOT-IMPLEMENTED states; §10.1 gives four adoption gates. Responsibilities are cleanly separated: 0050 owns unit-level objectives/instruction-assessment detail; 0048 owns procurement/trainer-selection meetings; 0049 neither fabricates a meeting nor claims a completed 0050 package (§1.1 p.3, §9 p.13).

## 7. Rendering — all 15 pages readable; fonts within floors — PASS
Font floors independently re-measured from the DOCX runs: **body min 10.5 pt** (10.5–24.0), **table min 9.5 pt** (631 runs @9.5, 14 @10.5), header 8.0, footer 8.5 — all compliant. Page-by-page (render_R01_955f7138): p.1 title/SAMPLE callout/30-sec table/id; p.2 §1 + §1.1 head; p.3 §1.1 tail + §2 table; p.4 §3 denominators + §3.1 matrix; p.5 §3.2 tail + §4 means; p.6 §4.1 option comparison + §4.1 reasons + §5 table head; p.7 §5 G3/G4 + scope-exclusion (intentional chapter white space); p.8 §6 + §6.1; p.9 §6.2 schedule + roles; p.10 §7 + quiz Q1–Q5; p.11 Q6–Q10 + §7.2 rubric; p.12 §8 risk + review; p.13 §9 + §9.1; p.14 §9.1 tail + §10; p.15 §10.1. No clipping, overlap, broken cells, or orphan headings. Every split table repeats its header on the continuation page (p.4→no; p.3→4, 4→5, 6→7, 10→11, 13→14 all carry the header correctly). **§10.1 begins with its heading and all four gate rows G1–G4 together on p.15** — as required. No regression observed after the corrections.

## Defects found

**D1 — Stale evidence sidecar (`SOURCE_MAP_R01.md`), non-DOCX.** Lines 10 and 45 still cite candidate SHA `c064ed159bf358ae…` and `render_R01_c064ed15/…page-16.png` (16 pages), whereas the actual candidate is `955f7138…` with 15 pages, as correctly recorded in `BUILD_METADATA_R01.json` (line 10) and `TECHNICAL_VISUAL_QA_R01.json` (line 11). Why it matters: the packet's provenance document contradicts the artifact it describes and could misdirect a downstream reader to a superseded SHA/render. **DOCX bytes: no change needed** — refresh the `SOURCE_MAP_R01.md` sidecar only.

**D2 — Imprecise in-DOCX cross-reference locator (cosmetic).** §2 source table, row 「業主／客戶需求」 (docx table index 5, row 1; rendered p.3): 「…同案Q04重要度資料列在**表3**」. 0049 prints no table numbered 「表3」, and 0033 R03's Q04 importance raw scores are in its **表8** (its 表3 is 「需求—課程—評量因果鏈」); the register's own basis text for these facts cites 0033 R03 表8. Why it matters: an evaluator cross-checking the stated locator cannot resolve 「表3」 to a printed table; the data is nonetheless directly present in 0049 §3.1 (p.4) and correctly sourced in the register, so impact is minimal. **DOCX bytes: optional tiny edit only** (change 「表3」 → 「0033 R03 表8」/「第3節」); not required for requirement satisfaction.

**No material defect exists** in `candidate/0049_R01.docx`: official wording, genre, three-source→course-plan content, all recomputed math, the 158-row register, SAMPLE/REAL boundaries, and all 15 rendered pages are correct and compliant. D1 is an evidence-sidecar inconsistency; D2 is a cosmetic locator imprecision. This is an independent candidate-quality review only and does not grant formal Human acceptance or promotion.