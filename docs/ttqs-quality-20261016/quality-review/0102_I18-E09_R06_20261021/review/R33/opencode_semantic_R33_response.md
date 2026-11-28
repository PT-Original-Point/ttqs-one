PARTIAL

**Candidate SHA-256**

`F17048266910F962D2B5DADBA62CB91863F1CECD2684486D80D3C9A0CEEF1C3A`

Semantic-review verdict only. This is not formal acceptance. No files were changed.

## Coverage and limitations

- Reviewed all 78 pages of the supplied page-by-page candidate text, including the cover, §§1–15, Forms A–F, §§10.1–10.3, §11 calculations, §§12.1–12.3 registers, §13 filing, §14 exceptions, and the version history.
- Read both complete package source documents: `source\SOURCE_PACKET_0102_I18-E09_R01.md` and `source\UNIQUE_BLUEPRINT_0102_I18-E09_R01.md`.
- Compared the candidate against the Blueprint’s genre, workflow, forms, sample boundaries, rejection/hold rules, and arithmetic requirements.
- No network, shell, GUI, or write operations were used. The binding candidate SHA was not independently recomputed. Visual/layout QA was not assessed and is separately recorded.
- The underlying official PDFs were represented by the source packet’s page 7/page 4 facts; I did not reopen the PDFs from the network. The historical 0102 baseline binary was unavailable, so historical body reuse could only be checked for textual similarity, not binary comparison.

## What substantially complies

- **Genre and purpose are correct.** The document is unmistakably a third-party evidence acquisition, authenticity-verification, training-linkage, and case-register tool, not an award certificate or success story.
- **Workflow is substantially complete.** It covers intake, consent/privacy, minimum-necessary requests, independent organizer verification, authenticity checks, training linkage, decision, filing, hold/reject, timeout, withdrawal, suspicious-source handling, and annual review.
- **Forms A–F are present and generally usable.** Form B and Form C are marked `SAMPLE TEMPLATE—NOT SENT`; Form D has 15 checks; Form E has the required linkage columns; Form F contains disposition, reasons, evidence locators, missing items, owner, deadline, reviewer, and next action.
- **Evidence versus training outcome is well separated.** The document correctly distinguishes self-report, learner screenshot, organizer source, checked original, training linkage, and formal scoring. It avoids claiming that an award proves training causation or a TTQS score.
- **The 2-point/4-point qualification is accurate.** It correctly treats the page 7 award reference as an example in the 4-point evidence list, not a score guarantee, and correctly describes the page 4 2-point standard as learner/target-customer belief in ability improvement.
- **The real/sample boundary is strong overall.** No real award, real certificate, real organizer reply, real signature, real association approval, or real-third-party original is asserted. The document repeatedly states `SAMPLE / SYNTHETIC`.
- **The 0/2 arithmetic is correct.** The sample dataset has two synthetic claims, zero verified award cases, and `0/2 = 0%`. The caveats correctly say this is not association performance, award rate, TTQS score, or proof that no award exists.
- **No material misuse of the unrelated `0102_122` artifact was found.** It is identified as a numeric-ID collision and not used as source material.

## Findings

### 1. High — Case register is transposed and contradicts its own “one row per claim” rule

**Page/section:** p.52–53, §12.1.

**Precise evidence:** p.52 says: “下表以欄位為列、案例為欄” and the table is indeed field rows × `CASE-01`/`CASE-02` columns. But p.53 immediately states: “一案一行，不把兩案寫在同一行.” The Blueprint item 13 requires a case register with one row per claim and a CSV-like structure.

**Why it matters:** The register is the operational index. The current orientation makes adding a third claim require a new column, weakens row-level review, and directly contradicts the document’s own maintenance rule.

**Required correction:** Transpose §12.1 to one row per `case_id`, with columns for learner ref, competition, claimed result, evidence state, case status, consent, source locator, verification status, training-link status, disclosure authority, decision, owner, deadlines, synthetic fact IDs, real-source requirement, and state. Keep the two sample cases as two rows.

### 2. High — R33’s locator repair is incomplete; several replacement-register locators are wrong or stale

**Page/section:** pp.55–63, §12.2; p.77, R33 history row.

**Precise evidence:**

- `F-0102-021` (p.55) cites CASE-01 Form E as “Table 21,” while `F-0102-008`, `F-0102-010`, `F-0102-011`, and `F-0102-035` cite the same CASE-01 Form E as “Table 22.”
- `F-0102-031` (p.60) also cites CASE-01 Form E as “Table 21”; the instructor observation is in the CASE-01 filled matrix, not that blank table.
- `F-0102-027` (p.59) and `F-0102-032` (p.60) cite CASE-02 Form E as “Table 22,” while `F-0102-014` and `F-0102-017` cite the same CASE-02 Form E as “Table 23.”
- `F-0102-036` (p.61) cites “Form D Table 19 row 13” for the duplicate/repost issue, but the duplicate check is Form D #12; row 13 is “同意與公開範圍” (p.31).
- `F-0102-045` and `F-0102-046` (pp.62–63) still cite “Table 34 row 7” even though the R33 history row (p.77) says the register was changed to “§12.1 欄位 × 個案語意座標.”
- The supplied page text visibly names only `表 18A`. References to `表 16` (p.4, p.39, p.49, p.73, p.78), `表 26`/`表 43` (p.11), and `表 36` (p.49) have no visible table captions, so a reader cannot unambiguously resolve them. `F-0102-023` and `F-0102-029` also show duplicated “CASE-01 CASE-01” / “CASE-02 CASE-02” text.

**Why it matters:** The document’s central promise is that the next person can locate the source. A wrong table or stale row coordinate can send the reviewer to the wrong evidence or make the register unusable.

**Required correction:** Audit every locator in §12.2. Correct 21→22 for CASE-01 Form E, 22→23 for CASE-02 Form E, and “Table 19 row 13” to the duplicate item’s actual Form D row (#12). Replace all table-number-only references with stable locators such as “§9.3 CASE-01 Form F, row 7” or “§12.1, `CASE-01`, `案件狀態`.” Remove the stale “Table 34 row 7” references, add visible table captions if table numbers are retained, and clean duplicated case text.

### 3. Medium — The two SAMPLE cases do not fully realize the Blueprint’s request-pending versus consent/identity-hold contrast

**Page/section:** p.15 §4.2; p.41–43 §§9.3–9.4; p.45–47 §§10.1–10.2; p.15, p.45.

**Precise evidence:** Both CASE-01 and CASE-02 have `consent_status UNKNOWN` and no valid consent. CASE-01 says the request draft and Form C draft “都不得送出” until consent is obtained (p.45). CASE-02 is HOLD for “同意不足＋身分不足” (p.43). The Blueprint item 11 asks for one synthetic case that “can be requested but remains pending” and another that “lacks consent or sufficient identity match and is held.”

**Why it matters:** As written, neither case is currently request-ready. CASE-01 is only “requestable after consent”; CASE-02 has consent plus identity/team blockers. This weakens the intended demonstration of a source-request-pending case.

**Required correction:** Either give CASE-01 a clearly labelled synthetic limited consent state—not a real signature or real approval—so that its organizer request can be shown as `PENDING_REAL_SOURCE`, or explicitly redefine the contrast and explain that both cases are pre-consent by design. Keep CASE-02’s consent/identity blockers distinct. The correction must remain visibly `SAMPLE / SYNTHETIC`.

### 4. Medium — `course_source` sample values do not follow the form’s allowed-value rule and are semantically ambiguous

**Page/section:** p.14, §4.1; p.15, §4.2.

**Precise evidence:** The field definition says: “來源類別＋檔名/位置；無可核來源填 `UNKNOWN`.” The sample instead uses: “`SYNTHETIC ONLY；無真實課程計畫、名冊或評量來源已核實`” and “`SYNTHETIC ONLY；無真實課程來源已核實`.” The phrase can be read as “there is no real course plan/roster/assessment and the source has been verified,” or “no real source has been verified,” which is contradictory for a required source-status field.

**Why it matters:** `course_source` is part of the training-link evidence chain. An ambiguous value can be mistaken for a verified course source.

**Required correction:** Put `UNKNOWN` in `course_source` exactly as the form rule requires. Move the explanation to `notes`: “無真實課程計畫、名冊或評量；課程來源 UNKNOWN，未核實。” Apply the same correction to both cases.

### 5. Medium — CASE-01 identity is mischaracterized as “對不上” when the record says UNKNOWN

**Page/section:** p.33, §7.3.

**Precise evidence:** The summary says: “原因不是『證明造假』，而是『無法確認＋同意不足＋身分對不上』.” But Form D #9 for CASE-01 is `未知` (p.33), and Form F #6 is `未知` (p.41). There is no official list or compared name. The document therefore converts an unresolved identity question into an adverse-sounding mismatch.

**Why it matters:** “身分對不上” is materially different from “no basis to compare.” It can push a reviewer toward a rejection mindset, contrary to the document’s own “UNKNOWN is not REJECTED” rules.

**Required correction:** Replace “身分對不上” with “身分無法對照／UNKNOWN.” Reserve “對不上” for a confirmed comparison against an official list. Keep the case at HOLD.

### 6. Medium — CASE-02’s internal review date is already past at the R33 date, with no replacement date

**Page/section:** p.15 §4.2; p.43 §9.4; p.47 §10.2; p.52 §12.1; p.53 maintenance rule.

**Precise evidence:** CASE-02’s `internal_review_date` is `2026-10-20`. R33 is dated `2026-10-23` on the cover/version history (p.1, p.77). The processing narrative ends at 2026-10-20 and says “維持 HOLD,” but no new future internal date is set. This conflicts with p.53: “期限一到就更新，不讓表格變成裝飾.”

**Why it matters:** The sample is a working example of active case control. A missed internal review date with no next date makes the example look stale and gives the administrator no next action.

**Required correction:** Record that the 2026-10-20 review occurred, set a new future `internal_review_date` with a reason, and update Form A, Form F, and §12.1 consistently. If the sample is intentionally frozen, label it explicitly as a historical snapshot and add a separate next-review date.

### 7. Medium — Form F’s “not a second ten-item gate” instruction remains operationally ambiguous

**Page/section:** p.4, one-minute guide step 7; pp.37–39 §§9.1–9.2; p.49 §11.1; p.73 §14.1.

**Precise evidence:** The document repeatedly says Form F is a consistency summary, “不是第二組十項全是的獨立門檻” (p.39; also p.4, p.49, p.73). But Form F contains ten `是／否／未知` checks. Several items are effectively mandatory through Form D: #9 “無重複、變造或明顯矛盾” depends on Form D #12, and #10 “來源可定位、可保存” depends on Form D #14. The form does not mark which items are core gates, which are descriptive, or what happens when a non-core item is “否.”

**Why it matters:** A small-association administrator may treat Form F as either a full ten-item gate or a purely narrative summary. Both readings produce different decisions.

**Required correction:** Add a “gate role / linked requirement” column to Form F mapping each item to one of the five core conditions or a Form D item. State the consequence of every `否` and `未知`. Alternatively, simplify Form F to mirror only the five core conditions plus optional narrative fields.

### 8. Medium — CASE-01’s HOLD reason and “缺少項目” list omit consent/authority

**Page/section:** p.41, §9.3; p.45, §10.1; p.48 comparison.

**Precise evidence:** Form F row 7 for CASE-01 is “否” because there is “未提供簽署或明確同意” (p.40–41). But the same section says: “示範判定：HOLD（待真實來源）” and “缺少項目：官方結果頁或主辦確認、獎狀影本、得獎者身分對照、競賽規則” (p.41). Consent and disclosure authority are absent from the missing-items list. p.45 says there is no consent/authorization; p.48 lists “同意與聯繫授權未取得” as a main blocker.

**Why it matters:** The decision summary understates one of the actual blockers and could lead the reader to think obtaining the source alone would clear the case.

**Required correction:** Add “有效同意與對外聯繫／揭露授權” to the missing-items list and change the label to something like `HOLD（來源＋同意／授權）`. Keep the same HOLD reason consistent across Form F, §10.1, and §12.1.

### 9. Low/Medium — Replacement register contains a duplicate-index row that is not a fact and uses the training-link column for a duplicate marker

**Page/section:** p.61, `F-0102-036`; p.54, §12.2; p.65, state vocabulary.

**Precise evidence:** `F-0102-036` says it is the “重複索引” of `F-0102-016`, “不另計事實,” but it is still given a separate `fact_id` row. Its training-link cell contains `DUPLICATE_OF=F-0102-016` instead of a training-link status. §12.2 says “一個合成事實一行,” and the state vocabulary is `SYNTHETIC_PLACEHOLDER`, `AWAITING_REAL_SOURCE`, `VERIFIED_REAL`, `RETIRED`.

**Why it matters:** The row is useful as a cross-reference but conflicts with the one-fact-per-row rule and can confuse counting or status review.

**Required correction:** Remove the duplicate row from the one-fact-per-row register and place the `DUPLICATE_OF=F-0102-016` cross-reference in a separate notes/alias field, or mark it `RETIRED` with an explicit duplicate-of note. Do not use the training-link column for a duplicate marker.

### 10. Low — The blanket “no reply is fabricated” statement is overbroad

**Page/section:** p.44, §10 boundary statement; p.45 §10.1; p.47 §10.2.

**Precise evidence:** p.44 says: “本文件不虛構任何送出、回覆、簽章、核准或得獎證明.” But p.45 contains a synthetic “學員來電，說自己參加競賽得到佳作”; p.47 contains a synthetic learner statement that “示範隊” is a nickname and an ambiguous “可以拿去用.” These are clearly labelled synthetic and are not real third-party replies, but the absolute “no reply” sentence is literally contradicted by the synthetic narration.

**Why it matters:** The real/sample boundary is otherwise strong; this wording unnecessarily undermines it.

**Required correction:** Qualify the sentence: “本文件不虛構任何真實送出、第三方／主辦回覆、簽章、核准或得獎證明；合成學員敘述僅為流程演練，且均標示 SAMPLE。” Keep the synthetic learner narration explicitly marked.

## Explicit check of both SAMPLE cases

| Item | `SYN-0102-CASE-01` | `SYN-0102-CASE-02` |
|---|---|---|
| Claim date | 2026-10-05 | 2026-09-30 |
| Course | 2026-03-02–2026-04-10, 36 hours | 2026-01-05–2026-02-15 |
| Competition | 示範盃技能競賽, 2026-08-22, synthetic | 示範盃技能競賽, 2026-08-22, synthetic |
| Claimed result | 佳作 | 冠軍 |
| Evidence | Synthetic screenshot without URL; no third-party original | Synthetic repost screenshot; no original link, no award certificate, no team-name match |
| Consent | `UNKNOWN`; no valid consent | `UNKNOWN`; no valid consent |
| Evidence state | `RECEIVED_UNVERIFIED` | `RECEIVED_UNVERIFIED` |
| Case state | `HOLD` | `HOLD` |
| Internal review | 2026-10-26, future at R33 | 2026-10-20, past at R33; no replacement date |
| Verified award | `0` | `0` |
| Real award asserted? | No | No |

**0/2 calculation:** Two synthetic claims are in scope. Verified award cases = 0. Therefore `0/2 = 0%`. The arithmetic and the stated caveats are correct. The candidate correctly says this is a workflow-control metric only, not an association award rate, performance measure, or TTQS score.

**Real-evidence boundary:** `real_awards = UNKNOWN`; `verified_awards = 0` for this SAMPLE dataset only; `formal_acceptance = NOT_GRANTED`. The candidate does not assert a real association approval, real signature, real certificate, real organizer reply, real winner list, real award, or real execution. CASE-01 and CASE-02 remain HOLD because no third-party source, consent, identity match, and training linkage are established.

## Conclusion

The core genre, purpose, workflow, forms, evidence/outcome distinction, 2-point/4-point qualification, sample boundary, and 0/2 arithmetic are sound. The document is not ready for PASS because material register and locator defects remain, and several status/threshold statements are inconsistent or under-specified.

**Verdict: PARTIAL. No formal acceptance is granted.**