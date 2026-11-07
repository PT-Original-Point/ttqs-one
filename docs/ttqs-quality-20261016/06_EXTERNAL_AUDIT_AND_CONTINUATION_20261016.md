# TTQS ONE｜R12 2026-10-26 24h 最新增量：從已暫停排程恢復真正 Writer/Review 閉環

**COMMAND=TTQS_ONE_20261026_R12_FULL_RECOVERY_DELIVERY**  
**完整操作指揮書（同 PR #92、已有檔案，非第二控制平台）：docs/ttqs-quality-20261016/reports/TTQS_ONE_R12_20261026_24H_Win10_GitHub_Codex_Worker_Audit_Execution.md**  
**指揮書 Git Blob SHA-1：63f26f0708249b211611d51b34a7fb90b4cd26a9；需按本案真實 Windows OS/CLI 最新讀回執行，GitHub 提交不等於本機已套用。**

Human 10/26 22:05 Windows 24h 報告顯示兩條 Codex automation 均 PAUSED、舊 OS Supervisor Disabled、GOAL/自然排程未證明續工，面板 8765/8766 OFFLINE；R11 放寬 Prompt 但沒有原生執行證據。最新 R12 **優先於下列 R11/R10/R09 的歷史出工處置**，已通過同 SHA 產物/審查不得重跑。其他安全、SAMPLE/REAL、獨立語意、Word 視覺規則保留。

精確增量：同 24h GitHub branch commit API 依 committer UTC 範圍分頁查得 **61 個不重複 SHA**（非本機僅列出的 13、非 61 件 DOCX）；本期只有 0100/0121/0122 3 個 doc_id 的 Word 變更，W1 OpenCode 6 session 僅 1 次有效文字審查，W2 Antigravity 14 attempts/10 正向有限範圍但實際 backend Gemini identity 多 UNKNOWN，可見 ≥391,827 tokens。0100 R09b 是最新而非舊 R10 SHA；0121 R02 SHA ae5da09e... 技術/23頁視覺 PASS、語意 PENDING，OpenCode 429 retryAfterMs=62226000；0122 R02 SHA d3a6a122... 28頁 Word＋W2 原文已存在但 packet asserted SHA 類型需無模型仲裁；0133 README PENDING 已落後於同 SHA W1 成功 review；0135 Word 可用但 semantic 受 429 限制。0110 R07 之後已有後續 Word/QA，禁止沿用 R10.1「0110 尚無 DOCX」舊結論。0142 為專案歷史 142 deliverable 序列末項，不得誤建 0143。請用同源資料按最新狀態縮減修復。

**下一合法順序**：Windows 目前 GOAL/Automation native PAUSED 原因、last/next/budget/最後一次有無 tool call 與 owner → 當次有權本機 Session 繼續已核准的可逆 READY、不等 120m → 0122 原始審查零 Token SHA 鏈仲裁 → 0133 舊 README 局部修正 → 0121/0135 等路由/失敗限定 QA 及其他有實際 READY 的 142 crosswalk 工件 → 合格 W1/W2 真派工/回收 → Word+QA → 最小 GitHub raw bytes readback → 下一 READY。Black console/52 Word COM/429 只局部診斷。無原生 Windows/PANEL/天然 120m trigger 收據一律 UNKNOWN，不自報 PASS。

---

# TTQS ONE｜R11 Human 2026-10-23：淨刪自我鎖，120 分鐘只補漏、不節流

**COMMAND=TTQS_ONE_20261023_R11_DELETE_LOCKS_CONTINUOUS_DELIVERY**
**STATUS=GITHUB_CONTROL_CANDIDATE; WINDOWS_EFFECTIVE_AUTOMATION_PROMPT=UNKNOWN; REAL_120M_TRIGGER=UNKNOWN; FORMAL_ACCEPTANCE=NOT_GRANTED**

Human 最新施工規格：取消固定一 BUILD + 一 REVIEW、每個 scheduling turn 只做一次 attempt、做完一個 bounded READY stage 就要等 120 分鐘、必須使用可能不存在的 /goal resume 才能工作、MainWindowHandle 無法量測就全面禁派、舊 Canary 重新開工 Gate。**120 分鐘仍保留為唯一原生補漏週期，不是工時/產能上限。每個合法 stage 終態確認後，在同一仍活躍的合法 Session 立即開始下一個 READY**，不同文件依 Windows 資源和真正作用範圍可並行。保留相同 DOCX/shared register/同一 Git ref 的單一寫入 owner、unknown-effect readback、全部必要品質和安全保護。

已修改同 repo 的 AGENTS.md、04_CODEX_GOAL_24X7_EXECUTION.md、05_HOURLY_NATIVE_WAKE_RESUME.md 頂端 R11：移除上述現役時間窗與固定席次自鎖。**Windows Codex App 的原生持久 prompt 尚未由本次外部寫入或驗證**；必須在現有 Codex 原生排程介面修改原本唯一的 ttqs-one-hourly-quality-goal-resume、讀回並觀測真正自然觸發；不直接修改未經支援的私有 toml/DB。舊 Disabled Supervisor / AUTONOMY_POLICY.md 未找到現役 consumer 前不得亂改。

**完整可執行施工指揮書**：Human 附件 TTQS_ONE_20261023_R11_自我限制淨刪與連續施工_完整Codex指揮書.md；SHA-256 a0b2d24f60abe4c7819ca64505bb0fb1aae181db5ab0136f0527f4b121679493；336行、39543 bytes。另附同一 120m 排程持久 Prompt 專用文本。Codex 必須實際閱讀並依附件 S0～S12 做精確 Windows 原生讀回、派工、回收、Word QA 和 GitHub 同 SHA 讀回；不只在對話自報完成。

## R11 新鮮已完成證據：舊 R10 待辦需修正
- 0100 R10 SHA 1563f89a1b83119c5f7c57a21cbf6b89cc0c213231c5d12f90fc4d58fa06039e：已有 GitHub 20檔精確回讀，除新 SHA/缺陷不重建。
- **0109 R14 的 X02/X03 已在 R10.1 之後結案**：10/23 10:41 commit 3463e230c31305af8d40670932c7cde08101e1dd 修 I18-E17 primary 對照與 I18-E08 負向近鄰；10:42 commit 009b1bce564fdf724bff9e73770d3baebc4250c5 的 github_readback_receipt_R14_X02.json 對 17/17 個遠端檔案核對一致，DOCX SHA 6f846e1737ff0d9b8baf40f459071f9258d51c267935d95222a89e7a05804a63 未變。**禁止再根據下方舊快照重修 0109 來源或重作完整 reviewer。**
- 0102 Windows R08c SHA 84c279d09484b88724dd59ae8a5155cb8d0be284133258e166269a80c26c67b4（57頁 Word 視覺證據、semantic PENDING）與 GitHub R35 SHA 04f71db94dd8949b2e0fc67fc0df5577c2a647138b95e3beadd3be2dea4457aa（text semantic PASS、visual BLOCKED）不得拼合成一個 PASS；先唯讀 source/content/QA 比較。
- 0110 Worker 失敗證據已有 20檔 GitHub raw-byte readback，但沒有候選 Word。OpenCode DeepSeek 32000 reasoning/0 output、MiMo 396秒無 assistant；Antigravity parser errors、partial、虛構保存期限，全部 NONADOPTED。0110 Antigravity Writer PAUSED。先 Python 對 L01～L09、C03～C07 題項/量尺/構面/分母建立可重算對照，6/8=75%、7/8=87.5%、+12.5百分點、target90%→REVISE，再以合格短包 OpenCode v2 外包，不同長 prompt 原樣重投。
- Windows Human 10:33 唯讀面板 8765/8766 無監聽、queue 10/19、thread automation ACTIVE/120m 但原生 last/next/natural trigger UNKNOWN；面板不是 READY/Writer 的 Gate。sandbox=unelevated、Node REPL 120s、hook 3s、multi_agent_v2=false 沒證據是 Writer 六分鐘上限，保留不盲改。

執行順序：S0 Windows native OS/owner/原生 scheduler prompt → S1 GitHub fresh exact HEAD → S2 確認舊 Policy 真正 consumer → S3 透過原生 UI 更新唯一排程有效 Prompt → S4 本機 AGENTS/GitHub readback → 選 0102 有界 diff 或 0110 無模型量表映射（依當前 OS READY）→ 真 CLI 小包回收 → Word／獨立語意 QA → 必要 GitHub bytes readback → **同一活躍 Session 直接施工下一 READY，不等待下個 120m**。

---

# TTQS ONE｜R10.1 2026-10-23 10:28 即時增量：0110 完整撰稿尚未成功（Human 最新施工修訂）

**COMMAND=TTQS_ONE_20261023_R10_1_0110_WORKER_FAILURE_DELTA**  
**來源**：PR #92 `0110_I18-E19_R01_20261023/worker/worker_closeout_0110_R01.md`、`github_readback_receipt_R01.json`；Human 外部指揮書最終完整附件 SHA-256 `609ad4438bb194b0305486b4a891fae9027de65df27749e22d927fd0f77ad823`（63,233 bytes，542 行）。下方 R10 09:50 關於「0110 source/Blueprint READY」是**來源就緒、尚未派工的歷史截面**；本 R10.1 優先。實際執行時先讀 GitHub/Windows 是否還有更新工作。
- GitHub `f3ffb6fedafb2760fb431bc0c29cc0c4e42f1786` 保存 0110 Worker 失敗收據的遠端讀回；先前 `675ed18e...` 有 Git 換行差異，經 `a5edf0a2...` 修復後 20/20 raw bytes exact match。**這只是失敗證據保存成功，不是候選 Word 成功。**
- OpenCode DeepSeek（CLI v2）0110 Writer：8,648 input／32,000 reasoning／0 output；MiMo 另一 Writer 約396秒無 assistant 回覆。二者皆無可採用稿，不能用免費模型型錄、session 或 exit 自報成功。
- Antigravity 0110：前兩次 CLI 參數錯誤，A3 3分鐘 timeout 只回不完整稿，補稿內容不連續且提出沒有來源的三年保存期限、聲稱已檢查實體檔案、聲稱 QA PASS、建議拿掉 SAMPLE 標記；全部 **REJECTED**，指定 Gemini 的真實 serving identity 仍 UNKNOWN。依現有 Human 三次失敗加三次修正停派規則，**只暫停 0110 的 Antigravity Writer 路由**，其餘獨立工作可繼續。現有設定中的 `--mode plan` 在 CLI 禁用 slash expansion 時有警告無效，不能當安全驗收。
- **下一個實質且低成本動作**：不要再派相同 0110 整篇。以 Python/來源表修正 Learner L01–L09（9題 vs 4構面）、Client C03–C07（5題 vs 3構面）的 item→construct→scale→N/A→分母映射；L04 頻率 4–1/0 不得混入一般 4–5 favorable formula；重算合成 `6/8=75.0%` → `7/8=87.5%`、差 `+12.5 percentage points`、target `90%`、應 `REVISE` 而非 CLOSE。未取得協會保留年限、批准或真實問卷不能憑空填寫。
- 0110 數據結構修好、OS 無同一 Writer 活躍，且**工作包真正縮小**時，才允許在合格免費 OpenCode CLI 以「單張量表映射／一份問卷／單份行動計畫」分段派工、逐件回收；Antigravity 路由不合格就不派 Gemini-only Writer。其間先處理下方 X01（0100已remote讀回）、X02/X03（0109遠端收據與錯誤 crosswalk）、X04（0102 R08c vs R35 相互獨立的 QA）。
- 上述只代表 GitHub 已保存 R10.1 候選操作規格。Windows live model/panel/scheduler/GOAL 和 Human 正式接受仍必須同來源 readback，未知寫 UNKNOWN。不得為追逐一個模型路由浪費整個 GOAL。

---

# TTQS ONE｜2026-10-23 R10 最新增量鑑識與「停止無效重做」指示（Human 指揮書附錄）

**COMMAND=TTQS_ONE_20261023_R10_EXACT_RECONCILIATION_AND_EXECUTION**  
**PROJECT_ID=TTQS_ONE；SCOPE=既有 PR #92 可逆 CANDIDATE；STATUS=GITHUB_CONTROL_CANDIDATE，Windows 實機 R10 施工尚未由本次 ChatGPT 驗證。**
**來源**：Human 提供 2026-10-22 09:30～2026-10-23 09:30 Windows 本機 24 小時報告，SHA-256 `dee4ae1bd40fcf0f41166c882e7e0de9b4028cd6142b4b6a90c1b10c43dc20fe`；R10 完整詳細指揮書為 Human 新版附件，SHA-256 `46838700c39d39a13454245f84be4579adb75270881d2c034c1c4d2e23d7d783`，約 58KB/514 行。本檔只登錄新發現與下一合法動作，不複製 58KB 全文；執行時 Human 附件和此段相容並行，後續 Human 最新命令優先。

**2026-10-23 約10:17 台灣 fresh GitHub**：PR #92 `open/draft`，HEAD 在寫本段前 `f275dc6acf7b2da25dec75de3b7c6a182a232d8e`，指定 24 小時窗口 36 commits；報告截止後再有 2 commits 新增 0110 I18-E19 的 source/Unique Blueprint。這些不是正式 TTQS 接受，也不是此刻 OS live Writer。

## P0｜先消除「已存在當未存在」與「同一文件不同 SHA 拼 PASS」

1. **0100 R10**：本機 09:30 報告稱缺 GitHub readback，但 GitHub 已有 `0100_R10_20261023/evidence/github_readback_receipt_0100_R10.json`，對應 commit `ccbc60cdd9b60e09262bb46d9b165b7396291140`、20個檔案 readback，DOCX SHA-256 `1563f89a1b83119c5f7c57a21cbf6b89cc0c213231c5d12f90fc4d58fa06039e`。先 fresh-read OS 實際候選與 GitHub，同 SHA 則不重推、不重建、不全文重審。
2. **0109 R14**：本機報告只知 staging；GitHub 已有 R14 Word/PDF/QA，DOCX SHA-256 `6f846e1737ff0d9b8baf40f459071f9258d51c267935d95222a89e7a05804a63`，但沒有同口徑全檔 raw-byte readback 收據。優先補最小遠端對帳，不重做已存在 Word/QA。另 `quality_summary_R14.json` 把 **I18-E08 / 0100+0101** crosswalk 收據用在 **0109 / I18-E17** 身上；這是 sidecar SOURCE_PROVENANCE 缺陷。先以正式 03 與 crosswalk 的 I18-E17 列修來源收據，查正文是否受影響；沒有正文缺陷就不動 DOCX bytes。
3. **0102 I18-E09**：Windows R08c DOCX SHA `84c279d09484b88724dd59ae8a5155cb8d0be284133258e166269a80c26c67b4`，有 Word 57頁 visual Scope，但該 SHA semantic PENDING／remote PENDING；GitHub R35 DOCX SHA `04f71db94dd8949b2e0fc67fc0df5577c2a647138b95e3beadd3be2dea4457aa`，同 SHA semantic TEXT_ONLY PASS，但 LibreOffice unavailable、Word COM timeout，visual BLOCKED。**不得拼兩個 SHA 的 PASS，不因 R35 數字較大就取代 R08c**。唯讀比較兩者正式來源、章節/CASE/算式/SAMPLE/缺陷/版面後選一條最短收斂路徑；builder exit 1 且有穩定 Word 先 bounded salvage；精確阻擋只停 0102 promotion lane。
4. **0103 I18-E10**：10/23 兩次 Writer 零輸出（一筆 32,000 reasoning，0 output）是**此次新派工失敗**，不是需求完全無 DOCX。GitHub 已有 R02 baseline、R03 未採用的 layout regression；優先局部修 R02 Word 分頁，禁止同大 prompt 再派整篇撰稿。

## P1｜雙 CLI Worker、成本與排程的限定改善

5. **Antigravity**：0100 R10 指定 Gemini 3.8 Flash High，實際 fallback 到 CCPA，回覆未採用；不能記 Gemini PASS/扣額。先用同一 Windows 帳戶的原生 CLI --help/模型設定/已知成功收據查來源；不能證實指定 Gemini 就停**這一條**文字路由，不能 Computer Use、權限繞過或未批准付費，其他 OpenCode READY 繼續。
6. **OpenCode v2**：0100 R10 Writer 4項小型修補有採用；0100 reviewer input 78,783/reasoning 48,079/output 4,614，0109 reviewer input 54,587/reasoning 34,991/output 1,627，0103 Writer 32,000 reasoning/0 output。減量目標是**短而專的來源包＋確定性靜態檢查＋只補欠缺語意範圍**，不是減少必要品質。已同 SHA 同範圍 PASS 不全文重派；免費模型型錄／exit0／session idle 都不能證明可用/付費/完成，所有 attempt 需回收原始回覆、exit/error、採用 SHA 與實際模型或 UNKNOWN。
7. **0110 / I18-E19**：PR #92 在 09:50 已有 `0110_I18-E19_R01_20261023/source/SOURCE_PACKET_0110_I18-E19_R01.md` 與 `UNIQUE_BLUEPRINT_0110_I18-E19_R01.md`；先查 OS 活躍 Writer/未同步工件，沒有衝突就當 `READY_WRITER`，做**學員問卷 + 目標客戶問卷 + 課後行動計畫**完整 SAMPLE 示範，不虛構真正組織績效或統計顯著。
8. **監控/排程**：Windows 09:30 快照 8765/8766 無 LISTEN；dashboard/MASTER_STATUS 10/05，queue 10/19，仍 STALE/OFFLINE。Codex Thread automation `RRULE:FREQ=HOURLY;INTERVAL=2` ACTIVE 只有設定層，真 last/next/natural run UNKNOWN，舊 OS Supervisor Disabled。先核 OS/本案 panel 原生來源，再按 04/05 原規則修唯一 120m 排程與真正續工；不可只重啟沒有 GitHub API 的舊 panel，也不能把 PTYSD Win11 Issue407 的面板冒充本案。

**單一下一合法動作**：在 Windows OS/Repo fresh-read 後，先處理低成本 0100/0109 遠端與身份收據，再並行有界 0102 分歧調查及（無 Writer 時）0110 合格 CLI Writer；每次一個 work scope、保留已完成 exact SHA、每個穩定候選與終態 QA 才最小推送 PR #92 並 raw-byte readback。勿新建 Supervisor/DB、勿每120分鐘寫重複長篇報告、勿把來源/模型/UI/正式接受不同層級混成 PASS。

---

# TTQS ONE｜2026-10-16 外部稽核 Findings 與 Codex GOAL 即時續工命令

> **證據身分：CANDIDATE／獨立外部稽核記錄**。基準 GitHub：\`PT-Original-Point/ttqs-one\`，PR #92，當時 head \`57f19ed8496aabbf99a8bb5bfc805a1293151ff5\`；查核日期 2026-10-16（台灣）。本記錄只新增可追溯 Findings 與已批准的下一施工動作，不把 Draft PR 升格 canonical、不撤銷既有 exact-SHA PASS、不修改 DOCX、OS 排程或對外服務。正式資料及 Windows 執行存活需各自 fresh-read。
>
> **Human 最新 Mission**：依原始點協會真正用途與官方「常見參考佐證資料」129 個具名方框，逐件交出成熟、完整、正確文類的 DOCX；有可重算的 SAMPLE/SYNTHETIC 實際示例、清楚 REAL 替換邊界、可供人閱讀和操作、獨立 exact-SHA 品質審查。每件穩定候選、QA 終態及重大進度須同步既有 GitHub 供外部稽核。不存在真實原件者不能捏造。延續既有 GOAL，不加新排程、第二套控制面或人工逐件核准 Gate。

## 1. 本次已真正直接驗證的 GitHub LIVE 事實

1. PR #92 仍是 **Draft**，當時 head \`57f19ed8496aabbf99a8bb5bfc805a1293151ff5\`，base \`submission-20261005-222304\`；正式 \`main\` 不因此改變。證據：https://github.com/PT-Original-Point/ttqs-one/pull/92
2. 0036 R08 真正已上傳到 \`docs/ttqs-quality-20261016/quality-review/0036_R08/\`：候選 DOCX、官方來源/藍圖/鄰項、完整抽出文字、75 筆合成清冊、完整 Word PDF、四張審查頁影像、技術/版面背景收據、原始 CLI stdout/stderr、完整與正規化語意審查結果、manifest、progress。證據：https://github.com/PT-Original-Point/ttqs-one/commit/57f19ed8496aabbf99a8bb5bfc805a1293151ff5
3. 外部稽核者**實際從 GitHub 抓取 DOCX 的 base64 位元組，獨立重算 SHA-256**：228,221 bytes；\`e2d4b3f5e906faaf3d473c7351bd79618a78dcf2c8f91a32a4e952d005ac5eae\`；與 manifest、進度及 reviewer 所綁 SHA 完全一致。**REMOTE_ARTIFACT_IDENTITY=PASS**；這不是僅依 Codex Builder 自報。
4. 文件正文確有 I07-E04 三大核心產物的文字/證據：9 步課設 SOP、已填完整示範進度、課程規劃流程圖、職能/需求→目標→教學→評量、三方案加權比較、210 分鐘時程、10 個合成案例前後測、四情境測驗與答案錨點。不是單純的空白表或只換標題。但本次文字與部分審查資料**不能單獨證明全文件圖像排版都完美**。
5. 同一 GitHub 分支的 \`quality-review/\` 目錄**當次僅列出 \`0036_R08/\`**。使用者提交之 Codex 工作紀錄對 0031/0032/0033/0034/0035/0039/0043 有本機工作敘述，但在此 GitHub 位置尚未查到這些最新穩定候選的獨立、完整遠端封包。其本機狀態不得由此判定為不存在或 FAIL；只能標 \`REMOTE_AUDIT_READY=NOT_VERIFIED\`。
6. 0036 CLI 審查封包顯示 \`status=SUCCESS\`、\`exit=0\`、審查結論 \`PASS\`，指令請求 \`gemini-3.8-flash-high\`、high effort；**CLI 回傳沒有實際 runtime model identity**，不得寫成 provider 驗證了模型。語意審查本身限定於給它的 source/packet；它沒有在工具端執行原始檔案驗證程式。此限制需保留。

## 2. 外部 Finding 與精確處置

### F-01（P1）0036 的全頁視覺驗收證據不全；不能覆蓋既有語意 PASS

- 0036 的獨立 reviewer **只直接目視第 14、16、18、19 頁**；第 1–13、15、17 頁引用抽取文字、原有 QA 與封包。**官方 I07-E04 的課程規劃流程圖位於第 5 頁，未在獨立審查中直接目視**。
- **既有 exact-SHA 語意結果保留 \`PASS_WITH_DECLARED_SCOPE\`；\`FULL_DOCUMENT_INDEPENDENT_VISUAL_COVERAGE=PARTIAL\`。** 在尚未發現實質缺陷前，**禁止為了補視覺收據重建 0036 DOCX 或重跑 16 萬 token 等級的完整語意審查**。
- 合法下一動作：使用既有 GitHub/Windows Word PDF（19頁）及原件，以同一 exact SHA 做**補充的只讀全頁視覺稽核**，第5頁流程圖必須檢查箭頭、否決分支、可閱讀性；其餘未直接目視頁檢查孤立表頭、溢出/壓字、截頁、圖/表對應；保存頁碼/缺陷定位與額外照片或簡明收據。若可見重大缺陷，**只對定位到的缺陷修復**，產新 SHA 並依受影響範圍複核；沒有缺陷則記 \`FULL_VISUAL_PASS\`，舊 Word bytes 不變。
- 此為「補完實際驗收」，不是創設第二個 reviewer Gate，也不停止其他已授權 READY 文件。

### F-02（P1）GitHub 外部可稽核進度未全面同步

- 本機已有候選/審查時，需在**完成穩定候選或 reviewer 終態**後，沿用原本 PR #92 對應分支推送必要的可公開 DOCX bytes、所用官方/Blueprint 索引、SAMPLE 替換清冊、PDF/圖片（有需要才附）、原始工具結果、QA 收據及 manifest/短進度。**GitHub source-of-truth 不等於所有本機 CURRENT 都已正式接受**。
- 每個上傳 commit 後需從 GitHub **同來源讀回 DOCX bytes／SHA、收據與最終判定**，才標 \`REMOTE_AUDIT_READY=YES\`；不能只用 \`git push exit 0\` 或 URL 存在認定。
- **優先同步已有穩定候選／審查證據的 0031、0032、0033、0039**，其各自版本與 exact SHA 必須先 OS fresh-read，不能依舊聊天硬編；0034/0035/0043 只有在最新候選固定且相應最小進度狀態清楚後同步。未驗收者照標 CANDIDATE/PENDING，不必等成為 PASS 才允許稽核讀取。
- **公開儲存庫資料邊界**：不要推未公開身分證件、學員/會員個資、受保護財務、真實簽名/第三方私密原件、憑證、金鑰或敏感醫療資訊。只推已可公開的原件/合成示例/必要去識別 QA；不能公開的原件保留在有權限的正式來源，以授權路徑與不可逆轉的摘要標記索引。缺少真實原件不可以假造；不能把只含索引等同於可公開原件已上傳。
- **同步觸發以實質變化為準**：每份穩定候選、獨立 QA 終態、重大故障或 Human 新規格，應產生可稽核 commit；沒有內容變化時不需要每小時空推 GitHub，也不必新增監控 DB。

### F-03（P2）0036 審查用量偏高，但不可降掉關鍵品質

- CLI 原始統計：\`input_tokens=141428\`、\`output_tokens=26701\`、\`thinking_tokens=20380\`、\`cache_read_tokens=1348414\`、\`total_tokens=168129\`。欄位口徑可能重疊，不得加總猜帳單金額，**實際費用 UNKNOWN**。
- 下一次只針對確切未驗區域做補充審查；新文件的獨立語意審查仍要獲得必要的原始 PDF/Blueprint/正文/示例與 register，不能透過縮掉驗收證據換取虛假 PASS。
- 沒有新 DOCX SHA/實質缺陷，不要每小時重跑同一個 reviewer。

### F-04（P2）0043 R03 與其他候選不可因 Builder 自檢宣稱完成

- 使用者提供的 2026-10-16 工作紀錄顯示 0043 R02 字級單位處理錯誤；已被技術檢查攔下。R03 回報19頁 Word 輸出、235段、14表，正文與表格字級達標，但**最終實體 SHA、全頁品質及獨立語意收據未在本次遠端觀測取得**。
- 先本機讀回最新 SHA/Word render/真實 reviewer 結論，完成必要 QA，依精確狀態同步；不能因前一輪失敗永久鎖住獨立 READY 車道，也不能在只有 metadata 改變時重建 Word。

### F-05（P2）外包失敗三次停派規則已有文字，尚無行為驗證

- 使用者已規定：Antigravity 或 OpenCode（v2）同一路由**連續三次錯誤，且三次修正仍不能正常執行與回報**，只暫停**該外包路由的新派工**；原始失敗、三次修正、工作進度、外部不明效果等必要內容整理到既有 GitHub PR/Issue；其他可用 READY 工作不得陪停。正常運作或尚未達門檻不能自己假設「已失敗三次」。
- 不自建新監督服務或高成本故障測試。將停止判定納入現有派工路徑，以有限的非破壞測試或下一次真實故障證據驗證；不為驗收故意製造三次額度消耗。
- Antigravity 使用原生 **CLI**（非 Computer Use UI）；OpenCode 採當前合法 **v2 CLI**；每次外包都需回收原始輸出、確認完成、獨立檢查，未回收不能當 PASS。

## 3. 立即給現有 Codex GOAL 的增量執行命令

\`\`\`text
COMMAND=TTQS_ONE_EXTERNAL_AUDIT_FINDINGS_20261016_CONTINUE
PROJECT_ID=TTQS_ONE
MODE=CONTINUE_EXISTING_GOAL_NO_NEW_SCHEDULER
TARGET_REPO=PT-Original-Point/ttqs-one
TARGET_BRANCH=work/ttqs-one-document-quality-contract-20261016
TARGET_PR=92
SOURCE_AUDIT_FILE=docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md
HUMAN_MISSION=PRODUCE_AND_VERIFY_FULL_HIGH_QUALITY_TTQS_DOCX

1. Fresh-read 本檔、01–05 品質及既有正式 Blueprint/142 crosswalk；對每個 Word doc_id 精確綁官方 requirement_id，不把 checkbox 流水號錯當 DOCX ID。最新 Human 授權的可逆文件施工可繼續；未核實的真實外部授權、正式簽章、送審/費用/身份等仍保留 Human Gate。
2. 只保留現有綁定 TTQS GOAL 對話的單一每小時排程；不要再改排程、另開獨立 hourly session、新建 supervisor/控制面。前次設定是使用者提供的工作紀錄，Windows/應用程式當下的存活與真實 hourly run 仍須 native readback；沒有實質變化不重複呼叫高階模型。
3. 首先以 OS/既有 repo 判斷哪一個 Builder/Reviewer 真正活著及未結外部效果、共享範圍 owner；同一文件一個 writer，不因暫時沒有回覆就重派 reviewer。不可把 RUNNING 記錄當 OS 存活。
4. **0036 R08 固定已獨立核對的 exact SHA，不重建。** 使用既有19頁 Word PDF/DOCX，以已核對的同一檔案補第5頁流程圖及剩餘未直接目視頁的視覺檢查；獨立原語意 PASS 保留 scope limitation。完成後僅新增補充 visual receipt；若有真缺陷附定位再修。
5. 並行處理下一 READY：0043 R03 確認本機最新 SHA、完整19頁視覺與獨立語意；如已完成則直接回收結果並更新 GitHub，不重跑。0031/0032/0033/0039 先讀既有審查原件；狀態不明維持 UNKNOWN，不能把舊回合的 PASS 誤套新 SHA。
6. **任何外包結果都要完整回收。** 技術/版面/獨立語意、失敗、超時或三次修正停派等重大材料變化，整理最小必要清冊；所有可公開候選、完整審查原始回覆、來源/Blueprint 定位、確切 SHA、SAMPLE register及必要的 Word/PDF/視覺證據，推送目前既有 PR #92 的候選分支。不得因先前只保存 Windows E:\TTQS 本機而宣稱外部可稽核。
7. 對每一 commit 做 GitHub 同來源重新取得位元組核對與 reviewer 收據一致；有共享寫入競爭/遠端 head 改變時 fresh-read 並整合，不 force push、不覆蓋他人新進度、UNKNOWN 效果不盲重試。保留所有舊版審查歷史及候選的現有 CANDIDATE 身份。
8. 三次錯誤＋三次修正仍無法運作：只停出錯的 Antigravity / OpenCode v2 派工路由；完整保存並同步事故摘要與可公開證據；其他 READY 文件仍續做。正常情況不額外建立新的測試代理或浪費高額 Token。
9. 一份文件真正完成一個 material delta 後，即進下一個 READY 文件。重點是正確的原始點協會專屬內容、真實辦訓邏輯、完整 SAMPLE、無假原件，不能把「所有字級 PASS／檔案已推送」當最終品質完成。
10. 每次有結果簡要回報：正式/候選 Spec SHA、實際完成 DOCX exact SHA/遠端 GitHub 路徑、獨立驗收及覆蓋範圍、REMOTE_READBACK、還有哪些受影響 BLOCKED、下一合法 READY、真正 Human Gate。無新實質變化不產生空白報告。

FIRST_NEXT_ACTION=CHECK_0036_MISSING_VISUAL_PAGES_WITHOUT_REBUILD_AND_SYNC_STABLE_CANDIDATES
OVERALL_GOAL_COMPLETE=NO
\`\`\`

## 4. 本次確認與未確認的狀態摘要

| 項目 | 判定 | 最小證據 |
|---|---|---|
| 0036 R08 GitHub exact DOCX bytes | **PASS** | 228,221 bytes，獨立重算 SHA-256 與 manifest 一致 |
| 0036 R08 獨立語意審查 | **PASS_WITH_SCOPE_LIMITATION** | 原始 CLI 輸出、七項準則及受限目視範圍 |
| 0036 R08 完整19頁獨立視覺驗收 | **PARTIAL** | 只直接目視 14、16、18、19 頁；第5頁圖缺目視證據 |
| 0036 R08 正式接受/真實協會核准 | **NOT_ACCEPTED** | 進度檔明載 CANDIDATE_ONLY |
| 0031/32/33/34/35/39/43 最新成果遠端同 SHA | **NOT_VERIFIED** | 當次 quality-review 只見 0036_R08 |
| 每小時排程最新實際是否觸發 | **UNKNOWN** | 需本機 Codex App/Windows native readback |
| 新版品質 GOAL 全體完成 | **NO** | 各具名佐證尚未全量獨立驗收 |

**下一步是實際品質與可稽核交付，不是再增加治理文件或排程。**


---

## 5. 2026-10-17 19:22 Human 最新增量｜省 Codex Token、CLI 外包、同步優先

\`COMMAND=TTQS_ONE_COST_AWARE_CLI_OUTSOURCING_SYNC_R01\`  
\`PROJECT_ID=TTQS_ONE\`  
\`TARGET_REPO=PT-Original-Point/ttqs-one\`  
\`TARGET_BRANCH=work/ttqs-one-document-quality-contract-20261016\`  
\`SOURCE_OF_COMMAND=THIS_FILE_SECTION_5\`  
\`AUTHORITY=HUMAN_LATEST_APPROVED_REVERSIBLE_CANDIDATE_WORK\`  
\`MODE=ONE_ACTIVE_WRITER; USE_EXISTING_GITHUB_PR_92_AND_NATIVE_CLI_ONLY; NO_NEW_CONTROL_PLANE\`

**適用與優先順序**：此節是 Human 2026-10-17 最新明確指示，補充本檔較早的稽核和 01–05；舊節中的「第一個動作檢查 0036 R08」已屬 10/16 歷史起點，**不得重新執行已完成的 0036/0043 全文重審或反覆產生活動日報**。新順序固定為：**本機↔GitHub 實質進度對帳與必要同步 → 外包 CLI Writer/Reviewer 真正派工及原始結果回收 → 修復已定位內容缺陷並持續下一個 READY → 降低 Codex 本體 Token 用量**。降低 Token 必須貫穿各步，不能以「先寫成本報告」拖延施工。

### 5.1 立即執行：本機、GitHub、命令領取三方讀回

1. 使用目前唯一真正有效的 Windows Writer/GOAL 原生工作環境，先唯讀核對 OS process command-line（不以 OpenCode service/Word COM 存活代替 Writer alive）、未提交變更、共享 register owner、既有 pending external effects、\`git status\`、精確 HEAD、各個本機最新 DOCX/QA SHA。對照同一 PR #92 分支與 Source/Blueprint；不要用本節建立第二個 ledger/queue、重複鎖或孤立工作目錄。
2. 截至 2026-10-17 18:40 台灣時間的已觀測遠端 HEAD 為 \`b53b85176ecbd8ec22e36aa766d24325636e3937\`：已有 0052 R02 exact-SHA 候選 \`9129aff2bb730d31f76a5cb457ed069f1cafd2460b4069219f697b35d2c11afa\`、0054 R14；**當時遠端未列 0055**。Human 19:20 Windows 畫面顯示 0055 R01 先發現表格 8.5 pt 與分頁缺陷、已進行 R02 修復；此為 HUMAN-SCREENSHOT，不是 GitHub LIVE、不是已完成驗收。請先讀本機最新 0055 Writer/Word/QA 真相，不重啟另一個 0055 Builder。
3. 對已穩定且可公開的本機候選及相應 QA/原始 reviewer 收據/合成清冊，**在既有分支一次提交必要差異，git fetch GitHub 後重算遠端 blob/exact DOCX SHA 與收據**；結果才標 \`REMOTE_SYNC_VERIFIED\`。對進行中的 0055，標 \`LOCAL_WIP\` 與目前完成階段；有重大進度且安全可公開時，在既有 PR 保存最短 checkpoint，不將未審候選冒稱 PASS。不要每頁、每次文字修正、每小時空動作都 commit；但正式穩定候選、review 終態、重大故障或 Human 新規則不得留在本機不對外同步。GitHub 與本機「同一穩定交付 checkpoint」必須精確一致；同步延遲或 WIP 必須明記，不聲稱逐秒同步。
4. **命令領取驗收**：讀回本節 \`COMMAND\` 及本文件最新 Git blob，另查 PR #92 留言 \`F-20261017-01\`～\`08\`（特別是 \`#issuecomment-6231114583\` 與 \`#issuecomment-6231360018\`），逐項判定 \`DISCOVERED / APPLICABLE / APPLIED / VERIFIED / OPEN / PARTIAL / BLOCKED\`；只對已真正修復且有 exact-SHA 及必要 reviewer/遠端讀回者寫 VERIFIED。0052 R02 只關閉 0052 本身正文工程資訊外露的有證據部分；F-08 的舊 0036 工作目錄污染與 Shell 方言錯誤仍須證明後續審查封包已修正，不能因 exit 0 或模型 PASS 自動結案。若本次仍無新穩定產物，保留 OPEN，勿為了 ACK 生成長文活動報告。
5. **0055 特別檢核**：任何 R02 版必須重新檢查正文字級至少 10.5 pt、表格至少 9.5 pt、字型實際 Word 匯出後分頁，專屬「講師遴選／聘任」邏輯、合成候選人分數、同案例來源及教學/行政可讀性；修復後才可委託 reviewer、回收新 SHA/原始回覆並同步。未通過不能因局部目視或 Worker 自稱 PASS 升格。

### 5.2 唯一合格外包路由與免費模型選型

- **所有受 Codex 委託的 AI Worker，只能透過本機已有且現場驗證版本與權限的 \`OpenCode v2 CLI\` 或 \`Antigravity CLI\` 進行。** 禁止使用 Computer Use、桌面 UI 點擊、螢幕操控、瀏覽器自動化、第三種 Worker/harness 或旁路遠端 API 冒充這兩條外包路由。Codex 自己可使用已授權的 Git/gh、PowerShell、Python、Microsoft Word COM 和 GitHub 工具完成原生施工/驗收，不以 GUI Worker 代替 CLI。
- **Antigravity 路由只准請求 \`gemini-3.8-flash-high\`**，無法使用時只停 Antigravity 該車道，不自動改模型、繞過授權、改成 Computer Use 或要求所有生產停工；沿用官方受支援參數與受限唯讀/可逆寫入權限，禁止 \`--dangerously-skip-permissions\`。0044 四次 headless 權限拒絕、三次修正後停派是有收據的舊事故；0054 R14 之後雖有成功回覆，**仍要從原生來源解釋如何恢復該路由的合法派工能力**，不能用成功字樣抹掉原事故/三修政策。
- **OpenCode v2：只允許實機 \`opencode models\` 或等價官方 CLI 列得出、當下可用、能無追加費用使用的免費 SKU**。選型參考 2026-10-17 每日免費模型查核：優先有界試用 DeepSeek V4.1 Flash Free；失敗或任務不適合再考慮 Muse Spark 1.3 Contributor Free、MiMo V2.6 Flash Free。該日既有社群小測僅 3 題/單次，不代表 TTQS 17 頁長文可靠，也不構成永久固定優先序。每次依 provider 當前型錄、配額、429/5xx/timeout 及一個極短 CLI 原生回覆測試選擇；禁止為單次失敗啟動無限 fallback 迴圈或消耗 Codex 高階模型重講整份文件。
- 特別注意 0052 R02 reviewer 收據記載 \`opencode/glm-5.3-flash-free\`、runtime 說 \`GLM-5.3-Flash Free\`，但 2026-10-17 OpenCode 公開價格表中一般 **GLM 5.3 Flash** 列為計費 SKU。這兩者不能在未查原生 provider SKU、實際帳務/剩餘免費資格與是否產生新費用之前視為同一免費服務；\`COST=UNKNOWN\`，不得從名稱推定 FREE、不得自動購買 credit/改付費模型。需 Human 新費用授權才可增加成本。
- OpenCode 與 Antigravity 分別保留實際 native command/版本/model request/runtime identity（若未回傳寫 UNKNOWN）/error 與 timeout；三次錯誤經三次有界修正仍失敗只暫停受影響路由，其他 READY 繼續。安全或權限不許的命令不走全域放行。

### 5.3 外包「有形交付與回收」，取代 Codex 反覆親自長篇撰寫

1. 將每件工作拆成一個真正小的可驗收工作物：官方方框與應用情境核對 → **專屬** Blueprint 的實際欄位/問卷/公式/完整 SAMPLE 答卷 → 寫出真實可開啟 DOCX/建置腳本 → Word 固定 PDF 技術與全頁目視 → 獨立語意（不同於 Builder）→ 定位缺陷的 bounded repair → exact-SHA 發布。Codex 只做項目選擇、任務派發、原生 deterministic L0 比對、必要品質仲裁與安全外部寫入，不重讀每頁或重做 Worker 可以完成的作文。每份 DOCX 的同一寫入範圍只有一位 Writer；獨立文件可並行但不共寫 CURRENT/register。
2. 每次 Worker 收到**限定文件的隔離 packet**：此件官方原文與頁次、已核實協會定位/同案例共用事實、該件獨有 Blueprint、負向近鄰差異、exact SRC/候選 SHA、僅需的 PDF/圖片/CSV、接受準則與工作路徑。不要任由模型在 \`E:\\TTQS\` 全磁碟或舊 \`_REVIEW_SYNC_0036...\` 遍歷；先修正 PowerShell 與 bash 語法不相容，使用本機支援的命令及絕對檔案路徑。不要在審稿封包內堆所有 157 方框、88 筆提交、完整聊天史或未相關 Word。
3. **每一個外包 attempt 必須實際回收**：native CLI exit code + 語意內容非空、原始 stdout/stderr 或保護敏感資訊後的可公開必要證據、模型身分與來源、輸入 packet SHA、候選 exact SHA、修改檔案清單、發現缺陷的頁/節/表、建議最小修補、QA scope、必要 token usage（input/output/cache/實際 billing 若 provider 有給）。\`exit 0\`、執行中、空回應、Worker 自評 PASS 都不是成功；不回覆不得派下一個重複同範圍 Worker。
4. **返工只交差異**：例如字級不合先由 Python/Word 確定性修；register 定位不合只改 register 並有界再審；PDF 孤頁只修 Word 分頁；內容誤解再由便宜且可用 CLI Writer 改相應章節。對未改 DOCX 的 metadata/hash，絕不重跑全 17 頁與完整高 Token reviewer。已確認 SHA 的舊 PASS 作歷史保留；真正改 DOCX 則以新 SHA 對受影響內容、跨頁與必要獨立語意重核。
5. 對每份成品實施標題盲測：拿掉工程標題仍能知道文件用途；對行政志工必須白話、完整、有責任/時機/步驟/實例，所有敏感療效及 REAL/合成邊界清楚。**工程 SHA、内部控制 metadata、JSONL 路徑不得寫進 Human Word 正文**，只留 sidecar。不能只有美觀與字級 PASS 就宣稱可用。

### 5.4 Codex Token 與每小時排程：只監測、修補、續工，不要每小時寫活動報告

1. **禁止為每小時喚醒、context compact、同一份日報改措辭、排程 ACTIVE 查核、無實質變化而重新生成長篇人類報告**。每小時任務的作用只是最低成本存活/命令差異/失敗補漏/合法 READY 續工；已有真實 Worker 在跑就不重派、不重啟、不叫另一批模型，也不為同一進展列幾十筆重覆 commits。只有完整候選、關鍵 QA 結果、重大故障或 Human 要求時，用既有 GitHub PR + 最短狀態更新；沒有變更就退出。長篇活動報告**僅 Human 明確索取時**製作一次。
2. 先由現有 native OS/Git \`L0\` 比對 \`git diff\`、GitHub HEAD、候選 SHA、queue/Writer pid 與 native scheduler last-run；**沒有 material delta 不叫 Codex/高階 LLM**。如果 Codex App hourly thread scheduled 每次喚醒都必然扣高階模型 Token，須先提出 native usage 與觸發證據，再依 05 已核准的二擇一規則，評估把**唯一喚醒 owner**切到既有 Windows Task Scheduler 的 cheap L0（先停舊、同來源讀回停用再啟動另一個，不能雙主）。此時若仍有正在寫的 0055 不得直接殺掉 GOAL/誤傷 Worker。無原生 last/next run 記錄則 \`SCHEDULED_WAKE=UNKNOWN\`，不要拿 UI「每小時／開啟」卡片、長回合及 Git commits 假稱實測。
3. Codex 本身的 Token 必須優先省：減少四個以上同時長期讀全量 repo 的子代理、重複載入 GitHub/官方文件、重複完整 Word 渲染及大段全量 stdout；先讓低成本 CLI Worker 真正產生成品或定位審查，再由 Codex 單次短仲裁。預設回覆只提供 doc_id、exact SHA、已證實修復/仍開啟、同步狀態、下一個 READY 一小段；每次模型輸入、輸出、快取命中、elapsed、找出的重大缺陷及返工成功率，沿用已有執行收據記錄，未知不得亂填 0。對高輸入案如 0043 的 Antigravity \`total_tokens=350812\`，下次先縮短 packet/輸出格式後以相同品質要求比較，**不可犧牲實質 QA 換漂亮 Token 數字**。
4. Codex 原生每小時排程已有 \`TTQS_GITHUB_COMMAND_PREFLIGHT_V1\` 的歷史設定讀回，不代表真實 scheduled-run 已通過。先 readback 原生 Prompt、last/next 與真正 triggered run；只在發現 Prompt 實際欠缺本節「無差異不耗 Token／不寫報告／只做同步與派工」能力時，**有界修改同一任務**並再讀回，不要每回合反覆「修排程」；也不要憑本 GitHub 文件就稱 Windows 持久化 Prompt 已更新。
5. 若人類當前的 0055 改稿有真正活躍 Worker，保留工作並在下一個合法 checkpoint 接手；禁止新 session、compact 或 hourly wake 重做同一文件。外部未知寫入只停影響的 push lane，其他純本地可逆工作可繼續。

**本節不是另一套監督系統，也不新增 Human 審批／新付費／Production 權限。正式/舊 canonical 差異仍依 01–05、 Human 最新要求標 \`SPEC_CONTROL_PLANE_REBASE_REQUIRED\`。**

\`ACCEPTANCE_THIS_COMMAND=NOT_YET_VERIFIED_ON_WINDOWS\`  
\`FIRST_NEXT_ACTION=READ_WIN10_NATIVE_WRITER_AND_LATEST_0055_LOCAL_SHA_THEN_SYNC_CHECKPOINT\`  
\`HUMAN_GATE=ONLY_NEW_COST_OR_CREDENTIAL_OR_IRREVERSIBLE_REAL_OPERATION_OR_FORMAL_TTQS_ACCEPTANCE\`


---

## 6. 2026-10-21 Human 最新命令｜R09 Windows 10 監控、兩個 CLI Worker、GitHub 一致性與兩小時續工完整操作契約

**COMMAND=TTQS_ONE_R09_WIN10_PANEL_WORKER_FULL_CLOSED_LOOP_20261021**  
**PROJECT_ID=TTQS_ONE**  
**SCOPE=既有 TTQS ONE 候選文件施工、PR #92、同一 Windows 10 主機、既有 GOAL 與唯一排程；不另設控制面。**  
**STATUS=CANDIDATE_INSTRUCTIONS; OS_NOT_VERIFIED; NOT_A_DEPLOYMENT_RECEIPT.**

### 6.0 絕對優先順序與防混專案規則

這份 R09 **補足** 2026-10-21 的 04 GOAL 防自鎖、05 唯一 120 分鐘排程與本檔 §5.2～5.4 的雙 CLI Worker 契約。後續有可核實的 Human 最新指示時，以最新 Human 為準。這裡不得回復到舊版每小時排程。

- 精確正式 repo：PT-Original-Point/ttqs-one；精確候選 PR：#92；目標分支：work/ttqs-one-document-quality-contract-20261016。**執行時重新讀 HEAD，不可固定以下歷史 SHA**。
- 2026-10-21 18:08 TPE 外部讀回：PR #92 OPEN/DRAFT，HEAD abc322e30e2bebd772e638daf4e6b7ae14c7b01a；這只有 GitHub 候選證據，**不是 OS 主機、排程或人類正式接受的現況**。
- R07 S12 主機收據觀察時間為 2026-10-21 16:14 TPE：在該時間點，沒有可驗證活躍 Writer；OpenCode service PID 45628 只是 service；18 個 WINWORD Automation 程序用途 UNKNOWN；BUILD_QUEUE 最後寫入 10/19，115 筆 PENDING 而沒有明示 READY。**不可把這些歷史 PID/數量填作現在 LIVE**。
- R07 0099 R17 的 DOCX SHA-256 293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b，有有界技術、版面及抽文語意收據；仍為 SAMPLE/CANDIDATE，不是正式 REAL。0097 R08 Word→PDF 停滯只封鎖 0097 渲染車道。
- 2026-10-03 的 AGENTS.md HOTFIX、2026-10-04 的 TTQS_HANDOFF/CURRENT_STATE.json 仍記載舊式 Antigravity 優先、OpenCode 停用及過期 10/05 截止日。它們是 HISTORICAL，不得覆蓋 10/17 §5 允許 OpenCode v2 CLI 與 10/21 R08 GOAL 規格。若本機 control plane 仍以舊值阻擋最新已批准可逆候選工作，標 SPEC_CONTROL_PLANE_REBASE_REQUIRED；**不得默默改寫舊史，也不能用舊規格自行新增 Human Gate**。
- **嚴禁拿別案監控面板冒充本案面板**：PT-Original-Point/ptysd-autonomous-factory 的 operator-panel/index.html 讀 Issue #407 與 PTYSD_OPERATOR_OBSERVATION_V1，host = DESKTOP-1B6PD2P / Win11；2026-10-13 的觀察已過期。這與本案 Windows 10 的 desktop-vmv4q60/j、GitHub PR #92 不同。它不提供本案主機同步驗收。只唯讀核對身分，不修改另一個專案。
- **三種權威須分離**：Windows OS/CLI 原生讀回 = 主機正在執行的真相；GitHub PR #92 + 實際 raw bytes = 可供跨 Session 稽核的遠端候選真相；監控面板 = 呈現層，只有當它的來源、snapshot、時間與這兩者對上才算同步，永遠不能自行產生正式接受。

### 6.1 第 1 階段：Windows 唯讀現場盤點（禁止先修改或派工）

在 Windows 同一執行帳戶內先讀回 username、hostname、Windows 版本、現行日期與時區、E:\TTQS 是否存在、Codex GOAL、作業系統排程、真正 PID/command line、Git 本機 HEAD、既有未同步成果及外部未結效果。最短 PowerShell 示例（**唯讀**）：

~~~powershell
$ErrorActionPreference = 'Stop'
$now = Get-Date
Write-Output "OBSERVED_LOCAL=$($now.ToString('o'))"
Write-Output "HOST=$env:COMPUTERNAME"
whoami
Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,LastBootUpTime
foreach ($p in @('E:\TTQS\TTQS_ONE_CODEX_RUNTIME','E:\TTQS\_github_sync_0064')) {
  [pscustomobject]@{ Path=$p; Exists=(Test-Path -LiteralPath $p) }
}
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -match '^(WINWORD|opencode-cli|agy|node|python|powershell|pwsh|Codex)\.exe$' } |
  Select-Object ProcessId,ParentProcessId,CreationDate,Name,CommandLine |
  Format-List
Get-ScheduledTask -ErrorAction SilentlyContinue |
  Where-Object { $_.TaskName -match 'TTQS|Codex' } |
  Select-Object TaskName,TaskPath,State,Triggers,Actions,Principal
~~~

- 如果需要查目前 Repo，本機已知 clone 候選路徑 E:\TTQS\_github_sync_0064 **僅作定位候選**。先檢查 .git、git remote -v、git status --porcelain=v1、git branch --show-current、git rev-parse HEAD，確認 repo identity 和 exact branch，不能對錯 clone 推送。
- 對 Windows 程序：同名、PID、process alive、service alive、GOAL active、排程 enabled 均非「真的正在寫 DOCX」。要把 PID 與 work_id、輸入 SHA、output location、該程序命令列、最後實際產物變更、相符 session/attempt 對起來；無法關聯則 ACTIVE_WRITER=UNKNOWN，不可標 RUNNING_VERIFIED。
- 任何尚未完成、未知結果或外部寫入狀態先同來源讀回，確認沒有雙主，**不能因新命令就重派相同 doc_id/revision**。18 個用途不明的 Word COM 程序不得全部 Kill；先以 parent、操作檔案、渲染 owner/時間與對應 log 局部定位。
- GOAL 顯示 paused 時，先讀官方原生 GOAL 狀態／原因；辨識是舊 queue 無 READY、已達平台限制、真正 Human Gate、目標自然結束、工具審批或排程同 thread 互鎖。不得以「看到 paused」即清空 GOAL、刪除歷史或重設執行緒。

**第 1 階段輸出**：OBSERVED_AT, HOST, USER, RUNTIME_PATH, LOCAL_REPO_ID, LOCAL_HEAD, REMOTE_HEAD, OS_GOAL_STATE+REASON, ACTIVE_WRITER+WORK_ID 或 UNKNOWN, UNRESOLVED_EFFECTS, SCHEDULER_OWNER+ID, QUEUE_MTIME。若少任何值保留 UNKNOWN，不填 0。

### 6.2 第 2 階段：辨識 Windows 10「真正的」TTQS 監控面板

1. **先定位既有面板**：找桌面捷徑實際 Target、打開的 localhost URL 或本機 HTML、伺服器程序 PID/command line、工作目錄、面板配置與資料來源路徑；用原生 Get-CimInstance、Get-NetTCPConnection -State Listen 與既有檔案索引。不得大範圍讀取使用者無關目錄，不得因找不到就新建 dashboard/service/DB/監督程序。
2. 判斷畫面 PROJECT_ID、repo/ref、PR/Issue、host、data_source、last_observed_at、last_published_at、expires_at、refresh interval。若對到 PTYSD / Issue #407 或其他 host，標 PANEL_PROJECT_MISMATCH，**不得用作 TTQS 對帳**。若完全找不到 TTQS 原有面板，標 PANEL_EXISTENCE=UNKNOWN/NOT_FOUND_ON_TESTED_PATHS，不冒稱已部署。
3. 不以 Windows 桌面截圖上的「正在運作」「最近更新」「綠燈」直接認定 Worker live。若現有面板只有 cached JSON、單一 GitHub 讀值、靜態 HTML 或超過自身 TTL 的 snapshot，必須標 STALE 或 UNKNOWN；不得補零、猜最後運作時間或製造假 PASS。
4. 若發現既有 TTQS 合格面板，修**既有資料接線**使其只讀相同 OS + PR #92 有來源的現況；禁止新增第二套面板／Supervisor／Quota DB／事件匯流排。若實體面板在另一專案，這個 R09 僅要求提出 TTQS 專用相容讀取策略及需另授權的跨案變更，**不得擅改另一專案程式或將它升格 TTQS 權威**。
5. 來源與秘密保護：不可把 Google/OAuth token、session cookie、Windows private env、模型 API key、學員真實個資或憑證上傳 GitHub 或面板；只公開白名單欄位與必要 hash/時間/狀態，PID/本機路徑如有敏感資訊需按原有政策遮罩。

**必查**：PANEL_URL_OR_PATH, PANEL_PROJECT_ID, PANEL_HOST_ID, PANEL_SOURCE_REF, PANEL_LAST_OBSERVED, PANEL_TTL, PANEL_LIVE_STATUS, PANEL_SOURCE_ISSUE_OR_PR。未取得實際面板來源，PANEL_GITHUB_ALIGNMENT=UNKNOWN，不能 PASS。

### 6.3 第 3 階段：OS ↔ GitHub ↔ 面板三方精確對帳（不建立新的狀態權威）

用**同一輪有時戳的觀測**，對以下欄位逐一列 LOCAL_OS / REMOTE_GITHUB / PANEL / MATCH / EVIDENCE：

- project_id + Windows host/user（不能混 PTYSD）、repo/ref/PR 與 GitHub HEAD；
- GOAL 真實 active/paused 及原因；排程 task_id、mode、interval=120m、last_run、next_run、最近三次 run 的 native receipt；
- 已接受的現在進行 work_id/doc_id/requirement_id/Blueprint SHA，source source_hash；
- Worker（Codex dispatcher、OpenCode v2、Antigravity CLI）每條路由的 PID/session、attempt、model requested、actual serving model 或 UNKNOWN、最後工具活動、完整輸出/錯誤；
- candidate DOCX exact SHA-256、Word/PDF 頁數、QA scope 與 verdict、SAMPLE/REAL、未結返工及局部阻擋；
- 本機未推送的穩定工件、GitHub 遠端已推送／讀回 hash、PR 最新提交時刻；
- 各來源 observed_at / published_at / expires_at／來源 API 是否讀不到及 timeout。

**狀態語意**：OS 已有活躍 Worker 而尚未產出穩定工件時，不把 GitHub 舊 HEAD 當作「同步失敗」，要顯示 REMOTE_STABLE_BEHIND_ACTIVE_WORK；若成果已穩定且 scope 已批准卻未推送，標 SYNC_PENDING。遠端有新 SHA 但面板仍顯示舊 SHA，標 PANEL_STALE_NEEDS_REFRESH。若面板只顯示「Green」但缺 exact work/receipt，標 UNVERIFIED_DISPLAY。

**通過規則**：有至少一筆真實 material delta（工件、QA、同步或明確故障），OS 原生收據、相應 GitHub remote bytes 和面板三方取到同 work_id + exact SHA + 對應時間；之後再做一次面板刷新，確認「已完成」「RUNNING」「BLOCKED」不把歷史狀態與現況混淆。無面板原生讀回時最多 PARTIAL，**絕不寫 ALL_SYNC=PASS**。

### 6.4 第 4 階段：先解除 GOAL 自鎖，再把唯一排程改每兩小時

按照 docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md 與 05_HOURLY_NATIVE_WAKE_RESUME.md **最上層 2026-10-21 ACTIVE 覆寫**執行。

1. 原生讀取現有 Codex App Scheduled task：task_id、thread_id、project/workdir、執行模式、enabled、prompt 完整保存內容、60 分鐘舊設定、last/next、最近三次 run，並查 Windows Task Scheduler 所有 TTQS 同類任務。禁止直接寫 App 私有 JSON/DB，也不可虛構 UI/CLI 所沒有的原生欄位。
2. 先鎖定**唯一有權接觸真正 E:\TTQS 工件的派工 Owner**；若舊每小時同 thread 排程只能向 paused GOAL 發文字訊息，SCHEDULE_TRIGGER=PASS / REAL_RESUME=FAIL，不可再繼續刷無 READY 的報告。
3. 若唯一舊任務支援直接在相同安全本機 Context 施工，**只修改原任務**為 120 分鐘；若只支援特定間隔則使用經原生支援的 UI/規則（例如 RRULE:FREQ=HOURLY;INTERVAL=2）；以原生來源讀回間隔、執行帳戶及 next run。**不保留第二個同作用 enabled 派工排程**。
4. 若 thread-bound Scheduled 的根本限制使之不能繼續本機施工，先安全停用舊任務並 readback，再檢驗同專案 standalone local mode 是否能讀本機 E:\TTQS。若仍不能且既有 Windows Task Scheduler 有受信任現役 Worker 入口，重用其原生 L0 觸發器做唯一每 120 分鐘低成本觀察，必要才啟動合格 Codex CLI/Worker。不得盲目復活過期的 TTQS_ONE_Codex_Supervisor 或另一專案 PTYSD 的排程。
5. 真正需要**無變化 0 次高階模型**時，應讓 Windows Task Scheduler / Git / OS 原生 L0 先檢查 material delta；不能宣稱 Codex App 每次 Scheduled 觸發必然 0 Token。
6. 在解開 stale queue 自鎖後，原生 GOAL 確認可由 /goal resume 恢復原工作時，先查是否仍有活躍相同 Worker 與未結 side effects，再恢復；不 /goal clear、不重設整條歷史。若 paused 有真正安全／身份／正式驗收 Gate，只停該範圍，不能假解鎖。
7. **驗收**分三層：NATIVE_120M_SETTING_PASS（原生讀回）；SCHEDULE_TRIGGER_PASS（真實定時到點，不是 UI 卡片）；AUTONOMOUS_CONTINUATION_PASS（觸發後真的有合法 SOURCE/BLUEPRINT/WORD/QA 增量與 GitHub 精確 readback，或精確獨立 blocker 且其他 READY 沒被誤停）。只手動 Run now 不能代替自然定時觸發。

### 6.5 第 5 階段：嚴格從需求重算逐階段 READY，禁止 NO_READY 循環自鎖

每次先讀本案當前 Human Mission、官方 TTQS PDF、第 157 核取項目矩陣、已接受任務、crosswalk、每份唯一 Blueprint、候選 SHA、QA、OS Writer。**不以舊 BUILD_QUEUE.json 有沒有 READY 字串決定全部停工**。

逐階段導出：
READY_SOURCE_PACKET → READY_UNIQUE_BLUEPRINT → READY_WRITER → READY_DETERMINISTIC_QA → READY_FRESH_SEMANTIC_REVIEW → READY_BOUNDED_REPAIR → CANDIDATE_PUBLISHED。

具體救援範例：
- 0100、0101 綁定 I18-E08（專案 157 索引 109，2 個不同文類），必須先 fresh-read 是否已有新工件及是否活躍 Writer，避免重派。
- 0100 是 8 人前後自評表：有可實際操作欄位、日期、前後測、分母、方法及 SAMPLE 完整填寫示範。
- 0101 是能力提升雷達分析報告：**真的具有五個維度可重算數據／雷達圖，結論、限制及改善方案**；不能把 0100 換標題當作 0101。
- 0099 R17 已驗證 SAMPLE 8×5×2=80 評分格、總分前75／後117／總增42／人均增5.25、示範 6/8 達標，若引用此案例，source facts ID、量表定義、得分方向、軸範圍與兩文件都要精確一致，不能暗加第二組資料。
- 無 REAL 第三方原件時，仍可製作誠實、完整的 SAMPLE／SYNTHETIC 候選及原件索取清冊，**不得偽造第三方信函、安檢證明、簽章、就業成效或保險憑證**；正式升格維持 Human Gate。

每份工件只在下一階段真正前置資料缺失時封鎖那一階段。例如 0097 R08 PDF export 失敗，只封鎖該候選 visual lane，不能把 0100 來源整理、0101 Blueprint 也判 NO_READY。

### 6.6 第 6 階段：雙 Worker 的精確「派工→回收」協定

**僅使用現有原生 OpenCode v2 CLI 與 Antigravity CLI 作 AI 外包。Codex 負責調度、仲裁、既有 Windows/Python/Word 原生工具及 GitHub 同步；不可用 Computer Use 或假扮兩個 Worker 的其他 harness。**

#### A. 派工前

- Worker 任務須有唯一 work_id、doc_id、requirement_id、正式來源定位與 SHA、專屬 Blueprint SHA、SAMPLE/REAL 界線、所需共用合成事實 snapshot、負向鄰項、工作角色（WRITER 或 REVIEWER）、禁止的外部效果、輸出格式、QA 接受條件及單一輸出目標。
- 真正確認 OS 沒有相同 work_id/相同寫入範圍仍活躍的 Writer，沒有 PENDING_OR_UNKNOWN side effect；若未知只停受影響寫入路由，其它獨立 READY 照做。
- OpenCode v2：先由當次原生模型型錄、免費額度、模型實際合法可用性讀回，選有實際證據不新增費用的免費 SKU。型錄有列、名稱有 free、舊每日報告推薦、exit 0 **均非真正可用或免費的充分證據**。
- Antigravity CLI：唯一准請求 gemini-3.8-flash-high；限定純文字輸入輸出，禁止 Computer Use、檔案工具讀寫、dangerously-skip-permissions、無聲切換至 CCPA 或其他模型。2026-10-20 Human GUI/CLI 的 Google AI Pro 帳戶與配額相符只是該時點觀察，不證明此次 CLI 子程序繼承相同憑證或供應端使用 Gemini；若偵測 fallback，不能宣稱指定模型 PASS。模型身分/帳務無原生證據寫 UNKNOWN。
- 優先短、小、專屬輸入包：只附此文件所需官方段落、事實、唯一 Blueprint、計算、已知缺陷；禁止把 12MB 報告、88 筆 commit、所有 157 項、重複完整回覆輸入模型。
- 每個 Worker 的精確 CLI 參數先從本機已安裝版本 --help / 現存成功腳本讀取；**不抄無法解析的舊參數**。同一路由無新修正/材料變化不得反覆空轉測試。

#### B. 派工與執行

- 只派**一次**受信任的 exact work/owner/attempt；於既有暫存工作目錄保存模型輸入摘要與原生 stdout/stderr／程序 exit。不能把 model request accepted 當作完成；不能因面板顯示 RUNNING 就另開同文件 Writer。
- 無法取得 runtime model identity 時保留 UNKNOWN；若 Antigravity fallback 或 429/no-route/timeout/permission denied，記「哪個車道／哪個 exact attempt」，不要停全部、不要危險權限繞過。
- Writer 交付的「完整內容」需有明確可解析結構與真實文稿/表格內容，不是只回應「完成」、「PASS」、「已建立」或在私人 Temp 留草稿。對 CLI exit 非 0 但已有穩定部分產物，先做原生檢查能否 salvage，不先重建。

#### C. 回收（必須逐件收據）

每個 attempt 回收至少：
work_id、owner、doc_id、attempt_id、started_at、ended_at、CLI version、requested_model、actual_serving_model 或 UNKNOWN、exit_code、timeout、stdout_bytes、stderr_bytes、raw stdout/stderr SHA、prompt/packet SHA、真正文字/文件輸出路徑及 SHA、是否用於下一件 DOCX、Token input/output/reasoning/cache（只有原生確有的才填）、計費（UNKNOWN 若無 provider invoice）、缺陷定位與下一單一步驟。

- **僅在完整回覆已被取回、解析／必要公式檢查成功、對應同 work/SHA、文件真實存在、指定 QA 完成時**可標 USEFUL_DELIVERABLE；exit 0 或 PASS 自報不足。
- WRITER 與獨立 REVIEWER 不能是同一個實質撰稿上下文；審查模型如只看抽取文字必須標 TEXT_ONLY_PASS，不可提升成看過 DOCX/圖像或人類已接受。
- 同一根因最多先核對已有失敗＋已採用的材料變更；§5 的三次錯誤／三次修正上限只對確實同一路由錯誤適用，不准為湊次數再造三次高 Token 故障；達停派條件只 pause 該 lane。沒新原生證據就直接暫停和走其他 READY。
- 返工只交修補差異：字級／頁碼／定位／雜湊用 Python/Word deterministic 工具；文字誤解才派便宜 CLI；相同 DOCX exact SHA 已有相同範圍 reviewer PASS 則不再完整重審。
- Codex 不可代替 Worker 寫完整正文再冒稱外包成功；若確需 Codex 接管為例外，記成本與理由，保留獨立審查。

### 6.7 第 7 階段：人類可用完整 Word 的品質 Gate（不犧牲品質換 Token）

由現有原生工具與不同撰稿者完成以下必要檢查，對 exact bytes 綁定：
1. 需求對應：唯一 157 核取項目身分、官方 PDF 實際頁次與原文，若編號是專案自編就明標 INTERNAL_INDEX，不能說官方 PDF 印製序號。
2. 專屬性：課程／問卷／會議／流程／評量／統計等文類有真正差異；通用 Blueprint、換標題相同正文、近鄰需求誤套皆 FAIL。進行標題盲測與負向近鄰識別。
3. 協會適用：第一頁以國中程度繁中說清楚誰、何時、做什麼、填什麼、去哪找資料、結果如何用；有完整可直接操作的示範、行政人員最短路徑與常見錯誤處理。AI 代理盲測只能稱代理檢查，**不能冒稱實際國中生/人類試讀完成**。
4. SAMPLE 完整：每一個合成數據、人物、金額、時間、課程、問卷、統計、事件及結果須可重算、相互一致且標 SAMPLE/SYNTHETIC 並有 REAL replacement register。除清楚標記 REAL 待替換區外，不得保留大面積待填、待核、空白表、空答案。
5. 真實性：第三方正式文件／簽署／政府證明未有原件時，提供索取流程與示範，絕不做偽造正式文件；REAL、正式 TTQS 升格仍需 Human/真實來源。
6. Word 正文與內部工程證據分離：正文禁止內部 SHA、GitHub 路徑、Blueprint JSONL、engine metadata 佔版；工程側錄單獨保留，不得刪除可追溯性。
7. OOXML 開啟、公式重算、中文字級（正文 ≥10.5pt、表格 ≥9.5pt）、A4版面、表格跨頁、孤立段落/空白頁、必要時 Word→PDF 全頁檢視；縮圖概覽不等於 reviewer 全尺寸目視。
8. 若只有 Word COM 匯出工具故障，固定該 DOCX SHA，先查對應 renderer owner、必要有限恢復；不為修工具重寫 Word，也不讓該故障阻止其他文件來源與撰稿。
9. 獨立 reviewer 的 PASS 要註明 exact SHA、輸入文字/圖像範圍、未驗證項目、非阻擋觀察與返工 scope。Reviewer 自報 PASS、prompt 要求回填五個 SHA 皆不能替代本機自己重算實際 bytes。
10. CURRENT 表示符合專案當時候選品質控制的可讀成果，不是 REAL／政府認證／協會正式接受；PR Draft、GitHub 對帳 PASS 不會改變此界線。

### 6.8 第 8 階段：遠端 GitHub exact-SHA 同來源發布與回讀

- 只有已有授權且真正穩定之候選、必要 QA 與原始 Worker 收據才進 PR #92 既有分支；不同文件有獨立 work scope；先 Git/GitHub HEAD + git status 看現場 pending，**不 force push、不混入不相關檔案、外部效果未知不盲重送**。
- Git Blob SHA（Git 物件 SHA-1）與 DOCX 檔案 SHA-256 是**不同演算法**，必須各自核對；PR status、commit 存在、exit 0 不表示 Word bytes 相同。
- 對已 fetch 回來的 exact remote ref 與本機 DOCX，用 Python **byte-safe** 的 subprocess 直接取得 Git blob raw bytes，再兩邊算 SHA-256；避免 PowerShell 文字重導向破壞 binary：

~~~python
from pathlib import Path
import hashlib, subprocess
repo = Path(r"E:\TTQS\_github_sync_0064")  # 僅候選：先驗證 remote identity
relative = "docs/ttqs-quality-20261016/quality-review/0099_R17_20261021/candidate/0099_R17.docx"
branch = "work/ttqs-one-document-quality-contract-20261016"
local_file = repo / relative
local_sha = hashlib.sha256(local_file.read_bytes()).hexdigest()
remote_bytes = subprocess.run(
    ["git", "-C", str(repo), "show", f"refs/remotes/origin/{branch}:{relative}"],
    capture_output=True, check=True
).stdout
remote_sha = hashlib.sha256(remote_bytes).hexdigest()
print({"local_sha256":local_sha, "remote_sha256":remote_sha, "MATCH":local_sha==remote_sha})
~~~

**執行此範例前**須以現行 repo、真實 relative path、正確 remote ref 並先 fetch，不能盲用上面的示例檔名／clone 或將示例結果冒充全部檔案驗收。對 manifest/QA/JSONL 要按其實際 raw bytes 或明確宣告的是解析後等價；Git 自動正規化換行時依實際產品政策處理，不能改寫原始 Worker 失敗收據。
- 發布後 fresh-read GitHub 同分支 HEAD、目標 blob/raw bytes、reviewer bound SHA、receipts、SAMPLE register 與必要文件索引；未驗證變更不能標 REMOTE_CONFIRMED。
- 若推送成功而回讀超時/UNKNOWN，只封鎖該 shared push lane 並重新讀回，不重複無條件 push；純本機獨立 READY 工作不陪停。

### 6.9 第 9 階段：每兩小時只做必要恢復，不重寫報告

**每一個合法排程觸發**按固定順序：
L0 原生 OS/GUI task trigger readback → 一次有界 Git fetch/HEAD + local status + PID/attempt/work_id + stable SHA 比對 → 回收上次未確認 Worker/end effects → 重新導出 Stage READY → 無 material delta、無 READY/new failure 則 silent no-op → 有 READY 則派一個 exact scope 或回收正在執行工作 → deterministic QA → 必要 reviewer → GitHub readback → 同源面板更新。

- 不在每次兩小時生成活動報告、長檔、Context compact 全史、逐分鐘 heartbeat、成本估算幻想、第二控制面。
- L0 無 material delta 的目標是**0 次高階模型**，前提是真由 Windows 原生 L0 觸發；Codex App Scheduled 自動傳訊可能已耗模型額度，不得自報絕對零 Token。
- 每次失敗只留下最短精確原因、哪個 lane、OS/provider 收據、下一個不同於前一回合的修復動作。不允許「暫無 READY → GOAL 已暫停 → 永不讀新來源」循環。
- 實際正在做的 0100／0101 或其他 doc_id 工作須在下次兩小時觀測前後保持同 owner；不能因 session compaction、排程或 GitHub 討論留言重派第二 Writer。
- 每兩小時清點既有免費模型狀況前先看已有失敗收據；沒有材料變化不得為查免費額度再花模型 Token。Codex 本體 Token 花在真正仲裁與未知重大品質，不花在長篇報告。

### 6.10 第 10 階段：24 小時兩個 Worker 的實際績效與成本稽核

直接從 Windows CLI 原生日誌、session、process、stdout/stderr、GitHub PR #92 收據重建**滑動過去 24 小時**的 attempt 明細表，欄位：
attempt_id / task_id / doc_id / worker / role / requested_model / actual_model_verified_or_UNKNOWN / start/end / input/ output/ reasoning/ cache_tokens_or_UNKNOWN / CLI exit / status / material_delta / adopted_in_DOCX / docx_sha / reviewer_sha / return_repair_round / model_error / raw_receipt / GitHub blob。

只計算資料完整且口徑一致的：
- dispatched attempts、實際有可用文字稿數、真正納入候選 DOCX 數、獨立審查覆蓋率、首次正確交付率、缺陷返工輪數、重複無效重試數、平均等待時間、每個可靠成果的模型使用量；
- OpenCode 與 Antigravity 各自成功與失敗原因，尤其 Antigravity 文字路由未派／fallback／無 Gemini 身分的真實數量，不因 CLI 回過字就算 Gemini Writer 已恢復；
- Codex GPT 自身輸入／輸出／快取 Token 必須有原生用量來源；不能拿 OpenCode reported tokens 冒充 Codex 費用。沒有 provider invoice 的費用 UNKNOWN，不能用 model 名稱推免費總額；
- 若近 24h 沒有某模型呼叫，要區分 NOT_DISPATCHED、ROUTE_PAUSED、AUTH_BLOCKED、quota、NO_READY、OS_TASK_NOT_TRIGGERED，不能只報 0 後聲稱省成本；
- 0099 R17 歷史 OpenCode session 顯示 input=108009、output=4753、reasoning=298；僅是個別審查的原生收據，**不是全日用量或計費帳單**。應在下一次真正可比的同類品質工作縮小輸入包，再在不降低內容驗收下比較效率。
- 將成本與返工資料收斂為既有 receipt 的短彙總，不另建持久 Quota DB/代理交易日誌；如 24h 來源完整性不夠，仍以 available sample + UNKNOWN 分母說明，**不虛構整體成功率**。

### 6.11 第 11 階段：反例測試（不得靠模型自報 PASS）

以下至少 14 項要用既有真實事故收據或便宜的 deterministic 模擬驗證，不准刻意重放大量模型請求：

T01｜OpenCode service PID alive、沒有 work_id/活躍 session → ACTIVE_WRITER 不得 PASS。  
T02｜18 個 WINWORD AutoEmbedding 但未知文件 owner → 不得全殺或稱 18 Writer。  
T03｜GitHub 新 HEAD、面板仍顯示舊 HEAD → PANEL_STALE；不冒充對齊。  
T04｜面板指向 PTYSD Issue407 / DESKTOP-1B6PD2P → PANEL_PROJECT_MISMATCH，不能作 TTQS 證據。  
T05｜原生排程啟用但只把訊息送入 paused GOAL → TRIGGER_PASS/WORK_RESUME_FAIL。  
T06｜BUILD_QUEUE 115 PENDING 無 READY 字串，但 0100/0101 合法來源可以準備 → READY_SOURCE_PACKET，不能停工。  
T07｜0097 PDF 匯出 180 秒失敗 → 只停渲染 lane，0100/0101 照做。  
T08｜Worker exit=0、但沒有文字或 DOCX → DELIVERABLE_FAIL。  
T09｜exit 非 0、但已有完整穩定 DOCX 與可檢驗收據 → 先 bounded salvage，不能盲重建。  
T10｜reviewer 說 PASS 但 SHA 是舊版或未自己讀 DOCX → 綁定失敗或僅 TEXT_ONLY。  
T11｜Antigravity 要求 Gemini 但 fallback 至 CCPA → GEMINI_ROUTE_NOT_VERIFIED，不能算 Gemini quota 使用。  
T12｜合成 Word 有空白問卷、內部 SHA、官方證明偽造或正文換標題 → 品質 FAIL，不能靠 technical PASS 升格。  
T13｜GitHub blob SHA 一致但本機 DOCX SHA-256 不相等 → 遠端候選完整性 FAIL；禁止改用不同演算法比對混過。  
T14｜一個未知 push 結果／另一個 Writer 正在工作 → 只暫停該寫入並讀回，不雙主、不全案停。  

**任何測試失敗必須附 exact locator、受影響範圍與修補行動。** 只建立文件／測試表，沒有 OS、provider 讀回不能自稱 T01–T14 已在 Windows 通過。

### 6.12 第 12 階段：正式验收分級與最短交付

分三層交付，不可互相冒充：

- **GITHUB_CONTROL_UPDATED=PASS**：只證明本節內容保存在 PR #92 GitHub 同來源，有對應 commit/blob readback。
- **WINDOWS_HOST_PANEL_ALIGNED=PASS**：必須有真實 Win10 面板來源和 OS readback、相同 project/host/head/work_id/doc SHA、來源 freshness、不混 PTYSD、不讓舊快照冒稱現在；沒有本機面板 live 讀回就 UNKNOWN/PARTIAL。
- **AUTONOMOUS_GOAL_WORK_RESUMED=PASS**：唯一 120m 原生 scheduler 已讀回設定與自然定時 run，該 run 真的回收/派發合法工作並留下新源包、Blueprint、Word 或 QA 的材料變化及 GitHub exact-SHA 遠端讀回；某獨立 lane blocked 不阻其他。

最後不得超過一頁（必要證據改指向已存在檔案），固定回報：

~~~text
PROJECT_ID=TTQS_ONE
REPORT_SCOPE=R09_OS_HOST_GITHUB_PANEL_WORKER_2H
OBSERVED_AT_TPE=
HUMAN_SPEC=2026-10-21 R09 / CANDIDATE
CANONICAL_SPEC=UNKNOWN_OR_VERIFIED_REF
GITHUB_PR=92
GITHUB_BRANCH=
REMOTE_HEAD_SHA=
WINDOWS_HOST_ID=
WINDOWS_USER=
OS_GOAL_STATE_AND_PAUSE_REASON=
ACTIVE_WORKER_OWNER_AND_WORK_ID=
SCHEDULER_ID_AND_OWNER=
SCHEDULE_INTERVAL=120m|NOT_APPLIED|UNKNOWN
NATIVE_LAST_RUN=
NATIVE_NEXT_RUN=
ACTUAL_2H_TRIGGER=PASS|FAIL|NOT_TESTED
OS_RESUME_ARTIFACT_SHA=
OPEN_CODE_24H_ATTEMPTS=VERIFIED_COUNT|UNKNOWN
ANTIGRAVITY_24H_ATTEMPTS=VERIFIED_COUNT|UNKNOWN
WORKER_RETURNED_ADOPTED_AND_REWORK=
CODEX_TOKEN_COST=VERIFIED_VALUE|UNKNOWN
PANEL_PATH_OR_URL=
PANEL_PROJECT_AND_HOST=
PANEL_LAST_OBSERVED_AT=
PANEL_DATA_SOURCE=
PANEL_OS_GITHUB_ALIGNMENT=PASS|PARTIAL|FAIL|UNKNOWN
READY_SOURCE_BLUEPRINT_OR_DOCX=
BLOCKED_SCOPE=
REAL_THIRD_PARTY_EVIDENCE=UNKNOWN_UNTIL_RECEIVED
HUMAN_FORMAL_ACCEPTANCE=NOT_GRANTED
GITHUB_REMOTE_ARTIFACT_READBACK=SHA_AND_LOCATOR|UNKNOWN
UNRESOLVED_EXTERNAL_EFFECTS=
NEXT_SINGLE_LEGAL_ACTION=
TRUE_HUMAN_GATE=NONE|EXACT_REASON
~~~

**完成條件**：立刻開始一項已授權且 OS 確實 READY 的可逆工作，先把結果回收到既有 GitHub；同步修現有排程及面板讀數。只有需真人 OAuth/MFA、身份、法律／契約、Production、新費用、重大不可逆權限或無法釐清重大外部效果才找 Human。沒有面板就如實報 NOT_FOUND_ON_TESTED_PATHS／UNKNOWN，不能為了回答 Human 建新服務。

**極簡復工驗收情境**：在 Win10 真正核對沒有相同 Writer 後，使用 0100/0101 其中一個 READY_SOURCE_PACKET 完成來源/唯一 Blueprint，存 source SHA → QA → GitHub 遠端 raw bytes 對帳 → 現役面板相同 HEAD/來源時戳 readback；下一次**真實 120 分鐘觸發**確認任務是延續而非重來。完成之前不得宣稱整個自動施工恢復正常。
