# 0103 R25 SAMPLE／SYNTHETIC 替換清冊

- Document: 0103 / official requirement I18-E10 / Unique Blueprint index 111
- Source candidate DOCX SHA-256: `0968cee79b351bf2293e7eee78b35adf9a3fbdede364dc8e660e632d59609d92`
- 狀態：僅為範例資料；不得視為原始點協會真實案件、真實人員、授權、核准、收件或訓練績效。只有取得有權來源並經權責人員核對後，才可依各列替換條件逐項替換。
- 清冊內容逐列擷取自候選 Word 的替換登錄表。

| fact_id | doc_id | case_id | section/table/cell locator | synthetic value | required REAL source | authorized custodian/role | replacement condition | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | 0103 | SAMPLE-CASE-01 | 案例一／Form A / case_id | SAMPLE-CASE-01 | 機構核定之真實案件編號 | 承辦 | 建立真實案件並取得編號 | SAMPLE_ONLY |
| S-02 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、C / 來源組織 | SAMPLE-ORG-A | 經查證之真實發文或受文單位 | 承辦／查核 | 單位身分與權限可查 | SAMPLE_ONLY |
| S-03 | 0103 | SAMPLE-CASE-01 | 案例一／Form A「需求承辦角色」（T8 R14）；存取紀錄 A-01「角色」（T15 R3） | SAMPLE-ROLE-REQ | 實際承辦人角色與授權 | 機構授權人 | 書面指派 | SAMPLE_ONLY |
| S-04 | 0103 | SAMPLE-CASE-01 | 案例一／Form A「案件負責人」（T8 R15）、Form B「負責人」（T9 R14）、Form C「處理人」（T10 R21）；存取紀錄 A-02「角色」（T15 R4） | SAMPLE-ROLE-OWNER | 實際負責人角色 | 機構授權人 | 書面指派 | SAMPLE_ONLY |
| S-05 | 0103 | SAMPLE-CASE-01 | 案例一／Form A / 課程／服務 | SAMPLE-COURSE-01 | 真實課程代碼與梯次 | 承辦 | 與課程紀錄一致 | SAMPLE_ONLY |
| S-06 | 0103 | SAMPLE-CASE-01 | 案例一／Form A / 目的 | SAMPLE-PURPOSE-01 | 真實用途與閱覽層級 | 隱私權責 | 目的經核定 | SAMPLE_ONLY |
| S-07 | 0103 | SAMPLE-CASE-01 | 案例一／Form A / 關係 | SAMPLE-REL-01 | 真實學員／客戶關係證明 | 承辦 | 關係可查且與課程一致 | SAMPLE_ONLY |
| S-08 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、C / 同意狀態 | SAMPLE-CONSENT-01（尚未取得） | 當事人或權責單位之書面同意 | 隱私權責 | 同意範圍、期限與撤回方式明確 | SAMPLE_ONLY |
| S-09 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、B / 權限狀態 | SAMPLE-AUTH-01（收件人代表權與機構書面寄送授權均未確認） | 機構書面寄送授權 | 機構授權人 | 對象、目的、資料與期限均核定 | SAMPLE_ONLY |
| S-10 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、C / 揭露範圍 | SAMPLE-SCOPE-01（未定） | 真實使用範圍核定 | 隱私權責 | 範圍可支持本次用途 | SAMPLE_ONLY |
| S-11 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、B / 通道 | SAMPLE-CHANNEL-01（草稿匣） | 機構核定通道清單 | 資料保管 | 通道已核定且可留存紀錄 | SAMPLE_ONLY |
| S-12 | 0103 | SAMPLE-CASE-01 | 案例一／Form B、F / 請求編號 | SAMPLE-REQ-01 | 真實請求紀錄編號 | 承辦 | 有寄送或正式請求紀錄 | SAMPLE_ONLY |
| S-13 | 0103 | SAMPLE-CASE-01 | 案例一／Form A、C / 位置代碼 | SAMPLE-LOC-01（草稿區） | 機構核定限制存取位置 | 資料保管 | 位置可控制存取 | SAMPLE_ONLY |
| S-14 | 0103 | SAMPLE-CASE-01 | 案例一／流程 / 日期 | SAMPLE-DATE-01（示意：2026-11-02） | 真實建案日期 | 承辦 | 以實際事件時間替換 | SAMPLE_ONLY |
| S-15 | 0103 | SAMPLE-CASE-01 | 案例一／流程 / 日期 | SAMPLE-DATE-02（示意：2026-11-03） | 真實草稿完成日期 | 承辦 | 以實際事件時間替換 | SAMPLE_ONLY |
| S-16 | 0103 | SAMPLE-CASE-01 | 案例一／流程 / 日期 | SAMPLE-DATE-03（示意：2026-11-06） | 真實接觸前檢查日期 | 隱私權責 | 以實際事件時間替換 | SAMPLE_ONLY |
| S-17 | 0103 | SAMPLE-CASE-01 | Form A 期限（T8 R16 C4）；Form B 時限（T9 R13 C3）；Form F 期限（T14 R11 C3）；D項N/A明細期限（T12 R2–R16 C3）；流程示例期限（T17 R11 C4） | SAMPLE-DATE-04（示意：2026-11-09） | 真實核定或追蹤期限 | 案件負責人 | 期限經權責核定 | SAMPLE_ONLY |
| S-18 | 0103 | SAMPLE-CASE-01 | 案例一／Form F「主要狀態」（T14 R3 C3） | REQUEST_DRAFT_ONLY | 真實寄送、回覆與來件證據 | 覆核人 | 每項均有證據後才可改狀態 | SAMPLE_ONLY |
| S-19 | 0103 | SAMPLE-CASE-01 | 案例一／Form F「覆核性質」（T14 R13 C3） | 示範判定（非人類驗收） | 具名且獲授權之覆核紀錄 | 覆核人 | 完成真實覆核並簽署 | SAMPLE_ONLY |
| S-20 | 0103 | SAMPLE-CASE-02 | 案例二／Form A / 案件編號 | SAMPLE-CASE-02 | 機構核定之真實案件編號 | 承辦 | 建立真實案件 | SAMPLE_ONLY |
| S-21 | 0103 | SAMPLE-CASE-02 | 案例二／Form C / 所示發文者 | SAMPLE-ORG-B（僅示意標籤） | 可獨立查證之真實發文單位 | 查核人 | 身分與代表權限可查 | SAMPLE_ONLY |
| S-22 | 0103 | SAMPLE-CASE-02 | 案例二／Form A「案件負責人」（T8 R15）、Form B「負責人」（T9 R14）、Form C「處理人」（T10 R21）；存取紀錄 A-03「角色」（T15 R5） | SAMPLE-ROLE-VERIFIER | 實際查核人角色與授權 | 機構授權人 | 書面指派且具獨立性 | SAMPLE_ONLY |
| S-23 | 0103 | SAMPLE-CASE-02 | 案例二／Form C / 來源通道；Form C原始訊息標頭／寄件紀錄狀態（T10 R7 C4） | SAMPLE-CHANNEL-02（轉傳） | 真實來源管道與傳輸紀錄 | 查核人 | 可追溯至原始來源 | SAMPLE_ONLY |
| S-24 | 0103 | SAMPLE-CASE-02 | 案例二／Form C、E / 來件編號 | SAMPLE-IN-02 | 真實來件登錄編號 | 資料保管 | 有實際來件與保管紀錄 | SAMPLE_ONLY |
| S-25 | 0103 | SAMPLE-CASE-02 | 案例二／Form C / 位置代碼 | SAMPLE-LOC-02（隔離區） | 機構核定隔離位置 | 資料保管 | 限制存取已設定 | SAMPLE_ONLY |
| S-26 | 0103 | SAMPLE-CASE-02 | 案例二／Form A、C / 同意狀態 | SAMPLE-CONSENT-02（未知） | 當事人或權責單位之書面同意 | 隱私權責 | 同意與範圍可查 | SAMPLE_ONLY |
| S-27 | 0103 | SAMPLE-CASE-02 | 案例二／Form A / 權限狀態 | SAMPLE-AUTH-02（收件人代表權與機構書面寄送授權均未知） | 可對外說明或提供之授權 | 隱私權責 | 權限可查 | SAMPLE_ONLY |
| S-28 | 0103 | SAMPLE-CASE-02 | 案例二／Form A、C / 揭露範圍 | SAMPLE-SCOPE-02（未知） | 真實使用與揭露範圍 | 隱私權責 | 範圍可支持查核或引用 | SAMPLE_ONLY |
| S-29 | 0103 | SAMPLE-CASE-02 | 案例二／流程 / 日期 | SAMPLE-DATE-05（示意：2026-11-10） | 真實來件與隔離日期 | 資料保管 | 以實際事件時間替換 | SAMPLE_ONLY |
| S-30 | 0103 | SAMPLE-CASE-02 | 案例二／Form A、F / 期限 | SAMPLE-DATE-06（示意：2026-11-13） | 真實隱私評估期限 | 案件負責人 | 期限經權責核定 | SAMPLE_ONLY |
| S-31 | 0103 | SAMPLE-CASE-02 | 案例二／Form F「主要狀態」（T14 R3 C4） | HOLD | 真實來源、原件、權限與查核證據 | 覆核人 | 解除條件全部成立才可改狀態 | SAMPLE_ONLY |
| S-32 | 0103 | SAMPLE-CASE-02 | 案例二／Form F「覆核性質」（T14 R13 C4） | 示範判定（非人類驗收） | 具名且獲授權之覆核紀錄 | 覆核人 | 完成真實覆核並簽署 | SAMPLE_ONLY |
| S-33 | 0103 | SAMPLE-CASE-01 | 存取紀錄 A-01 / 存取事件 | SAMPLE-ROLE-REQ 於 SAMPLE-DATE-02 閱覽草稿 | 真實存取紀錄 | 資料保管 | 有實際系統或紙本紀錄 | SAMPLE_ONLY |
| S-34 | 0103 | SAMPLE-CASE-01 | 存取紀錄 A-02 / 增補事件 | SAMPLE-ROLE-OWNER 於 SAMPLE-DATE-03 增補停止註記 | 真實增補紀錄 | 案件負責人 | 增補內容與理由可查 | SAMPLE_ONLY |
| S-35 | 0103 | SAMPLE-CASE-02 | 存取紀錄 A-03 / 隔離檢視 | SAMPLE-ROLE-VERIFIER 於 SAMPLE-DATE-05 檢視 | 真實查核存取紀錄 | 資料保管 | 有實際存取紀錄 | SAMPLE_ONLY |
| S-36 | 0103 | SAMPLE-CASE-02 | 存取紀錄 A-04 / 隱私增補 | SAMPLE-ROLE-PRIVACY 於 SAMPLE-DATE-05 增補限制 | 真實隱私審查紀錄 | 隱私權責 | 有實際審查與簽署 | SAMPLE_ONLY |
| S-37 | 0103 | SAMPLE-CASE-01 / SAMPLE-CASE-02 | 案例一、二／Form F「下一位負責人」（T14 R8 C3–C4）；案例一流程步驟10（T17 R11）；案例二流程步驟10（T19 R11）；存取紀錄 A-04「角色」（T15 R6） | SAMPLE-ROLE-PRIVACY | 實際隱私／資料存取權責角色 | 機構授權人 | 書面指派 | SAMPLE_ONLY |
| S-38 | 0103 | SAMPLE-CASE-01 / SAMPLE-CASE-02 | Form F覆核角色兩案例（T14 R12 C3–C4）；D項N/A逐項覆核角色（T12 R2–R16 C3）；替換清冊（T20 R39 C5） | SAMPLE-ROLE-REVIEWER | 實際覆核人角色與授權 | 機構授權人 | 書面指派且非唯一承辦 | SAMPLE_ONLY |
| S-39 | 0103 | SAMPLE-CASE-02 | 案例二 / Form A / field: 合法目的 | SAMPLE-PURPOSE-02（真偽查核演練） | 真實用途及閱覽層級之權責書面核定 | 隱私／資料存取權責 | 目的、閱覽者及範圍以書面核定；核定前不接觸 | SAMPLE_ONLY |
| S-40 | 0103 | SAMPLE-CASE-02 | 案例二／Form E（T13）R2「claim_id」 | SAMPLE-CLAIM-02 | 經權責核定、可回查且與案件一致的真實主張識別碼；無法確認時填 UNKNOWN | 承辦／覆核人 | 以可查的核定來源替換；未核定不得引用 | SAMPLE_ONLY |
