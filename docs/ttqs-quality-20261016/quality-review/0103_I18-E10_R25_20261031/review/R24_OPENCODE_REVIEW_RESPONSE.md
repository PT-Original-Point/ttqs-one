# R24 Independent Exact-SHA Semantic Review — 0103 / I18-E10

## Verdict: **PARTIAL**

One remaining blocker (metadata/provenance, not evidence-semantics). Both R23 locator findings are **closed** on this SHA. All substantive scope checks (genre, boundary, gates, D01–D15, HOLD logic, replacement register, SAMPLE/REAL) pass on the extracted body.

Review basis: the bound SHA strings in the packet header only; extracted text only; no file writes, no DOCX/PDF render, no visual inspection claimed.

## R23 findings — closure check (both verified against locators in the extracted body)

| # | R23 finding | Verification against this body | Status |
|---|---|---|---|
| 1 | Form C row locators in T12 D01–D15 stale after new T10 row | Re-derived T10 row maps from the actual header: R6 送達證據, R7 原始訊息標頭／寄件紀錄, R8 格式, R9 發文者, R10 收件者, R11 文件日期, R12 文件／參考編號, R13 簽名／用印, R14 頁數, R15 檔案特徵／雜湊, R16 保管位置, R17 存取限制, R19 與課程連結, R21 處理人, R22 本附件收件狀態. Every T12 citation (D01–D15, T10 R6/R7/R8/R9/R10/R11/R12/R13/R14/R15/R16/R17/R19/R22) matches. D04 wording now states the field exists (T10 R7) but the original header has not been received — exactly the repair target. | **CLOSED** |
| 2 | T20 S-17 cited T17 R11 C5; Table 17 has 4 columns | T17 header confirms 4 columns (步驟／示意行動／證據／判定與下一步). R11 = step 10; C4 contains "SAMPLE-DATE-04 前確認權限與同意路徑". S-17 now reads "流程示例期限（T17 R11 C4）" — valid. | **CLOSED** |

## Full locator audit (all checked; none stale)

- **T8 (Form A, 22 rows):** R7 來源類別, R8 關係, R9 合法目的, R10 最小資料, R11 同意狀態, R12 收件人代表權／寄送授權, R13 揭露範圍, R14 需求承辦角色, R15 案件負責人, R16 期限, R17 通道核定, R21 source_requested, R22 同意例外依據 — all match the Form A filling instruction (T8 R9/R11/R12/R13/R17), Form B pre-send list, T12 D02/D07/D12/D13, and T26. C4 = Case-01 column consistent with the 5-column header.
- **T9 (Form B, 15 rows):** R7 權限依據, R8 通道, R9 授權狀態, R13 追蹤日, R14 負責人, R15 狀態 — match T12 D01/D12 and S-04/S-09/S-17.
- **T11:** header + D01–D15 at R2–R16 — matches T12 D11 (T11 R12), T12 D15 (T11 R16), T19 step rows, and T12 rule paragraph.
- **T12 (N/A register):** R2–R16 C3 carries SAMPLE-ROLE-REVIEWER／SAMPLE-DATE-04 consistently; final 決定 paragraph correctly scopes Case-02 (D03 FAIL = screenshot, not fraud; D15 UNKNOWN, hence HOLD).
- **T13 (Form E, 12 rows):** R2 claim_id, R4 可引用陳述, R6 課程／服務, R9 對照紀錄, R11 連結類型, R12 限制與下一步 — match T12 D06/D14 and T26.
- **T14 (Form F, 14 rows):** R3 主要狀態 (C3 REQUEST_DRAFT_ONLY／C4 HOLD), R6 判定範圍, R7 限制, R8 下一位負責人, R11 期限, R12 覆核角色, R13 覆核性質 — match S-18/S-19/S-31/S-32/S-37/S-38 and T26.
- **T15:** A-00..A-04 at R2–R6 — match S-03/S-04/S-22/S-37.
- **T20:** header + S-01..S-40 → S-38 at R39; "替換清冊（T20 R39 C5）" correctly self-locates its own synthetic value. T20 R39 C5, T14 R12 C3–C4, T12 R2–R16 C3 for S-38 all valid.
- **T19/T26:** Form C T10 R22 reference in Case-2 step 1 valid; T26 row locators (T10 R2/R5/R16/R22; T8 R7/R21; T13 R4/R11/R12; T14 R6) all valid.

## Scope checks (evidence highlights)

- **Genre/title-blind:** 感謝函取得與真偽查核工作紀錄 = acquisition/authenticity work record + unissued template; explicitly "不是感謝函，也不能代替…原始文件". PASS.
- **I18-E10 purpose/limits:** Page-7 indicator-18 4-point context quoted verbatim; explicit "例示清單，不是…就一定得分" and T2 can-see/cannot-infer matrix. PASS.
- **Negative neighbors:** 0096/I18-E03 distinguished as page-6/1-point vs page-7/4-point; 0102, 0100/0101, 0097 excluded; cross-ref only on same real case else UNKNOWN. PASS.
- **Gates:** Send blocked without T8 R9/R11/R12/R13/R17; "在請求中詢問同意不構成同意"; NOT_REQUIRED_BY_AUTHORITY requires documented basis. Template contains no request to compose praise, backdate, co-sign, or guarantee results. PASS.
- **Attachment vs case status:** T10 R22 labeled 附件層級，非案件主狀態； T7 RECEIVED_UNVERIFIED row and T19 step 1 hold this distinction. PASS.
- **D01–D15:** N/A register with reason + locator + reviewer/date + "N/A≠PASS"; N/A-permitted-only rules for D12/D14; VERIFIED_REAL blocked by any UNKNOWN/FAIL/CONFLICT/unreviewed N/A. PASS.
- **HOLD authority/deadline:** T14解遷條件 requires non-requester authorized reviewer, per-item evidence, SAMPLE-DATE-06 expiry → 維持HOLD, no auto-release; monthly re-check; 未核實前不接觸. PASS.
- **Status/math/date consistency:** Case 1 REQUEST_DRAFT_ONLY in T8 R18/T9 R15/T16/T14 R3; Case 2 HOLD in T8 R18/T9 R15 (correctly annotated NOT_APPLICABLE, Form F 主狀態仍為 HOLD)/T18/T14 R3; 0/0 = N/A, denominator = received originals only; date chains DATE-01→04, DATE-05→06 coherent. PASS.
- **SAMPLE/REAL boundary:** Every SAMPLE value mapped (S-01–S-40, incl. S-39/S-40 for later additions); no quoted letter content, no issuer reply, no signature/consent/acceptance invented; 人類正式驗收 NOT GRANTED everywhere. PASS.

## Blocker

| # | Severity | Locator | Finding |
|---|---|---|---|
| B-1 | Minor blocker (provenance metadata) | Candidate cover, 候選狀態 paragraph (after 文件性質， before 一分鐘開場指引； not in any table) | Body self-describes "CANDIDATE（版本 R20…）R18 exact-SHA 語意審查為 PARTIAL；R20 等待新的 exact-SHA 獨立審查”. The bound packet is the R24 candidate with an R23 PARTIAL prior review; the in-body version/correction-history line is stale and omits R23. Per the packet directive, revision inference is taken from the SHA binding, not this label — but an internal provenance record whose own correction trail is outdated is an internal-consistency defect (the document mandates "更正用增補…版本要有先後關係” for its subjects). Fix = one addendum-style line update; no evidence-semantics content affected. |

## Non-blocking notes

- N-1: T20 S-02/S-05/S-12/S-13 locator enumerations are non-exhaustive (e.g., SAMPLE-ORG-A also appears at T9 R4 C3 and the unissued draft; SAMPLE-REQ-01 also at T17 R5/R11 C3) — all facts are still row-mapped; no wrong positions.
- N-2: T12 D04's "目前只能判 UNKNOWN" sits inside a Case-1 N/A row; reconcilable because the row's structural basis is "無查核對象” and the sentence explicitly bars treating the check as done — no change required.

## Conclusion

All R23 findings are closed on this exact SHA; no semantic, boundary, or gate defect found. The single stale in-body version-history label (B-1) keeps this at **PARTIAL**; after one-line update and rebind of the DOCX SHA, the content reviewed here would support PASS. Formal acceptance remains NOT GRANTED; no real letter exists or is implied.
