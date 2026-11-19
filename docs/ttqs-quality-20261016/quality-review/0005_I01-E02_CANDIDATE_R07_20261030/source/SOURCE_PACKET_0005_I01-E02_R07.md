# 0005 I01-E02 R07｜來源與修復封包

狀態：CANDIDATE。沒有 REAL 調查、協會核准或 Human 正式接受的主張。

## 文件識別與官方要求
- 文件：0005《目標市場需求分析報告》；需求識別 I01-E02；本案 crosswalk serial 002 只作專案內對照，官方 PDF 未印出 002。
- 官方來源：official_requirement.pdf，第 1 頁「目標市場需求調查。」；SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。
- 唯一 Blueprint：0005 R02 row SHA-256 24c927721f8b7f446eb239f65306fd52cd466ae701b6383e8f26771287bc4275；Markdown SHA-256 27c2e7873d880807a09c4cf887258648c3f2fb3edfd82e3b496c2f76e2791c54。
- 142 分件 crosswalk：沿用 R06 封包記錄的 SHA-256 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679；R06 封包 SHA-256 420f3171eca8f823c46d6d256b9401c67d4fef5233cd13ded8460e0b5a6e623b。該對照將 0003 問卷、0004 執行／樣本流向、0005 分析分開；不把歷史 142 序號當官方要求數。

## R07 對 R06 獨立 PARTIAL 的有界修復
R06 parent DOCX SHA-256：b6ae9cd46a2bae5dd07a55f2a453762bb8ac33c7dd4dc1bf93aea3420c06b9c7（原始位元組複本保存在 history/0005_I01-E02_R06_parent.docx）。R07 只修已定位缺口，保留其他 43 項合成事實與既有計算：
1. 正文明列 002 是專案 crosswalk serial，官方 PDF 未印出此號。
2. 對照 0004 R01 的合成批次期間 2026-10-28 至 2026-10-29。
3. U005 的 INELIGIBLE／OUTSIDE_FICTIONAL_TARGET_SEGMENT 只作 0004 合成輸入；來源未列可重算資格條件，故不冒稱獨立驗證，真實套用前條件或證據缺漏即 HOLD。
4. 增設 8 個指標的來源／題項、有效值、分母、排除與解讀界線字典；明列 MISSING、DECLINED、NA、NOT_ASKED，不作零分或插補。
5. 將 Q1 合成答案「志工」與 0003 R14 顯示選項對齊，更新本件相依的 SYN-0005-004／041。
6. 將高緊急度 ≥4 切點標為本例示範值，非官方／協會門檻；真實分析需預先定義。
7. 更新來源追溯為 0003 R14，保留其 exact-SHA PARTIAL 限制：Q3 DECLINED 在編碼表漏列。該問題不影響此例的有效三順位合成答卷；真實 Q3 拒答須 HOLD 直到來源 codebook 對齊。
R07 DOCX SHA-256： a36c501893bcb4d2dadaf0adfa7d8638df5e426650a8876182a8f83aebfa1a7c。
R07 replacement register：43 資料列，SHA-256 e9598f6ffac5cf89d4ad834b49aaf6a55f455044918f6750622c8a6f0d489ca6。除 SYN-0005-004、035、041 三筆受上述修復影響外，其餘 40 筆值保留不變。

## 輸入來源 exact SHA-256
- 0005 source markdown：d0d252ed25c7f198623d4ddba16489680cb3d7cc28afaea8dec3b447e7fae404。
- 0005 Unique Blueprint R02 Markdown：27c2e7873d880807a09c4cf887258648c3f2fb3edfd82e3b496c2f76e2791c54；row：24c927721f8b7f446eb239f65306fd52cd466ae701b6383e8f26771287bc4275。
- 0003 R14 DOCX：162c3243e276b1672d1f1aac5e42adf5b63da7d2f98e77c35bc53a2b8e5ec4f4。
- 0003 R14 source packet：e9037a51cc10882e0b5c73b5180119ff8f94554ce89c72d897ed9d903b107f0e。
- 0003 R14 replacement register：d4f1aa86489e67cc494b5f8faa63a52a1fe3821cbe0171bcd3735bf032e61a64。
- 0003 R03 Blueprint row：9ca8530d276ed7afff1b65f066e049c5ba74de5d65546c02cc04423ca98898f2；Markdown：2733e5f8aec6951f9e475a2d12d854e8f6950d3fb6eef85b29c8dfbb12ae0dbf。
- 0004 R01 source packet：ed66b95a1856751b559702fe7b944595ec827651435b652a380725b9cf8a219d。
- 0004 R01 synthetic register plan：c356d284fc71c2deb6a03647ee2c70e62baaea9bf96351e2b7fb151e8788c3e3。
- 0004 Unique Blueprint R01：09937d2b74cf2794d01afe591b116adea406d3b2f16c13e8164fd74997f9550c。
- R06 source packet：420f3171eca8f823c46d6d256b9401c67d4fef5233cd13ded8460e0b5a6e623b。

## SAMPLE／REAL／接受狀態
本報告只使用完整 SAMPLE／SYNTHETIC 示範。無真實問卷、真實樣本、協會核准、第三方原件或正式會議證據。R07 視覺檢查及新 exact-SHA 獨立語意審查尚未完成，均為 PENDING；R07 不是 HUMAN_ACCEPTED 或 CURRENT。
建立時間（Asia/Taipei）：2026-10-30T05:55:35.712961+08:00
