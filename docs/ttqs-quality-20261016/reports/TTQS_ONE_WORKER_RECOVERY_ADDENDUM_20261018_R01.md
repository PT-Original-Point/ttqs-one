# TTQS ONE 外包 Worker 修復與候選驗收增補 R01

日期：2026-10-18（Asia/Taipei）
對應分支：`work/ttqs-one-document-quality-contract-20261016`
本次起始 GitHub HEAD：`6a876b806da1c5b50e88488d9bd703ca983f22e5`（已由本機 fetch 與 PR #92 head 核對）

## 結果摘要

- 0057 R07、0058 R08、0059 R03、0060 R08 均有 exact-SHA 候選及已完成的獨立語意結果；各自仍是 CANDIDATE，未宣稱原始點協會正式接受或實際執行。
- 本次新增的 0060 R08 reviewer 已完成，候選 SHA `92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3` 維持不變，OpenCode v2.0.29 / `opencode/mimo-v2.6-flash-free` exit 0、語意 PASS。四個變動頁（18、19、20、23）已直接目視；其餘 22 頁影像雜湊與 R07 基準一致。
- 0057 R09 Blueprint 的 OpenCode 審查本身 exit 0、PASS；先前產生的 host receipt 有未展開變數及路徑截斷。原 bytes 已保留，修正後收據可追溯 prompt、候選、結果、stdout、stderr 與 exit code。沒有改動任何 DOCX。
- 0057 R07 Word 匯出 PowerShell 程序在 17 頁 PDF、17 張 PNG 與 manifest 都已完成後，仍閒置超過四小時。確認輸出已穩定、CPU 無變化、沒有 Writer 子程序後，只終止該 PowerShell PID 42464；未停止另兩個 Word automation 程序，也未更動候選。
- 沒有新建排程或控制平台。`opencode-cli.exe serve --service` 是服務程序，不代表有活躍文件任務；本次沒有發現活躍 Antigravity Writer／Reviewer。

## Worker 錯誤、修復與回收證據

| 路由 | 實際錯誤與證據 | 修復／回收結果 |
|---|---|---|
| Antigravity 0058 R08 R01 | CLI exit 2；`--print` 將 `--print-timeout` 誤讀為 prompt，原始 stderr SHA `3B325DBA9A7C584F3CB106E670DC0D8277B602AE7834769DF3BA4D9F89A4A374`。 | 將 prompt 正確附於 print 參數並調整參數順序；轉入下一次有界呼叫。 |
| Antigravity 0058 R08 R02 | CLI exit 2；timeout `1200` 缺少時間單位，原始 stderr SHA `6821B1D8B5BE2A979DF85C99D02A2802EFEEAE15F7CEE40DCA3D911BDB700E21`。 | 使用該 CLI 接受的時間單位，未更改安全權限。 |
| Antigravity 0058 R08 R03 | CLI exit 0 但回覆空白；stdout 記錄 headless `RunCommand` 權限遭拒。這不是審查 PASS。沒有 Computer Use，也沒有使用 `--dangerously-skip-permissions`。 | 改用已存在的唯讀 allow rule，設定 hash 前後相同。R04 以 `gemini-3.8-flash-high`、high effort、sandbox、`computer_use=false` 成功回覆。 |
| Antigravity 0058 R08 R04 | exit 0、stderr 空、候選 SHA 前後均為 `0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B`；回覆 SHA `B69932A79805524A994A0A346DD799F06195CAFE058C9448AAC8CB6CD914D6A2`。 | 對 R08 exact SHA 給出語意 PASS；原始 stdout、response、route receipt 均在 `quality-review/0058_R01/review/opencode_v2_semantic_R05/`。 |
| OpenCode Space Bunny 0058 | `opencode/space-bunny-free` exit 1；原始 stdout 回報 provider quota 429（FreeUsageLimitError），stderr 空，候選未變。 | 未升級付費或重複同一 quota 呼叫；改用可用的免費 `opencode/longcat-2.5-preview-free`，exit 0，對同一 SHA 完成獨立 PASS；結果 SHA `8B402602765113692E2899ECF5CAB5A51E5564D6B0823966A5D7A73CD7FF3AF2`。 |
| OpenCode 0057 R09 receipt | 審查者 exit 0 並 PASS；host receipt 寫入流程留下 `$docHash` 等未展開 token 及截斷路徑。 | 原錯誤 receipt 以 R00 原 bytes 保存；權威 receipt 已改為可核對實際 hashes 的版本。修正 receipt SHA `FD0010D4198C4CE4C5F3F577599540C9384B400D7D6D76C7B9ADA8095A1A2379`；保存原件 SHA `44802C27B1521887F2DD05E3ED0639BD9625C64FCEBF59D28F642E5D283CC5E3`。此為 receipt 產生器問題，不是 DOCX 或 reviewer 結果失敗。 |
| OpenCode 0060 R08 | 新一輪 CLI exit 0、stderr 空，耗時 1,295.007 秒；raw stdout SHA `E996ADFD3E90BBE42CCA3142F9A3B842379B50746FC00ADFF39FA38E5D93A34D`，candidate before/after 完全一致。 | exact-SHA 獨立語意 PASS；收據 `quality-review/0060_R01/review/opencode_v2_semantic_R08/independent_review_receipt_R08.md` SHA `9528A766E582936AE17D0CD5674F02CE2165069B64BAFA03220D7E65925507C3`。 |

完整 Antigravity 原始回覆與歷史嘗試仍保存在 R12 稽核報告及其索引內；本增補不重寫或省略那些原始檔。R12 原始報告 SHA-256：`A77C486304E6FAD1FC6AE3069EC7BC600AF8DB4BECF91AA357BF7711741513E8`。

## 候選狀態與下一 READY

| DOCX | 官方需求／方框 | exact SHA-256 | 當前品質結果 |
|---|---|---|---|
| 0057 R07 | I13-E01／061 | `A8D67C3F89105D85E47B554007624CE1231C6FB3340E3A9D3BFD14B6AE838705` | R06 完整語意 PASS 繼承，加 R07 有界增量 Antigravity PASS；R07 版面渲染完整。 |
| 0058 R08 | I13-E02／062 | `0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B` | Antigravity R04 與 OpenCode LongCat 獨立語意 PASS；R08 技術／視覺收據 PASS。 |
| 0059 R03 | I13-E03／063 | `0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0` | exact-SHA 語意狀態 PASS；34 頁視覺檢查 PASS。 reviewer 明示其未目視影像，視覺結論來自獨立本機 QA。 |
| 0060 R08 | I14-E01／065 | `92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3` | OpenCode Mimo exact-SHA 語意 PASS；技術及變動頁視覺檢查 PASS；保留一項不阻斷的表格標題 10 pt 觀察。 |

下一個可施工文件為 DOCX 0061 = I14-E02 = checkbox 066「檔案管理系統（索引、權限、檢索、備援）」。舊檔 `1600` 與 `1693` 是相同 SHA 的未重新驗收工作稿；`1689` 是較早版本，均含待填／待核欄位，僅作歷史參照，不作正文模板。0060 R08 已清楚排除 0061 的整體檔案管理架構；新件須以其經驗證的分類代碼作為合成案例輸入，並清楚與 0062–0064 的建檔原件、查詢改善及檢索速度測試分界。

所有狀態均為候選工程品質證據，未取代 Human 正式接受、真實原件、協會授權或實際執行記錄。