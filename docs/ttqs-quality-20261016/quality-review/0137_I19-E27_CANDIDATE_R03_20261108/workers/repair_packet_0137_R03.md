# 0137 R03 限定修補 Writer 工作包

工作類型：只建立新候選 R03；不得修改或覆寫 R02。
輸入 DOCX：E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0137_I19-E27_CANDIDATE_R02_R11_20261025\0137_I19-E27_媒體採訪與正面報導原件查驗表_R02.docx
輸入 DOCX SHA-256：3899167f0437ec76df42e6229685564d910250c6a822b627ec15b5f9cfcfecc8
預期輸出 DOCX：E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0137_I19-E27_CANDIDATE_R03_20261108\candidate\0137_I19-E27_媒體採訪與正面報導原件查驗表_R03.docx

獨立 OpenCode 全文審查（候選 R02 exact-SHA）回報 PASS_WITH_FINDINGS：
1. MEDIUM，表 4 第 2–14 資料列「實際登錄內容」欄 13 格為空白；雖已說明沒有真實媒體原件，但空格仍像待填。
2. LOW，正文第 5、16 段把本會稱為「原始點協會」，與其餘「本會」不一致。

## 唯一授權修補
A. 對 python-docx 的 `tables[3]`（第 4 張表）第 2–14 列（0-based row 1..13）第二欄（0-based cell 1）填入目前真實狀態。第 2–12 列及第 14 列填：`UNKNOWN/HOLD：尚無可回查真實媒體原件`；第 13 列「決策」填：`HOLD：尚無可回查真實媒體原件`。不得編造 REAL 資料。
B. 僅將正文中精確字串「原始點協會」改為「本會」；候選中目前兩處。不得改官方來源引文、評核需求或其他文字。
C. 其餘正文、所有 SAMPLE/SYNTHETIC 案例/數值、12 張表、register、格式與欄位一律保留。替換清冊不變；此次只填 REAL 原件待取得的欄位，不新增合成事實。
D. 使用 R02 另存新檔至上述 R03 路徑。必須保留 R02 原檔位元組。對空白儲存格應修改既有段落/空 run 的文字並保留字型、段落與表格格式；不可縮小字級、改頁面尺寸或重建整份文件。

## Writer 終態輸出
只寫新 R03 DOCX 和此工作資料夾內的 `writer_receipt.json`。回執記錄輸入/輸出 SHA-256、位元組、變更欄位/文字、修改表格儲存格數、register 未改的理由及成功/失敗。若不能保留版面或要改動授權範圍，停止並回報，不要改 R02。
