# 0038 I08-E02｜獨立正式來源位元組身分補充

建立時間（UTC）：2026-11-06T02:12:50.8485759Z
狀態：`SOURCE_IDENTITY_VERIFIED_BOUNDED`。本檔只補記正式來源身分及頁面追溯，不是 0038 DOCX 的內容、技術或版面 QA，也不是正式接受。

## 1. 原 packet 保留基線

原始 packet：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0038_PREFLIGHT\SOURCE_PACKET_0038_I08-E02_R01_20261101.md`

- bytes：7,481
- SHA-256：`06EBDFA5FCEB229AB609C4C873A21955AA8092A77FA91BA1557B1B7A6FDE987A`
- 原檔 LastWriteTimeUtc：`2026-11-01T03:55:28.0000000Z`
- 原 packet §2.1 對 PDF 原始位元組標為 UNKNOWN，並明確區分 page PNG SHA 與 PDF SHA。本補充不覆寫或改寫原 packet。

## 2. 官方來源、版本識別與位元組核對

TTQS 官方清單頁：`https://ttqs.wda.gov.tw/ttqs/menu_010_02.php?type_id=5`
該頁列出的「TTQS查核佐證文件資料表-訓練機構版.pdf」直接連結：
`https://ttqs.wda.gov.tw/download_files/6475978659d646f58e3eddc3b1ea51d9/TTQS%E6%9F%A5%E6%A0%B8%E4%BD%90%E8%AD%89%E6%96%87%E4%BB%B6%E8%B3%87%E6%96%99%E8%A1%A8-%E8%A8%93%E7%B7%B4%E6%A9%9F%E6%A7%8B%E7%89%88.pdf`

唯讀 HTTP 讀回：清單頁與 PDF 均 HTTP 200；PDF `Content-Type=application/pdf`、`Content-Length=303044`、`Last-Modified=Wed, 07 Jan 2026 08:11:36 GMT`、`ETag="5b98503ead7fdc1:0"`。ETag 是伺服器標頭，不作 SHA 證據。讀回 PDF 位元組在記憶體計算 SHA-256，未另存或覆寫來源檔。

官方下載 PDF 與兩個本機檔案的核對結果完全一致（同長度、同 SHA-256）：

- 官方下載連結（讀回日 2026-11-06）：303,044 bytes；SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`
- 疑似來源檔：`E:\TTQS\_official_TTQS_checklist.pdf`；303,044 bytes；SHA-256 同上；檔案時間 `2026-09-25T18:05:56.0000000Z`
- 2026-09-23 任務包副本：`E:\TTQS\人才發展品質管理全量文件製作任務包_20260923\人才發展品質管理全量文件製作任務包_20260923\官方原始資料\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`；303,044 bytes；SHA-256 同上；檔案時間 `2026-09-23T05:38:30.0000000Z`

PDF 文件資訊：9 頁；第 2、3 頁頁框各為 595.32 × 842.04 pt。`/Author=ITRI_iCAP`、`/Creator` 與 `/Producer=Microsoft® Word LTSC`；內嵌 CreationDate/ModDate 均為 `2026-01-07 15:56:01 +08:00`。官方 HTTP Last-Modified 與 PDF 內嵌日期相差 15 分 35 秒，分別保留，不推定其成因。PDF metadata 未提供獨立版號；本補充以官方頁當次連結、SHA-256 及內嵌日期共同識別此位元組版本。兩個本機 LastWriteTime 是副本檔案時間，不當成官方版次。

可在本機重算疑似來源檔 SHA-256：
`Get-FileHash -LiteralPath 'E:\TTQS\_official_TTQS_checklist.pdf' -Algorithm SHA256`

## 3. I08-E02 文字及 page 2/3 圖像追溯

官方 PDF 以第 8 項「訓練方案的系統設計」呈現相關內容；PDF 頁面本身沒有印出內部代碼 `I08-E02`，該代碼與官方第 8 項的對應沿用原 0038 packet。PDF 第 2 頁下半開始第 8 項，涵蓋訓練課程設計流程、訓練方案產出，以及相關文件對方案要素之檢討改善；第 3 頁上半接續第 8 項，列出改善效果及課程規劃會議紀錄佐證。頁序、表格跨頁位置及文字與本資料夾的兩張 page PNG 相符。

- `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0038_PREFLIGHT\official-2.png`：500,594 bytes；SHA-256 `F72BF94BDFC5E1DA907DAF2CE322F1916A69F54AF5185F28A1DAB21237577783`；1158 × 1638 px；PNG DPI metadata 約 139.98；LastWriteTimeUtc `2026-10-16T18:35:38.0000000Z`。
- `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0038_PREFLIGHT\official-3.png`：392,645 bytes；SHA-256 `58F3C876F7CED30CE444E208238094248958C7DF08764228A30CF7CC8B456B50`；1158 × 1638 px；PNG DPI metadata 約 139.98；LastWriteTimeUtc `2026-10-16T18:35:38.0000000Z`。

核對方式：對同一份已驗 SHA 的官方 PDF 第 2、3 頁，以 pypdfium2 在記憶體按 140 dpi 渲染；渲染尺寸均為 1158 × 1638，與既有 PNG 同尺寸。再以 PDF 文字擷取和頁面視覺逐頁核對第 8 項、跨頁續文及頁碼。PNG 與 PDF 是不同格式，SHA 必然分別計算；本次不宣稱 PNG 與渲染影像逐像素相等，也沒有舊 PNG 產生工具/命令的原始收據可證明其歷史 rasterizer。可支持的結論是：兩張 PNG 的頁面內容與位置可追溯至同一份已由官方網站直接讀回、位元組 SHA 相同的 PDF。

## 4. 差異、限制與範圍

- 原 packet 的 PDF SHA `UNKNOWN` 是當時缺少可重算原件位元組的狀態；本補充以獨立 addendum 提供現在取得的來源鏈，不更改原 packet 及其時間。
- PDF 內嵌日期、官方伺服器 Last-Modified、兩個本機副本 mtime 是不同時間來源；只有 PDF 位元組 SHA 相等可證明副本位元組相同。未據此推定官方歷史發布或版本更替紀錄。
- 無明示版號；官方網頁/主機與當次下載 SHA 證明讀取當下該官方連結供應相同位元組，不是數位簽章或長期封存證明。
- PNG 的頁面文字、頁碼與版面定位相符；缺少其原始渲染收據，因此不宣稱 PNG 生成工具鏈或逐像素來源可證。
- 本補充只解決來源 PDF 身分及 page 2/3 定位；不對 0038 DOCX、既有 QA、內容品質或正式接受作任何更新或判定。
- 寫入前後 `0038_PREFLIGHT` 既有 101 個檔案（排除本 addendum）的路徑、大小、LastWriteTimeUtc、SHA-256 合併快照一致；快照 SHA-256：`7D2C1A14E02D6B20B3F41286F1AF9E50A91B4F9EBE05111B582F76AA295039CF`。