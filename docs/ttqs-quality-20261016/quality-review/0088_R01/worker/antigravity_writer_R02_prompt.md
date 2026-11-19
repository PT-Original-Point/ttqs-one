TTQS ONE 0088 / I17D-E02 的 bounded text-only repair writing task。只回覆可貼入 Markdown 正文與 register 的修補文字，不呼叫工具、不讀寫檔案、不操作 GUI/Computer Use、不宣稱正式核准或真實個案。只用 gemini-3.8-flash-high。所有案例清楚標 SAMPLE/SYNTHETIC，不假稱原始點協會已採行。

定位：被審 R03 DOCX SHA-256 416e1fbd4c2057862ffe1946c6473f10fa69399a341132764b06bc5d8471034a。獨立 OpenCode v2 exact-SHA reviewer 判 PARTIAL。只修以下項目，保留正確數字和其他正文：

B1 §2.3/§9.1：新增可重算的 SAMPLE cohort reconciliation：訓練名冊15件，12件符合追蹤資格且均於2026-07-29到期，另3件以不同可檢核合成理由排除，列代碼與原因。正式填寫要按核准名冊逐案比對，不可假設分母。

B2 §3.2–3.3、§7.1、§12：聯絡/資料使用依據未記錄前不得聯絡。空白欄位包含依據來源、涵蓋範圍、確認日期、期限、確認角色、覆核日期、PASS/HOLD/STOP、拒絕/撤回處理。SAMPLE只展示「若有合成核准條件才可聯絡」的虛構流程，不稱協會政策、真實同意或法律保證；無gate不得寫成已聯絡。

B3 C04/C06/C08/C10 有提供文件/支持/轉介/聯絡待辦，不可標CLOSED。新增完整SAMPLE action handoff表：case、待辦、承辦角色碼、建立/轉交日、期限、狀態、下次追蹤。狀態OPEN_ACTION；只有待辦已有具體責任人與期限的移交紀錄且追蹤程序完成，才可標CLOSED_AFTER_HANDOFF。不得假造真人、真實服務或實際轉介。

B4 C01/C02/C07/C09皆為自述考照結果而無原件，全部一致標SELF_REPORTED / NOT_VERIFIED + HOLD；C09自述未通過不得視為核驗失敗或CLOSED。C12三次無回覆只代表本輪聯絡結束，考照仍NO_RESPONSE / UNKNOWN。

B5 §9.3/§13：register每一synthetic_value須可逐列對照正文原文字值，新增「就業原件數=0」與「考照原件數=0」。若狀態碼無法完全同文，正文列對照表且register保存顯示值及正規化碼。165為舊版列數；不得預設新版仍165。

B6 C11/C12無回覆時，就業及技能關聯用UNKNOWN / NO_RESPONSE，不能填N/A。考照N/A只依事前訓練計畫無目標並記來源；若C12有目標，來源為訓前合成計畫/名冊，不得寫成無回覆者已確認。分開記錄目標期限與到期判斷。

另新增不納入12案統計的SAMPLE edge cases：E2已看文件但未第三方核驗、E3在有權限時查核第三方、拒答/停止聯繫、身份/日期衝突HOLD、取得新原件後重開並重算。每例列輸入、判斷、記錄、責任角色、下一步，聲明不更動12案分母。附必要replacement-register CSV rows：唯一key、case_id、fact_type、精確正文值、section/table locator、required source/action、state=SYNTHETIC_NOT_REAL。缺證據寫UNKNOWN/HOLD，不假造核驗結果。

輸出：1) Finding→修補章節表；2) 可直接插入/取代的繁體中文Markdown，含12案一致的gate/處置/待辦修補表；3) register新增/修改CSV列；4) 修改後需重算指標/分母/expected result。只交修補包，不重寫全篇，不自稱PASS。
