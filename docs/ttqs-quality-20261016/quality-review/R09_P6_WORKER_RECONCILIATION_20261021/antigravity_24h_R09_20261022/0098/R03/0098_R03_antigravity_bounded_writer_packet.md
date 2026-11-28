TTQS ONE bounded writer patch task. Work only from the included R02 excerpts. Do NOT edit files, use tools, use Computer Use, or emit a new full manuscript. Return one JSON object only, with schema:
{
  "verdict":"PATCH_READY or BLOCKED",
  "base":{"document_id":"0098","requirement_id":"I18-E06","revision":"R02","manuscript_sha256":"...","register_sha256":"..."},
  "section_replacements":[{"section_heading":"exact heading","replacement_markdown":"complete replacement for that one subsection"}],
  "register_updates":[{"fact_id":"FACT-0098-003","field_or_locator":"..."}],
  "register_additions":[{"fact_id":"FACT-0098-119","document_id":"0098","requirement_id":"I18-E06","field_or_locator":"...","value":"...","classification":"SAMPLE/SYNTHETIC or SOURCE/CONTROL","source_or_basis":"...","real_replacement_needed":"YES/NO","real_replacement_source":"...","owner_role":"...","verification_rule":"...","printed_page":"PENDING_FINAL_RENDER"}],
  "retired_duplicate_id_lineage":{"FACT-0098-074":"FACT-0098-022",...},
  "checks":{"main_12_invite_flow_unchanged":true,"main_10x5_matrix_unchanged":true,"no_real_people_or_approvals":true}
}

Authority: official page 7 exact text and unique Blueprint are included. Do not alter requirement, core case, dates, main flow counts, score matrix, or R02 arithmetic. R02 DOCX exact SHA is a3888f6e7582050379126d0f6cb384167fc43b110b1f9bed713ff38585756021; it remains historical. Intended R03 must address exact-SHA reviewer findings below with minimal bounded additions.

REPAIRS REQUIRED:
1) P2-01: label the invented Q3 2026 cohort/program name explicitly SAMPLE/SYNTHETIC in §2.1; add a fact-level replacement-register row for cohort/period/population scope, with REAL replacement source and role/check.
2) P2-02: add a row-level `告知／問卷版本` field to §3.4 Table 3.4 and a matching register row. Include a short, practical synthetic notice/consent text associated with `SYN-NOTICE-v1`; state consent is voluntary, purpose is only system/process feedback, declining has no service/training consequence, only minimal coded data, REAL retention/contact/authority must be filled from approved policy and is UNKNOWN here. Preserve L08 as no response/no individual consent.
3) P2-03: add a compact role alias matrix in §3.1 or §8.1 mapping operational sample roles to candidate REAL evidence-owner roles and the second-review/authorization rule. Explicitly say candidate titles are not asserted current association posts/appointments; REAL role assignment requires governing documents. Clarify §8.1 roles are evidence-source owners, distinct from operational actors.
4) P3-01: correct FACT-0098-003 duplicated locator using register_updates; include tombstones for duplicate fact IDs 074–085 merged to 022–033 and 089–091 merged to 051–053. Add locator coverage for §1.4, §7.1, §8.1 in a register/receipt, not by changing unrelated DOCX control facts. Do not invent lost content.
5) P3-02: add a brief clearly synthetic zero-denominator vignette in §5.2 and cross-reference it from §5.4: group N=0 => mean=N/A (denominator zero), never 0; exclude from weighted overall mean and disclose N=0. It must not alter current sample counts.
6) P3-03: add one complete synthetic withdrawal event record (request/source/time/scope/disposition/owner/version/denominator effect) and explicitly keep it OUTSIDE the main Table 4.1 and 10x5 dataset; it is an isolated process example, not an actual association request/decision. Add corresponding fact-level register row(s).
7) P3-04: add a concise separate synthetic paper-batch/receipt log, and integrate exactly one current invited code C04 as paper in Table 3.4. Use a synthetic receipt time before its existing Table 4.1 response time 2026-09-11 16:05:50; record paper batch, receipt/logging role, consent/notice version, preservation, and state this is still the existing C04 response, not an added invite/response. Keep all 12 invitation/11 unique/10 valid denominator counts unchanged. Add register row(s).
8) P3-05: in §5.2 item 5, expose the prior dataset v1 results: Q3 34/10=3.40, grand 201/50=4.02, learner Q3 21/6=3.50 exactly meeting the synthetic `<=3.50` threshold. Label as synthetic history; v2 remains Q3=3.30 and grand=4.00. Register these facts.
9) P3-06: quote the two official crosswalk neighbor titles VERBATIM and state the 0098-side locator that distinguishes this survey process instrument: Table 5.1 Q1-Q5 are system/process items; §5.5 item 2 excludes skill/capability outcome claims. Register the source mapping (not synthetic).

Return only valid JSON; no Markdown fences or commentary. Every new invented fact must have an individual or tightly atomic replacement row. Do not mark the work as PASS, accepted, real, or approved. If any requested repair cannot be done without changing the core sample arithmetic, set BLOCKED and explain in the JSON.

BASE MANUSCRIPT/REGISTER HASHES:
{
  "document_id": "0098",
  "requirement_id": "I18-E06",
  "manuscript_sha256": "4b8e5f6ab8e3b5c50c778009059933dd73c5dfc203b57e5453b3e0a9c481c68e",
  "register_sha256": "63bf6d73a3af1bdb58f3ff9fead60a653c576799fe203a1270c88231f88552bf",
  "official_page7_sha256": "2238fda775d4d72e281275a2df745f578e6b44b5eec9e99d8979e8da72f21db2",
  "unique_blueprint_sha256": "cba2e2d175907021f237992a346b750d33c41fb8a1810b6040c5f4c603be3d48",
  "crosswalk_sha256": "1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679"
}

OFFICIAL REQUIREMENT:
執行目標客戶及學員滿意度調查及分析（系統及流程面）。

NEGATIVE NEIGHBOR SOURCE TITLES (crosswalk verbatim):
0097 / I18-E05: 問卷調查等顯示目標客戶及學員認為訓練有達成能_分析報告
0099 / I18-E07: 提出目標客戶及學員對訓練達能力提升之說明（學_分析報告

REGISTER SCHEMA:
["fact_id", "document_id", "requirement_id", "field_or_locator", "value", "classification", "source_or_basis", "real_replacement_needed", "real_replacement_source", "owner_role", "verification_rule", "printed_page"]
REGISTER EXISTING FACT IDs:
FACT-0098-001, FACT-0098-002, FACT-0098-003, FACT-0098-004, FACT-0098-005, FACT-0098-006, FACT-0098-007, FACT-0098-008, FACT-0098-009, FACT-0098-010, FACT-0098-011, FACT-0098-012, FACT-0098-013, FACT-0098-014, FACT-0098-015, FACT-0098-016, FACT-0098-017, FACT-0098-018, FACT-0098-019, FACT-0098-020, FACT-0098-021, FACT-0098-022, FACT-0098-023, FACT-0098-024, FACT-0098-025, FACT-0098-026, FACT-0098-027, FACT-0098-028, FACT-0098-029, FACT-0098-030, FACT-0098-031, FACT-0098-032, FACT-0098-033, FACT-0098-034, FACT-0098-035, FACT-0098-036, FACT-0098-037, FACT-0098-038, FACT-0098-039, FACT-0098-040, FACT-0098-041, FACT-0098-042, FACT-0098-043, FACT-0098-044, FACT-0098-045, FACT-0098-046, FACT-0098-047, FACT-0098-048, FACT-0098-049, FACT-0098-050, FACT-0098-051, FACT-0098-052, FACT-0098-053, FACT-0098-054, FACT-0098-055, FACT-0098-056, FACT-0098-057, FACT-0098-058, FACT-0098-059, FACT-0098-060, FACT-0098-061, FACT-0098-062, FACT-0098-063, FACT-0098-064, FACT-0098-065, FACT-0098-066, FACT-0098-067, FACT-0098-068, FACT-0098-069, FACT-0098-070, FACT-0098-071, FACT-0098-072, FACT-0098-073, FACT-0098-086, FACT-0098-087, FACT-0098-088, FACT-0098-092, FACT-0098-093, FACT-0098-094, FACT-0098-095, FACT-0098-096, FACT-0098-097, FACT-0098-098, FACT-0098-099, FACT-0098-100, FACT-0098-101, FACT-0098-102, FACT-0098-103, FACT-0098-104, FACT-0098-105, FACT-0098-106, FACT-0098-107, FACT-0098-108, FACT-0098-109, FACT-0098-110, FACT-0098-111, FACT-0098-112, FACT-0098-113, FACT-0098-114, FACT-0098-115, FACT-0098-116, FACT-0098-117, FACT-0098-118
SELECTED EXISTING REGISTER ROWS:
[
  {
    "fact_id": "FACT-0098-003",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "Cover | document-control block | Cover | document-control block | revision field field",
    "value": "R02",
    "classification": "CONTROL/METADATA",
    "source_or_basis": "Candidate revision control",
    "real_replacement_needed": "NO",
    "real_replacement_source": "Candidate revision control",
    "owner_role": "—",
    "verification_rule": "Increment only when substantive candidate changes.",
    "printed_page": "P1"
  },
  {
    "fact_id": "FACT-0098-072",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§2.2 | learner-population bullet | L01–L08 range and count",
    "value": "8 synthetic learner codes L01-L08; not real attendance evidence",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic scenario setup in sections 2.1-2.2",
    "real_replacement_needed": "YES",
    "real_replacement_source": "Authorized class roster and attendance records, with personal data retained in its protected source",
    "owner_role": "調查執行角色",
    "verification_rule": "Reconcile eligible learners against the authorized roster and preserve only approved pseudonymous IDs in the analysis copy.",
    "printed_page": "P5"
  },
  {
    "fact_id": "FACT-0098-073",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§2.2 | target-client-population bullet | C01–C04 range and count",
    "value": "4 synthetic client codes C01-C04; not real client evidence",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic scenario setup in sections 2.1-2.2",
    "real_replacement_needed": "YES",
    "real_replacement_source": "Authorized client/referral frame and invitation basis, stored in the protected source",
    "owner_role": "調查執行角色",
    "verification_rule": "Verify the population definition and each invitation basis against authorized source records.",
    "printed_page": "P5"
  },
  {
    "fact_id": "FACT-0098-099",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§3.4 | Table 3.4 row L01 | channel, send-batch, roster-version, invitation-basis and consent cells",
    "value": "網頁表單連結（SYN）；SYN-SEND-01；SYN-LIST-v1；合成抽樣框內代碼；提交時勾選告知同意（合成）",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic invitation/consent log; no REAL communication or consent record is provided",
    "real_replacement_needed": "YES",
    "real_replacement_source": "正式發送日誌、實際抽樣名冊版本、問卷告知版本及個別同意紀錄",
    "owner_role": "調查執行角色（示範稱呼，非協會實有人員）",
    "verification_rule": "按對象代碼核對管道、批次、名冊版次、邀請資格及同意狀態；無回覆不得標為已同意。",
    "printed_page": "P8"
  },
  {
    "fact_id": "FACT-0098-110",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§3.4 | Table 3.4 row C04 | channel, send-batch, roster-version, invitation-basis and consent cells",
    "value": "網頁表單連結（SYN）；SYN-SEND-01；SYN-LIST-v1；合成抽樣框內代碼；提交時勾選告知同意（合成）",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic invitation/consent log; no REAL communication or consent record is provided",
    "real_replacement_needed": "YES",
    "real_replacement_source": "正式發送日誌、實際抽樣名冊版本、問卷告知版本及個別同意紀錄",
    "owner_role": "調查執行角色（示範稱呼，非協會實有人員）",
    "verification_rule": "按對象代碼核對管道、批次、名冊版次、邀請資格及同意狀態；無回覆不得標為已同意。",
    "printed_page": "P8"
  },
  {
    "fact_id": "FACT-0098-117",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§5.2 | calculation/display rule paragraph",
    "value": "Rates use decimal half-up to 1 decimal; means half-up to 2; zero denominator displays N/A",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic worked case or explicit calculation-control demonstration; not REAL association evidence",
    "real_replacement_needed": "YES",
    "real_replacement_source": "Check formula precision and N/A behavior when denominator equals zero",
    "owner_role": "依實際更正／調查程序正式指派；本稿未指派真人",
    "verification_rule": "以獲授權的原始來源、版本、計算與覆核紀錄驗證；來源缺失時維持 UNKNOWN。",
    "printed_page": "P15"
  },
  {
    "fact_id": "FACT-0098-118",
    "document_id": "0098",
    "requirement_id": "I18-E06",
    "field_or_locator": "§5.1 first paragraph; §4.4 version cells",
    "value": "SYN-DATA-v2 is the analysis set; v1 remains the preserved source version",
    "classification": "SAMPLE/SYNTHETIC",
    "source_or_basis": "Synthetic worked case or explicit calculation-control demonstration; not REAL association evidence",
    "real_replacement_needed": "YES",
    "real_replacement_source": "Confirm candidate matrix points to v2 and the correction trail preserves v1",
    "owner_role": "依實際更正／調查程序正式指派；本稿未指派真人",
    "verification_rule": "以獲授權的原始來源、版本、計算與覆核紀錄驗證；來源缺失時維持 UNKNOWN。",
    "printed_page": "P12, P14"
  }
]

SOURCE-BOUND CURRENT SECTIONS (exact R02 text):

### 1.3 負向鄰項之嚴格鑑別與拒絕
為維護佐證架構之獨立性，本文件在標題遮蔽或移除檔名之情況下，仍可由其專屬之「管道時序、樣本流向管制、重複表單隔離、10×5題項矩陣與資料交接紀錄」清楚辨認，並與相鄰指標嚴格區隔：
1. **拒絕混淆 0097 / I18-E05《問卷調查等顯示目標客戶及學員認為訓練有達成能力提升分析報告》**：
   - 0097 號文件聚焦於「受訓學員與目標客戶是否主觀認定訓練達成能力提升」之成效衡量（屬於訓練成效層級之能力認知）。
   - 本件（0098）僅記錄「滿意度調查之系統發送、收件流向、有效性檢驗與題項滿意度之流程面數據」，不評估亦不宣稱學員能力之實質增長。
2. **拒絕混淆 0099 / I18-E07《提出目標客戶及學員對訓練達能力提升之說明》**：
   - 官方列示的 0099 / I18-E07 為「提出目標客戶及學員對訓練達能力提升之說明（學習技能面）」。本文件只記錄滿意度調查的執行與系統／流程分析，不推定 0099 必須採用特定訪談方法。
   - 本件（0098）嚴守問卷調查之執行系統與行政統計流程，不涉及學員課後行為轉變或組織績效歸因之質性論述。

---

### 2.1 調查母體與接觸範圍
本示範案例之計畫母體設定為「2026年第三季志願服務與行政技能精進訓練班」。母體涵蓋全體結訓之在冊學員，以及指派或接受服務之目標客戶（包括合作機構業務聯絡窗口、服務對象代表或志工督導代表）。

---

### 3.1 執行階段與操作控制點
以下列出可直接採用的執行順序、責任角色、控制點與輸出。角色名稱是流程示範用稱呼，不代表協會現有職稱或組織編制：

| 執行階段 | 責任角色 | 具體操作內容 | 關鍵控制點（Checkpoints） | 階段產出產物 |
| :--- | :--- | :--- | :--- | :--- |
| **階段一：名冊建置** | 滿意度調查執行員 | 匯入學員與客戶代表名單，產生去識別代碼 L01–L08 及 C01–C04。 | 確認無重複對象、確認聯絡電子管道有效性。 | 受邀名冊與發送清單 |
| **階段二：正式發送** | 滿意度調查執行員 | 依正式授權管道發送問卷與填答告知；逐代碼記錄管道、發送批次、名冊版次、邀請依據及同意狀態，連結表3.4與原始發送日誌。 | 核對寄送結果與受邀框；無回覆者不得記為已同意；保存告知版本與退信／失敗狀態。 | 逐筆邀請／同意日誌及發送日誌 |
| **階段三：進度催收** | 滿意度調查執行員 | 於發送後指定間隔比對未填名單，執行一次性溫馨提醒通知。 | 排除已回覆者，避免對同一對象過度打擾。 | 提醒通知寄送紀錄 |
| **階段四：收件截件** | 滿意度調查執行員 | 到達設定截止時間時停止本期收件；若調查平台支援即關閉提交，否則記錄人工截件時間，逾期回覆另行標記。隨後匯出原始作答資料。 | 將原始匯出檔另存唯讀副本，或採經核定的保全方式，記錄檔名、時間、版本及 SHA-256（若可取得）。 | 原始回覆資料庫（Raw CSV） |
| **階段五：數據清洗** | 教學行政覆核員 | 逐筆核對重複作答、缺漏作答，劃分有效與排除樣本。 | 執行 L02 重複隔離、標註 L07 不完整排除。 | 樣本流向判定總表 |
| **階段六：交接分析** | 教學行政覆核員 | 計算指標、產出統計矩陣、記錄異常，交接教學課務組。 | 依正式授權程序完成交接確認，記錄資料清單、版本、接收時間及存取權限；若未指派覆核責任，先填 `UNKNOWN`。 | 調查交接紀錄表 |

---

### 3.4 合成逐筆邀請來源、名冊版次與同意狀態對照表
本表是合成日誌欄位的完整填寫示例，不是實際聯絡紀錄。所有代碼、批次、名冊版次、管道及勾選狀態均為 SAMPLE/SYNTHETIC；實際資料應以獲授權的發送日誌與告知版本替換。回覆事件以表4.1的同代碼列追溯。

| 對象代碼 | 來源管道 | 發送批次 | 名冊版次 | 邀請依據 | 個別同意狀態 | 回覆流向索引 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| L01 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 L01 |
| L02 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 兩次提交均示範勾選告知同意 | 表4.1 L02；重複件見§4.2 |
| L03 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 L03；更正見§4.4 |
| L04 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 L04 |
| L05 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 L05 |
| L06 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 L06 |
| L07 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意；Q3缺答 | 表4.1 L07；排除見§4.3 |
| L08 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 截止前未回覆；無個別同意紀錄 | 表4.1 L08 |
| C01 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 C01 |
| C02 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 C02 |
| C03 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 C03 |
| C04 | 網頁表單連結（合成） | SYN-SEND-01 | SYN-LIST-v1 | 合成抽樣框內代碼 | 提交時勾選告知同意（合成） | 表4.1 C04 |

---

---

### 4.3 缺失、偏差與待更正資料
1. **L07 缺答**：合成紀錄設定 L07 缺填 Q3，其餘題目不代填；依完整作答規則列為不完整排除，不進入五題分數計算。
2. **L08 未回覆**：合成紀錄設定 L08 截至 2026-09-12 17:00 未回覆，為 1/12（8.3%）。沒有可比較背景資料，無法判斷未回覆者是否與回覆者不同，不推斷其滿意度。
3. **更正與爭議**：不得覆寫原始回覆。任何更正必須連結申請來源、範圍、前後版本、覆核角色及分母影響；本稿的完整合成演練見§4.4。

---

### 5.2 調查流向指標逐步計算
本示範期間為 2026-09-05 09:30 至 2026-09-12 17:00（Asia/Taipei；合成時間），更正事件發生於其後，只改變分析資料版本，不新增或刪除回覆。
1. **接觸邀請數（N_invite）**：12 人（學員8人、目標客戶4人）。
2. **原始表單提交數（N_sub）**：12 筆（含 L02 的兩筆提交）。
3. **重複提交隔離數（N_dup）**：1 筆；唯一回覆數 N_resp = N_sub − N_dup = 12 − 1 = 11。
4. **有效完整回覆數（N_valid）**：10 份；不完整排除數1份（L07），未回覆數1人（L08）。
5. **合成更正版本**：SYN-DATA-v1 的 Q3 總分34、全題總分201；SYN-DATA-v2 依§4.4更正 L03 的 Q3 後，Q3總分33、全題總分200。邀請12、唯一回覆11、有效表單10、有效題項50均不變。
6. **核心比率**：
   - 回覆率 = 唯一回覆數 / 接觸邀請數 = 11 / 12 = 91.6667% → **91.7%**。
   - 回覆中有效率 = 有效完整回覆數 / 唯一回覆數 = 10 / 11 = 90.9091% → **90.9%**。
   - 邀請到有效產出率 = 有效完整回覆數 / 接觸邀請數 = 10 / 12 = 83.3333% → **83.3%**。
   - 未回覆比例 = 未回覆數 / 接觸邀請數 = 1 / 12 = 8.3333% → **8.3%**。

**計算與顯示規則**：百分比先以未四捨五入的原始分數計算，再採十進位四捨五入（half-up）顯示至小數第1位；量表均值同樣先用未四捨五入值計算，顯示至小數第2位。結果須同列分子、分母、單位與本例期間。若任何計算的分母為0，顯示 `N/A（分母為0，無法計算）`，不得顯示為0%或0分；該項不併入整體平均，並說明缺少的母數。

---

### 7.3 流程異常升級途徑
1. **回覆率偏低**：在截止前發現回覆情況低於協會已核定的提醒目標時，記錄目前分子、分母與剩餘時間，通知正式指定的主管角色並記錄處置。若沒有已核定目標，標記 `UNKNOWN`，不得自行宣稱門檻已觸發。
2. **資料安全或外洩疑慮**：先限制受影響資料的存取，保留必要日誌，依協會正式通報程序交由獲授權角色處理；不要在分析表複製個人敏感資料。
3. **撤回、更正或爭議**：依正式授權流程記錄申請來源、範圍、處置依據、覆核者及資料集版本；執行者不得自行覆寫原始紀錄。

---

### 8.1 真實數據替換核對清單（Real Replacement Register Checklist）
為使未來機構正式實施時，能順利將本件示範稿升格為真實業務紀錄（REAL），特訂定逐項替換指引：

| 示範項目（SAMPLE/SYNTHETIC） | 本示範文件數值或內容 | 升格為 REAL 所需之真實佐證原件與資料來源 | 查核與覆核驗證規則 | 替換權責角色 |
| :--- | :--- | :--- | :--- | :--- |
| **專案案號與期別** | `SYN-I18E06-2026-01` | 協會正式核定之年度訓練計畫公文或開班通知書。 | 核對班期代碼與年度預算書、簽呈一致。 | 課務承辦人 |
| **調查時程** | 2026-09-05 至 09-12 | 真實發送郵件日誌、線上調查系統後台時間戳記原始檔。 | 發送、催收與截止日期符合正式開班結訓時程。 | 資訊管理員 |
| **參與對象代碼與名冊** | L01–L08, C01–C04（共12人） | 真實參訓學員簽到退紀錄表、受訓合作機構指派函件。 | 查核參訓名單符合開班資格，抽樣框母體具真實性。 | 行政志工 |
| **原始問卷作答數據** | SYN-DATA-v2 10×5 矩陣（總分200；v1原列保留） | 線上調查後台未經編輯之匯出 CSV 檔，或實體紙本簽收問卷原件。 | 逐筆比對原始匯出檔與分析表，數值百分之百吻合。 | 教學行政覆核員 |
| **重複表單隔離** | L02 第2筆重複隔離紀錄 | 原始問卷資料庫匯出檔中標註有重複時間戳記之原始列。 | 確認隔離之重複筆數與系統日誌完全相符，未滲入分析。 | 系統管理員 |
| **缺漏排除表單** | L07 缺答 Q3 排除 | 原始作答檔案中出現缺漏之真實表單紀錄。 | 查驗判定為無效問卷之理由符合公告之清洗準則。 | 教學行政覆核員 |
| **管道與同意紀錄** | 表3.4逐碼示範管道、批次、名冊版次與同意狀態 | 授權發送日誌、名冊版本、問卷告知與同意欄位 | 逐碼覆核；無回覆者不得記為已同意 | 調查執行角色 |
| **資料更正與版本** | SYN-CORR-01；D_v1→D_v2；Q3 34→33 | 正式更正申請、處理依據、原始及更正版本、授權覆核 | 保留原始檔，逐欄重算並核對分母不變 | 資料覆核角色 |
| **統計比率與均值** | SYN-DATA-v2：回覆率91.7%、Q3均值3.30、總題項均值4.00 | 依真實有效數據重新以公式計算之報表。 | 重新驗算分子、分母，確認無手動算術偏差。 | 統計主辦人 |
| **改善提案與決議** | `SYN-PROP-2026-01`（未核准） | 理事會會議紀錄、訓練委員會審查決議或主管簽核簽呈。 | 必須具備協會首長或法定主管之正式簽名、決議字號。 | 秘書處主管 |
| **作業簽章與覆核** | 虛擬作業角色標記 | 協會正式在職員工或正式任命志工幹部之親筆簽章或電子憑證。 | 驗證簽章人具備章程所授權之職責權限。 | 專案經理 |