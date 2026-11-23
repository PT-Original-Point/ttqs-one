# TTQS ONE isolated writer work package
WORK_ID=TTQS_ONE_0034_I07-E02_WRITER_R01_NEMOTRON_20261118
DOC_ID=0034
REQUIREMENT_ID=I07-E02
ROLE=Writer; produce original requirement-specific document body, not a review.
REQUESTED_MODEL_ROUTE=opencode/nemotron-3.5-lightning-free
SOURCE_PACKET_SHA256=60D822319476A457A5814318F3C96C50E60005792C20BD92F47E9F0DEB89C934
UNIQUE_BLUEPRINT_SHA256=C5FB6EC1552714E18EB2FF3C0363DDC2C57C4A5D953CC1D261193A84EA320845

## Exact deliverable
Return a complete, self-contained Traditional Chinese (Taiwan) document body in Markdown. It is for a learner competency inventory/analysis used to plan appropriate courses. It is NOT a market survey, method-improvement history, course-design process flow, or full downstream course plan. Follow the exact official checkbox and unique Blueprint below.

## Required mechanics
- Start with a decision summary: sample learner cohort, competency gaps, proposed learning response, decisions, and unverified REAL facts.
- Explain scope, learner group/tasks, competency framework/version, evidence-gathering method/date range, evidence source/type/strength, and limits.
- Define observable scale anchors. If no REAL scale exists, use Blueprint's local 1-4 demonstration scale and label it SAMPLE/SYNTHETIC design, never official TTQS scoring.
- Provide a populated learner-by-competency matrix with target, self-reported/observed level kept distinct, evidence location/type/strength, and UNKNOWN where unsupported.
- Calculate each gap only where comparable evidence supports both operands; show formula and operands. A zero/negative gap must not create an unnecessary course. Include one evidence-insufficient item that is explicitly not yet a training need.
- For every priority gap, provide the traceable chain: gap ID and evidence -> observable learning result -> course unit/activity -> selection rationale and non-training alternative -> assessment evidence/rubric -> decision state (proposal/planned, never completed) -> follow-up if not met.
- Complete one internally consistent SAMPLE/SYNTHETIC worked example with differentiated learners or roles, at least one supported training gap and one UNKNOWN/non-training disposition. Totals, ratios, dates, hours, scores, counts and outcomes must recalculate.
- End with a usable evidence index and a per-ID SAMPLE/SYNTHETIC fact and REAL replacement register. Every invented person/code, role, date, sample count, score, ratio, course hour, priority, decision and outcome gets a unique `SYN-0034-...` ID; reuse the same ID when repeating the same fact. Every register ID must appear in the body. Each replacement row gives required REAL source/location and status `UNKNOWN`.

## Truth and boundary rules
- Actual association learners, customer survey, competency standard, learner artifacts, course decisions and performance are UNKNOWN unless the supplied source says otherwise. Do not invent them.
- No third-party originals, certificates, signatures, approvals, external results or achievements. No fake signatures/seals.
- Clearly label synthetic scenario and facts. Do not leave blank/待填/待核 fields or finish with an empty template.
- Use concise evaluator-facing language, filled Markdown tables with short cells, and concrete steps. Target 6-10 substantive pages without filler.
- Do not copy or use another DOCX body. Keep exact negative-neighbor boundaries for 0033/I07-E01, 0035/I07-E03, 0036/I07-E04 and 0049/I11-E01.
- Do not call tools, edit files, claim QA/visual/review/GitHub actions, or include commentary. Output only the full document body in Markdown.

===== FORMAL SOURCE PACKET =====
# SOURCE_PACKET_0034_I07-E02_R01

**Stage:** READY_SOURCE_PACKET  
**doc_id:** 0034  
**requirement_id:** I07-E02  
**Crosswalk title (exact row value):** 針對學員做職能盤點或職能分析並據以規劃適切課_可直接使用成品  
**Source readiness:** READY_FOR_CANDIDATE_BUILD_AS_SAMPLE  
**REAL evidence status:** UNKNOWN

## 1. Selection and occupancy boundary

The repo copy of the formal 129-requirement to 142-deliverable crosswalk maps I07-E02 to exactly one deliverable, 0034. IDs 0025 through 0032 were excluded as instructed. 0033/I07-E01 is the intervening item, but the existing SOURCE_PACKET_MANIFEST for 0028 records codex_active_thread_scope as “0031, 0032, 0033, 0039; no 0028 in summary.” That is an owner-scope warning, not proof of a live 0033 writer. Because it is unresolved, 0033 was conservatively skipped.

Before this folder was created, no 0034/I07-E02 candidate, source packet, dedicated Blueprint, lock, or owner-metadata path was found under E:\tqrepo\docs\ttqs-quality-20261016\quality-review. The proposed output folder was absent, and the local process-command-line scan found no 0034/I07-E02 owner process. The scan did observe unrelated work on 0031 and 0027; neither is this item. Owner state outside this checkout and local host observation is UNKNOWN. This packet makes no global no-owner claim.

## 2. Formal crosswalk binding

Crosswalk readback: docs/ttqs-quality-20261016/quality-review/0028_SOURCE_PACKET_20261117/source/inputs/CROSSWALK_129_REQUIREMENTS_TO_142_DELIVERABLES_R01.csv  
Data rows: 129  
File SHA-256: 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679

The same SHA-256 was independently read from the 0024, 0026, and 0028 repo copies.

Selected raw CSV row (line 29; UTF-8 bytes without line ending):

I07-E02,1,0,0034,針對學員做職能盤點或職能分析並據以規劃適切課_可直接使用成品

Selected-row SHA-256: 57817AF91A28A6544E3E82D950CE6E1F33DA7943C8A31B85F76A8ECBAE1CCE70

## 3. Official requirement and page

Official source: docs/ttqs-quality-20261016/quality-review/0026_R11_20261117/source/inputs/OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf  
PDF SHA-256: 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709  
Page locator: physical PDF page 2, printed page 2, indicator 7 “訓練需求相關的職能分析及應用”, second checkbox in that indicator.

Official checkbox text:

> 針對學員做職能盤點或職能分析並據以規劃適切課程的證明資料。

Canonical text SHA-256 (exact UTF-8 text above, no trailing newline): DFC48B7C01B026F7255A3483D078AE794B912884C760417491DB84CAD218BBA9

Page readbacks checked in this run:
- Existing pypdf full-page readback: docs/ttqs-quality-20261016/quality-review/0031_SOURCE_PACKET_20261118/OFFICIAL_PAGE2_READBACK_PYPDF.txt; SHA-256 3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C.
- Existing pdfplumber full-page readback: docs/ttqs-quality-20261016/quality-review/0031_SOURCE_PACKET_20261118/OFFICIAL_PAGE2_READBACK_PDFPLUMBER.txt; SHA-256 1AC41C2ECB737C004589C0F04422121E751CD22AC6E1F89DA1030A5AF46E17D0.
- Existing page-2 image readback, visually inspected; SHA-256 35A71CB3D892DD81428CE607CE0C0BC2F43694C9B6F080F38F8A55BAFB96EED4.
- Source-binding receipt: docs/ttqs-quality-20261016/quality-review/0031_SOURCE_PACKET_20261118/SOURCE_PACKET_RECEIPT.json; SHA-256 B1CD26DF67395206571135991089CCEE0C3C3BC590986897E0B99D9C4D339BDD. It binds the readbacks to the same official PDF SHA above.

The pypdf readback contains the full checkbox phrase across a line wrap; the pdfplumber readback contains it in adjacent text fragments because table reading order interleaves columns. The existing page image confirms the phrase and checkbox location. This run reread and hash-bound the official PDF and page readbacks and inspected the existing page image. The current local Python lacks pypdf and Poppler pdftotext is unavailable, so no new text extraction or page render is claimed or created.

## 4. 157-item Blueprint index binding

Index: docs/ttqs-quality-20261016/quality-review/0026_R11_20261117/source/inputs/BLUEPRINT_157_CHECKBOXES_LIVE_R01.md  
Index SHA-256: AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216  
Numbered items counted: 157  
Mapped item: 034 (I07, official page 2)

Exact index row (line 87; UTF-8 bytes without line ending):

034｜**職能盤點及課程規劃：評分與落差、真實示例**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

Index-row SHA-256: 06F473BD5B25ED541690A4F035EEC0BA08B3F2B8FCADD7B723AD55A3B912F61F

The official PDF is the requirement authority; the index is a candidate content specification. They agree on learner competency inventory/analysis and course planning from the identified gaps.

## 5. Genre boundary and negative neighbors

This deliverable is a learner competency inventory and gap-to-course fit analysis. It must show what learners need to do, what evidence indicates their current level, how gaps were interpreted, and why selected course content addresses those gaps.

- 0033 / I07-E01: customer, learner, and competency-needs investigation and course planning. Keep broad survey and demand-planning evidence there; reference its verified inputs when available. Do not substitute a survey for the learner-level competency analysis here.
- 0035 / I07-E03: review and improvement of competency-analysis methods over time. Do not turn this item into a method-review history.
- 0036 / I07-E04: course-design schedule, process flow, and training-plan artifacts. Do not make those process-control artifacts the main deliverable.
- 0049 / I11-E01: course plan aligned to commissioning organization, learners, and competency needs. Use only enough module and assessment detail to substantiate the 0034 gap-to-course match; do not duplicate the full downstream course plan.

## 6. Required output mechanics

The future DOCX must be a complete, readable analysis with filled tables and a worked example, not a blank questionnaire or heading-only shell. At minimum it must contain:
1. A concise decision summary naming the analyzed learner group, the competency gaps found in the example, the selected learning response, and what remains unverified.
2. Scope, cohort/role definition, competency framework and version, evidence-gathering method, evidence dates, and the source or SAMPLE/SYNTHETIC status of each input.
3. A defined competency scale with observable anchors. Any local scale or prioritization rule must be labeled as a demonstration design, not an official TTQS score or threshold.
4. A competency inventory and learner/evidence matrix separating target level, observed or reported current level, evidence source, evidence strength, and UNKNOWN values.
5. A gap calculation and rationale for each selected competency; show the operands and do not hide group variation behind an average.
6. A traceable gap-to-course matrix: gap → learning objective → topic/module → practice → assessment evidence → planned decision. State why the planned course addresses the gap and identify non-training or further-validation responses where appropriate.
7. A filled SAMPLE/SYNTHETIC case that is internally consistent, includes a clear decision, and can be recomputed from its registered facts.
8. An evidence index with document/page or record locator, source class, supported claim, and status.
9. Cross-document references that identify upstream needs evidence and downstream course-plan artifacts without claiming they exist or are accepted.

## 7. SAMPLE/REAL truth boundary and readiness decision

The official crosswalk, official PDF, page readbacks, and index establish the requested deliverable and its genre. They do not establish this association’s current learner group, client demand, competency framework, participant scores, assessment results, or delivered courses. Those association facts are UNKNOWN in this source packet.

Build readiness: READY_FOR_CANDIDATE_BUILD_AS_SAMPLE. The future example may use a coherent fictional learner group and invented competency evidence only when every invented person label, date, count, score, ratio, decision, course detail, and outcome is visibly marked SAMPLE/SYNTHETIC and registered under unique fact_id values. Do not fabricate survey returns, real participant records, employer statements, certificates, signatures, approvals, or completed outcomes. Keep any planned assessment distinct from an actual result.

The 2026-10-23 R11 control documents named in the task are not present at their expected paths in this checkout. This packet follows the R11 override supplied in the Human instruction and does not infer unseen control-plane state.

## 8. Stage limits

This folder contains only this source packet, its unique Blueprint, and the SHA receipt. No DOCX was created; no model or agent was called; no Word COM or new PDF render was used; no queue, CURRENT, dashboard, shared fact register, or GitHub state was changed; no commit was made.
===== UNIQUE BLUEPRINT =====
# UNIQUE_BLUEPRINT_0034_I07-E02_R01

**Stage:** READY_UNIQUE_BLUEPRINT  
**doc_id:** 0034  
**requirement_id:** I07-E02  
**Blueprint genre:** 學員職能盤點與課程適配分析報告  
**Crosswalk title (exact row value):** 針對學員做職能盤點或職能分析並據以規劃適切課_可直接使用成品

## 1. 唯一驗收目的

讀者能從一份可抽查的分析中，沿著「學員或群體 → 職能要求 → 現況證據 → 差距 → 課程選擇 → 評量證據」追溯判斷：依據哪些學員職能分析規劃了哪些適切課程，以及每個課程選擇如何回應已辨認的差距。

官方要求錨定在訓練機構版《查核佐證文件資料表》PDF 第 2 頁、指標 7「訓練需求相關的職能分析及應用」第二個佐證方框。正式 crosswalk 對應 I07-E02 至 0034。官方來源沒有規定特定評分量尺、公式或課程時數；Blueprint 不得把示範量尺冒充官方門檻。

## 2. 文件形態與讀者用途

製作一份完整的職能盤點及課程適配分析報告，讓訓練規劃者、課程負責人和抽查者可以：

- 看出分析對象、任務或職務邊界，以及每項職能要求來自何處。
- 分辨目標程度、目前證據、學員自評、觀察或作品證據及其可信程度。
- 重算每項差距並檢查群體差異，不以平均數掩蓋個別需求。
- 看出每項優先差距如何連到學習目標、課程單元、練習和評量證據。
- 分辨建議、計畫、SAMPLE/SYNTHETIC 演練和已發生的 REAL 結果。

## 3. 專屬內容結構與 mechanics

### A. 決策摘要

摘要須列出分析範圍、主要差距、建議的訓練或非訓練處置、決策理由、支持它的資料狀態，以及尚未驗證的事項。不能只重述需求或課程名稱。

### B. 範圍、來源與職能要求

以可追溯表格記錄：

| 必要欄位 | 填寫與判讀規則 |
|---|---|
| 對象／群體及任務範圍 | 使用有來源支持的對象描述；合成示例以虛構代碼識別，不使用真實可識別個資 |
| 職能項目與可觀察行為 | 把抽象標籤拆成可檢查行為；說明其與任務的關係 |
| 要求程度及依據 | 引用有版本的職務、客戶要求、課程標準或其他來源；缺來源時標 UNKNOWN，不偽稱協會制度 |
| 資料期間及方法 | 說明自評、結構式訪談、工作樣本、觀察或其他方法；列出題目/量規版本與限制 |
| 證據定位 | 記錄檔名、頁碼/段落、日期或行號、資料性質及狀態 |

不得把 I07-E01 的市場或客戶需求調查、或本 Blueprint 自行設計的案例，寫成已核實的現行職能標準。

### C. 量尺與證據可信度

若真實來源沒有既定量尺，可採以下清楚標示為 SAMPLE/SYNTHETIC 的教學示例尺度：1 為需逐步指導；2 為可完成部分步驟但需檢核；3 為能依標準獨立完成；4 為能處理變化並說明判斷。這是案例用管理設計，不是官方 TTQS 評分量尺或通過標準。

每筆目前程度須附證據種類與強度，例如學員自評、情境題、操作作品、結構式觀察或經核實的主管紀錄。自評不得改寫成觀察事實；來源不足、互相矛盾或沒有直接證據時列 UNKNOWN/需驗證，不填入推測分數。

### D. 職能盤點和差距判讀

以「對象 × 職能」呈現目標程度、目前程度、來源、證據強度、差距、判讀與限制。若採用教學示例公式，明列：

差距 = 目標程度 − 目前程度

只在兩端都有可比且有來源支持的值時計算。示例中的正差距表示待發展項目；零或負值不得自動導出不必要課程。說明優先順序的理由，並保留需要不同支援的個別差異。不得把這個示範公式或任何建議優先級描述為 TTQS 官方規定。

### E. 差距至課程設計的可追溯鏈

每個列為優先的差距至少須能沿下列欄位逐列查驗：

| 欄位 | 必須回答 |
|---|---|
| 差距 ID 與支持證據 | 哪一個可定位證據支持本項判讀？ |
| 預期學習結果 | 學員學完後需展示何種可觀察行為？ |
| 課程單元/活動 | 哪個內容或練習直接處理該行為？ |
| 選擇理由 | 為何此活動適配此差距？有何更小或非訓練替代方案？ |
| 評量證據 | 用何種題目、操作或作品確認學習？列評分錨點或判讀規則 |
| 決策狀態 | 建議、已規劃、待驗證或已執行；未提供執行原件時不得標成已執行 |
| 後續處置 | 未達示例目標、資料不充分或差距非訓練所能處理時如何處置 |

這是證明適配性的最小規劃細節，不是完整課程執行計畫。每個重點差距至少要有一條完整鏈；不得用「安排相關課程」代替。

### F. 完整 SAMPLE/SYNTHETIC worked example

為避免空表，候選文件須完成一個內部一致的虛構案例。可選一個虛構學員群體、數項可觀察職能、明示的目標程度與證據、逐項差距、課程單元和可檢查的評量計畫。案例應展示至少一項需要訓練的差距，以及一項不應直接判為訓練需求的情況（例如資料不足或問題需要先驗證）。

所有虛構姓名/代碼、角色、日期、樣本數、評分、課程時數、優先級、比率、決策和結果均逐項登錄唯一 fact_id；每頁及表格清楚標示 SAMPLE/SYNTHETIC。重算差距和彙總值，列分子、分母及算式。若寫入未來或預定評量，標為「計畫」，不可寫成已完成訓練、已改善能力或實際績效。不得仿造第三方簽名、機構回覆、證照或原始作品。

### G. 證據索引與交叉文件

文末索引逐項連接主張、來源文件/頁碼或段落、來源類別、支持範圍和 REAL SOURCE / UNKNOWN / SAMPLE/SYNTHETIC 狀態。引用其他交付物時只記錄可驗證的 cross-reference，不假定其存在或已接受。

## 4. 負向近鄰與拒收邊界

- 0033 / I07-E01 是需求調查及規劃來源；本件可以引用經核對的需求，但不能用調查表代替學員職能盤點和差距分析。
- 0035 / I07-E03 著重職能分析/運用方法的檢討改進；本件不冒充跨期方法改進紀錄。
- 0036 / I07-E04 是課設進度、流程圖和訓練規劃書等成套產出；本件不以通用流程圖或空白規劃表取代差距至課程的證據鏈。
- 0049 / I11-E01 是更下游、面向業主/受訓者/職能需求的課程計畫；本件只保留證明適配所需的學習目標、單元與評量，不重製整份課程計畫。
- 不以只有自評的分數宣稱客觀能力，不以課程名稱宣稱差距已消除，不把單一群體平均值當成每位學員的需求。
- 不填入沒有來源的協會現況、真實學員、客戶需求或課程成效。

## 5. 真實資料、合成示例與 source binding

本階段讀到的正式 crosswalk、官方佐證資料表、頁面 readbacks 和 157-item index 沒有提供協會真實學員名冊、客戶調查、職能標準、個人作品/評量、現行課程決策或執行成效。這些事實保持 UNKNOWN。

Source binding:
- Crosswalk SHA-256: 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679
- Selected crosswalk raw-row SHA-256: 57817AF91A28A6544E3E82D950CE6E1F33DA7943C8A31B85F76A8ECBAE1CCE70
- Official PDF SHA-256: 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709; physical/printed page 2, indicator 7, second checkbox
- Canonical official checkbox-text SHA-256: DFC48B7C01B026F7255A3483D078AE794B912884C760417491DB84CAD218BBA9
- 157-item index SHA-256: AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216
- Index item 034 raw-row SHA-256: 06F473BD5B25ED541690A4F035EEC0BA08B3F2B8FCADD7B723AD55A3B912F61F

## 6. Readiness and independent review boundary

Source and genre are sufficient to build a complete SAMPLE/SYNTHETIC candidate: READY_FOR_CANDIDATE_BUILD_AS_SAMPLE. REAL association facts remain UNKNOWN. Candidate readiness does not mean semantic PASS, formal acceptance, CURRENT, REAL, approved, or effective. The future exact candidate still requires the configured deterministic gate and a fresh independent exact-SHA semantic/usability review under the applicable current control.

## 7. Writer constraints

Create a new requirement-specific body from the official source and this Blueprint. Do not copy a peer DOCX body or reuse another item’s tables as a substantive template. Preserve exact 0033/0035/0036/0049 boundaries. Keep all synthetic claims visibly classified and uniquely registered; never make up third-party evidence or real results.
