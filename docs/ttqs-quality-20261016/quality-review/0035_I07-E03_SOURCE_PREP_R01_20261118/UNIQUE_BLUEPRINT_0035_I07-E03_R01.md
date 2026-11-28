# UNIQUE_BLUEPRINT_0035_I07-E03_R01

**Stage:** READY_UNIQUE_BLUEPRINT  
**doc_id:** 0035  
**requirement_id:** I07-E03  
**Blueprint genre:** 職能分析與運用方法檢討改進報告  
**Crosswalk title (exact row value):** 對相關職能分析及運用的方法均能適時檢討隨時改_完整工作稿

## 1. 唯一驗收目的

讓讀者可以追查職能分析及運用方法的版本、檢討依據、問題判讀、改善決策、方法變更和後續驗證。文件需回答：何時檢討、檢查什麼、依據哪些案例或紀錄、發現何種限制、改了哪些方法、改版後如何確認改善，以及哪些結果仍未知。

官方佐證表 PDF 第 2 頁指標 7 第三個方框要求對相關職能分析及運用的方法適時檢討並改進。官方沒有指定週期、評分算法、統計門檻或核准流程；本 Blueprint 不創設官方規則。

## 2. 文件形態與用途

製作一份方法檢討與改善追蹤報告，主體是方法本身及其前後變更證據，而非某一學員的職能評量或完整課程計畫。每個改善主張應連到可定位的前態證據、決定、改版內容及後態查驗。

讀者應能區分：
- 已核實的 REAL 方法、版本與檢討紀錄；
- 因缺少真實紀錄而尚未確認的 UNKNOWN 欄位；
- 用來展示檢討閉環的 SAMPLE/SYNTHETIC 案例。

## 3. 專屬內容結構與 mechanics

### A. 檢討範圍與方法版本

首頁摘要後，記錄檢討對象、適用的職能分析及運用步驟、方法版本/日期/來源、使用情境、檢討觸發原因、資料期間、參與角色及權責來源。沒有版本文件、觸發紀錄或授權證據時標 UNKNOWN；不可用推測補成協會現況。

### B. 方法流程與檢查標準

以版本化流程或表格列出各步驟的輸入、判讀規則、輸出、留存證據和失效分支。至少檢查：

- 任務或需求如何轉為職能項目及可觀察行為；
- 要求程度、評量錨點和來源是否清楚；
- 自評、訪談、作品、觀察等證據是否被正確區分；
- 不同評估者能否依同一規則得出可解釋的判斷；
- 差距、優先順序及應用決定是否可追溯到證據；
- 對資料不足、矛盾、偏差或不適合用訓練解決的情況是否有處置；
- 方法輸出能否被下游規劃者使用，而不失去來源與限制。

標準須可觀察和可覆核。任何量尺或一致性指標均須說明操作定義與用途，並標示其為內部或 SAMPLE 設計；不得暗示為官方評核門檻。

### C. 前態證據與問題判讀

每項發現使用唯一 finding_id，至少列出：

| 欄位 | 判讀要求 |
|---|---|
| 方法版本/步驟 | 指向受檢方法和實際步驟 |
| 證據及定位 | 文件、頁碼/段落、紀錄日期或案例代碼，並標 REAL SOURCE / UNKNOWN / SAMPLE |
| 觀察到的缺口 | 描述規則不清、證據不足、結果不一致、應用中斷或其他具體情況 |
| 影響與限制 | 說明可能影響何種判讀或規劃；區分已觀察與推論 |
| 根因假設 | 列出可查證原因及待驗證處，不把假設寫成事實 |
| 處置決定 | 採納、拒絕並說明理由、試行或待核 |

不要僅以「需要改善」作為發現，不以單一虛構故事聲稱真實制度缺陷。

### D. 改版與前後對照

每項採納或試行的變更，列出舊版規則/欄位、改版後規則/欄位、變更理由、影響步驟、版次差異、負責角色的來源狀態，以及生效/試行/待核狀態。前後比較須盡量固定案例、輸入和評量條件，使讀者看出差異來自方法變更或指出無法排除的混淆因素。

用同一組可追溯案例重走方法流程，呈現前後判斷、理由、證據鏈是否完整、適用分支及使用者可理解性。只有在有證據支持時才計算一致性、覆蓋率或錯誤率；列出分子、分母和公式，並說明小樣本限制。不存在的現況數據標 UNKNOWN，不補造 REAL 基線。

### E. 改善行動與驗證閉環

追蹤表至少包括 finding_id、修訂動作、責任角色/授權狀態、目標日期/檢查點、版本或紀錄定位、執行狀態、驗證方法、驗證證據、結果及下一步。把四種狀態清楚分開：建議、已決定、已實施、已驗證。無原件時不得寫成已核准或已完成。

對未改善、資料不足或改善副作用，記錄保留問題、暫行風險控制、是否需要補充案例/評估者、下一次檢討觸發條件。

### F. 完整 SAMPLE/SYNTHETIC worked example

候選文件須完成一個可重算的合成案例：明確標出被檢方法版本為虛構示例，展示具體方法缺口、一項明確修訂、相同或可比案例的前後重新判讀、檢討決策和後續查驗狀態。案例至少包含一個已改善的可觀察方法特性，以及一個仍未知或待驗證的限制，讓結尾形成真實的改善追蹤結果而非空表。

所有虛構角色、日期、版本、案例數、評分、計算值、finding、變更、決策及結果，逐項登錄唯一 fact_id；每頁及表格標示 SAMPLE/SYNTHETIC。若後態只是設計或預定試行，必須標「計畫/待驗證」，不可寫成實際完成。不得仿造會議簽名、核准或協會真實檢討紀錄。

### G. 證據索引與事實狀態

文末以索引連結每項方法主張、版本、紀錄位置、來源類別、支持範圍和 REAL SOURCE / UNKNOWN / SAMPLE/SYNTHETIC 狀態。交叉引用相鄰交付物時只記錄已可定位的文件，不宣稱其候選存在、已完成或已接受。

## 4. 負向近鄰與拒收邊界

- 0033 / I07-E01 是需求調查和需求配適規劃；本件檢討職能分析及運用方法，不重作客戶/學員調查。
- 0034 / I07-E02 是學員職能盤點、差距判讀及課程適配；本件不重製學員評量報告或干擾其 W1 寫作。
- 0036 / I07-E04 是課程設計進度、流程圖和規劃書等產出；本件不以這些工具文件取代前後方法比較。
- 0031 / I06-E02 聚焦訓練人員職能評估方法；本件聚焦 I07 設計指標中的職能分析與運用方法檢討，避免混同人員任職/職能證明。
- 0049 / I11-E01 是下游課程計畫；本件只追蹤方法輸出如何被使用，不產出整份課程方案。

## 5. SAMPLE/REAL truth boundary與source binding

目前正式 crosswalk、官方佐證資料表、頁面 readbacks 和 Blueprint index 沒有證明協會實際使用中的方法版次、檢討週期、評估者、會議決定、修訂紀錄或改善結果；這些均為 UNKNOWN。

Source binding:
- Crosswalk SHA-256: 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679
- Selected crosswalk raw-row SHA-256: 37234356C7F899B23DDDA413BF9414ECBA9DCAB9AA8A8371E346577B6608420A
- Official PDF SHA-256: 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709; physical/printed page 2, indicator 7, third checkbox
- Canonical official checkbox-text SHA-256: EBE1EFED47EA845CAC6E58290CFF84521A41AA50F0B888646F1CFAB1F893524B
- 157-item index SHA-256: AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216
- Index item 035 raw-row SHA-256: CBAEB2F6BDAE04BA9ABAA051A07433CC6F4AD321DBAD4DBC16AAEBBD140A80A4

## 6. Readiness and independent review boundary

Source and genre are sufficient for a complete SAMPLE/SYNTHETIC candidate: READY_FOR_CANDIDATE_BUILD_AS_SAMPLE. REAL association records remain UNKNOWN. Candidate readiness is not semantic PASS, formal acceptance, CURRENT, REAL, approved or effective. The future exact candidate still requires its applicable deterministic gate and fresh independent exact-SHA semantic/usability review.

## 7. Writer constraints

Write a unique requirement-specific review report from the official source and this Blueprint. Do not use peer DOCX body text or peer substantive tables as templates. Preserve boundaries with 0033, 0034, 0036 and 0031. Register synthetic facts individually and do not invent signatures, approvals, actual review history or realized improvement.