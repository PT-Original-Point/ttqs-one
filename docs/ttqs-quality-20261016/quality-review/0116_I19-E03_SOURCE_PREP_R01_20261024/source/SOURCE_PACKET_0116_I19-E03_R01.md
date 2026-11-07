# 0116 / I19-E03 專屬來源包 R01

狀態：SOURCE_PREPARED；僅授權建立候選工具與 SYNTHETIC 示範，不代表原始點協會已追蹤學員、取得就業成果或正式接受。

## 文件身分與唯一命題
- project_id：TTQS_ONE；doc_id：0116；requirement_id：I19-E03。
- 文件名稱：學員訓後就業狀況追蹤調查表。
- 157 Blueprint 內部對照索引：127，I19-L1「就業口述資訊：證據不足與合法補證路徑」。127 不是 DOCX 編號，也不宣稱為官方紙本方框印刷序號。
- 官方紙本 checkbox 印刷序號：UNKNOWN_NOT_ASSERTED。
- 命題：把訓後就業口述轉成有日期、母體、回覆狀態、問項、統計口徑、證據等級與補件處置的可追溯紀錄；自陳不能冒充雇主或其他第三方證明。

## Fresh-read 正式來源
本來源包以 PR #92 分支 HEAD 7573bc1525e1fb40d36f72c2e8833ebf100374f6 為基準，分支 work/ttqs-one-document-quality-contract-20261016。

1. 訓練機構版 TTQS 查核佐證文件資料表 PDF：送審資料/評核依據/TTQS查核佐證文件資料表-訓練機構版 (3).pdf；Git blob 9c7621decdad585b743bf2b3d949ee5518b7bee0；本機 SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709；303044 bytes。頁7指標19標題為訓練系統的市場功能—目標市場及顧客的價值創造；1分常見參考佐證包含「口頭說明學員訓後就業狀況，但未有具體紀錄及評量」。頁8列出更高分級的不同例示，不可把本件工具或 SAMPLE 誤報為2至4分成果。
2. 03_157_CHECKBOX_BLUEPRINTS.md，Git blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63：I19-L1第127項「就業口述資訊：證據不足與合法補證路徑」；需特定來源、核心正文/示範、決策或結果、跨文件事實連結，不得空欄交差。
3. 02_GENRE_WRITING_MANUAL.md，Git blob 4ff863d9f534b6359fc1c7c1685bd8cce02da886：指標19需呈現市場/顧客價值證據；就業追蹤須有可操作問項、清楚分母、來源及不確定性，不能用滿意度替代就業證據。
4. 01_HUMAN_MISSION_AND_ACCEPTANCE.md，Git blob 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e：SAMPLE/SYNTHETIC與REAL分開；禁止捏造協會執行、第三方文件、核准與簽名。
5. 現行129至142 crosswalk：docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv；blob 1ac4a8419088d947947031b758e29c35a3606514；精確列 I19-E03,1,0,0116,學員訓後就業狀況追蹤調查表。
6. 現行142 Blueprint seed：docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/blueprint_seed_142.csv；建立工件前須重新讀取 blob 並寫入 manifest，不可用舊版本猜測。
7. 本機正式清單副本：19指標_129項現有文件對應填表清單.csv SHA-256 bc2e70b087cc2d6904de454f967d811223f1c87257a3dae7c1dae3aee1dad45d；142份文件逐項檢查與填表建議.csv SHA-256 166eb3cd3d8026206e88f06cb083aa162d2ddd464d53883a3ce5ac411adcea6a。對應列指出主要紀錄仍待取得，不能勾為完整；本機副本的原始 GitHub 路徑未定位前，遠端 blob 標 UNKNOWN。

## 活動候選與舊件隔離
活動 runtime 原先沒有0116 R01 source-prep 資料夾。掃描僅找到0065備份樹內的歷史文件。舊檔 0116_138「指標19_2分_進行訓後薪資調查」是不同命題，絕不可沿用內容、計算或審查。其他舊0116修訂只供歷史追溯，不承接 PASS。

沒有提供協會完成者名冊、聯絡授權、真實回答、就業證明、雇主資料、核准追蹤紀錄或個資政策。因此本包問卷資料與數字均為 SYNTHETIC ONLY；現實績效維持 UNKNOWN / HOLD。公開文件不得含姓名、身分證、電話、雇主名稱或受限原件。

## 固定示範口徑
案例 SYN-0116-COHORT-01；結訓日2026-06-30；90日基準日2026-09-28；八個匿名合成代碼，六份合成回覆、兩個合成未回覆。四名回覆者自陳受僱/自營、兩名自陳求職；四筆自陳均沒有提供第三方證明。
- 回覆率 6/8=75.0%。
- 回覆者自陳受僱/自營比例 4/6=66.7%，僅描述回覆者。
- 本示範有佐證的自陳就業筆數 0/4=0%；只表示沒有原件輸入，不表示真實就業為零。
- 全體完成者的就業比例、協會實績、訓練因果效果均 UNKNOWN。未回覆不得算失業。

## 跨件界線與接續
0115/I19-E02是心得與知識分享；0117/I19-E04是考照追蹤。兩者不能替代就業分母或共用本例數字。0100/0101及其他課程文件不提供本例事實；不同案例不共用fact_id。若未來建立真實跨件關聯，須先核定相同cohort、期間及來源索引。

R01 source-prep outputs：本包、唯一Blueprint、8-row dataset、SYNTHETIC replacement register、source manifest、validator與validation receipt。通過原生校驗後才進Writer。真實替換需合法完成者名冊、母體定義、聯絡依據、原始回覆、追蹤日、受限原件索引、獨立核驗及資料保存規則；原件不得上傳公開PR。