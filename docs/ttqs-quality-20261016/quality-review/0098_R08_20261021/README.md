# DOCX 0098 R08｜I18-E06 候選與驗收證據

## 身分與狀態

- DOCX 識別：0098；正式佐證要求：I18-E06；官方核取方框印製序號：UNKNOWN。
- 官方要求原文：執行目標客戶及學員滿意度調查及分析（系統及流程面）。
- R08 是 SAMPLE/SYNTHETIC 示範候選，不是 REAL 執行紀錄，也未取得 TTQS 正式接受。
- 不能將 DOCX 編號 0098 誤認為官方 checkbox 流水號。

## 本版成品與來源

- DOCX SHA-256：a5d4bb14c884ff2d19db7bb6a86f999de0604d9ac6bacd9eb26f0b5db2c9cdba
- PDF SHA-256：8df3d14be78a8e35ef762f5bb2bc0949e269921f430de4f2197d3f119c268c78；共 29 頁。
- 合成替換清冊 SHA-256：9fa51aef4394a3e0f8ae8e42a42cdfa8b49356802427614e1ac439cb512e29e4；192 筆、192 個唯一 FACT ID，頁碼定位 0 筆待補。
- Manuscript SHA-256：060d23554903cf6eaaaad7914717ba2f34f57d022f2756fa1e7d9165617b9fcb
- Official requirement readback SHA-256：2238fda775d4d72e281275a2df745f578e6b44b5eec9e99d8979e8da72f21db2
- Unique Blueprint SHA-256：cba2e2d175907021f237992a346b750d33c41fb8a1810b6040c5f4c603be3d48
- 官方 129–142 對照表 SHA-256：1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679
- Blueprint seed SHA-256：280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0

## 審查結果

- 獨立 exact-SHA 語意審查：PASS，OpenCode CLI v2 `opencode/nemotron-3-ultra-free`；審查對象 DOCX SHA 必須與上列完全相同。只有兩項正確處理的 note，0 項實質阻擋 finding；回覆與派工收據放在 `evidence/`。
- 技術檢查：PASS；DOCX ZIP 全部項目可讀；PDF 29 頁；192 筆清冊皆有頁碼定位。
- 視覺檢查：PASS（有明確範圍）；直接檢視第 1、9、13、27、28、29 頁。R08 第 2–28 頁影像與 R07 相同，沿用 R06 全頁 contact-sheet 檢視證據。第 13 頁是較稀疏的橫向續表頁，但重複表頭與資料可讀，沒有截切；末頁沒有孤立第 30 頁。
- 正式接受：NOT GRANTED。語意與技術候選 QA 通過不等同正式接受。

## SAMPLE / REAL 界線與缺件

所有 192 筆替換清冊資料及文件中的問卷、邀請、日期、數值、同意旗標與分析均為 SAMPLE/SYNTHETIC。未提供或驗證真正邀請名冊、原始問卷、系統匯出、核准告知／同意文本、個別肯定同意證據、正式更正紀錄、真實簽章或交接原件。這些 REAL 證據均維持 UNKNOWN/HOLD。樣本旗標只供流程追蹤，不可代表真實同意或真實回覆。

## 套件內容

- `candidate/`：可開啟的 R08 DOCX 與對應 manuscript。
- `inputs/`：官方要求讀回、0098 Unique Blueprint、正式 129–142 crosswalk 與 142 seed。
- `evidence/`：192-row SAMPLE/SYNTHETIC 替換清冊、技術/頁碼/視覺/語意審查原始回覆與收據、版本壓縮收據、綜合裁定。
- `render/document.pdf`：R08 的 29 頁 Word PDF。
- `render/pages/`：直接目視範圍頁面的 PNG（01、09、13、27、28、29）。

## 稽核限制

本套件是候選文件與驗收證據，不是正式送審件。Reviewer's semantic PASS 不宣稱其做過視覺檢查；視覺檢查是另一份有界本機收據。未提供 REAL 原始資料、權責核准或正式簽章，因此不推定協會已執行或核准任何事項。