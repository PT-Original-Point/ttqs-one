# 9/1 External TEST Direct Deploy

用途：只有在 **External TEST Portal 產品內容 `external-viewer/**` 確實需要改版**，而 GitHub Actions `TEST` environment 的 OAuth credential 不可用時，才以一次 Google 身分授權直接更新既有 TEST Apps Script Portal。

## 正常路徑優先

- 若只是驗證器、測試、控制碼、文件或其他不改 `external-viewer/**` 的變更，`deploy/test` 走 **BLACKBOX_ONLY_NO_PROVIDER_MUTATION**：沿用既有 script／deployment／URL，直接對現有 Portal 跑 repository verify 與匿名產品黑箱。
- 這種 verifier-only 變更不需要 Google OAuth，也不應 push Apps Script content 或建立新 deployment。
- receipt 必須分開記錄真正已部署的 `sourceSha` 與本次驗證器的 `verificationSha`，禁止把 verifier-only commit 冒充已部署產品版本。

## Direct OAuth fallback 邊界

- 僅 TEST／SAMPLE／CONTROL；`realProdTouch=0`。
- 不要求 GitHub CLI、不登入 GitHub、不更新 GitHub Secret。
- Google OAuth **只要求兩個最小部署 scope**：
  - `https://www.googleapis.com/auth/script.projects`
  - `https://www.googleapis.com/auth/script.deployments`
- 不要求 `spreadsheets.readonly`、Drive、Gmail、Cloud Platform 或使用者資料 scope。
- 本機 OAuth 憑證置於隔離臨時 HOME，腳本結束自動刪除。
- 部署來源固定下載 canonical `main` 的 `external-viewer/Code.gs`、`external-viewer/appsscript.json`、REST 部署器與產品黑箱 classifier。
- **重用既有 TEST Apps Script project 與既有 deployment**；不得無故建立第二套 script 或 deployment。Direct helper 會對固定 identity 做 readback，漂移即 fail closed。
- provider 更新後必須讀回 content／deployment identity、`ANYONE_ANONYMOUS`、`USER_DEPLOYING`，再做匿名 HTTP 產品黑箱。

## 產品黑箱範圍

黑箱不是只驗證 HTTP 200 或 `19 / 19`。目前 D8/D9 Gate 會 fail closed 檢查：

- TEST／SAMPLE 與 `EXTERNAL_READONLY` 身分。
- 官方 19 指標語意導航，含 12a–12e、17a–17d 關鍵子項。
- SAMPLE 因果鏈。
- 四類 TEST Forms 生命週期與 4/4 ACCEPTED。
- `FAILED → TIME_RETRY → MATCHED_EXACTLY_ONCE → FINAL_ACCEPTED` 與 `AttemptHistory=append-only`。
- 19 指標佐證／來源下鑽與受控 Drive fallback。
- runtime 不呼叫 Google Sheets／Drive API。
- SAMPLE／CONTROL 不得宣稱為 REAL。

Apps Script HtmlService 可能把 `/` 或 `=` 序列化轉義；classifier 只做必要的等價字元正規化，再檢查完整語意標記，不會把 Gate 弱化成零散關鍵字。

此 Direct OAuth 路徑只是產品內容真的需要更新時的 TEST fallback；不等於 REAL／PROD 啟動，也不改變 9/1 T Gate Mission。若現有 Portal 產品內容沒有變更，不應為了跑黑箱而重新要求人類 OAuth。
