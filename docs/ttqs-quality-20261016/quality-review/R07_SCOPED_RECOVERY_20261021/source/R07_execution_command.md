# TTQS ONE｜2026-10-21 深度外部稽核與 Codex 精確施工指揮 R07

> **COMMAND=TTQS_ONE_20261021_DEEP_AUDIT_SCOPED_RECOVERY_R07**  
> **PROJECT_ID=TTQS_ONE**  
> **對象**：Windows 10 原生 Codex（總控）與 OpenCode v2 CLI／Antigravity CLI（已授權的 Worker）。  
> **狀態**：CANDIDATE INSTRUCTION，供 Codex 領取，不代表 Windows 已執行、不代表正式 TTQS 驗收。  
> **任務**：保存已完成的七份 Word、修復真缺陷、阻止無效重跑，恢復低 Token 的 CLI 外包與準確 GitHub 同步，持續下一件真正 READY 的文件。  
> **最高限制**：不擴權、不花新增費用、不使用 Computer Use、不捏造真人／第三方／簽章／同意／實績、不使用未授權模型、不建立第二套任務／資料庫／Supervisor／排程。  
> **注意**：Human 最新 Mission 已授權可逆候選施工，不能因上一個 Session 或單一 Worker 故障要求逐件批准。新費用、OAuth/MFA、重大權限、正式送審／接受、真實對外效果仍屬真正 Human Gate。

## R07 最新讀回與不重做原則（2026-10-21 約 14:00 台灣時間）

**本節優先於本檔較早記錄的 0099 R01 待修描述；它是新的 GitHub LIVE 觀察，不代表已取得 Windows OS 即時狀態。**

- PR #92（open／draft），最新 HEAD：`3308da622ed43f2bb37f3f757e4744ae359c43a6`；分支 `work/ttqs-one-document-quality-contract-20261016`。
- 0099／I18-E07 的 `UNIQUE_BLUEPRINT_0099_R02.md` 已由提交 `edd017abc7d815a612e43ffce40d6dd34f1d3e64` 建立，並由 `3308da6...` 補充澄清；Git blob `5ec600d4fe2bed76b448daf80382d39dacc5d93b`。R02 明示取代 R01，R01 原有 160 格錯誤只作歷史反例，**禁止再把 160→80 當成未完成的修稿任務**。
- 本輪直接對 GitHub R02 表格重算：8 人、前後各 5 維共 80 個原始評分格；逐人總分與差值 8/8 一致；前測總分 75、後測 117、平均增加 5.25；後測符合合成教學門檻 6/8。這僅證明藍圖數值的限定範圍檢查，**不是 0099 Word 建置或正式品質通過**。
- 最後觀察到 0099 遠端目錄僅有 inputs/R01 與 R02 藍圖；沒有本輪可證實的 0099 DOCX。Windows 可能已繼續生成，先查目前工件、PID、session、工作目錄及輸出 SHA，**不得自動重派同一 Writer**。
- 0092～0098 七份 GitHub DOCX 二進位的 SHA-256 已由外部稽核獨立重算，7/7 與報告相符；**檔案存在不等於七份品質全通過**。
- **仍未完成的是真正 Windows 執行、0096 收據 SHA 衝突、0096 內部索引錯用、0098 實體 Word 工程資訊核對、0097 Word 輸出、0094 reviewer 判定及 0099 Word 完成與驗收。** 僅修未證實已關閉的缺陷；發現更新的實物與受信收據後應立即縮減施工範圍。
- GitHub 內容是公開候選稽核副本，R06/R07 是施工指示；正式接受、真人資料、已部署背景工作與新增費用均不得自動推定。

## A. 執行前只讀事實：嚴格區分四種證據

- **LIVE GitHub**: 2026-10-21 ~14:00 Asia/Taipei fresh read of PR #92, `PT-Original-Point/ttqs-one`, `work/ttqs-one-document-quality-contract-20261016`, HEAD `3308da622ed43f2bb37f3f757e4744ae359c43a6`, OPEN/DRAFT. This is a point-in-time observation; reread before any mutation.
- **Latest GitHub delta**: `3308da6` clarified 0099 Blueprint R02; `edd017a` created R02 fixing 160 to 80 scoring cells and synthetic safeguards; `74e3176` created historical R01; `5c071e3` read back 0098 R08. Current 0099 specification is R02, not R01. No 0099 DOCX was present in the most recently fetched 0099 directory.
- **Human 指示／專案 Mission**：`docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md` Git blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`；157 項索引 `03_157_CHECKBOX_BLUEPRINTS.md` Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`；外包/同步增量 §5 `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` Git blob `263aaca84891bba8dca087875804343c3670e921`。以上有候選性質，不能自己冒稱覆寫舊正式 canonical；新 Human Mission 可逆施工仍可合法繼續。若版本不相容，標 `SPEC_CONTROL_PLANE_REBASE_REQUIRED`，但不以舊 CP 阻擋已批准準備施工。
- **LOCAL HISTORICAL**：Human 交付本機報告的共同 24h 窗 `2026-10-20 09:46:38`～`2026-10-21 09:46:38` 台灣時間；R03 凍結 11:47:30。這些報告的 Windows PID/程序狀態、當時模型 quota 不代表現在仍然相同。

### 四份附件完整性（已在外部稽核端實際重算 SHA-256）

| 附件 | bytes | SHA-256 | 判讀 |
|---|---:|---|---|
| `TTQS_ONE_本機施工記錄_最近24小時_20261021.md` | 39,472 | `50821b4b9774e1c0551c2f9f6aa5fb775dd146b4d6475bf507834a1a217aec30` | 24h 主要摘要 |
| `TTQS_ONE_Win10_本機施工歷程_外部稽核整合總報告_20261021_R01.md` | 13,700,200 | `1ad94bb79c5745b229cfa30381531d613cc56180bd103b53654b0d4ce171c5ac` | 帶大量歷史附錄 |
| `TTQS_ONE_Win10_本機施工歷程_外部稽核整合總報告_20261021_R02.md` | 13,958,595 | `e365623f306aea4e46897dd474c6d886a5d4c11968bac401fef723b7809cd943` | 前 13,700,200 bytes 與 R01 完全一致，後附 258,395 bytes |
| `TTQS_ONE_Win10_本機施工歷程_外部稽核整合總報告_20261021_R03.md` | 13,972,163 | `c92a524fa5c8ac9e8fbc8ad7e7430edcc1a94e5cce19cc10f399c27a4e75108d` | 開頭新增 13,568 bytes，後面逐位元組嵌入整份 R02；99.90% 是重複歷史 |

**成本命令**：R03 14 MB 只作歷史鑑識，不可每次喚醒重新全文餵 Codex 或 Worker。日常只讀本 R07、當前 Human/正式規格、受影響文件的最新 SHA/收據與 GitHub diff；沒有實質變化用 Git/OS/檔案雜湊退出，不呼叫高階模型、不寫報告。

## B. 外部稽核的直接成果與風險

### B1. 確實有遠端 Word，全部 7/7 重算成功

外部稽核從 **GitHub API 二進位內容（非 Codex 報告中的自報）**獨立重算下列七份 DOCX 的 SHA-256，均與本機報告所宣稱的最新指定版本相同。這一項 `REMOTE_DOCX_BYTES_MATCH=PASS(7/7)`，不等於 `QUALITY=PASS`。

| doc_id | requirement | version | remote independently hashed SHA-256 | 品質現況（分層） |
|---|---|---|---|---|
| 0092 | I17D-E06 | R03 | `ed577847dba59d29cd1da0d1d64372a21ed07d8aee164ff044c3870ff958391b` | 技術+18頁版面收據 PASS、OpenCode 文字語意 PASS；reviewer 未獨立讀 DOCX 二進位或看頁圖。保留 CANDIDATE。 |
| 0093 | I17D-E07 | R16 | `d12b256f2a0162749ff685235e90665a0d440a0f4c6365da00fbbe1c479707e5` | R15 全文語意 PASS 附3項 minor；R16 僅第7/34頁差異 PASS；不要重做無變更頁。CANDIDATE。 |
| 0094 | I18-E01 | R18 | `ecf9717cdc7f7785ed6c7b18b9dd8e29af21a5b2641e13acf3b4b813371b5e18` | 技術及23頁視覺收據 PASS_SCOPED；OpenCode 一次未執行26項工具請求、後兩次403，沒有語意 verdict。REVIEW_LANE_BLOCKED，不重建原 Word。 |
| 0095 | I18-E02 | R15 | `c70521d50fbec6cdc3b53ce3dc35fa2613069e60c58625b7eb2f96a5a6fd3658` | 技術/46頁版面收據 PASS；R15 只對頁碼定位 F-01 差異 PASS，不可冒稱 R15 全篇新審。CANDIDATE。 |
| 0096 | I18-E03 | R13 | `6ece53befed3ecb1b42e523b80da80decd33b0a7d55e4e1fe75ddf79b905d445` | 技術/69頁版面收據 PASS；review packet 是 R13，但 return receipt 仍寫 R12 SHA，exact-SHA review chain `CONFLICT`。CANDIDATE；只停錯綁驗收，不重造 Word。 |
| 0097 | I18-E05 | R07 | `026288491716d626a7bcac14a515313da7846f5a204703da9bad3a9010edf214` | 技術/有界語意差異 PASS；Word COM PDF 匯出 300 秒+120秒仍無本版 PDF，視覺 `UNKNOWN/BLOCKED`。CANDIDATE。 |
| 0098 | I18-E06 | R08 | `a5d4bb14c884ff2d19db7bb6a86f999de0604d9ac6bacd9eb26f0b5db2c9cdba` | 遠端 R08 技術 PASS、29頁 scoped visual PASS、OpenCode 文字語意 PASS，192 筆清冊；但現行 manuscript 有工程 SHA/路徑疑點，必須依 Human 正文契約核對最終 DOCX。CANDIDATE，未正式接受。 |

### B2. 最需解決的 Finding 清單（只修精確受影響範圍）

| Finding | 嚴重度 | 可定位的事實 | 合法最小修法／結案證據 |
|---|---|---|---|
| F01-0096-REVIEW-BIND | P0/驗收 | `0096_R13_20261021/review/review_input_manifest.json` DOCX=R13 `6ece53...`、packet SHA `514296...`；同資料夾 `return_receipt.json` DOCX 卻為舊 R12 `1c4626...`、packet SHA `cadad0...`。 | 不改原始歷史收據。查原生 `stdout.jsonl`、當次真正交付 packet bytes、reviewer response 和 session ID 是否確實綁 R13。若能證明只有收據組裝錯，另附勘誤收據且原回條保留；否則原結論不得升格，待合法 reviewer 一次 bounded 覆核。**不重建69頁 DOCX**。 |
| F02-0098-HUMAN-BODY | P1/內容契約 | 遠端 `0098_R08_20261021/candidate/0098_R08_manuscript.md` 第49、443、444行有實際 64位十六進位 SHA、內部版本及路徑；Mission 01 第45行禁止工程 SHA/控制欄位進人類展示正文。 | Windows 對最終 R08 DOCX 重新抽文字；若確認正文同樣出現，僅搬到 README/manifest/sidecar，保留人類能理解的來源說明。新增 R09 只修受影響內容並做頁面/語意必要差異驗證；若只存在 manuscript 而不在 DOCX，先修文字來源/側錄，不亂重建 DOCX。 |
| F03-0098-PATH | P1/可取用性 | 同稿第443行寫 `evidence/0098_R08_synthetic_replacement_register.csv`；現行 GitHub 真實檔案為 `evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`，且 DOCX 位於 `candidate/` 下。 | 比對 Word 是否含該錯誤文字；修正 sidecar/正文中受影響部分，提供真正可用的相對取用方法。修改實體 Word 才新 revision/SHA；需點開實際檔案測試，不接受「文案宣稱已修」。 |
| F04-0096-CHECKBOX-ID | P1/需求身分 | `03_157_CHECKBOX_BLUEPRINTS.md` 內部 157 項順序：0092 I17D-E06 對 099；**0096 I18-E03 對 104**。但 0096 GitHub 多個 mapping/review/README 把 `official_checkbox_serial=099`，錯綁且與0092碰撞。官方 PDF p6 是未印刷流水號的核取欄。 | 保留 requirement ID I18-E03 與 DOCX ID 0096；把 099 改成「專案157項索引=104」，「官方印製流水號=不適用/來源未印列」，不要用舊欄偷偷稱官方 104。先修衍生 mapping 收據；若 Word 有錯標再定點改 Word。保留舊 SHA/歷史不變。 |
| F05-0094-403 | P1/Worker | `0094_R18/opencode_route_receipt.json`：首次 26 個 tool calls 均未執行；之後 MiniMax/MiMo 各一次 HTTP 403，無 verdict，第一次 input 91,352、cache_read 1,168,092。 | 停掉當時失敗路由；優先用 **10/21 11:34 曾在 0098 R08 成功的** `opencode/nemotron-3-ultra-free`（仍需 OS/CLI fresh 可用性、no-new-cost 核對）作一次受限唯讀 R18 review；任一403立即停該路由，改做其他 READY。不改 Word。 |
| F06-0097-WORD | P1/版面 | Word 開檔診斷約0.9秒成功，但 ExportAsFixedFormat >300s、SaveAs2 >120s，沒有同 R07 SHA 對應的 PDF；若存在其他舊 WINWORD 程序不能直接殺。 | 確認所有活躍文件及 Word PID/owner，於隔離 Office automation 範圍有界修 renderer；一旦從 **R07本版** 得 PDF+PNG+相同候選 SHA，完成 scoped visual；失敗只停該 render lane。絕不沿用 R06 PDF。 |
| F07-0099-BLUEPRINT-MATH | CORRECTED IN GITHUB CANDIDATE / verify OS | R01 contained a wrong 160-cell figure; current R02 `UNIQUE_BLUEPRINT_0099_R02.md` resolves it to 80 raw cells. Direct recalculation found 8 consistent learner rows, 75/117 totals, 5.25 mean gain, 6/8 sample threshold. | Do NOT repeat the 160-to-80 edit or rewrite R01. Verify R02 and actual Windows writer status before continuing; this does NOT mean the 0099 DOCX exists or passed QA. |
| F08-0099-SOURCE | P1 / next writer | I18-E07 has source-bound Blueprint R02 on PR #92; at last live read GitHub shows `0099_R01/inputs/` with R01 historical and R02 current; no 0099 DOCX was observed. | If OS confirms no active 0099 writer and current task is READY, dispatch exactly one writer based on R02; if writer is in progress recover the result without duplicate dispatch. |
| F09-REPORT-BLOAT | P1/Token | R03 13,972,163 bytes，99.90% 為同位元嵌入 R02；R02 又有98.15%重複 R01。R01/R02 原文保留有稽核價值，但每回合全讀完全無必要。 | 保留所有原始檔，不再嵌套新一版巨型報告；只有新 Finding+新 SHA+結果的增量 PR/短 receipt；未有變化就 L0 退出。 |
| F10-SAMPLE-VS-REAL | P1/業務 | 0092～0099 目前均 SAMPLE/SYNTHETIC，沒有實際第三方函、學員真實問卷、同意、簽章、核准與正式評核結果；部分文件達34/46/69頁，內容技術化。 | 製品 QA 與 Human 正式接受分開；保留原完整示範，新增 30 秒導引與小協會可操作流程，**不是把所有工程 SHA/ID或難懂表格塞進 Word**；實際成效不升格。 |
| F11-ANTIGRAVITY-ID | P2/路由 | 10/20 Human GUI/CLI 同一 Google AI Pro 帳戶，CLI /usage weekly 92.52%、five-hour 100%；歷史 CLI 曾有成功長文與 fallback 警告；所有 R03 文字呼叫的真正 provider serving model 仍缺獨立證明。 | 不再要求 Human 重複登入；Windows 同使用者 fresh-read；AGY 只允許 `gemini-3.8-flash-high` 的隔離純文字內容車道，不允許 Computer Use、檔案工具、危險權限繞過或 CCPA fallback 當成 Gemini 合格。無證明則 model identity UNKNOWN，但文字可否回收需獨立判。 |
| F12-DUPLICATE-GENRE | P2/適切性 | 0092/I17D-E06 與 0096/I18-E03 官方核取項都可見「感謝函」，兩份正文都是索取／驗證第三方函件，但指標目的不同。 | 題目盲測、負向鄰項檢查兩件是否實質可區別：17D 為訓後成果/組織工作需求，18 為目標客戶/學員對訓練功能/效用的回饋；不要只改標題、複製同一內文，更不能偽造第三方感謝函。若不同指標可合法共享同一原件，建立各自使用範圍/出處而非兩份假原件。 |

## C. 立即優先序（不等於全部必須串行）

1. **S0 先 fresh-read**：驗證 GitHub/Windows 最新狀態、當前 task owner、未結外部寫入/同步；不能假設上一回合仍在跑，不以 `opencode serve`、舊 WINWORD 或 Codex GUI 長時間顯示替代 OS 活動證據。
2. **S1 current state check**: 0099 Blueprint R02 already fixes the 80-cell count and has been arithmetically verified externally; confirm its bytes and Windows execution status, then continue only uncompleted authorized work. Fix the 0096 incorrect internal item 099 vs 104 separately.
3. **S2 清除無效的品質回條**：0096 R13 SHA錯綁溯源，決定 metadata-only 勘誤還是一次有界重新確認；0098 R08 工程資訊和錯路徑先從實體 Word 抽文核對，不擅自降級所有已核實的數學 PASS。
4. **S3 獨立解決其餘兩條車道**：0097 renderer（不動 Word 正文）、0094 語意 reviewer（不動候選 Word）。一條失敗，另一條仍可進行。
5. **S4 經 S1 通過且無現役寫入競爭後，0099 派**單一 Worker 產專屬完整文字；Windows 原生產 Word、QA，另一個模型/Worker 審 exact SHA。已通過的 0092/0093/0095 不重跑。
6. **S5 最後 GitHub 同來源讀回**每個新增穩定候選/QA/狀態/重大事故；不為每分鐘小進展 commit。完成一個真正 material delta 就接下一個 READY；如僅候選而無 REAL，保持 NOT_ACCEPTED。

## D. Codex 逐步施工操作：每一步都有輸入、輸出、通過／失敗分支

### S0｜真正接管目前 Windows 與 GitHub（第一優先、唯讀）

**輸入**：`E:\TTQS`、本機既有 `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016`、已知 10/20 歷史同步工作目錄 `E:\TTQS\_github_sync_0064`（只是曾出現的路徑，執行時必須 Test-Path/驗證 remote）；現有 PR #92 與 01/03/06 原文。不得直接套用歷史 PID、歷史 HEAD 或歷史 phase。

**0.1 用 Windows PowerShell 5.1 唯讀確認**（已有類似原生收據時直接重用，不能為了做漂亮報告重複掃整個 E 槽）：

```powershell
$ErrorActionPreference='Stop'
$project='E:\TTQS'
$work='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016'
$repo='E:\TTQS\_github_sync_0064'
foreach($p in @($project,$work,$repo)) {
  '{0} => {1}' -f $p,(Test-Path -LiteralPath $p)
}
whoami
Get-Date -Format o
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -match '^(agy|opencode-cli|WINWORD|python|node|codex)(\.exe)?$' } |
  Select-Object ProcessId,ParentProcessId,CreationDate,Name,CommandLine |
  Format-List
if(Test-Path -LiteralPath (Join-Path $repo '.git')) {
  git -C $repo remote -v
  git -C $repo status --porcelain=v1
  git -C $repo branch --show-current
  git -C $repo rev-parse HEAD
}
```

**安全限定**：原生命令列可能有憑證、Email、URL token、完整 prompt。Codex 應在本機核對，公開 GitHub 收據只保留遮蔽後可驗證的程序身分／PID／時間／狀態，不公開 secrets。`WINWORD.EXE` 與 `opencode-cli.exe serve` 的 PID 不足以判定活躍 Writer；對每個疑似進行中工作，核對工作目錄、輸出檔 `LastWriteTime`、CLI session、原生子程序、其任務/候選 SHA。**不能看到 PID 就重派／殺掉程序**。

**0.2 GitHub fresh-read**：再次從 GitHub provider `GET PR #92`（repo、head branch、head SHA、draft state）、本分支 `01`、`03`、`06`，`quality-review/0092..0099` 最新包、目前 PR 最後幾筆提交與評論。若 GitHub HEAD 已較本手冊的 3308da62 前進，必須重算有效 finding；新實體 DOCX 已修好就只核對收據並結案，不再照舊命令重建。

**0.3 唯一 Worker 檢查**：對任一文件 `doc_id`，當前本機有且只有一個已確認 owner 可寫入該候選；若有不明 writer，先採保守不覆寫、只讀確認。`RUNNING` 字串及過期 lease 不等於 OS alive；未知結果不要盲重派。不同 doc_id 且真正相互獨立的 READY 工件可以平行，但同一 `CURRENT`、register 或 Word 目標只能單一 writer。

**輸出**：只需一段不超過約 20 行的本機摘要：`repo/ref/head`、未提交/未同步差異、現役 writer 的 PID+doc_id、`0092..0099` 每件 current SHA/品質範圍、受阻車道、下一個合法步驟。不存第二份任務 DB。

**判定**：repo 精確綁定＋無雙主＝`S0_PASS`；若 repo 路徑不在上述位置，先從現有 git worktree / Codex 工作目錄找實際 remote，不新建 repo、不把不存在當作已同步；若 Windows 無法讀 PR，保持已授權本機唯讀工作，PR 寫入車道暫停。

### S1 | Verify 0099 Blueprint R02 and continue an existing writer; do not re-edit R01

**Current source**: `docs/ttqs-quality-20261016/quality-review/0099_R01/inputs/UNIQUE_BLUEPRINT_0099_R02.md`, Git blob `5ec600d4fe2bed76b448daf80382d39dacc5d93b`; R01 blob `2d8d0ff...` is historical. Keep official I18-E07 p7, internal 157-item index 108, and original source/crosswalk bindings.

**1.1 CURRENT R02 IS ALREADY FIXED**: R02 says 8 learners x 2 stages x 5 dimensions = 80 raw scoring cells. Derived totals and threshold classifications are additional facts, not raw scoring cells. External check passed row sums (8/8), pre=75, post=117, change=42, mean change=5.25, pass=6/8. Use fresh OS and GitHub to confirm no newer edits. Do not produce R03 simply to correct this already-fixed issue. Confirm whether Windows 0099 worker exists/already finished; unknown effects require readback before redispatch.

**1.2 確定性重算**：使用本機已有 Python 或最小短暫 Python 指令（不可為此增加服務）檢查以下資料。這是目前已核實 Blueprint R02 的固定測試向量；若新的正式 Blueprint 在 S0 後已改動，先用最新來源重新生成向量，不能強行使用舊值：

```python
# 0099 Blueprint R02 reference fixture; synthetic demonstration only.
rows = [
 ('A01',[2,2,1,2,1],[3,3,3,3,3]),
 ('A02',[2,2,2,2,2],[3,3,3,3,4]),
 ('A03',[3,2,2,2,2],[3,3,3,3,2]),
 ('A04',[2,2,1,2,2],[3,3,2,3,2]),
 ('A05',[3,3,2,2,2],[4,4,3,3,4]),
 ('A06',[1,2,1,1,2],[3,2,2,3,2]),
 ('A07',[2,2,2,2,2],[3,3,3,3,3]),
 ('A08',[2,1,2,1,2],[3,3,3,3,2]),
]
assert len(rows)==8 and len({r[0] for r in rows})==8
assert all(len(pre)==5 and len(post)==5 for _,pre,post in rows)
assert len(rows)*5*2 == 80    # 不是160
pre_sums=[sum(r[1]) for r in rows]; post_sums=[sum(r[2]) for r in rows]
assert sum(pre_sums)==75 and sum(post_sums)==117
assert sum(post_sums)-sum(pre_sums)==42
assert sum(1 for _,p,q in rows if sum(q)>=14 and q[1]>=2 and q[3]>=2)==6
assert [sum(pre[i] for _,pre,post in rows) for i in range(5)]==[17,16,13,14,15]
assert [sum(post[i] for _,pre,post in rows) for i in range(5)]==[25,24,22,24,22]
print('0099 R02 FIXTURE CHECK PASS: 80 scoring cells, totals 75/117, 6/8 pass')
```

**1.3 寫作模型不得自己修改 fixture**：0099 SAMPLE 的8人、5維、同一基準及統計公式先固定；如原數據不合理，由有界修訂的 Blueprint 明確標理由、受影響欄及新 fixture SHA，而不是在 Word 中偷偷改分數。算術不通直接 `BLUEPRINT_PREFLIGHT_FAIL`、**0099 Writer 車道暫不派工**；其他0094/0096/0097/0098車道照常。

**1.4 genre 與協會適切性**：0099 是**學習技能面**，不得把0097「自認能力提升問卷」或0098「調查系統滿意度」換標題重用。既有 0099 Blueprint 使用「志工服務活動紀錄整理與佐證判讀」完整合成案例，有8份前後技能作品、五維量規、180分鐘示例與改善追蹤；是 SAMPLE，不是協會已開課證據。保留專屬實際操作練習，內容以原始點協會小團隊行政可行為先，不憑空設大型教研、數據分析、HR 部門。

**R07 completion fields**: `0099_BLUEPRINT_R02_BLOB=<fresh>`; `scoring_cells=80`; `sample_math=PASS_SCOPED`; `OS_0099_WRITER=<verified/UNKNOWN>`; `0099_DOCX=<exact SHA or NOT_YET_VERIFIED>`; `NEXT_READY=<safe action>`. Do not assert DOCX/QA completion based solely on the blueprint.

### S2｜0096 審查 SHA 錯綁及 157 項序號（不得直接修改舊審查回覆）

**2.1 定位同一份 GitHub 候選**：
- `docs/ttqs-quality-20261016/quality-review/0096_R13_20261021/candidate/0096_R13.docx`，SHA `6ece53befed3ecb1b42e523b80da80decd33b0a7d55e4e1fe75ddf79b905d445`。
- `review/review_input_manifest.json`：同候選 R13 + `review_packet_sha256=5142964a...`。
- `review/return_receipt.json`：`candidate_docx_sha256=1c462613...`（R12）且 packet `cadad053...`；**這是已在遠端原文核對的實際衝突**。
- 原始 `review/native_cli_stdout.jsonl`、`review/independent_semantic_review_response.md`、`review/session_export_sanitized.json`、`review/review_packet.md`；先求出各原始 SHA。遇到出錯原因未知，不重派相同 Worker 自證。

**2.2 決策分支**：
- `A: OS 本機 raw dispatch argv/input payload + session + response` 能夠證明當時 reviewer 確實看 R13 及其全量/有界範圍，而 return receipt 後製時錯貼 R12 → 新增**獨立勘誤收據**記載原錯欄、正欄、生成因果、原收據 blob 及本機可讀證據、修正的 review scope；保留舊回條不覆寫、不要求重新審稿。
- `B: 無法證明 reviewer 究竟看哪版` → 狀態 `REVIEW_BINDING_UNKNOWN`，不能由 Codex 改一個 JSON 欄就蓋 PASS。允許一個範圍明確、不同 Worker 的 read-only 0096 R13 exact-SHA 複核，只有在可用且合規的模型路由下派一次；若無路由，維持本條 reviewer lane BLOCKED。
- `C: 實際查出讀舊 R12` → R13 語意未完成；保存歷史結果，派一個新 reviewer 而非假修收據。

**2.3 修序號且避免移花接木**：`03_157_CHECKBOX_BLUEPRINTS.md` 逐項說明：索引099是0092/I17D-E06；索引104是0096/I18-E03。官方 PDF p6 沒有印這種流水號。對 0096 的 `official_checkbox_serial=099` 類欄位更正為**內部施工索引 104**和**官方印製序號未提供/不適用**兩個不同欄。錯誤出現在原生 Word 時只做必要的 R14 局部修訂；若只存在 metadata，DOCX SHA 不變。掃描 0092 與 0096 是否因同一索引碰撞而共享錯誤來源、同篇正文或混用第三方來函，必要時做 title-blind/negative neighbor 判斷。

**結案條件**：精確來源、同一候選 SHA、reviewer 確實輸入 SHA、回覆 SHA、勘誤與 PR 遠端讀回可連成一條鏈；否則 `OPEN`，不能打 `PASS`。真實感謝函原件依然 `HOLD`。

### S3｜0098 R08：保存已通過數學與29頁候選，只處理人類正文與路徑的真缺陷

**3.1 不准立刻開 R09**：先從目前最新的本機 `0098_R08.docx` 和遠端固定 Git blob `3d49780e1e7f6495b50fbf31690fd24378638466`，取得 DOCX 實際正文閱讀順序（標題、一般段落、表格儲存格、頁眉頁尾、超連結文字）；以現有 python-docx/Word 擷取，不用模型猜。分開比對 `candidate/0098_R08_manuscript.md` 第49／443／444行。留出「Word body」「sidecar」「原始稿」三欄證據。

**3.2 人類正文掃描**：一般資訊呈現可以講「來源檔案、可回復、版本」，**不應**在給國中生和協會行政操作的正文硬塞 `doc_id` 原料欄、64位原始 SHA、JSON 欄位、GitHub 路徑或內部未解鎖的系統操作。以確定性檢查列出可疑所在章/表/儲存格，人工/有界 reviewer 再辨別：

- 危險例：直接出現 `9fa51aef...e29e4`、`f7cf2071...7dbe...`、`evidence/0098_R08_synthetic_replacement_register.csv`、Git repo路徑、原料 `fact_id`、未解釋工程 metadata。
- **不可錯誤封鎖**：「正式對外問卷匯出時需保存原始檔案雜湊」這種教學性說明有其業務用途；只有嵌入實際內部 SHA／工程路徑的控制資料才移出人類正文。
- 人類可用寫法示例：「本件為填妥的示範調查；如將來改用真實資料，依同套件『示範事實替換清冊』逐筆核對；請勿將示範勾選當作真人同意。」完整 SHA、FACT ID、退役譜系及檔案定位放在 `README/manifest/evidence` 內，不刪證據。

**3.3 路徑查核**：manuscript 的 `evidence/0098_R08_synthetic_replacement_register.csv` 在 GitHub 上不存在；實際相對套件路徑 `evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`，且候選 Word 在 `candidate/` 子目錄。把「給人找資料的說明」修成從套件根目錄可找到的正確位置；若 Human Word 正文真的有這串錯路徑，產生新 R09 exact SHA/最小版面變更。若只有 manuscript 有錯，只對它與相關側錄採正確修復，不擅改已完成的 R08 Word。

**3.4 驗收依賴精確差異**：
- 未改 DOCX bytes：保持 `0098_R08 SHA=a5d4...c9cdba`，不重渲染、不重做 78,455 input-token 全篇審查；只新增受影響側錄與路徑核對收據。
- 有改 DOCX bytes：新 revision（R09 或目前尚不存在的新合法版次），由同一 Word 輸出新 PDF，所有有變的頁面高解析目視，未變頁須以**同一渲染器與設定**證明逐頁一致；核對數據 12受邀/11唯一/10有效、Q3=3.30、總均=4.00、192 清冊事實及 SAMPLE/同意界線，對新 SHA 做受影響的獨立語意審查。若修正意外更動實質分析或整份文類，才擴大審查範圍。
- 不准以舊 `0098 R04 PARTIAL` 覆蓋已取得 R08 的好結果；也不准以 R08 model PASS 免除 Human 正文契約的已定位缺陷。

**結案**：word-body 檢查位置、路徑 existence check、受影響頁清冊、新舊 SHA、review scope、remote Git readback；現有 R08 的 REAL 和正式接受仍為 NOT_GRANTED。

### S4｜0097 R07：Word COM 匯出故障（獨立版面車道）

1. OS 讀取 R07 固定 DOCX SHA `026288...d214`；確認檔案可用 Microsoft Word 開啟、Docx zip 完整，不重建無關文字。
2. 列出所有 `WINWORD.EXE` PID、owner/啟動時間/父子程序、開啟的文件與最近輸出；不確定來源的程序**不可直接 Taskkill**，可能有真實使用者或其他文件正在使用。
3. 找出先前 `ExportAsFixedFormat >300s`、`SaveAs2 >120s` 的原生錯誤、Word COM instance、壞掉的 PowerShell Quit 調用。先修原命令簽章與隔離環境，不使用「再多等半小時」的方法。
4. 若確認可在安全的隔離 Word instance 試一次，設明確的 timeout（依既有已核准上限）、核對生成 PDF `mtime`、頁數/大小、來源 Word SHA 於前後不變；有任何操作效果不明時停止該渲染實例，避免多次幽靈 Word。
5. 若兩次已證明無法輸出且環境無實質改善，維持 `VISUAL_BLOCKED_WORD_COM`；不要用舊 R06 PDF 替代。可評估**已存在且獲准**的替代渲染路線，但不自動安裝新軟體、不擴大權限或啟付費工具。
6. PDF 成功後，PDF→PNG→contact sheet 應**同一 PDF SHA**，頁碼完整、抽樣高解析至少變更頁＋可能跨頁頁；對所有頁有可見概覽/一致性證據，不以一張縮圖假稱審查者看過每頁原尺寸。獨立語意 delta 原 PASS 保留範圍。

**結案**：`0097_VISUAL=PASS_SCOPED_WITH_EXACT_SHA` 或 `BLOCKED` + 已驗原因；不改 Word 成品才不新 version。

### S5｜0094 R18：停止舊免費路由重試，拿真正的獨立語意結果

1. 固定 DOCX R18 SHA `ecf971...b18`、`DOCX_TEXT_EXACT.txt`、源 PDF 第6頁、專屬 Blueprint、46列清冊與近鄰 0095/0096；**不重建候選**，不要再次要求 build agent 審判。
2. 查 `opencode-cli.exe --version / --help`、既有自由模型監控報告與最新**原生成功收據**。10/21 11:34 0098 R08 已使用 `opencode/nemotron-3-ultra-free` 返回語意 PASS；可優先評估同一可用 route，**但目錄列出/歷史成功 != 現在可用、費用仍要合規**。
3. 只派一個 `--agent plan` 或此環境已實證的唯讀 agent，不允許 Worker 執行檔案、shell、建立工具 call 或改候選；packet 只放 I18-E01、當件 R18 完整文字、必要 SAMPLE、負向鄰項與精確 SHA，不重複載入其他 157 格、14 MB 活動史。
4. 返回必須含 `verdict=PASS/PARTIAL/FAIL`、doc_id/I18-E01、candidate SHA、審查範圍、證據引用位置、具體缺陷、SAMPLE/REAL 界線、source/neighbor；原生 exit/stdout/stderr/session/報稱模型/用量分別記。`exit 0` 不等於有 verdict；`403/429/no-route` 若未有新實質前置變化，**停止該 route，不重試同一錯誤**。
5. 如無合格免費路由，不得偷偷切付費模型；`0094_REVIEW_BLOCKED`，續做0097/0099等 READY。若已成功，保存原回覆與 scope，遠端同步 QA，不必為結論再重建 Word。

**結案**：有來源綁定、真實非空判定、無未執行工具請求誤充結果，`REVIEW_RESULT_WITH_SCOPE`；否則列出實際阻擋原因。實際 serving model 無供應商收據仍記 UNKNOWN。

### S6｜0092／0093／0095：避免誤傷已穩定候選

- **0092 R03**：18頁 Word＋文字審查 PASS_WITH_SCOPE；未取得真實第三方感謝函。只處理確定的新錯件/內容缺陷或必需的最小metadata；不要為了 Reviewer 沒讀二進位而重寫候選，因遠端二進位本次外部已獨立重新算 SHA 相符。
- **0093 R16**：R15 全篇 reviewer 加 R16 第7/34頁 delta 是有界可用證據。原本文內有功能性真空白工具及完整 SAMPLE；若抽查真找到未填示例再有界修改，不因搜尋到「待核/空欄」就一律打 FAIL。
- **0095 R15**：46頁、211筆清冊，F-01 是頁碼 p38→p39 的 bounded review；真實完成稿品質不可被單一 delta PASS 無條件擴張。其他正文語意已有原始先前審查時應先檢視其 scope，僅補未覆蓋或已定位缺陷，不無故重審。
- 三件沒有 material delta 就不叫模型、不新增版本、不重寫 SHA；正式接受／REAL 均維持 NOT_GRANTED/UNKNOWN。

### S7｜真正的 CLI Writer/Reviewer 派工與回收（省 GPT/Codex Token 的核心）

**7.1 先決策「需不需要模型」**：

| 實際變動 | 正確處理者 | 可以跳過什麼 |
|---|---|---|
| SHA／來源路徑／metadata／目錄或無需判斷的字級錯 | Windows Git/Python/Word L0 | 不呼叫 Codex 高階作文、不呼叫第二位 Reviewer、不重寫完整 DOCX（若僅 sidecar） |
| 已有完整正文，只有頁碼/分頁/孤頁問題 | Word/Python 渲染與差異頁 QA | 不重跑全文語意、不重寫合成數據 |
| 內容缺章、官方要求錯件、SAMPLE 例不完整 | 受限 Antigravity 或 OpenCode CLI Writer | Codex 不自行長篇代寫；限定要修的章/表/欄 |
| 需要真正新語意審查 | 不同 Worker 的唯讀 CLI reviewer | 不用 Builder 自評、只審精確 SHA 及必要的正式原文/專屬鄰項 |
| 只是每小時喚醒或前次 checkpoint 無異動 | Git/OS L0 | **不呼叫任何模型、不產生報告** |

**7.2 Antigravity**：只以本機存在的 `C:\Users\J\AppData\Local\agy\bin\agy.exe` 執行，仍先在 Windows 本身 `--version`、`--help` 核對此版本支持的參數；先前成功腳本 `0061_R01/review/antigravity_docx_R03/run_review_R03.ps1` 已有 `--input-format stream-json --output-format stream-json --model gemini-3.8-flash-high --effort high --mode plan --sandbox --print-timeout 15m` 的歷史可讀範例。**請重用當前合法、已實測的原生呼叫形狀，不能把歷史參數當永久 API 保證。** 曾有 `--print-timeout 360000` 缺時間單位致本機 exit 2；必須透過 help 驗證時間格式與 STDIN JSON schema，不能在未派發模型前浪費重試。登入/額度在 10/20 Human GUI/TUI 曾成功同帳戶，但必須由現在的 CLI 自行讀回必要可用性，不能再反覆要求 Human 相同登入。

**7.3 禁止事項**：Antigravity 只作無工具、純文字文稿或審查，`gemini-3.8-flash-high` 是唯一允許請求模型；禁止 Computer Use、shell/file tool、GUI 自動控制、危險權限略過、任意 Gemini→CCPA/其他模型轉接算作指定模型成功。`requested_model` 必填；若原生無提供服務端 `actual_serving_model`，標 `UNKNOWN`；仍可獨立驗證「確實回覆文字」但不能寫「供應商確認 Gemini」。file-writer 事故路由維持 PAUSED，成功文字路由不自動解封檔案寫入。

**7.4 OpenCode v2**：依現役 CLI `--version/--help` 和免費模型監控報告選同時點可用的合法**免費**模型。完整答案任務優先沿用當次原生成功的路由，而非選歷史曾 403 的模型；必要 reviewer 使用已證明可唯讀的 `plan` 或權限禁止的 agent。OpenCode `--agent build` 曾出現26個未執行工具要求，不能再當 semantic reviewer。`cost=0` 僅為 CLI session metadata，不等於 Google／OpenCode／供應商所有費用均零；遇任何付款或 credit 要求直接停止該費用路由並回報真正 Human Gate。

**7.5 每個 attempt 必須回收的最小證據**（使用現有各文件 review/receipt，**不另建任務資料庫**）：

```text
project_id, doc_id, requirement_id, task_kind=WRITER|REVIEWER|PATCH,
input_source_sha, blueprint_sha, candidate_sha_if_review,
requested_model, runtime_model_metadata, actual_serving_model_or_UNKNOWN,
attempt_id, session_id_or_UNKNOWN, started_at, ended_at_or_UNKNOWN,
model_request_sent=TRUE|FALSE|UNKNOWN, native_exit_code,
stdout_bytes, stderr_bytes, raw_visible_response_sha, extracted_deliverable_sha,
result=VALID_TEXT|VALID_REVIEW|PARTIAL_TEXT|EMPTY|ERROR|UNKNOWN,
review_scope=FULL_TEXT|BOUNDED_DELTA|TECHNICAL|VISUAL|NONE,
blocking_findings_with_exact_locations, next_action, git_remote_readback
```

- CLI **命令列本地就失敗**：`model_request_sent=FALSE`，該 attempt 不能算使用了模型，也不產生候選。
- CLI `exit=0` + 空 stdout 或只生成計畫／26個未執行 tool calls：`NO_USABLE_DELIVERABLE`。
- CLI `exit!=0` + 仍有非空有用正文：先保存 stdout/錯誤，當作 `PARTIAL_RECOVERABLE_OUTPUT`，只能在驗證完整性後交下游，不可直接標正式 PASS；不應直接丟掉已得內容。
- reviewer `PASS` 但 candidate_sha、input_packet_sha、response/receipt 互相矛盾：`REVIEW_BINDING_CONFLICT`，拒絕升格。
- 同一前置不變又收到 403／429／no-route／permission denied：停止**該模型×路由×工具 scope**，不要把所有 TTQS 工作陪停，也不要機械重試三次。
- 未取得 request ID／session 存活與否不清楚：先查真正原生程序與檔案，再決定是否重派；未知外部效果禁止盲送第二份。

**7.6 Writer 的唯一交付格式**：每件只回一份**完整的專用文字稿**（或清楚標明受影響節的定點修補），內含真正可用的章節、合成完整答例、表格、公式、必要原件取得流程，與 SAMPLE/REAL 界線；禁止只交 Checklist、JSON 元資料、待填考卷、摘要計畫、三頁共用 SOP 或偽造第三方原件。Codex 先做廉價格式檢查，合格才由已存在的 Python/Word builder 生成 Word。禁止模型自行編造協會真實人名、正式組織架構、核准與成果。

**7.7 Reviewer 的唯一交付格式**：`candidate_exact_sha + verdict + scope + title_blind + closest_three_negative_neighbors + genre_correct + synthetic_register_completeness + math + document_operational_usability + source_locator + explicit_findings`。若 Reviewer 沒看 Word 二進位／PDF/所有頁，必須如實寫 `TEXT_ONLY`；不能把 packet 自帶 SHA 重述稱為「審查者重算 SHA」。重大 finding 應有節／表／欄／頁和最小修補，方便下一輪局部返工。

### S8｜寫稿品質：必須達到協會小型訓練機構、國中程度容易理解，而不犧牲 TTQS 專業

**8.1 使用者可讀 Word 首頁**：以一般行政人員讀得懂的繁體中文，在30秒看到「這份是什麼／對應何官方要求／何時要用／誰可執行／做哪三步／示範資料在哪／真人資料仍缺什麼」。不應有一整頁技術控制表。正文至少10.5pt、表格至少9.5pt，跨頁表頭重複；拒絕靠縮到8pt塞成數十頁。

**8.2 原始點協會專屬而不造假**：來源表確實核實才稱「本會現有制度」。未驗證的人力、課程、授權、證照、設備、財務、志工職務全部列 REAL UNKNOWN；可另設 `SAMPLE` 小團隊角色安排（一位行政主辦、多職能可兼任，真正需利益迴避/核准者依現行授權查核），不發明專責人資、稽核、教研與資料管理部門。課程示範選合理社區服務/志工活動/訓練行政能力，不作任何醫療治療或療效承諾。

**8.3 不能只有空白**：有問卷空白答欄是**可供真人日後使用的工具**，可以保留；但同包必須有填好完整 SAMPLE 個案、答案、計算、異常處置、改善建議、追蹤、REAL 來源替換說明。第三方來函/就業證明/感謝函只有索取、未寄稿、核驗或來源索引可作完整示範，不能捏造「第三方已出具」的正式原件。

**8.4 低成本實用性檢查（模型只能作初步代理，真人測試不能冒稱完成）**：
1. 遮住文件標題與 doc_id，請另一 reviewer 從中間三頁識別其文類/用途，並說出與相鄰三個 checkbox 的不同。
2. 模擬沒有參與開發的志工行政：能否從首頁找到「如何開始、填哪張表、哪裡看已填例、出錯怎麼辦、誰確認、何時記錄」六個答案；每個必須指回具體節/表，不可只回答「詳見內部系統」。
3. **真正的國中生/非專業行政真人閱讀測試，沒有 Human 或受試者原始記錄前只能標 NOT_TESTED**；AI 自評 `易懂=PASS` 不等於真人驗收。
4. 紀錄至少一個具體錯誤案例與恢復做法，而不是只有成功流程；公式須列出分子分母、樣本數、N/A 規則、限制。
5. 20頁以上的制度/分析文件不自動 FAIL；但要求易找到核心人類操作區、完整版 SAMPLE 和 sidecar 追溯，避免用頁數／清冊列數替代專業品質。

**8.5 工程控制資訊分離**：`SHA-256 64位字串`、JSON、原始 FACT/queue/CLI、內部 Git 路徑、Raw PR 資料只放適當 sidecar，不要藏在正文/首頁。保留真正行政人員需要的「來源憑證索取」、「合法保存」、「資料整理」文字。正式表單所需審計識別可以用業務可讀的文件編號、版本日期，不顯露內部原料欄。

**8.6 異常回歸**：每件 Word 修改都檢查章節與讀取順序、字級、公式、SAMPLE 角色、時間前後邏輯、同意與簽署界線、跨頁表頭、孤立頁、所有文內路徑可用、清冊每原子值唯一鍵及頁定位；版本數很高的 0093/0095/0096/0098 不因修元資料就再重做全篇。

### S9｜GitHub 同步與真正讀回：不要只報 `git push exit 0`

**9.1 觸發**：一份穩定候選確定下來、Reviewer 有終態、明確重大錯誤/安全事故、Human Mission/Blueprint 重大新命令、來源更正，就在現有 PR #92 分支提交**最小必要公開差異**。純 PID 未變、每小時喚醒、同一份 Word 假改版本、相同收據複製不構成提交理由。只需要合法共同來源，不另建同步 DB。

**9.2 本地前狀態與競爭寫入**：用 `git fetch` 讀最新 remote HEAD；`git status --porcelain` 檢查無未授權差異；確認同一寫入範圍只有單一 owner。HEAD 前進後先比對新提交與本次要改的路徑；不要 force-push、不要覆蓋他人新完成的 0099。若共享寫入效果 UNKNOWN，只停止受影響 Git 推送，其他本機已授權施工可繼續。

**9.3 公開檔案界線**：只推必要可公開 DOCX、正式公開要求或授權摘錄、專屬 Blueprint、去識別 SAMPLE 清冊、QA 原文/經遮蔽的 CLI 回條、manifest、必要 PDF/代表頁；不得公開原始學員/會員個資、姓名電話、診療資訊、銀行資料、金鑰、未公開合約、未授權第三方原件或含聯絡方式的未審 raw stdout。先驗證「可公開」才 stage，絕不 `git add -A` 混入其他本機 WIP/暫存目錄。

**9.4 GitHub 與本機同一位元身分核對**（PS5.1 原生、只讀驗證範例；以下 `$repo/$file/$repoRelative` 必須以 S0 所確認的實際合法路徑替換，不能原樣盲執行）：

```powershell
$branch = 'work/ttqs-one-document-quality-contract-20261016'
$ref = 'refs/remotes/origin/' + $branch
# $repo 必須是現有核實的 repository worktree，例如 E:\TTQS\_github_sync_0064
# $file 是絕對候選 DOCX 本機路徑；$repoRelative 是同一份遠端 repo 相對路徑
if (-not (Test-Path -LiteralPath $file)) { throw 'LOCAL_FILE_NOT_FOUND' }
git -C $repo fetch origin $branch
if ($LASTEXITCODE -ne 0) { throw 'GITHUB_FETCH_FAILED' }
$remoteHead=(git -C $repo rev-parse $ref).Trim()
$localSHA=(Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant()
$localBlob=(git -C $repo hash-object --no-filters -- $file).Trim()
$remoteObject=(git -C $repo rev-parse "${ref}:$repoRelative").Trim()
if($localBlob -ne $remoteObject) { throw 'REMOTE_DOCX_RAW_BYTES_MISMATCH' }
"GITHUB_EXACT_BLOB_MATCH remote=$remoteHead blob=$localBlob localSHA256=$localSHA"
```

這是 raw Git blob 位元組對帳。需要獨立比對遠端 SHA-256 時，用現有 Python 對 `git show <remote-ref>:<path>` 的**位元組 stdout**做 `hashlib.sha256`，而不是在 PowerShell 5.1 用 `git show > file`（文字編碼重導可能改變 binary/JSONL）。保持已經驗證過的局部 `.gitattributes -text` 行為，不要為全部 repo 廣泛關閉換行正規化。

**9.5 同步結果才可寫**：`COMMIT_SHA`、`PR_HEAD_READBACK`、`DOCX_LOCAL_SHA`、`DOCX_GIT_BLOB_SHA`、`DOCX_REMOTE_BLOB_MATCH`、`DOCX_REMOTE_SHA256_WHEN_READ`、`REVIEW_RESPONSE_SHA`、`REVIEW_SCOPE`、`SAMPLE_ONLY`、`FORMAL_ACCEPTANCE=NOT_GRANTED`。不是每個文件都要將整份歷史附錄推送；引用原檔位置和 exact SHA 即可追溯。

### S10｜防呆反例：不新增一套驗收平台，只使用既有 native script/CI/收據

只需在**一次有界的 disposable 測試環境**驗證判斷器，不碰真實候選位元或改寫既有 PASS。不要為證明壞路由而真的連發3次模型。

| 反例 | 預期判定 | 不得發生 |
|---|---|---|
| 0096 R13 review packet 與回條分別填 R13/R12 SHA | `REVIEW_BINDING_CONFLICT` | 自動 `SEMANTIC_PASS_EXACT` |
| 0096 標 I18-E03 且「官方印刷流水號099」 | `SOURCE_IDENTITY_MISMATCH`，要求內部索引104 | 以 doc ID 0096 或 099 猜官方印刷號 |
| 0099 Blueprint 8×5×2 卻說160 | `BLUEPRINT_PREFLIGHT_FAIL` | 不核算就派全文 Writer |
| 0098 人類正文含未解釋 64位工程 SHA／不存在的清冊路徑 | `HUMAN_BODY_CONTRACT_FAIL`/`BAD_PATH`（Word 有證據才判 Word） | reviewer 用算術 PASS 覆蓋這個缺陷 |
| 0094 reviewer 只輸出26個未執行工具要求或403 | `NO_VERDICT/ROUTE_BLOCKED` | 繼續無變更同路由重試、或冒稱已審 |
| 0097 無 R07 PDF 只有 R06 視覺圖 | `VISUAL_UNKNOWN` | 冒稱 R07 全頁視覺 PASS |
| 兩個同SHA的 DOCX 副本、另一個不同資料夾的PNG | 只算同一候選、PNG不增加DOCX數 | 文件件數暴增 |
| cli exit 0 但回應空白，或 exit1 但有部分文字 | 分列 `NO_USABLE_ARTIFACT`/`PARTIAL_RECOVERABLE` | 單靠 exit 判完成／丟棄正文 |
| 只有 SAMPLE 完整且沒有 REAL 原件 | `CURRENT_CANDIDATE` | `FORMAL_ACCEPTED/REAL=YES` |
| 無新的 Git diff/新 SHA/新事故 | `L0_NO_MATERIAL_DELTA`、本次退出 | 每小時生成10MB報告或呼叫高階模型 |

### S11｜成本與品質同時驗收：避免「省 Token = 降低品質」

以既有 CLI native receipts、Git commit 與文件結果做**下一批10件**的改善比較，沒有完整帳務證據就保留 UNKNOWN，不假算新台幣。不要為監控新增 OSS、採樣守護程序或數據倉庫。

必須能按文件/attempt 讀到以下項目（缺來源就 UNKNOWN）：

1. `generated_unique_doc_ids`：不同官方需求且真正有 Word 的數量，不含 PDF/PNG/同 SHA 副本。
2. `candidate_exact_sha_count`、`revision_count`：同文件實際不同版本數，變更原因和缺陷是否收斂；不得只看提交數。
3. `independent_semantic_coverage`：FULL_TEXT、BOUND_DELTA、UNKNOWN 分開計，不以文字 reviewer 自填 SHA 替代 binary。
4. `visual_coverage`：全頁概覽、原尺寸審查頁、頁面像素繼承依據分開列。
5. `fix_first_pass`：一次限定修補後是否真的關閉具名 blocker；錯誤因由應分類（內容/公式/版面/路由/收據/權限）。
6. `cli_dispatch/useful_output/docx_built`：三種不同成功率，不把14/35文字回覆比例當 DOCX 完成率。
7. `input/output/reasoning/cache_usage`：依各 CLI 原生欄位存，不把可能重疊的 reasoning 欄與 output 相加猜總 bill；Codex GPT-6 用量沒有 readback 就 UNKNOWN。
8. `remote_sync_lag`：只對「穩定候選或審查終態」到相同 GitHub checkpoint 的時間計算；WIP 不要求秒級推送。
9. `human_operability`：國中程度/初任行政可讀性的代理檢查有章節定位，真人測試若沒有原件標 `NOT_TESTED`。
10. `public_data_boundary`：任何個資/第三方原件洩漏風險均需 prior privacy check；不能靠免費 Worker 繞安全界線。

**優先順序**：錯誤預防＞完整可用文件＞合格 QA＞節省 Token＞增加文件數/commit 數。已觀測的0096 review input=298,815、reasoning=229,438、cache read=915,328；0094 有91,352 input+1,168,092 cache read 卻無 verdict；0098 R08 reviewer 有78,455 input。下一批必須降低**重複無效上下文**，但不能把來源/完整 SAMPLE/負向鄰項這些真正有品質價值的證據全部砍掉。

### S12｜正式結案格式；無 material delta 不要長報告

每完成一件穩定候選或本輪具名 Finding，直接在現有 PR #92 提交短證據摘要，並由同一 GitHub readback。平時給 Human 不超過約15行（重大事故可例外），固定：

```text
PROJECT_ID=TTQS_ONE
SPEC=CANDIDATE Human 2026-10-16; CANONICAL=<fresh exact ref or UNKNOWN>
GITHUB_PR=92 ; HEAD_BEFORE=<SHA> ; HEAD_AFTER=<SHA or UNCHANGED>
ACTIVE_WRITER=<doc_id/worker/PID + OS evidence or NONE/UNKNOWN>
APPLIED_FINDINGS=<F01..F12: exact scope, proof, new SHA or unchanged>
0099_BLUEPRINT=<source-bound / 80-cell check PASS/FAIL / writer-ready>
REMOTE_DOCX=<doc_id/revision/local_sha/remote_blob/readback>
TECHNICAL=<PASS/PARTIAL/UNKNOWN + exact target>
VISUAL=<PASS_SCOPED/BLOCKED/UNKNOWN + pages and PDF SHA>
SEMANTIC=<PASS_WITH_SCOPE/PARTIAL/BLOCKED/UNKNOWN + reviewer input SHA>
SAMPLE_REAL=SAMPLE_ONLY; REAL_EVIDENCE=<PENDING/UNKNOWN>
FORMAL_ACCEPTANCE=NOT_GRANTED
OPEN_BLOCKERS=<exact doc_id / lane / reason>
READY_NEXT=<one exact permitted action per independent lane>
HUMAN_GATE=<only actual new identity/cost/rights/formal-real external effect, else NONE>
```

**R07 的真正驗收**：不是回一句「已看完附件」或「修正 PASS」，而是 Windows 原生 source/owner 已讀回、具名 F01–F12 有實際結果或精確 BLOCKED、成功修補的檔案具 exact SHA/必要 QA 並 GitHub 遠端驗證，以及其他 READY 文件持續合法施工。**沒有 Human 正式接受或 REAL 證據，不得升格。**

---

## E. 執行命令（貼給目前同一條 Windows Codex，附件只讀本 R07，不要重新餵14MB歷史報告）

```text
project_id=TTQS_ONE
COMMAND=TTQS_ONE_20261021_DEEP_AUDIT_SCOPED_RECOVERY_R07

你必須完整讀取這份 R07 一次，按 S0→S12 落實實際的原生施工、派工、精確審查、GitHub 同來源讀回。R07 是外部審核修復指示而不是已執行狀態；執行時以最新 Human Mission、PR #92 HEAD、各工作原始位元與真實 Windows PID 為準。

優先在現役與遠端核對後：
1. 0099 R02 has ALREADY fixed 160 to 80 on GitHub. DO NOT repair R01 again. Fresh-check the R02 source/blob and Windows active 0099 worker, and only dispatch one writer if not currently dispatched and actually READY.
2. 只查證與修正 0096 R13 審查 input/return 的 R13-R12 SHA 錯綁，保留原收據；修正 I18-E03 專案157索引應為104而不是099，勿假稱官方 PDF 有印流水號。不重建69頁 DOCX 除非 Word 正文真的需要局部修。
3. 直接檢查 0098 R08 實際 DOCX 是否含工程 SHA/錯路徑；有實體缺陷才定點修新版，否則只改 sidecar。不得重做已核實的數學與全篇 QA。
4. 分別處理 0094 R18 的真正免費模型審查（最新有成功紀錄的 Nemotron route 只可當候選，fresh verify），0097 R07 的 Word PDF 匯出與視覺，不因一車道阻擋另件。
5. 持續 0099 真正來源就緒的專屬 DOCX 生產；Antigravity 只允許 Gemini 3.8 Flash High 純文字 CLI；OpenCode v2 只用當時真正可用且不新增費用的免費路由。Codex 不自己長篇代寫、不使用 Computer Use/危險權限繞過、不瞎重試。
6. 每一實質成果採既有 Git/GitHub PR #92 提交及 exact blob/SHA readback；無變化只 L0 退出，不製作巨型日報、不新建 Supervisor、Task DB、監控匯流排或多個人工 Gate。

任務未真的執行不要自稱 PASS；不要因換 Session、未授權重試或 ACTIVE 排程卡片認定在背景施工。每階段遇 BLOCKED 僅停受影響 lane，主動移交其他 READY 工作。按 S12 的最短終態回報。
```

## F. 可信證據定位（閱讀順序，避免再輸入完整歷史）

- GitHub PR #92：`https://github.com/PT-Original-Point/ttqs-one/pull/92`
- Human Mission：`docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md`
- 寫作類型指南：`docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md`
- 157 專案施工索引：`docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`（099=I17D感謝函；104=I18感謝函；107=I18-E06；108=I18-E07）
- 最新外包命令沿革：`docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` §5；不要把該檔 0036 歷史起點當作本輪 READY。
- 0096 直接矛盾：`docs/ttqs-quality-20261016/quality-review/0096_R13_20261021/review/{review_input_manifest.json,return_receipt.json}`。
- 0098 最新 Word/側錄/QA：`docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/`；正文稿第49、443、444行、actual `evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`。
- 0099 CURRENT blueprint: `docs/ttqs-quality-20261016/quality-review/0099_R01/inputs/UNIQUE_BLUEPRINT_0099_R02.md`, observed Git blob `5ec600d4fe2bed76b448daf80382d39dacc5d93b`. Historical R01 remains audit history only.
- 0094 reviewer 真故障：`docs/ttqs-quality-20261016/quality-review/0094_R18/opencode_route_receipt.json`。
- 0097 Word 匯出阻擋：`docs/ttqs-quality-20261016/quality-review/0097_R01/R07/`。
- 官方《TTQS查核佐證文件資料表—訓練機構版》PDF p6–7：I17D、I18 的真核取需求；這份 PDF 有 checkbox 文字，沒有在每格旁印 099/104 的流水號。PDF 與專案自編 157 號必須分開。
- 4 個 Human 上傳歷史報告的原始 SHA/位元組在本檔 A 節；**只在定位歷史事故時以搜尋/範圍擷取，不重讀四份全文**。

**外部稽核已做：**GitHub 7 份 Word 二進位 SHA-256 獨立重算、相關 GitHub README/原始 QA 收據比對、官方 PDF p6–7 原文核對、附件四份逐位元組去重核對、0099 Blueprint 算術回歸檢查。**尚未做：**Windows 即時 OS 驗收、真實新 Worker 派工、GitHub 修復寫入、0098 最新 Word 實際內文逐字 extraction、真實國中生閱讀測試、協會正式接受；以上不可在 Codex 報告中偷填 PASS。
