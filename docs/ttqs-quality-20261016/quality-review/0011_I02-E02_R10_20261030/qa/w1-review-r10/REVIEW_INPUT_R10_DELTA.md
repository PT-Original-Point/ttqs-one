# 0011 / I02-E02 — R10 exact-SHA semantic delta review

## Identity and source binding
- Work: TTQS-0011-W1-SEMANTIC-R10-DELTA-20261030
- Candidate: `0011_I02-E02_R10.docx`
- Candidate SHA-256: `f539798262faaf9aac358e9839f5bfa7d65dd0c89969c765738fcd02abc17426`
- Prior candidate R09 SHA-256: `b2e96abedac44af5ad343eaa4576d5819ee8e7373145f65d5a7258274481e2c9`
- Doc ID: `0011`; official requirement ID: `I02-E02` (these are different identifiers)
- Official checkbox serial: `UNKNOWN`; do not invent a numeric serial.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; printed page 1.
- Exact official requirement: 「與訓練政策有關之訓練產品與市場定位。」
- Current Blueprint file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`
- Current Blueprint row SHA-256: `6243ec2921c7af4be7ed1d3538003f3cb2d4474d427a394a7146cbf8f0806dd5`
- 129-to-142 crosswalk file SHA-256: `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`; this requirement maps to deliverable `0011` only.
- R09 prior independent reviewer terminal SHA-256: `3ff27b67c868ba81e33a60afaede5eff950ec082f68a53749c3e66339ec1be7c`; prior raw stdout SHA-256: `9d2b84fde18fa636b33ff235d8b004ddb52e313253a1e1a84da63471b2589767`; verdict PARTIAL.
- R10 technical receipt SHA-256: `2677209db32d30ccb19966352025a82d0783eba58e0c745a38a3082cca180862`; R10 visual receipt SHA-256: `2d9bb3a345bee6026c605f36bb68beaf7aec7250a0f7281f5b3ac97345d1bb40`; visual status PASS_VISUAL, 28 Word-native pages.
- R10 changed-excerpt UTF-8 SHA-256: `331090ac1da97086956537884ee218ef230ffe9048c7f0b01aef7d5d613ab310`.
- Deterministic document comparison: R09 and R10 each have 27 tables; all 27 table cell matrices are identical. Paragraph comparison found one revised formula paragraph and two added appendix-index paragraphs; the table set is unchanged.

## Prior R09 findings to resolve
1. Formula/scale text mislabeled the standardized result as 0–100. R10 now needs a coherent explanation for 1–5 input ratings, 100 percentage-point weights, weighted score, and standardization to a 20–100 range. Recompute the table's three examples: A 340÷5=68.0, B 430÷5=86.0, C 380÷5=76.0; verify weights total 100 and no claim says the scale is 0–100.
2. The former §12 opening incorrectly described the deliverable as a text draft and said it was not a DOCX. R10 must accurately identify itself as an SAMPLE/SYNTHETIC DOCX candidate while still denying formal policy/effect, signatures, course notice, independent QA, TTQS acceptance, or real association approval.
3. Blueprint required an attachment index/version section. R10 adds §12.1; verify its statements against the actual document headings/content: case examples are embedded in §7, forms A–E are embedded in §8, replacement register is embedded in §10, and there are no separate attached files.

Prior R09 semantic review otherwise passed the official requirement/genre mapping, title-blind fit, negative-neighbor distinction from 0010/I02-E01 and 0012/I02-E03, SAMPLE/REAL boundary, and the document's other example calculations. This review should preserve that prior scope only if the delta does not undermine it; do not re-review unrelated unchanged content.

## Current candidate excerpts extracted from the exact R10 DOCX
Candidate body extraction was performed directly from the file whose SHA-256 is bound above. The following excerpt digest is `331090ac1da97086956537884ee218ef230ffe9048c7f0b01aef7d5d613ab310`.

### Corrected score explanation
以各因素評分 1–5 分、權重合計 100 百分點計算，標準化加權分數（20–100）= Σ（各因素分數 × 該因素權重百分點）÷ 5；全部因素為 1 分時為 20 分，全部為 5 分時為 100 分。建議判讀：80–100 可列入進一步設計；65–79 需修改後重算；低於 65 暫緩。即使總分達 80，只要政策條文未核實、關鍵需求來源缺失、重要風險未處置或核定權責不明，一律 HOLD。評分者及覆核者分別留存依據，覆核者須逐項重算；不同意時保留兩種分數和理由，由授權者作成可追溯決定，不取平均掩蓋分歧。

### Score example table
| 方案代碼／版本 | 政策契合（25%） | 需求證據（25%） | 遷移方法（20%） | 可近性（15%） | 可行性（15%） | 加權點數 | ÷5 分數 | 依據定位／限制 |
| A 單向概念講授 SAMPLE | 3 [F026] | 3 [F027] | 2 [F028] | 5 [F029] | 5 [F030] | 3×25+3×25+2×20+5×15+5×15=340 [F041] | 340÷5=68.0 [F042] | 合成設計假設；無正式政策、實際需求或市場來源，不得作核定決策 |
| B 情境演練工作坊 SAMPLE | 4 [F031] | 5 [F032] | 5 [F033] | 4 [F034] | 3 [F035] | 4×25+5×25+5×20+4×15+3×15=430 [F043] | 430÷5=86.0 [F044] | 案例中暫列最高；僅表示假設情境內的設計偏好 |
| C 合作單位客製小班 SAMPLE | 5 [F036] | 4 [F037] | 4 [F038] | 3 [F039] | 2 [F040] | 5×25+4×25+4×20+3×15+2×15=380 [F045] | 380÷5=76.0 [F046] | 合作需求、授權及替代方案原件均未提供；必須 HOLD |

### Document headings
- 1. 目的、適用範圍與官方要求
- 1.1 文件界線與相鄰工作
- 2. 政策對照與管理原則
- 2.1 權威來源順序
- 2.2 政策—產品核對規則
- 3. 產品類別、目標學員與定位敘述
- 3.1 建議產品分類
- 3.2 目標學員分群規則
- 3.3 定位敘述格式
- 4. 需求蒐集與職能轉譯
- 4.1 需求來源及品質欄位
- 4.2 可直接使用的需求題目與統計口徑
- 4.3 需求轉職能的必填鏈
- 5. 市場定位矩陣與選擇規則
- 5.1 評分方法
- 5.2 定位決策欄位與產出
- 6. 課程設計審查、更新責任與偏離處置
- 6.1 職責配置
- 6.2 從需求到發布的程序
- 6.3 課程設計審查清單及決策
- 6.4 更新週期與責任
- 6.5 監測指標與覆核計算
- 6.6 偏離、退件與 HOLD 處置
- 7. 完整 SAMPLE／SYNTHETIC 桌面案例
- 7.1 案例邊界與假設政策卡
- 7.2 產品、學員與需求示例
- 7.3 定位矩陣完整算例
- 7.4 完整課程設計及審查紀錄示例
- 7.5 偏離登錄與結案條件示例
- 8. 可複用表單及填寫示例
- 表單 A｜政策—產品追溯表填寫示例
- 表單 B｜需求—職能轉譯表填寫示例
- 表單 C｜定位矩陣及計算覆核表填寫示例
- 表單 D｜課程設計審查與決定表填寫示例（REV-S-001；示例日期 2026-10-21；角色代碼 R-S01／R-S02，均為合成）
- 表單 E｜版本更新／偏離處置表填寫示例
- 9. 官方要求追溯與替換原則
- 10. 逐事實 Synthetic Replacement Register 與 REAL 替換
- 10.1 清冊讀法
- 10.2 逐項替換與覆核步驟
- 10.3 替換責任與保存定位
- 11. 退件與 HOLD 條件總表
- 12. 版本、保管及使用限制
- 12.1 附件索引

### §12 through end of document
12. 版本、保管及使用限制
12.1 附件索引
本件沒有另外附掛的外部檔案。完整 SAMPLE／SYNTHETIC 案例列於 §7，可複用表單 A–E 列於 §8，逐事實替換清冊列於 §10；以上均為本 DOCX 內嵌內容，不是 REAL 原件或另行核准文件。
本檔為 SAMPLE／SYNTHETIC 制度文件（DOCX）候選草案，並非正式制度、簽核紀錄、課程公告、獨立 QA 結果或 TTQS 接受證明。草案可供授權人員討論欄位、門檻、權責及週期；正式採用前須以真實政策與權責文件逐項校正，完成真實資料替換及獨立覆核，再依協會程序核准。任何正式使用者須另保存受控版本、正式決定、實際來源及變更軌跡；本草案不代替那些原件。

## Required review output
Independently inspect the attached review packet only. Do not edit, write, render, browse, invoke tools, or claim REAL facts. Return one JSON object with:
`verdict` (`PASS`, `PARTIAL`, or `FAIL`), `candidate_sha256`, `doc_id`, `requirement_id`, `official_checkbox_serial`, `blueprint_row_sha256`, `reviewed_scope`, `checks`, `findings` with exact paragraph/section/table locators, `calculation_recheck`, `sample_real_boundary`, `neighbor_scope_inheritance`, `extraction_sha256`, `limits`, and `formal_acceptance` (must be `NOT_GRANTED`).

A PASS here means only: the R09 findings listed above are corrected on this exact R10 SHA, and the scoped delta is coherent with the unchanged, previously reviewed R09 content. Do not claim a new full-corpus review, visual inspection, model identity proof, REAL evidence, or formal acceptance.
