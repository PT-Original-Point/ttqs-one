# Independent exact-SHA review — TTQS ONE DOCX 0058 R05

## Candidate binding / identity
- **doc_id**: 0058; **requirement**: I13-E02; **checkbox serial**: 062; **official page**: 4 (indicator 13, second checkbox), continuation p.5.
- **Requested DOCX SHA-256**: `34DC48094F3260F65477BBD914F45966965A11D15D6A5FE7AA2666068310A020`
- **Independently calculated DOCX SHA-256**: `34DC48094F3260F65477BBD914F45966965A11D15D6A5FE7AA2666068310A020` — **MATCH**.
- **Supplied rendered PDF SHA-256**: `B92CC49A466ECC0B8249CCFD1DA827C9668717D722D31C6B40B019BEC3FEB9BE` — **not independently verified** (see limitations).
- **Candidate unchanged**: Yes. No project file was modified, created, or overwritten; only temporary files under `C:\Users\J\AppData\Local\Temp\opencode` were used.

## Overall verdict: **PARTIAL**

The artifact is semantically strong and internally consistent, but it is still a SAMPLE/SYNTHETIC candidate and is **not suitable to promote beyond a SAMPLE candidate** without real evidence replacement and formal human acceptance.

---

## 1. Exact official identity and genre — PASS
- DOCX title/header/footer and Table 1-1 identify `TTQS-0058 | I13-E02 | official checkbox 062 (資料表第4頁) | R05 | case SYN-0058-202608`.
- Official requirement verbatim present in §1 and Table 10-1.
- §10 (Tables 10-2, 10-3) explicitly separates 0057/I13-E01/checkbox 061 (macro institutional review) and 0059/I13-E03/checkbox 063 (retraining/certificates/internship); 0058 is scoped to micro-level personal SMART plans, 30-day tracking, four-column records, incentive proposal, and three-level quantitative results. Document serial (0058) is not conflated with checkbox serial (062).

## 2. Mature usable procedure and tools — PASS
- §2 SOP (Table 2-1) six steps with proposal timelines, outputs, and roles marked “建議由章程授權者指定”.
- §3 four-step rubric 0–4 (Table 3-1) and pre/post results (Table 3-2).
- §4 six individual SMART action plans with per-learner targets, assistance, barriers, and verdicts (Table 4-1).
- §5 four-column standard (Table 5-1), complete case record REC-0058-A01-DEMO (Table 5-2), three-level analysis (Table 5-3).
- §6 incentive proposal with formula, threshold, ethics veto, non-monetary reward (Tables 6-1, 6-2).
- §7 two blank operational forms (Tables 7-1, 7-2).
- §8 replacement register REQ-0058-01…08 (Table 8-1).
- §9 audit/reject matrix (Table 9-1).
- §10 source/neighbor/version control (Tables 10-1…10-3).

## 3. Complete operational forms, rubric, sample case, criteria, ownership, timing, evidence instructions — PASS
- All 18 tables present (Table 0 front guide box + 17 content tables matching the blueprint). Blank forms are explicitly labeled “實際使用時另開新表填寫”; rejection criteria in §8 (ERR-0058-01…10) cover source, privacy, denominator, arithmetic, genre, evidence, plan-vs-result, missing evidence, unauthorized approval, and medical boundary.

## 4. Recomputed arithmetic — PASS
- Pretest scores A2 B2 C1 D2 E3 F2: sum 12, mean 2.00; ≥3 = 1/6 = 16.7%.
- Posttest A4 B3 C3 D4 E3 F2: sum 19, mean 3.1667 (3.17); ≥3 = 5/6 = 83.3%.
- Attainment change: (5/6 − 1/6)×100 = 66.6667% → **+66.7 pp** (endpoint 83.3−16.7 = 66.6 is rounding display only). Mean gain +1.1667 (+1.17).
- SMART: achieved A,B,D,E = 4/6 = 66.7% vs 75% target (≥5) → **not met**; evidence submit 5/6 = 83.3%; submitter success 4/5 = 80.0% (supplementary only).
- Four-column: A 1/2→2/2, B 2/4→3/4, C 1/3→2/3, D 3/4→4/4, E 2/4→3/4, F 0/2→0/2.
  - Team A (9 opportunities): 4/9=44.4% → 7/9=77.8%, +33.3333% → **+33.3 pp**.
  - Team B (10 opportunities): 5/10=50.0% → 7/10=70.0%, **+20.0 pp**.
  - Organization (19 opportunities): 9/19=47.4% → 14/19=73.7%, 5/19×100=26.3158% → **+26.3 pp**.
- Incentive: A 60%×7/9 + 40%×3/3 = 46.67+40.00 = 86.67 → 86.7 (pass, rank 1); B 60%×7/10 + 40%×2/3 = 42.00+26.67 = 68.67 → 68.7 (fail, rank 2); threshold 70.0.
- All displayed counts, denominators, and case_id/facts are internally consistent with the blueprint and content JSON. F’s 2 opportunities are retained in both team (10) and organization (19) denominators.

## 5. SAMPLE/SYNTHETIC boundary — PASS (with caveat)
- Repeated, explicit boundary statements in §1, front matter, Table 1-1, §10; all synthetic facts labeled SAMPLE_UNVERIFIED in the register; 41 synthetic facts (F01–F41) plus 8 REQ-0058 items with status UNKNOWN.
- No fabricated signatures, approvals, certificates, government letters, bank/accounting evidence, or external achievements; approvals consistently framed as “提案、未核定、未生效” and roles as “建議由章程授權者指定”.
- Caveat: Table 10-3 (version history) contains the literal strings “待填” and “待核定” in historical defect descriptions, and the §7 warning quotes “待填/待核”. These are meta-descriptions rather than current blank placeholders, but a strict automated gate may flag them.

## 6. Title-blind identity and negative-neighbor boundaries — PASS
- Genre is “訓後工作應用、個人行動計畫及團隊/組織成效紀錄與操作工具（示範提案）”, not meeting minutes, generic satisfaction survey, SOP-only, or certificate log.
- Negative neighbors I13-E01/0057 and I13-E03/0059 are explicitly distinguished in §10 and Table 10-2.

## 7. Rendered layout inspection — PARTIAL (text-level only)
- Extracted layout via Word COM: **32 pages**; 18 tables; header/footer repeat on every page; font minimum 9.5pt (tables) / 10.5pt+ (body), satisfying floors.
- Table 5-2 splits across pages 15–16 **without repeating the header row** on the continuation page (minor usability defect).
- Tables 10-3 and 7-1/7-2 split across pages; continuation starts with data rows (minor).
- No visually blank/sparse pages; page 14 (6 paragraphs) is a legitimate explanatory block before Table 5-2.
- **Limitation**: I cannot view the supplied PDF or the eight contact-sheet images with this tool; layout judgment is based on extracted text and paragraph/page mapping only, not on visual rendering. My own Word→PDF conversion produced a different SHA (`EB0C9797423F579CEDD131F862AA6191D1EBAA23055C1833ABC0F248E317DA91`) from the supplied rendered PDF, likely due to environment/render settings; this does not indicate a content defect.

## 8. Suitability to promote beyond a SAMPLE candidate — NOT YET
- The document is semantically strong and calculation-correct, but it remains `PRE_BUILD_SYNTHETIC_DRAFT` / SAMPLE / SYNTHETIC. Promotion beyond a SAMPLE candidate requires: (a) real evidence replacement per REQ-0058-01…08, (b) human acceptance, and (c) legal/organizational authorization. None of these are present or implied.

## Material issues (with locators)
1. **Minor — literal forbidden-token exposure**: Table 10-3 rows R00/R04 and the §7 warning paragraph contain “待填”/“待核定”. Locators: Table 10-3, rows “R00” and “R04”; §7 paragraph “【操作防呆與真實邊界特別警告】”. Not a current blank placeholder, but may trip strict grep gates.
2. **Minor — non-repeating table header on split**: Table 5-2 (pages 15→16) and Table 7-2 (pages 23→24) continuation pages begin with data rows; header row not repeated. Locator: pages 16 and 24 first paragraphs.
3. **Limitation — visual verification unavailable**: Supplied PDF and 8 contact sheets could not be rendered/viewed by this reviewer; PDF SHA not independently verified.

## Final recommendation
- **Content verdict: PARTIAL** (no blocking semantic/arithmetic/identity defect; minor wording/layout items; SAMPLE status prevents promotion).
- Recommend: (a) optionally reword Table 10-3 historical rows to avoid literal “待填/待核定” strings if strict static gates are enforced; (b) enable repeat-header-row on Tables 5-2 and 7-2 for continuation pages; (c) keep as SAMPLE candidate pending REQ-0058-01…08 real evidence and formal human acceptance. Do not treat this review as formal acceptance.