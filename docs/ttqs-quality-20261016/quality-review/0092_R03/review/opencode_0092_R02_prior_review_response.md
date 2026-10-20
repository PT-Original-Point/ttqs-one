## Verdict: **PASS** (reasoned; all findings below are nonblocking — no blocking defect found)

**Exact candidate SHA-256 (repeated as supplied by the packet):**
`33392cdbe71a56bfd57833d2ed7e9c26dd0e869ae86f66901fb36821c4d8baf2`
(SHA re-computation was not performed — no external tools permitted; byte-level identity is therefore UNKNOWN and accepted as packet-asserted.)

**Scope:** Semantic and practical-utility review of the complete text extracted from candidate 0092 R02 against official requirement `I17D-E06` / checklist serial `099` / official text 「感謝函。」 (source PDF p. 6), using only the supplied packet. Candidate-only review; no file edits, no external tools. **Page locators: UNKNOWN** — the extraction carries body order only, no page breaks, so all locators below are section/table locators.

---

### Findings (locator + quoted phrase + assessment)

1. **Genre and operational scope — correct.** §1.1 「如何依據真實合作資料，向第三方禮貌索取由第三方自行撰寫的感謝函」 and §5.2 usage box 「下列文字是未寄出的合成稿」. The deliverable reads as an association-side request draft + evidence-validation register; no sentence imitates or claims a third-party-issued letter. §1.3 「不允許本會替第三方撰寫、簽署、用印」. Not a wrong-genre substitution.

2. **Official requirement fidelity — correct.** Cover row 「官方要求 I17D-E06　｜　官方 157 項清單序號 099　｜　佐證表第 6 頁」 and §2.1 「第 6 頁…『感謝函。』」. Official text is quoted verbatim, not rewritten by historical drafts; §10 correctly separates the three identifiers: 「0092 是 DOCX 文件編號；099 是官方 157 項清單中的流水號」. Matches the packet's distinct-identifier rule (`I17D-E06` ≠ `099`).

3. **Status integrity — correct.** 30秒使用說明: 「未寄出；截至 2026-10-02 未收到第三方原件」; §5.3 rows 「實際寄出狀態 | 未寄出」, 「第三方回覆狀態 | 未寄出；沒有第三方回覆」 (F021), 「原件收件狀態 | 未收到第三方原件」 (F014). Consistent with F013/F014/F021; no implied dispatch, receipt, reply, or archive record anywhere.

4. **Arithmetic and its limits — correct and bounded.** §3.2 enumerates exactly 8 required fields (F001–F005, F007–F009); §6.1 「8 ÷ 8 × 100% = 100%（0092-F020-E2）」 with numerator/denominator defined; §6.4 「欄位完整度算例 100%；第三方原件未收到；六項查驗未開始；不得納入正式佐證」. §2.1 places 「本件 8/8 欄位完整度等於感謝函有效、第三方背書或評核得分」 in the *cannot-conclude* column. The 100% never implies third-party evidence or formal compliance.

5. **Six verification checks — all not-started, no PASS.** §5.4 CHK-01…CHK-06 each 「未開始／無原件」, mapped to F022–F027; §2.2 step 5 「無原件或重大疑點：保持 HOLD，不填 PASS」. No check is marked PASS or inferred.

6. **Decision / exception / rejection / hold rules — present.** §6.3 status table (HOLD｜暫緩 / REJECT｜不採認 / REVIEWABLE / CANDIDATE) with condition + next step per row; §7.1 exception table (發現狀況｜即時控制｜更正／追蹤要求｜不可採取的作法); §7.2 minimum correction fields; §6.3 disposition consistent with F016 「不納入正式佐證」 and F017 「示例欄位完整度算例成立；第三方證據核實未成立」.

7. **Fact register completeness — 27/27 present.** §11 lists F001–F020 (E2) and F021–F027 (E3), each with 正文定位 / REAL 替換所需依據 / 責任・狀態「尚未替換」; §8 「以正式資料替換全部 27 筆合成事實」. No dropped or merged IDs; substitution instructions are actionable (specific source class per fact, named responsible role).

8. **Minor issue — two register locators do not resolve as written.** §11 F001 locator 「§5.2 索取稿主旨」, but §5.2 subject reads 「主旨：就『職場數位協作實作課程』索取客觀回饋（合成草稿）」 — 案件甲 does not appear there. §11 F002 locator 「§5.2 寄件方」, but §5.2 contains no literal 「本會（合成示例）」. Both values *do* appear correctly at §4.2 and §5.3 (「案例識別 | 案件甲（合成示例）」, 「寄件方／承辦角色 | 本會（合成示例）…」). Traceability defect in 2 of 27 rows; values themselves are correctly marked SAMPLE. Nonblocking.

9. **Minor issue — required table shape partially realized.** Blueprint table 「欄位—定義—來源—填寫者—驗證規則」 vs. §4.1 「登錄欄位資料字典」 columns 「欄位群 | 要填的內容 | 填寫者／驗證規則」: a distinct 來源 column is absent from that table. The source element exists elsewhere — §3.1 「可接受的来源例子」 and §5.3 「來源鍵／說明」 — so all five elements are covered across §3.1/§4.1/§5.3, but not in one table. Nonblocking conformance gap.

10. **Minor issue — two unregistered/unverifiable values.** §1.2 「不表示原始點協會目前設有這些部門」 introduces an entity name not among the 27 registered facts and not tagged SAMPLE (used only inside a disclaimer, so no claim is made). §2.1 「I17d『成果評估』」 asserts a category label not corroborated by the packet (packet supplies page 6, text, ID, serial only); the official quoted text itself is exact. Nonblocking.

11. **Fabrication controls — clean.** No invented approval, sent date, reply, signature, seal, original number/date, named person, or archive record found. §5.3 「出具者／日期／編號／位置 | 不適用；未收原件」; §6.3 REJECT covers rewrite/impersonation; §12.2 「R02 候選示範稿｜…尚未核定，不代表協會正式發布」. Repair phrases: none of the four flagged strings (每項待確認資料 / 以下待核資訊 / bare 待核 as status / 先列為待核) appear anywhere; status vocabulary used is 「未開始／無原件」 + HOLD, permitted by the Writer task.

12. **Neighbor separation — correct.** §2.3 table 「0091 | I17D-E05 學員就業證明」, 「0093 | I17D-E07 學員訓後雇主問卷調查表」 with the checkable differentiator 「問卷回答與感謝函是不同資料；不能推論相同結論」 (§10), and 「不與 0091 或 0093 共用實際課程、學員或第三方事實」 (§2.3 closing). Neither neighbor's evidence is reused.

13. **UNKNOWN items (explicit):** candidate page numbers — **UNKNOWN**; font sizes (≥10.5pt body / ≥9.5pt table) — **UNKNOWN**, not derivable from text; docProps `Description` value (python-docx string removal) — **UNKNOWN**, not visible in body text; independent SHA recomputation — **UNKNOWN** (tools not permitted).

---

### Title-blind test: **PASS**
With title, filename, and number masked, the body still self-identifies: 用途 line 「讓承辦人準備第三方感謝函索取稿」, §1.1 request-and-verify proposition, §5.2 full request draft, §5.3 register, §5.4 original-verification checklist, and §2.1/§12.1 point to the official 「感謝函。」 at 佐證表第 6 頁. It cannot be moved to 0091 (employment proof) or 0093 (employer questionnaire) without modification, because those distinctions are argued in-body (§2.3, §10).

### Eligible for candidate-only acceptance review: **YES**
Eligible for candidate-only acceptance review (not formal association acceptance): all 12 required sections, all four required tables (one with reduced columns), all required fields, the 27-fact register, the 8/8 bounded calculation, and the correct HOLD/不納入 disposition are present and internally consistent. Formal association acceptance remains unavailable by design (no real original, six checks not started).

### Nonblocking observations (5)
1. §3.3 expresses deadlines only as stage gates (起草前／寄出前／收到後／決定前); no target intervals for reply follow-up or correction — acceptable while unsent, but a live SOP will need intervals (as registered facts).
2. §9.3 「調閱紀錄表（空白工作表）」 contains placeholder cells 「（實際調閱後填）」; disclaimed by 「空表不代表曾經調閱」 and supplementary to the completed §4.2/§5.3 samples, yet a hasty evaluator could read it as unfinished.
3. §12.2 version history is a single line; a version table with date/author/change summary would better serve the 「版本」 requirement.
4. Responsible roles are generic labels (承辦/覆核/保管/授權決定者, §1.2) rather than an explicit 責任角色代碼 column, though §11 notes 「角色代碼及職務名稱不能替代真人授權資料」.
5. §2.1 left column retains the vague status word 「維持待補或不納入」; not one of the four banned repairs, but aligning it with the HOLD/查驗未完成 vocabulary would remove the last ambiguous status wording.