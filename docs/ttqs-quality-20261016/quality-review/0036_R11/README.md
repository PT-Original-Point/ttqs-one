# 0036 R11 課程設計進度與訓練規劃

**狀態：候選文件；R11 獨立語意審查為 PARTIAL，需修復圖5-1兩個回接箭頭；未提升為正式文件，也未獲 Human 正式接受。**

## 對應需求與精確版本

- DOCX 0036 = I07-E04 = 官方訓練機構版方框流水號 036。
- 官方要求：「有課程設計進度表、課程規劃流程圖說明、訓練規劃書等佐證資料。」來源是官方佐證資料表第2頁。
- 候選 DOCX SHA-256：`1e08913a7e330fcbd52f50645138f97b8c951022ef69bc5bd1ee3d2971c9a7c7`。
- 前版 R10 SHA-256：`765e36f07c5e92964d3d5aa438564ef4578e0b2d6ca684b2123687cff5686a6a`。R10 的完整獨立 PARTIAL 原始回覆及派審雜湊截短更正說明收在本目錄 `review/lineage_0036_R10_*.md`。

## R11 定位修正

1. §6 進度列與 §14 合成案例將 190 分鐘統一標示為課程與評量，另加 20 分鐘休息，總計 210 分鐘，與 §9 的實際時段一致。
2. §15 增加逐項可重複使用的交接紀錄欄：完成／未完成、核對日期、原件名稱與頁／表／欄位定位；未完成時記責任角色、期限及暫停措施。表單明示為空白格式，不代表協會已完成交接。
3. §5 流程圖在本版未更動。完整 Word 輸出第5頁影像隨包提供給獨立 reviewer，核對來源確認、缺口分析、目標評量覆蓋與授權發布分支。

R11 只修改 R10 審查所列文字、表單欄位，沒有重新生成全份案例、流程圖或評量內容。原有 84 筆 SAMPLE/SYNTHETIC 替換登錄保留；修訂 F033 時間分類，並增加 F085 記錄新欄位設計，R11 共 85 筆。新期限、角色、日期與案例均不代表原始點協會真實規定或實績。

## 技術與版面範圍

- DOCX 可讀、38 張表格；R10 至 R11 只改變 `word/document.xml`。
- Word COM 輸出 PDF SHA-256：`1a5f67f3858b764999cba87193106c76f47c01f533dd36fafec3bbf0c8e9ad42`；19頁，19張144 dpi頁圖。
- 相對 R10 直接目視變動頁：6、16、17；其他16頁逐像素相同。第17頁含交接紀錄欄位與真實替換清單，沒有空白或孤列頁。
- 技術及版面收據不替代獨立語意審查；本版目前維持候選狀態。

## SAMPLE／REAL 界線

所有合成資料均須依 `inputs/sample/SYNTHETIC_REPLACEMENT_REGISTER_0036_R11.csv` 逐項以有權限的正式原件替換，並重做來源、權限及計算覆核。未取得的原件保持待取得；不得把課程草案、空白欄位或示範結果寫成協會正式核准、公告、排課、辦訓或成效。

## 附件與可追溯來源

本包包含 R11 DOCX、Word PDF、19頁影像、官方來源 PDF、完整需求映射、相鄰 Blueprint、唯一 Blueprint、85筆替換登錄、R10獨立審查原文、R11修復及技術／版面收據。來源雜湊在 `inputs/source_provenance.json` 和 `PROGRESS.json`。官方 PDF 的已核實完整 SHA-256 為 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。


## R11 獨立語意審查 R01

- 判定：**PARTIAL**，精確綁定 R11 DOCX SHA `1e08913a7e330fcbd52f50645138f97b8c951022ef69bc5bd1ee3d2971c9a7c7`。原始審查回覆見 `review/0036_R11_independent_semantic_review_R01.md`。
- 唯一阻擋缺陷：第5頁圖5-1兩個「否」修訂分支缺少返回箭頭，分別應回到需求來源核對及課程矩陣重配。§5文字雖有說明，流程圖仍須無推斷即可操作。
- 其他語意檢查：官方要求/文類、相鄰方框辨識、190+20=210時間、§15交接表、85筆SAMPLE替換追溯及案例計算均 PASS。視覺判定限第5頁。
- 下一版 R12 僅修正這張內嵌流程圖，保留其餘 R11 DOCX 內容；完成後另行 exact-SHA 審查。

## GitHub command preflight readback

- 原生 Automation `ttqs-one-hourly-quality-goal-resume` 已更新並讀回：ACTIVE、HOURLY、同一 GOAL thread；持久化 prompt 含 `TTQS_GITHUB_COMMAND_PREFLIGHT_V1`。Prompt SHA-256 `fe0529b760020af2cea0998234a6f306e3a05168175e5449c77864031843006e`。
- 本回合從 live branch HEAD `99e252ad31e05e3809d49ad4df3093c0397163f7` 讀完 06 外部稽核命令，來源 blob SHA-1 `70449889fd464106fe204496004bee13018d4a51`；完整讀取01–05規格。
- 唯一啟用的 TTQS hourly automation 數量為1；standalone hourly automation PAUSED；Windows `TTQS_ONE_Codex_Supervisor` DISABLED。Automation 工具未提供最近實際觸發與下一次執行時間；因此不宣稱 scheduled wake smoke 已驗證。
- 完整原生讀回欄位見 `review/TTQS_GITHUB_COMMAND_PREFLIGHT_R01.json`。
