```json
{
  "candidate_sha256": "07728568bab741562f6bdaed00c4237b786957dc5a41067eeafe9fb03f2a53fd",
  "edits": [
    {
      "locator": "T10 R21 C1",
      "old_cell": "來件狀態（本附件）",
      "replacement": "來件狀態（本附件子碼；非 T7 主狀態）",
      "reason": "Status taxonomy — separate attachment code"
    },
    {
      "locator": "T10 R21 C2",
      "old_cell": "NOT_RECEIVED",
      "replacement": "ATTACHMENT_NOT_RECEIVED",
      "reason": "Status taxonomy — separate attachment code"
    },
    {
      "locator": "T10 R21 C3",
      "old_cell": "NOT_RECEIVED",
      "replacement": "ATTACHMENT_NOT_RECEIVED",
      "reason": "Status taxonomy — separate attachment code"
    },
    {
      "locator": "T10 R21 C4",
      "old_cell": "RECEIVED_UNVERIFIED",
      "replacement": "ATTACHMENT_RECEIVED_UNVERIFIED",
      "reason": "Status taxonomy — separate attachment code"
    },
    {
      "locator": "T13 R2 C4",
      "old_cell": "E-02",
      "replacement": "SAMPLE-CLAIM-02",
      "reason": "Replacement register — unregistered claim ID E-02"
    },
    {
      "locator": "T14 R10 C4",
      "old_cell": "維持 HOLD；非承辦覆核逐項確認後才可解除：原件/可驗證副本、來源與發文代表權、完整性/日期/服務關聯、書面同意(目的/範圍)或核驗法定免同意依據、個資最小化/存取限制、D01-D15 適用性。重大矛盾未解，或適用項仍為 UNKNOWN/FAIL/CONFLICT/未覆核之 N/A，均不得解除；原件持續隔離。",
      "replacement": "維持 HOLD；解除須全部成就，並由 SAMPLE-ROLE-REVIEWER（樣本覆核角色；示範判定，非人類驗收）依機構權責書面授權逐項覆核：原件/可驗證副本、來源與發文代表權、完整性/日期/服務關聯、書面同意(目的/範圍)或核驗法定免同意依據、個資最小化/存取限制、D01-D15 適用性。SAMPLE-DATE-06 屆期未成就：維持 HOLD，按月覆核並留存紀錄；不得自動解除或自動結案。僅於機構權責書面授權下，始得解除、升級或結案；重大矛盾未解或適用項仍為 UNKNOWN/FAIL/CONFLICT/未覆核 N/A 者不得解除；原件持續隔離。",
      "reason": "HOLD release and closure — named sample reviewer, deadline-expiry disposition, no auto-release"
    },
    {
      "locator": "T14 R11 C4",
      "old_cell": "SAMPLE-DATE-06",
      "replacement": "SAMPLE-DATE-06（屆期未成就＝維持 HOLD、按月覆核；不得自動解除／結案）",
      "reason": "HOLD release and closure — deadline-expiry disposition"
    },
    {
      "locator": "T19 R2 C4",
      "old_cell": "狀態 RECEIVED_UNVERIFIED",
      "replacement": "附件子碼 ATTACHMENT_RECEIVED_UNVERIFIED（非 T7 主狀態；Form F 主狀態其後為 HOLD）",
      "reason": "Status taxonomy — disambiguate attachment status from T7 main disposition"
    },
    {
      "locator": "T20 R4 C4",
      "old_cell": "案例一／Form A、Form B、Form E「需求承辦」及存取紀錄 A-01 / 需求承辦角色",
      "replacement": "案例一／Form A「需求承辦角色」；存取紀錄 A-01「角色」",
      "reason": "Replacement register — S-03 locator (Form B R14 is 負責人; Form E has no role field)"
    },
    {
      "locator": "T20 R5 C4",
      "old_cell": "案例一／Form A、Form B、Form C、Form E、Form F「案件負責人」及存取紀錄 A-02",
      "replacement": "案例一／Form A「案件負責人」、Form B「負責人」、Form C「處理人」；存取紀錄 A-02「角色」",
      "reason": "Replacement register — S-04 locator (Form F R8 is SAMPLE-ROLE-PRIVACY)"
    },
    {
      "locator": "T21 R12 C4",
      "old_cell": "案例一／Form F / 結果與狀態",
      "replacement": "案例一／Form F「主要狀態」及「理由」",
      "reason": "Replacement register — S-18 locator"
    },
    {
      "locator": "T21 R12 C5",
      "old_cell": "SAMPLE-OUTCOME-01：無寄送、無回覆、無原件；REQUEST_DRAFT_ONLY",
      "replacement": "REQUEST_DRAFT_ONLY（示意；無寄送、無回覆、無原件）",
      "reason": "Replacement register — S-18 value not verbatim in body"
    },
    {
      "locator": "T21 R13 C4",
      "old_cell": "案例一／Form F / 覆核意見",
      "replacement": "案例一／Form F「覆核性質」",
      "reason": "Replacement register — S-19 locator"
    },
    {
      "locator": "T21 R13 C5",
      "old_cell": "SAMPLE-REVIEW-01：示範判定",
      "replacement": "示範判定（非人類驗收）",
      "reason": "Replacement register — S-19 value not verbatim in body"
    },
    {
      "locator": "T21 R16 C4",
      "old_cell": "案例二／Form A、Form C、Form F、Form E「查核角色」及存取紀錄 A-03",
      "replacement": "案例二／Form A、Form B「負責人」、Form C「處理人」；存取紀錄 A-03「角色」",
      "reason": "Replacement register — S-22 locator (Form F R8 case 2 is SAMPLE-ROLE-PRIVACY)"
    },
    {
      "locator": "T21 R25 C4",
      "old_cell": "案例二／Form F / 結果與狀態",
      "replacement": "案例二／Form F「主要狀態」及「理由」",
      "reason": "Replacement register — S-31 locator"
    },
    {
      "locator": "T21 R25 C5",
      "old_cell": "SAMPLE-OUTCOME-02：僅截圖、無原件、未接觸；HOLD",
      "replacement": "HOLD（示意；僅截圖、無原件、未接觸）",
      "reason": "Replacement register — S-31 value not verbatim in body"
    },
    {
      "locator": "T21 R26 C4",
      "old_cell": "案例二／Form F / 覆核意見",
      "replacement": "案例二／Form F「覆核性質」",
      "reason": "Replacement register — S-32 locator"
    },
    {
      "locator": "T21 R26 C5",
      "old_cell": "SAMPLE-REVIEW-02：示範判定",
      "replacement": "示範判定（非人類驗收）",
      "reason": "Replacement register — S-32 value not verbatim in body"
    },
    {
      "locator": "T21 R31 C4",
      "old_cell": "案例一、二／Form F「隱私／資料存取角色」；案例二流程步驟10；存取紀錄 A-04",
      "replacement": "案例一、二／Form F「下一位負責人」；案例一流程步驟10；案例二流程步驟10；存取紀錄 A-04「角色」",
      "reason": "Replacement register — S-37 locator"
    },
    {
      "locator": "T27 R9 C5",
      "old_cell": "SOURCE_READY_ONLY",
      "replacement": "SOURCE_READY_ONLY（僅指來源封包就緒；本文件狀態為 CANDIDATE）",
      "reason": "Provenance/status labeling — scope SOURCE_READY_ONLY to source packet"
    }
  ],
  "new_register_rows": [
    {
      "fact_id": "S-40",
      "doc_id": "0103",
      "case_id": "SAMPLE-CASE-02",
      "section/table/cell locator": "案例二／Form E「claim_id」（T13 R2）",
      "synthetic value": "SAMPLE-CLAIM-02",
      "required REAL source": "真實來件與可回查之主張編號／來源紀錄",
      "authorized custodian/role": "查核人",
      "replacement condition": "有真實來件、原件或可驗證副本，且來源可回查",
      "status": "SAMPLE_ONLY"
    }
  ],
  "hash_in_body_note": "Do not embed the post-patch DOCX SHA-256 in the body (self-referential). Proposed body wording, to be placed at the cover version note once its exact text is supplied: 「版本與最終 DOCX SHA-256 由外部收據綁定，不內嵌於文件；本文所載 07728568bab741562f6bdaed00c4237b786957dc5a41067eeafe9fb03f2a53fd 為修補前候選版，來源封包 05b94f04…aede、藍圖 c4f0c3b9…b8f1c 同由外部收據綁定。」",
  "validation_notes": [
    "SHA binding discrepancy: the header prints 63 hex chars (…41067eeaf9fb03f2a53fd); the reviewer binding string is the valid 64-char 07728568bab741562f6bdaed00c4237b786957dc5a41067eeafe9fb03f2a53fd (extra 'e'). This patch uses the reviewer's 64-char value; confirm before applying.",
    "DEFERRED (exact cell text not in supplied extract, so no old_cell bound): T12 R3 C? D02 -> cite Form A「來源類別」; T12 R5 D04 -> cite Form C「格式」「送達證據」（無訊息標頭欄位）; T12 R9 D08 -> cite Form C「頁數」「檔案特徵／雜湊」; T12 R14 D13 -> cite Form C「同意／範圍」「存取限制」及 Form F「限制」; T12 R16 D15 -> cite Form D D01–D14 欄位（無「矛盾清單」欄）. Supply T12 extract to bind.",
    "DEFERRED: T27 R2/R3/R7 field names -> replace claim_text/linkage_type/evidence_limit/disposition_scope with 可引用陳述/連結類型/限制與下一步/判定範圍, and source_locator with Form C「保管位置」；Form A 填寫指示 gate -> replace 「收件人代表權」「核定通道」 with Form A 權限狀態（T8 R12）與 目前記錄來源／預期取得方式（非核定通道）（T8 R17）. Exact paragraph/cell text required before binding.",
    "DEFERRED: T7 R7 definition -> append 「RECEIVED_UNVERIFIED 僅為主狀態；附件層級一律使用 ATTACHMENT_* 子碼，不構成主狀態」 (needed to close the taxonomy finding with the T10/T19 edits above).",
    "T13 R2 C4 E-02 renamed to SAMPLE-CLAIM-02 and registered as S-40; verify SAMPLE-CLAIM-02 appears only where intended and that no stale E-02 cross-reference remains.",
    "SAMPLE-OUTCOME-01/02 and SAMPLE-REVIEW-01/02 were non-verbatim; register values now mirror Form F text. If those IDs also occur elsewhere in the full DOCX, reconcile rather than leaving orphans.",
    "Preserved: SAMPLE/SYNTHETIC labeling, UNKNOWN/HOLD, NOT GRANTED (no Human acceptance), no auto-release or auto-close, no association approval or real letter/signature/consent/outcome claimed. HOLD release still requires association-authorized review; sample reviewer is SAMPLE-ROLE-REVIEWER only.",
    "No PASS rows were altered; editorial-only items (T22 R8 duplicate, D+10/D+20 wording, Form B NOT_APPLICABLE label, checklist checkbox, SAMPLE-DATE-04 dual use) are out of scope for this patch."
  ]
}
```