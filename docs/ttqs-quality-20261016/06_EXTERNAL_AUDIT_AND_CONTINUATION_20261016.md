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
