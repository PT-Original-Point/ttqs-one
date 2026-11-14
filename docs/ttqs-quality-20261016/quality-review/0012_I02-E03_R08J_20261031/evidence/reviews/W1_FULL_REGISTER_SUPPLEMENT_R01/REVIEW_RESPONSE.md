# Exact-SHA Semantic Review Verdict — R08J

**Candidate SHA-256:** `1b2ad16bb36d9ba867fd517067d0e2c61529b1bfe390e045e01cd05fca7795e6` (bytes 75966, per packet receipt)
**Review scope (independent, completed):** full candidate body in document order including all 不得/懸置控制 tables (§2–§10), §12 register SYN-001–SYN-068, §13; official source PDF page 1 extract; verbatim Unique Blueprint 0012 row; verbatim neighbor rows 0011/I02-E02 and 0013/I02-E04; full replacement register CSV (68 rows). Note: the packet's R08H/R08I/R08J history sections are **empty** — no repair receipts exist, so all "prior finding closure" is judged solely on the current candidate text.
**Model identity:** UNKNOWN — I cannot independently attest which model produced this review; the CLI provides no attestation. (Environment labels may exist, but they are not an independent attestation.)

```json
{
  "work_id": "TTQS-0012-W1-SEMANTIC-R08J-FULL-20261031-01",
  "candidate_sha256": "1b2ad16bb36d9ba867fd517067d0e2c61529b1bfe390e045e01cd05fca7795e6",
  "verdict": "PASS",
  "verdict_scope": "semantic content only; not formal acceptance; DOCX rendering/font checks not performed",
  "checks": {
    "official_scope_and_genre_match": true,
    "required_operational_elements_complete": true,
    "calculation_semantics_correct_and_unconflated": true,
    "prior_findings_P_U_source_and_SYN042_fixed_in_text": true,
    "register_alignment_complete_no_orphan_synthetic_facts": true,
    "no_fabricated_REAL_or_third_party_or_signature_or_decision": true,
    "negative_neighbors_0011_0013_rejected": true,
    "title_blind_identifiable_and_directly_usable": true
  },
  "findings_count": {"medium": 1, "low": 3, "informational": 3},
  "critical_requirements_absent": false,
  "model_identity": "UNKNOWN",
  "formal_acceptance": false
}
```

## Detailed finding list

**Confirmed correct (no defect):**
1. **Scope/genre.** Official line 「補助參與機構公開招生課程或進階課程優惠辦法之規定。」 verified verbatim in the official page-1 extract under item 2「對外明確的訓練政策」常見參考佐證資料， matching the candidate's own claim (「30秒使用說明」¶3; §11 table). The work product is an operable discount/subsidy procedure document (roles, eligibility, application, review, calculation, approval boundary, notification/appeal, correction, tracking, retention) — correct genre for an `evidence_record`.
2. **Calculation semantics — all seven values verified, not conflated:** E = max(0, 6,000−0−0) = 6,000; P = 0 explicitly labeled as a SAMPLE assumption, not an audit result (§7 row 013, §9.2, SYN-066); U = max(0, 6,000−0) = 6,000 (§7 row 014, §9.2, SYN-067); rate amount 6,000×20% = 1,200; B = min(1,200; 1,500; 4,000; 7,000; 6,000) = 1,200 with the last min-term correctly identified as U (§9.2 row 014); remaining unpaid 4,800 (SYN-028) and remaining budget 5,800 (SYN-029) are kept in **separate** rows with an explicit no-confusion note. No identity mismatches between body, §9.2, and register.
3. **P/U-source prior findings closed in text.** The no-zero-default rule (「空白或不代表未付款…不得填0」; UNKNOWN→HOLD) is enforced consistently at §7 rows 013–016, §7 matrix rows 013–016, §9.1, §9.2 note, §9.3, and register SYN-066–SYN-068. Payment source/locator fields exist (§7 rows 015–016).
4. **SYN-042 locator fix verified.** Register row SYN-042 locates 「草案版本 0.2」 at §13 文件識別項; §13 indeed states it. Closure confirmed against the current text.
5. **Register alignment.** All 68 SYN rows resolve to body locators; no unregistered synthetic fact found (dates 2026-11-02/03/04/05/10/12, roles S-ADM-01/S-APP-01/S-REV-02/S-COURSE-01/S-CALC-01/S-FIN-01/S-ORG-01/S-LEARNER-01, amounts 6,000/1,500/4,000/12,000/5,000/7,000/1,200/4,800/5,800, declaration text, correction entry, monthly metrics all have owning rows). Monthly report sums check (0+0+0+1=1); N/A and UNKNOWN-not-zero rules consistently applied.
6. **Fabrication control.** Final status HOLD with no approver, no date, no signature, no budget, no third-party artifact; §13 explicitly prohibits REAL marking. Nothing claims association decisions or execution.
7. **Negative neighbors.** §1.3 and §11 (用途辨識 + 相近需求分工) explicitly reject 0011/I02-E02 (market positioning) and 0013/I02-E04 (annual course publication); both directions stated in the neighbor rows are reciprocated.
8. **Title blind test.** With title/filename masked, sections 1–11 identify the deliverable as a discount/subsidy regulation via its unique mechanism set (public-recruitment/advanced-course classification, subsidy rate/ceilings/available-quota, offset formula, conflict-of-interest, appeal, post-course reconciliation).

**Findings (none blocking):**

- **F-01 (medium) — Official-requirement↔form-field↔attachment-locator traceability table not realized as a single explicit table.** Blueprint `required_tables_or_figures` demands 「官方要求—表單欄位—附件定位追溯表」. The substance exists but is dispersed: §11 maps official requirement → document sections (not per field), and §7's matrix maps field → source/locator per field. No one table joins all three axes.
 *Smallest repair:* add ~5 rows to §11 or a small 3-column table (official row → form fields → attachment locator) without touching any other text.
- **F-02 (low) — Metric denominator wording drift in §10.3.** Control row 004 defines 「完整度＝可讀欄位件數／受理數」， while the SAMPLE monthly metric is 「正式來源核驗完成率」 with a different stated denominator (「須核驗資格或金額的唯一正式受理非測試案件」, SYN-062). Related but not identical; flag to keep no two names for the same ratio.
 *Smallest repair:* one clause in §10.3 row 004 distinguishing 完整度 from 來源核驗完成率 or unifying the term.
- **F-03 (low) — §12 preamble grouping inaccurate.** It says SYN-043–056 are 追蹤頻率/觸發/期限 examples, but SYN-043–045 are role codes, the §7 responsibility mapping, and the declaration full text.
 *Smallest repair:* reword the grouping sentence to "SYN-043–045 角色/責任映射及聲明示範；SYN-046–056 更正追蹤與追蹤頻率示例".
- **F-04 (informational/cosmetic) — §13 contains two near-duplicate 「文件狀態：SAMPLE／SYNTHETIC…」 bullets.** Merge or differentiate; no semantic conflict (both proscribe LINE/REAL).
- **F-05 (informational) — Receipt traceability gap.** The packet's R08H/R08I/R08J sections are empty, so fix verification rests on the candidate text itself (this review found the fixes present, but no independent receipts cross-check the repair history).
- **F-06 (informational/out-of-scope) — Font floors (body ≥10.5pt, tables ≥9.5pt), pagination, and visual page checks are not assessable from extracted text/tables.** Requires a DOCX rendering check under a separate UI/layout review; excluded from this semantic verdict.

**Conclusion:** For candidate SHA `1b2ad16b…7795e6`, every critical semantic requirement is present and correct; the seven headline amounts/formula values do not conflate; prior finding areas (payment P / unpaid U / source-verification fields; SYN-042 locator) are verifiably fixed in the current text; the register is complete and aligned; nothing REAL or third-party is fabricated; both negative neighbors are rejected. **Verdict: PASS** with F-01 recommended for the next repair round. This is not formal acceptance.
