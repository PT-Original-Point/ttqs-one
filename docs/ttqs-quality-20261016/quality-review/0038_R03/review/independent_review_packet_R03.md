# Consolidated independent review packet

Open the exact DOCX/PDF/PNG files at the absolute paths supplied in the request. The material below contains text/context; it is not a replacement for verifying the actual binary SHA.


---

## ATTACHED SOURCE: review/review_request_R03.md

# Independent semantic review request — TTQS ONE 0038 R03

Review this candidate independently from its builder. Do not trust prior PASS statements. Read the exact candidate DOCX, the full ordered text extraction, current Unique Blueprint row, official source page images, current spec/source map, neighbor rows, synthetic replacement register, R02 historical review, and all R03 render pages if your tools permit.

## Exact identity
- DOCX: `3a887bd3835b3a30b9fdb489257c8a09f79d3c2ce25c10565fae2b4e173f7efa` (verify SHA-256 yourself before analysis)
- PDF render: `85974e68937426d2a7b80844527098a0370cbe39200f3563ee773fdf15543f2a`
- Project/doc/requirement/official sequence: TTQS_ONE / 0038 / I08-E02 / 039
- Current controlling spec commit: `639b9eacce93f84f49ee20714f1bad337c6a961e`
- Correct neighbors: 0037=I08-E01 and DOCX 0039=I08-E03. Do not confuse DOCX ID and checkbox sequence.

## Files
- Candidate: `candidate/0038_R03.docx`
- Ordered text: `review/0038_R03_full_text_exact_sha.md`
- Blueprint: `inputs/BLUEPRINT_CURRENT_0038.jsonl`
- Neighbors: `inputs/BLUEPRINT_NEIGHBORS_0037_0039.jsonl`
- Official source screenshots: `inputs/official-2.png`, `inputs/official-3.png`
- Replacement register: `evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`
- Rendered PDF and all 14 page images: `evidence/render_final/`
- Source map: `inputs/SOURCE_MAP.md`
- R02 previous semantic report: `../0038_R02/evidence/qa/independent_semantic_review_R02.md` (context only; exact SHA is R02, not this candidate)

## Required independent checks
1. Exact official wording and Unique Blueprint mapping; distinguish doc_id 0038 from official checkbox sequence 039 and from DOCX 0039/I08-E03.
2. Correct genre and title-blind specificity; distinguish I08-E01 multi-period review and I08-E03 planning meeting.
3. Mature operational usefulness to a small volunteer training association. Check that the document actually records design deficiency, alternative comparison, specific revision, implementation sample, result analysis, limitations, follow-up, and return conditions.
4. Review the 24-row A/B worked example, denominators, threshold, rates, mean gains, weighted option scores, B08 exception, and no causal overclaim.
5. Verify SAMPLE/SYNTHETIC versus REAL, association approval/execution, third-party and authority boundaries; no fabricated original evidence.
6. Exact link between each synthetic case row and the replacement register, the source/decision/review crosswalk, and candidate citations.
7. Review the text and pages with the title hidden. Do not treat a builder's technical QA as semantic acceptance.
8. Provide PASS / PARTIAL / FAIL. Every finding must cite section/page or exact wording. Explicitly distinguish semantic review from pixel inspection; if you cannot inspect pixels, say so. State blockers and any content defect requiring correction.

Return a concise but substantive report with candidate SHA, PDF SHA if verified, criterion-by-criterion verdict, findings with locations, and final verdict. Do not change any file. A PASS means the R03 content is semantically acceptable as a SAMPLE/CANDIDATE only; it does not grant association acceptance or formal promotion.


---

## ATTACHED SOURCE: review/0038_R03_full_text_exact_sha.md

# DOCX text extraction for independent review

- Candidate SHA-256: `3a887bd3835b3a30b9fdb489257c8a09f79d3c2ce25c10565fae2b4e173f7efa`
- Extraction: python-docx in OOXML body order; paragraphs and table rows preserved.
- This text accompanies, and is bound to, the candidate DOCX; reviewer must independently hash/open DOCX.

---

訓練方案系統設計改善執行與成效示範紀錄

文件 0038　｜　I08-E02　｜　官方具名方框序號 039

SAMPLE / SYNTHETIC COMPLETE EXAMPLE｜非原始點協會實際辦訓、核准、簽署或成效紀錄

這份紀錄供誰使用

供小型訓練機構承辦人檢討一項課程設計、記錄實際修改，並用同一量尺核對執行結果。行政人員可按本件順序完成找出缺口、比較方案、修訂課程、記錄樣本、重算結果及決定下一步；評核委員可查看官方需求、逐筆資料和判讀限制。

本例的示範結論

完全虛構的兩組各12人資料中，講授為主組後測達標3/12（25.0%）；加入情境演練與回饋組達標11/12（91.7%）。修訂組平均分增加2.92/8分，對照組增加1.08/8分，兩組增益差1.83分。這些數字只示範記錄與計算，既非協會實績，也不能證明因果效果。

唯一命題：訓練設計改善是否有事前假設、可比較選項、具體改動、可重算執行結果及有限度的後續決定。

案例：SYN-I08E02-2026-01；假設課程「社區關懷志工服務溝通與轉介界線」。

資料狀態：全篇日期、角色、課程、樣本、量尺、分數、決定均為合成示範；沒有任何真人或協會原始紀錄。

來源定位：官方訓練機構版佐證表 I08 p.2；p.3為相鄰項續頁。本件對應 I08-E02。

使用方式

實際使用時，將 SAMPLE 欄位換成經授權可查的課程版本、執行與評量資料，再保存附件位置、去識別方式及覆核軌跡。沒有真實資料時，保留本件為示範稿，不得勾選成協會已執行或正式通過。

1　官方要求與本件工作邊界

官方文字：「針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。」本件以一項課程設計的缺口、替代方案、設計變更、執行記錄和結果判讀回應此命題；不以會議形式取代實際改善證據。

對照項 | 本件如何處理 | 查核位置
官方定位 | I08-E02；官方方框序號039；資料表p.2，續頁p.3。 | 本頁及來源索引
0038文類 | 執行與樣本紀錄；呈現操作流向、逐筆示範、計算和後續處置。 | §2、§5–§9
0037負向鄰項 | I08-E01重點是跨期設計變化；本件記錄一項改善的執行與效果，不代替跨期檢討。 | 差異說明
0039負向鄰項 | I08-E03重點是規劃會議議程、意見、決議及追蹤；本件沒有假造會議或核准。 | 差異說明
真實界線 | 協會原始執行未驗證；案例獨立，不宣稱與0037或0039共用事實。 | 替換清冊與來源圖

合成案例的前提

本例假設承辦人發現講授與知識測驗不足以觀察志工的溝通、隱私及轉介界線，因此提出加入短情境演練的假設。這不是對原始點協會現行課程、服務對象、工作角色或既往成效的陳述。

2　設計缺口、觀察與方案比較

示範問題與可檢驗假設

合成基準設計假設為120分鐘講授為主，評量集中於知識題。它能檢查記憶，卻未直接觀察學習者是否說明服務目的、取得同意、保護資訊、守住非醫療界線並作適當轉介。此處只是示範設計假設，不是查得的協會課程缺陷。

假設：總時數、課程目標、量尺和評量時點相同時，以35分鐘情境演練與回饋取代部分講授，會提高學習者在等難度情境中展現目標行為的比例。

比較方案與示範評分

各項1–5分，5分代表較符合；加權分＝Σ（分數×權重），總分上限5.00。權重先於評分設定，合計100%。

準則／權重 | A 增加講義 | B 情境演練＋回饋 | C 外聘全日實作
可觀察行為證據 40% | 2×.40=.80 | 5×.40=2.00 | 5×.40=2.00
小型課程可執行 25% | 5×.25=1.25 | 4×.25=1.00 | 2×.25=.50
隱私／非醫療界線 20% | 3×.20=.60 | 5×.20=1.00 | 5×.20=1.00
結果可追溯 15% | 2×.15=.30 | 5×.15=.75 | 4×.15=.60
加權總分 | 2.95/5.00 | 4.75/5.00 | 4.10/5.00

示範取捨：B得分最高且不增加總時數，以可觀察行為與回饋替代部分講授。A成本較低，但仍不能直接檢查行為；C觀察力較高，卻需更多經費及外部師資。上述分數與選擇是假設值，沒有協會正式決議。

從缺口到可驗證結果

設計缺口 | 具體修改 | 可查結果 | 事前判定規則
只用知識題 | 加入情境演練，評D1、D2。 | 前後測向量及評分表。 | 總分≥6/8。
服務界線混淆 | 加入界線示範、兩情境練習和回饋。 | D3、D4分數及異常覆核。 | D3、D4均>0。
改善無固定口徑 | 兩組同時數、同量尺、配對前後測。 | 逐筆資料、有效數和增益。 | B達標率≥80%，關鍵失誤=0才建議續試。

本例沒有真實需求調查、職能盤點或先前實績支持此假設。真實執行時，須先附需求來源及版本差異再確認是否試作。

3　修訂後課程設計與執行安排

示範課程：「社區關懷志工服務溝通與轉介界線」。對象是假設的社區關懷志工學習者；不得推定協會已開辦。兩組總時數同為120分鐘。

120分鐘教學安排

時間 | 活動與方法 | 引導者操作 | 學習者產出／檢核
00–10 | 情境前測 | 說明匿名代碼及評分；發等難度情境卡。 | 完成四項行為前測。
10–20 | 目的、同意與拒絕權 | 示範先說明目的並詢問是否願意繼續。 | 重述可停止及改約界線。
20–40 | 開放提問與中性摘要 | 示範開放問句，區分聆聽、推測和承諾。 | 完成摘要並確認理解。
40–55 | 隱私及非醫療界線 | 比較必要資訊與多餘細節；示範停止並轉介。 | 指出何時不記、不建議、不代替專業判斷。
55–80 | 兩人一組演練 | 輪替服務者與觀察者，每人至少完整演練一次。 | 依D1–D4記錄可見行為。
80–105 | 個別後測情境 | 用另一等難度情境評分，不提示答案。 | 四項分數及簡短觀察事實。
105–115 | 回饋與重試 | 說明具體行為後給一次練習；正式分數不覆寫。 | 完成回饋練習，保留首測值。
115–120 | 轉用計畫 | 提示選一項下次可採行的服務行為。 | 記錄一項可觀察行動。

目標與證據對應

可觀察目標 | 教學活動 | 評量證據
說明目的並取得同意 | 目的／拒絕權示範和演練 | D1：先說明並取得同意
以開放問題理解需求 | 問句、摘要及理解確認 | D2：開放提問與中性摘要
保護隱私並守住界線 | 必要資訊及非醫療界線情境 | D3：隱私與角色界線
辨識超出角色問題並轉介 | 轉介流程示範及後測 | D4：合宜路徑且不作保證

4　評量工具、量尺與資料控制

前後測用難度相當但不同的情境，避免直接重複答案；兩組使用同一量尺。每項0–2分，總分0–8；正式判定同時符合總分和關鍵項條件。

項目 | 0分 | 1分 | 2分 | 關鍵
D1 目的與同意 | 直接追問或假定同意。 | 說明目的或詢問意願，未同時做到。 | 先說明目的，再詢問是否願意並接受拒絕。 | 否
D2 開放提問與摘要 | 誘導或封閉主導，未確認理解。 | 做到開放提問或摘要其中一項。 | 開放提問、中性摘要並確認理解。 | 否
D3 隱私與服務界線 | 不必要蒐集／揭露，或提供超出角色判斷。 | 保護部分資訊，但界線不完整。 | 只記必要資訊，明確不診斷、不承諾醫療效果。 | 是
D4 適當轉介與後續 | 未轉介，或作未確認保證。 | 指出資源但未說明下一步。 | 說明適當聯繫及可確認後續，不保證結果。 | 是

達標規則：總分至少6/8，且D3>0、D4>0。未達標保留原始分數，另記補強與重測；不得刪列或改寫為通過。

等難度情境與執行資料

情境 | 前測示例 | 後測示例 | 同等要求
目的與隱私 | 活動後談到家庭近況；志工不確定能否記錄及轉述。 | 電話關懷中對方談及不願公開的生活資訊並詢問保密。 | 說明目的、詢問同意、只記必要資訊、說清保密界線。
角色與轉介 | 對方問志工能否判斷身體不適原因。 | 對方請志工保證某項服務一定有效。 | 不診斷、不保證；說明適當專業聯繫路徑。

缺漏、重複與資料保存

檢查點 | 本示範記錄 | 真實執行控制
同意與代碼 | 24列假設代碼；無姓名或聯絡方式。 | 未同意者不納入評量，只列合計與排除原因。
配對與重複 | 前後測配對24；重複代碼0。 | 以原件和日期核對；更正留軌跡，無法判定者列理由。
缺測與評分 | 缺測0；不以未達標作排除理由。 | 漏評不得補分；依事前規則列缺漏並報有效分母。
權限與保存 | 實際位置及存取權限UNKNOWN。 | 依核實保存期、權限、刪除和備份規則辦理。

5　樣本批次、納入規則與資料流向

本批次所有資料都是SAMPLE/SYNTHETIC。假設樣本框為24名符合條件的學習者，A、B兩組各12名；以下日期、渠道、同意狀態及排除數均非實際協會紀錄。

欄位 | 全批次示範值 | 真實替換與核對來源
母體與樣本框 | 假設24名參加者；A與B各12名。 | 正式招生範圍、課程對象及去識別樣本框。
納入與排除規則 | 預先假設：同意參與、完成前後兩次評量、D1–D4均可評才納入有效配對。未同意、缺任一測或缺評項須記理由。 | 納入規則版本、同意紀錄、逐筆缺漏及排除清單。
日期與執行渠道 | A組2026-09-08；B組2026-09-15。模擬紙本情境卡及匿名評分表。 | 實際日期、課程簽到、使用工具及原始評量表。
代碼與同意 | A01–A12、B01–B12為合成代碼；假設同意24/24；不含姓名、電話或簽名。 | 合法同意及代碼對照保管方式；公開版只留去識別資料。
缺漏、重複與更正 | 有效24；缺漏0；重複0；排除0。B08加總覆核見§7；沒有其他更正。 | 原始列、重複檢查、差異版次、更正人及日期。
保存與存取 | 本候選無個資；協會實際保存位置、權限和期限均UNKNOWN。 | 協會核實的權限表、保存年限、刪除和備份紀錄。

樣本流向與分母

階段 | 筆數 | 計算／判定 | 說明
接觸合格樣本框 | 24 | — | 假設樣本框，不是協會名冊。
發出邀請 | 24 | 24/24 | 全數受邀，尚非回收數。
收到成對前後測 | 24 | 24/24 | A組12、B組12；以代碼配對。
有效成對資料 | 24 | 有效率=24/24=100% | 有效率=有效數÷回收成對數；分母是回收數。
排除／缺漏 | 0 | 0筆 | 沒有因未達標而排除的列。

若成對回收數為0，有效率應寫N/A並註明無回收分母，不可填0%。24/24有效率只表示資料可計算，不等於達標率或學習效果。

共同欄位定義：每列保留case_id、合成日期、組別、渠道、同意／納入判定、D1–D4前後向量、缺漏／重複狀態及更正理由。真實執行時，原始附件路徑及覆核角色須可追查。

6　完整示範批次：比較組 A

A組示範日期為2026-09-08，渠道為模擬紙本情境評量；各列同意／納入與缺漏、重複、更正狀態見附表A。講授為主設計並非協會既有課程。向量順序D1/D2/D3/D4，合計與差值可直接重算。

A組逐筆結果｜講授為主

代碼 | 前測 D1/D2/D3/D4 | 前測 | 後測 D1/D2/D3/D4 | 後測 | 差值 | 判定
A01 | 1/1/1/0 | 3 | 1/1/1/1 | 4 | +1 | 未達
A02 | 1/1/1/1 | 4 | 1/1/1/2 | 5 | +1 | 未達
A03 | 0/1/1/0 | 2 | 1/1/1/0 | 3 | +1 | 未達
A04 | 1/1/1/2 | 5 | 2/1/1/2 | 6 | +1 | 達標
A05 | 1/1/1/0 | 3 | 1/1/1/1 | 4 | +1 | 未達
A06 | 1/1/1/1 | 4 | 1/1/1/2 | 5 | +1 | 未達
A07 | 1/1/1/2 | 5 | 2/1/1/2 | 6 | +1 | 達標
A08 | 0/1/1/0 | 2 | 1/1/1/0 | 3 | +1 | 未達
A09 | 1/1/1/1 | 4 | 1/1/1/2 | 5 | +1 | 未達
A10 | 1/1/1/0 | 3 | 1/1/1/1 | 4 | +1 | 未達
A11 | 1/1/1/2 | 5 | 2/1/2/2 | 7 | +2 | 達標
A12 | 1/1/1/1 | 4 | 1/1/1/2 | 5 | +1 | 未達

A組小計：前測總分44、後測總分57；平均由44/12=3.67升至57/12=4.75，平均增益13/12=1.08分；後測3/12達標，D3或D4為0者2/12。

7　完整示範批次：修訂組 B

B組是假設的同為120分鐘、加入情境演練、行為量尺與回饋的修訂設計。總時數、前後測計分及達標門檻與A組一致；兩組並非隨機分派。各列渠道、同意／納入與資料狀態見附表A。

B組逐筆結果｜情境練習與回饋

代碼 | 前測 D1/D2/D3/D4 | 前測 | 後測 D1/D2/D3/D4 | 後測 | 差值 | 判定
B01 | 1/0/1/1 | 3 | 2/2/2/1 | 7 | +4 | 達標
B02 | 1/2/0/1 | 4 | 2/2/1/2 | 7 | +3 | 達標
B03 | 0/1/1/0 | 2 | 1/2/1/2 | 6 | +4 | 達標
B04 | 1/1/1/2 | 5 | 2/2/2/2 | 8 | +3 | 達標
B05 | 0/1/1/1 | 3 | 1/2/1/2 | 6 | +3 | 達標
B06 | 2/1/0/1 | 4 | 2/1/1/2 | 6 | +2 | 達標
B07 | 2/1/1/1 | 5 | 2/1/2/2 | 7 | +2 | 達標
B08 | 0/1/0/1 | 2 | 1/1/1/2 | 5 | +3 | 未達
B09 | 1/1/1/1 | 4 | 2/2/2/2 | 8 | +4 | 達標
B10 | 1/1/0/1 | 3 | 1/2/1/2 | 6 | +3 | 達標
B11 | 1/2/1/1 | 5 | 2/2/1/2 | 7 | +2 | 達標
B12 | 1/0/2/1 | 4 | 1/1/2/2 | 6 | +2 | 達標

B組小計：前測總分44、後測總分79；平均由44/12=3.67升至79/12=6.58，平均增益35/12=2.92分；後測11/12達標，D3或D4為0者0/12。

異常覆核 SYN-ANOMALY-001

B08後測向量1/1/1/2，加總為1+1+1+2=5分，低於6分門檻。覆核後與表列總分一致；D3=1、D4=2，關鍵界線通過。保留「未達標」，不刪除此筆、不補分，也不以回饋後重試分數覆寫正式後測。

異常 | 核對 | 處置 | 資料影響
B08總分不足 | 原始向量重算5，與列值一致。 | 保留有效列並標未達；補練後須另建重測紀錄。 | 分母仍24；B組達標分子仍11。

8　計算、結果與可歸因界線

指標 | 講授為主 A | 修訂設計 B | 重算方式
有效成對樣本 | 12/12 | 12/12 | 各組有效列數。
平均前測（0–8） | 44/12=3.67 | 44/12=3.67 | 前測各列向量加總÷12。
平均後測（0–8） | 57/12=4.75 | 79/12=6.58 | 後測各列向量加總÷12。
平均增益 | (57−44)/12=1.08 | (79−44)/12=2.92 | 平均後測−平均前測，單位分。
後測達標率 | 3/12=25.0% | 11/12=91.7% | 總分≥6且D3、D4均>0。
關鍵項為0 | 2/12=16.7% | 0/12=0% | D3或D4任一為0；分母各組12。

兩組差異怎麼讀

平均增益差=(79−44)/12−(57−44)/12=22/12=1.83分（0–8量尺）。後測達標率差=11/12−3/12=8/12=66.7個百分點。有效率24/24=100%是資料可用比例，不是學習成效；達標率按各組有效樣本計算。

示範判讀：B組達標率高於事前設定的80%，且關鍵項為0者為0；本案例內可記為「建議下一輪小規模續試，並對B08補強」。這不是協會已核准或已採行。

限制與退件條件

兩組都是合成小樣本，未隨機分派，也沒有真實出席、需求、評分者一致性或外部來源。基線平均相同只是示範資料設計，不能推論改善造成差異、母群效果或協會實際成效。

分母不明、量尺不一致、逐筆加總錯誤、以不及格為由刪列、關鍵項為0仍算通過、重複或缺漏未揭露、合成事實未登錄、虛構核准，任一出現即退回受影響內容。

9　後續處理、真實替換與查核索引

本例示範的後續工作

時點 | 工作 | 責任角色（示範） | 完成判定
執行前 | 取得正式課程版次，確認對象、評量用途及量尺版本。 | 課程承辦角色 | 有版本、來源和授權依據。
每次執行 | 記錄邀請、同意、配對、缺漏、排除及異常。 | 執行／資料角色 | 分母可重算，逐筆值可追源。
課後覆核 | 非原評分者抽核原始表與加總；更正留初值及理由。 | 覆核角色 | 範圍、差異、處置留痕。
下一輪前 | 比較真實基線與修訂結果；說明組成和評分差異。 | 承辦角色 | 限制、失敗個案及再測時點明確。

改成真實紀錄前的替換清單

核對正式機構名稱、課程代碼、計畫版次及具權限的承辦角色。

取得原版與修訂版課程計畫、需求／職能來源及變更記錄。

以真實日期、納入規則、邀請／同意、前後測原表、出席及排除紀錄替換樣本。

核驗評分者權限、量尺版次、校準、原始值、更正軌跡和資料保管權限。

重算有效率、平均分、增益、達標率、關鍵項與限制；缺正式核准或簽章時保留UNKNOWN。

逐筆更新 replacement register，記錄原件位置、去識別方式和覆核人。

官方與專案來源索引

來源 | 定位與用途
官方評核依據 | 訓練機構版佐證表 I08 p.2、續頁 p.3；PDF SHA記於SOURCE_MAP.md。
正式項次與藍圖 | 0038→I08-E02→官方序號039；對照目前Blueprint row、142序列及01/02/03規格。
相鄰要求 | 0037/I08-E01為多期設計檢討；0039/I08-E03為規劃會議。本案例不宣稱同案。
合成事實清冊 | SYNTHETIC_REPLACEMENT_REGISTER.csv含case_id、doc_id、定位、REAL原件及核實角色。
官方要求逐項對照 | 附表B連結官方命題、紀錄欄位、來源、判定及覆核位置。
版本收據 | SOURCE_MAP.md、BLUEPRINT_CURRENT_0038.jsonl、PROGRESS.json及manifest.json。

目前狀態

本件為CANDIDATE示範文件；逐項驗收狀態以隨附收據為準，協會正式接受未授與。此件只回應0038/I08-E02，不取代真實課程原件、0037跨期檢討或0039會議紀錄。

一次執行的控制順序（角色均為合成示範）

階段 | 負責角色（均為示範） | 操作與控制點 | 輸出
定位 | 承辦角色 | 記錄官方要求、課程版次與缺口；推測不可寫成事實。 | 問題與來源
比較 | 設計覆核角色 | 用事前權重評分三方案並保留取捨。 | 方案比較表
修訂 | 課程引導角色 | 將可觀察目標對到活動、評分行為和通過規則。 | 變更表
執行 | 引導者／觀察者 | 同時數、同量尺完成兩組示範；記錄樣本流向。 | 逐筆樣本
覆核 | 資料覆核角色 | 核對加總、配對、缺漏、排除及關鍵界線。 | 覆核軌跡
判讀 | 承辦角色 | 計算比例與增益，列限制及下一步。 | 成效判讀

正式使用時須依協會實際章程、分工及資料權限確認角色；本表不構成現職指派或授權證據。

附表A　24筆合成樣本逐列追溯

本表逐列連結§6、§7的A01–A12、B01–B12分數紀錄。渠道、同意及納入均為合成假設，並非真人同意或協會實際執行證明；各列均符合本例預設完整配對條件。

case_id | 渠道（SYNTHETIC） | 同意／納入判定（SYNTHETIC） | 缺漏／重複／更正（SYNTHETIC）
A01 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A02 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A03 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A04 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A05 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A06 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A07 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A08 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A09 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A10 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A11 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
A12 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B01 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B02 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B03 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B04 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B05 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B06 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B07 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B08 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B09 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B10 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B11 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）
B12 | 模擬紙本情境卡／匿名評分表 | 同意=是（合成假設）；納入=是，原因：完成前後測且D1–D4均有評分 | 缺漏=0；重複=0；更正=0（未更動原值）

狀態定義：缺漏=未完成前後測或量尺項；重複=重複代碼列；更正=對原始值有更動。真實執行不得把未知狀態填0，須保留原值、原因、核對人及日期。每列REAL替換所需原件為合法同意／納入依據、課程簽到、匿名化前後測原表及更正／覆核軌跡；缺一項即維持UNKNOWN。

附表B　官方要求、紀錄欄位與覆核位置對照

本表把官方命題拆成可查的紀錄鏈。SAMPLE資料只示範欄位與計算；REAL欄列出升格前必須取得的原件，不代表原始點協會已持有或核准。

官方命題／查核問題 | 本件紀錄欄位與位置 | SAMPLE來源／REAL替換原件 | 判定與限制 | 覆核位置
訓練方案系統設計是否適時檢討並改善？ | 設計缺口、可檢驗假設、加權方案、修訂活動、目標與評量對應。 | SAMPLE：§2–§4；REAL：原版／修訂課程計畫、需求或職能來源、版本差異及授權依據。 | 示範方案B加權4.75/5.00；此為假設選擇，非協會決議。 | §2方案比較表；§3時程與目標表；§9替換清單。
執行後是否有良好效果？ | 樣本框、前後測量尺、24筆逐列結果、有效分母、達標與增益。 | SAMPLE：§5–§8及附表A；REAL：出席、合法同意、匿名前後測原表、評分者權限與覆核紀錄。 | A 3/12、B 11/12達標；合成小樣本、非隨機，不能推論因果或協會成效。 | §5納入／樣本流向；§6–§7逐筆表；§8計算與限制。
每列資料能否追到執行狀態？ | 渠道、同意、納入理由、缺漏、重複及更正狀態。 | SAMPLE：附表A逐列欄位與替換清冊；REAL：課程簽到、同意依據、逐筆原表、差異更正軌跡。 | 本例24列皆假設同意、納入，缺漏／重複／更正皆0；實際未知不得填0。 | 附表A；replacement register各SYN-A/B-ROW列；§5處理規則。
判定是否有來源且可覆核？ | 來源、公式、判定門檻、異常及限制。 | SAMPLE：逐筆表、量尺、替換清冊；REAL：正式計畫、原始評量、核准量尺及資料權限記錄。 | 公式可重算；正式來源、核准與協會實績尚未驗證，維持SAMPLE。 | §4量尺；§8彙總；§9來源索引；附表B。


---

## ATTACHED SOURCE: inputs/SOURCE_MAP.md

# 0038 R03 source map and lineage

- Project/doc: TTQS_ONE / DOCX 0038.
- Formal requirement mapping: Unique Blueprint `deliverable_id=0038`, `requirement_id=I08-E02`; official checkbox sequence **039**. DOCX 0039 is a different deliverable (`I08-E03`) and is only a negative neighbor here.
- Official requirement: 針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。
- Official source: 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》，I08 p.2; p.3 is adjacent continuation context. Official PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`. Page images are `official-2.png` and `official-3.png`.
- Unique Blueprint current file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; exact 0038 raw row SHA-256: `2504485c1698a5c83ac2205938c05b532edc8d697f2441ad1d6a0c324897b73e`.
- Current spec branch/head used for R03: `work/ttqs-one-document-quality-contract-20261016` / `639b9eacce93f84f49ee20714f1bad337c6a961e`. Spec blob IDs:
  - `01` `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`
  - `02` `4ff863d9f534b6359fc1c7c1685bd8cce02da886`
  - `03` `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`
  - `04` `62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d`
  - `05` `60ae010c58140e1710ed24016085c6dfaf6ffaee`
  - `06` `70449889fd464106fe204496004bee13018d4a51`
- Current complete 0038 row: `BLUEPRINT_CURRENT_0038.jsonl`. Neighbor rows: `BLUEPRINT_NEIGHBORS_0037_0039.jsonl`.
- Negative neighbors: 0037/I08-E01 concerns cross-period review of system design changes; 0039/I08-E03 concerns a course-planning/design-review meeting. This sample is a separate case and does not claim to represent either neighbor.
- Candidate lineage: R03 was made from exact R02 SHA `bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4` by raising only 20 nonempty top-level body runs below the 10.5 pt Blueprint floor to 10.5 pt. All paragraph and table text remains identical; see `evidence/build/patch_receipt_R03.json`.
- R03 candidate DOCX SHA-256: `3a887bd3835b3a30b9fdb489257c8a09f79d3c2ce25c10565fae2b4e173f7efa`. Rendered PDF SHA-256: `85974e68937426d2a7b80844527098a0370cbe39200f3563ee773fdf15543f2a`.
- R02 semantic report is historical evidence for the R02 SHA only. It is not an R03 exact-SHA review. A new independent review of R03 is pending.
- No REAL association execution, approval, participant, measurement, or outcome has been authenticated. Dates, roles, course details, options, participant codes, scores, and decisions are SAMPLE/SYNTHETIC.


---

## ATTACHED SOURCE: inputs/BLUEPRINT_CURRENT_0038.jsonl

{"deliverable_id":"0038","requirement_id":"I08-E02","final_filename":"0038__針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿.docx","document_genre":"執行與樣本紀錄｜針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿","document_purpose":"本件專屬焦點：針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿；需直接回應的官方佐證要求為：針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。","primary_user_or_reader":"供承辦人逐次登錄執行、樣本流向、缺失與覆核，供主管追溯資料品質。","evidence_role":"證明蒐集或執行如何發生及資料如何納入；合成例必須明確標示。 本文件只擁有 I08-E02 的直接紀錄／分析口徑；不得吞併其他要求的事實。","source_of_truth":"官方查核佐證表精確原文『針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。』，表內頁次 2，讀取狀態 PDF_VISUAL_SPOTCHECKED；REQ_157_MAP 對應 I08-E02；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。","required_sections":"執行目的及本次紀錄範圍；計畫母體、抽樣框與納入規則；執行步驟、管道與時序；樣本／案件流水欄位定義；邀請、回收、有效及排除流向；缺失、重複與偏差處理；資料保管、權限與去識別；完整合成批次逐筆示例；覆核、修正及異常升級；與工具及後續分析的交接；真實紀錄替換與查核清單；證據位置與版本索引","required_tables_or_figures":"執行階段—責任角色—操作—控制點—輸出；邀請／接觸／回收／有效／排除流向明細；完整合成樣本逐筆紀錄及納入判定；官方要求—紀錄欄位—來源—覆核追溯表","required_fields_or_questions":"合成個案代碼；接觸或執行日期（合成）；來源管道與同意狀態；納入／排除判定及理由；缺失／重複／更正軌跡","required_calculations_or_analysis":"逐步呈現接觸數、回收數、有效數及排除數；有效率=有效數/回收數。分母為0時標示N/A及原因；樣本皆為合成記錄並逐項登錄替換簿。","required_cross_references":"同要求分件 無；相鄰要求 I08-E01, I08-E03；共用原始來源時只引用核實結果，不複製別份文件正文。","real_data_required":"升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。","third_party_evidence_required":"若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。","prohibited_fabrication":"不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。","title_blind_test":"遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿』並證明『針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。』；若可無修改移作其他要求即失敗。","negative_choice_neighbors":"0037《相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品》（I08-E01）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0039《課程規劃與設計審查會議紀錄》（I08-E03）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。","acceptance_tests":"移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿』，且能指出直接回應『針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。","document_role":"execution_record","official_requirement_text":"針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。","official_checkbox_text":"針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。","official_evidence_table_page":"2","official_source_readback_status":"PDF_VISUAL_SPOTCHECKED","official_visually_checked_pages":"2-3","requirement_deliverable_siblings":"0038","docx_body_template_policy":"FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.","synthetic_population_rule":"缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。","historical_blueprint_source":"04cacba7df28af6a006c5e60896e0112a53387b7ae4157d8c33ab0a658f91022","historical_body_use":"PROHIBITED","source_map_notes":"129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."}


---

## ATTACHED SOURCE: inputs/BLUEPRINT_NEIGHBORS_0037_0039.jsonl

{"deliverable_id":"0037","requirement_id":"I08-E01","final_filename":"0037__相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品.docx","document_genre":"專屬佐證紀錄｜相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品","document_purpose":"本件專屬焦點：相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品；需直接回應的官方佐證要求為：相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。","primary_user_or_reader":"供執行人員、主管與評核閱讀者追溯要求、事實、證據位置及覆核狀態。","evidence_role":"保存此項要求專屬的原始紀錄或證據索引；不代替第三方原件。 本文件只擁有 I08-E01 的直接紀錄／分析口徑；不得吞併其他要求的事實。","source_of_truth":"官方查核佐證表精確原文『相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。』，表內頁次 2，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I08-E01；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。","required_sections":"紀錄目的、責任及適用界線；官方要求拆解與證明路徑；來源、形成時點及納入規則；欄位定義及證據位置；完整合成紀錄示例；核對、計算與一致性判定；例外、缺證及更正軌跡；真實原件與合成示例的區別；覆核、保管及調閱規則；相關要求及文件交叉引用；真實資料替換清單；附件索引與版本","required_tables_or_figures":"欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表","required_fields_or_questions":"合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動","required_calculations_or_analysis":"若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。","required_cross_references":"同要求分件 無；相鄰要求 I07-E04, I08-E02；共用原始來源時只引用核實結果，不複製別份文件正文。","real_data_required":"升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。","third_party_evidence_required":"若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。","prohibited_fabrication":"不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。","title_blind_test":"遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品』並證明『相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。』；若可無修改移作其他要求即失敗。","negative_choice_neighbors":"0036《有課程設計進度表、課程規劃流程圖說明、訓練規_完整工作稿》（I07-E04）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0038《針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿》（I08-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。","acceptance_tests":"移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『相關文件紀錄能顯示近年來訓練目標、訓練方法、_可直接使用成品』，且能指出直接回應『相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。","document_role":"evidence_record","official_requirement_text":"相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。","official_checkbox_text":"相關文件紀錄能顯示近年來訓練目標、訓練方法、課程時程安排、師資遴選、學員遴選條件、 訓練教材、設施與環境、訓練評估方法等的檢討及改善過程。","official_evidence_table_page":"2","official_source_readback_status":"PDF_TEXT_EXACT_PAGE_MATCH","official_visually_checked_pages":"","requirement_deliverable_siblings":"0037","docx_body_template_policy":"FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.","synthetic_population_rule":"缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。","historical_blueprint_source":"f40d08fe195af13c3a1cbc396018bb0a9f67457b02d1b6c074fb8da731dd4435","historical_body_use":"PROHIBITED","source_map_notes":"129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."}
{"deliverable_id":"0039","requirement_id":"I08-E03","final_filename":"0039__課程規劃與設計審查會議紀錄.docx","document_genre":"會議運作與紀錄｜課程規劃與設計審查會議紀錄","document_purpose":"本件專屬焦點：課程規劃與設計審查會議紀錄；需直接回應的官方佐證要求為：課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。","primary_user_or_reader":"供主席、記錄人與參與者依議程討論、形成決議、指定責任與追蹤。","evidence_role":"連結議題、討論證據、決議、責任及期限；不得偽造真實出席、簽名或核定。 本文件只擁有 I08-E03 的直接紀錄／分析口徑；不得吞併其他要求的事實。","source_of_truth":"官方查核佐證表精確原文『課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。』，表內頁次 3，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I08-E03；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。","required_sections":"會議目的、範圍與議程；角色分工及決策規則；出席欄位及合成示例聲明；背景資料與逐項討論題；證據、不同意見與判斷理由；決議文字及適用範圍；責任人、期限、資源與驗收；未決事項與升級條件；完整示範紀錄及後續追蹤；紀錄校核與核定邊界；真實會議資料替換清單；附件及交叉引用索引","required_tables_or_figures":"議程—資料—引導問題—預期輸出；議題—證據—討論—決議逐列紀錄；決議—責任—期限—驗收證據—狀態追蹤；合成參與角色及非真實出席聲明","required_fields_or_questions":"合成會議代碼與示範日期；角色代碼而非真人姓名；議題／證據／不同意見；決議及授權邊界；責任角色／期限／驗收標準","required_calculations_or_analysis":"會議工具無組織實績計算；示範決議追蹤完成率=已驗收決議數/應追蹤決議數，逐步展示合成例；不得呈現偽造簽名、真實出席或正式核准。","required_cross_references":"同要求分件 0040；相鄰要求 I08-E02, I09-E01；共用原始來源時只引用核實結果，不複製別份文件正文。","real_data_required":"升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。","third_party_evidence_required":"若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。","prohibited_fabrication":"不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。","title_blind_test":"遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『課程規劃與設計審查會議紀錄』並證明『課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。』；若可無修改移作其他要求即失敗。","negative_choice_neighbors":"0038《針對訓練方案的系統設計能適時檢討及改善，執行_完整工作稿》（I08-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0041《課程規劃書（能顯示包含講師、行政、企業學員、_完整工作稿》（I09-E01）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0040《訓練評估方法與成效指標對照表》（I08-E03）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。","acceptance_tests":"移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『課程規劃與設計審查會議紀錄』，且能指出直接回應『課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。","document_role":"meeting_record","official_requirement_text":"課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。","official_checkbox_text":"課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。","official_evidence_table_page":"3","official_source_readback_status":"PDF_TEXT_EXACT_PAGE_MATCH","official_visually_checked_pages":"","requirement_deliverable_siblings":"0039 | 0040","docx_body_template_policy":"FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.","synthetic_population_rule":"缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。","historical_blueprint_source":"4b6ebe093bc083642ac9329855c0ced1c5dddccbe465936cc8e464dcbc7da947","historical_body_use":"PROHIBITED","source_map_notes":"129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."}


---

## ATTACHED SOURCE: evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv

fact_id,case_id,doc_id,document_locator,synthetic_value,assumption_reason,required_real_source_for_replacement,responsible_role_to_verify,status
SYN-CASE-001,SYN-I08E02-2026-01,0038,首頁案例識別,假設課程：社區關懷志工服務溝通與轉介界線,完整示範假設，非協會事實,正式課程代碼、計畫、適用對象,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-PERIOD-001,SYN-I08E02-2026-01,0038,§2 執行期間,比較組 2026-09-08；修訂組 2026-09-15,完整示範假設，非協會事實,真實課程日期、簽到及執行紀錄,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-POP-001,SYN-I08E02-2026-01,0038,§2 樣本框,假設24名符合條件者，A/B各12名,完整示範假設，非協會事實,真實招生名冊、納入規則及去識別抽樣紀錄,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-FLOW-001,SYN-I08E02-2026-01,0038,§5 樣本流向表,接觸24、邀請24、成對回收24、有效24、排除0,完整示範假設，非協會事實,邀請、同意、前後測原件及排除紀錄,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-ROLE-001,SYN-I08E02-2026-01,0038,§2 角色流程表,示範引導者、觀察評分者、資料保管者；非現役人員,完整示範假設，非協會事實,正式職務分工及授權資料,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-BASELINE-001,SYN-I08E02-2026-01,0038,§3 比較基準,120分鐘講授為主；非已查證的協會課程,完整示範假設，非協會事實,原版課程計畫、教材、評量及版本核准紀錄,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-CHANGE-001,SYN-I08E02-2026-01,0038,§3–§4 修訂設計,總時數同為120分鐘；以情境演練、量尺與回饋取代35分鐘部分講授,完整示範假設，非協會事實,修訂計畫、版次差異及執行證據,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-OPTIONS-001,SYN-I08E02-2026-01,0038,§3 方案評分表,權重40/25/20/15；加權總分2.95/4.75/4.10,完整示範假設，非協會事實,需求來源、評分者記錄及選案依據,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-RUBRIC-001,SYN-I08E02-2026-01,0038,§5 評量量尺,D1–D4各0–2；總分0–8；達標≥6且D3、D4>0,完整示範假設，非協會事實,量尺版次、評分工具與試評者校準,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-THRESHOLD-001,SYN-I08E02-2026-01,0038,§8 示範判讀規則,續行建議門檻：B組達標率≥80%且關鍵失誤=0,完整示範假設，非協會事實,事前核准的評估方案與負責人簽認,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-STORAGE-001,SYN-I08E02-2026-01,0038,§5/§9 資料處理,假設使用匿名代碼；實際保存位置與權限 UNKNOWN,完整示範假設，非協會事實,真實資料存取、保存、刪除和備份規則,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-DECISION-001,SYN-I08E02-2026-01,0038,§8 示範決定,建議下一輪小規模試行；非協會核定或採行,完整示範假設，非協會事實,真實審查、核定、課程版控及後續追蹤,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-ANOMALY-001,SYN-I08E02-2026-01,0038,§7 B08覆核,後測1/1/1/2加總5；保留未達標，不排除,完整示範假設，非協會事實,原始評量表及評分複核軌跡,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-01,SYN-I08E02-2026-01,0038,§6/§7及附表A A01逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/0合計3;後測=1/1/1/1合計4;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-02,SYN-I08E02-2026-01,0038,§6/§7及附表A A02逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/1合計4;後測=1/1/1/2合計5;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-03,SYN-I08E02-2026-01,0038,§6/§7及附表A A03逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=0/1/1/0合計2;後測=1/1/1/0合計3;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-04,SYN-I08E02-2026-01,0038,§6/§7及附表A A04逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/2合計5;後測=2/1/1/2合計6;差=1;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-05,SYN-I08E02-2026-01,0038,§6/§7及附表A A05逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/0合計3;後測=1/1/1/1合計4;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-06,SYN-I08E02-2026-01,0038,§6/§7及附表A A06逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/1合計4;後測=1/1/1/2合計5;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-07,SYN-I08E02-2026-01,0038,§6/§7及附表A A07逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/2合計5;後測=2/1/1/2合計6;差=1;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-08,SYN-I08E02-2026-01,0038,§6/§7及附表A A08逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=0/1/1/0合計2;後測=1/1/1/0合計3;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-09,SYN-I08E02-2026-01,0038,§6/§7及附表A A09逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/1合計4;後測=1/1/1/2合計5;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-10,SYN-I08E02-2026-01,0038,§6/§7及附表A A10逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/0合計3;後測=1/1/1/1合計4;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-11,SYN-I08E02-2026-01,0038,§6/§7及附表A A11逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/2合計5;後測=2/1/2/2合計7;差=2;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-A-ROW-12,SYN-I08E02-2026-01,0038,§6/§7及附表A A12逐筆列,日期=2026-09-08;組別=講授為主對照;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/1合計4;後測=1/1/1/2合計5;差=1;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-01,SYN-I08E02-2026-01,0038,§6/§7及附表A B01逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/0/1/1合計3;後測=2/2/2/1合計7;差=4;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-02,SYN-I08E02-2026-01,0038,§6/§7及附表A B02逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/2/0/1合計4;後測=2/2/1/2合計7;差=3;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-03,SYN-I08E02-2026-01,0038,§6/§7及附表A B03逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=0/1/1/0合計2;後測=1/2/1/2合計6;差=4;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-04,SYN-I08E02-2026-01,0038,§6/§7及附表A B04逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/2合計5;後測=2/2/2/2合計8;差=3;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-05,SYN-I08E02-2026-01,0038,§6/§7及附表A B05逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=0/1/1/1合計3;後測=1/2/1/2合計6;差=3;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-06,SYN-I08E02-2026-01,0038,§6/§7及附表A B06逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=2/1/0/1合計4;後測=2/1/1/2合計6;差=2;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-07,SYN-I08E02-2026-01,0038,§6/§7及附表A B07逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=2/1/1/1合計5;後測=2/1/2/2合計7;差=2;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-08,SYN-I08E02-2026-01,0038,§6/§7及附表A B08逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=0/1/0/1合計2;後測=1/1/1/2合計5;差=3;判定=未達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-09,SYN-I08E02-2026-01,0038,§6/§7及附表A B09逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/1/1合計4;後測=2/2/2/2合計8;差=4;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-10,SYN-I08E02-2026-01,0038,§6/§7及附表A B10逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/1/0/1合計3;後測=1/2/1/2合計6;差=3;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-11,SYN-I08E02-2026-01,0038,§6/§7及附表A B11逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/2/1/1合計5;後測=2/2/1/2合計7;差=2;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL
SYN-B-ROW-12,SYN-I08E02-2026-01,0038,§6/§7及附表A B12逐筆列,日期=2026-09-15;組別=情境練習修訂;渠道=合成紙本情境卡/匿名評分表;同意=是（合成假設）;納入=是（完成前後測且D1-D4均有評分，符合事前完整配對規則）;缺漏=0;重複=0;更正=0（未更動原值）；前測=1/0/2/1合計4;後測=1/1/2/2合計6;差=2;判定=達標,完整示範假設，非協會事實,去識別前後測、課程簽到、同意及資料清理原件,待協會核實之授權角色（身分 UNKNOWN）,SYNTHETIC_REPLACE_BEFORE_REAL


---

## ATTACHED SOURCE: ../0038_R02/evidence/qa/independent_semantic_review_R02.md

## TTQS ONE 0038 R02 獨立語意審查

**整體語意判定：PASS。** 本次直接審查 R02 DOCX 正文、官方來源與當前 Unique Blueprint，沒有沿用 R01 的判斷。

- **DOCX SHA-256：** `bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4`
- **PDF SHA-256：** `f549d34db5d841dc04b61df3ce217a7ad1e2e5ee97d5f53106896ad3f5776012`（14 頁）

兩個 SHA 均與指定值相符，並於審查後重算確認。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/candidate/0038_R02.docx" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render/0038_R02.pdf" purpose="source"}

| 審查項目 | 判定 | 內容與定位 |
|---|---|---|
| 官方映射 | **PASS** | 0038 = I08-E02 = 官方方框 039。§1（第 2 頁）引用官方原文，與官方表第 2 頁及第 3 頁續頁脈絡一致。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/inputs/SOURCE_MAP.md" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/inputs/BLUEPRINT_CURRENT_0038.jsonl" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/inputs/official-2.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/inputs/official-3.png" purpose="source"} |
| 文類與標題盲辨 | **PASS** | 正文呈現設計缺口、方案比較、修訂、執行樣本及成效判讀；遮住標題仍可辨識為訓練方案改善執行紀錄。內容不會被誤認為 0037 的跨期檢討或 0039 的規劃會議紀錄。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-02.png" purpose="source"} |
| 小型志工協會的實用性 | **PASS** | 第 3–5 頁提供可執行的 120 分鐘課程流程、可觀察目標、活動與評量對應、D1–D4 評分量尺及達標規則；第 9–10 頁提供判讀限制與真實資料替換步驟。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-04.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-05.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-10.png" purpose="source"} |
| R01 逐筆追溯缺項 | **PASS** | 附表 A（第 12–13 頁）逐列對應 A01–A12、B01–B12，列出合成渠道、同意與納入理由、缺漏／重複／更正狀態。24 個代碼與正文 24 筆分數紀錄、替換清冊 24 筆逐列紀錄一致；日期亦由 A/B 組執行段落及清冊逐列對應。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-12.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-13.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv" purpose="source"} |
| R01 官方要求交叉索引缺項 | **PASS** | 附表 B（第 14 頁）以五欄連結官方問題、紀錄欄位與位置、SAMPLE／REAL 來源、判定與限制、覆核位置；第 10 頁來源索引也指向附表 B。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-14.png" purpose="source"} |
| SAMPLE／REAL 與權限界線 | **PASS** | 封面及正文說明日期、角色、課程、樣本、分數與決定均為合成示範。第 11 頁及附表 A、B 均明確指出未證明協會實際辦訓、同意、核准或成效；正式角色與權限須由協會核實。 |
| 計算與同案一致性 | **PASS** | 我重新計算 24 筆分數，沒有列級差異。A 組前／後測總分 44／57、達標 3/12；B 組 44／79、達標 11/12；平均增益差 1.83 分、達標率差 66.7 個百分點。方案加權分 A/B/C 為 2.95／4.75／4.10；B08 後測 5 分，正確保留為未達標。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-07.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-08.png" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/render_final/page-09.png" purpose="source"} |
| 14 頁版面與閱讀品質 | **PASS** | 我逐頁檢視 14 張頁面渲染。正文、圖表、附表 A 跨頁表頭及附表 B 均可讀，未見裁切或妨礙操作的斷表。第 11 頁留白較多，但狀態和責任流程仍完整同頁。 |

R02 已補足本次指定的兩項缺項，**沒有發現尚需修復的實質語意缺陷**。審查結果綁定上述 DOCX 與 PDF SHA；現存 manifest／QA 收據仍標示獨立語意審查待辦、正式接受未授與。本次依你的只讀要求未回寫收據，也未修改或重建檔案。:codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/manifest.json" purpose="source"} :codex-file-citation{path="E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/qa/technical_qa.json" purpose="source"}
