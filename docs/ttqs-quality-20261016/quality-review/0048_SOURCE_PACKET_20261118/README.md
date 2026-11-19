# TTQS ONE 0048 / I10-E03 來源包

狀態：READY_SOURCE_PACKET、READY_UNIQUE_BLUEPRINT。這是 CANDIDATE 來源包，不是正式接受文件；尚未建立 DOCX。

本件依 PR #92 現行分支 HEAD 03348e7811dfe57a5b6e46efed1598b929db563d 的專屬 Blueprint row 0048，對應 142 交付 crosswalk 中的 I10-E03 至 0048。官方核取項在查核佐證表第 3 頁。此文件應保存大型採購決議與師資遴聘審查紀錄的證據欄位和調閱索引，不代替第三方原件。

## Writer 必須保留的界線

- 官方精確要求與專屬結構見 OFFICIAL_REQUIREMENT_EXTRACT.md、UNIQUE_BLUEPRINT_ROW.json。
- source 資料夾收錄綁定的官方 PDF、完整 crosswalk 與 Blueprint 原始位元組；SHA 在 SOURCE_MANIFEST.json。
- 缺少真實原件時，只製作清楚標示 SAMPLE/SYNTHETIC 的完整示例，逐項登錄替換清冊。
- 不得虛構協會實際採購、會議通過、師資遴聘、簽名或審查結果；不得留下空白待填表單。
- 本來源包沒有 DOCX，候選 SHA 為 UNKNOWN。

## 來源讀取方法

- 官方 PDF 第 3 頁分別以 pypdf 與 pdfplumber 讀取；完整文字檔保留。
- 官方頁面影像已用 Poppler render，直接檢視第 3 頁的目標核取項。
- crosswalk、Blueprint 原始檔從 PR #92 分支當前 live HEAD 的 Git blob bytes 讀回。
