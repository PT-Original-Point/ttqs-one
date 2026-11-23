# TTQS ONE 0048 R02_TEXTFIX 候選

狀態：CANDIDATE。這是 doc_id 0048、需求 I10-E03 的修補候選。此封裝標籤為 R02_TEXTFIX；DOCX 內部版次仍為 R02，因為本次為回收後的定點修補，未改寫版次欄位。既有遠端 0048_R02 原候選及其 PARTIAL 收據保留不動。

## 需求與來源綁定

官方具名需求：I10-E03「大型採購均辦理會議通過、師資遴聘後亦經過會議或審查通過並留有紀錄。」
官方來源 SHA-256：805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709，第 3 頁，來源 PDF 共 9 頁。
Blueprint row SHA-256：8B258F9125F2B1209629D0356539537E00C322073739EC65D05C58590847EF72。
DOCX SHA-256：D05F229A85903B2BF52C49D19F4926FCA872D69E2737833FCDC75F07FD897BD2（50,972 bytes）。

## 外包與回收

W1 OpenCode v2 曾對 0048-I10-E03-SCOPED-REPAIR-R02 執行範圍修補，呼叫路由 opencode/longcat-2.5-free。原派工啟動收據記錄 PID 7272/session ses_e1434ddb4ffepT7Ty4U0pVZsIY，但終態與 exit code 未完整捕獲；Worker 正文已實際回收，採用版本及 typo 修正收據均附於 evidence/worker/。未把未知 exit 冒稱成功。

W1 OpenCode v2 以 opencode/nemotron-3.5-lightning-free 對上述固定 DOCX SHA 做獨立語意審查；終態與回覆均為 PASS，0 blocking findings。供應端實際模型 UNKNOWN，原生 CLI exit code UNKNOWN。請求路由與實際供應模型分開記錄。

## 同一候選 SHA 的品質證據

- 確定性技術 QA：PASS；包含需求識別、兩個完整 8/8 範例、合成 ID 登錄、placeholder、字級門檻、OOXML 完整性及 SAMPLE/REAL 界線。
- Word 原生渲染：11 頁；PDF SHA-256 5636FDE5C997B111E15A020B599383424B061EDFBF7DD2C1C279D5D9917CFA52。
- 全頁視覺檢查：11/11 頁 PASS，無觀察到裁切、重疊或不可讀表格；頁圖與 PDF 一併保存。
- W1 獨立語意審查：固定候選 SHA PASS，需求適配、可用性、計算一致性及 SAMPLE/REAL 邊界均 PASS。
- 所有 QA 收據均應以候選 SHA D05F229A…FD897BD2 對帳；不得與舊遠端 0048_R02 的 SHA 混用。

DOCX 中的案例及角色是 SAMPLE/SYNTHETIC；沒有聲稱真實協會採購、會議、遴聘、核准或第三方原件。此候選不構成正式接受或 REAL 升格。GitHub raw-byte readback 應在候選提交後以相同 PR ref 另行驗證。