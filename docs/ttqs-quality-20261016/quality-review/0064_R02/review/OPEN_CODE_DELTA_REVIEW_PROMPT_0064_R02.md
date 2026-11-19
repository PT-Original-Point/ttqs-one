# TTQS ONE 0064 R02｜exact-SHA 獨立差異複核

這是 R02 對 R01 已完成完整獨立審查後的有限文字修復。請只讀，不得修改或重建任何檔案，不得呼叫 Computer Use。這次複核必須直接核對 R02 exact SHA，不能把舊 R01 verdict 直接改標成 R02 PASS。

## 本機資料

請從目前工作目錄直接讀取：

- 新候選：`candidate/0064_R02.docx`
- 新抽取正文：`review/docx_text_0064_R02.txt`
- 新 PDF：`evidence/0064_R02.pdf`
- 變更頁面：`evidence/pages_R02/page_01.png`、`page_08.png`、`page_09.png`
- R02 獨特 Blueprint：`UNIQUE_BLUEPRINT_0064_R02.md`
- 修復差異記錄：`review/R02_REPAIR_CHANGELOG.md`
- R02 builder、technical QA、visual QA、raw-data reconciliation：`build/build_docx_0064.py`、`evidence/technical_qa_0064_R02.json`、`evidence/visual_review_0064_R02.json`、`review/final_integrity_check_0064_R02.json`
- R01 前版候選：`candidate/0064_R01.docx`
- R01 完整獨立審查 PASS 回覆及 receipt：`review/opencode_reviewer_0064_R01.response.md`、`review/opencode_reviewer_0064_R01.receipt.json`

## exact SHA 及差異範圍

- R01 已審查 SHA：`E7A18CCC4429A69678C8C36D362F27FAC452B95E8889C894F8892DE9E5568369`
- R02 預期審查 SHA：`32361FE578CD1A493DF17D37CD3BA0C25AD38AA54B829EDDBC6EFA20E5B1A113`
- 重新雜湊 R02 DOCX；不符預期即停止並回報 FAIL。
- R02 僅修復：封面刪除 `exact-SHA` 工程字眼並保持「尚未完成獨立審查」；§10 把錯字「不捷造」改為「不臆造」；附錄索引把「側車」改為「另附電子檔」。封面版本號由 R01 更新為 R02。
- 逐段差異已由本機比對；除上述修正與候選版本標示外，正文相同。頁面 PNG 的 2–7、10–11 與 R01 逐位元相同；僅第 1、8、9 頁影像改變。
- benchmark、fixture、summary、替換清冊及 0060 來源 register 的 SHA 均沿用 R01 且未改動；R01 完整 PASS 的資料／數學／日期／權限／用途邊界結論可作 unchanged-scope evidence。R02 自身的 exact SHA、上述三項文字、三頁新渲染及 candidate status 必須直接複核。

## 複核要求

1. 重新雜湊 R02 DOCX、PDF，確認其與 R02 visual receipt 對應；確認 R02 仍標 CANDIDATE、未宣稱 Human 接受。
2. 直接讀取 R01 正式 reviewer 回覆，確認舊 verdict 確為 PASS 且綁定 R01 SHA；讀取 R02 repair changelog、diff、final integrity 收據及三張改變頁面。
3. 確認 R02 除版本號、三處修正外無其他正文變更；修正語意正確、文字自然，沒有新排版問題；三頁完整可讀且 11 頁總數一致。
4. 確認 benchmark/raw data/replacement register/source hashes 沿用 R01，並由 R02 deterministic receipt 綁定，不把舊 R01 SHA 誤當成新文件 SHA。
5. 如有任何新缺陷，明列頁碼、定位、短摘錄、影響與最小修正；無缺陷才可以對 R02 SHA 給 PASS。

## 回覆格式

第一行列 R02 實測 SHA、預期 SHA、是否相同。總 verdict 只能為 `PASS`、`PARTIAL` 或 `FAIL`。分列 R01 可承接的 unchanged-scope findings，以及 R02 直接檢查的變更與 exact-SHA findings；明確說明任何限制。未直接核對 R02 SHA 或改變頁面不得給 PASS。
