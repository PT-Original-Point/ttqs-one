# 0064 R06 semantic review evidence packet

Candidate DOCX SHA-256: `f83eeda42589da66c23918d522ad983178a252da9b6dd2240b725e9c9cfb50a1`
Source commit: `ac9a13e394fcb25414d69a6f538f95c700cc26c9`
The complete candidate body extraction is attached separately as `candidate_text_R06.txt`. Source file hashes are also recorded in `input_manifest_R06.json`.

## Official source, page 5
- File: `official_source_page5.txt`
- SHA-256: `bf25836d48bf22ab7ddc25f43d6d31b4fb9b2ef838426f009517683e8eced3fc`

                 內涵說明（以下為        常見參考佐證資料
  項目    評核指標項目    例，但不以此為      （並註明資料來源及頁碼）
                     限）
                 進訓練成果轉移的     業主提供回訓或相關機制、學
                 達成並展現適當資      習心得交流的平台、證照、實
                 料說明。          習或其他相關機制的建議或協
                               助，展現訓練成果轉移的達成
                               並展現連接性執行。
                              其他：
                              訓練資料與訓練過程及成果的
                 展現訓練流程相關      紀錄與分類，均有系統化歸納
        14.訓練資料分 文件有適當系統化      方法編碼。
          類與建檔   紀錄，並有分析及     訓練檔案管理系統。
          及管理資   運用紀錄。        完整的訓練文件建檔資料。
          訊系統化   對訓練流程相關文     是否提供查詢功能，並具持續
                 件或紀錄有適當的      改善機制。
                 保存及建檔。       資訊系統化程度及檢索速度。
                              其他：
                             訓後定期性綜合檢討或管理審查
                 展現定期的課後檢討    制度會議紀錄。
                 紀錄及適當的審查檢   訓練的結案報告，包括資源的運
       15.評估報告及  討改善機制。       用、財務的支配、訓練成果的展
         定期性綜合課後檢討紀錄應展現       現、檢討及改進的方法。
         分析      學員建議及回饋、訓   訓練執行評估指標分析及相關統
                 練需求、訓練目標、    計分析。
                 訓練方法等之檢討。   訓後改善建議追蹤報告。
                             其他：
  查核             展現整體訓練過程    訓練流程的管控方法及紀錄。
（Review）         中，有持續管控且符   訓練異常處理方法、紀錄與工
                 合程序要求，並彙整    具。
                 結果進行定期（年    訓練的內外稽核流程與紀錄。
       16.管控及異常  度）審查。       其他：
         矯正處理    建立適當的程序辦
                 法，訓練流程異常
                 時，應有紀錄及因應
                 措施，必要時採取適
                 當矯正措施防止再
                 發。
                 0分 未執行。     課後滿意度調查分析與課後檢討
                 1分 執行滿意度調    講師、學員、人資、部門主管等
       17.訓練  17a 查。          利益關係人的建議回饋紀錄。
  成果   成果評估反應    2分 依滿意度調查分  課程結案報告（含問卷調查統計
（Outcome） 的多元性評估 析，學員/講師回     分析、課程規劃紀錄等含對後續
       和完整性      饋，彙整分析作為下    課程的開課建議事項）。
                 次課程規劃之修正依   依反應評估進行課程改善的行動
                 據。           方案。

                       5


## Unique Blueprint R02
- File: `0064_UNIQUE_BLUEPRINT_R02.md`
- SHA-256: `0f521debdaeeef17f2c47d11cccbb193e2a4b0f8370bf4dd56da86d512c0f3d8`

# DOCX 0064 唯一 Blueprint R02

## 資訊系統化程度及檢索速度_完整工作稿

> 本檔是可直接派發給下一位 Writer 的施工藍圖。Writer 依本 Blueprint 產生 DOCX 正文即可，**不得**自行改寫需求或省略表格。本 Blueprint 本身是 sidecar（規格書），DOCX 正文不得出現 SHA、sidecar 路徑、內部控制碼。

---

## 0. 文件控制與來源界線

| 項目 | 值 |
|---|---|
| PROJECT_ID | TTQS_ONE |
| DOCX | 0064 |
| 官方需求 | I14-E05（指標14，第5項內涵） |
| 官方方框流水號 | 069 |
| 預定題名 | 資訊系統化程度及檢索速度_完整工作稿 |
| 文件文類 | 短測試報告 ＋ 可複製低成本「檢索速度測試程序（SOP）」 |
| 版本 | R02 |
| 狀態 | 可逆 SAMPLE/SYNTHETIC 候選施工；**不是**協會真實績效、**不是**正式接受 |
| Blueprint 唯一輸出 | inputs/0064_UNIQUE_BLUEPRINT_R02.md |
| Writer 目標模型 | opencode/deepseek-v4.1-flash-free（OpenCode v2 CLI，實測 v2.0.29；報告提及 v2.0.32 未升級，不宣稱已升級） |
| 費用記錄 | 若本次執行回報實際費用→原樣保存；否則記 provider billing **UNKNOWN** |
| 產生物 | 僅一份 DOCX 正文 ＋ build receipt；**不得**建立/修改其他 DOCX，**不得**修改本封包 |

**唯一 SAMPLE 測試情境（鎖定，不可混用 ID）**

- Training case：**SYN-0060-2026-A01**（課程「社區志工接待與資源轉介界線」，日期 2026-08-15，報名12、到課10、缺席2）。此 case 只在跨件連結區出現，本文件不重做其分類/編碼。
- 本文件 benchmark ID：**SYN-0064-BENCH-2026-01**。與 SYN-0060-2026-A01 **不可混為同一 ID**。
- 測試語料：封閉採用 0062 R04 的 12 個 SAMPLE artifact_id／假路徑；不是由 0064 新建、不是實體檔案、不是協會系統。
- 測試操作員：2 位匿名合成操作員 **A / B**。
- 觀測總量：2 人 × 12 任務 × 2 模式 = **24 對、48 個計時觀測**。
- 環境：合成設定（Windows 11 Pro、16 GB RAM、SSD、本機 Excel 索引、離線 SAMPLE_ROOT 資料夾）——**不是**協會現有設備。

**SAMPLE/REAL 界線（全篇適用）**

- 所有工時、操作員、環境、版本、路徑、統計值皆為 SAMPLE/SYNTHETIC，須逐項登錄（見 §13）。
- **不得**寫成協會真實系統已運作、已改善、已通過官方評分。
- **不得**把 67.9% 或任何數字稱為「協會實際績效提升」；只能稱「本示範情境下之差異」。

---

## 1. 首頁導讀（30 秒看懂）— 內容規定

首頁導讀**必須**是一個資訊密集的「30 秒摘要區」，不得是空泛導讀頁。Writer 依下表逐格填寫，每格 1–2 句。

| 導讀欄位 | 必須寫明的內容 |
|---|---|
| 這份文件是什麼 | 一份「檢索效率短測試報告」＋可複製的「低成本檢索速度測試程序」，用於回答方框 069 「資訊系統化程度及檢索速度」。 |
| 對應官方方框 | 官方需求 I14-E05／官方方框流水號 069；原文提示「系統化與檢索速度：明確測試環境、時間、統計」。 |
| 誰會讀 | 評核委員（抽查可重現性）、承辦/行政志工（照 SOP 重做）、資訊窗口（確認環境與權限）。 |
| 測試了什麼 | 固定 12 筆封閉語料、2 位操作員、兩種檢索模式（階層資料夾瀏覽 vs 欄位索引查找），比較找回「正確記錄與處理狀態」所需時間與正確率。 |
| 關鍵數字（SAMPLE） | 資料夾法 mean 101.75 秒／中位 95.5／P90 137／正確率 91.7%；索引法 mean 32.625 秒／中位 28.5／P90 47／正確率 100%；配對平均節省 69.125 秒/任務；總時間減少 67.9%。 |
| SAMPLE 界線 | 以上全部為合成示範值；環境與人員為假設值；正式採用前須由協會填入真實設備、索引版本、權限與測試日。 |
| 結論在哪 | 結論見 §10；重測程序見 §11；退件/保留條件見 §12、§16。 |
| 一句話結論 | 在本示範情境與示範門檻下，索引法滿足四項示範門檻；資料夾法未達正確率與時限門檻；索引法仍有一筆慢任務（B/T08，62 秒）須報告與追查。 |

> 版面：首頁導讀放最前，唯讀者 30 秒可掌握「用途／方框／讀者／界線／結論位置」。

---

## 2. 官方題意與文件文類

**官方內涵（須原文引用官方佐證表 PDF 第5頁第14項）**：訓練流程文件應適當系統化記錄、分析及運用。該項 5 個方框中，**第 5 個方框原文**為：

> 「資訊系統化程度及檢索速度。」

**方框 069 專屬提示**：「系統化與檢索速度：明確測試環境、時間、統計。」

**本文件文類定位**

1. **短測試報告**：呈現一次可重現的檢索效率測試，含條件、任務、原始資料、統計、限制、結論。
2. **可複製的低成本檢索速度測試程序（SOP）**：讓協會能用同一方法在自己的真實語料上重測。
3. **限制聲明（必須寫）**：本文件**不**聲稱任何真實系統已建置或已運作；**不**評估 0061 的權限/備份設計；**不**重做 0063 的查詢改善；**不**複製 0062 的完整建檔清冊。

**文類禁區（出現即退件）**

- 不得寫成 0061 的權限/備份手冊。
- 不得寫成 0062 的完整建檔清冊。
- 不得寫成 0063 的查詢服務改善報告。
- 不得只給空白表單或純標題。

---

## 3. 鄰近方框差異表（0061–0064 分工）

Writer 必須產出下表（跨件連結欄需指名可引用的 SAMPLE 事實 ID）。

| 方框/需求 | 文件 | 各自證據目的 | 0064 不重複的內容 | 跨件連結（可引用事實） |
|---|---|---|---|---|
| 066 / I14-E02 | 0061 | 檔案管理系統及權限／備份／收件控制 | 0064 不做權限矩陣、備份策略、收件控制設計 | 引用同一 training case SYN-0060-2026-A01；引用 0061 示範索引 **F-0061-2026-0001** 僅作「索引存在」事實，**不得**寫成已建置實體系統或新增索引 |
| 067 / I14-E03 | 0062 | 訓練文件建檔清冊及定位 | 0064 不重做建檔清冊本體 | 使用 0062 R04 的 **12 個 SAMPLE artifact_id（A-0062-01…12）** 與假路徑作封閉語料；假路徑不是實體檔案；A-0062-08 為 HOLD |
| 068 / I14-E04 | 0063 | 查詢服務、失敗查詢與改善重測 | 0064 不重做 query-service 設計與改善日誌 | 0064 只比較「在指定資料集與程序下，找回正確記錄/狀態所需時間與正確率」；沿用 0063 的『失敗查詢須重測』精神，但不引用其改善日誌內容為本文件主體 |
| 069 / I14-E05 | 0064（本件） | 可重現的檢索效率測試：時間、命中/正確狀態、分布、限制 | —（本件主體） | 連結 SYN-0060-2026-A01、A-0062-01…12、H-0062-0001 |

**HOLD 專屬規定（必寫）**：0062 的 **A-0062-08** 評量彙整樣張目前 **HOLD**（來源日期/定位未核），**不得開啟、不得計為可用內容**。正確檢索回覆僅回傳 **artifact_id、HOLD 狀態及阻擋代碼 H-0062-0001**，不得揭露版本、檔名、路徑、評量內容或其他受限欄位。

**來源狀態與測試狀態必須分開**：0062 R04 DOCX §6 的 R1–R7、R9–R12 是合成樣本登錄，樣本版本為 V01、樣本狀態為 VERIFIED；R8/A-0062-08 樣本狀態為 HOLD。0062 R04 同節的 REAL 欄則明示 12 列的真實來源存在、真實定位及政策仍 UNKNOWN，REAL 狀態全部 HOLD。0064 只能把這些值稱為「0062 樣本登錄欄」，不能稱為協會真實文件狀態。0064 的計時、操作員、SYN-IDX-v1、測試資料及 HIT/NO_HIT 均為額外虛構測試夾具；不表示曾實際執行或已建置索引。

**SHA 存放規定**：上表與全篇 DOCX 正文**不得**出現任何 SHA-256；SHA 只留 sidecar（見 §14、§16）。

---

## 4. 封閉語料清單（12 項）

規則：
- 語料只限 0062 R04 DOCX §6 清冊的 12 個 `artifact_id`；不得新增第 13 筆。
- 0062 R04 的 `SAMPLE_ROOT` 與列出的檔名/路徑都是虛構標籤，實體檔案不存在。本測試只計時讀取合成清冊的 metadata，不開啟任何檔案。
- `V01`、`VERIFIED` 是 0062 R04 **樣本登錄欄**；不代表 REAL 欄。0062 R04 明示所有 12 列的 REAL 存在/定位/政策未核，REAL 狀態均 HOLD。
- 0064 的檢索結果欄位採三種明確區隔：`retrieval_outcome=HIT / NO_HIT / HOLD` 是本示範的檢索結果；`sample_record_status=VERIFIED / HOLD` 是 0062 的樣本登錄狀態；`real_evidence_status=HOLD` 是 0062 的真實證據狀態。禁止使用 `SAMPLE record=VERIFIED / REAL evidence=HOLD` 取代任何一種狀態。
- A-0062-08 對查詢者只回 `artifact_id + HOLD + H-0062-0001`；不顯示版本、檔名、路徑或內容。

| 任務 | artifact_id | 類型代碼 | 0062 R04 樣本版本/樣本狀態 | 0062 R04 REAL 狀態 | 0064 測試回覆界線 |
|---|---|---|---|---|---|
| T01 | A-0062-01 | NEE | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T02 | A-0062-02 | NAN | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T03 | A-0062-03 | PLN | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T04 | A-0062-04 | LSN | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T05 | A-0062-05 | RSC | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T06 | A-0062-06 | ATT | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T07 | A-0062-07 | DLG | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T08 | A-0062-08 | ASM | 不揭露 / HOLD | HOLD（存在、定位、政策 UNKNOWN） | 僅回 ID、HOLD、H-0062-0001；禁止版本/檔名/路徑/內容 |
| T09 | A-0062-09 | FDB | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T10 | A-0062-10 | FUP | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T11 | A-0062-11 | EXC | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |
| T12 | A-0062-12 | IMP | V01 / VERIFIED | HOLD（存在、定位、政策 UNKNOWN） | 回傳 ID、V01、VERIFIED、REAL-HOLD；路徑僅為假標籤 |

**命中正確性**：非 T08 任務須同時回對 artifact_id、樣本版本、樣本登錄狀態與 REAL-HOLD，才記 `HIT`；找不到或任一欄錯誤記 `NO_HIT/錯誤`，仍保留在分母。T08 只以 ID、HOLD 與阻擋碼判正確；HOLD 安全回覆不是錯誤。

**類型代碼工作性展開（SAMPLE，需回讀 0062 R04 確認；本表不得當成官方定義）**

| 代碼 | 工作性展開（僅供施工理解） | 備註 |
|---|---|---|
| NEE | 需求評估類 | SAMPLE 解讀 |
| NAN | 需求分析類 | SAMPLE 解讀 |
| PLN | 訓練計畫類 | SAMPLE 解讀 |
| LSN | 教案／課程設計類 | SAMPLE 解讀 |
| RSC | 資源清單類 | SAMPLE 解讀 |
| ATT | 出席/簽到類 | SAMPLE 解讀 |
| DLG | 溝通/會議紀錄類 | SAMPLE 解讀 |
| ASM | 評量彙整樣張 | **錨定**：封包明示 A-0062-08=評量彙整樣張；本件為 HOLD |
| FDB | 回饋類 | SAMPLE 解讀 |
| FUP | 後續追蹤類 | SAMPLE 解讀 |
| EXC | 例外/異常處理類 | SAMPLE 解讀 |
| IMP | 改善紀錄類 | SAMPLE 解讀 |

> Writer 注意：不得把上表「工作性展開」寫成官方定義；DOCX 正文須標「類型代碼以 0062 建檔清冊為準，展開為本文件 SAMPLE 解讀」。

---

## 5. 可重現測試條件表（填寫示範）

Writer 必須產出完整「測試條件表」，逐列填示範值，並標明每列「正式採用前替換來源」。

| # | 條件項 | 示範設定（SAMPLE/SYNTHETIC） | 正式替換來源 |
|---|---|---|---|
| 1 | 裝置 | Windows 11 Pro 合成環境 | 協會實際電腦規格（Human/資訊窗口） |
| 2 | 記憶體 | 16 GB RAM | 實機規格 |
| 3 | 儲存 | SSD | 實機規格 |
| 4 | 索引檔案 | 本機 Excel 索引檔，版本 **SYN-IDX-v1** | 實機索引版本與檔名 |
| 5 | 網路狀態 | 離線 | 實測網路狀態 |
| 6 | 資料根目錄 | `SAMPLE_ROOT/`（**假路徑**，檔案不存在） | 真實資料源路徑 |
| 7 | 操作員數 | 2 位（匿名合成 A、B） | 實際受測人數 |
| 8 | 完成順序 | A：先 folder 後 index；B：先 index 後 folder | 實際順序設計 |
| 9 | 練習 | 每位操作員於各模式前做 1 次非計分練習（不同假 ID） | 實際練習設計 |
| 10 | 清除前次快取 | 每次模式切換前清除瀏覽/索引快取 | 實際清除方式 |
| 11 | 中間休息 | 兩模式之間休息 **10 分鐘** | 實際休息安排 |
| 12 | 計時起點 | 操作員讀完標準任務文字、主持人說「開始」 | 實際起點定義 |
| 13 | 計時終點 | 正確 artifact_id、SAMPLE 版本/狀態及 REAL-HOLD 同時顯示即停止；A-0062-08 僅回 ID、HOLD 與阻擋碼，**不開啟資料** | 實際終點定義 |
| 14 | 查無資料停止規則 | 最多等 **180 秒**才停止；失敗任務**仍納入統計**（不得從分母刪除） | 實際規則 |
| 15 | 時間精度 | 秒（整數秒） | 實際精度 |
| 16 | 示範測試日 | 2026-10-17（SAMPLE 情境日期；**未實測**） | 協會實測日期及原始紀錄 |

> 明文禁區：**不得**為了讓數字好看而允許「只取快例」、**不得**在失敗時把該任務自 n 中刪除。

---

## 6. 12 張標準任務卡

規則：每張卡固定欄位＝任務文字／查詢條件／預期 artifact_id／預期版本／預期狀態／不得揭露欄位／特殊規則。所有卡一致，唯 T08 測安全 HOLD。

**共同查詢條件定義**
- 模式 A（階層資料夾瀏覽）：僅用 SAMPLE_ROOT 目錄階層，不使用欄位索引。
- 模式 B（欄位索引查找）：使用本機 Excel 索引，以 artifact_id／類型／版本／狀態欄查得 locator 與狀態。
- 兩模式皆須回報：artifact_id、SAMPLE版本/狀態及REAL佐證狀態全部一致。

**共同不得揭露欄位**：文件內容欄（僅允許顯示 artifact_id／版本／狀態等 metadata）。T08 例外：**全部內容欄**皆不得揭露，只回 HOLD 狀態與 H-0062-0001。

---

**T01**
- 對應：A-0062-01（NEE）
- 任務文字：「在封閉語料中，找到 A-0062-01 的記錄，回報其 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄逐層瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-01｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：僅回 metadata。

**T02**
- 對應：A-0062-02（NAN）
- 任務文字：「找到 A-0062-02 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-02｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T03**
- 對應：A-0062-03（PLN）
- 任務文字：「找到 A-0062-03 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-03｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T04**
- 對應：A-0062-04（LSN）
- 任務文字：「找到 A-0062-04 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-04｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T05**
- 對應：A-0062-05（RSC）
- 任務文字：「找到 A-0062-05 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-05｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T06**
- 對應：A-0062-06（ATT）
- 任務文字：「找到 A-0062-06 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-06｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T07**
- 對應：A-0062-07（DLG）
- 任務文字：「找到 A-0062-07 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-07｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T08（安全 HOLD 測試）**
- 對應：A-0062-08（ASM，評量彙整樣張，HOLD）
- 任務文字：「找到 A-0062-08 的記錄，回報其處理狀態；若為受限狀態，回報阻擋代碼，**不得開啟內容**。」
- 查詢條件：folder＝依類型目錄瀏覽至該項；index＝以 artifact_id 欄查找狀態欄。
- 預期 artifact_id：A-0062-08｜預期版本：**不揭露**｜預期狀態：**HOLD / H-0062-0001**
- 不得揭露欄位：**全部內容欄**（評量內容一律不公開）
- 特殊規則：達標＝回傳 HOLD 與 H-0062-0001 並停止；若開啟或洩漏內容＝安全失敗（見 §12）。

**T09**
- 對應：A-0062-09（FDB）
- 任務文字：「找到 A-0062-09 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-09｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T10**
- 對應：A-0062-10（FUP）
- 任務文字：「找到 A-0062-10 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-10｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：單一任務無時限加成，但整體受 180 秒停止規則約束（示範中 A/T10 folder 為 NO_HIT）。

**T11**
- 對應：A-0062-11（EXC）
- 任務文字：「找到 A-0062-11 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-11｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

**T12**
- 對應：A-0062-12（IMP）
- 任務文字：「找到 A-0062-12 的記錄，回報 artifact_id、版本與處理狀態。」
- 查詢條件：folder＝依類型目錄瀏覽；index＝以 artifact_id 欄查找。
- 預期 artifact_id：A-0062-12｜預期版本：V01（0062 R04 SAMPLE 版本）｜預期 SAMPLE 狀態：VERIFIED；預期 REAL 佐證狀態：HOLD
- 不得揭露欄位：內容欄｜特殊規則：無。

---

## 7. 原始資料表（完整 24 對計時值）

格式：操作員／任務／資料夾秒／資料夾結果／索引秒／索引結果（＋本 Blueprint 附加之「配對節省秒」＝資料夾秒−索引秒，供 §8 交叉核對）。**HOLD 列與 NO_HIT 列須醒目標記**（粗體＋底色或外框）。

| # | 操作員 | 任務 | 資料夾秒 | 資料夾結果 | 索引秒 | 索引結果 | 節省秒（derived） |
|---|---|---|---|---|---|---|---|
| 1 | A | T01 | 92 | HIT | 28 | HIT | 64 |
| 2 | A | T02 | 81 | HIT | 22 | HIT | 59 |
| 3 | A | T03 | 115 | HIT | 34 | HIT | 81 |
| 4 | A | T04 | 68 | HIT | 19 | HIT | 49 |
| 5 | A | T05 | 76 | HIT | 25 | HIT | 51 |
| 6 | A | T06 | 130 | HIT | 43 | HIT | 87 |
| 7 | A | T07 | 88 | HIT | 23 | HIT | 65 |
| 8 | A | T08 | 142 | **HOLD** | 58 | **HOLD** | 84 |
| 9 | A | T09 | 95 | HIT | 31 | HIT | 64 |
| 10 | A | T10 | 104 | **NO_HIT** | 27 | HIT | 77 |
| 11 | A | T11 | 121 | HIT | 38 | HIT | 83 |
| 12 | A | T12 | 72 | HIT | 21 | HIT | 51 |
| 13 | B | T01 | 104 | HIT | 32 | HIT | 72 |
| 14 | B | T02 | 90 | **NO_HIT** | 25 | HIT | 65 |
| 15 | B | T03 | 128 | HIT | 39 | HIT | 89 |
| 16 | B | T04 | 74 | HIT | 23 | HIT | 51 |
| 17 | B | T05 | 84 | HIT | 29 | HIT | 55 |
| 18 | B | T06 | 118 | HIT | 47 | HIT | 71 |
| 19 | B | T07 | 102 | HIT | 27 | HIT | 75 |
| 20 | B | T08 | 156 | **HOLD** | 62 | **HOLD** | 94 |
| 21 | B | T09 | 89 | HIT | 28 | HIT | 61 |
| 22 | B | T10 | 96 | HIT | 33 | HIT | 63 |
| 23 | B | T11 | 137 | HIT | 45 | HIT | 92 |
| 24 | B | T12 | 80 | HIT | 24 | HIT | 56 |

**結果標記說明（必寫）**
- **T08／A-0062-08 為 HOLD**：資料夾法 2 次、索引法 2 次都只回傳 HOLD，**不得打開樣張**。HOLD 是**預期正確結果**（安全達標），不是失敗。
- **NO_HIT 僅出現在資料夾法**：A/T10 與 B/T02 為 NO_HIT（未於 180 秒內命中）。
- **HIT 定義**：artifact_id、0062 樣本版本/樣本狀態與 REAL-HOLD 符合預期；**不代表檔案存在、真實資料可用或本測試真的執行過**。T08 依 HOLD 安全回覆專則判定。

**核對線索**：所有「節省秒」相加應等於 1659＝2442−783（見 §8）。

---

## 8. 結果分析表（含公式與排序位置）

**統計規則（須原文寫進 DOCX，讓委員可重算）**
- n = 24 pairs；每一模式各自 n = 24。
- Mean = sum(秒) / 24。
- Median = 偶數樣本慣用中位數＝排序後第 12、13 位之平均。
- P90 = nearest-rank：rank = ceil(0.90 × n) = ceil(21.6) = **第 22 位**排序值。
- Max 獨立另列（不與 P90 混用）。
- 全部任務（含 NO_HIT 與預期安全 HOLD）**均納入**時間與正確率分母；HOLD 可是正確安全回覆，不等於命中失敗。

**8.1 主分析表**

| 統計量 | 資料夾法（folder） | 索引法（index） | 說明／排序位置 |
|---|---|---|---|
| n | 24 | 24 | 配對數相同 |
| 總秒數 sum | 2442 | 783 | 由 24 列加總 |
| Mean | 101.75 秒 | 32.625 秒 | sum/24 |
| Median | 95.5 秒 | 28.5 秒 | folder 第12/13位＝95、96；index 第12/13位＝28、29 |
| P90（nearest-rank, rank 22） | 137 秒 | 47 秒 | folder 排序第22位＝137；index 排序第22位＝47 |
| Max | 156 秒 | 62 秒 | folder max 出現在 B/T08；index max 出現在 B/T08 |
| 正確率（ID＋SAMPLE版本/狀態＋REAL-HOLD；T08按ID/HOLD/碼） | 22/24 = **91.7%** | 24/24 = **100%** | folder 未達者＝A/T10、B/T02（NO_HIT） |
| 安全揭露違規次數 | 0 | 0 | T08 兩模式皆未開啟內容 |

**8.2 配對節省與總量減少**

| 指標 | 公式 | 值 |
|---|---|---|
| 配對平均節省 | (folder mean − index mean) = 101.75 − 32.625 | **69.125 秒/任務** |
| 總時間減少率 | (2442 − 783) / 2442 = 1659 / 2442 | **0.679361… = 67.9361% → 67.9%** |

> 禁語：**不得**把上述差異稱為「協會實際績效增益」或「系統實際效能提升」。只可稱「本示範情境之差異」。

**8.3 分布補充（次要統計，供「分布」要求；SAMPLE-derived，須可重算）**

| 指標 | 資料夾法 | 索引法 |
|---|---|---|
| A 平均 | 1184/12 = 98.67 秒 | 369/12 = 30.75 秒 |
| B 平均 | 1258/12 = 104.83 秒 | 414/12 = 34.5 秒 |
| 最慢任務 | T08（A 142 / B 156） | T08（A 58 / B 62） |
| 最快任務 | T04（A 68） | T04（A 19） |
| 秒數全距 max−min | 156−68 = 88 秒 | 62−19 = 43 秒 |

> 若 §8.3 有任一數值與重算不符，Writer 必須先修正再送審；不得保留不符的數字。

---

## 9. 時間比較圖（一張，簡潔）

Writer 產生**一張**直觀圖，重點呈現三統計量：

- 圖型：群組長條圖（grouped bar）。
- 類別（X 軸）：Mean／Median／P90。
- 數列（Legend）：資料夾法（folder）／索引法（index）——**建議只用兩色**。
- 資料值：
  - Mean：folder 101.75，index 32.625
  - Median：folder 95.5，index 28.5
  - P90：folder 137，index 47
- 標籤：顯示資料標籤（秒）；Y 軸標題「秒（秒數越低越好）」。
- 必須標註：圖標題含「SAMPLE/SYNTHETIC」，圖說「本圖為合成示範值，非協會真實績效」；圖說引用 §7 為資料來源。
- 24 列原始值**不得**壓縮成圖而省略文字表；圖是輔助，§7 文字表必須並存且字級不縮。

---

## 10. 結論（限縮於示範情境）

**10.1 判讀（須逐句寫）**
- 在本示範情境與示範門檻下（見 10.3），**索引法**滿足四項示範門檻；**資料夾法**未達正確率（91.7% < 100%）與時限（中位 95.5 > 30、P90 137 > 60）門檻。
- 索引法**仍有一筆慢任務 B/T08 = 62 秒**，須報告並追查；平均值或任一快例**不得**掩蓋單筆慢任務或錯誤狀態/權限。
- 所有差異僅為 SAMPLE；**不得**推論協會已有成效。

**10.2 最小改善建議（不超過 4 項）**
1. 為 A-0062-08 等 HOLD 項建立一致的狀態阻擋與回報流程，避免誤開內容。
2. 針對索引法慢例（如 B/T08）建立「慢任務清單」，於測試後個別檢視（同時保留原始資料）。
3. 為資料夾法 NO_HIT 個案建立命中率改善紀錄與重測機制（沿用 0063 的失敗查詢重測精神）。
4. 正式採用前，填入真實設備/索引版本/權限/測試日，並以同一程序重測一次作為 REAL 候選。

**10.3 示範驗收門檻（明文標示：非官方 TTQS 評分門檻，僅本示範用）**

| 準則 | 門檻 | 資料夾法 | 索引法 |
|---|---|---|---|
| 精確符合預期 ID＋SAMPLE版本/狀態＋REAL-HOLD（T08例外） | 100% | 91.7% ✗ | 100% ✓ |
| 未授權揭露 | 0 次 | 0 ✓ | 0 ✓ |
| 中位時間 | ≤ 30 秒 | 95.5 ✗ | 28.5 ✓ |
| P90（nearest-rank） | ≤ 60 秒 | 137 ✗ | 47 ✓ |

> 索引法四項皆達；資料夾法僅「零未授權揭露」達標。門檻是**示範用**，不是官方評分標準。

---

## 11. 實際採用的重測 SOP 與可複製空白記錄表

**11.1 重測 SOP（步驟，供協會照做）**

1. **授權與範圍**：取得合法測試授權；確認個資/權限邊界；圈定封閉語料集（原始 12 筆或替代集）。
2. **登錄環境**：填入實際裝置、RAM、儲存、索引檔版本、網路狀態、資料根目錄。
3. **登錄人員與順序**：填入受測人數、先後完成順序、練習方式、休息時間。
4. **定義起訖與停止**：明列計時起點（讀完任務文字＋主持人說開始）、終點（ID、SAMPLE版本/狀態、REAL狀態同時顯示；T08僅ID/HOLD/阻擋碼）、HOLD 停止規則、180 秒無資料停止規則。
5. **逐任務計時**：每任務記錄資料夾秒/結果、索引秒/結果；失敗任務保留、不刪。
6. **安全檢核**：受限項（HOLD）只回狀態與阻擋代碼；不得開啟內容。
7. **計算**：依 §8 公式重算 mean/median/P90(rank 22)/max/正確率/節省。
8. **錯誤處置**：任一錯誤結果須登記、分類（命中失敗/狀態錯誤/安全違規）、決定重測或保留。
9. **複核**：由第二人複核原始秒數與計算。
10. **重測**：對失敗/慢任務排定重測，並保留第一次原始資料。

**11.2 可複製空白記錄表（Writer 提供空白版）**

| 欄位 | 填寫說明 |
|---|---|
| benchmark ID / 示範測試日 | 示範日期需標 SAMPLE；實測後另記真實日期與原始證據 |
| 操作員代號 / 功能角色 | 去識別代號；合成示例不得寫成真實人員 |
| 任務編號 / 0062 清冊列 | T01–T12 與 R1–R12 一對一 |
| 方法 | folder / index，逐次記錄 |
| 開始/結束時間與耗時 | 原始時刻及整數秒；不得只留平均值 |
| retrieval outcome | HIT / NO_HIT / HOLD / ERROR；不得與樣本狀態混用 |
| 回報 artifact_id / SAMPLE 版本 | A-0062 ID；T08 版本固定不揭露 |
| SAMPLE 登錄狀態 | VERIFIED / HOLD；T08 僅狀態回覆 |
| REAL 佐證狀態 | 依 0062 R04 全列 HOLD；只有實際核實後才可改列並附來源 |
| 回報定位標籤 | SAMPLE 假路徑標籤；不得宣稱實體檔案存在 |
| 是否正確 / 錯誤分類 | 是/否；命中失敗、欄位錯誤、狀態錯誤、安全違規或其他 |
| 備註 | 偏差、停止、HOLD 代碼；禁止放個資或受限內容 |

**11.3 填寫示例（均為虛構記錄，未實測）**

| 日期 | 操作員/角色 | 任務/方法 | 開始→結束 | 秒 | 結果 | 回報值 | 正確性/備註 |
|---|---|---|---|---:|---|---|---|
| 2026-10-17（SAMPLE） | A／合成查找員 | T08 / folder | 00:00:00→00:02:22 | 142 | HOLD | A-0062-08；版本不揭露；HOLD/H-0062-0001；未開啟 | 是；安全停止 |
| 2026-10-17（SAMPLE） | A／合成查找員 | T10 / folder | 00:00:00→00:01:44 | 104 | NO_HIT | 未回報目標欄位 | 否；失敗例保留分母 |
| 2026-10-17（SAMPLE） | A／合成查找員 | T01 / index | 00:00:00→00:00:28 | 28 | HIT | A-0062-01；V01；SAMPLE=VERIFIED；REAL=HOLD | 是；路徑僅為假標籤 |

> 所有示範日期、操作員、時間、方法與結果都是 SYNTHETIC，沒有實際受測者或實際檢索事件。正式採用須由協會按空白表實測並保留原始記錄。

## 12. 可執行 HOLD / REJECT 標準

任一情形成立即處置如下（Writer 須把本表完整寫入 DOCX）：

| # | 觸發條件 | 判定 | 處置 |
|---|---|---|---|
| 1 | 無合法測試授權 | HOLD | 停止測試，取得授權後重啟；不得先做後補 |
| 2 | 個資/權限未確認 | HOLD | 暫停；確認權限與個資範圍後再測 |
| 3 | 測試語料無法定位 | HOLD/REJECT | 若語料集不成立→REJECT 重建語料；若個別項→HOLD 該項並記錄 |
| 4 | 時鐘/計時方法不一致 | REJECT | 重新定義起訖並重測；不一致之觀測不得計入統計 |
| 5 | 只取快例、剔除慢例或失敗例 | REJECT | 還原完整 24 對資料重算；不得自分母刪除失敗任務 |
| 6 | 把 HOLD 項打開或公開評量內容 | REJECT（安全失敗） | 立即停止、標記安全違規、不得計為達標；追查並重測 |
| 7 | 缺原始時間記錄 | HOLD | 補齊原始秒數與結果後方可分析 |
| 8 | 數學不符（mean/median/P90/max/百分比與原始值不符） | HOLD | 依 §8 公式修正後再送審 |
| 9 | 將 SAMPLE 寫成 REAL（宣稱協會已有成效） | REJECT | 更正文件為 SAMPLE；不得以此升格 |
| 10 | 未經獨立 reviewer 精確綁定 candidate SHA | HOLD | 不得升格 CURRENT；送獨立語意審查 |

> 通則：**平均值或任一快例不得掩蓋錯誤狀態/權限或單筆慢任務**。

---

## 13. Synthetic Replacement Register（完整、逐列可追溯）

**13.1 欄位和資料界線**

Register 至少記載：benchmark ID、SAMPLE 情境日期、操作員代號與合成功能角色、任務/0062 清冊列、folder 與 index 的原始秒數及結果、預期記錄碼、SAMPLE/REAL 狀態分欄、0062 R04 精確來源列、虛構路徑標籤、REAL 替換來源、功能責任角色與升格前必要證據。所有計時和操作紀錄為合成資料，並非實際測試紀錄。

**13.2 固定示範條件**

- Benchmark ID：`SYN-0064-BENCH-2026-01`。
- 示範日期：`2026-10-17`（SAMPLE 情境日期；沒有實測，不得稱為測試完成日）。
- 合成操作員 A、B：功能角色均為「義工/訓練行政查找員（SYNTHETIC）」，無真實姓名或人事任命。
- 環境：Windows 11 Pro、16 GB RAM、SSD、離線、虛構 `SAMPLE_ROOT`、虛構 Excel 索引 `SYN-IDX-v1`；不得宣稱原始點協會已使用該環境或索引。
- 觀測：12 任務 × 2 操作員 × 2 方法＝24 對、48 個合成秒數；無任何真實操作事件。
- 任務範圍：只查 0062 R04 樣本清冊 metadata；不開啟或讀取假路徑指向的文件。
- 固定 REAL 狀態：0062 R04 的 12 列均為 REAL-HOLD；樣本 VERIFIED 不改變 REAL 狀態。

**13.3 逐次計時值（完整 24 對；每列均有日期、角色、來源列與結果）**

| Trial ID | SAMPLE日期 | 操作員/合成功能角色 | 任務 / 0062來源列 | folder 秒 / 結果 | index 秒 / 結果 | 預期資料碼 | 資料性質 |
|---|---|---|---|---|---|---|---|
| SYN-0064-A-T01 | 2026-10-17（SAMPLE） | A / 合成查找員 | T01 / R1 | 92 / HIT | 28 / HIT | M01 | 未實測・SYNTHETIC |
| SYN-0064-A-T02 | 2026-10-17（SAMPLE） | A / 合成查找員 | T02 / R2 | 81 / HIT | 22 / HIT | M02 | 未實測・SYNTHETIC |
| SYN-0064-A-T03 | 2026-10-17（SAMPLE） | A / 合成查找員 | T03 / R3 | 115 / HIT | 34 / HIT | M03 | 未實測・SYNTHETIC |
| SYN-0064-A-T04 | 2026-10-17（SAMPLE） | A / 合成查找員 | T04 / R4 | 68 / HIT | 19 / HIT | M04 | 未實測・SYNTHETIC |
| SYN-0064-A-T05 | 2026-10-17（SAMPLE） | A / 合成查找員 | T05 / R5 | 76 / HIT | 25 / HIT | M05 | 未實測・SYNTHETIC |
| SYN-0064-A-T06 | 2026-10-17（SAMPLE） | A / 合成查找員 | T06 / R6 | 130 / HIT | 43 / HIT | M06 | 未實測・SYNTHETIC |
| SYN-0064-A-T07 | 2026-10-17（SAMPLE） | A / 合成查找員 | T07 / R7 | 88 / HIT | 23 / HIT | M07 | 未實測・SYNTHETIC |
| SYN-0064-A-T08 | 2026-10-17（SAMPLE） | A / 合成查找員 | T08 / R8 | 142 / HOLD | 58 / HOLD | M08 | 未實測・SYNTHETIC |
| SYN-0064-A-T09 | 2026-10-17（SAMPLE） | A / 合成查找員 | T09 / R9 | 95 / HIT | 31 / HIT | M09 | 未實測・SYNTHETIC |
| SYN-0064-A-T10 | 2026-10-17（SAMPLE） | A / 合成查找員 | T10 / R10 | 104 / NO_HIT | 27 / HIT | M10 | 未實測・SYNTHETIC |
| SYN-0064-A-T11 | 2026-10-17（SAMPLE） | A / 合成查找員 | T11 / R11 | 121 / HIT | 38 / HIT | M11 | 未實測・SYNTHETIC |
| SYN-0064-A-T12 | 2026-10-17（SAMPLE） | A / 合成查找員 | T12 / R12 | 72 / HIT | 21 / HIT | M12 | 未實測・SYNTHETIC |
| SYN-0064-B-T01 | 2026-10-17（SAMPLE） | B / 合成查找員 | T01 / R1 | 104 / HIT | 32 / HIT | M01 | 未實測・SYNTHETIC |
| SYN-0064-B-T02 | 2026-10-17（SAMPLE） | B / 合成查找員 | T02 / R2 | 90 / NO_HIT | 25 / HIT | M02 | 未實測・SYNTHETIC |
| SYN-0064-B-T03 | 2026-10-17（SAMPLE） | B / 合成查找員 | T03 / R3 | 128 / HIT | 39 / HIT | M03 | 未實測・SYNTHETIC |
| SYN-0064-B-T04 | 2026-10-17（SAMPLE） | B / 合成查找員 | T04 / R4 | 74 / HIT | 23 / HIT | M04 | 未實測・SYNTHETIC |
| SYN-0064-B-T05 | 2026-10-17（SAMPLE） | B / 合成查找員 | T05 / R5 | 84 / HIT | 29 / HIT | M05 | 未實測・SYNTHETIC |
| SYN-0064-B-T06 | 2026-10-17（SAMPLE） | B / 合成查找員 | T06 / R6 | 118 / HIT | 47 / HIT | M06 | 未實測・SYNTHETIC |
| SYN-0064-B-T07 | 2026-10-17（SAMPLE） | B / 合成查找員 | T07 / R7 | 102 / HIT | 27 / HIT | M07 | 未實測・SYNTHETIC |
| SYN-0064-B-T08 | 2026-10-17（SAMPLE） | B / 合成查找員 | T08 / R8 | 156 / HOLD | 62 / HOLD | M08 | 未實測・SYNTHETIC |
| SYN-0064-B-T09 | 2026-10-17（SAMPLE） | B / 合成查找員 | T09 / R9 | 89 / HIT | 28 / HIT | M09 | 未實測・SYNTHETIC |
| SYN-0064-B-T10 | 2026-10-17（SAMPLE） | B / 合成查找員 | T10 / R10 | 96 / HIT | 33 / HIT | M10 | 未實測・SYNTHETIC |
| SYN-0064-B-T11 | 2026-10-17（SAMPLE） | B / 合成查找員 | T11 / R11 | 137 / HIT | 45 / HIT | M11 | 未實測・SYNTHETIC |
| SYN-0064-B-T12 | 2026-10-17（SAMPLE） | B / 合成查找員 | T12 / R12 | 80 / HIT | 24 / HIT | M12 | 未實測・SYNTHETIC |


**13.4 樣本資料對照及逐列 REAL 替換清冊**

每列來源均為 `0062 R04.docx §6「樣本原件清冊」` 指定 R 列；該清冊列是 SAMPLE metadata，不證明實際檔案存在。A-0062-08 的版本、檔名與路徑不向查詢者揭露，以下只記保密規則，不重述其受限欄位。

| 資料碼 | 任務/ID | 精確樣本來源 | SAMPLE版本/狀態 | REAL狀態 | SAMPLE假路徑標籤（不得開檔） | REAL替換代碼 | 允許查詢回覆 |
|---|---|---|---|---|---|---|
| M01 | T01/A-0062-01 | 0062 R04.docx §6 / R1 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/NEE/SAMPLE__0062_NEE_需求來源樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M02 | T02/A-0062-02 | 0062 R04.docx §6 / R2 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/NAN/SAMPLE__0062_NAN_需求分析樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M03 | T03/A-0062-03 | 0062 R04.docx §6 / R3 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/PLN/SAMPLE__0062_PLN_訓練計畫樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M04 | T04/A-0062-04 | 0062 R04.docx §6 / R4 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/LSN/SAMPLE__0062_LSN_教案大綱樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M05 | T05/A-0062-05 | 0062 R04.docx §6 / R5 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/RSC/SAMPLE__0062_RSC_資源確認樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M06 | T06/A-0062-06 | 0062 R04.docx §6 / R6 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/ATT/SAMPLE__0062_ATT_簽到出席樣張.xlsx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M07 | T07/A-0062-07 | 0062 R04.docx §6 / R7 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/DLG/SAMPLE__0062_DLG_教學流程樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M08 | T08/A-0062-08 | 0062 R04.docx §6 / R8 | 不揭露 / HOLD | HOLD；存在、定位、政策 UNKNOWN | `不揭露（HOLD）` | REAL-SRC-E | ID + HOLD + H-0062-0001；不回版本/檔名/路徑/內容 |
| M09 | T09/A-0062-09 | 0062 R04.docx §6 / R9 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/FDB/SAMPLE__0062_FDB_學員回饋樣張.xlsx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M10 | T10/A-0062-10 | 0062 R04.docx §6 / R10 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/FUP/SAMPLE__0062_FUP_課後追蹤樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M11 | T11/A-0062-11 | 0062 R04.docx §6 / R11 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/EXC/SAMPLE__0062_EXC_分類異常樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |
| M12 | T12/A-0062-12 | 0062 R04.docx §6 / R12 | V01 / VERIFIED | HOLD；存在、定位、政策 UNKNOWN | `SAMPLE_ROOT/0062/SYN-0060-2026-A01/IMP/SAMPLE__0062_IMP_改善追蹤樣張.docx` | REAL-SRC-A+B+C+D | ID + V01 + SAMPLE=VERIFIED + REAL=HOLD；路徑只標為虛構 |



**13.5 REAL 替換來源代碼、責任角色與必要證據**

| 來源代碼 | 需要取得的真實資料 | 責任功能角色 | 升格前必要證據 |
|---|---|---|---|
| REAL-SRC-A | 經授權的現行清冊及 SAMPLE ID 對應 REAL ID | 訓練承辦＋資料權責人 | 核准的對照表、來源位置與逐列簽核/核對紀錄 |
| REAL-SRC-B | 原件實際存在性、可存取定位、文件版本；不得沿用 SAMPLE_ROOT | 資訊窗口＋資料權責人 | 權限核准、遮蔽後真實定位、存取測試與來源版本紀錄；A08 只驗 metadata，不開內容 |
| REAL-SRC-C | 實際設備、作業系統、索引檔/版本、網路與計時環境 | 資訊窗口 | 設備登錄、索引匯出或版本資訊、環境截圖/紀錄 |
| REAL-SRC-D | 實際操作日期、匿名受測者角色/同意、順序、逐筆原始秒數與結果 | 主持人＋訓練承辦 | 測試授權、匿名化原始記錄、完整 24 對資料、獨立重算與覆核 |
| REAL-SRC-E | A-0062-08 的有權來源日期、受限 metadata 定位、存取政策與 HOLD 處置 | 權責人＋資訊窗口 | 有權來源、日期/定位依據、權限決定、HOLD 解除書面證據；缺一項即保持 HOLD |

逐列對應：M01–M07、M09–M12 使用 REAL-SRC-A+B+C+D；M08/A-0062-08 使用 REAL-SRC-E。環境和測試整體仍須完成 REAL-SRC-C+D。沒有證據時不得把樣本值搬到 REAL 欄。

**13.6 衍生數值登錄（全部由上述 SYNTHETIC 原始值計算）**

| 指標 | folder | index | 推導/界線 |
|---|---:|---:|---|
| n / 秒數總和 | 24 / 2442 | 24 / 783 | 含預期安全 HOLD 與 NO_HIT 未命中例 |
| 平均秒數 | 101.75 | 32.625 | 算術平均 |
| 中位數 | 95.5 | 28.5 | n=24，排序第12與13值平均 |
| P90 | 137 | 47 | nearest-rank，ceil(0.9×24)=22，取第22值 |
| 最大值 | 156 | 62 | 不得以平均遮蔽慢例 |
| 正確率 | 22/24 = 91.7% | 24/24 = 100% | T08 安全 HOLD 算正確；NO_HIT 算錯誤 |
| A 操作員平均 | 98.67 | 30.75 | 1184/12；369/12 |
| B 操作員平均 | 104.83 | 34.5 | 1258/12；414/12 |
| 操作員平均差距 | 6.17 | 3.75 | B 平均減 A 平均，四捨五入至 2 位 |
| 範圍（max-min） | 88 | 43 | 156−68；62−19 |
| 配對平均節省 | — | 69.125 秒/任務 | 101.75−32.625；示範值 |
| 總時間減少率 | — | 67.9% | (2442−783)/2442=67.9361%；示範值 |
| 目標索引版本 | — | SYN-IDX-v1 | 合成測試夾具標籤；不是協會系統 |

> 以上是可重算的 SYNTHETIC 示範資料，不是協會測量結果。表中沒有一筆 REAL 計時或 REAL 成效；正式比較必須重新授權、實測並以原始資料重算。

## 14. 來源與跨件事實對照表

> 本表為 Blueprint sidecar。**DOCX 正文不得出現 SHA-256**，SHA 只留本 sidecar 或 build sidecar。

| 來源 file | section/table/item | 已核事實 | 使用位置（DOCX 節） | 狀態 |
|---|---|---|---|---|
| 01_HUMAN_MISSION_AND_ACCEPTANCE.md（SHA CE228E4B…C6E7） | Mission 與驗收 | 施工授權與驗收原則 | §0、§16 | 已核（sidecar） |
| 02_GENRE_WRITING_MANUAL.md（SHA 0F4183A1…E649） | 指標14 手冊 | 檢索速度須含試驗方法/條件/樣本/測次/結果；非實測標 SAMPLE | §2、§5、§8 | 已核（sidecar） |
| 03_157_CHECKBOX_BLUEPRINTS.md（SHA 7732C40F…A70A） | 方框 069 專屬提示 | 「系統化與檢索速度：明確測試環境、時間、統計」；須有特定來源定位/示範/決策結果/跨件連結 | §1、§2、§6 | 已核（sidecar） |
| 06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md（SHA 908C5BF3…5994） | 外包及同步契約 | 施工/審查/升格流程邊界 | §16 | 已核（sidecar） |
| 官方佐證表 PDF 第5頁（SHA 805386B7…4709） | 第14項第5方框 | 原文「資訊系統化程度及檢索速度。」 | §2 | 已核（sidecar） |
| REQUIREMENT_SOURCE_RECONCILIATION.csv（SHA FF6DE9F5…A2B9） | I14-E05 列 | doc_id 0064、標題「資訊系統化程度及檢索速度_完整工作稿」、count 1；**historical plan, not authoritative** | §0 | 僅序列/標題參考 |
| 0060 R08（SHA 92962DF7…B5C3） | — | training case SYN-0060-2026-A01、日期/人數 | §0、§3 | 跨件引用（不重做） |
| 0061 R03（SHA 3D4FE20F…8C9C） | — | 示範索引 F-0061-2026-0001 | §3 | 跨件引用（僅事實） |
| 0062 R04（SHA 460C4FCA…6D92） | DOCX §6 清冊 R1–R12 | 樣本版 V01、樣本狀態 VERIFIED 11/HOLD 1；12列 REAL 存在/定位/政策 UNKNOWN、REAL-HOLD；A08 阻擋碼 H-0062-0001 | §3、§4、§6、§7、§13 | 跨件語料來源，樣本與 REAL 狀態分欄 |
| 0063 R02（SHA B1E8210B…79F5） | — | 失敗查詢重測精神 | §3、§10 | 跨件精神引用 |

---

## 15. 寫作風格與 Word 版面

- **語言**：繁體中文；語氣行政、志工可懂。
- **字級**：正文 ≥ **10.5 pt**；表格 ≥ **9.5 pt**；**嚴禁**為縮頁數而縮字。
- **表格**：跨頁表格須**重複表頭**；同一表格不拆成孤頁（不孤頁）。
- **24 列原始資料**：**不得**縮小偷渡；須完整可讀。若跨頁，表頭重複並標「續」。
- **圖**：僅 §9 一張；須標 SAMPLE/SYNTHETIC。
- **頁數建議**：12–16 頁。
- **段落**：每節先結論後依據；避免空話；每個數字須有來源節可回查。
- **禁用語**：不得出現「待填／待核／空白表／保持空白／會後填寫」於**未標示的 REAL 替換區以外**（見 §16）。

---

## 16. 退件/保持候選條件與 exact SHA 驗收要求

**16.1 四類驗收分開（不得互相取代）**

| 類別 | 檢查內容 | 失敗後果 |
|---|---|---|
| 技術驗收（STATIC） | 字級門檻、表頭重複、無空表、無禁用語、數學可重算 | 未過→保持候選，回修 |
| 全頁視覺驗收 | 不孤頁、圖表可讀、24 列不縮 | 未過→保持候選，回修 |
| 跨文件驗收 | 與 0060–0063 分工清楚、無抄襲、負向鄰界成立、A-0062-08 未被開啟 | 未過→退件重建相關節 |
| 獨立語意驗收 | 由**新獨立 reviewer** 於**精確 candidate SHA** 上判定文類/可用性/評核面向 | 未過→HOLD，不得升格 CURRENT |

**16.2 硬性退件條件（任一即退件）**
- 出現空白表/純標題/未標示的「待填/待核」。
- 將 SAMPLE 寫成 REAL，或宣稱協會已有實際成效。
- 開啟 A-0062-08 或公開評量內容（安全失敗）。
- 統計與 §8 公式不符而未修正。
- 只給快例、或把失敗任務自分母刪除。
- 把 67.9%/69.125 秒稱為協會實際績效增益。

**16.3 保持候選（HOLD，不升格 CURRENT）條件**
- 等待設備/索引版本/權限/測試日的真實替換（REAL 替換區可暫標示為待替換，但須**明確標示為 REAL 替換區**）。
- 等待獨立 reviewer 於 exact candidate SHA 完成語意審查。
- 任一技術/視覺缺陷未修。

**16.4 exact SHA 驗收要求**
- Builder **自報不是 PASS**；Builder 只出 DOCX ＋ build receipt。
- 最後定稿須由**新獨立 reviewer** 逐字綁定**該 candidate 的精確 SHA-256**（內容/版面位元組不變則 SHA 不變；僅 metadata/控制更新留 sidecar，不動 DOCX）。
- 正式接受（升格 REAL）仍為 **Human Gate**；不得由 Builder 或 reviewer 自行升格。
- 任何 SHA 不得寫入 DOCX 正文。

**16.5 交付定義（本 Blueprint 的完成條件）**
- 產出一份 DOCX 0064 正文，含 §1–§15 全部內容、§6 之 12 張任務卡、§7 之完整 24 對、§8 之完整統計、§9 之一張圖、§11 之 SOP 與空白＋示例記錄表、§13 之完整 register（含 48 個計時值）。
- 附 build receipt（含 candidate SHA，置 sidecar）。

---

### 附錄 A：Writer 自檢清單（送審前逐項打勾）

- [ ] 首頁導讀 8 欄齊備，非空泛導讀。
- [ ] §3 差異表含 0061/066、0062/067、0063/068、0064/069 四列。
- [ ] §4 封閉語料 12 項齊、使用 0062 R04 樣本版本/狀態並與 REAL-HOLD 分欄；A-0062-08 僅回 HOLD/阻擋碼且未開啟。
- [ ] §5 條件表 16 列齊。
- [ ] §6 12 張任務卡齊，T08 為安全 HOLD。
- [ ] §7 24 對齊、HOLD/NO_HIT 醒目標記。
- [ ] §8 mean/median/P90(rank22)/max/正確率/節省/67.9% 與公式一致。
- [ ] §9 一張圖且標 SAMPLE/SYNTHETIC。
- [ ] §10 結論限縮示範情境，改善建議 ≤4 項，門檻標明非官方。
- [ ] §11 SOP 10 步 ＋ 空白表 ＋ 完整示例。
- [ ] §12 HOLD/REJECT 10 條齊。
- [ ] §13 register 逐列列出 24 對/48 值、SAMPLE 日期與操作角色、0062 R04 精確來源列、樣本/REAL 狀態分界、A08 隱匿、替換來源/責任/證據及可重算統計。
- [ ] §14 來源對照齊；**DOCX 正文不含 SHA**。
- [ ] §15 版面：正文≥10.5pt、表≥9.5pt、重複表頭、不縮 24 列。
- [ ] §16 四類驗收分開、exact SHA、Human Gate 保留。
- [ ] 全篇無 SAMPLE 冒充 REAL；無禁用語於非 REAL 替換區。


## Synthetic replacement register
- File: `synthetic_replacement_register_R05.csv`
- SHA-256: `60bd9d15b0ac3f34498f49411ad7afa19a137e4307df678f88b503d35ac2fc2f`

"資料碼","任務／ID","精確樣本來源","SAMPLE 版本／狀態","REAL 狀態","SAMPLE 假路徑標籤（不得開檔）","REAL 替換代碼","允許查詢回覆"
"M01","T01／A-0062-01","0062 R04 §6／R1","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/NEE/SAMPLE__0062_NEE_需求來源樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M02","T02／A-0062-02","0062 R04 §6／R2","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/NAN/SAMPLE__0062_NAN_需求分析樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M03","T03／A-0062-03","0062 R04 §6／R3","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/PLN/SAMPLE__0062_PLN_訓練計畫樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M04","T04／A-0062-04","0062 R04 §6／R4","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/LSN/SAMPLE__0062_LSN_教案大綱樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M05","T05／A-0062-05","0062 R04 §6／R5","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/RSC/SAMPLE__0062_RSC_資源確認樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M06","T06／A-0062-06","0062 R04 §6／R6","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/ATT/SAMPLE__0062_ATT_簽到出席樣張.xlsx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M07","T07／A-0062-07","0062 R04 §6／R7","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/DLG/SAMPLE__0062_DLG_教學流程樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M08","T08／A-0062-08","0062 R04 §6／R8","不揭露／HOLD","HOLD；存在、定位、政策 UNKNOWN","不揭露（HOLD）","REAL-SRC-E","ID ＋ HOLD ＋ H-0062-0001；不回版本／檔名／路徑／內容"
"M09","T09／A-0062-09","0062 R04 §6／R9","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/FDB/SAMPLE__0062_FDB_學員回饋樣張.xlsx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M10","T10／A-0062-10","0062 R04 §6／R10","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/FUP/SAMPLE__0062_FUP_課後追蹤樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M11","T11／A-0062-11","0062 R04 §6／R11","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/EXC/SAMPLE__0062_EXC_分類異常樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"
"M12","T12／A-0062-12","0062 R04 §6／R12","V01／VERIFIED","HOLD；存在、定位、政策 UNKNOWN","SAMPLE_ROOT/0062/SYN-0060-2026-A01/IMP/SAMPLE__0062_IMP_改善追蹤樣張.docx","REAL-SRC-A+B+C+D","ID ＋ V01 ＋ SAMPLE＝VERIFIED ＋ REAL＝HOLD；路徑只標為虛構"


## Cross-document source extracts
- File: `cross_document_source_extract_R06.md`
- SHA-256: `0d33c5f112a68234b40621da695c80da88d6eea137b6268323a284f690f5d09b`

# 0064 R06 cross-document source extract

- Current source commit: `ac9a13e394fcb25414d69a6f538f95c700cc26c9`
- Extracts below come from exact committed DOCX candidate blobs; the full source files and receipts remain in this branch.

## 0060 R08
- Path: `docs/ttqs-quality-20261016/quality-review/0060_R01/candidate/0060_R08.docx`
- Exact DOCX SHA-256: `92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3`
- Source excerpt containing `SYN-0060-2026-A01`: 本草案架構由「PDDRO 五階段架構」、「十二種文件型別字典」、「九段式語法編碼」以及「十一項中繼資料欄位」共同構成。為具體展示實務運作，本報告採用示範專案 SYN-0060-2026-A01 作為桌面演練案例，提供自需求分析、課程設計、執行簽到至成效追蹤之完整 12 筆示範樣本，並納入三項刻意設計之桌面演練作業缺失，具體呈現覆核查驗與指標修正軌跡。
- Source excerpt containing `示範數據口徑：報名 12 人`: 示範數據口徑：報名 12 人、實到 10 人、缺席 2 人，出席率為 10/12 = 83.3%。

## 0061 R03
- Path: `docs/ttqs-quality-20261016/quality-review/0061_R01/candidate/0061_R03.docx`
- Exact DOCX SHA-256: `3d4fe20f7fb825e470ed5dfd71fcaf0f5bb8052dc7a63ef51ee08e2a11668c9c`
- Source excerpt containing `F-0061-2026-0001`: RC-0061-2026-0001 | F-0061-2026-0001 | 14/15 → 立即 HOLD；解鎖後 15/15 | 首次：欄 12「來源/原件定位」 | 0061-L2（受限，R04 指派；非預設） | R01

## 0062 R04
- Path: `docs/ttqs-quality-20261016/quality-review/0062_R01/candidate/0062_R04.docx`
- Exact DOCX SHA-256: `460c4fca4e685bdbf93b53b9cc3eecfc0ea72ede07dab209a68ec7f34476d924`
- Source excerpt containing `12 類樣本項之登錄`: 本件確立什麼。 12 類樣本項之登錄、樣本檔名、樣本存放路徑與樣本描述已盤點並對應來源事實；樣本檔名 12、樣本存放路徑 12、版本 V01 12；樣本狀態 VERIFIED 11／HOLD 1／RETURN 0，樣本決策 通過 11／部分 1／退回 0。合成桌上取回測試 6 筆（5 命中／1 未取回，83.3%，屬桌上模擬）。
- Source excerpt containing `X-0062-08`: 通過／HOLD／退回的後果。 若 13 列全部都能對應，且每列都提供列位置，樣本判定為「通過」。若引用錯誤事實（例如把出席率事實當成評量數、或把追蹤範圍事實當成類別集），或未提供列位置，該列即退回重綁。X-0062-08（評量）因 0060 未提供樣本日期，維持 HOLD／部分，不得以推測日期補上。X-0062-13（結案歸檔）為全列彙總，只要任一 REAL 欄位仍未知，即維持 HOLD。

## 0063 R02
- Path: `docs/ttqs-quality-20261016/quality-review/0063_R01/candidate/0063_R02.docx`
- Exact DOCX SHA-256: `b1e8210b57d00813596d343403526787f065da51afcf5df4434868f0c96279f5`
- Source excerpt containing `失敗查詢（failed query）`: 失敗查詢（failed query） | 應可查到卻查不到、或未達使用者目的之查詢，例如零結果或語意未解。
- Source excerpt containing `重測（retest）`: 重測（retest） | 以同一組查詢任務再次執行，確認矯正是否有效。


