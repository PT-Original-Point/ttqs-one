# 0133 來源包 I19-E22 R01

狀態：SOURCE_PREP_COMPLETE；候選資料僅供可逆建置；REAL 成果及正式接受均 UNKNOWN。

## 核實身分
- project_id：TTQS ONE
- doc_id：0133（內部 142 序列文件編號）
- 142 crosswalk requirement_id：I19-E22
- 157 Blueprint index：146；官方指標 I19-L3；官方參考佐證資料表 PDF 第 8 頁
- 官方原文：「每年訓練班次、人次均持續成長。」
- 文件文類：年度班次與參訓人次登錄表及多年度趨勢分析
- 官方印刷方框流水號：UNKNOWN；不可用 doc_id、內部 ID 或 157 index 代替。

## 來源版本
來源讀取基準：GitHub PR #92 分支 `work/ttqs-one-document-quality-contract-20261016`，HEAD `69434ddef4012e4ac1e94d2dfed638f67f926f19`。以下 blob 與 SHA 由該 HEAD 直接讀取。

| 來源 | 路徑 | Git blob | SHA-256 |
|---|---|---|---|
| 官方佐證資料表 PDF | `docs/ttqs-quality-20261016/quality-review/0031_R06/inputs/official_source.pdf` | `9c7621decdad585b743bf2b3d949ee5518b7bee0` | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` |
| 157 唯一 Blueprint | `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md` | `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216` |
| 142 crosswalk | `docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv` | `1ac4a8419088d947947031b758e29c35a3606514` | `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` |
| 142 Blueprint seed | `docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/blueprint_seed_142.csv` | `f20ac9ae37700eb03a93b8da4407e7bf4788b602` | `280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0` |
| 詳細 142 Blueprint | `docs/ttqs-quality-20261016/quality-review/0040_R04/inputs/BLUEPRINT_CURRENT.jsonl` | `cab446ede479001334289d18062e6b8bb2340dc3` | `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e` |
| 逐指標寫作手冊 | `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md` | `4ff863d9f534b6359fc1c7c1685bd8cce02da886` | `7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa` |
| Human Mission | `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md` | `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | `07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8` |

## 官方資料位置與辨識

官方 PDF 第 8 頁常見 3 分參考佐證列載：「每年訓練班次、人次均持續成長。」同頁相鄰項包括學員訓後創業案例、證照/就業、個人產品不良件數下降及會員人數/會費逐年增加。0133 只處理班次及人次，不把鄰項資料挪入本件。官方資料表說明為常見參考例，並非原始點協會已發生成果、已核准事實或評核分數。

142 crosswalk 當前列：`I19-E22, 1, 0, 0133, 年度訓練班次與參訓人次趨勢表`。157 index146 對應 I19-L3 的「年度班次/人次：完整多期數據」。

## 真實資料界線

本次沒有取得原始點協會年度課程清冊、實際辦理紀錄、結班資料、參訓名冊/簽到、核准統計口徑、簽核或外部佐證。案例日期、課程、班次、參訓人次、來源鍵、角色、彙總及成長率均為 SAMPLE/SYNTHETIC。`REAL_EVIDENCE=UNKNOWN`；不得宣稱協會班次或人次實際成長，不得寫成已核准或評核已接受。

專屬內容及驗收見 `UNIQUE_BLUEPRINT_0133_I19-E22_R01.md`。歷史 0133 DOCX 僅為存在性/錯件風險線索；不得複製或作正文模板。
