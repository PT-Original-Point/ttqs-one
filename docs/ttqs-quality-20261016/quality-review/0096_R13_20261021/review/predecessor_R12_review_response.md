## R12 exact-SHA semantic review — DOCX 0096 / I18-E03

**Binding.** DOCX SHA-256 `1c4626130b160cf64f90e8c8f507f01bafbc09b70f7f1f4510051c7b11241d33`; body SHA-256 `479ff59c88189eb41f3065c2af1ded5220db3a1d320c1bb487b507b1f957b3ef`; CSV SHA-256 `84efb4a40b8a1c8903e3e7f17558db4cf4d49983830226bd63a7fffdee34a237` (121 data rows); packet SHA-256 `cadad053fa17dbcc5ddfe6a66627a5db3c7350e0c3e64f8f0febd0c19d156dc6`. State `CANDIDATE_NOT_FORMALLY_ACCEPTED`; DOCX 0096 and I18-E03 are distinct from official checkbox serial 099. This is a text-only semantic review. I did not inspect the Word-rendered pages; visual receipt `35902dbe9a7f77471b05b10c8355946b2dc046e830dce83ae494acf4a05fdce9` is separate and is not verified by me.

### F1–F12

| Finding | Verdict | Evidence and residual |
|---|---|---|
| **F1 Status precedence** | **PARTIAL** | 第八節「受控狀態及日常用語映射」correctly sets HOLD → INVESTIGATE → REJECT and says unsigned alone is not a specific contradiction (EX-03). But 第三節流程三第 6 點 and 流程四第 6 點 still list 「未簽名文件」 as an INVESTIGATE trigger after formal filing: 「正式立案後如有未簽名文件、具體身分疑點、代簽疑慮或其他可指認矛盾，狀態記 INVESTIGATE」. That directly conflicts with 第八節/EX-03: 「單純未簽名或來源待核是缺口，不自行構成矛盾」. Minor also: 第八節 EX-08 uses 「立案時記錄期限…」 for a HOLD case. **Minimal repair:** in 流程三/四 change to 「未簽名文件先記缺件；只有另有具體身分疑點、代簽疑慮或其他可指認矛盾並正式立案後，才記 INVESTIGATE」; change EX-08 to 「於登錄／建立追蹤時」. |
| **F2 Register role owners** | **PASS** | 第十二節 HOLD-IDENTITY-01, HOLD-LOCATION-01, HOLD-ORIGINAL-REFERENCE-01, HOLD-RELATION-01, HOLD-SHA-NOT-CALCULATED, HOLD-GAPS-01 align with 第五節 owners. SAMPLE-ACTION-03/04/INV-05 rows now state executor, reviewer, and escalation path: e.g. SAMPLE-ACTION-03 「SAMPLE 承辦角色（未指派，執行）；SAMPLE 覆核角色（複核）；未完成時提報經指定核准角色」. No material residual. |
| **F3 Register locators / CSV sync** | **PARTIAL** | Stale `SAMPLE-DUE-RULE-INV-05` row is gone. Section 9 locators for SAMPLE-CASE-002, SAMPLE-OLD-CATEGORY-01, SAMPLE-NEW-CATEGORY-01, SAMPLE-CORRECTION-REASON-01, SAMPLE-ROLE-HANDLER-02, SAMPLE-ROLE-REVIEWER-02 are now exact: 資料列 1/3/4/5/7/8 with the correct field names. CSV is 121 rows and mirrors the body table. **But the SAMPLE-CASE-INV-05 row is wrong:** locator says 第六節「完整十三欄位 INVESTIGATE…」第 1 列〈收件追蹤編號〉, yet the displayed value is 「SAMPLE-CASE-INV-05 示例值（全為 SAMPLE／SYNTHETIC；無實際收件）」— that is the table header, not field 1. Field 1 actually reads 「SAMPLE-CASE-INV-05｜演練追蹤碼；非實際收文流水號」. The CSV repeats the same wrong value, so CSV/body sync is exact only in the sense that both contain the same semantic error. This contradicts 第十二節 「每一列顯示值須與正文相符」 and 第十三節 A5 「已比對…值、定位」. **Minimal repair:** change the Table 12 and CSV row to the field-1 text; regenerate the CSV and update A5 SHA/sync receipt. Minor: SAMPLE-COMPLETENESS-04 and some Section 8/「案例結論」 locators are table-level or paraphrased rather than exact row/field. |
| **F4 Undefined actors** | **PASS** | 第二節「角色名稱與範圍（內部控制角色共三類）」maps 承辦人/承辦角色, 覆核人/覆核角色, 核准角色/權責主管/主管. External 評核委員 is expressly not a fourth internal role and is gated by HOLD-EVALUATOR-ACCESS-01. 第十三節 final approval uses 經指定核准角色. |
| **F5 CASE-003 completeness** | **PASS** | 第七節 CASE-003 row 11 no longer contains SAMPLE-ROLE-HANDLER-03: it lists only SAMPLE-REVIEW-03, SAMPLE-DATE-REVIEW-03, SAMPLE-ROLE-REVIEWER-03. 第六節 field 11 says 「承辦角色只列於第 13 欄」; field 13 contains the handler. Field 13 is now framed as 「無核心缺證；…RESTRICTED 列件後續追蹤」 with 2026-11-26 follow-up, 2026-11-27 escalation to 經指定核准角色, and pause of restricted use. Minor wording: 「以覆核日 2026-11-19 起算」 but day 1 is enumerated as 11-20; the enumerated dates and due date are correct. Minor optional: row 11 omits SAMPLE-COI-03, but the table is a summary and does not change the 12/12 count. |
| **F6 CASE-004 authorization/feedback** | **PASS** | 第六節 field 9 states written authorization with validity 2026-10-18–2026-10-31; field 10 uses SAMPLE-FEEDBACK-COURSE-04 and COURSE-04/SESSION-04, distinct from Section 4 SAMPLE-COURSE-05. No COURSE-05 sentence leaks into CASE-004. Field 13 now contains SAMPLE-ROLE-HANDLER-04, SAMPLE-ROLE-REVIEWER-04, a five-workday follow-up to 2026-10-27, authorization/channel check, pause, and escalation. Correct. |
| **F7 Field-13 gap inventories** | **PASS** | CASE-001 field 13 now says 「第 1 追蹤編號及第 2 收件日期／途徑僅為 SAMPLE；未實際收件，沒有 REAL 收件時間或途徑」 and then lists fields 3–11, field 12 no number. CASE-004 field 13 is no longer 「無格式欄位待填」; it has a sample handler, reviewer, deadline, and pause rule. INV-05 field 13 lists 9/10 gaps and deadline. No material residual. |
| **F8 INV-05 timeline/excerpts** | **PASS** | 第六節 INV-05: filing 2026-11-10, start 2026-11-11, five workdays to 2026-11-17, escalation 2026-11-18; excerpts A/B and sources A/B are separate; future/non-scheduled warning present. Arithmetic correct. Minor: no named escalation recipient; the row says 「未完成時依核定程序提報」, while CASE-003/004 name 經指定核准角色. |
| **F9 17d official claim** | **PASS** | The 17d assertion is removed. 第一節 and 第十一節 assert only page 6 I18-E03 「感謝函。」 and defer other same-name/adjacent items to the formal source. Official/checkbox IDs remain distinct. **Separate Blueprint gap:** see N1 below (required trace table). |
| **F10 Real-looking association** | **PASS** | 「原始點協會」 no longer appears. Samples use SAMPLE codes, 「示範組織」, or generic roles; no named real third-party issuer. |
| **F11 0098 overlap** | **PASS** | 第四節 A section says 0096 does not collect, log, retain, or analyze general course opinions; routes them to DOCX 0098/I18-E06. Mini-survey questions remain removed. 第二節/第十一節 also separate 0095, 0097, 0098. |
| **F12 A4, phrases, RESTRICTED, privacy** | **PASS** | 附件四 uses A/B tracking and B is conditional; malformed field-13 phrase is rewritten; HOLD-CONTROL-NO-01 includes qualified or approved RESTRICTED; 第十節 privacy wording is purpose-limited. |

### New material Blueprint gap

**N1 — Required official trace table is missing (PARTIAL).**  
Blueprint `required_tables_or_figures` requires 「官方要求—表單欄位—附件定位追溯表」. 第十一節「官方要求與本件欄位對照」 is prose only: it says the main content is in Sections 4/5/6/7/9 and attachments A1–A4, but it does not provide a row-by-row table mapping official requirement/page → form fields 1–13 → attachment/evidence location → review/status. This is a Blueprint nonconformance and weakens the 「逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核」 acceptance test. **Minimal repair:** add a table in 第十一節 with at least these columns and rows: official requirement (page 6, I18-E03, 「感謝函。」) / form fields (1–13 or grouped) / evidence location (Section 5/6/7, A1/A2/A3/A4) / review or status. Do not copy neighbor content.

### Arithmetic checks

- **CASE-001:** SAMPLE fields 1,2,4,6 = 4/12; HOLD fields 3,5,7–12 = 8/12; 4+8=12; 100%; REAL 0/12. Correct.
- **CASE-003:** 12/12 SAMPLE = 100%; REAL 0/12 = 0%. Review 2026-11-19 is Thursday; enumerated workdays 11-20 Fri (1), 11-23 Mon (2), 11-24 Tue (3), 11-25 Wed (4), 11-26 Thu (5); escalation 11-27 Fri. Correct, subject to the 「以覆核日起算」 wording note.
- **CASE-004:** 12/12 = 100%; REAL 0/12 = 0%. Start 2026-10-21 Wednesday; 10-21 (1), 10-22 (2), 10-23 (3), 10-26 (4), 10-27 (5). Authorization 10-18–10-31 covers receipt 10-19, review 10-20, follow-up 10-27. Correct.
- **INV-05:** 12/12 = 100%; REAL 0/12 = 0%. Filing 2026-11-10 Tuesday; start 11-11 Wednesday; 11-11 (1), 11-12 (2), 11-13 (3), 11-16 (4), 11-17 (5); escalation 11-18 Wednesday. Correct.
- SHA demos are 64 hex characters and expressly labeled uncalculated/non-file digests. No arithmetic error found.

### Crosswalk, SAMPLE/REAL, CSV, usability

- **Crosswalk/neighbors:** 0095/I18-E02 (mechanism), 0096/I18-E03 (this thank-you-letter solicitation/receipt tool), 0097/I18-E05 (ability questionnaire), 0098/I18-E06 (survey execution/sample flow/analysis) remain distinct. No item substitution or copied neighbor facts found.
- **SAMPLE/REAL boundary:** Text-level PASS. All cases are labeled SAMPLE/SYNTHETIC; no real names, signatures, receipts, authorizations, reviews, or organizational approvals; REAL 0/12 throughout; no fabricated third-party letter. Binary/metadata/embedded-object content was not verified.
- **CSV consistency:** 121 rows, unique fact_ids, matches the body Table 12 row count/order, and Section 9 locators are corrected. One semantic value/locator defect remains: SAMPLE-CASE-INV-05. Some rows use paraphrases or table-level locators, but they are not the main blocker.
- **Operator usability:** PARTIAL. The role glossary, state mapping, process flow, blank forms, completed examples, and register are usable, but the F1 unsigned/INVESTIGATE contradiction and the F3 register value defect can still cause inconsistent case handling. The missing N1 trace table also slows official cross-checking.

### Overall disposition

**Overall: PARTIAL** for DOCX SHA `1c4626130b160cf64f90e8c8f507f01bafbc09b70f7f1f4510051c7b11241d33`, body SHA `479ff59c88189eb41f3065c2af1ded5220db3a1d320c1bb487b507b1f957b3ef`, CSV SHA `84efb4a40b8a1c8903e3e7f17558db4cf4d49983830226bd63a7fffdee34a237`.

Not FAIL: the official I18-E03/page-6 focus, state precedence framework, three-role glossary, 0095/0097/0098 separation, SAMPLE/REAL boundary, CASE-003/004 follow-up structure, and arithmetic are substantially correct. Not PASS because F1 and F3 retain material inconsistencies and N1 is a Blueprint-required table gap.

**Minimal repair order:**
1. Fix 第三節流程三/四 「未簽名文件」 wording to match 第八節/EX-03.
2. Fix SAMPLE-CASE-INV-05 in Table 12 and the CSV to the field-1 value; regenerate CSV, update A5 SHA and sync receipt.
3. Add the 第十一節 official-requirement/form-field/attachment trace table.
4. Optional cleanups: add a Section 9 correction date; clarify CASE-003 start-date wording; name 經指定核准角色 in INV-05 escalation; change EX-08 to 「登錄／建立追蹤時」; tighten paraphrased/table-level register locators.
5. Re-audit the new exact DOCX/body/CSV SHAs; no changes are authorized by this review.
