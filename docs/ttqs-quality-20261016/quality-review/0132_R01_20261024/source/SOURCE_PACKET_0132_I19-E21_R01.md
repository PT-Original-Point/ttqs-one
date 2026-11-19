# 0132｜來源包｜I19-E21｜R01

狀態：`SOURCE_PREP_COMPLETE`；僅授權可逆候選施工，尚無本版 Word 候選、REAL 結果或正式接受。

## 身分與官方要求

| 欄位 | 核實內容 |
|---|---|
| 專案 | TTQS_ONE |
| 文件編號 | 0132（142 序列 doc_id；不是官方方框流水號） |
| 內部要求 | I19-E21（僅為內部 142 序列 crosswalk） |
| 專案 157 Blueprint | index 145，I19-L3，官方資料表第 8 頁 |
| 文件名稱 | 個人產品不良件數與訓後改善分析表 |
| 文類 | 分析／評估報告，含可重算的不良件數及分母、趨勢、其他影響因素、可執行追蹤 |
| 官方方框原文 | 「個人產品不良件數有下降趨勢。」 |
| 官方 printed checkbox serial | `UNKNOWN`；不得以 0132、I19-E21 或 157 index 145 代替 |

## 同源規格與精確版本

本來源包以 PR #92 branch `work/ttqs-one-document-quality-contract-20261016` 的 HEAD `59614bfdb06d7e04000ed4fbc30dbec1bd8f542a` 為讀取基準。

| 來源 | 路徑／定位 | Git blob SHA |
|---|---|---|
| 官方佐證資料表 PDF | `quality-review/0031_R06/inputs/official_source.pdf`, p.8 | `9c7621decdad585b743bf2b3d949ee5518b7bee0` |
| 官方 PDF 位元組 SHA-256 | 同上，9 頁 PDF；本機逐頁提取 p.8 | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` |
| 人類 Mission | `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md` | `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` |
| 逐指標寫作手冊 | `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md` | `4ff863d9f534b6359fc1c7c1685bd8cce02da886` |
| 157 唯一 Blueprint 清單 | `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`, I19-L3 index145 | `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` |
| 142 文件 crosswalk | `quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv`, I19-E21 | `1ac4a8419088d947947031b758e29c35a3606514` |
| 142 文件 seed | `quality-review/0098_R08_20261021/inputs/blueprint_seed_142.csv`, 0132 | `f20ac9ae37700eb03a93b8da4407e7bf4788b602` |
| 詳細內部 Blueprint row | `quality-review/0040_R04/inputs/BLUEPRINT_CURRENT.jsonl`, deliverable_id=0132 | `cab446ede479001334289d18062e6b8bb2340dc3` |
| 現行 AGENTS | `AGENTS.md` | `2e8d4eddd68c650f38db8cb48d421b838e693ecb` |
| Goal R11 | `docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md` | `65e7fd5a406877e875174402a0d3ddc68b6111a1` |
| 120m R11 | `docs/ttqs-quality-20261016/05_HOURLY_NATIVE_WAKE_RESUME.md` | `dbdb2e567e8e5c2b7eb0632f060a45a7ae371a49` |
| R11 continuation | `docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` | `b566c5c71d1a88e012eca2eeac90c8a3e4ecc06c` |

## 需求邊界與來源解讀

官方句子要求顯示個人產品不良件數有下降趨勢，不能把趨勢圖或訓後時間相鄰直接寫成因果。寫作手冊對 I19 的成果佐證要求數據、分母、單位、改善幅度及可歸因邊界；I17d 亦明確要求不良率下降需基準、單位及歸因限制。故本件同時列「不良產品單位數」與「每百件受檢產品不良率」，避免產量改變造成只看件數的錯判。

目前沒有原始點協會真實產品、受訓者、檢驗紀錄、正式標準、訓練日期或改善結果提供給本案。所有示範值必須標為 `SAMPLE / SYNTHETIC`，不得推導真實協會成果、正式決議或評核分數。

詳細內部 Blueprint row 的 generic `成果率 = 符合成果人數／可評估人數` 不適用本件的產品不良件數。此來源包以官方原文及 02/03 的專屬缺陷趨勢要求，將公式具體化為 `不良單位數／同範圍受檢單位數`；不修改官方要求，也不把 0132 改成 0131 的證照／就業成果率。

## 鄰項拒絕與防錯

- 0131／I19-E20 是學員證照通過與訓後就業追蹤，分母是學員／追蹤對象；不是產品不良件數。
- 0133／I19-E22 是年度訓練班次及參訓人次趨勢；不是產品品質趨勢。
- 0130／I19-E19 是訓後創業案例及第三方真實個案核查；不得挪用個案或第三方事實。
- 本件沒有可共用的 REAL case_id。獨立示例 ID 為 `SYN-0132-CASE-01`；不得共用 0131 的合成學員成效數據。

## 下一階段輸入

`UNIQUE_BLUEPRINT_0132_I19-E21_R01.md` 定義專屬文類、資料欄位、公式、完整合成算例、其他影響因素、日常操作、HOLD/REJECT 條件與驗收範圍。Word Writer 只可依本件官方來源與此 Blueprint 寫稿；不得以 0131 或舊 0132 正文作模板。