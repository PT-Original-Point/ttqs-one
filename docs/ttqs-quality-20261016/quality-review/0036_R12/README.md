# 0036 R12｜課程設計進度與訓練規劃

**狀態：CANDIDATE，獨立 exact-SHA 語意審查進行中；未提升為正式文件，未獲 Human 正式接受。**

## 官方需求與唯一 Blueprint

- DOCX 0036 = I07-E04 = 訓練機構版官方方框 036。
- 官方來源第2頁要求課程設計進度表、課程規劃流程圖說明及訓練規劃書。
- Unique Blueprint 指定 SOP 文類，需有需求來源核對、能力缺口、可衡量目標、課程矩陣、進度及授權放行控制。
- 官方 PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。Blueprint 列及來源對照 SHA 保存在 `inputs/blueprint/`、`inputs/mapping/` 及 `PROGRESS.json`。

## R11 Finding 與 R12 精確修復

R11 的獨立 exact-SHA 語意審查為 PARTIAL，原始回覆保存在 `review/lineage_0036_R11_independent_semantic_review_R01.md`。唯一阻擋是第5頁圖5-1兩個「否」修訂框未畫回接箭頭。

R12 只替換 DOCX 內嵌 `word/media/image1.png`：

1. 來源不足的修訂框沿左側回接至「核對官方要求、需求來源、適用對象與工作任務」。
2. 目標沒有直接評量的修訂框沿右側回接至「配課程單元、教法與時程」課程矩陣。

R11 至 R12 只有該 PNG package part 改變；正文段落、38 張表、計算與其餘內容未變。第5頁 Word 渲染影像直接檢視；R12 仍為19頁，其餘18頁與 R11 逐像素相同。無新增標籤，避免縮放後文字過小。

- R11 DOCX SHA-256：`1e08913a7e330fcbd52f50645138f97b8c951022ef69bc5bd1ee3d2971c9a7c7`
- R12 DOCX SHA-256：`e2be3928f96d45bdee6d18762b169c92e7817d10d0c0f87e4854bd16756febbb`
- Word PDF SHA-256：`092e92c70e224287de86b099cb989f4caf97da86d30397f93132990b84ea5bb2`
- 85筆 SAMPLE/SYNTHETIC 替換登錄 SHA-256：`73e53cb809c8ee7af291b76128896348134e4157b79dc3c013ca95b1d3d28150`

## 適用界線

所有案例、時程與評量資料仍為 SAMPLE/SYNTHETIC，不代表原始點協會已辦訓、核准或有真實成效。空白交接表不是已完成紀錄；不得以本候選冒稱正式 TTQS 接受。

## 獨立審查與遠端讀回

R12 exact-SHA 獨立語意審查為 PASS（指定範圍；第5頁直接目視，其餘18頁沿用與R11逐像素相同的審查鏈）。原始回覆位於 `review/0036_R12_independent_semantic_review_R01.md`，SHA-256 `7cd58f04456820f084621c11062b07db46e38b4b2bf52e93210054e4dffc831d`。技術/頁面收據在 `review/0036_R12_technical_and_visual_receipt_R01.json`；R12 修復依據與流程圖來源、成品圖及重現腳本分別在 `review/`、`inputs/flowchart/`、`evidence/flowchart/`、`build/`。候選與44項初始封包已從 GitHub 逐 blob 回讀零差異；本次 raw review 加入後會再讀回更新封包。


## R12 獨立語意審查 R01

- 判定：**PASS（指定範圍）**，exact SHA `e2be3928f96d45bdee6d18762b169c92e7817d10d0c0f87e4854bd16756febbb`。完整原始回覆：`review/0036_R12_independent_semantic_review_R01.md`。
- Reviewer 直接核對 R12/R11 DOCX bytes、來源與映射、38 張表、85筆替換登錄及第5頁最終 Word render；R11 的兩項唯一 Finding 均由回接箭頭關閉。
- 第5頁兩個「否」修訂分支各自回到正確核對/設計節點；方向、可讀性和授權 fail-closed 條件通過，沒有遮字、裁切或放行旁路。
- 本次只直接目視第5頁；其他18頁與R11逐像素相同，沿用R11審查鏈，沒有宣稱重新目視全部19頁。
- PASS 僅是此候選 SHA 的獨立語意審查結論；仍未正式接受或升格。
