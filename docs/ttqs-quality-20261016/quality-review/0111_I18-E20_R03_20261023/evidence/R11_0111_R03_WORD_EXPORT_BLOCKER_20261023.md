# 0111 R03 Word 匯出阻擋收據

## 綁定候選

- 文件：0111 / I18-E20；官方 checkbox serial：UNKNOWN_NOT_ASSERTED。
- DOCX SHA-256：f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50（75,015 bytes；本次未修改）。
- 文稿、技術檢查及獨立語意檢查：PASS；語意檢查只涵蓋正文，不含頁面視覺。
- Word 原生匯出/視覺驗收：BLOCKED；未取得 PDF，不得宣稱視覺 PASS 或正式接受。
- REAL 證據：UNKNOWN/HOLD；內容仍為 SAMPLE/SYNTHETIC.

## 有界匯出嘗試

1. attempt01：啟動器找不到 PowerShell 7 目錄內不存在的 powershell.exe；未派出 Worker。
2. attempt02：Windows PowerShell 5.1 子程序找不到 Get-FileHash，未開啟 Word；舊錯誤處理再次呼叫缺失命令而遮住原始錯誤。
3. attempt03：同一 Get-FileHash 執行環境錯誤；未開啟 Word。已改用 .NET SHA-256。
4. attempt04：使用隱藏 Word PID 69372、只讀開檔及已在 0102 R08c 驗證的 ExportAsFixedFormat 參數；150 秒仍無 PDF，確切停滯 COM 階段 UNKNOWN.

attempt04 清理比對曾因 ConvertFrom-Json 將建立時間降到整秒而錯拒同一程序。以原始 owner JSON 與 OS StartTime 比對後，PID 69372 與 exporter PID 64336、WINWORD.EXE 路徑、/Automation -Embedding、非 baseline PID 完全相符，建立時間差 0.0002 ms；只終止這個本次隱藏 Word PID。既有 Word 程序均未觸碰。

## 處置

- 不重建 DOCX；精確 SHA 保持不變。
- 僅暫停 0111 R03 的 Word 原生匯出/視覺車道；其他 READY 文件可繼續。
- 只有取得可定位的新診斷或不同且已驗證的渲染路徑後，才考慮重開此車道。
- 收據 JSON SHA-256：9064553e60f07a2f3be4ca981ea5a7721ac4d9fe3b461836f2b045c341d0497d。

## 附件

- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_launch_failure_R11_attempt01.json — 613 bytes — SHA-256 74d3c7b5c921b3ffb49263b8d53bc82fda3b16463740a0f9b41ea7c8f1b370cb — launcher failure before worker dispatch
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_failure_analysis_R11_attempt01-03.json — 1661 bytes — SHA-256 5df75913d54576ba81aa26cbfd8bce044d9ae86b8edecd0046a92700311ce000 — failure analysis
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_runner_R11_attempt02.json — 985 bytes — SHA-256 6726417674f5c40a7c78db9c9598ce5069197fa697636b2a59dbf9525330a1e3 — child exit receipt
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt02.stderr.txt — 618 bytes — SHA-256 0289b5e9efb6ea9fe330c4c68504ded86ca7529949038d54f18f7fdb84ce4878 — raw error output
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_runner_R11_attempt03.json — 985 bytes — SHA-256 a7bd9757a15d5e4b75bd9b7a730e9e7cf73025dc189215c0309ccc3ad03c93f5 — child exit receipt
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt03.stderr.txt — 647 bytes — SHA-256 332930a400b7d284c812ef9fc40fc2ff2ec2ca2501bad976c5a7e88c8c11f10c — raw error output
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt04.ps1 — 6581 bytes — SHA-256 b3458ecbfbc7cd5f8231983565989f9c70467f12ec6cb068074e2b46ffc6bb5c — bounded Word exporter script with .NET SHA
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/run_export_word_R11_attempt04.ps1 — 4417 bytes — SHA-256 3fe9dc633d731f0fa95e54ebb3f4601275a72c653695eef0a91da6b55c3fe65d — hidden timeout/ownership runner
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt04.stdout.txt — 0 bytes — SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 — raw stdout
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt04.stderr.txt — 0 bytes — SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 — raw stderr
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_owner_R11_attempt04.json — 686 bytes — SHA-256 ee5a1233a38edb3c32d79fb969a938c64b6f1266d3f6970ebf5bc51dabe687ac — Word PID owner marker
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_timeout_R11_attempt04.json — 1055 bytes — SHA-256 e6408041e27609595ab72ec959ce57f5e31a4abc256b3bf68376ae74c909b415 — 150-second timeout
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_export_owned_process_cleanup_R11_attempt04.json — 1310 bytes — SHA-256 d7306e4e1e64a24029c52b87426a482ac06c8aec53b43cee85e5a10110cde7ab — exact owned PID cleanup and timestamp comparison
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_native_ps5_module_probe.stdout.txt — 311 bytes — SHA-256 427ba2967f80924b219a0c0e18f4faf1a961af8de7112baf2e35f6286abf1937 — native PS5 module probe stdout
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_native_ps5_module_probe.stderr.txt — 1148 bytes — SHA-256 c5328774a7fd821db8fa7149acb35e16c999c48cff3b998e0b9666496c0a76a2 — native PS5 module probe stderr
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_native_ps5_module_probe2.stdout.txt — 574 bytes — SHA-256 7704cd66935a16dca8fa6aad194b9187246ba8a15159d0089e7dfcbf73860a9e — native PS5 module probe stdout
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/evidence/word_native_ps5_module_probe2.stderr.txt — 608 bytes — SHA-256 15666eead3bb35125757119f6fbba9515cc1c062e80b7686a18b4d8fd5edddb9 — native PS5 module probe stderr
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/candidate/0111_I18-E20_特殊績效及社會面成果證據登錄表_R03.docx — 75015 bytes — SHA-256 f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50 — unchanged candidate reference; already remotely present
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt01.ps1 — 5819 bytes — SHA-256 13cd6f6caa8fe35893e85b4bbbc007b6b56edd281b6b2c21e3bc22f00aed22d7 — first exporter script
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/run_export_word_R11_attempt01.ps1 — 4390 bytes — SHA-256 20f2c78dbe79cf24db5c2967f5b939eed510a25a66b6ad9e58e013a7d71a71e8 — first hidden launcher script
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt02.ps1 — 5822 bytes — SHA-256 f820e7a82fe4da0fc6c52a7f360e1948993d259f2658cb3105627c5082f5a344 — second exporter script; native hash cmdlet unresolved
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/run_export_word_R11_attempt02.ps1 — 4418 bytes — SHA-256 b1b8b7b1ed05109dbf113e68e610a5c5897be95e27df1b987da86dc8d9390ce5 — second hidden launcher script
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/export_word_R11_attempt03.ps1 — 6400 bytes — SHA-256 67e318cb2447debd337d4774d4b81ed8a17a134e7a5b38259cd376dae595a84b — third exporter script; catch diagnostics repair
- docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R03_20261023/writer/run_export_word_R11_attempt03.ps1 — 4415 bytes — SHA-256 cde02f3dd5096ffe15da87fc79b6759bc649367ca66224f6607c1c8908fc607d — third hidden launcher script
