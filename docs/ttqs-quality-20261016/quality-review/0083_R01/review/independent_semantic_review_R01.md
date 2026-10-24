# Independent exact-content review — DOCX 0083 body

**Reviewed body SHA-256:** `d37dccab2a9a7b20f235f55dbc9dba9a6c46850ad4949b3aecd5f3c79a743751` (computed; matches).

**Verdict: FAIL** — the mandatory 81-row register is absent/misstated, and the body contains an unsourced association fact. These are material, not editorial.

## Material findings

**1. Critical — The 81-row replacement register is absent and is not coextensive with the body’s SAMPLE values.**
- **Locators/quotes:** L677: “請以配套的 81 列登錄表 … 對應 R-001 至 R-081.” L682: “未登錄的 SAMPLE 值不得留在正文、表格或附件.” Extra SAMPLE-bearing fields include L312 (“G1-04 技能缺口”), L318 (“G1-10 目標期／天數 | 84 天”), L327–L329 (“G1-19… SAMPLE ONLY”; “G1-20… SAMPLE ONLY”; “G1-21… 2026-03-09／SAMPLE v1”), and L359–L361 (T1-12 self-report quotations). No R-001–R-081 table appears before the body ends at L688.
- **Requirement:** Blueprint §7.5 (R-001–R-081 table), §12.1 (清冊鎖), §12.5 (“未入冊之 SAMPLE 值即視為洩漏 → REJECT”), §13 (Writer condition 4; FAIL condition “列數不符”), Appendix E; source packet §5.
- **Why:** A cross-reference to an unattached CSV is not the register. The body’s extra fields carry SAMPLE values that the blueprint’s 81 rows do not cover, so the claimed 81-row count is not a complete inventory; the body violates its own L682 rule. The replacement/QA chain cannot be verified.
- **Correction:** Insert the full six-column R-001–R-081 table in §7.5/Appendix E. Because 81 rows are locked, remove or merge the extra SAMPLE-bearing fields into the blueprint’s locked fields (or explicitly expand the register and stop calling it 81). The narrowest edit is to restore the locked field set and insert the table.

**2. High — The locked G1/T1/A1/E1 field-ID crosswalk is broken.**
- **Locators/quotes:**
  - G1: L127 (“G1-04 | 技能缺口與學習連結”) vs Blueprint G1-04 = 行動目標; L315 (“G1-07 基準值 | 4 次”) vs Blueprint R-009 = G1-07 目標值; L319 (“G1-11 目標期限”) vs Blueprint R-010 = G1-08 期限; L197 (“T1-10 = T1-05 ÷ G1-09 的目標值”) vs Blueprint target value G1-07.
  - T1: L178 (“T1-12 學員自述”) vs Blueprint R-027 = T1-12 協助請求連結; L184 (“T1-15 證據… T1-16 授權… T1-17 下次角色／期限; T1-18 狀態”) vs Blueprint R-028–R-031 = T1-14–T1-17.
  - A1: L237/L661 A1 table has no A1-00–A1-07 IDs, but L538 says “補 A1-03、A1-04.”
  - E1: L260/L266 E1-05 = 連結, E1-06 = 可定位, E1-07 = 授權, vs Blueprint E1-05 = 可定位, E1-06 = 授權, E1-07 = 可讀性.
- **Requirement:** Blueprint §3–§6, §7.5, §12.1–§12.2, §13; source packet §3.2–§3.3.
- **Why:** The register and decision table use field IDs. With these shifts, R-009/R-010 and R-027–R-031 point to different fields; a user following the body’s IDs cannot locate the register rows. The added self-report/authorization columns are substantively useful, but the uncoordinated renumbering breaks the 81-row crosswalk.
- **Correction:** Restore the blueprint IDs (or add an explicit old→new mapping table) and update every internal reference; label A1-00–A1-07; align E1-05/06/07.

**3. High — Unsourced association fact.**
- **Locator/quote:** L609: “協會為志工基礎運作；本文件只示範如何記錄一位學員的訓後行動與追蹤。”
- **Requirement:** Blueprint global status/§1/§7/§13; source packet §1/§4; review requirement that no invented association, institution, or real operation appears.
- **Why:** This is an affirmative claim about the association’s real operating model, not a SAMPLE/PROPOSED statement, and no source in the attached packet supports it. It sits beside the body’s own denial of association facts and can be mistaken for evidence.
- **Correction:** Delete the clause or replace it with “本文件不主張協會之組織型態或實際運作方式；以下僅為合成示例.”

**4. High/Medium — Genre/scope is narrowed to volunteer service.**
- **Locators/quotes:** L4 (“本紀錄供志工服務培訓承辦…”), L24 (“主要讀者 | 志工服務培訓承辦…”), L63 (“志工服務或模擬服務情境中的訓後實作”).
- **Requirement:** Blueprint §1.4 (purpose/readers), §2; source packet §1–§2 (unique genre = 學員行動計畫追蹤紀錄; the synthetic case is independent).
- **Why:** Official 0083 applies to individual trainee action plans in training institutions generally. These lines make volunteer service the applicability condition, not just the §8 synthetic setting; this can exclude other training contexts and blur the sample/real boundary. The reader row also narrows the blueprint’s reader set.
- **Correction:** Replace with “供培訓承辦…” and “各類訓後實作；志工服務僅為第 8 節合成示例.”

**5. Medium — Period vs cumulative threshold is misapplied.**
- **Locators/quotes:** L326 (“G1-18 成功判準 | 累計達成率 ≥80%”); L398 (“T1 與 T3 的本期達成率均為 75.0%，低於示例門檻 80%”).
- **Requirement:** Blueprint §7.1 G1-18 (cumulative ≥80%), §7.4, §8.5; body §9.3 (period and cumulative must be separate).
- **Why:** A cumulative 80% threshold is being used to judge period rates. The period rates are 75/100/75; the cumulative rates are 25.0/58.3/83.3. The PARTIAL conclusion is still supportable by AID/evidence, but the stated reason is a category error.
- **Correction:** Keep the conclusion but reword: “即使累計 83.3% 達到數值門檻，T1/T3 本期僅 75.0%，且 AID/證據未結，故仍判 PARTIAL” — or define a separate period threshold.

**6. Medium — Blank forms are not fully executable; A1 references dangle.**
- **Locators/quotes:** L127, L135, L137, L139 (G1 rows with no 缺漏處理); L178/L184 (T1 table has no per-field 缺漏處理 column); L237/L661 (A1 table lacks A1-00–A1-07 IDs); L538 (“補 A1-03、A1-04”). The body’s own L118 says “每個欄位都應有用途；缺漏時依右欄處理.”
- **Requirement:** Blueprint §3–§6 (each field has definition/options/missing handling), §12.3 (every field has definition and missing handling); source packet §3.2, §4.
- **Why:** Four G1 rows have no missing disposition; T1/A1/E1 lack per-field missing handling; the decision table points to A1-03/A1-04 that the form never labels. Users cannot apply the forms consistently.
- **Correction:** Add the missing G1 dispositions; add a 缺漏處理 column/table to T1/A1/E1; label A1-00–A1-07; replace “A1-03、A1-04” with the exact column names/IDs.

**7. High/Medium — Blueprint-mandated control artifacts are absent.**
- **Locators/quotes:** L19 (“正文版本 | R01；設計依據為 UNIQUE_BLUEPRINT_0083_R03”) — no §1.2 SHA table; L557 (“## 12. 隱私、最小資料、語言與保存”) and L597 (“## 13. 跨文件邊界”) — no content lock/consistency matrix/Word spec, no Table-N1; the body ends at L688 with no appendices A–E.
- **Requirement:** Blueprint §1.2 (SHA table + recompute), §2 (appendices A–E), §11.2 (≥12 negative tests), §12.1–§12.5 (content lock, consistency table, acceptance matrix, Word spec, SAMPLE/REAL isolation), §13 Writer condition 1.
- **Why:** Without the SHA table and appendices, the body cannot be source-verified; without negative tests and content-lock/Word spec, the blueprint’s completeness and isolation controls are missing. If these are intentionally separate, the body does not say so and cannot be reviewed as the complete body.
- **Correction:** Add the §1.2 SHA table with recomputed hashes and appendices A–E; add Table-N1 with ≥12 negative tests; add the §12 content lock/consistency/Word spec, or explicitly mark this file as body-only and not the complete review package.

## Explicit checks

- **Numeric/date consistency:** PASS on arithmetic and D+n. T1: 3÷4=75.0%, 3÷12=25.0%; T2: 4÷4=100.0%, 7÷12=58.3%; T3: 3÷4=75.0%, 10÷12=83.3%; differences −1/−1/−2. T0=2026-03-06; T1 +28; T2 +56; T3 +84. The baseline/target wording has a clarity caveat (L316 says “含起訖日，28 天”; L337 says Mar 6–May 29, 84 days, which is 85 days if read inclusively; D+84 supports 84 elapsed days). This does not change the 4/28 vs 12/84 rate. The period/cumulative application fails as stated in finding 5.
- **Real/sample boundary:** PARTIAL — not clean. Passes: NOT EXECUTED / REAL=UNKNOWN/HOLD / FORMAL_ACCEPTANCE=NOT_GRANTED; explicit synthetic disclaimer (L303); no real names; EVID-01–EVID-05 all HOLD/UNKNOWN; AID-02 not approved; 0082 not a real referral (L607). Fails/needs correction: L609 asserts a real association operation; L686 (“完成替換後，移除 SAMPLE 標籤與示例值”) is the only sentence that could erase the boundary if read prematurely, though L677/L682/L688 condition it; the missing 81-row register prevents verification that every SAMPLE value is registered. The body does not claim formal acceptance; this review does not grant it.
- **Genre/purpose:** Identity PASS: DOCX 0083 = I17C-E02 = checkbox 089; title and §1.1 match; core columns 目標/實際/阻礙/協助/成效; §2.1 distinguishes 17c’s five evidence types; §13 distinguishes 0082/088 and 090. Scope PARTIAL/FAIL: L4/L24/L63 narrow the genre to volunteer service, and L609 adds an unsourced association fact. The synthetic case itself is properly labeled and does not claim a real event.
- **AID timeline:** PASS on substance: AID-01 2026-04-03 REQUESTED → 2026-04-13 PROVIDED, before T2 2026-05-01; AID-02 2026-05-29 REQUESTED, PENDING; 2026-06-26 only SAMPLE. Minor label ambiguity at L376: AID-02 status shown as “PENDING” while L246/L367 use “REQUESTED/PENDING”; clarify that PENDING is the commitment/date, not the AID status.
- **Formal acceptance:** The body correctly states NOT EXECUTED and FORMAL_ACCEPTANCE=NOT_GRANTED; it does not claim formal acceptance. This review also does not grant formal acceptance.

## Reviewer scope and limitations

- Reviewed only the attached Markdown body (688 lines; SHA-256 verified) against `SOURCE_PACKET_0083_R01.md` and `UNIQUE_BLUEPRINT_0083_R03.md`.
- Did not edit any file, build a DOCX, inspect the external `SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv`, verify repository history, or confirm any real-world event, person, institution, employment, or authorization.
- Did not assess DOCX layout, watermark rendering, table pagination, or visual SAMPLE/REAL isolation; those are Word-level checks outside this text review.
- The referenced CSV was not attached; its absence from the body is finding 1.
- Line numbers are 1-based Markdown lines in the reviewed body.
- This is an independent text review, not formal acceptance, and it does not infer that any sample event occurred.

**Minor copyedit (non-material):** L506 “旧筆” → “舊筆”; L202/L571 “未確定时” → “未確定時.”
