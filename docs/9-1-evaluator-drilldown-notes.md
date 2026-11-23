# 9/1 顧問 TEST Portal 現場操作與驗收筆記

## 目的與邊界

- 使用者：2026/09/01 TTQS 顧問與現場主持人。
- 環境：TEST only。
- 資料分類：TEST／SAMPLE／CONTROL only；不得把任何 SAMPLE 轉成 REAL。
- Portal：`https://script.google.com/macros/s/AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh/exec`
- Portal 是匿名外部唯讀快照：不計算 TTQS 官方分數、不做 REAL／PROD 寫入、不在執行期直連 Google Sheets／Drive 或 TTQS ONE 核心資料庫。
- 正式 T Gate 仍保留給顧問本人實機操作、問題收錄、必要修正與人類確認；技術黑箱 PASS 不等於整體 T Gate PASS。

## 開場前 30 秒

1. **預設直接開私人／無痕視窗，且不登入任何 Google 帳號。** Portal 為 `ANYONE_ANONYMOUS`，不需要登入。
2. 可接受替代：只登入單一 Google 帳號的獨立瀏覽器 Profile／一般視窗。
3. 已同時登入複數 Google 帳號的一般視窗不是現場標準路徑；已實測 Safari 與 Brave 可能被 Google multi-login session／Cookie／帳號路由導到錯誤頁。
4. 若乾淨 session 仍無法開啟，才進 deployment／permission／entrypoint 診斷；不要因 multi-login 路由錯誤重跑 OAuth 或重建 deployment。
5. Portal 內 Google Drive 連結是選配；顧問調閱成功不依賴 Drive 登入。若真的要開受控 Drive 原件，另用適當登入 Profile／分頁，不把它當 Portal 本身的必要條件。

## 顧問最短驗收路徑

### A. 官方 19 指標語意

- 先按「官方19指標」。
- 確認 1–19 全部可見，並可看到指標 12 的 12a–12e、指標 17 的 17a–17d。
- 每張指標卡先看官方查核焦點摘要，再展開「查看佐證與來源」。
- 抽查制度／程序／課程／證據／來源物件／Observation locator 是否能一路追溯。
- 不要求顧問接受任何系統自評分；Portal 明確不自動評分。

### B. SAMPLE 因果鏈

按「SAMPLE因果鏈」，依序檢查：

`需求蒐集 → 需求／職能落差分析 → 課程設計 → 執行 → 評量 → 追蹤 → 改善`

重點不是文件數量，而是每一步是否能說明「前一步如何形成下一步」以及對應的 SUPPORTS 證據／來源定位。此鏈只證明 TEST／SAMPLE 方法，不得預先形成 REAL 課程。

### C. 四類 TEST Forms 生命週期

按「四表生命週期」，確認四類都有 ACCEPTED readback：

- NEEDS：4 筆 Observation。
- REGISTRATION：6 筆 Observation。
- REACTION：2 筆 Observation。
- FOLLOWUP30：2 筆 Observation。
- 合計：14 筆 TEST Observation。

每類至少抽一筆代表 Observation，確認 Observation ID、原始收件 locator 與處理物件可見；外部 Portal 不公開原始個資回答。

### D. 失敗／重試／exactly-once

按「故障／重試」，直接讀既有 S3 TEST runtime 證據，不為現場表演重新製造故障：

`FAILED → TIME_RETRY → MATCHED_EXACTLY_ONCE → FINAL_ACCEPTED`

確認：第一次處理失敗、第二次重試成功、job／party／survey／evidence duplicate = 0／0／0／0、provider raw write = 0、`AttemptHistory=append-only`。

### E. 權限與 SAMPLE／REAL 邊界

顧問應能直接從畫面確認：

- `EXTERNAL_READONLY`。
- Web App 是部署版本內嵌的去識別靜態快照。
- 不在執行期呼叫 Google Sheets／Drive API。
- 不提供新增、修改、刪除、核准、正式啟動或背景工作控制。
- 17–19 的正式成果仍須由未來 REAL 營運證據形成。
- SAMPLE／CONTROL 永不得宣稱為 REAL。

## 現場判定

目前技術與產品前置條件已能覆蓋上述五條驗收路徑；匿名產品黑箱會逐項檢查其核心標記，任何必要標記缺失都 fail closed。

9/1 現場只有在以下事實都完成後，才可由人類確認 T Gate：顧問本人實際操作上述路徑、顧問問題／缺口已被收錄、必要修正已完成並重新驗證。T Gate 通過前禁止 `REAL_WRITE`、`PROD_ENABLE`、`REAL_COURSE_LOCK`、`SAMPLE_AS_REAL`。
