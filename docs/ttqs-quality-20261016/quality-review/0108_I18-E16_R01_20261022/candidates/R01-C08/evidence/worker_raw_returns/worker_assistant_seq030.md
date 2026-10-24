## 8. SAMPLE → REAL 逐欄替換清冊

> **SAMPLE / SYNTHETIC — 替換計畫，尚未執行**  
> REAL 欄位一律 UNKNOWN；任何一欄未補齊，整筆 HOLD，不得只替換金額。

| # | 替換欄位／區塊 | SAMPLE 現值（僅示範） | REAL 必要來源 | 授權／同意或法源 | 遮罩規則 | 保管位置 | 責任角色 | 完成條件 | 缺件狀態 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 文件識別與版本 | 0108／R01／SYN-COHORT-0108-A | 正式文件識別、版本核定、來源錨定 | TODO：文件治理核定 | 公開版保留文件 ID 與版本，不貼個資 | UNKNOWN（TODO：受控版本庫） | TODO：文件治理 | 文件 ID、版本、來源錨定一致 | UNKNOWN／HOLD |
| 2 | 班別與觀察期間 | 2026-01-01 至 2026-03-31；2026-04-01 至 2026-04-30；2026-07-01 至 2026-09-30 | 班別核定、課程日期、觀察窗核准 | TODO：課程與資料治理核准 | 公開版只留季度與代碼 | UNKNOWN（TODO：受控資料夾） | TODO：課程承辦 | 期間完整、連續且與名冊一致 | UNKNOWN／HOLD |
| 3 | 名冊、完訓與配對 | SYN-P01 至 SYN-P08；內部代碼 | 正式名冊、完訓或出席、受控配對表、代碼版本 | TODO：課程管理與資料治理權限 | 只留內部代碼；去除姓名、身分證、帳號 | UNKNOWN（TODO：受控資料夾） | TODO：課程承辦／資料保管 | 同一人配對無歧義，完訓可回查 | UNKNOWN／HOLD |
| 4 | 薪資口徑 | 固定本薪；排除固定津貼、變動津貼、加班費、獎金、非現金 | 薪資項目定義、計薪週期、稅前／稅後、口徑版本 | TODO：薪資資料治理核准 | 公開版只列口徑說明，不列逐人金額 | UNKNOWN（TODO：薪資受控區） | TODO：薪資保管人 | 全體一致、版本化、可重算 | UNKNOWN／HOLD |
| 5 | 基準薪資 | 六筆完整；P07 不適用；P08 缺件 | 三個完整月正式給付紀錄或可回查薪資報表 | TODO：當事人同意或確認其他合法依據 | 不列姓名、帳號、雇主全名 | UNKNOWN（TODO：薪資受控區） | TODO：薪資保管人 | 三個月完整、稅前、同一口徑 | UNKNOWN／HOLD |
| 6 | 追蹤薪資 | 六筆可比；P07／P08 不可比 | 同上，且與基準期同一口徑 | TODO：同上 | 同上 | UNKNOWN（TODO：薪資受控區） | TODO：薪資保管人 | 三個月完整、可回查、口徑不變 | UNKNOWN／HOLD |
| 7 | 雇用關係 | 六筆同一雇主；P07 為就業轉換 | 到職、在職、離職、轉換或正式人事資料 | TODO：人事資料權限 | 不揭露雇主全名與地址 | UNKNOWN（TODO：人事受控區） | TODO：課程承辦／人事窗口 | 同一人、同一雇主、連續雇用 | UNKNOWN／HOLD |
| 8 | 權限、同意或法源 | 無真實同意；不主張取得 | 同意書、契約、法令依據、撤回或終止紀錄 | TODO：資料保護角色核定 | 公開版不展示同意書或簽章 | UNKNOWN（TODO：資料保護受控區） | TODO：資料保護角色 | 法源或同意已核實，範圍與期間相符 | UNKNOWN／HOLD |
| 9 | 來源索引、遮罩與第二人重算 | SYN-Pxx-B／F／T／H；流程示例 | 來源清單、索引對照、遮罩版、獨立重算表、差異紀錄 | TODO：資料治理與覆核指派 | 去除姓名、ID、帳號、雇主、簽章、條碼、QR code | UNKNOWN（TODO：受控資料夾） | TODO：資料保管人／獨立覆核人 | 每數字可回查；重算一致；遮罩檢查通過 | UNKNOWN／HOLD |

**替換規則：**

- 不得只替換金額；來源、口徑、授權、遮罩、保管、覆核與版本必須同步替換。
- 任一欄 UNKNOWN，該筆即 HOLD；不得把 UNKNOWN 填成 0、空白或「無加薪」。
- REAL 公開版不得逐人列薪資；必要時只在受控場合閱覽，公開版以群組彙總或遮罩索引呈現。
- 每次替換建立新版本，舊版不得覆寫；差異與修正須留軌跡。

## 9. 個案狀態與決策紀錄

### 9.1 證據狀態與個案處置分離

| 層次 | 允許值 | 意義 | 不得做的事 |
|---|---|---|---|
| 證據狀態 | COMPLETE | 兩期、口徑、雇用、授權、來源均完整 | 不得跳過第二人重算 |
| 證據狀態 | MISSING_BASELINE／MISSING_FOLLOWUP | 缺少一期來源 | 不得以 0 代替 |
| 證據狀態 | INCOMPARABLE_COMPONENTS | 薪資組成或計薪週期不可比 | 不得硬算差額 |
| 證據狀態 | EMPLOYMENT_CHANGE | 雇用關係變更或追蹤期才到職 | 不得稱為加薪或未加薪 |
| 證據狀態 | AUTHORITY_UNKNOWN | 同意或法源未核實 | 不得先公開或使用 |
| 證據狀態 | SOURCE_UNTRACEABLE | 數字無法回到來源 | 不得保留為已驗證 |
| 證據狀態 | REVIEW_MISMATCH | 兩人重算不一致 | 不得自行選一個版本 |
| 證據狀態 | UNKNOWN | 尚未取得或尚未判定 | 不得推定為 0 |
| 個案處置 | VERIFIED_COMPARABLE | 證據完整且可比 | 分母：是 |
| 個案處置 | INCREASE | 已驗證差額大於 0 | 分母：是；不得寫因果 |
| 個案處置 | NO_CHANGE | 已驗證差額等於 0 | 分母：是；不得與缺件混淆 |
| 個案處置 | DECREASE | 已驗證差額小於 0 | 分母：是 |
| 個案處置 | EMPLOYMENT_TRANSITION | 基準不適用或雇用轉換 | 分母：否；不得稱未加薪 |
| 個案處置 | HOLD | 缺件、不可比、未授權或重算不一致 | 分母：否；補件前不得結案 |
| 個案處置 | EXCLUDE_WITH_REASON | 非本班、未完訓、非薪資、期間外、重複等 | 分母：否；保留原因與原值 |
| 個案處置 | REJECTED_RECORD | 已確認來源錯置、遭竄改或明確無效 | 分母：否；保留稽核軌跡 |

### 9.2 個案決策紀錄欄

| 欄位 | 填寫值 |
|---|---|
| 決策紀錄 ID | UNKNOWN（TODO：建立流水號） |
| 案件／個案代碼 | UNKNOWN |
| 班別與期間 | UNKNOWN |
| 證據狀態 | UNKNOWN |
| 個案處置 | UNKNOWN |
| 是否納入分母 | UNKNOWN |
| 排除／保留理由代碼 | UNKNOWN |
| 基準與追蹤來源索引 | UNKNOWN |
| 首算結果 | UNKNOWN |
| 第二人重算結果 | UNKNOWN |
| 差異與處理 | UNKNOWN |
| HOLD 責任人與期限 | TODO |
| 關閉證據或後續動作 | UNKNOWN |
| 版本與日期 | UNKNOWN |
| 覆核角色／日期 | UNKNOWN |
| 核准狀態 | NOT_GRANTED |

### 9.3 HOLD 的可操作門檻

符合任一項即 HOLD，不得先算成 0 或先寫結論：

1. 基準期或追蹤期任一原件缺失。
2. 少於三個完整月、月份不連續或計薪週期不同。
3. 薪資組成不可比，或固定津貼、變動津貼、加班費、獎金誤入。
4. 同一人配對不可靠，或姓名、代碼、期間有歧義。
5. 觀察期間未經核定，或與班別、名冊不一致。
6. 雇用關係變更未解釋，或追蹤期才到職。
7. 同意、契約或法源未核實，或撤回狀態不明。
8. 來源無法回查，或原件與索引不一致。
9. 第二人重算不一致，或差異尚未解決。

**HOLD 處理：** 凍結該筆計算；保留原始值與 UNKNOWN；指定責任人與期限；補件後重新判定。不得把 HOLD 改寫成 0、未加薪、無差異或已排除。

### 9.4 EXCLUDE_WITH_REASON 的可操作門檻

符合任一項，且已留下原值與理由，可排除：

- 非本班或非本次觀察對象。
- 未完訓、缺席過多或無法確認參與。
- 非薪資收入、補助、保險給付或非現金給付。
- 基準或追蹤落於核定期外。
- 變動給付、加班費或獎金誤入固定本薪。
- 重複資料，且已確認同一筆不應重複計算。

**處理：** 不得刪除原列；填理由代碼、來源、判斷角色與日期；分母維持不含該筆。若只是缺件，先 HOLD，不得直接排除。

### 9.5 REJECTED_RECORD 的可操作門檻

只在已確認下列情形時使用：

- 來源錯置，且與其他案件或期間明顯不符。
- 文件遭竄改、變造或關鍵欄位無法辨識。
- 文件明確無效，或與已知正式紀錄衝突且無法調和。
- 重複且身分衝突，經查證仍無法確認哪一筆有效。

**處理：** 由兩個角色分別確認；保留原值、索引、差異、判斷理由與日期；不得公開可識別個資；不得在尚未查證前指控偽造。僅缺件、未回覆、口徑不同或重算不一致，應先 HOLD，不得直接 REJECTED_RECORD。

### 9.6 決策處理流程

| 步驟 | 動作 | 輸出 | 停止條件 |
|---|---|---|---|
| 1 | 收件、登錄、給代碼 | 收件紀錄與來源清單 | 無來源即 HOLD |
| 2 | 判定證據狀態 | COMPLETE 或 UNKNOWN 等 | 缺件即 HOLD |
| 3 | 判定雇用與口徑 | 可比或不可比 | 不可比即 HOLD／EXCLUDE |
| 4 | 製作人首算 | 算式與版本 | 無算式不得進總表 |
| 5 | 獨立重算 | 覆核表與差異 | 不一致即 HOLD |
| 6 | 給處置 | INCREASE／NO_CHANGE／DECREASE／TRANSITION／HOLD／EXCLUDE／REJECTED | 未完成不得結案 |
| 7 | 關閉或核定排除 | 關閉證據、理由、日期 | 未關閉不得標完成 |
| 8 | 遮罩與歸檔 | 公開版、受控版、版本紀錄 | 遮罩未過不得公開 |

## 10. 薪資證據追溯／收件／雙人覆核表（TEMPLATE）

> **TEMPLATE — 可填表單，尚未執行。**  
> 填寫規則：未知填 UNKNOWN；待辦填 TODO；不適用填 N/A；缺件填 MISSING；不得空白；不得以 0 代替未知。

### 10.1 收件封面（表單 A）

| 欄位 | 填寫值 |
|---|---|
| 收件編號 | UNKNOWN |
| 文件版本 | UNKNOWN |
| 班別代碼 | UNKNOWN |
| 案件代碼 | UNKNOWN |
| 收件日期 | UNKNOWN |
| 收件角色 | TODO |
| 來源類型 | UNKNOWN |
| 基準期 | UNKNOWN |
| 課程期 | UNKNOWN |
| 追蹤期 | UNKNOWN |
| 幣別／稅別 | UNKNOWN |
| 薪資口徑版本 | UNKNOWN |
| 資料狀態 | SAMPLE／SYNTHETIC（本表） |
| REAL 狀態 | UNKNOWN |
| 缺件總數 | UNKNOWN |

### 10.2 薪資證據追溯（表單 B）

| 證據項 | 來源索引 | 來源類型／期間 | 金額或月均 | 口徑／同一人／雇主 | 授權／法源 | 遮罩／保管 | 初核／備註 |
|---|---|---|---|---|---|---|---|
| 名冊與完訓 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 身分配對 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 基準薪資 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 追蹤薪資 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 雇用關係 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 薪資口徑 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 同意／法源 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 來源索引與遮罩 | UNKNOWN | UNKNOWN | N/A | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |
| 第二人重算 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／UNKNOWN | UNKNOWN |

### 10.3 薪資明細與計算（表單 C）

| 薪資項目 | 基準合計 | 基準月均 | 追蹤合計 | 追蹤月均 | 納入固定本薪 | 來源索引 | 備註 |
|---|---:|---:|---:|---:|---|---|---|
| 固定本薪 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 固定津貼 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 變動津貼 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 加班費 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 獎金／一次性 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 其他 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 是／否／UNKNOWN | UNKNOWN | UNKNOWN |
| 合計 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

| 計算欄位 | 公式 | 填寫值 |
|---|---|---|
| 可比較 n | 完整可比者 | UNKNOWN |
| 基準合計 | ΣB | UNKNOWN |
| 基準平均 | ΣB ÷ n | UNKNOWN |
| 追蹤合計 | ΣF | UNKNOWN |
| 追蹤平均 | ΣF ÷ n | UNKNOWN |
| 淨差額 | ΣF－ΣB | UNKNOWN |
| 平均差額 | 淨差額 ÷ n | UNKNOWN |
| 總額相對變化 | 淨差額 ÷ ΣB × 100 | UNKNOWN |
| 增加人數 | D_i＞0 | UNKNOWN |
| 增加比例 | 增加人數 ÷ n × 100 | UNKNOWN |
| 增加者平均差額 | 增加者差額合計 ÷ 增加人數 | UNKNOWN |
| 分母 | 可比較且完整者 | UNKNOWN |
| 個案處置 | 依第 9 節 | UNKNOWN |

### 10.4 雙人覆核（表單 D）

| 欄位 | 製作人 | 獨立覆核人 |
|---|---|---|
| 角色代碼 | TODO | TODO |
| 日期 | UNKNOWN | UNKNOWN |
| 看過哪些來源 | UNKNOWN | UNKNOWN |
| 基準合計 | UNKNOWN | UNKNOWN |
| 追蹤合計 | UNKNOWN | UNKNOWN |
| 淨差額 | UNKNOWN | UNKNOWN |
| 平均差額 | UNKNOWN | UNKNOWN |
| 總額相對變化 | UNKNOWN | UNKNOWN |
| 分母與排除名單 | UNKNOWN | UNKNOWN |
| 差異與原因 | UNKNOWN | UNKNOWN |
| 結論 | UNKNOWN | UNKNOWN |
| 獨立性 | UNKNOWN（TODO：確認非同一人） | UNKNOWN（TODO：若否即 HOLD） |

### 10.5 收件與缺件清單（表單 E）

| 檢核項 | 必要 | 狀態 | 缺件處理 | 責任角色 | 期限 |
|---|---|---|---|---|---|
| 班別與期間核定 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 名冊與完訓 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 配對鍵 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 基準薪資 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 追蹤薪資 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 雇用關係 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 同意／法源 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 來源索引與遮罩 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |
| 第二人重算 | 是 | UNKNOWN | HOLD | TODO | UNKNOWN |

## 11. 結論限制與跨文件負向近鄰

### 11.1 結論限制

| 情境 | 可寫 | 不可寫 |
|---|---|---|
| 描述合成差異 | 「在此 SYNTHETIC 樣本中觀察到兩期固定本薪差異。」 | 「訓練造成加薪。」 |
| 描述增加比例 | 「可比較的 6 筆中 4 筆增加。」 | 「66.7% 學員加薪。」 |
| 描述缺件 | 「P08 基準缺件，狀態 HOLD／UNKNOWN。」 | 「P08 為 0、未加薪或無差異。」 |
| 描述就業轉換 | 「P07 為就業轉換，不納入分母。」 | 「P07 沒有加薪。」 |
| 描述樣本 | 「合成樣本的描述性比較。」 | 「協會成效、全體學員、市場水準。」 |
| 描述比例 | 「匹配樣本總額相對變化 3.406%，顯示 3.4%。」 | 「訓練效果 3.4%。」 |

### 11.2 跨文件負向近鄰

| 文件 | 事實類型 | 不能替代 0108 的原因 | 允許的關聯 | 禁止的關聯 |
|---|---|---|---|---|
| 0100／0101 | 能力自評、雷達變化 | 能力分數不是薪資給付 | 可作不同構面的獨立紀錄 | 不得當薪資證據或換算加薪 |
| 0102 | 競賽獎項 | 獎項不是薪資變動 | 可獨立呈現獲獎事實 | 不得稱獲獎等於加薪 |
| 0107 | 證照考試結果 | 證照通過不等於薪資提高 | 可獨立呈現考試結果 | 不得把證照數當薪資差額 |
| 0109 | 網站使用頻率 | 使用頻率不是薪資資料 | 可獨立呈現使用情形 | 不得代替薪資來源 |
| 0108 | 薪資變動紀錄 | 使用獨立 SYN-COHORT-0108-A | 僅在合法共用 REAL 來源時才可引用同一 source ID | 不得宣稱與其他文件共用真實案例 |

**跨文件規則：** 不得因文件編號相鄰、同一課程或同一講師，就推定共用學員或薪資資料。只有找到合法且可回查的共用 REAL 原始來源，才可引用相同 source ID；不得複製其他文件的數字來製造證據鏈。

### 11.3 對外結論檢查

- 是否明确標示 SAMPLE／SYNTHETIC 或 REAL？
- 是否写出分母、排除數與 HOLD 數？
- 是否把 UNKNOWN 誤寫成 0？
- 是否把就業轉換誤寫成未加薪？
- 是否使用「造成、效果、提升、證明」等因果動詞？
- 是否把 6 人合成結果外推至協會、全體或市場？
- 是否引用未經授權的 REAL 來源或可識別個資？

## 12. 來源錨定、版本與變更紀錄

### 12.1 來源錨定

| 來源項目 | 識別值 | 角色／限制 |
|---|---|---|
| 官方 PDF | quality-review/0036_R13/inputs/official/TTQS_evidence_table_training_institution_source.pdf | 官方佐證表來源 |
| 官方 PDF SHA-256 | 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709 | 用於來源核對 |
| 官方 PDF 第 7 頁 | 文字抽取檔第 649 行：「提高薪資紀錄。」 | 本件官方要求；第 648、650 行分屬 I18-E15、I18-E17，不得混入 |
| 官方 PDF Git blob | 9c7621decdad585b743bf2b3d949ee5518b7bee0 | 來源版本錨定 |
| 映射檔 blob | ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b | 0108 → I18-E16、第 7 頁 |
| 映射結果 | 0108__提高薪資紀錄_可直接使用成品.docx | 僅為映射值；不主張該檔存在或已驗收 |
| 157 Blueprint registry blob | 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63 | 第 117 項：外部薪資證據合規取得 |
| 來源包 SHA-256 | f11df2f92edb7c63bc7dbddefe8461188dfdf90c4be9e0c0c4ae284f15457d5f | 本稿來源包 R01 |
| Unique Blueprint SHA-256 | 41713064e2744c12831cb56098cc3ceb5661279048eb16123583f6c26d2f64ab | 本稿唯一藍圖 |
| Writer 契約 SOURCE_HEAD | 75d8f79679e3b3df2a88555e78637404674ff018 | 本稿輸入契約錨定 |
| 來源包所載 PR #92 HEAD | 3dad3490872be0169cfbe9bb1b6564434694a8a6 | 與上列分別保留，不推定同一 |
| 第 7 頁共用渲染圖 | page7_render_0107_source.png；SHA-256 b4b229b154ae401cff6305f8dd413d967ac7a347165d112c355fa15689a358a1 | 與 0107 共用之官方頁面來源；不是 0108 成品或協會證據 |
| 官方印刷流水號 | UNKNOWN | 117 僅為內部索引，不得推定為官方序號 |
| 協會真實薪資證據 | UNKNOWN | 本案未提供，不得以合成資料替代 |

**來源治理註記：** 來源包與 Writer 契約記載的 HEAD 分別保留；正式 REAL 替換前，由來源治理角色確認最終錨定，不得自行推定同一提交。

### 12.2 版本與變更紀錄

| 版本 | 日期 | 變更摘要 | 依據 | 文件狀態 | 覆核 | 核准 | 正式接受 |
|---|---|---|---|---|---|---|---|
| R01 | 2026-10-22 | 建立 0108 合成示範稿、替換清冊、決策門檻與營運表單 | 來源包 R01；Unique Blueprint R01 | CANDIDATE／VISUAL_PENDING | UNKNOWN | UNKNOWN | NOT_GRANTED |

### 12.3 文件控制完成欄

| 必填欄位 | 值 |
|---|---|
| 文件 ID | 0108 |
| 官方要求 | I18-E16｜提高薪資紀錄 |
| 專案藍圖內部索引 | 117（非官方序號） |
| 合成案例 ID | SYN-COHORT-0108-A |
| 版本／日期 | R01／2026-10-22 |
| 資料狀態 | SAMPLE／SYNTHETIC |
| REAL 狀態 | UNKNOWN |
| 正式接受 | NOT_GRANTED |
| 獨立覆核 | UNKNOWN（TODO） |
| 視覺檢查 | VISUAL_PENDING |
| 保管位置 | UNKNOWN（TODO：受控資料夾） |
| 來源錨定 | 見 12.1；UNKNOWN 項目待補 |
| REAL 替換清冊 | 未執行；UNKNOWN／TODO |
| 決策紀錄 | UNKNOWN（TODO） |
| 下一步 | TODO：完成 REAL 來源、授權、遮罩、雙人覆核與版本更新 |