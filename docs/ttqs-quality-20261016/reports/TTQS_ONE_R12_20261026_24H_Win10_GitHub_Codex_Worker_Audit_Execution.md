# TTQS ONE｜R12 施工總指揮書：10/26 24 小時雙 Worker、GitHub、Windows GOAL 與高品質 DOCX 閉環

**PROJECT_ID：TTQS_ONE**  
**COMMAND：TTQS_ONE_20261026_R12_FULL_RECOVERY_DELIVERY**  
**版本定位：Human 最新的可逆 CANDIDATE 施工指揮；不自動升格正式 canonical 或 HUMAN_ACCEPTED。**  
**正式庫：PT-Original-Point/ttqs-one；PR #92；分支 work/ttqs-one-document-quality-contract-20261016；每次執行 fresh-read，下面 SHA 只能作查核錨點。**  
**本機稽核區間：2026/10/25 22:05:07～10/26 22:05:07（Asia/Taipei）。**  
**報告原件：TTQS_ONE_最近24小時_Win10本機施工記錄_20261026_2205_TPE.md；SHA-256 68f72f3781da69be9507176d6b28b8d4b59c32a149b70a7fd48e2a5591824b3d。**  
**R12 GitHub 實時讀取錨點：HEAD 510d16faa15926e23ce62257541df23015a6290c；PR Open/Draft；最後 commit committer timestamp 2026/10/26 14:50:09 TPE。**  
**實施分界：本 R12 是施工指令與外部讀回，不能冒稱 Windows 已恢復 GOAL/排程、Worker 已啟動或 Human 正式核准。**

## 0. 命令權威與不可變品質界線

0.1 Human 最新明確命令 > 目前已接受 Mission/Spec > 相容政策 > 同專案受信任現況 > 舊 Chat、舊 R06～R11 歷史。只在 TTQS_ONE 施工，不讀寫 PTYSD Win11 控制面板或它的 Issue #407。若 R11 文字「已修復」與 Windows 10/26 22:05 的 PAUSED 實況矛盾，以各自觀測層級區分：R11 遠端規格已寫入，但 Windows 套用與自然觸發未通過。

0.2 官方 PDF 157 格＝129 個具名佐證與 28 個未命名「其他」；歷史 142 個 DOCX 是專案文件序號規劃，非官方具名需求數，也不是 142 份都通過。依 03_157_CHECKBOX_BLUEPRINTS.md、官方 9 頁 PDF、official_129_to_142_crosswalk.csv 逐條對應 1:N 拆件。**0142 是此舊 142 序列末號，不准自動建立 0143 冒充下一個官方方框。** 應重新盤點 0001～0142，每一件確實缺的是來源、Blueprint、完整 SAMPLE、Word、視覺、語意、遠端還是真實原件，選合法下一階段。28 個未命名 Other 維持等待命名，不能以填空新件灌水。

0.3 成品需是實際可開啟、人類易讀、文類特有的完整 DOCX。無真實協會資料時提供數學一致且完整填寫的 SAMPLE/SYNTHETIC 示例和替換清冊；不得偽造協會核准、第三方原件、醫療/個資、政府證明、簽章、付款或真實成效。Word 正文字級 ≥10.5pt、表格 ≥9.5pt；正文不塞 Git hash、JSON、執行器術語。不同 Reviewer 對「同一候選 SHA」做來源／文類／負向近鄰／可用性語意審查，Word 原生渲染及版面由獨立可核收據支持。TEXT_ONLY_PASS 不是 VISUAL_PASS，也不是 HUMAN_ACCEPTED。未核實欄位填 UNKNOWN，不得填 0 或 PASS。

0.4 人類允許已批准的可逆候選工程連續施工。不得新增第二套 Supervisor、Agent Bus、持久 Quota DB、監控自製服務、重複 Scheduled 或另一組 Writer 主控。對外未知寫入先同來源讀回，單一寫入 scope 不雙主；OS 秘密與 Windows sandbox=unelevated、Human 生產/費用/簽署/OAuth/MFA Gate 保留。不要為提高速度調高 Windows 管理員權限、使用 Computer Use 或 Antigravity dangerously-skip-permissions。

## 1. 已核實的 24 小時數字（先改掉錯誤口徑）

1.1 Human 本機報告可核：24h 修改 4 個 DOCX 位元檔，實際 3 個 doc_id（0100、0121、0122）；其中 0121 的 attempt01 為中間殘檔，不另計交付。11 個不同 doc_id 取得正向**有限範圍**候選語意結果（W2 10、W1 1）；0 Human FORMAL_ACCEPTED、0 REAL 升格。最後 DOCX 10/26 07:15，14h50m 無新 DOCX；最後 GitHub 提交 14:50，到報告截止 7h15m 無新 commit。這些是報告觀測，不推定此刻 Windows 仍沒有活動。

1.2 OpenCode v2：6 個 session＝4 件實際文件審查、2 個純路由探測；真正回收有效者僅 0133 一件（GLM-5.3-flash-free TEXT_ONLY_WITH_NONBLOCKING_FINDINGS）。其餘 HTTP 429 或沒有輸出。成功 0133 input=21,828、output=2,463、reasoning=12,224，session cost=0.0 非真實帳單確認。**OpenCode 服務 PID 不是 Writer PID。**

1.3 Antigravity CLI：14 個 attempt；10 個正向有限範圍結果、3 個失敗、0122 一個自報 PASS 但未完成可重現仲裁。至少 8 筆可見使用量合計 391,827 tokens，缺漏使總量與費用 UNKNOWN。絕大多數 W2 收據只有 requested/CLI reported gemini-3.8-flash-high，無 provider backend identity；實際 Gemini serving model 仍 UNKNOWN。0121 一筆 35,297 tokens 遭 RunCommand 權限拒絕而輸出空白，絕不能計成完成。

1.4 **本機報告「24h 13 筆 GitHub 提交」少算**：外部於同一 HEAD 以 REST commits?sha=branch&since=2026-10-25T14:05:07Z&until=2026-10-26T14:05:07Z 分頁重讀，找到 **61 筆不重複 commit SHA**，都是同 24h 的提交者時間；粗按 commit 標題分為約 32 筆收據/位元同步、20 筆審查、6 筆候選/修補、1 筆來源、2 筆其他。這是**committer timestamp**，不能冒充實際 push 事件時間。先修既有 24h 報表查詢起迄/分頁/UTC+08 的錯誤，不重跑 61 個工作。

1.5 PR #92 metadata 曾顯示 614 筆 PR 變更計數；GitHub PR commits API 可能僅回傳 250 筆，**不可用第 3 頁 50 筆就說專案全部歷史只有 250**。本次另外以 branch commit API 回看 700+ 筆歷史提交及 quality-review 現存目錄；本次深度抽查目前重要工件與收據，並非宣稱每份數千歷史工件的全文品質均已逐件驗證。今後採 PR 相關變更、目標工件、exact source 與 SHA 分層稽核。

1.6 **發現遺漏狀態投影**：0133 最新 GitHub 已有 OpenCode 成功 REVIEW_RESPONSE_R02、DISPATCH_RECEIPT.json（同候選 SHA 25116afb...），但最初 0133 README 仍說 independent review PENDING。不可只讀舊 README 就重新派審；應讀最新帶 exact SHA 的 terminal receipt 後以 sidecar 最小更正。0122 R02 的舊 candidate status 亦仍標 PENDING，但已存 Antigravity reviewer archive；必須先審證據鏈，不能直接自報 PASS，也不要直接丟棄。

## 2. 根因分級：確定、推論、未確認

**P0 確定**：Windows 10/26 22:05 兩條 Codex automation 設定都是 PAUSED；thread-bound 120m、standalone 60m 均未取得自然 trigger/next run 憑證；舊 OS Supervisor Disabled。沒有可核實啟用的 TTQS 自動續工，R11「Prompt 放寬」沒有保證控制執行層啟用。這是 7h～15h 停滯最重要的可驗證恢復優先項；**是否由人類、平台預算、thread 中斷或其他因素導致 PAUSED 仍 UNKNOWN**。

**P0 高相符但待現場驗證**：OpenAI 官方 Using Goals in Codex 說 Goals 是 thread state；要在活躍/idle/within budget 且無 queued work 才接續。Plan-only 不會續、沒有 tool call 的續工會被抑制、中斷可暫停。這可以合理解釋歷史「只寫 PRECHECK / NO_READY」自鎖，但不是本次 PAUSED 的既定根因。原生 /goal resume 在支援 Goals 的 Codex 版本中有官方文件；必須讀當機版版本與 UI command，若不可用不可無限循環嘗試，也不能編輯私有 Goal DB 或 /goal clear。

**P1 確定**：W1 免費 GLM/Nemotron 多次 HTTP 429；W1 DeepSeek/MiMo 路由探測 exit 1 零成果，不能每日無效輪試。0121 10/26 14:42 OpenCode 429 原始收據 retryAfterMs=62226000（約 17h17m）；依當次本機時間到期約 10/27 08:00 TPE，**以當前 provider 回應／帳戶配額為準，過期之前不做完全相同重試**。其他 route 429 時個別記 retry window，不能全體復活。

**P1 確定**：0121 Antigravity CLI RunCommand 被拒，輸出空白而 shell exit=0，且回報 35,297 tokens。禁止在純文字 REVIEW 中使模型執行檔案／終端／權限工具；用只有必要正文文字的 stdin packet、無需 file tool 的請求。任何 denied tool call、輸出空白、只思考無終態 = FAIL_OR_PARTIAL，不能採用。

**P1 確定**：0122 Word COM 匯出 wrapper exit=1 但確有 28 頁 PDF，當時觀察 52 個 WINWORD.EXE。這是「包裝器狀態與產物」不一致；52 個 PID **不等於 52 個活躍 Word Writer，也不表示可全部殺除**。只對該 renderer/PID/進程父子/產物做有界調查；DOCX 同 SHA 不需重建。

**P1 確定**：OpenCode 有互動 TUI/黑色視窗事件，兩次無模型 preflight exit124；現有 root cause 只指向某個 CLI 啟動方式，尚未證明確切 PID/Automation 因果。修復時用無模型 --help / run --help 及本機現成成功腳本對照；非互動、stdin 已關閉、stdout/stderr 轉檔、CreateNoWindow；先受限測試，再開實質模型。MainWindowHandle=0 或缺值不是全面停止理由。

**P1 推論待驗**：W1/W2 主要做 Reviewer，而非出完整可採用 Writer 稿；大量審查與反覆同步沒有轉成相稱新 Word。應把確定性測試/已通過 SHA 先回收，按真正需要派一次合格短 Writer/Reviewer；不要再用巨型 prompt 重審同一版。

**P2 確定**：Windows 曾找不到 TTQS 專用面板，8765/8766 無 LISTEN，READBACK 快照停在 10/23；PANEL_ALIGNED=UNKNOWN/STALE。監控面板既非任務權威也非施工 Gate，不能為修面板而停 DOCX。另一個 PTYSD Win11 Issue407 的 operator-panel 不屬 TTQS ONE。

## 3. S0｜一次性唯讀現場恢復，不以歷史快照宣稱 LIVE

**起點**：在目前 Windows 10 真正持有 E:\TTQS 寫入權限的 Codex Session 執行。每次新 Session 僅有界讀，別重新讀 700 commits 全文、超過 10MB 日報或整個 E:\TTQS。實際需先核對 HOST/USER，若與原本 J 帳戶不同就不使用其 session、token 或 PID。

~~~powershell
$ErrorActionPreference = 'Stop'
$now = Get-Date
"OBSERVED_LOCAL=$($now.ToString('o'))"
"HOST=$env:COMPUTERNAME"
whoami
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption,Version,BuildNumber,LastBootUpTime
$paths = @(
  'E:\TTQS',
  'E:\TTQS\TTQS_ONE_CODEX_RUNTIME',
  'C:\Users\J\.codex\automations\ttqs-one-hourly-quality-goal-resume\automation.toml',
  'C:\Users\J\.codex\automations\ttqs-one-standalone-quality-resume\automation.toml'
)
foreach ($p in $paths) {
  [pscustomobject]@{ Path=$p; Exists=(Test-Path -LiteralPath $p) }
}
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -match '^(Codex|opencode-cli|agy|WINWORD|python|powershell|pwsh|node)\.exe$' } |
  Select-Object ProcessId,ParentProcessId,CreationDate,Name,CommandLine |
  Format-List
Get-ScheduledTask -ErrorAction SilentlyContinue |
  Where-Object { $_.TaskName -match 'TTQS|Codex' } |
  Select-Object TaskName,TaskPath,State,Triggers,Actions,Principal
Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object { $_.LocalPort -in 8765,8766 } |
  Select-Object LocalAddress,LocalPort,OwningProcess
~~~

**資安**：上述 command line／排程 Action 若含 token、cookie、private path、學員真個資，只於本機診斷，輸出公開 GitHub 前遮罩；不能上傳使用者本機完整環境變數。取 PID 只代表程序存在，還需 work_id+session_id+source SHA+last tool activity 才能標 ACTIVE_WRITER。時間超出相同觀察窗口要寫 STALE。

**完成條件**：一張短的 OS 事實表，含 OBSERVED_AT, HOST, USER, real worktree, actual CLI versions, active work_id, unknown pending external effects, scheduler native IDs/status。若 Git/GitHub remote 已有某工件，先依相同 repo/branch/bytes readback，不盲重送。

## 4. S1｜先處理真正的 GOAL／Scheduled 暫停，不能只改 GitHub Prompt

4.1 目前歷史現況：thread-bound 120m TOML SHA-256 628e8b463ea2d489342a68342a8116f66ed248768c31b0dd42de328dfe336977、state=PAUSED；standalone 60m SHA 443313876c25cd73baffd515fcd3bc6d1ef24acf4a7e6e49b835de98aa87df6、state=PAUSED；OS Supervisor Disabled。S0 時先讀**現在原生 Codex Automation 管理頁面**，精確確認同一 task ID、thread ID、enabled/paused、120m、last/next、effective prompt、最近三次 invocation、執行工作區可否讀 E:\TTQS。不要透過私有 TOML 改值聲稱 native 已套用。

4.2 在原 Codex thread 透過原生命令顯示 /goal 狀態，查到其 version、pause reason、budget remaining、最近兩次 continuation 是否有 tool call、是否 pending user input/approval 或已達限額。**官方 Codex Cookbook 提供 /goal pause、/goal resume、/goal clear（支援版本起點為 0.128.0）**，但不能保證 Windows 此版本、此介面皆暴露相同 command；原生可用才依目前 Human 續工授權執行 resume。沒有命令時，不使用 /goal clear，不改私人 DB；以現有有權執行的 local Codex thread/CLI 繼續可逆工作，同時回報 GOAL UI 仍 PAUSED 的局部落差。不要靠回覆「GOAL ACTIVE」代替本機工具增量。

4.3 唯一排程：先確認原 thread-bound 120m 的本機存取能力和 last-run。若能真正讀本機、派既有合格 CLI 並有原生收據，**只恢復這條**，保存完整 native task 設定與前後狀態；不啟動仍 PAUSED 的 standalone，也不啟動 Disabled Supervisor。若 thread-bound 本質只能送訊息而不能接觸 E:\TTQS，先確認原有 standalone 在合法本機 project context 的 native parity（同一 source/owner/無未結效果），再遵照「先停舊＋讀回停用→只啟新」的單主切換；沒有 parity 不宣稱已修復 24/7。

4.4 每兩小時只是 watchdog / crash 補漏，**不是完成一個 stage 後必須等待下次喚醒**。有合法 READY、有 tool access、無同 scope 活躍 Writer，就立即執行下一個階段。定時事件如僅送出文字，記 CONFIG_PASS / DELIVERY_PASS / WORK_RESUME_FAIL，不叫 AUTO_RESUME_PASS。每次到點若只是計畫、沒有 tool call，依官方 Goal 防空轉設計可能不再自動續，故必須立即檢查現役 owner 和合法 READY，不能再次空轉 NO_READY。

4.5 在 S0～S3 沒恢復之前可以繼續**同一當下已授權有權操作的 Codex session**的可逆文件施工；不能因排程/面板 Gate 問題把文件全部停止。只有涉及工作程序真的無法執行/費用/人類外部授權時才局部封鎖。

4.6 驗收區分：NATIVE_TASK_ENABLED、INTERVAL_120M、NATIVE_LAST_RUN、NATIVE_NEXT_RUN、MANUAL_INVOKE、NATURAL_TIMED_TRIGGER、RESUMED_MATERIAL_WORK、GITHUB_BYTE_READBACK。手動 Run-now 只能測能力，**不是**自然到點驗收；若需要跨時間自然觸發才有證據，必須保留 NOT_YET_OBSERVED 而不是想像 PASS。

## 5. S2｜精確回收已存在成果，避免一份 Word 一直重做

**優先序：現成原生收據驗證與狀態投影修補 → 本地確定性計算／最小 DOCX 修改 → 真正缺少才派 AI Writer/Reviewer。**

**0100 / I18-E08 / R09b**：GitHub 10/26 新 DOCX SHA 0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c，技術/視覺與 W2 delta semantic 收據存在，且 remote readback。舊 R10 的 SHA 1563... 是歷史另一版，**不可錯把舊 R10 的 PASS 直接套在 R09b**。先核 R09b 的 inherited baseline scope 及增量是否涵蓋所有 changed body/表格/F1–F4，符合即保留；不要為純側錄、README 改版重建。

**0121 / I19-E09 / R02（P0 審查缺口）**：DOCX SHA ae5da09e834f5a8e9097a85ac87d4fe2f76acf9626049d3b0bea7c5f35042efe，23頁、27項技術/視覺 PASS、remote 19 個檔案原始位元組已核對（本機摘要另引用 7/7 新增審查封包，兩種計數的**清單範圍不同**），語意 PENDING。OpenCode GLM 10/26 14:42:52 的 429 retryAfterMs=62226000、no reviewer output、candidate unchanged。此時**不得重建 DOCX、不得同輸入/同路由立即重試、不得無授權付費 fallback**。先從 R01 6項 partial finding、R02 差異、原先 official source+Blueprint、R02 full extract 建獨立短 reviewer packet；真正有合法替代 free W1 route 或 W2 text-only reviewer 且可證實無未結 attempt 才派一輪；若都不可用標 REVIEW_LANE_BLOCKED_UNTIL_ROUTE_READY，並行其他 READY 文稿／QA。W2 0121 歷史 RunCommand denied 的原 prompt 不得照抄。

**0122 / I19-E10 / R02（P0 零 Token 先救回）**：DOCX SHA d3a6a1222d0389172dc6ab9737d06c5e46f4b45ed3a661324f3b885b751b7b86；28頁、3行分隔線及2符號局部修復、技術/視覺同 SHA，GitHub readback。現有 ANTIGRAVITY_R02_SEMANTIC_REVIEW_ARCHIVE.md 保存 W2 original review 及原始輸出 hash，自報文字範圍 PASS，並明示 packet-asserted-only SHA；本機尚缺可重現的獨立仲裁收據。**第一個動作不是再派 W2**，而是用原本唯一 exact DOCX 位元組本機重算 SHA→重抽全部文字→重算 reviewer 所見 extracted text hash 81d144264640265ec015d412bdb08f3e74578b001b7621e7d4462863fb1a1e33→查原始 review prompt 的實際封包內容/順序/來源/抽取範圍與真實 stdout hash e5857259…、回覆 040c302a…→查 reviewer 確實是不同於 Writer 的上下文、有針對 I19-E10 的逐題計算/負向鄰項定位、沒有偷改來源/正文。全部符合則最小新增**限定 TEXT_SEMANTIC_SCOPE 的本機獨立仲裁**，與既有 Word-native VISUAL 同 SHA 合併為 CANDIDATE QA，不得稱 W2 曾直接開 DOCX 或 backend Gemini 已證實；若抽取值對不上，準確定位，不能靠補寫 metadata 自行把它改成 PASS。只有證據不足且合格路由已可用，才做一次小封包新審。

**0133 / I19-E22 / R01**：原始 README 仍說 independent review PENDING，但 GitHub 已有 OPENCODE_GLM_SEMANTIC_R02_20261026T0805 的 session/native 成功收據，reviewer body SHA 437a43e31542249f093f9f68e8e8777d9e92939f75305fa74ace0bb2f4f62d1f，candidate exact SHA 25116afb8206e0828c8b3a4a763845a9c3e672a4cb49969a64a2a3737d87256b，獨立 TEXT_ONLY_WITH_NONBLOCKING_FINDINGS。先核實真出於同候選且沒有新的修改、技術及11頁視覺同 SHA，再只更新 README/狀態側錄，保留舊 receipt，**不重建 DOCX、不重派 review**。

**0135 / I19-E25 / R01**：有10頁可開啟完整 SAMPLE DOCX（SHA cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da），OpenCode DeepSeek 原審查 429，exact SHA 語意 PENDING。來源/文稿/替換清冊和 55/55 GitHub readback 已在；只待一個合法獨立 reviewer 路由，不重建 Word。若 W1 額度仍擋、W2 審查可以純文字、不能使用 file/shell tool，則限制 scope 派單一審查，不冒稱 Gemini backend 已驗證。

**0130、0131、0132、0134、0136、0138、0140、0141、0142**：依本期記錄已有 scope 限定語意/QA/遠端；按 exact SHA+原始 terminal receipt+所審範圍逐件補投影/必要短缺即可。特別 0134 R01 無回覆後 R02 已在同 SHA 回收 PASS，**不需 R03 重派**；0138 有 140段/21表/149列同 SHA 審查及15頁視覺，同 SHA 時不要每次再花 69,550 tokens；0138 16檔中的文字 sidecar 是 normalized text equality，不能聲稱全部 16/16 raw bytes 一致。若未有真正形式 HUMAN ACCEPTED，維持 CANDIDATE。

**0137、0139、0140、0141、0142 及更舊需求**：必須從正式 142 crosswalk、現有 quality-review/README/候選/QA 精確導出尚缺 stage；不要只因文件名稱出現就算正式完成。若新稿寫作可 READY，優先選來源、Blueprint、完整合成事實皆穩定且尚無活躍 Writer 的合法 item；模型 reviewer 429 不擋獨立 Writer/來源/技術 stage。禁止生成未具名 Other 或假造 0143。

## 6. S3｜雙外包 Worker 的派工前防呆

**W1 OpenCode v2 CLI**：實際 CLI 有 2.1.4 版收據，成功 0133 的 OpenCode GLM session 作已知成功參考。Windows 現場重新確認當前安裝版本/路徑，不照抄 2.0.32 舊用法。先用無模型 --version、run --help、models 讀路由；單看模型目錄有列、名稱含 free 並不代表可用或完全免費。對每個 429 僅記 exact provider route、retryAfter、帳戶窗口、原始 stdout/stderr，不連續探測五種免費模型。相同 429 沒到重新可用窗口不派同輸入；不存在可授權免費路由時，W1 該路由明確 BLOCKED，而非全專案停工。

**W2 Antigravity CLI**：歷史當前 v1.4.7；僅 request gemini-3.8-flash-high。使用獨立小文字封包，由 stdin/--print 的當前 --help 支援參數輸入；**純文字模式禁止 RunCommand、讀寫檔案工具、Computer Use、授權繞過、模型 silent fallback**。尤其 0121 35k tokens/0 採用的受拒工具呼叫，應在本機對 actual prompt/CLI mode 做 diff，移除工具指示和無關整個 repo 背景，不能以全域授權解決。真 provider-serving model/Google 額度不知道就 UNKNOWN；即便 CLI 自報 Gemini，也不等於供應端身分已核。

**派工者 Codex 的工作契約**：每一個小工作物包含 doc_id、requirement_id、source locator+hash、unique Blueprint hash、同一 CASE facts、SAMPLE replacement register locator、近鄰反例、稿件角色 WRITER/REVIEWER、輸入完整性 SHA、允許輸出的章節/修補差異、停止條件與成本警戒。沒有這些欄位，不叫模型幫忙「自己找」。工作物分割以一張問卷、一個分析表、一個決策流程、一組跨文件算式為適當單位；全文一次輸出曾觸發截斷，優先 3～5 個可獨立回收段落/表格，再原生 deterministic 組裝同一 Word，**不得把不同段落接縫當已通過**。

**同一 Writer 不能審自己**。W1 或 W2 外包 Writer 有輸出且實際採用才計 WRITER_DELIVERABLE；Codex 若因外包路由失敗而從官方來源代寫，明確標 CODEX_FALLBACK_WRITER、成本/原因，之後依既有驗收聘請不同語意審查上下文。不能因 Writer 免費路由 429 而永遠不做可以確定性生成的表單/公式或進度準備。

**必要精確結果回收**：work_id、doc_id、attempt_id、PID、CLI version、requested model、native actual model 或 UNKNOWN、stdout/stderr raw hash+bytes、exit+timeout、tool_denied、completion?、是否完整、是否採用、採用到哪個文件、結果 SHA、上下文角色、input/output/reasoning/cache Token 或 UNKNOWN、計費或 UNKNOWN、next exact action。Shell exit0 但工具拒絕、回覆空白、只有 JSON wrappers、半篇截斷者一律 FAIL/INCOMPLETE；先 salvaging 具有可驗證內容的段落，不重啟同一大 request。

**時間與成本停止規則**：同一原始錯誤未有 material input/tool/config 變化，不再重試。同一路由依既有 Human「連續三次錯誤且三次有界修正仍失敗」停止派工，只影響該 route；更早遇安全拒絕/FreeUsageLimit 直接依真實釋放條件暫停，不湊滿三次。單一審查輸入超過 40k tokens 時先檢查是否真的需要全文、是否已有 baseline PASS 與 text-diff；這是優化提醒，不是會阻擋必要全文驗收的新 Hard Gate。

## 7. S4｜CLI 視窗、Windows 執行與超時處理

7.1 先在**當前真正 CLI.exe** 以 --version、--help、run --help 做無模型測試，從官方工具返回成功程式參數再構造派工；**絕對禁止直接呼叫不帶 subcommand 的 opencode-cli.exe** 當作寫稿命令，那可能直接啟動互動 TUI。原有 10/26 preflight exit124/控制碼為失敗證據，不能當成功引數模板。

7.2 Windows 子程序使用 native noninteractive launcher：UseShellExecute=false、CreateNoWindow=true、RedirectStandardInput/Output/Error=true，向 stdin 寫入完整封包後關閉輸入，並非互動；stdout/stderr 必須持續異步清空或導到不同檔案，避免管線塞死。只用每個已安裝 CLI 的當版 --help 確認 argv 和 timeout unit，不猜舊 --print 位置、--print-timeout 單位。每個 PID、父子程序、last write、elapsed 與 session_id 要同 work_id 連上。若真正出現前景黑窗，先辨認 exact PID/父程序再修這一種啟動路線，不 Kill 全部 OpenCode service，也不因 MainWindowHandle 缺失全面停派。

7.3 不使用無界 timeout。timeout 是**一次 attempt 的安全邊界**，不是 GOAL 工作節流；命中 timeout 前須先評估部分穩定產物是否可採用。若已產生完整 Word/PDF，wrapper exit != 0 只能標 WRAPPER_FAILED_ARTIFACT_PRESENT 待查，先以本機 zip/hash/頁數/圖像 QA 檢查；不得把正常產物砍掉重建。若要終止，鎖定該 work_id 的精確子程序樹、保留最小 stdout/stderr，不能對 52 個 WINWORD.EXE 一次性全部 kill。

7.4 Word COM 專用：原生執行前檢查同檔 Word owner／孤兒 renderer、目前 Word 使用者互動實例；用獨立受信工作目錄和短生命週期 COM 實例，確保文件 Close、Application Quit、釋放 COM 參考；只有經 PID/parent/時間/文件所有權確認**本工作建立**的殘留程序才可處置。計算 Python docx zip、Word export PDF hash、頁數、最終每頁 PNG/全頁視覺，再把 Exit/Artifact/ProcessClear 三欄分別回報。不可只因 exit 1 判產品壞掉，更不可只因 PDF 存在判一切 PASS。

## 8. S5｜正式文件品質與不重做的判定演算法

每份文件選**一個穩定候選 SHA**，先找最新來源/Blueprint、同 SHA deterministic/visual/semantic scope 與 REAL 限制；按照下列次序：
A. 字面配對錯／README PENDING 而有同 SHA 終態 → 只修 sidecar/README，DOCX 不動。
B. Reviewer 原始輸出已有 PASS 但缺仲裁 → 零模型驗證原始 stdout、輸入封包/body/候選 hash、角色獨立、來源定位；能證實就限定範圍結案，否則定位最小缺漏。
C. 真版面錯／字級不足但文本沒錯 → Word deterministic 最小 repair，**新 DOCX SHA 必須重核影響的視覺及語意 delta**，舊版 PASS 保留歷史不得跨 SHA 拼。
D. 內容有錯、公式/分母錯／近鄰誤用 → 先 Python 重算與 source facts diff，必要才短包 Writer，然後 different reviewer 對新 SHA 審。
E. 外部真實來源不存在 → 完整 SAMPLE 可交付，正式 REAL 與政府 TTQS 送審不得假升格。
F. 既有同 SHA、同範圍全 PASS → 鎖此範圍，下一個 READY，不因最新 GitHub control commit/README 微調重審。

最低驗收：官方 requirement、genre 專屬性、真 SAMPLE 完整可用、清楚真實限制、所有數值重算、字級、Word 全頁無溢出/孤頁、必要獨立語意、封包 SHA、遠端 bytes。Human 對實際可讀/可操作的品質最終仍有抽查權；不能讓 AI 自評代替。

## 9. S6｜GitHub 最小推送與 24h 全窗統計

9.1 E:\TTQS 根本不是 Git checkout；先定位現役受信 clone，驗證 remote origin 精確為 PT-Original-Point/ttqs-one，branch 為 work/ttqs-one-document-quality-contract-20261016。禁止直接在 E:\TTQS 根目錄執行 git log 就認定沒有 repo；也禁止為解決分散問題再建第二個 project DB。使用既有唯一 Git clone/working tree 和已知正式 PR，不從舊 clone 亂 force push。

9.2 **減少 GitHub 提交顆粒過細**：10/25～10/26 同窗 61 commit 中，按標題粗分約 32 個屬證據/同步、20 個審查、6 個候選/修補。0134 曾把數個 review sidecar 一檔一 commit 再逐個正規化，浪費時間和回讀成本。每個已穩定獨立文件 scope 優先一次檢查完整 package/manifest/QA 與必要原始 Worker 收據後做**一個**有界原子 commit；必須遠端回讀再追加必要的 receipt commit（若既有流程要求）。不要每張縮圖、一頁 PNG、一個 receipt 都推一次。不同 worker 未結／未知 push 時不得合批造成不明覆蓋，必要才細分。

9.3 公開 repo 只保留公開必要來源、去識別 SAMPLE、完整 Word、必要精確 worker/QA 收據及最小可重現工具；不要上傳完整登入憑證、Google/OAuth session、個資、自由格式模型隱藏推理。文稿正文不含巨型工程收據。對 DOCX/PDF 查 raw SHA-256，對 JSON/MD/TXT 区分 BYTE_EXACT vs TEXT_NORMALIZED_EQUIVALENT；不同換行/BOM 不可宣稱 raw bytes 完全一致。使用 Git SHA-1 與檔案 SHA-256 分別陳述，不相互代替。

9.4 24h GitHub 實算 PowerShell/Codex 原生步驟：時間區間一律台灣 ISO offset-aware，換成 UTC；針對具名 branch REST commits 並明確傳 since/ until /per_page/page，逐頁直到無資料、去重 commit SHA，保留 query/utc 起迄/head 與回覆數；不要被 PR commits 250 結果上限截斷，或把提交時間當推送時間。另按 commit file changes 求實際 DOCX SHA、doc_id、review/metadata/binary 數，不用 61 commit=61 文件。只有最近 Human 指定的 24h 需要此報告，**每次兩小時正常續工不重跑完整 24h 長報告**。

9.5 每件內容上傳需新鮮 remote head、相同 path 該 branch raw blob、local raw sha、未知 side effects 先讀回；完成後回讀全部真正需覆蓋的工件清單及 SHA，再發布簡短更新。GitHub PR Open/Draft ≠ MAIN merged ≠ REAL/HUMAN正式接受。

## 10. S7｜監控面板與資料來源，不得因找不到阻擋 Writer

10.1 Windows 10/26 報告：8765/8766 無 LISTEN；本機快照截至 10/23；沒找到可確認的 TTQS 現役 dashboard。先查**使用者實際打開的 URL、捷徑 Target、服務 PID/Port、資料來源、Project ID、source HEAD/observed_at/expires_at**；不能拿 PTYSD Win11 operator-panel 當 TTQS 的 panel，也不能用單個舊 JSON 冒稱 LIVE。

10.2 如果真正現役 TTQS panel 不存在，寫 PANEL_NOT_FOUND_ON_TESTED_PATHS；維持最小原生 GitHub + PowerShell 即時對帳，不新增第二個 dashboard service 或 Supervisor 去畫漂亮燈號。沒有 panel **不是**來源/Word/Reviewer 的 READY Gate。

10.3 若找得到現有面板，只修真正引用的既有讀取路徑，更新同時點 project/host/branch/head/work_id/owner/doc SHA/QA/observedAt/lastHeartbeat，不上傳隱私；按同來源 fresh snapshot 與遠端 bytes 覆核，才可叫 PANEL_ALIGNED。沒有 OS live 觀測就是 UNKNOWN。

## 11. S8｜R11 自造鎖淨刪的現場鑑別

11.1 已知 GitHub R11 在 AGENTS.md／04／05 中刪除固定 1 BUILD＋1 REVIEW、每 scheduling turn 只一次及要求不存活的 resume 前置。**但 Windows 10/26 22:05 原生設定兩條 PAUSED，且未證明本機現役所有 control consumer 已讀 R11。** 必須逐個檢查當前 Codex effective prompt、真正使用的 AGENTS、本機 runtime consumer、owner 及 disabled Supervisor；若舊 AUTONOMY_POLICY.md 沒現役 reader 就保留 HISTORICAL，不去修改過期程式碼假裝解鎖成功。

11.2 KEEP：單一 scope Writer、最小本機 OS 權限、必要獨立 QA、SAMPLE/REAL/正式核准、未知 side effect readback、CLI 無 Computer Use、模型無無聲 fallback。REMOVE/NARROW：非必要的一階段一喚醒冷卻、固定僅兩個不相關工作、舊 Canary 重啟門檻、黑窗觀測未知全停、OS Task Scheduler 名稱當 READY、Model 429 扩大成整案停工。

11.3 真正受使用者授權的活動工作可以當次持續，不因原生排程暫停而等 120m；但不能承諾在 Codex App 關閉/會話中斷之後仍有 24/7 實際續工，除非原生 scheduled active、last/next/自然事件及可取 local work 的證據都已驗證。不可新增偽心跳／第二控制面來填缺口。

## 12. S9｜驗收測試矩陣：不必再消耗模型演示已知錯誤

T01 時區與 UTC：依相同 24h REST 找 61 筆，不是本機 13；若未同數，找出分頁/時間條件差異，不能改報表數字掩飾。
T02 0133 已有 native GLM reviewer exact-SHA PASS 而 README pending → 只修 metadata，DOCX hash 不變。
T03 0122 W2 review packet SHA 在 Word/body/原始回覆之間不吻合 → 不給語意 PASS；吻合則不重派全篇。
T04 0121 與 0135 同路由 429 → 指定 lane 暫停、不重試、不停其他來源/Writer。
T05 W2 0121 exit0、tool denied、空回覆 → FAIL，35,297 tokens 不計 useful review。
T06 W2 requested Gemini、backend identity UNKNOWN → 不能報 Gemini serving已驗證／配額扣除。
T07 OpenCode service alive 沒 work_id / session 進展 → NOT_ACTIVE_WRITER。
T08 52 WINWORD PID owner 未知 → 不得 52 個全 kill。
T09 Word wrapper exit1＋穩定28頁 PDF/相同 SHA → SALVAGE_RENDER_SCOPE，不重建 DOCX。
T10 0138 DOCX/PDF exact；部分 sidecar 只 normalize equality → 不給 16/16 raw exact。
T11 GitHub 61 commits 但只有3 doc_id 的 Word 本期改動 → 不以 commit 當文件數。
T12 兩條 automation PAUSED → NATIVE_RESUME 不得 PASS；只修改 GitHub Prompt 不等於已套用。
T13 120m configured/人工 Run-now ≠ 自然觸發；真的 scheduled event 要有 task id、scheduledAt、native receipt。
T14 前一 GOAL turn 無 tool call/Plan-only → 不應以自動下一輪一定會發生假設 PASS。
T15 同 doc_id 同 SHA Reviewer 結案 → 不再為 status 改動全文重建。
T16 同 doc/revision 有實際活躍 Writer → 不能新派第二 Writer；不同 READY 可按資源平行。
T17 Word 正文空問卷／假簽名／無來源三年保存期限 → FAIL，不能以大模型 PASS 掩蓋。
T18 128/129等新錯字 / INTERNAL_INDEX 誤當官方 serial → official requirement exact mapping FAIL。
T19 GitHub branch HEAD 新、Windows/Panel 舊 → STALE 與 REMOTE_STABLE_BEHIND_ACTIVE_WORK 分開。
T20 Unresolved GitHub push result → same-source readback before retry。
T21 0142 後自動新建 0143 作官方方框 → FAIL，應從 142 crosswalk 重算缺件。
T22 0 TRUE READY / 但來源 packet 可建 → READY_SOURCE_PACKET，不自行 PAUSE 全案。
T23 Reviewer TEXT_ONLY_PASS＋同 SHA Word visual PASS → 可形成不同 scope 互補收據，不能宣稱 Reviewer 看過版面。
T24 同步事件有 61 commits/多個 receipt，但無人類 REAL 或 Human Acceptance → REMAINS_CANDIDATE。

每項測試使用歷史原生收據或少量可逆 deterministic fixture；**不要重新送模型 429、RunCommand denied、TUI crash 或未授權權限以「測試」**。有 FAIL 必須指出哪個既有讀取/程式碼／原生設定、實際最小 patch、retest 與是否波及其他 lane。

## 13. S10｜下個同一 Session 的實際施工順序，不要再停在活動報告

A. **立即**：S0 OS 現場／原生 Automation PAUSED 真因和現役 work，確定不存在某個活躍 Writer 被重啟風險；同時 S1 取 GitHub 最新 HEAD。此為一次性 bounded read，不可因 GOAL PAUSED 就停止已被 Human 授權的本機可逆工作。
B. **無模型快修**：先審 0122 原始 reviewer input/response/extract SHA，能閉環就輸出 scope exact 判定；再修 0133 stale README/sidecar。穩定候選不得重建。
C. **查真阻擋**：0121 的 GLM 免費路由明確 429 至 provider 窗口；0135 同類；使用一條可用、獨立、純文字、不新增費用的合法 W2 或重新驗證後的 W1 來補語意；沒有可用路由只 park 該 REVIEW lane，下一 READY 照作。
D. **落地生產**：依 142 crosswalk 搜尚缺 SOURCE/BLUEPRINT/COMPLETE_SAMPLE/Word/QA 的文類，先做確定性來源事實與完整合成案例，真正合法且來源就緒時派合格 W1/W2 小包 Writer。沒有 CLI Writer 可用時允許 Codex 依已確認 Human 源事實完成必要候選稿，標 CODEx_FALLBACK_WRITER，必須不同 reviewer 後續把關；不能用空白表灌量。
E. **最小發布**：以功能範圍分組保存必要完整候選/QA/原始 Worker receipts，一次最小 GitHub push，再同源 raw-byte readback。只在真正 material delta 發生時短報告。
F. **不停在單輪**：上一個 stage 完成並有終態就立刻選下一 READY，不等兩小時。沒有 READY_DOCX 時至少查 READY_SOURCE_PACKET/BLUEPRINT 或 READY_SCOPED_QA；不得回覆「暫無 READY」後關閉 GOAL。
G. **事後對齊**：原生 120m 唯一 scheduled task 的 enabled+last/next+natural trigger 與本機 E:\TTQS 存取實證；panel 如找不到只 UNKNOWN，不是交付 Gate。

## 14. S11｜每次真正成果回收時需要的最小格式

~~~text
PROJECT_ID=TTQS_ONE
COMMAND=TTQS_ONE_20261026_R12_FULL_RECOVERY_DELIVERY
OBSERVED_AT_TPE=<native host time>
REPO=PT-Original-Point/ttqs-one
PR=92
REMOTE_HEAD_AT_START=<fresh SHA>
REMOTE_HEAD_AFTER=<fresh SHA or NOT_PUSHED>
WIN10_HOST_AND_USER=<native verified>
GOAL_NATIVE_STATUS_AND_REASON=<active/paused/budget/unknown>
SCHEDULE_ID_MODE_INTERVAL=<native readback or UNKNOWN>
NATURAL_TRIGGER_AND_INVOCATION=<PASS/NOT_YET_OBSERVED/UNKNOWN>
REAL_WORKER_OWNER_AND_ATTEMPT=<pid/session/work_id or NONE/UNKNOWN>
W1_ROUTE=<healthy/429 until.../unavailable/UNKNOWN>
W2_ROUTE=<healthy_scope/tool_denied/identity_unknown/UNKNOWN>
DOC_ID_REQUIREMENT=<exact ID/code>
SOURCE_AND_BLUEPRINT_SHA=<exact/UNKNOWN>
CANDIDATE_DOCX_SHA256=<exact/UNCHANGED/NONE>
SEMANTIC_SCOPE=<TEXT_FULL/TEXT_DELTA/PENDING/PARTIAL>
VISUAL_SCOPE=<PAGES+SHA/PENDING>
SAMPLE_REGISTER=<exact SHA/NONE>
GITHUB_RAW_BYTES=<PASS with count/UNKNOWN/NOT_PUSHED>
HUMAN_FORMAL_ACCEPTANCE=NOT_GRANTED
REAL_EVIDENCE=NOT_VERIFIED
MATERIAL_DELTA=<specific fact, not plan or status alone>
BLOCKED_SCOPE=<specific route/file/permission>
UNRESOLVED_EXTERNAL_EFFECTS=<specific or NONE_CONFIRMED>
NEXT_READY_STAGE=<one precise stage>
~~~

只有 Human 問 24h 才出 24h 全表；平日最多一頁增量＋必要 SHA。沒有真正新成品時坦承零新增，但一定處理其他合法 READY。不能把 Reviewer 自報、狀態檔為 ACTIVE、排程卡片綠色或 GitHub commit 本身視為 DOCX 成功。

## 15. 最終判定與責任切割

- **REMOTE_INSTRUCTION_READY**：本 R12 GitHub 文件與 PR 讀回通過，只能說指示可被 Codex 取得。
- **WINDOWS_NATIVE_GOAL_AND_AUTOMATION_ACTIVE**：須 Windows 原生同來源證據，不因 ChatGPT 改 GitHub 而 PASS。
- **W1/W2_OUTSOURCING_PRODUCTIVE**：至少一個新 work_id 真正完成外包內容、被 DOCX/Review 採用、QA exact SHA、遠端讀回；只呼叫模型或花 token 不合格。
- **QUALITY_CANDIDATE_COMPLETED**：Word/數學/文類/視覺/獨立語意與 SAMPLE 清冊依完整驗收契約通過，仍非 REAL/HUMAN_ACCEPTED。
- **AUTONOMOUS_TWO_HOUR_RECOVERY**：有唯一原生 task 的真自然觸發，接續已存在工作，沒有雙主與因 pause/no-tool-call 再自鎖；尚未觀測自然觸發即 UNKNOWN。
- **FINAL_MISSION_DONE**：129 個具名需求逐件 1:N 真正完成、Human 許可與真實原件/第三方保留界線，不能以 142 個檔名或 61 筆 GitHub commit 冒充。

**下一個實際操作永遠是：原生觀測 → 看見具體缺口 → 做最小合法動作 → 同來源 readback → 下一個 READY。請執行，不要再提交大篇「理解計畫」或重建已完成 Word。**

---
**外部參考（不同於本專案證據）：** OpenAI 官方 Using Goals in Codex：https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex ；官方 Scheduled Automations：https://developers.openai.com/api/docs/guides/agents-api/sessions/automations （Agents API 架構不等於 Windows Codex App native Scheduled；不可照搬 API 冒充本地已安裝）。