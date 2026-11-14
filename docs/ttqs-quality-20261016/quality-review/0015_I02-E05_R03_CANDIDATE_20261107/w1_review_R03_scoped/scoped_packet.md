# Prior full independent review
# Independent Semantic Review — TTQS 0015 / I02-E05 客戶需求評估與回覆表 (candidate R02, SAMPLE)

## Scope limitations (stated up front)
Text-only semantic review. I did not perform font/point-size inspection, independent SHA-256 byte hashing, visual/page-layout verification, or any official acceptance act. SHA values below are quoted from the packet, not recomputed.

---

## 1. Official requirement fidelity
- **P014** reproduces the official text verbatim: 「客戶提出的課程需求的相關表單 （文件），而揭露的呈現方式， 可以為EDM、海報、網站網頁等方式加以呈現。」 — exact match including spacing. **PASS.**
- **P015** anchors source to PDF p.1 and correctly states the internal-evaluation scope: the customer's original form is retained by 0014; public disclosure is proven by 0016/0017 artifacts and their publication records, not by this internal form. This is the correct semantic response to I02-E05 for the assessment/response genre — it does not impersonate the public disclosures nor the intake form.

## 2. Blueprint structural completeness
All required sections map: 30-second use block (P006–P011), §1 official req/scope, §1.3 dictionary + inclusion/exclusion (TABLE 1 rows 納入/排除), §2 receipt/clarification/controls (TABLEs 2–4), §3 scale/weights/decision gates (TABLEs 5–7), §4 results/limitations/actions (TABLEs 8–9), §5 reply draft & timelines (TABLEs 10–11 + draft text), §6 channel gates (TABLE 12), §7 handoff (TABLE 13, §7.2 closure conditions), §8 HOLD/rejection/appeal (TABLEs 14–15), §9 register (TABLE 16), §10 REAL acquisition list (TABLE 17), §11 requirement mapping + negative neighbors (TABLEs 18–19). All five required tables are present. **PASS with one gap (defect D1 below).**

## 3. Mathematical correctness (all recomputed)
- Weighted score: weights 20+15+15+10+15+10+10+5 = **100** ✓; weighted components (80+60+45+40+45+20+40+20) = 350; 350 ÷ 5 = **70/100** ✓ (P031 and TABLE 6 total row consistent; denominator 100 and per-item 5 stated; integer retention stated; N/A rule stated and confirmed absent).
- Cost chain: 6×3,000=18,000; 4×1,500=6,000; 12×250=3,000; 6×1,000=6,000; 1×2,000=2,000; subtotal **35,000** ✓; coordination 10% = 3,500 ✓; planning subtotal **38,500** ✓; balance 48,000−38,500 = **9,500** ✓, correctly labeled “不得稱為利潤” (P032, SYN-041).
- Course skeleton: 1+1.5+1.5+1+1 = **6 h** ✓ (TABLE 13, SYN-057–062).
- Completeness stats: 8÷8=100%, verified originals 0÷8=0% ✓ (P038, SYN-051/053).
- Decision routing: 70 falls in 65–79 → 附條件接受 (TABLE 7), consistent with P035 and hard-gate override row. **No arithmetic defects.**

## 4. Synthetic register coverage
TABLE 16 embeds the full register verbatim (SYN-001–073 + CTRL-01–08), matching the controlled register exactly in values, locators, replacement sources and responsible roles. I traced every SYN/CTRL key to at least one body occurrence and found no orphan keys and no unregistered substantive synthetic fact. Closest candidates: draft version "R01" (TABLE 11) — covered in substance by SYN-055 though not keyed; acceptable. **PASS.**

## 5. Fully populated coherent SAMPLE
No empty cells, no 「待填／待核」， no future-tense-as-completion in TABLEs 1–15, 17–19 or the draft (P045–P054). The single blank cells in TABLE 6's 合計 row are structural aggregate cells, not placeholders. Internal coherence holds: 12 people/6 h/Nov wk2/NT$48,000 propagate consistently across TABLEs 1, 2, 3, 13; the draft (P048–P050) matches the sample facts and explicitly forbids treating the draft as sent. **PASS.**

## 6. Real vs synthetic boundaries
Boundary declarations are dense and consistent: P003/P004 (no real client, approvals, sending), P020, P025, P028 (all scores non-V), P032 (estimates not quotes), P034, P043, P053, P070, P072, P077, plus §10 as an explicit REAL-acquisition zone and TABLE 17's closure condition requiring per-key verifications before SAMPLE labels may be removed. Third-party originals (certificates, signatures, contracts) are only indexed for lawful acquisition, never fabricated (TABLE 17 row「合約及第三方原件」； H03 row in TABLE 14). **PASS.**

## 7. Distinction from 0014/0016/0017 and adjacent requirements
- vs 0014: P005 + TABLE 2 row 2 + TABLE 19 row 1 — key-reference only, no re-created intake fields, TABLE 1 limitation「0014 本身未建立或讀取」keeps the sample honest.
- vs 0016/0017: P005, §6, TABLE 12, TABLE 19 rows 2–3 — no publishable ad copy or page body; only gates and version references.
- vs 0013 (I02-E04) and 0018 (I03-E01): TABLE 19 rows 4–5 explicitly reject both. Blind-title identifiability is achieved via the unique mechanism chain 澄清→評分→決策→回覆草稿→交接 (TABLE 18 last rows). **PASS.**

---

## Defect register (substantive items only, by exact location)

| # | Severity | Location | Defect |
|---|----------|----------|--------|
| D1 | Minor | Missing section | Blueprint `required_sections` includes 「附件索引、覆核與版本」； §11 (P073–P077) covers 覆核/版本/證據位置 but no explicit attachment/appendix index exists. Since no external attachments are claimed, an explicit N/A statement or a one-row index referencing §11.1 evidence locators would close it. |
| D2 | Minor | P022–P024, P027, P029, P033, P037–P040, P042, P044, P058, P063, P067, P074–P075 | Heading-to-table mapping is purely positional (TABLE 1–19 are never referenced by number in the prose). Readers must infer the pairing by sequence; adding 「如表 N」 to each heading would remove ambiguity. |
| D3 | Minor | P003 vs TABLE 11 row 3 | Two version axes collide without explanation: 本稿 R02 vs 回覆草稿 R01. Both are defensible (document revision vs unrevised draft) but the text never states they are distinct objects. |
| D4 | Minor | P006–P011 | The 30-second block omits the blueprint's primary reader (主管與決策者)； readership is only implied by P002. |
| D5 | Trivial | P049 | 「請在實際寄出通知所列的補充期限前確認日期…」 is mildly self-referential in a draft that is itself the notification; recommend rephrasing to 「請在本件回覆所列期限前…」. |
| D6 | Packet-level | Packet header | Candidate SHA `f2507c73…` differs from `existing_worker_draft_sha256` `e77db0bd…` with `draft_state: UNADOPTED_NOT_REVIEWED`. Unresolvable in text-only scope; requires byte-level verification outside this review. |
| D7 | Trivial | P038 | No explicit analysis period is declared for §4.1 statistics (the case timeline 2026-10-29 收件 implies it, but the period is not stated as a parameter). |

No substantive defects were found in: official-text fidelity, requirement response mapping, calculations, denominators/rounding, register completeness, inventions/impersonation, neighbor contamination, or SAMPLE/REAL labeling.

---

## Verdict: **PASS**

Reasoning: the candidate meets the blueprint's genre contract as a 客戶需求評估與回覆表 — every required table exists and is fully populated, all arithmetic recomputes correctly with denominators stated, the synthetic register is embedded complete and traceable with no orphans, real/synthetic boundaries are enforced at every load-bearing claim, the official requirement is quoted exactly and answered within genre, and all five neighbor deliverables (0013/0014/0016/0017/0018) are positively differentiated with rejectable difference fields. The seven defects listed are navigability, labeling, and packet-lineage issues (D1–D7); none changes the document's meaning, validity, or evidence posture. Recommended fixes (D1–D5) are cosmetic and should be applied in a next revision, but do not block adoption on semantic grounds.
# Exact content difference
--- R02

+++ R03

@@ -1,6 +1,6 @@

 P000 0015｜客戶需求評估與回覆表
 P001 需求識別： I02-E05
-P002 文件用途： 內部課程需求評估、決策、客戶回覆草稿與課程設計交接。
-P003 本稿狀態：R02 SAMPLE 候選；完整工作案例均為 SAMPLE／SYNTHETIC。
+P002 文件用途：供主管與決策者及承辦角色進行內部課程需求評估、決策、客戶回覆草稿與課程設計交接。
+P003 本稿狀態：R03 SAMPLE 候選；完整工作案例均為 SAMPLE／SYNTHETIC。
 P004 真實性界線： 本稿沒有真實客戶、合約、講師或場地能力證明、核准、寄送、排課或服務承諾。示範角色與數值不得移作機構實績。
 P005 與 0014 的界線： 0014《客戶課程需求申請表》負責客戶提出需求及收件；本件只引用其案件識別碼及必要摘要，負責內部澄清、評估、決策、回覆和交接，不重製申請／收件欄位。0016 EDM 與 0017 網站課程揭露頁是另行製作的公開揭露成品，本件只記錄其發布條件與交接資訊。
@@ -37,5 +37,5 @@

 P036 4. 分析結果、限制與行動
 P037 4.1 母數、趨勢及證據強度
-P038 本案例母數為 1 件虛構需求；8 個評分面向已評分，評分完整率為 8 ÷ 8＝100%。真實原件核實數為 0 ÷ 8＝0%。單一 SAMPLE 案件不能支持客戶分群、趨勢、機構能力或歷史接案率推論；因此不製作趨勢圖，不把一件案例外推成實績。分數只展示算法與決策路由。
+P038 本案例分析期間為合成收件日 2026-10-29 的單一演練；母數為 1 件虛構需求。8 個評分面向已評分，評分完整率為 8 ÷ 8＝100%。真實原件核實數為 0 ÷ 8＝0%。單一 SAMPLE 案件不能支持客戶分群、趨勢、機構能力或歷史接案率推論；因此不製作趨勢圖，不把一件案例外推成實績。分數只展示算法與決策路由。
 P039 4.2 差距優先序
 P040 4.3 結論、證據、建議與追蹤
@@ -48,5 +48,5 @@

 P047 您好：
 P048 感謝提出 Excel 資料整理與視覺化課程需求。依本 SAMPLE 情境中的需求摘要，我們可先整理一份 6 小時的初步設計方向，目標包括建立樞紐分析圖、解讀 KPI 並撰寫行動摘要。
-P049 目前僅為「附條件的初步設計建議」。確切日期、講師資格與可用時段、場地容量及設備、無障礙需求、正式費用與服務範圍仍須逐項確認；目前沒有完成排課、正式報價、合約簽署或開課承諾。請在實際寄出通知所列的補充期限前確認日期、場地／設備及參訓需求，以便重新核對資源與費用。若資料尚未齊全，本案將維持 HOLD，待資料完整後再評估。
+P049 目前僅為「附條件的初步設計建議」。確切日期、講師資格與可用時段、場地容量及設備、無障礙需求、正式費用與服務範圍仍須逐項確認；目前沒有完成排課、正式報價、合約簽署或開課承諾。請在本件回覆所列的補充期限前確認日期、場地／設備及參訓需求，以便重新核對資源與費用。若資料尚未齊全，本案將維持 HOLD，待資料完整後再評估。
 P050 在核實需求、能力、資源及核決權限之前，我們不會將本課程定稿或公開發布。後續若產生 EDM、海報或網站課程頁，會另行核對內容、版本及發布授權。
 P051 敬祝順心
@@ -75,6 +75,7 @@

 P074 11.1 需求對照及使用條件
 P075 11.2 負向鄰項辨別
-P076 來源定位：訓練機構版 TTQS 查核佐證資料表第 1 頁；本件對應 I02-E05 客戶課程需求。
-P077 文件狀態：本件為 SAMPLE／SYNTHETIC 候選稿，未完成品質驗收；不是 REAL 成案，也不是機構核准、客戶通知或課程承諾。
+P076 附件與證據索引：本合成示例沒有真實外部附件；官方要求來源見本節來源定位，示例事實與替換方式見第 9 節，真實資料原件需求見第 10 節。實案若有附件，應記錄名稱、版本、來源、保存位置及授權狀態。
+P077 來源定位：訓練機構版 TTQS 查核佐證資料表第 1 頁；本件對應 I02-E05 客戶課程需求。
+P078 文件狀態：本件為 SAMPLE／SYNTHETIC 候選稿，未完成品質驗收；不是 REAL 成案，也不是機構核准、客戶通知或課程承諾。
 T00 R000 欄位 | 定義／分母 | 本案例值 | 來源與證據強度 | 限制
 T00 R001 案件鍵 | 0015 內部追蹤鍵 | SYN-015-001 | SAMPLE 情境 | 不可當作真實案件編號
@@ -154,5 +155,5 @@

 T10 R001 回覆案件鍵 | SYN-015-001
 T10 R002 草稿狀態 | SAMPLE；未核准、未寄送
-T10 R003 草稿版次 | R01
+T10 R003 草稿版次 | R01（回覆草稿版次；與本文件 R03 修訂版次分開）
 T10 R004 對象 | CL-SYN-01（虛構代碼；不是電子郵件地址或真人）
 T10 R005 建議寄送期限 | 資料完整後 5 個工作日內；本例只展示流程，未計算真實寄送日期
# Previous SHA f2507c73a7cb92729e5b574ebd04997c5c716c28cfc83cddbc5e14a263da676d
# Candidate SHA 384082390bc7322e3cb58d9c0dc4e195af2a5eff40506681e7f12e5c2a7af635