# 0117 / I19-E04 / R09 layout root-cause repair

狀態：CANDIDATE。未主張 REAL、正式接受或送審。

候選 DOCX SHA-256：78aba2030004475f09bd236436cc2d964bd1ef4b1ce5adba87d47377b4281c97

R09 僅修正 R08 的 Word 分頁缺陷：移除 RETAKES 列內的 pageBreakBefore，將原八筆清單分成兩張各含表頭的六欄表格，並更新版次標籤。8 個原始資料列 ID、正文、數值及樣本資料均保留。

技術 QA：PASS_DETERMINISTIC_ONLY；22 頁 Word 原生開啟，正文至少 10.5 pt、表格至少 9.5 pt，四項百分比重算一致。
全頁視覺：PASS_VISUAL_SCOPE；22 頁縮圖總覽，20–21 頁逐頁放大檢查，表頭重複、四列完整、無拆列。
W1 語意增量審查：輸出正文已從 OpenCode 原始 stdout 回收，候選 SHA 相同，結果 PASS_SCOPED_DELTA、0 個阻斷發現。OpenCode v2.3.0 的 process exit code UNKNOWN；provider.free-limit HTTP 429 發生在完整回覆之後；實際供應模型 UNKNOWN。原始 stdout、回收收據及審查封包一併保存。這些限制不被冒稱為 CLI exit 0 或已知供應模型。
GitHub 同來源原始位元組讀回：PASS；於不可變提交 63e7090b4921c87276131e3111800df0c5b21409 讀回 64,906 bytes，SHA-256 78aba2030004475f09bd236436cc2d964bd1ef4b1ce5adba87d47377b4281c97、Git Blob SHA-1 0843f50b64e704660eb77b7ed545a361cfe5b095 均與候選相符。後續提交僅包含此收據與索引更正；須由現行 PR HEAD 同路徑 Blob 核對是否可沿用。
