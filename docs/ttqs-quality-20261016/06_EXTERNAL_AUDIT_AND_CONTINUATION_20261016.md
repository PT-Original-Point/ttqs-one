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
