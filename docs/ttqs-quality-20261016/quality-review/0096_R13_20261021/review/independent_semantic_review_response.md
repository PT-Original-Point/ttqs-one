## R13 independent exact-SHA semantic review — DOCX 0096 / I18-E03

### Binding and scope

**Bound artifacts**

- DOCX 0096 R13 SHA-256: `6ece53befed3ecb1b42e523b80da80decd33b0a7d55e4e1fe75ddf79b905d445`; 98,816 bytes.
- DOCX body reading-order SHA-256: `25f30e48576e8a2891b5882ea2c4b0337a33feffb2c7ae8fb44ebe9a650f3a15`.
- Synthetic replacement CSV SHA-256: `16d238c7fde83318c3d9f5c5c4c8a295ee210c34edf9ba68759a78991a0c1a91`; 121 data rows.
- Manifest source-binding hash: `3cbcb6ab41a4d4bd968275a082125aaeaa66d9800093b79625ad9449517a2657`.
- Register-sync receipt: `4a3204a48021a5cf7d54ea6ac19a202e43fb7ae986d3ca164b3a20948c9faee5`.
- Static technical receipt: `ac35504dc6c6b6c3806ba5c879d02e26aeac56641cde7c811c6ff39fb4d35e93`.
- Visual receipt: `27c97e6c345a68f050e5856bdcf2799e25401c9f22466e806a5276693cafdd54`.

The packet does not state a standalone packet-file SHA-256. I bind to the listed DOCX/body/CSV hashes and the manifest’s source-binding and sync receipts.

**Identity and state.** DOCX 0096, requirement I18-E03, and official checkbox serial 099 remain distinct identifiers. The official requirement is page 6, I18-E03, 「感謝函。」. Candidate state is `CANDIDATE_NOT_FORMALLY_ACCEPTED`; nothing in this review is organizational acceptance.

**Scope limits.** This is a text-only semantic review of the supplied packet, body, and CSV. I did not inspect the DOCX binary, fonts, layout, embedded objects, metadata, tracked changes, or the 69 rendered pages. The visual and static receipts are separate evidence; I do not treat them as my semantic verdict and do not claim to have visually inspected anything. I did not recompute any SHA-256.

---

## Overall verdict

# **PASS**

R13 resolves the three material R12 residuals — F1 (unsigned-only versus INVESTIGATE), F3 (SAMPLE-CASE-INV-05 value/locator and CSV sync), and Blueprint N1 (official trace table). All F1–F12 pass on the supplied text. The remaining issues are editorial or granularity issues that do not change the official traceability, state logic, neighbor separation, arithmetic, or SAMPLE/REAL boundary.

This is **not** a finding of formal acceptance. It is a semantic-review PASS for the exact candidate SHA.

---

## F1–F12 assessment

| Finding | Verdict | Evidence and exact locations |
|---|---|---|
| **F1 Status precedence** | **PASS** | 第三節流程三第 6 點 now says 「未簽名文件先記缺件並維持 HOLD；只有另有具體身分疑點、代簽疑慮或其他可指認矛盾，依核定程序正式立案後，才記 INVESTIGATE」. 第三節流程四第 6 點 says the same and cross-refers to 第八節 EX-03. 第五節欄位 13, 第八節「受控狀態及日常用語映射」, EX-03, and 第十一節追溯表第 3 列 all preserve the same rule. EX-08 now starts at 「登錄／建立追蹤時」, not 「立案時」. No remaining unsigned-only → INVESTIGATE trigger found. |
| **F2 Register role owners** | **PASS** | 第二節「角色名稱與範圍」 defines the three internal roles. 第五節 field owners align with 第十二節 rows `HOLD-GAPS-01`, `HOLD-RELATION-01`, `HOLD-IDENTITY-01`, `HOLD-LOCATION-01`, `HOLD-ORIGINAL-REFERENCE-01`, `HOLD-SHA-NOT-CALCULATED`. `SAMPLE-ACTION-03`, `SAMPLE-ACTION-04`, and `SAMPLE-ACTION-INV-05` name executor, reviewer, and escalation route. |
| **F3 Register locators / CSV sync** | **PASS** | 第六節 INV-05 table row 1, field 1 reads `SAMPLE-CASE-INV-05｜演練追蹤碼；非實際收文流水號`. 第十二節 `SAMPLE-CASE-INV-05` shows the same value and locates it at 「第六節『完整十三欄位 INVESTIGATE 桌上演練 SAMPLE-CASE-INV-05』下表第 1 列（資料列；欄位 1）〈收件追蹤編號〉」. The CSV row matches. The stale `SAMPLE-DUE-RULE-INV-05` row is absent. 第九節 six locators are exact: data rows 1/3/4/5/7/8 for `SAMPLE-CASE-002`, `SAMPLE-OLD-CATEGORY-01`, `SAMPLE-NEW-CATEGORY-01`, `SAMPLE-CORRECTION-REASON-01`, `SAMPLE-ROLE-HANDLER-02`, `SAMPLE-ROLE-REVIEWER-02`. Minor: the INV-05 table header now duplicates field 1 instead of saying 「示例值（全為 SAMPLE／SYNTHETIC；無實際收件）」; this is cosmetic, not a value/locator defect. |
| **F4 Undefined actors** | **PASS** | 第二節 role table maps 承辦人／承辦角色, 覆核人／覆核角色, 核准角色／權責主管／主管. External 評核委員 is expressly not a fourth internal role and is gated by `HOLD-EVALUATOR-ACCESS-01`. 第十三節 final approval uses 經指定核准角色. |
| **F5 CASE-003 completeness** | **PASS** | 第六節 CASE-003 field 11 lists only `SAMPLE-REVIEW-03`, `SAMPLE-DATE-REVIEW-03`, `SAMPLE-ROLE-REVIEWER-03`, and says 「承辦角色只列於第 13 欄」. Field 13 contains `SAMPLE-ROLE-HANDLER-03`, reviewer, 2026-11-26 due date, 2026-11-27 escalation, and restricted-use pause. 第七節 CASE-003 row 11 excludes the handler and shows 12/12 SAMPLE, 0/12 REAL. Minor: 「以覆核日 2026-11-19 起算」 but day 1 is enumerated as 11-20; the enumerated dates and due date are correct. |
| **F6 CASE-004 authorization / feedback** | **PASS** | 第六節 CASE-004 field 9 states written authorization 2026-10-18–2026-10-31. Field 10 uses `SAMPLE-COURSE-04` / `SAMPLE-SESSION-04` / `SAMPLE-FEEDBACK-COURSE-04`, distinct from Section 4’s `SAMPLE-COURSE-05`. Field 13 contains handler, reviewer, five-workday follow-up to 2026-10-27, authorization/channel check, pause, and escalation. No COURSE-05 sentence leaks into CASE-004. |
| **F7 Field-13 gap inventories** | **PASS** | 第六節 CASE-001 field 13 identifies fields 1–2 as SAMPLE, lists fields 3–11 as missing, and says field 12 is not numbered. CASE-004 field 13 has a sample handler, reviewer, deadline, and pause rule. INV-05 field 13 lists the outstanding field 9 authorization and field 10 training-link gaps and the deadline. No 「無格式欄位待填」 replaces the required inventory. |
| **F8 INV-05 timeline / excerpts** | **PASS** | 第六節 INV-05: filing 2026-11-10, start 2026-11-11, five workdays to 2026-11-17, escalation 2026-11-18. Excerpts A/B and sources A/B are separately coded. The future/non-scheduled warning is present. 12/12 SAMPLE, 0/12 REAL. Minor: field 13/register role says 「未完成時依核定程序提報」 without naming 經指定核准角色, unlike CASE-003/004; the general Section 8 escalation rule supplies the role. |
| **F9 17d official claim** | **PASS** | No 17d assertion remains. 第一節 and 第十一節 assert only page 6, I18-E03, 「感謝函。」 and defer other same-name/adjacent items to the formal source. Official requirement, DOCX ID, and checkbox serial 099 are not conflated. N1’s trace table is present; see below. |
| **F10 Real-looking association** | **PASS** | `原始點協會` is absent. Samples use SAMPLE codes, 「示範組織」, or generic roles. No named real third-party issuer, signature, receipt, or approval is fabricated. |
| **F11 0098 overlap** | **PASS** | 第四節 A explicitly says 0096 does not collect, log, retain, or analyze general course opinions and routes them to DOCX 0098／I18-E06. 第二節 neighbor table and 第十一節 after-table prose separate 0095／I18-E02, 0097／I18-E05, and 0098／I18-E06. No questionnaire items or survey-execution data are imported. |
| **F12 A4, phrases, RESTRICTED, privacy** | **PASS** | 附件四 uses A/B tracking; B is conditional on qualified listing or approved RESTRICTED and formal register assignment. `HOLD-CONTROL-NO-01` includes the qualified/approved RESTRICTED condition. 第十節 privacy is purpose-limited and prohibits public upload of real originals. Minor: 第四節 says 「以下兩種不同內容」 even though A is not collected; the text immediately says A is routed to 0098 and not collected by 0096. |

---

## Prior R12 residuals: F1, F3, N1

### R12 F1 — unsigned-only versus INVESTIGATE: **resolved**

The repair is substantive, not cosmetic. The three relevant locations now agree:

- 第三節流程三第 6 點: unsigned document → missing item + HOLD; only a separate concrete identity/signature/source contradiction, after formal filing, → INVESTIGATE.
- 第三節流程四第 6 點: same, cross-referring to 第八節 EX-03.
- 第八節 EX-03: 「單純未簽名或來源待核是缺口，不自行構成矛盾」; status is HOLD until a concrete contradiction is formally filed.
- 第八節 opening state mapping: 「未簽名本身或單純缺少來源欄位不等於具體矛盾，不得單憑此改列 INVESTIGATE」.
- 第五節欄位 13 and 第十一節 row 3 repeat the same rule.
- EX-08 now uses 「於登錄／建立追蹤時」 for deadline/start/responsibility recording.

No material F1 residual remains.

### R12 F3 — SAMPLE-CASE-INV-05 value and CSV sync: **resolved**

The register row now reads:

`SAMPLE-CASE-INV-05｜演練追蹤碼；非實際收文流水號`

This is exactly field 1 of the INV-05 table. The locator identifies 「下表第 1 列（資料列；欄位 1）〈收件追蹤編號〉」. The CSV row matches. The earlier defect — displaying a table header instead of field 1 — is gone.

Minor new observation: the INV-05 table’s second header cell now also reads `SAMPLE-CASE-INV-05｜演練追蹤碼；非實際收文流水號`, duplicating the first data row. The other cases use a descriptive header such as 「SAMPLE-CASE-003 示範填寫內容（全為 SAMPLE／SYNTHETIC）」 or 「SAMPLE-CASE-004 示例值（封閉演練假設，非真實）」. Restoring a descriptive INV-05 header would improve table quality, but the register value and locator are now correct.

### R12 N1 — Blueprint-required trace table: **resolved**

Blueprint `required_tables_or_figures` requires:

「官方要求—表單欄位—附件定位追溯表」

第十一節 now contains a four-column table:

| 官方要求／正式來源 | 表單欄位 | 文件內證據位置 | 覆核與狀態 |

It covers all 13 fields in four grouped rows:

1. Fields 1–4 — tracking number, receipt date/route, original date/number, issuer identity.
2. Fields 5–8 — identity verification, original medium, custody location, SHA/paper N/A.
3. Fields 9–11 — external-use authorization, training link, review/conflict check.
4. Fields 12–13 — controlled evidence number, missing-evidence/follow-up/deadline/responsibility.

Each row cites the same official source: page 6, I18-E03, 「感謝函。」. Each row gives document/attachment locations and a review/status rule. No 0095/0097/0098 requirement is imported into the table.

**Row-by-row assessment**

| Trace-table row | Official source | Form fields | Evidence location | Review/status | Blueprint fit |
|---|---|---|---|---|---|
| 1 | Page 6, I18-E03, 「感謝函。」 | 1–4 | Section 4 solicitation/A1; Section 5 A2 fields 1–4 | Invitation is not receipt; HOLD if original/receipt information missing | Satisfies |
| 2 | Same | 5–8 | Section 5 A2 fields 5–8; Section 6 cases; Section 7 calculation | Legal-source verification; SHA only for actual electronic file; HOLD if unverified | Satisfies |
| 3 | Same | 9–11 | Section 5 A2 fields 9–11; Section 6 case determinations; A3 correction tracking | Separate evaluation-viewing versus public authorization; conflict check; HOLD; INVESTIGATE only after formal filing | Satisfies |
| 4 | Same | 12–13 | Sections 6–7; Section 9 rejection/correction; A2/A3/A4 | Control number only after review and formal register assignment; HOLD/INVESTIGATE/REJECT rules; SAMPLE, REAL 0 | Satisfies |

**Granularity caveat:** the table groups fields rather than providing one row per field. The Blueprint requires a trace table, not a mandatory 13-row matrix, and the prior repair guidance expressly allowed 「1–13 or grouped」. The table therefore satisfies N1 in substance. A 13-row version would be more granular and easier to audit field-by-field, but its absence is not a material nonconformance.

**Evidence-location caveat:** some locations are broad — for example, A3 is cited for fields 9–11, and A4 is cited for fields 12–13. These are related control records rather than per-field attachment slots. This is a precision issue, not a missing trace table.

---

## Arithmetic checks

All dates and percentages rechecked against the text:

- **CASE-001:** SAMPLE fields 1, 2, 4, 6 = 4/12; HOLD fields 3, 5, 7–12 = 8/12; 4 + 8 = 12; 12 ÷ 12 = 100%; REAL 0/12. Correct.
- **CASE-003:** review 2026-11-19 is Thursday. Enumerated workdays are 11-20 Friday (1), 11-23 Monday (2), 11-24 Tuesday (3), 11-25 Wednesday (4), 11-26 Thursday (5); escalation 11-27 Friday. 12/12 SAMPLE = 100%; REAL 0/12 = 0%. Correct. Minor wording issue: 「以覆核日 2026-11-19 起算」 while day 1 is 11-20; the enumeration removes practical ambiguity.
- **CASE-004:** start 2026-10-21 is Wednesday. Enumerated workdays are 10-21 (1), 10-22 (2), 10-23 (3), 10-26 (4), 10-27 (5). Authorization 2026-10-18–2026-10-31 covers receipt 10-19, review 10-20, and follow-up 10-27. 12/12 SAMPLE = 100%; REAL 0/12 = 0%. Correct.
- **INV-05:** filing 2026-11-10 is Tuesday. Start 2026-11-11 Wednesday. Enumerated workdays are 11-11 (1), 11-12 (2), 11-13 (3), 11-16 (4), 11-17 (5); escalation 11-18 Wednesday. 12/12 SAMPLE = 100%; REAL 0/12 = 0%. Correct.
- **SHA demonstrations:** the `SAMPLE-DIGEST-03/04` strings are 64 hexadecimal characters and are expressly labeled `DEMO ONLY`, uncomputed, and not file digests. No arithmetic or digest claim is overstated.

---

## Crosswalk and neighbor separation

The crosswalk identifies:

- 0095 / I18-E02 — satisfaction-survey mechanism.
- 0096 / I18-E03 — thank-you-letter solicitation, receipt, and verification.
- 0097 / I18-E05 — ability/satisfaction questionnaire analysis.
- 0098 / I18-E06 — survey execution, sample flow, and analysis handoff.

The candidate keeps these distinct:

- 第二節 table explicitly states that 0096 does not replace 0095, 0097, or 0098 and does not infer their actual results.
- 第四節 routes general course opinions to 0098／I18-E06 and says 0096 does not collect, log, retain, or analyze them.
- 第十一節 after-table prose repeats the separation and says 0096 only provides voluntary thank-you-letter solicitation, original receipt verification, and controlled individual-feedback traceability.
- No questionnaire questions, sample-flow statistics, or mechanism-analysis content from neighbors are copied.

The document adds 0098/I18-E06 as a routing neighbor beyond the Blueprint’s two negative-choice neighbors (0095 and 0097). That is appropriate because 0098 is the survey-execution/analysis deliverable and the official item 18 context involves satisfaction surveys; it is used only for separation, not as imported content.

---

## SAMPLE / REAL boundary

Text-level boundary is strong:

- Section 1 says the document is a working guide and form tool, not a third-party thank-you letter, and all SAMPLE/SYNTHETIC examples are not real receipt records.
- Section 4’s reply example is explicitly labeled 「SAMPLE / SYNTHETIC / 虛構訓練情境 / 未實際收發 / 無簽名 / 非 REAL 佐證」 at top and bottom. The feedback sentence is expressly 「不是受訓者原話」.
- Section 6 cases are labeled SAMPLE/SYNTHETIC; CASE-001, CASE-003, CASE-004, and INV-05 all state REAL 0/12.
- CASE-003’s RESTRICTED status is conditional on real verification and is explicitly not a real organizational decision.
- CASE-004’s 「合格列件」 is a hypothetical single-status exercise, not an actual listing or approval.
- Section 12 identifies all sample facts and replacement sources.
- Section 13 says the document does not attach a consent form and does not represent that any authorization was obtained.

No fabricated third-party letter, real name, signature, receipt, authorization, review, or organizational approval was found in the text. The 12/12 SAMPLE rates are consistently distinguished from real evidence and are not presented as actual performance.

**Unverified:** binary metadata, embedded objects, fonts, layout, page coverage, tracked changes, and visual rendering.

---

## CSV / register synchronization

The CSV contains 121 data rows, matching the packet’s stated count and the body’s Table 12 row count. The keys are unique. The body and CSV appear row-for-row consistent for the substantive facts I checked, including the corrected `SAMPLE-CASE-INV-05` row and the Section 9 correction rows.

Specific checks:

- `SAMPLE-CASE-INV-05` value and locator match field 1 of the INV-05 table. **Corrected.**
- `SAMPLE-DUE-RULE-INV-05` is absent. **Stale row removed.**
- `SAMPLE-ACTION-03`, `SAMPLE-ACTION-04`, and `SAMPLE-ACTION-INV-05` mirror the body’s field 13 text and role assignments.
- `HOLD-GAPS-01` mirrors CASE-001 field 13.
- `SAMPLE-COMPLETENESS-01` mirrors the Section 7 CASE-001 calculation paragraph.
- Section 9 rows `SAMPLE-CASE-002`, `SAMPLE-OLD-CATEGORY-01`, `SAMPLE-NEW-CATEGORY-01`, `SAMPLE-CORRECTION-REASON-01`, `SAMPLE-ROLE-HANDLER-02`, and `SAMPLE-ROLE-REVIEWER-02` use exact data-row/field locators.

**Minor register issues, non-blocking:**

- 第十三節 A5 says 「以 fact_id 對照第十二節表格五欄」, but Table 12 and the CSV each have six columns. The A5 prose immediately lists six comparison items (unique key, value, location, source, role, review points), so this is an internal count typo.
- Some locators are section- or table-level rather than exact field-level: `SAMPLE-COMPLETENESS-01` (「第七節狀態標記率核算及結果段」), `SAMPLE-COMPLETENESS-04` (「第七節 SAMPLE-CASE-004 計算表與結論」), and the `PENDING-*` rows (letter section/placeholder locations). These are less precise than the Section 9 and Section 6 row/field locators, but they identify the correct passage.
- Several facts intentionally repeat the full text of one cell — for example, `SAMPLE-ACTION-03` and its date/role keys, or `SAMPLE-ACTION-INV-05` and its date/role keys. This is redundant but consistent.
- A few CSV values paraphrase body formatting rather than quote it verbatim — for example, `SAMPLE-DATE-LETTER-04` and `SAMPLE-COMPLETENESS-04`. The meaning matches the body; this is a precision/editorial issue, not a semantic mismatch.

I did not recompute the CSV SHA-256; I bind to the packet’s stated hash.

---

## Operator usability

The document is substantially usable by an association administrator:

- 第二節 gives a three-role glossary and explicit scope boundaries.
- 第三節 gives eight sequential processes with inputs, actions, completion conditions, responsible roles, records, and exception handling.
- 第五節 provides a 13-field blank receipt/verification form with definitions and verification guidance.
- 第六節 provides complete SAMPLE/SYNTHETIC worked cases for HOLD, RESTRICTED, qualified-listing, and INVESTIGATE branches.
- 第七節 provides reproducible 12-field calculations.
- 第八節 provides a single-status mapping and EX-01–EX-09 exception table.
- 第九節 provides a correction/tracking form and a synthetic correction example.
- 第十節 provides custody and privacy rules.
- 第十一節 provides the official trace table and neighbor separation.
- 第十二節 provides the replacement register.
- 第十三節 provides version/signature fields, attachment inventory, A4 access-control form, and a real-data promotion checklist.

**Minor usability issues:**

- 第一節 uses 「HOLD」 once before it is defined in 第八節; a first-use gloss such as 「保留列管（HOLD）」 would help the 30-second reader.
- 第四節 says 「以下兩種不同內容」 even though A is not collected; the text immediately clarifies A is routed to 0098, but the framing is slightly confusing.
- The INV-05 table header duplication and the A5 「五欄」 count are editorial.
- The CASE-003 start-date wording and the INV-05 escalation-recipient shorthand are minor ambiguities, not blockers.

---

## Material findings

**None.** No material F1–F12 defect, no unresolved R12 F1/F3/N1 residual, no official-focus substitution, no neighbor-content import, no arithmetic error, no real/synthetic boundary breach, and no fabricated third-party evidence were found in the supplied text.

## Minor non-blocking observations for a future editorial pass

1. Restore a descriptive header to the INV-05 table instead of duplicating field 1.
2. Correct 第十三節 A5’s 「五欄」 to six columns, or say 「五個非鍵欄位」.
3. Add a 異動日期 row to the Section 9 synthetic correction example, matching the blank correction table.
4. Clarify CASE-003’s 「以覆核日 2026-11-19 起算」 as 「自次一工作日 2026-11-20 起算」.
5. In INV-05 field 13/register role, name 經指定核准角色 as the escalation recipient, as CASE-003/004 do.
6. Reconsider 第四節’s 「以下兩種不同內容」 wording so it does not imply 0096 collects category A.
7. Tighten `SAMPLE-COMPLETENESS-01/04` and `PENDING-*` locators to page/table/field level where possible.
8. The manifest’s `official_checkbox_text` reads `"感謝函：索取稿及原件登錄，不假裝已收函"`, which is an internal operational gloss rather than the exact page-6 text `"感謝函。"`. The body correctly uses the official text; the manifest field should be corrected or relabeled so it does not imply the official checkbox text includes that gloss.

---

## Final disposition

**Overall: PASS** for DOCX 0096 R13 SHA-256 `6ece53befed3ecb1b42e523b80da80decd33b0a7d55e4e1fe75ddf79b905d445`, body SHA-256 `25f30e48576e8a2891b5882ea2c4b0337a33feffb2c7ae8fb44ebe9a650f3a15`, and CSV SHA-256 `16d238c7fde83318c3d9f5c5c4c8a295ee210c34edf9ba68759a78991a0c1a91` (121 data rows).

The prior R12 material residuals F1, F3, and N1 are resolved. F1–F12 all pass. The remaining observations are editorial precision issues, not material semantic defects. This verdict is not an organizational acceptance, and it does not substitute for binary, font, layout, metadata, or visual verification. No files were edited, no tools were used, and no browsing was performed.
