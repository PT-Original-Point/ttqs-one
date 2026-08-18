# 9/1 External TEST Direct Deploy

用途：當 GitHub CLI 裝置登入或 TEST Environment OAuth secret 不可用時，以一次 Google 身分授權直接部署 TTQS ONE External Evaluator Portal TEST。

控制邊界：
- 僅 TEST／SAMPLE／CONTROL。
- 不要求 GitHub CLI、不登入 GitHub、不更新 GitHub Secret。
- Google OAuth 僅要求 `spreadsheets.readonly`、`script.projects`、`script.deployments`。
- 部署來源固定下載 `main` 的 `external-viewer/Code.gs`、`external-viewer/appsscript.json` 與 REST 部署器。
- 本機 OAuth 憑證置於隔離臨時 HOME，腳本結束自動刪除。
- 新建 Apps Script 專案並發布匿名唯讀 Web App；匿名頁面必須通過 TEST/SAMPLE、EXTERNAL_READONLY、19/19、SAMPLE 因果鏈、佐證下鑽等產品黑箱標記。
- `realProdTouch=0`。

此路徑是 9/1 D7 的可交付 fallback，不等於 REAL／PROD 啟動，也不改變 T Gate Mission。
