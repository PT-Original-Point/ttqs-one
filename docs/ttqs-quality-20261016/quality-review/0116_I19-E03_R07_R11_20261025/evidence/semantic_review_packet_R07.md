# Independent review request: 0116 / I19-E03 / internal Blueprint index 127 / R07
DOCX SHA256=82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c
Inspect the entire exact-DOCX extraction plus source packet, unique Blueprint, official pages 7-8, writing guidance, fixed dataset and replacement register. Prior R06 reviewer is supplied only as finding context; independently verify current R07 from the attached evidence and recompute relevant facts. This is a text-only semantic review: do not use tools or claim DOCX byte inspection, Word visual inspection, or verify any SHA independently. The local coordinator bound request, extraction header, and current technical receipt to the DOCX SHA; you should report this as request/header/receipt consistency, byte-level hash UNKNOWN. Layout is PENDING and outside your scope.

Return an explicit PASS/PARTIAL/FAIL semantic verdict bound to exact docx SHA and extraction SHA; cite exact sections, form/table row/field and question locators. Recheck:
1) official purpose fit and correct document type;
2) title-blind identification and negative neighboring requirements (0115 and 0117);
3) operational completeness of questions, forms, joins, statuses, denominator, evidence routes, hold/reject;
4) arithmetic and all synthetic row facts vs fixed dataset;
5) the R06 ADVISORY-1/2/3 repairs: demo cells 01/02/06 other_factors now UNKNOWN, the 4 self-reported employed rows are distinguished from 2 job-seeking self-reports, and index 127 explicitly cannot be called the official printed serial;
6) SAMPLE/REAL and consent/third-party boundaries;
7) replacement register mapping and human usability.
If a defect remains, state minimum exact repair and do not PASS. State visual scope as NONE. Do not assert formal acceptance.



# MATERIAL: R07 exact DOCX text extraction SHA256=cdad739b42e07e752910756fb9fdaa66681fbdbc4b95eceda778620c86199e98

<<<BEGIN MATERIAL>>>
DOC_ID=0116
REQUIREMENT_ID=I19-E03
BLUEPRINT_INTERNAL_INDEX=127
OFFICIAL_PRINTED_CHECKBOX_SERIAL=UNKNOWN_NOT_ASSERTED
SOURCE_PACKET_SHA256=3430b1a95755ad773e12380cf1c0b599dbf4b057d1a0f34f47b7dee51fa08c9d
DOCX_SHA256=82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c
EXTRACTION_NOTE=Document-order extraction of the exact DOCX; layout verdict is recorded separately.

學員訓後就業狀況追蹤調查表
文件編號 0116     需求編號 I19-E03     候選版 R07
文件狀態：CANDIDATE R07｜SYNTHETIC ONLY 示範｜未代表原始點協會已執行追蹤、取得就業成果、取得同意或通過核准。本件對應官方指標19之1分參考佐證「口頭說明學員訓後就業狀況，但未有具體紀錄及評量」，用途是提供補足紀錄的可操作方法，不自行評分，不得宣稱達到2至4分成果。157 Blueprint 內部索引127對應 I19-L1「就業口述資訊：證據不足與合法補證路徑」。索引127僅是內部位置，絕不可寫成或宣稱為官方紙本印刷序號；該官方印刷序號為 UNKNOWN_NOT_ASSERTED。
一、目的、使用者、官方要求與證據邊界
目的：把「學員訓後就業」這類口述資訊，轉成具有日期、母體、回覆狀態、逐題問項、統計口徑、證據等級與補件處置的可追溯紀錄；自陳只能以 SELF_REPORT_ONLY 記錄，不得冒充雇主或其他第三方證明。
預定使用者：(1) 訓練機構辦理人員（承辦、覆核）——用來凍結追蹤母體、安排90日追蹤、登錄回覆與缺漏、決定補件；(2) 查核人員——用來檢查分母、算式與證據等級是否一致。
官方要求對應：訓練機構版 TTQS 查核佐證文件資料表（頁7指標19「訓練系統的市場功能—目標市場及顧客的價值創造」）指出，僅口頭說明學員訓後就業狀況而無具體紀錄及評量屬1分常見參考；本表即為建立具體紀錄之工具。就業追蹤須有可操作問項、清楚分母、來源與不確定性，且不得以滿意度資料替代就業證據。
證據邊界四條硬線：
1. 本件全部示範資料為 SAMPLE_SYNTHETIC_ONLY；本包未提供協會完成者名冊、聯絡授權、真實回答、就業證明、雇主資料、核准追蹤紀錄或個資政策，故真實績效為 UNKNOWN / HOLD。
2. 公開文件不得出現可識別個資：姓名、身分證、電話、雇主名稱、住址一律禁止；受限原件只存受權限保護位置，公開表僅記索引。
3. 自陳（受訪者說自己就業）與第三方文件（投保、聘僱契約、自營登記）分流記錄與分流計數；未提供第三方文件即計入「無佐證文件輸入」。
4. 本表不得推論訓練造成就業、就業率改善或顧客價值提升。
二、母體、分母與納入規則
分母母體（cohort）定義：同一 course_id 下、結訓日相同（或同一結訓區間）、已完成結業之學員集合。母體一經凍結即不可中途更換；凍結時須同時記錄：
[TABLE]
欄位 | 定義 | 真實欄
cohort_id | 唯一追蹤批次代碼 | ____（留白）
course_id | 課程代碼 | ____（留白）
結訓日 | 完成日，追蹤90日以此起算 | ____（留白）
完成者人數 n | 分母基數 | ____（留白）
名冊來源 | 已授權完成者名冊之來源索引 | ____（留白）
納入規則 | 例：結訓日當天已完成結業、身分為學員 | ____（留白）
排除規則 | 例：已撤回同意、重複代碼、非完成者 | ____（留白）
追蹤基準日 | 結訓日後第90日；例示 2026-06-30 → 2026-09-28 | ____（留白）
聯絡授權及來源索引 | 有權者核定之聯絡依據 | ____（留白）
建立／覆核角色與日期 | 真實授權欄 | ____／____（留白）
版次 | 表單版本 | R07 候選工具；正式使用前由權責人核定
[/TABLE]
規則：(1) 分母固定為凍結母體人數，不以回覆者自成分母；(2) 有效回覆分子只計仍可依原同意範圍使用的完整或部分問卷，拒答（DECLINED）與撤回（WITHDRAWN）均不計分子；(3) 拒答與撤回者仍保留在凍結母體分母中並分開報數，撤回後如同意條款要求刪除，刪除其可識別回答且不納入分析；(4) 未回覆保留在分母並單列 UNKNOWN，不得列為失業；(5) 本例分母＝8，真實母體與分母 UNKNOWN，尚未獲准凍結。
三、聯絡授權與個資 HOLD 流程
聯絡前四項必要檢查（缺任一項即觸發對應 HOLD，禁止發出任何通知）：
1. 目的核可：本次聯絡目的已敘明並由有權者核定 → 否則 HOLD_NO_CONTACT_AUTHORITY。
2. 個資告知：已準備告知訊息（用途、保存期間、調閱對象、撤回權）→ 否則 HOLD_PRIVACY_POLICY。
3. 聯絡權限：承辦人經授權可依核准程序接觸該母體 → 否則 HOLD_NO_CONTACT_AUTHORITY。
4. 保存與調閱依據：回覆資料存哪、誰可調閱、保留多久 → 否則 HOLD_PRIVACY_POLICY。
執行順序與紀錄：核准程序 → 發出通知（記通知日／方式／送達證明代碼）→ 追蹤基準日起之回覆窗口內登錄回覆 → 若依核准程序允許，最多安排一次後續聯絡 → 仍無回覆記 UNKNOWN。沒有已核准延長程序時，承辦人不得自行延長回覆窗口或增加聯絡次數。
代理填寫禁止：核驗人、覆核日、責任人、期限等欄位，權責人未提供時一律留白並標 HOLD，不得代填或以示例填充。
四、問卷十二題（實際問項、選項與跳答／缺答規則）
每題逐題填錄答案代碼。個別題拒答記 NA_REFUSED；邏輯上不適用記 N_APPLICABLE；未回答、未收到或未核實記 UNKNOWN。正式輸入資料不得保留未註記空值。空白線與空格只代表尚未填寫的空白表單，不構成觀察值或零值。公開版只出現匿名追蹤代碼。
Q01 追蹤代碼／cohort：只填隨機非識別碼（含 cohort_id）。規則：缺 cohort 或出現重複碼 → 該份 HOLD_SOURCE_MISMATCH；不收姓名、電話、身分證。
Q02 追蹤目的與自願選擇：選項：同意參與／不同意（停止）／撤回（停止並保留紀錄）。規則：不同意或無聯絡依據 → 立即停止接觸；不同意記 DECLINED，不得視為負面成果。
Q03 結訓時狀態（基準）：受僱／自營接案／求職中／在學／暫無工作／其他／不願回答。規則：只用已核實之名冊基準或結訓時自陳；基準值缺漏不得以目前狀態回填。
Q04 目前狀態（追蹤基準日時點）：受僱／自營接案／求職中／在學／暫無工作／其他／不願回答／不適用。規則：缺答與「暫無工作」分開記；缺答＝UNKNOWN，不得算失業。
Q05 若狀態改變，改變月份與方向：填 YYYY-MM＋方向（如求職→受僱），未改變填 N_APPLICABLE，月份不清楚填 UNKNOWN，拒答填 NA_REFUSED。由受僱轉為非就業者仍記錄方向；若沒有新就業起始月，employment_start_month 填 N_APPLICABLE，不得寫成「未改變」。不問雇主名稱或地址；月份僅為自陳時點，不能單獨證明就業。
Q06 工作任務是否使用課程所學：經常／有時／尚未／無法判定／不適用。規則：屬自陳行為描述，不作因果計分；目前狀態非就業者多記 N_APPLICABLE。
Q07 描述一個不含個資的使用情境：開放題（可跳答）。規則：跳答不等於缺答失格；入公開稿前須去識別化，出現他人姓名即遮除。
Q08 自評訓練與目前狀態的關聯：0（無關）／1／2／3／4（高度相關）／無法判定／不願回答。規則：主觀歸因，非因果證據；不得加總成「訓練效果分數」。
Q09 同期其他影響因素（可複選）：自行求職準備／家庭因素／其他課程／景氣變化／雇主用人需求／其他／不願回答。規則：未答不等於沒有其他因素；複選結果只用於描述。
Q10 是否願意另行提供可選佐證核驗：同意／不同意／無文件可提供。規則：問卷本身不收原件；同意＝當事人自願且資料處理有權限時，才另行安排索取（REQUEST_EVIDENCE），不同意＝DECLINED。
Q11 可提供佐證類別（若 Q10 同意）：勞保投保資料／聘僱或任用文件／自營登記或交易紀錄／其他／無／不願回答。規則：原件不入公開版；只收至受限位置並建索引。
Q12 是否需要後續職涯或課程支持：需要／不需要／待確認（可附說明）。規則：僅登記需求，不得承諾就業或保證課程結果。
五、四張可操作表單
A. 母體與聯絡表（每 cohort 一張）
[TABLE]
欄位 | 本例填值（SYNTHETIC ONLY） | 真實欄
cohort_id / course_id | SYN-0116-COHORT-01 / SAMPLE-COURSE-01 | 空（HOLD）
結訓日／追蹤基準日 | 2026-06-30 / 2026-09-28 | 空
完成者 n | 8（合成） | 空
名冊來源 | 合成資料集 SYNTHETIC_DATASET_0116_R06.csv | 空（需合法完成者名冊）
納入／排除 | 全部八筆納入；無排除 | 空
用途 | 就業狀態追蹤紀錄示範 | 空（需核定）
聯絡授權 | SAMPLE_ONLY_NOT_REAL_CONSENT｜無真實授權 → HOLD_NO_CONTACT_AUTHORITY | 空
建立／覆核角色與日期 | 空 | 空＋HOLD
[/TABLE]
A2. 每次聯絡作業紀錄（每次實際嘗試一列）
每一次實際聯絡分開登錄，不可只在回覆表填最後結果。固定欄位如下；本次示範未提供任何送達方式、聯絡嘗試或送達證明，因此以下空列只供未來填寫，不代表已聯絡。
[TABLE]
欄位 | 填寫 / 選項
cohort_id | ____
匿名追蹤碼 | ____
預定追蹤日 | ____
實際聯絡日與時間 | ____
方式 | 電郵／簡訊／電話／其他
送達狀態及來源代碼 | 已送達／退回／未確認
嘗試序次 | 1 或 2（依核准程序）
回覆日 | ____
結果／下一步 | 已回覆／無回覆／拒答／撤回／待處理
[/TABLE]
操作規則：每列須有聯絡權限索引；沒有送達證據記 UNKNOWN，不得推定送達。最多一次後續聯絡僅在已核准程序允許時辦理；程序未核定或本人拒絕/撤回時停止聯絡並記 HOLD/DECLINED/WITHDRAWN。不得依本示範的回覆日期反推聯絡方式或聯絡次數。
B. 個別回覆登錄表（每人一列）
每份個別回覆以 cohort_id + 匿名追蹤碼作唯一 join key，與 A 母體表、A2 每次聯絡紀錄及 C 受限佐證索引勾稽。A2 可對同一人有多次獲准聯絡列；B 主表每人一列；B1 逐題續表每位回覆者一份，Q05–Q11 答案逐題填入；C 每一件或每一來源之索引另列一筆。不可只寫「另列於下表」而未標明表名與位置。
[TABLE]
欄位 | 填寫 / 選項
cohort_id | ____
匿名碼 | ____
Q02 狀態 | ____
Q03 基準狀態 | ____
Q04 目前狀態 | ____
回覆日 | ____
缺答／拒答／撤回處置 | ____
[/TABLE]
B1 逐題答案續表（每位回覆者一份；以 cohort_id + 匿名碼連結 A2 與 C）
[TABLE]
題號／欄位 | 答案或索引值 | 缺答碼／處理說明
cohort_id | ____ | 必填；缺漏即 HOLD_SOURCE_MISMATCH
匿名追蹤碼 | ____ | 必填；與母體及聯絡紀錄相同
Q05 狀態變化方向／月份 | ____ | N_APPLICABLE／UNKNOWN／NA_REFUSED 擇一註明
Q06 技能使用 | ____ | FREQUENTLY／SOMETIMES／NOT_YET／UNSURE／N_APPLICABLE
Q07 去識別化使用情境 | ____ | UNKNOWN 或 NA_REFUSED；公開前去識別
Q08 自評關聯（0–4） | ____ | UNKNOWN／NA_REFUSED，不得解讀為因果
Q09 同期其他因素 | ____ | UNKNOWN／NA_REFUSED；未選因素不等於沒有因素
Q10 另行提供佐證意願 | ____ | 未核實同意不得索取原件
Q11 可提供佐證類別 | ____ | 與 Q10 及 evidence_id 勾稽
evidence_id | ____ | 無文件填 NONE_PROVIDED，不表示已核驗
缺答／拒答／撤回處置 | ____ | UNKNOWN／NA_REFUSED／DECLINED／WITHDRAWN
填表與覆核角色／日期 | ____ | 未提供真實責任資料時留空並標 HOLD
[/TABLE]
C. 受限原件索引（每件一列；原件不入公開 GitHub）
一筆索引只連結一個文件來源，使用 cohort_id + 匿名追蹤碼 + evidence_id 對回 B1。真實原件僅存有權限的受限位置；公開表不留姓名、電話、雇主或原件影像。沒有收到文件時必須用 NONE_PROVIDED；沒有可核實欄位一律用 UNKNOWN，不可留空或用零代替。
[TABLE]
欄位 | 真實填寫值（空表使用） | 安全示範值（未提供原件）
evidence_id | ____ | NONE_PROVIDED
cohort_id | ____ | SYN-0116-COHORT-01
匿名追蹤碼 | ____ | SYN-0116-01
佐證類型／來源持有人代碼 | ____ | UNKNOWN
收件日期／授權用途索引 | ____ | UNKNOWN
核對欄位與適用期間 | ____ | UNKNOWN
遮罩、刪除規則 | ____ | UNKNOWN
受控位置代碼 | ____ | UNKNOWN
核驗角色／日期／結果 | ____ | UNKNOWN／HOLD
保存依據／調閱紀錄 | ____ | UNKNOWN
本例處理結論 | ____ | 沒有文件輸入；不得標 VERIFIED
[/TABLE]
本例安全示範列只表示未提供文件，不代表存在或核驗任何真實佐證。
D. 匯總、缺漏處置與判讀表
D1 指標彙總（分母固定為凍結完成者 cohort）
[TABLE]
指標 | 本例分子／分母與算式 | 結果及解讀限制 | 覆核角色／日期／公開決策
有效問卷回覆率 | 6 份可用完整或部分回覆／8 人；6/8×100% | 75.0%；僅描述本示範 | UNKNOWN；未授權真實發布
回覆者自陳受僱／自營比例 | 4／6；4/6×100% | 66.7%；只描述仍可使用之回覆者 | UNKNOWN；非全體就業率
樣本佐證提供率（輸入，不等於核驗） | 0 筆文件輸入／4 筆自陳就業；0/4×100% | 0%；只表示示範沒有原件輸入，不表示真實零就業 | UNKNOWN；不可稱已核驗
全體完成者就業比例 | UNKNOWN／8；未定義 | UNKNOWN；不得把未回覆視為失業 | HOLD
[/TABLE]
D2 回覆狀態對帳（拒答與撤回留在凍結分母）
[TABLE]
狀態 | 合成筆數 | 是否計入回覆率分子 | 凍結分母處理／後續動作
有效完整或部分回覆 | 6 | 是；撤回前回答只有在同意範圍仍允許使用時才計 | 留在分母
未回覆 NO_RESPONSE | 2 | 否 | 留在分母；結果 UNKNOWN；依核准窗口至多一次聯絡
拒答 DECLINED | 0 | 否 | 留在分母、分開報數並停止接觸
撤回 WITHDRAWN | 0 | 否 | 留在分母、分開報數；依同意條款刪除或排除既有回答
凍結母體對帳 | 8 | 不適用 | 6+2+0+0=8；差異非0即 HOLD_SOURCE_MISMATCH
[/TABLE]
D3 缺答、補件與判讀決策紀錄
[TABLE]
議題／待補欄位 | 本例狀態或處置 | 決策角色／日期 | 結案門檻／可否公開
Q05–Q11 題級缺答 | 未記錄或未回覆一律 UNKNOWN；不作「無」推論 | UNKNOWN | 補齊來源與逐題覆核後重算
第三方就業佐證 | 0/4 文件輸入；非真實零就業 | UNKNOWN | 不得標 VERIFIED；受權核驗後才可更新
個資告知、聯絡授權與保存依據 | 本示範無真實文件，維持 HOLD | UNKNOWN | 權責人確認流程前不得啟動真實追蹤
本例整體公開判讀 | 只限 SAMPLE_SYNTHETIC_ONLY 描述 | UNKNOWN | 真實結果 UNKNOWN／HOLD；不宣稱因果或改善
[/TABLE]
六、固定八筆 SYNTHETIC 示範（SYN-0116-COHORT-01）
全部八列標記 SAMPLE_SYNTHETIC_ONLY、data_origin=SAMPLE_SYNTHETIC_ONLY、consent_status=SAMPLE_ONLY_NOT_REAL_CONSENT。個人列與總數不可改動，除非升版並更新全部收據。
[TABLE]
匿名碼 | 回覆狀態／回覆日 | 基準→目前狀態 | 就業起始月 | 技能使用 | 自評關聯 | 其他因素 | 佐證
SYN-0116-01 | RESPONDED／2026-09-28 | 求職中→受僱 | 2026-08 | SOMETIMES | 2 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-02 | RESPONDED／2026-09-28 | 求職中→受僱 | 2026-08 | UNSURE | 1 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-03 | RESPONDED／2026-09-28 | 受僱→受僱 | N_APPLICABLE | FREQUENTLY | 2 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-04 | RESPONDED／2026-09-28 | 自營→求職中 | N_APPLICABLE | NOT_YET | 0 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-05 | RESPONDED／2026-09-28 | 受僱→求職中 | N_APPLICABLE | NOT_YET | 0 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-06 | RESPONDED／2026-09-28 | 在學→受僱 | 2026-09 | UNSURE | 1 | UNKNOWN | SELF_REPORT_ONLY／NONE_PROVIDED
SYN-0116-07 | NO_RESPONSE／UNKNOWN | 求職中→UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
SYN-0116-08 | NO_RESPONSE／UNKNOWN | 在學→UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
[/TABLE]
就業起始月為 N_APPLICABLE 的列：03 為受僱未改變；04、05 轉為求職中，沒有新的就業起始月。表中的基準→目前狀態仍保留方向資訊，不得將這三列誤讀為狀態均未改變。
代碼對照表（供登錄與核對；未知值不得改填為「否／無」）
[TABLE]
儲存代碼 | 中文顯示／定義
RESPONDED／NO_RESPONSE | 已收到可用完整或部分問卷／追蹤窗口內未收到問卷
DECLINED／WITHDRAWN | 明確拒絕後停止接觸／撤回後依同意範圍處理資料
UNKNOWN | 未答、未收到、未核實或來源不明；不等於失業、否或無
N_APPLICABLE／NA_REFUSED | 題目在該情境不適用／受訪者拒答單一題
EMPLOYED／SELF_EMPLOYED／JOB_SEEKING／STUDYING | 受僱／自營接案／求職中／在學
FREQUENTLY／SOMETIMES／NOT_YET／UNSURE | 經常使用所學／有時使用／尚未使用／無法判定
NOT_RECORDED | 欄位未記錄，按 UNKNOWN 處理；絕不代表「沒有其他因素」
SELF_REPORT_ONLY／NONE_PROVIDED | 僅受訪者自陳／沒有第三方文件輸入
SAMPLE_ONLY_NOT_REAL_CONSENT／SAMPLE_SYNTHETIC_ONLY | 合成同意欄旗標／全列均為合成示範，不是真實同意或真實紀錄
[/TABLE]
逐項準確摘要：有效回覆6份（01–06），未回覆2份（07、08）；拒答與撤回均為0，故 6+2+0+0=8。自陳目前受僱者為01、02、03、06；求職中為04、05；07、08未回覆、目前狀態 UNKNOWN。基準狀態分布仍為受僱2、自營1、求職中3、在學2。四筆就業自陳的第三方文件均為 NONE_PROVIDED，不能標 VERIFIED。Q09在八筆皆未提供因素內容，統一按 UNKNOWN 解讀，不得推論為「沒有其他因素」。同意欄旗標是合成值，非真實同意。
七、計算與統計口徑（全部算式）
1. 有效問卷回覆率＝仍可依同意範圍使用的完整或部分問卷份數÷凍結母體人數＝6/8×100%＝75.0%。明確拒答（DECLINED）與撤回（WITHDRAWN）不計分子，但仍留在凍結分母並分開列數；本例二者皆0。未回覆也留在分母，狀態為 UNKNOWN。
2. 回覆者自陳受僱／自營比例＝自陳目前狀態為受僱或自營之回覆者÷回覆者數＝4/6×100%＝66.7%。此值只描述回覆者，不外推至全體完成者，也不加權、不補值。
3. 樣本佐證提供率＝有第三方原件輸入之就業自陳÷自陳就業之回覆者＝0/4×100%＝0%。此數字僅表示本示範未附任何原件，不是協會真實零就業；真實就業率為 UNKNOWN。
4. 全體完成者就業比例＝UNKNOWN。第六節兩名列為 UNKNOWN，不得列為失業或直接併入回覆者分母。
5. 自評關聯平均（如有需要）＝(2+1+2+0+0+1)/6＝6/6＝1.0，僅為回覆者主觀自評之描述值，非訓練效果分數。
八、缺答、拒答、撤回處理與證據路由
缺答：Q03–Q11 個別未答或未核實 → 題級記 UNKNOWN；只在該題的有效答案統計中排除，不改變凍結母體與整體回覆率分母。Q04 缺答 ≠ 失業。空白只允許出現在尚未填寫的空白表單；提交資料若留空，驗收退回補註 UNKNOWN、N_APPLICABLE 或 NA_REFUSED。
拒答（DECLINED）：Q02 不同意即為個案拒答，留在凍結分母、排除有效回覆分子、單列拒答數並停止接觸。Q10 不同意只代表不提供可選文件，不得自動把整份已回覆問卷改成拒答；單題不願回答記 NA_REFUSED，該題排除且不作負面推估。
回覆率對帳式：凍結母體 n = 有效完整/部分回覆 + NO_RESPONSE + DECLINED + WITHDRAWN + 其他待核狀態；各狀態須互斥且合計等於 n，否則 HOLD_SOURCE_MISMATCH。回覆率分子只納入仍可合法使用的完整或部分問卷；拒答與撤回永不計入分子，亦不得從凍結分母中刪除。示範：8 = 6 + 2 + 0 + 0，6/8=75.0%。
撤回（WITHDRAWN）：撤回後不得再聯絡，該個案保留在凍結分母並單列撤回數，不計入有效回覆分子。撤回前回答只有在原同意條款仍允許使用時才可分析；若要求刪除，依授權政策刪除或不可逆去識別並留存最小化處理收據。未確認處理依據前維持 HOLD。
證據等級與路由決策（每筆就業自陳逐一判定，本例權責人欄均留白 → 全部在真實運作前維持 HOLD）：
[TABLE]
狀態 | 進入條件 | 本示範結果
VERIFIED | 有合法來源、適用範圍、原件索引、核對結果，且由有權真人確認 | 0筆（示範未提供任何核驗原件）
SELF_REPORT_ONLY | 僅就業狀態為受僱之回覆者自陳 | 4筆（01、02、03、06；另2筆為求職中）
REQUEST_EVIDENCE | 當事人自願同意且資料處理有權限 | 0筆（本例同意旗標非真實）
HOLD_NO_CONTACT_AUTHORITY | 缺聯絡授權 | 全案成立（承辦人欄留白）
HOLD_SOURCE_MISMATCH | cohort 或名冊來源不一致 | 未成立（synthetic 內一致；真實接入前仍須核對）
HOLD_PRIVACY_POLICY | 缺個資告知／保存／調閱依據 | 全案成立
UNKNOWN | 未回覆、不清楚、無資料 | 2筆（07、08）
DECLINED | 拒答或不同意 | 0筆
REJECTED | 原件不適用、日期超出、來源不明、重複件或用途不合法（需記理由） | 0筆
[/TABLE]
退件門檻（任一成立即 HOLD／REJECT，只擋本文件、不封鎖其他文件）：缺母體來源或分母；把未回覆當失業；把自陳當第三方核驗；日期或 cohort 不一致；無聯絡或資料用途依據；分母混用；把自評因果化；小樣本誇大為顯著效果；公開資料含可識別內容；SAMPLE／REAL 混寫；以0115知識分享或0117考照資料替代就業；把索引127寫成紙本印刷序號。
九、判讀限制與行動決策紀錄
判讀限制：(1) 六筆回覆、兩筆未回覆，樣本極小，66.7% 僅描述該示範，不得推論顯著性或趨勢；(2) 未回覆與失業混同污染風險，禁止以回覆者率推估全體就業率；(3) 就業自陳無一附原件，證據強度止步 SELF_REPORT_ONLY；(4) 技能使用與自評關聯是隨時間變動的主觀回答，不得當作訓練因果評量或顧客價值證據；(5) 結果對「誰被納入母體」高度敏感，母體規則未經核定前任何真實數字都不可發布。
行動決策紀錄（真實運作時逐項填寫，本示範全部留白＋HOLD）：
[TABLE]
決策項 | 欄位 | 本示範狀態
是否建立真實 cohort | cohort_id、結訓日、n、名冊來源 | 空｜HOLD_SOURCE（無名冊）
是否開始聯絡 | 授權索引、個資告知版本 | 空｜HOLD_NO_CONTACT_AUTHORITY / HOLD_PRIVACY_POLICY
是否索取佐證 | 同意者、REQUEST 日、到期日 | 空
是否核驗 | 核驗角色、核對結果、VERIFIED 註記 | 空
判讀發布 | 分母覆核、限制說明、可否公開 | 空（真實發布前禁）
[/TABLE]
跨文件界線：0115／I19-E02 是心得與知識分享文件，不提供就業分母或就業數字；0117／I19-E04 是考照追蹤文件，不與本件共用分母或例數。0100、0101 等其他課程文件不提供本例事實；不同案例不共用 fact_id。僅在已核實相同 cohort、相同期間與來源索引後，才可互相引用，且不得拼接分子分母。
十、真實資料替換清單（Evidence Replacement Checklist — 收尾必核對）
替換 SAMPLE 前須備齊：合法完成者名冊（含納入/排除規則與凍結分母）、母體與聯絡依據、個資告知與保存/調閱規則、實際問卷回收、追蹤日期、受限原件索引、獨立核驗紀錄、覆核與保存規則；原件不得上傳公開 PR。逐項核對：
[TABLE]
# | 項目 | 現狀 | 最小替換與驗收條件
1 | SYN-0116-COHORT-01 八名完成者 cohort | SAMPLE_SYNTHETIC_ONLY | 已授權完成者名冊＋納入/排除規則＋凍結分母；排除公開個人識別碼
2 | SYN-0116-01..08 追蹤代碼 | SAMPLE_SYNTHETIC_ONLY | 已授權假名ID，僅在受保護來源內對接真實身分
3 | SYN-0116-RESP-06 六份回覆 | SAMPLE_SYNTHETIC_ONLY | 含日期的實際問卷回收＋含拒答/撤回之送達與聯絡紀錄
4 | SYN-0116-EMP-04 4/6 自陳就業 | SAMPLE_SYNTHETIC_ONLY | 實際回覆紀錄；分母與缺答覆核後方可發布
5 | SYN-0116-VER-00 0/4 書面佐證 | SAMPLE_SYNTHETIC_ONLY | 合法佐證＋來源索引、範圍、日期、核驗角色與受控存放
6 | SYN-0116-DATE-90 90日基準日 2026-09-28 | SAMPLE_SYNTHETIC_ONLY | 實際結訓日＋核准之追蹤間隔
7 | SYN-0116-SKILL 技能使用與關聯答項 | SAMPLE_SYNTHETIC_ONLY | 實際問卷回答；自陳歸因不得當因果
8 | SYN-0116-CONSENT 同意旗標 | SAMPLE_SYNTHETIC_ONLY | 實際告知/同意依據與聯絡授權；替代示例旗標
[/TABLE]
替換後每筆重新計算，重寫第七節算式與第六節表格，建立新收據；舊收據不可沿用。以上清單完成前，本件全部數字維持 SYNTHETIC ONLY，真實就業成果狀態為 UNKNOWN／HOLD。
<<<END MATERIAL>>>

# MATERIAL: 0116 official source packet SHA256=3430b1a95755ad773e12380cf1c0b599dbf4b057d1a0f34f47b7dee51fa08c9d

<<<BEGIN MATERIAL>>>
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
<<<END MATERIAL>>>

# MATERIAL: 0116 unique Blueprint SHA256=6932127686187f201bc41315fb2e6ae98003767053f7dad2d4061e6d46428263

<<<BEGIN MATERIAL>>>
# UNIQUE BLUEPRINT｜0116 / I19-E03｜R01

狀態：候選正文規格，不是協會正式表單或已執行調查。

## 1. 文類、讀者與遮題測試
文類是「訓後追蹤調查表＋回覆登錄／證據等級分析工作表」。讀者為訓練行政承辦人及查核人員。拿到文件可凍結追蹤母體、安排90日追蹤、記錄未回覆、區分自陳與原件、重算有限範圍統計，並決定 HOLD / REQUEST / VERIFIED。遮住標題仍可辨識為結訓學員90日就業狀態追蹤；不能誤認為滿意度問卷、薪資調查、雇主滿意調查或就業證明原件。

## 2. 官方命題及禁止外推
對應官方指標19、1分參考佐證「口頭說明學員訓後就業狀況，但未有具體紀錄及評量」。本件提供補足紀錄的方法，不證明原始點協會已有就業成果，也不自行評分。157 Blueprint索引127是內部位置，紙本方框印刷號 UNKNOWN_NOT_ASSERTED。

## 3. 承辦流程與異常分支
1. 結訓時建立唯一cohort、課程ID、完成日、母體來源、納入/排除規則並凍結分母。
2. 聯絡前確認目的、個資告知、聯絡權限與保存依據；缺一則HOLD_NO_CONTACT_AUTHORITY或HOLD_PRIVACY_POLICY。
3. 追蹤基準日按完成日後90天計算，實際聯絡窗口須有已核准程序；沒有程序不可自行延長。
4. 只使用隨機代碼，不在公開表或問卷填個人姓名、身分證、電話、雇主名稱。
5. 通知、送達、回覆、不回覆、拒答、撤回分列；未回覆不等於失業。
6. 用逐題問卷記錄基準狀態、目前狀態、技能使用、自評關聯、其他因素、可選佐證類型。
7. 自陳原答與第三方文件分開。原件只存受權限保護位置；公開表只記索引、核驗範圍、核驗角色和日期。
8. 覆核母體、日期、缺答、重複碼、分母和證據等級；核驗人未提供時不得代填。
9. 報告分子、分母、未回覆數、拒答數、證據層級、來源和限制。
10. 判斷VERIFIED、SELF_REPORT_ONLY、REQUEST_EVIDENCE、HOLD、UNKNOWN或REJECTED；責任人和期限只能由有權者填寫。
11. 到期未回覆依核准程序最多安排一次後續聯絡；仍未回覆記UNKNOWN，不推定結果。
12. 只有相同且已核實cohort才可連回結案或其他追蹤文件；不得跨件混用不同樣本。

## 4. 完整問卷題目
Q01 追蹤代碼/cohort：只填隨機非識別碼；缺cohort或重複碼HOLD。
Q02 追蹤目的及自願選擇：同意/不同意/撤回；不同意或無聯絡依據即停止。
Q03 結訓時狀態：受僱/自營接案/求職/在學/暫無工作/其他/不願回答；只用已核實基準來源。
Q04 目前狀態：受僱/自營接案/求職/在學/暫無工作/其他/不願回答/不適用；缺答與失業分開。
Q05 若狀態改變，月份與方向：YYYY-MM/未改變/不清楚/不願回答；不問雇主名稱或地址。
Q06 工作任務是否使用課程所學：經常/有時/尚未/無法判定/不適用；屬自陳。
Q07 描述一個不含個資的使用情境：開放題/跳答；公開稿須去識別。
Q08 自評訓練與目前狀態的關聯：0無關至4高度相關/無法判定/不願回答；主觀歸因、非因果證據。
Q09 同期其他影響因素：自行求職/家庭因素/其他課程/景氣/雇主需求/其他/不願回答；可複選，未答不等於沒有。
Q10 是否願意另行提供可選佐證核驗：同意/不同意/無文件；問卷本身不收原件。
Q11 可提供佐證類別：投保/聘僱/自營登記或交易/其他/無/不願回答；不在公開版貼原件。
Q12 是否需要後續職涯或課程支持：需要/不需要/待確認及可選說明；不得承諾就業。

## 5. 必備可填表
A 母體與聯絡表：cohort/course、結訓日、完成者n、名冊來源、納入排除、追蹤日、用途、聯絡授權及來源索引、建立/覆核角色日期、版次。
B 個別回覆表：匿名碼、聯絡日/方式/送達、回覆日、同意/拒答/撤回、基準/目前狀態、改變月份、技能使用、自評關聯、其他因素、佐證類別/索引、核驗、缺漏、後續處置、覆核。
C 受限原件索引：evidence_id、類型、收件日、來源持有人、授權用途、核驗欄位、遮罩與刪除規則、受控位置代碼、核驗角色/日期/結果、保存依據、調閱紀錄。原件不入公開GitHub。
D 匯總判讀表：指標、分子、分母、公式、拒答/缺答、結果、證據層級、限制、可否作公開主張、補資料與決策角色。

## 6. 固定合成案例與計算
唯一dataset為SYNTHETIC_DATASET_0116_R01.csv，cohort SYN-0116-COHORT-01，結訓2026-06-30、90日基準日2026-09-28。八個匿名合成ID，六份回覆、兩個未回覆；四名回覆者自陳受僱/自營、兩名求職中；四筆就業自陳沒有任何實際第三方證明輸入。個人列和總數不可改動，除非升版且更新所有收據。
- 回覆率=6/8=75.0%，分母是本例八名完成者。
- 回覆者自陳受僱/自營比例=4/6=66.7%，只限回覆者。
- 佐證核驗率=0/4=0%，只表示本示範未附原件；不是協會真實零就業。
- 全體完成者就業比例=UNKNOWN；未回覆兩人不可列為失業或直接併入回覆者分母。
- 不可由本問卷推出訓練造成就業、就業率改善或顧客價值提升。

## 7. 証據狀態與決策
VERIFIED：合法來源、適用範圍、原件索引、核對結果均由有權真人確認。
SELF_REPORT_ONLY：只有受訪者說明，可作有限描述。
REQUEST_EVIDENCE：當事人自願同意且資料處理有權限時，才可另行索取。
HOLD_NO_CONTACT_AUTHORITY：沒有聯絡授權。
HOLD_SOURCE_MISMATCH：cohort/名冊來源不一致。
HOLD_PRIVACY_POLICY：缺個資告知、保存或調閱依據。
UNKNOWN：未回覆、不清楚或沒有資料。
DECLINED：拒答/不同意，不能視為負面成果。
REJECTED：原件不適用、日期超出、來源不明、重複件或用途不合法；需記理由。

## 8. 退件門檻
缺母體來源或分母；把未回覆當失業；把自陳當第三方核驗；日期/cohort不一致；沒有聯絡或資料用途依據；分母混用；把自評因果化；小樣本誇大成顯著效果；公開資料含可識別內容；SAMPLE/REAL混寫；以0115知識分享或0117考照資料替代就業；把Blueprint索引127寫成紙本印刷序號。任一項成立即HOLD/REJECT，依原因阻擋本文件，不封鎖其他文件。

## 9. 鄰件及真實替換
0115/I19-E02只支持知識分享；0117/I19-E04只支持考照追蹤。僅在核實相同cohort、期間和來源後可互相引用，不得共用或拼接分子分母。所有核定者、承辦人、覆核日、政策版本均留真實授權欄。替換SAMPLE需取得合法完成者名冊、定義明確的母體、聯絡依據、實際答卷、追蹤日期、受限原件索引、核驗紀錄、覆核與保存規則；每筆重新計算，保護個資。

## 10. Writer交付驗收
文件須完整列出12題、四張操作表、聯絡與缺漏流程、證據級別、八筆固定示範、全部算式與限制、REAL替換清冊、鄰件區隔及可執行的HOLD/REJECT決策。正文不能只留空表或只描述流程。不可更改來源映射或合成數字；若必須更改先提出Blueprint差異和新版本，舊收據不可沿用。

<<<END MATERIAL>>>

# MATERIAL: Synthetic dataset R06 (unchanged fixed source) SHA256=76c80580eb677278dc94f88608f3c8d36a5a37b61a25ac0bd791379373706adf

<<<BEGIN MATERIAL>>>
case_id,cohort_id,course_id,completion_date,followup_due_date,response_date,response_status,baseline_status,followup_status,employment_start_month,training_skill_use,training_relation_self_rating_0_4,other_factors_status,evidence_class,evidence_index,consent_status,data_origin
SYN-0116-01,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,JOB_SEEKING,EMPLOYED,2026-08,SOMETIMES,2,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-02,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,JOB_SEEKING,EMPLOYED,2026-08,UNSURE,1,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-03,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,EMPLOYED,EMPLOYED,N_APPLICABLE,FREQUENTLY,2,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-04,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,SELF_EMPLOYED,JOB_SEEKING,N_APPLICABLE,NOT_YET,0,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-05,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,EMPLOYED,JOB_SEEKING,N_APPLICABLE,NOT_YET,0,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-06,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,2026-09-28,RESPONDED,STUDYING,EMPLOYED,2026-09,UNSURE,1,UNKNOWN,SELF_REPORT_ONLY,NONE_PROVIDED,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-07,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,UNKNOWN,NO_RESPONSE,JOB_SEEKING,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY
SYN-0116-08,SYN-0116-COHORT-01,SAMPLE-COURSE-01,2026-06-30,2026-09-28,UNKNOWN,NO_RESPONSE,STUDYING,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,SAMPLE_ONLY_NOT_REAL_CONSENT,SAMPLE_SYNTHETIC_ONLY

<<<END MATERIAL>>>

# MATERIAL: Synthetic replacement register R06 (unchanged fixed source) SHA256=6d3071d7b9ba8091ccd0fbed1af7bb38ea5c85467d2f8b70a30272dfac6d4650

<<<BEGIN MATERIAL>>>
item_id,data_or_claim,status,source_or_owner,real_replacement_required,minimum_replacement_and_acceptance
SYN-0116-COHORT-01,cohort of eight completers,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,authorized course roster with inclusion/exclusion rules and frozen denominator; exclude public personal identifiers
SYN-0116-01..08,respondent tracking codes,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,authorized pseudonymous IDs linked only in protected source
SYN-0116-RESP-06,6 responses from 8,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,actual dated questionnaire returns and delivery/contact log including refusal/withdrawal
SYN-0116-EMP-04,4/6 self-reported employed or self-employed,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,actual response records; publish only after denominator and missingness verified
SYN-0116-VER-00,0/4 documentary evidence in sample,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,lawful evidence with source index, scope, date, verifier role and access-controlled storage
SYN-0116-DATE-90,90-day follow-up 2026-09-28,SAMPLE_SYNTHETIC_ONLY,blueprint example,YES,actual course completion date and approved follow-up interval
SYN-0116-SKILL,skill use and training relation answers,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,actual survey responses; self-attribution must not be treated as causality
SYN-0116-CONSENT,consent flags,SAMPLE_SYNTHETIC_ONLY,synthetic dataset,YES,actual notice/consent basis and contact authority; replace illustrative flags

<<<END MATERIAL>>>

# MATERIAL: Official page 7 text SHA256=48865d4f23eb5459153c879a859e0d0d21e4a9b306644116d2d35d75c56acc67

<<<BEGIN MATERIAL>>>
 
7 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
的效果。 
4分 目標客戶及學員
認為訓練有顯著具體
績效。 
認為訓練有達成能力提升的效
果。 
 執行目標客戶及學員滿意度調查
及分析（系統及流程面） 。 
 提出目標客戶及學員對訓練達能
力提升之說明（學習技能面） 。 
 學員培訓前後自我評量表 及雷達
分析圖呈現提升效果。 
 指導學員參加技能競賽獲獎。 
 感謝函。 
 證照獲取率。 
 其他： 
3分之常見參考佐證資料： 
 問卷調查及課後行動計 畫評估表
等顯示目標客戶及學員認為訓練
有績效改善的效果。 
 提出目標客戶及學員對訓練達組
織績效改善之說明（財務面） 。 
 高證照通過率之證明資料。 
 提高薪資紀錄。 
 社群網站知識討論區，人員使用
網站頻率高。 
 其他： 
4分之常見參考佐證資料： 
 問卷調查及課後行動計 畫評估表
等顯示目標客戶及學員認為訓練
對組織績效的改善 及提升均有顯
著的效果。 
 提出目標客戶及學員對訓練達特
殊 績 效 之 說 明 （ 社 會 面 、 其
他） 。 
 輔導考照 及 學 員 回 訓 率 持 續 提
高。 
 會員人數逐年增加。 
 其他： 
 
19. 訓 練 系 統 的 市
場功能 
─ 目標市場
及顧客的價
值創造 
評分標準： 
1分 目標市場及顧客
價值均有提升，然而
未有具體紀錄及評
量。 
2分 目標市場及顧客
價值均有部分提升效
果。 
1 分之常見參考佐證資料： 
 目標市場及顧客價值均有提 升，
然而未有具體紀錄及評量。 
 提出心得與知識分享執行成效
（系統及流程面） 。 
 口頭說明學員訓後就業狀況，但
未有具體紀錄及評量。 
 學員考照通過率有增加，但未有
<<<END MATERIAL>>>

# MATERIAL: Official page 8 text SHA256=57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e

<<<BEGIN MATERIAL>>>
 
8 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
3分 目標市場及顧客
價值均有一定程度提
升的效果。 
4分 目標市場及顧客
價值均有顯著具體的
提升績效。 
具體紀錄及評量。 
 感謝函。 
 其他： 
2 分之常見參考佐證資料： 
 有具體紀錄可辨識目標市場及顧
客價值均有部份提升效果。 
 相關證據顯示有初步訓練成果，
且有部份佐證資料。 
 提出學員滿意度、考試測驗或心
得報告（學習技能面） 。 
 提出課後追蹤調查與分析結果、
證照通過情形（學習技能面） 。 
 部份會員透過訓練後，事業成就
上突破原有格局。 
 企業主雇用結訓後學員，肯定機
構訓練的成效。 
 部份學員能運用所學於職務中。 
 進行訓後薪資調查，部份訓後學
員微幅調薪。 
 其他： 
3 分之常見參考佐證資料： 
 有量化之效益可呈現目標市場及
顧客價值均有一定程度提 升的效
果。 
 相關證據顯示個人訓練後之績效
改善成果。 
 提出市場競爭力、營業額、工作
流程、成本控制或客訴率等營運
表現（財務面） 。 
 學員訓後創業案例。 
 學員證照通過、就業率高。 
 個人產品不良件數有下降趨勢。 
 每年訓練班次、人次均持續成
長。 
 會員人數及會費收入均逐年增
加。 
 其他： 
4 分之常見參考佐證資料： 
 經營績效中之數據呈現目標市場
及顧客價值均有顯著具體的提 升
績效。 
 提出參與社會公益活動、獲頒公
民營單位獎項、結合學校單位產
<<<END MATERIAL>>>

# MATERIAL: I19 writing guidance excerpt SHA256=c5bbf601105fff9eca65b36206003f6db00d66d6cabdc86451db83663894637d

<<<BEGIN MATERIAL>>>
# I19 writing guidance excerpt

Source: current PR #92 `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md`, Git blob 4ff863d9f534b6359fc1c7c1685bd8cce02da886. This concise working excerpt paraphrases that source.

For I19, do not substitute learner satisfaction for external market or client value. For an exam/pass-rate evidence tool, make the population, eligible cohort, exam period, denominator, numerator, verification source, follow-up window and missing/retake handling explicit. Keep each evidence purpose distinct. If real operating data or third-party sources are unavailable, provide a full practical SAMPLE tool and clearly leave real performance UNKNOWN; never claim a real score, increase, certificate, approval or audit result. Include usable questions/fields/forms, calculation definitions, complete synthetic examples, limitations and a source-based evidence replacement path. Distinguish internal Blueprint indices from official printed checkbox serials.

<<<END MATERIAL>>>

### PRIOR EXACT-SHA REVIEW — R06 FINDINGS AS DEFECT CONTEXT ONLY
<<<BEGIN MATERIAL>>>
# Independent Semantic Review — 0116 / I19-E03 / Blueprint 127 / candidate R06

**Verdict: PASS (semantic only)** — bound to the exact DOCX SHA-256 below. PASS covers content semantics only; it is not formal acceptance of any TTQS score, association performance, or layout (visual review is the coordinator's separate scope).

**SHA binding**

| Item | Value | Binding status |
|---|---|---|
| DOCX SHA-256 (review scope) | `eb4c1efef5bb4f7888e29f4c202c3c2d44997cfd0f31131253294bc564679af2` | Three-way consistent: review request ↔ extraction header `DOCX_SHA256` ↔ R06 technical QA `docx_sha256`. Not independently recomputed (no tools) → consistency verified, byte-level hash UNKNOWN |
| Extraction inspected | `6560270d…bc6e9` (header + QA receipt agree) | consistent |
| Dataset inspected | `76c80580…06adf` (material header + QA receipt agree) | consistent |
| Source packet | `3430b1a9…08c9d` (header + QA receipt + packet material agree; now 64 hex — R05 F1 fixed) | consistent |

**Method statement:** no tools used, no files read or modified, no visual/layout inspection performed. Only the attached packet was examined; receipts (technical QA, Word render) were read as scoped attestations, not proof.

---

## Scope actually inspected

| Inspected in full | Attested only (not verifiable here) | Out of scope → UNKNOWN |
|---|---|---|
| R06 exact-DOCX extraction, header + §1–§10 incl. all 14 tables and Q01–Q12; source packet R01; unique Blueprint R01; R06 synthetic dataset (8 rows × 17 cols); R06 replacement register (8 rows); official PDF p.7 and p.8 text excerpts; I19 guidance excerpt; R05 review (used only to re-test each prior finding myself) | 157 Blueprint file row 127; crosswalk CSV row; full genre manual / mission doc; PR #92 blobs; all SHA-256 values | DOCX bytes; Word-native PDF and 12 page rasters (render receipt `visual_review: PENDING`; coordinator did this separately); fonts/page breaks/clipping; paragraph count 92 |

Partial extraction-completeness check performed: the 14 `[TABLE]` blocks in the extraction map one-to-one and in order to the QA receipt's `table_shapes` (12×3 §2, 9×3 A, 10×2 A2, 8×2 B, 13×3 B1, 12×3 C, 5×4 D1, 6×4 D2, 5×4 D3, 9×8 §6 demo, 10×2 code dictionary, 10×3 §8 routing, 6×3 §9 action, 9×4 §10 checklist). Table-level extraction fidelity is therefore corroborated; paragraph fidelity is not.

---

## Prior R05 findings — disposition (each re-verified against R06 content)

| ID | R05 severity | R06 status | Evidence / locator |
|---|---|---|---|
| F1 malformed 40-char source-packet SHA | MAJOR | **FIXED** | Header `SOURCE_PACKET_SHA256=3430b1a9…08c9d` is 64 hex and matches the packet material header and QA receipt `source_packet_sha256` |
| F2 false「未改變」on rows 04/05 | MAJOR | **FIXED** | §6 demo table: 03/04/05 就業起始月 = `N_APPLICABLE`; post-table prose:「03 為受僱未改變；04、05 轉為求職中，沒有新的就業起始月…不得誤讀為狀態均未改變」; QA check `false_unchanged_rows_removed: true` |
| F3 dangling B cross-reference | MINOR | **FIXED** | §5 Form B prose now names the continuation (`B1 逐題答案續表…Q05–Q11`; `C 每一件…另列一筆`) and forbids unnamed「另列於下表」; B1 table now exists (13×3) |
| F4 Form B missing contact fields / no join rule | MINOR | **FIXED** | §5 A2 table (每次聯絡作業紀錄: 實際聯絡日/方式/送達狀態/嘗試序次/回覆日/結果) + explicit join rule「cohort_id + 匿名追蹤碼作唯一 join key，與 A、A2、C 勾稽」 |
| F5 Form C prose-only | MINOR | **FIXED** | §5 Form C is now a fillable 3-column table (11 field rows incl. 核驗角色/日期/結果、保存依據/調閱紀錄、受控位置代碼) with NONE_PROVIDED/UNKNOWN safe-demo values |
| F6 Form D incomplete columns | MINOR | **FIXED (substantively)** | Required content now present across D1 (指標/算式/結果與限制/覆核角色與公開決策), D2 (拒答/撤回是否計入分子、凍結分母處理), D3 (缺答、補件、決策角色/日期、結案門檻/可否公開) |
| F7 no code↔option dictionary | MINOR | **FIXED** | §6 代碼對照表 maps RESPONDED/NO_RESPONSE, DECLINED/WITHDRAWN, UNKNOWN, N_APPLICABLE/NA_REFUSED, EMPLOYED/SELF_EMPLOYED/JOB_SEEKING/STUDYING, FREQUENTLY/SOMETIMES/NOT_YET/UNSURE, NOT_RECORDED, SELF_REPORT_ONLY/NONE_PROVIDED, SAMPLE flags |
| F8 unannotated dataset blanks / undefined「—」 | MINOR | **FIXED** | R06 dataset has no blank cells (rows 07/08 = UNKNOWN; rows 03/04/05 start month = N_APPLICABLE); candidate renders only defined codes; QA `no_undefined_dataset_blanks: true` |
| F9 DECLINED/WITHDRAWN numerator rule unstated | MINOR | **FIXED** | §2 rules (2)(3), §7.1「不計分子，但仍留在凍結分母並分開列數」, §8「永不計入分子，亦不得從凍結分母中刪除」, D2 table |
| F10「佐證核驗筆數」label vs rate | LOW | **FIXED** | D1 row 3 renamed「樣本佐證提供率（輸入，不等於核驗）0/4×100%」 |
| F11 ambiguous serial wording | LOW | **MOSTLY FIXED** | Header now states「此為內部索引，官方紙本 checkbox 印刷序號 UNKNOWN_NOT_ASSERTED」and §8 retire threshold names「把索引127寫成紙本印刷序號」; residual grammar note = ADVISORY-3 |
| Ob1 receipts unverifiable | OBS | **Open by design** | See Visual scope limitation |
| Ob2 official text attested only | OBS | **Mostly resolved** | Official p.7/p.8 text now attached and verified verbatim (see below); crosswalk/157 row still attested |

---

## Criterion-by-criterion results

**1. Official purpose fit — PASS.** Official p.7 text (attached) reads exactly: 指標19「訓練系統的市場功能─目標市場及顧客的價值創造」, 1分參考佐證「口頭說明學員訓後就業狀況，但未有具體紀錄及評量」. Candidate §1 positions itself as the tool to convert oral information into traceable records,「不自行評分」,「不得宣稱達到2至4分成果」— correct, since attached p.8 shows 2–4分 require completed survey/analysis, pass rates, salary records, etc., none of which exist here. No self-scored claim anywhere; QA `no_formal_acceptance_claim: true`.

**2. Title-blind genre fit + negative neighbors — PASS.** With the title removed, the content is unmistakably a post-training employment follow-up survey plus response-logging/evidence-classification worksheet (Q01–Q12 employment-status items, frozen cohort denominator, response-status accounting, evidence routing). Negative neighbors excluded: satisfaction survey (Q08「主觀歸因，非因果證據；不得加總成訓練效果分數」; §1 hard line 4), salary survey (no salary field anywhere; the old 0116_138 salary-survey proposition is absent), employer-satisfaction survey (no employer-respondent items; Q10/Q11 collect only learner-side optional evidence), certificate originals (原件不入公開版, C is index-only), certification tracking (no pass-rate denominator — that is 0117).

**3. Working survey/follow-up forms — PASS.** Q01–Q12 all present, distinct, with full option sets and per-item skip/missing rules (Q05 direction+month logic incl. the non-employment transition rule; Q07 skip ≠ disqualification + de-identification; Q10 refusal ≠ whole-questionnaire refusal). Forms A, A2, B, B1, C, D1–D3 are all fillable tables (14-table inventory corroborated against the QA receipt). Contact pre-checks, HOLD codes, no-self-extension rule, one-follow-up-contact cap, and proxy-fill prohibition all present (§3, A2).

**4. Case joins — PASS.** Join chain cohort_id + 匿名追蹤碼 (+ evidence_id for C) is stated explicitly in §5 B/B1 prose and is consistent across A (SYN-0116-COHORT-01 / SAMPLE-COURSE-01 / n=8 / 2026-06-30→2026-09-28), A2, B, B1, C safe-demo values (SYN-0116-01, evidence_id NONE_PROVIDED) and the dataset's case_id/cohort_id columns. B1's Q05–Q11/evidence_id rows line up with §4 and with C's per-item index rows; no「另列於下表」dangling reference remains.

**5. Arithmetic / denominators / status codes — PASS** (recomputation table below). Frozen-denominator rule, mutually exclusive statuses, and UNKNOWN ≠ unemployment are enforced consistently in §2, §7, §8 and D2.

**6. SAMPLE/REAL boundary — PASS.** SAMPLE_SYNTHETIC_ONLY throughout: header, §1 four hard lines, §5 A (HOLD_NO_CONTACT_AUTHORITY), §5 C note, §6 row flags + code dictionary, §7 (真實就業率 UNKNOWN), §8 routing (VERIFIED 0, REQUEST_EVIDENCE 0, HOLD whole-case), §9, §10. No fabricated roster, consent, contact, delivery, employment proof, verifier, signature, approval or score. Consent flags are explicitly non-real.

**7. Replacement register completeness — PASS.** §10 checklist items 1–8 map 1:1 to register rows (COHORT-01, 01..08, RESP-06, EMP-04, VER-00, DATE-90, SKILL, CONSENT) with the same minimum acceptance conditions (authorized roster + inclusion/exclusion + frozen denominator; protected pseudonymous IDs; dated actual returns + delivery log; evidence with source index/scope/date/verifier/controlled storage; actual completion date + approved interval; consent/authority basis). Includes the recompute-and-reissue-receipts rule and the originals-not-in-public-PR rule.

**8. Human usability — PASS with advisories.** An administrator can execute the full flow (freeze → authorize → contact → log → classify → compute → decide) from the document alone; an auditor can recompute every figure. Residual nits are ADVISORY-1/3 only.

**9. Cross-document consistency (0115/0117) — PASS.** §8 cross-boundary + retire thresholds: 0115/I19-E02 = knowledge sharing, 0117/I19-E04 = certification tracking; no shared denominators or spliced numerators; fact_id separation; 0100/0101 excluded as fact sources; cross-reference permitted only after verified same cohort/period/source index. Matches the source packet exactly.

---

## Arithmetic recomputation (independent)

| Check | Recomputation | Candidate claim | Result |
|---|---|---|---|
| Response rate | 6 ÷ 8 = **75.0%** | 6/8 = 75.0% | ✅ |
| Respondent employed/self-employed | currently employed 01,02,03,06 = 4; self-employed now 0; 4 ÷ 6 = **66.7%** | 4/6 = 66.7% | ✅ |
| Documented-evidence input rate | 0 of 4 employment self-reports (all NONE_PROVIDED); **0%** | 0/4 = 0% | ✅ |
| Self-rating mean | (2+1+2+0+0+1) ÷ 6 = 6 ÷ 6 = **1.0** | 1.0 | ✅ |
| Baseline distribution | EMPLOYED 2 (03,05), JOB_SEEKING 3 (01,02,07), SELF_EMPLOYED 1 (04), STUDYING 2 (06,08) = 8 | 2/3/1/2 | ✅ |
| Status reconciliation | 6 + 2 + 0 + 0 = **8**; statuses mutually exclusive | same | ✅ |
| 90-day date | 2026-06-30 + 90 d = 2026-07-31 (d31) → 2026-08-31 (d62) → **2026-09-28 (d90)** | 2026-09-28 | ✅ |
| Row-by-row vs R06 dataset | all 8 rows: response status/date, baseline→current, start month, skill use, rating, evidence class/index, consent, origin | — | 8/8 on all substantive fields; only 其他因素 token on rows 01/02/06 differs → ADVISORY-1 |
| Routing counts | employment self-reports: SELF_REPORT_ONLY 4, VERIFIED 0, REQUEST 0, REJECTED 0; UNKNOWN 2 (07,08); DECLINED 0; whole-case HOLD_NO_CONTACT_AUTHORITY / HOLD_PRIVACY_POLICY | same | ✅ (scope sentence「每筆就業自陳逐一判定」present; see Observation) |
| Question set / retire thresholds / register items | Q01–Q12 = 12 distinct; §8 thresholds = 12/12 Blueprint §8; register = 8/8 | same | ✅ |
| §6 summary prose vs dataset | 6 responses (01–06), 2 no-response (07,08), employed 01/02/03/06, job-seeking 04/05, baseline 2/1/3/2, all evidence NONE_PROVIDED | same | ✅ |

No arithmetic, denominator, date, count or status-code error found.

---

## Defects and advisories (no MAJOR, no MINOR)

| ID | Severity | Locator | Defect | Minimum required repair |
|---|---|---|---|---|
| ADVISORY-1 | LOW | §6 demo table, rows SYN-0116-01/02/06, column 其他因素 = `NOT_RECORDED`; R06 dataset `other_factors_status = UNKNOWN` for all 8 rows | Token in the fixed demo table does not match the fixed dataset value on three rows. No numeric effect (NOT_RECORDED is defined「按 UNKNOWN 處理」, and §6 prose states「Q09在八筆皆未提供因素內容，統一按 UNKNOWN 解讀」), but strict row-fidelity to the dataset is broken. | Render those three cells as `UNKNOWN` (or re-issue dataset + all receipts on a version bump); fold into any future revision |
| ADVISORY-2 | LOW (observation) | §8 routing table, row SELF_REPORT_ONLY = 4筆 (01,02,03,06) | Dataset `evidence_class = SELF_REPORT_ONLY` appears on all six respondent rows; the table's count is scoped to 就業自陳 by its preamble, so internally coherent, but a reader could misread it as contradicting the dataset. | Optionally append「（就業自陳4筆；04、05為非就業自陳）」to the row |
| ADVISORY-3 | LOW | Header sentence「…此為內部索引，官方紙本 checkbox 印刷序號 UNKNOWN_NOT_ASSERTED，不得寫成印刷序號」 | Last clause still lacks an explicit subject/object (R05 F11 residual). Operatively unambiguous because §8 names the exact retire trigger. | Rewrite as「索引127為內部位置，不得寫成或宣稱為官方紙本印刷序號（該序號 UNKNOWN_NOT_ASSERTED）」 |

None of these blocks acceptance on semantic grounds.

---

## SAMPLE / REAL determination

**SAMPLE_SYNTHETIC_ONLY throughout; real performance = UNKNOWN / HOLD.** No association decision, consent, contact attempt, delivery proof, employment outcome, third-party document, verifier result, signature, approval or score is asserted as real. All approver/reviewer/owner fields blank + HOLD; all four employment self-reports capped at SELF_REPORT_ONLY / NONE_PROVIDED; VERIFIED/REQUEST_EVIDENCE/REJECTED = 0; the document forbids causality, improvement and 2–4分 claims and forbids publishing real figures before denominator review.

## Title-blind and cross-document results (summary)

Title-blind: identifiable as an employment follow-up survey + logging worksheet; all five negative neighbors excluded (above). Cross-document: 0115 and 0117 correctly fenced (no shared denominators/numerals, fact_id separation, misuse = retire trigger), 0100/0101 excluded; internal index 127 (I19-L1) asserted as internal only, printed checkbox serial UNKNOWN_NOT_ASSERTED — never asserted as a serial anywhere in the candidate.

## Visual scope limitation

I did not inspect the DOCX, the Word-native PDF, or any page raster and claim no layout knowledge; the render receipt reports `visual_review: PENDING` and 12 pages (page 8 landscape), and the QA receipt reports fonts ≥10.5/9.5 pt and 3 sections — these are attestations only, checked here solely for internal consistency (table count/shapes, 8 synthetic rows, 6/2/0/0 counts all agree with the extracted content). The coordinator's Word-native page review remains the sole source for layout conclusions.

## Uncertainties

1. All SHA-256 values (DOCX, extraction, dataset, packet, PDF excerpts) were verified for length and cross-document consistency, never recomputed → byte-level verification UNKNOWN.
2. Extraction completeness/order vs the actual DOCX: tables corroborated (14/14 shapes match in order); the 92-paragraph count is unverified.
3. Layout, page breaks, fonts, clipping, section orientation — UNKNOWN (coordinator's scope).
4. 157 Blueprint file row 127, crosswalk CSV row, full genre manual and mission doc remain attested-only; the official p.7/p.8 wording is now directly verified from attached text (Ob2 resolved for the official scoring text).
5. Whether ADVISORY-1 stems from Writer rendering or dataset handling cannot be determined without the DOCX.
6. The R05 review was used only as a defect checklist; every prior finding was re-tested independently against the R06 content above.

**Final rationale:** Every R05 major and minor defect is verifiably repaired in the R06 extraction, all mappings, denominators, formulas, status codes, joins, register items and SAMPLE/REAL fences recompute and reconcile exactly against the fixed dataset, and the document remains a title-blind-appropriate employment follow-up tool that claims no score and holds all real performance at UNKNOWN — leaving only a zero-impact token-fidelity nit and two phrasing advisories, with layout outside this semantic scope — **PASS**, bound to DOCX SHA-256 `eb4c1efef5bb4f7888e29f4c202c3c2d44997cfd0f31131253294bc564679af2`.
<<<END MATERIAL>>>

# MATERIAL: R07 technical QA receipt SHA256=242fd2ed9d08db8d57ccad89540dec9c6d3b904c2f963124e2b0b599413db1e5

<<<BEGIN MATERIAL>>>
{
  "doc_id": "0116",
  "requirement_id": "I19-E03",
  "revision": "R07",
  "docx_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0116_I19-E03_SOURCE_PREP_R01_20261024\\candidate\\0116__學員訓後就業狀況追蹤調查表_R07.docx",
  "docx_sha256": "82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c",
  "docx_bytes": 59080,
  "source_markdown_sha256": "c85e5b13ad82f8aea8b7387292f73f264e99a89c0748ba94d45822c16f3d9f42",
  "dataset_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0116_I19-E03_SOURCE_PREP_R01_20261024\\source\\SYNTHETIC_DATASET_0116_R06.csv",
  "dataset_sha256": "76c80580eb677278dc94f88608f3c8d36a5a37b61a25ac0bd791379373706adf",
  "source_packet_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0116_I19-E03_SOURCE_PREP_R01_20261024\\source\\SOURCE_PACKET_0116_I19-E03_R01.md",
  "source_packet_sha256": "3430b1a95755ad773e12380cf1c0b599dbf4b057d1a0f34f47b7dee51fa08c9d",
  "extraction_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0116_I19-E03_SOURCE_PREP_R01_20261024\\worker_0116_R01\\candidate_text_extraction_R07.txt",
  "extraction_sha256": "cdad739b42e07e752910756fb9fdaa66681fbdbc4b95eceda778620c86199e98",
  "paragraph_count": 92,
  "table_count": 14,
  "table_shapes": [
    {
      "rows": 12,
      "cols": 3
    },
    {
      "rows": 9,
      "cols": 3
    },
    {
      "rows": 10,
      "cols": 2
    },
    {
      "rows": 8,
      "cols": 2
    },
    {
      "rows": 13,
      "cols": 3
    },
    {
      "rows": 12,
      "cols": 3
    },
    {
      "rows": 5,
      "cols": 4
    },
    {
      "rows": 6,
      "cols": 4
    },
    {
      "rows": 5,
      "cols": 4
    },
    {
      "rows": 9,
      "cols": 8
    },
    {
      "rows": 10,
      "cols": 2
    },
    {
      "rows": 10,
      "cols": 3
    },
    {
      "rows": 6,
      "cols": 3
    },
    {
      "rows": 9,
      "cols": 4
    }
  ],
  "min_body_font_pt": 10.5,
  "min_table_font_pt": 9.5,
  "sections": [
    {
      "width_cm": 21.0,
      "height_cm": 29.7,
      "orientation": "PORTRAIT"
    },
    {
      "width_cm": 29.7,
      "height_cm": 21.0,
      "orientation": "LANDSCAPE"
    },
    {
      "width_cm": 21.0,
      "height_cm": 29.7,
      "orientation": "PORTRAIT"
    }
  ],
  "synthetic_rows": 8,
  "response_counts": {
    "RESPONDED": 6,
    "NO_RESPONSE": 2,
    "DECLINED": 0,
    "WITHDRAWN": 0
  },
  "self_report_employed_count": 4,
  "third_party_evidence_input_count": 0,
  "baseline_distribution": {
    "EMPLOYED": 2,
    "JOB_SEEKING": 3,
    "SELF_EMPLOYED": 1,
    "STUDYING": 2
  },
  "checks": {
    "zip_integrity": true,
    "correct_doc_and_requirement": true,
    "all_twelve_questions": true,
    "synthetic_and_real_boundary": true,
    "response_rate_math": true,
    "employment_ratio_math": true,
    "sample_evidence_ratio_math": true,
    "source_hash_is_local_sha256": true,
    "no_undefined_dataset_blanks": true,
    "response_status_reconciles": true,
    "sample_self_report_count": true,
    "third_party_input_count_zero": true,
    "baseline_distribution": true,
    "case_ids_present": true,
    "false_unchanged_rows_removed": true,
    "decline_withdraw_denominator_rule": true,
    "form_b_join_and_question_table": true,
    "form_c_fillable_safe_sample": true,
    "form_d_dispositions_and_decisions": true,
    "body_font_min_10_5": true,
    "table_font_min_9_5": true,
    "landscape_dataset_section": true,
    "no_formal_acceptance_claim": true
  },
  "technical_status": "PASS_PENDING_WORD_EXPORT_VISUAL_AND_SEMANTIC"
}
<<<END MATERIAL>>>
