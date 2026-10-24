Patch text only. No file is changed; this is not formal acceptance.

## A. `PATCH_DECISIONS`

| Finding | Disposition | Changed locations |
|---|---|---|
| 1 | Rebuild §12.1 as one row per `case_id`; remove case-as-column orientation; add operational fields. | §12.1, B below |
| 2 | Full §12.2 locator audit; remove ordinal/table-number locators; fix Form E and Form D #12; remove duplicates; alias 036. | §12.2, D below |
| 3 | Define CASE-01 as SAMPLE workflow with simulated limited consent and request pending; real outbound `NOT_SENT`; real contact blocked. Keep CASE-02 as absent-consent/identity-comparison HOLD. | §§4.2, 9.3–9.4, 10.1–10.3, 12.1 |
| 4 | Set both `course_source` values to exactly `UNKNOWN`; move explanation to `notes`. | §§4.2, 12.1, 12.2 |
| 5 | Replace CASE-01 “身分對不上” with `UNKNOWN／目前無法對照`; reserve mismatch for verified comparison. | §7.3 summary; §10.3; §14.1 |
| 6 | Record CASE-02 review on `2026-10-20`; set next SAMPLE-only review `2026-10-30` with reason. | §§4.2, 9.4, 10.2, 12.1 |
| 7 | Replace Form F ten-check form with five-gate form mirroring the gate, not an extra gate. | §§4, 9.1–9.2, 9.3–9.4, 11.1, 14.1, 15.5 |
| 8 | Add valid consent and contact/disclosure authority to CASE-01 missing-items and HOLD reason. | §§9.3, 10.1, 12.1 |
| 9 | Remove `F-0102-036` from fact rows; add alias note `DUPLICATE_OF=F-0102-016`. | §12.2, D below |
| 10 | Qualify the no-fabrication statement: no real sending/reply/signature/approval/award proof; synthetic learner narrative is marked simulation. | §10 boundary; §§10.1–10.2 |

## B. `SECTION_12_1_REPLACEMENT`

**表 12.1｜案例登錄表（一案一行；SAMPLE／SYNTHETIC）**

| case_id | learner_ref／claim | course | competition／result | evidence_state／case_status | consent_status（real world） | SAMPLE workflow／request | authority | source_locator | verification／training_link | decision | owner／internal_review_date | external_due_date | synthetic_fact_ids | real_source_required／notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SYN-0102-CASE-01` | `P-SYN-01`；`2026-10-05`；電話＋訊息 | `SYN-COURSE-01`；`2026-03-02～2026-04-10`；36 小時；`course_source=UNKNOWN` | 示範盃技能競賽（合成名稱）；`2026-08-22`；（合成）示範技能發展協會；照顧服務類／個人組；佳作；學員自述＋一張無網址截圖 | `RECEIVED_UNVERIFIED`；`HOLD` | `UNKNOWN`（無有效同意；無簽署） | `SAMPLE_WORKFLOW_CONSENT=SYNTHETIC_SIMULATED_LIMITED_CONSENT`（僅流程模擬，非真實同意／非簽署）；`REQUEST_STATE=PENDING_REAL_SOURCE`；`OUTBOUND_REQUEST=NOT_SENT`；`REAL_CONTACT=BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY` | 模擬限縮範圍：內部查核＋向主辦查證，不含公開；`CONTACT_AUTHORITY=UNKNOWN`；`DISCLOSURE_AUTHORITY=UNKNOWN` | `NONE／UNLOCATED`（無官方網址、無第三方原件；未實際搜尋） | `NOT_STARTED／UNKNOWN`；`NOT_ESTABLISHED` | `HOLD`（來源＋有效同意／聯繫及揭露授權） | 行政志工 A（合成角色 A；非現任人員）；`2026-10-26` SAMPLE only；非外部期限；檢查模擬限縮同意是否可轉為真實同意／授權 | `NOT_SET／NOT_SENT` | `F-0102-003–011；F-0102-019–024；F-0102-031；F-0102-035；F-0102-038；F-0102-040；F-0102-042；F-0102-045` | 有效同意與聯繫／揭露授權；受限身分對照；官方競賽規則及結果頁或獨立主辦確認；課程計畫、課綱、出席與評量原件。SAMPLE／SYNTHETIC；無真實課程計畫、名冊或評量；課程來源 `UNKNOWN`，未核實；實際對外請求 `NOT_SENT`。 |
| `SYN-0102-CASE-02` | `P-SYN-02`；`2026-09-30`；他人轉貼截圖 | `SYN-COURSE-02`；`2026-01-05～2026-02-15`；時數 `NOT FOUND IN INPUT`；`course_source=UNKNOWN` | 示範盃技能競賽（合成名稱）；`2026-08-22`；（合成）示範技能發展協會；照顧服務類／團體組；冠軍；他人轉貼截圖，無原始連結 | `RECEIVED_UNVERIFIED`；`HOLD` | `UNKNOWN`（無有效同意；無簽署／明確授權） | `SAMPLE_WORKFLOW_CONSENT=NO_SIMULATED_CONSENT`；`REQUEST_STATE=NOT_READY_FOR_REQUEST`（同意缺席）；`OUTBOUND_REQUEST=NOT_SENT`；`REAL_CONTACT=BLOCKED_CONSENT_ABSENT` | 未取得；`CONTACT_AUTHORITY=UNKNOWN`；`DISCLOSURE_AUTHORITY=UNKNOWN` | `NONE／UNLOCATED`（僅合成轉貼截圖；無原始連結、無官方公告） | `NOT_STARTED／UNKNOWN`；`NOT_ESTABLISHED` | `HOLD`（有效同意缺席＋身分／隊名無從對照；非 `REJECTED`） | 行政志工 B（合成角色 B；非現任人員）；`2026-10-30` SAMPLE only；`2026-10-20` SAMPLE 覆核已完成；非外部期限；原因：同意及身分／隊名對照缺件未補，維持 HOLD | `NOT_SET／NOT_SENT` | `F-0102-012–017；F-0102-025–030；F-0102-032；F-0102-041；F-0102-043–044；F-0102-046` | 有效同意與聯繫／揭露授權；受限身分及正式隊名／隊員對照；官方競賽規則及結果頁或獨立主辦確認；課程計畫、課綱、出席與評量原件。SAMPLE／SYNTHETIC；無真實課程計畫、名冊或評量；課程來源 `UNKNOWN`，未核實；不得寫成身分不符或造假。 |

**欄位定義／註記**

- 一列一 `case_id`；不得以案例為欄。`CASE-01`／`CASE-02` 只在 `case_id` 出現，不重複貼標籤。
- `consent_status` 只記真實世界狀態；`SYNTHETIC_SIMULATED_LIMITED_CONSENT` 是工作流模擬，永不構成真實同意、簽署或授權。
- `PENDING_REAL_SOURCE` 只表示 SAMPLE 草稿已備、等待真實來源；不代表已寄出、已聯繫或已回覆。`NOT_SENT` 表示無實際寄送、傳訊、電話或表單提交。
- `source_locator` 一律用「章節＋指名表單／欄位／案例」，不得使用表號、列號或 `row` 序號。
- `CASE-01 Form E` 為 §8.3 單一已填矩陣；`CASE-02 Form E` 為 §8.4 單一已填矩陣。CASE-02 重複查核為 §7.3 Form D `#12`。
- `internal_review_date` 為 SAMPLE 內控日，不是外部期限；`external_due_date` 僅在實際寄出且取得期限後設定。
- `F-0102-036` 不列入事實欄；見 D 的別名註記。
- `0/2=0%` 不變：兩個合成主張、零件已驗證得獎。

## C. `FORM_F_REPLACEMENT`

**表 9.1｜Form F 案例決定表（五項核心條件；與 Form D 同一門檻；SAMPLE／SYNTHETIC 候選）**

| Gate | 核心條件 | 允許狀態 | 對應紀錄 |
|---|---|---|---|
| 1 | `official_source_award_confirmation`：官方來源或主辦確認競賽與獎項 | `YES／NO／UNKNOWN` | Form D `#1–#8、#10` |
| 2 | `identity_match`：得獎者／隊名可與學員受限身分對照 | `YES／NO／UNKNOWN` | Form D `#9`；§13.2 |
| 3 | `training_linkage`：課程目標→教授／練習→評量→競賽技能，且時間序與限制可追溯 | `YES／NO／UNKNOWN` | Form E（§8.3／§8.4） |
| 4 | `valid_consent_disclosure_authority`：有效同意及聯繫／揭露權限 | `YES／NO／UNKNOWN` | Form A；Form D `#13` |
| 5 | `locator_preservation`：來源可定位、原件可保存／回查 | `YES／NO／UNKNOWN` | Form D `#11、#14、#15` |

**判定後果**

| 狀態組合 | 判定 |
|---|---|
| 五項全部 `YES` | `ELIGIBLE_FOR_HUMAN_REVIEW`；可進入真實來源審查，完成真實來源審查後才可記 `VERIFIED_REAL`。不是自動核准或評分。 |
| 任一 `UNKNOWN` | `HOLD`；不得 `VERIFIED_REAL`；記缺件、責任角色、下次檢視日。 |
| 任一可補正 `NO`（來源未收到、無對照基礎、訓練紀錄缺、同意／授權待補、定位未完成） | `HOLD`；指定補正動作。 |
| 已確認偽造、官方否認獎項、經比對確定非本人、可靠證據證實變造 | `REJECTED`（僅該證據項）；保留原檔、理由及覆核角色。 |
| 未授權揭露或揭露權限不明 | 立即 `STOP_DISCLOSURE`；案件 `HOLD`；已揭露者啟動事件處理。 |
| 五項全部 `YES` 但尚未完成真實來源審查 | `HOLD`；不得提前記 `VERIFIED_REAL`。 |

`NO` 僅表示該條件在此次檢視未成立，不單獨證明造假。`Form F` 與 `Form D` 是同一門檻的不同記錄面，不是第二組十項門檻。

**已填 SAMPLE**

| 欄位 | `SYN-0102-CASE-01` | `SYN-0102-CASE-02` |
|---|---|---|
| `record_type` | `SAMPLE／SYNTHETIC` | `SAMPLE／SYNTHETIC` |
| `review_date` | `2026-10-23`（SAMPLE 文件覆核日） | `2026-10-20`（SAMPLE 覆核已完成） |
| `reviewer_role` | 覆核角色（SAMPLE；姓名 `NOT FOUND IN INPUT`；未指派真人） | 覆核角色（SAMPLE；姓名 `NOT FOUND IN INPUT`；未指派真人） |
| `owner_role` | 行政志工 A（合成角色 A；非現任人員） | 行政志工 B（合成角色 B；非現任人員） |
| Gate 1 | `UNKNOWN`；無官方來源或主辦確認，只有合成無網址截圖；SAMPLE 請求待源，`OUTBOUND_REQUEST=NOT_SENT`。定位：§7.3 CASE-01 Form D `#1–#10`；§12.1 `source_locator` | `UNKNOWN`；只有合成轉貼截圖，無官方來源或主辦確認。定位：§7.3 CASE-02 Form D `#1–#10`；§12.1 `source_locator` |
| Gate 2 | `UNKNOWN／目前無法對照`；無官方名單或可比對姓名／隊名，非已確認不符。定位：§7.3 CASE-01 Form D `#9` | `UNKNOWN／無對照基礎`；僅「示範隊」暱稱，無官方名單或隊員資料，非已確認不符。定位：§7.3 CASE-02 Form D `#9`；§10.2 處理經過第 1–2 點 |
| Gate 3 | `UNKNOWN`；`NOT_ESTABLISHED`；僅 SAMPLE 課程情境，`course_source=UNKNOWN`。定位：§8.3 CASE-01 Form E | `UNKNOWN`；`NOT_ESTABLISHED`；僅 SAMPLE 課程情境，`course_source=UNKNOWN`。定位：§8.4 CASE-02 Form E |
| Gate 4 | `NO`；無有效真實同意、無聯繫／揭露授權；模擬限縮同意僅工作流，不是簽署或真實同意。定位：§4.2 `consent_status`／`consent_date`；§12.1 | `NO`；無同意；無模擬同意；聯繫／揭露授權 `UNKNOWN`。定位：§4.2 `consent_status`／`consent_date`；§12.1 |
| Gate 5 | `NO`；無官方定位、無第三方原件；保存與回查未完成。定位：§7.3 CASE-01 Form D `#11、#14、#15` | `NO`；無原始連結、無第三方原件；保存與回查未完成。定位：§7.3 CASE-02 Form D `#11、#14、#15` |
| `overall_decision` | `HOLD`（來源＋有效同意／聯繫及揭露授權） | `HOLD`（有效同意缺席＋身分／隊名無從對照） |
| `evidence_state` | `RECEIVED_UNVERIFIED` | `RECEIVED_UNVERIFIED` |
| `evidence_used_and_locator` | SAMPLE 無網址截圖情節；無第三方原件、官方連結或可核定位 | SAMPLE 轉貼截圖情節；無原始網址、官方公告或第三方原件 |
| `missing_items` | 有效同意與對外聯繫／揭露授權；官方結果頁或主辦確認；獎狀影本；得獎者身分對照；競賽規則；真實課程／評量紀錄；可定位保存 | 有效同意與聯繫／揭露授權；官方結果頁或主辦確認；獎狀；正式隊名／隊員對照；競賽規則；真實課程／評量紀錄；可定位保存 |
| `next_action` | `OUTBOUND_REQUEST=NOT_SENT`；`REAL_CONTACT=BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY`；`2026-10-26` 檢視模擬限縮同意是否可轉為真實同意／授權 | 維持 HOLD；以 Form B 重新說明同意範圍；未取得同意／授權前不對外查證；`2026-10-30` 下次 SAMPLE 覆核 |
| `next_review_date` | `2026-10-26`（SAMPLE only；非外部期限） | `2026-10-30`（SAMPLE only；`2026-10-20` 覆核後所設；非外部期限；原因：同意及身分／隊名缺件未補） |
| `formal_approval` | `NOT_GRANTED` | `NOT_GRANTED` |

**§9.2 判定門檻替換文字**

可送人類複核的唯一判定規則：Form F 五項核心條件（官方來源／獎項確認、身分對照、訓練關聯、有效同意／揭露權限、來源定位與保存）全部為「是」，且 Form D 的對應必要查核完成；全部「是」只表示可進入真實來源審查，完成真實來源審查後才可記 `VERIFIED_REAL`。任一「未知」或可補正之「否」→ `HOLD`；已確認偽造／矛盾 → `REJECTED`（僅該證據項）；未授權揭露 → `STOP_DISCLOSURE`。Form F 與 Form D 是同一門檻的不同記錄面，不是第二組十項門檻；不一致先 `HOLD` 更正。

## D. `SECTION_12_2_FULL_LOCATOR_AUDIT`

Locator convention: section + named case/form/field/item only. No table numbers, row numbers, or ordinals.

| fact_id | Current fact identity | Exact corrected locator | Case／value context |
|---|---|---|---|
| `F-0102-001` | Cover global no-claim disclaimer | 封面「資料狀態」及「SAMPLE／SYNTHETIC」聲明 | GLOBAL; `real_awards=UNKNOWN`; `formal_acceptance=NOT_GRANTED` |
| `F-0102-002` | Authorization phrase unknown | §2.3「授權狀態怎麼寫」 | GLOBAL; 待依章程及授權名冊確認 |
| `F-0102-003` | CASE-01 learner alias | §4.2 CASE-01 `learner_ref`；§12.1 CASE-01 `learner_ref` | CASE-01; `P-SYN-01` |
| `F-0102-004` | CASE-01 course ID | §4.2 CASE-01 `course_id`；§10.1 基本資料課程；§12.1 CASE-01 `course_id` | CASE-01; `SYN-COURSE-01` |
| `F-0102-005` | CASE-01 competition name | §4.2 CASE-01 `competition_name`；§10.1 基本資料競賽；§12.1 CASE-01 `competition` | CASE-01; 示範盃技能競賽（合成） |
| `F-0102-006` | CASE-01 organizer | §4.2 CASE-01 `organizer`；§10.1 基本資料主辦 | CASE-01; （合成）示範技能發展協會 |
| `F-0102-007` | CASE-01 competition date | §4.2 CASE-01 `competition_date`；§10.1 基本資料競賽日期 | CASE-01; `2026-08-22` |
| `F-0102-008` | CASE-01 claimed result | §4.2 CASE-01 `claimed_result`；§8.3 CASE-01 Form E「競賽技能與主張結果」；§10.1 基本資料主張獎項；§12.1 CASE-01 `claimed_result` | CASE-01; 佳作（SAMPLE，未核實） |
| `F-0102-009` | CASE-01 organizer locator not searched | §6.4 查證紀錄表 CASE-01「管道來源」「網址或頁面名稱」；§12.1 CASE-01 `source_locator` | CASE-01; 尚未搜尋、未定位 |
| `F-0102-010` | CASE-01 skill score | §8.3 CASE-01 Form E「評量紀錄」 | CASE-01; `78/100`（SAMPLE） |
| `F-0102-011` | CASE-01 instructor observation | §8.3 CASE-01 Form E「評量紀錄」「其他佐證」 | CASE-01; 流程完整（SAMPLE） |
| `F-0102-012` | CASE-02 learner alias | §4.2 CASE-02 `learner_ref`；§10.2 基本資料；§12.1 CASE-02 `learner_ref` | CASE-02; `P-SYN-02` |
| `F-0102-013` | CASE-02 course ID | §4.2 CASE-02 `course_id`；§10.2 基本資料；§12.1 CASE-02 `course_id` | CASE-02; `SYN-COURSE-02` |
| `F-0102-014` | CASE-02 claimed result | §4.2 CASE-02 `claimed_result`；§8.4 CASE-02 Form E「競賽技能與主張結果」；§10.2 基本資料；§12.1 CASE-02 `claimed_result` | CASE-02; 冠軍（SAMPLE，未核實） |
| `F-0102-015` | CASE-02 team-name clue | §10.2 處理經過第 1–2 點；§12.1 CASE-02 `notes` | CASE-02; 「示範隊」 |
| `F-0102-016` | CASE-02 duplicate/repost concern | §7.3 CASE-02 Form D `#12`；§10.2 處理經過第 4 點；§12.1 CASE-02 `notes` | CASE-02; 截圖與另一貼文相似 |
| `F-0102-017` | CASE-02 attendance | §8.4 CASE-02 Form E「評量紀錄」 | CASE-02; `14/18`（SAMPLE） |
| `F-0102-018` | Retention period unresolved | §13.6「保存期限」 | GLOBAL; 待依法規、同意及政策確認 |
| `F-0102-019` | CASE-01 claim date/channel | §4.2 CASE-01 `claim_date`、`claim_channel`；§10.1 處理經過第 1 點 | CASE-01; `2026-10-05`；電話＋訊息 |
| `F-0102-020` | CASE-01 course dates/hours | §4.2 CASE-01 `course_dates`；§10.1 基本資料課程期間；§8.3 CASE-01 Form E「時間序」 | CASE-01; `2026-03-02～2026-04-10`；36 小時 |
| `F-0102-021` | CASE-01 category | §4.2 CASE-01 `category`；§10.1 基本資料組別；§8.3 CASE-01 Form E「競賽技能與主張結果」 | CASE-01; 個人組 |
| `F-0102-022` | CASE-01 consent missing | §4.2 CASE-01 `consent_status`、`consent_scope`；§9.3 CASE-01 Form F Gate 4；§10.1 基本資料同意；§12.1 CASE-01 `consent_status` | CASE-01; `UNKNOWN`；無簽署或明確同意 |
| `F-0102-023` | CASE-01 internal review date | §4.2 CASE-01 `internal_review_date`；§10.1 處理經過第 5–6 點；§12.1 CASE-01 `internal_review_date` | CASE-01; `2026-10-26` SAMPLE only；no duplicate label |
| `F-0102-024` | CASE-01 owner role | §4.2 CASE-01 `owner_role`；§10.1 基本資料；§12.1 CASE-01 `owner_role` | CASE-01; 合成角色 A |
| `F-0102-025` | CASE-02 claim date/source | §4.2 CASE-02 `claim_date`；§10.2 處理經過第 1 點 | CASE-02; `2026-09-30`；他人轉貼 |
| `F-0102-026` | CASE-02 course dates | §4.2 CASE-02 `course_dates`；§10.2 基本資料；§8.4 CASE-02 Form E「時間序」 | CASE-02; `2026-01-05～2026-02-15` |
| `F-0102-027` | CASE-02 category | §4.2 CASE-02 `category`；§10.2 基本資料；§8.4 CASE-02 Form E「競賽技能與主張結果」 | CASE-02; 團體組 |
| `F-0102-028` | CASE-02 consent missing | §4.2 CASE-02 `consent_status`、`consent_scope`；§9.4 CASE-02 Form F Gate 4；§10.2 處理經過第 3 點；§12.1 CASE-02 `consent_status` | CASE-02; `UNKNOWN`；含糊措辭非同意 |
| `F-0102-029` | CASE-02 internal review date | §4.2 CASE-02 `internal_review_date`；§9.4 CASE-02 Form F `next_review_date`；§10.2 處理經過第 6 點；§12.1 CASE-02 `internal_review_date` | R33 `2026-10-20`；R34 next SAMPLE-only `2026-10-30`；no duplicate label |
| `F-0102-030` | CASE-02 owner role | §4.2 CASE-02 `owner_role`；§10.2 基本資料；§12.1 CASE-02 `owner_role` | CASE-02; 合成角色 B |
| `F-0102-031` | CASE-01 instructor speed observation | §8.3 CASE-01 Form E「評量紀錄」「其他佐證」 | CASE-01; 速度待加強（SAMPLE） |
| `F-0102-032` | CASE-02 no formal score | §8.4 CASE-02 Form E「評量紀錄」 | CASE-02; 無正式評量分數（SAMPLE） |
| `F-0102-033` | Pending synthetic claims count | §11.2「本示範資料集」`合成待審主張`；§11.4「主張收件率」 | GLOBAL; 2 件 |
| `F-0102-034` | Suggested roles only | §2.1「最低限度的人員配置」；§4.1 `owner_role`；§13.1 受限區／審閱區 | GLOBAL; 流程設計 |
| `F-0102-035` | CASE-01 skill description | §8.3 CASE-01 Form E「競賽技能與主張結果」 | CASE-01; 個人組技能描述 |
| `F-0102-037` | All unsent request templates | §5.1 書面索取稿；§5.2 CASE-01 SAMPLE 摘要；§6.2 書面查證稿；§6.3 電話腳本；§6.4 查證紀錄表 | GLOBAL; `SAMPLE TEMPLATE—NOT SENT` |
| `F-0102-038` | CASE-01 evidence state | §4.2 CASE-01 `evidence_state`；§9.3 CASE-01 Form F `evidence_state`；§12.1 CASE-01 `evidence_state` | CASE-01; `RECEIVED_UNVERIFIED` |
| `F-0102-039` | Verified award count | §11.2「已驗證得獎案例」；§11.4「已驗證率」 | GLOBAL; `0` |
| `F-0102-040` | CASE-01 course source | §4.2 CASE-01 `course_source`；§10.1 基本資料課程；§12.1 CASE-01 `course_source` | R34 value `UNKNOWN`; explanation in `notes` |
| `F-0102-041` | CASE-02 course source | §4.2 CASE-02 `course_source`；§10.2 基本資料；§12.1 CASE-02 `course_source` | R34 value `UNKNOWN`; explanation in `notes` |
| `F-0102-042` | CASE-01 consent date | §4.2 CASE-01 `consent_date`；§9.3 CASE-01 Form F Gate 4；§12.1 CASE-01 | CASE-01; `UNKNOWN` |
| `F-0102-043` | CASE-02 consent date | §4.2 CASE-02 `consent_date`；§9.4 CASE-02 Form F Gate 4；§12.1 CASE-02 | CASE-02; `UNKNOWN` |
| `F-0102-044` | CASE-02 evidence state | §4.2 CASE-02 `evidence_state`；§9.4 CASE-02 Form F `evidence_state`；§12.1 CASE-02 | CASE-02; `RECEIVED_UNVERIFIED` |
| `F-0102-045` | CASE-01 decision | §9.3 CASE-01 Form F `overall_decision`；§10.1「目前判定」；§12.1 CASE-01 `decision` | CASE-01; `HOLD` |
| `F-0102-046` | CASE-02 decision | §9.4 CASE-02 Form F `overall_decision`；§10.2「目前判定」；§12.1 CASE-02 `decision` | CASE-02; `HOLD` |
| `F-0102-047` | Verified rate | §11.2「已驗證率」；§11.4「已驗證率」；§15.5 | GLOBAL; `0/2=0%` |
| `F-0102-048` | Valid consent rate | §11.4「同意檢核率」；§11.2「揭露權限具備」 | GLOBAL; `0/2=0%` |
| `F-0102-049` | Independent channel located rate | §11.4「查證管道定位率」 | GLOBAL; `0/2=0%` |
| `F-0102-050` | Source acquisition and verification rates | §11.4「第三方來源取得率」「已驗證率」 | GLOBAL; `0/2=0%` each; do not interchange |
| `F-0102-051` | Identity match count | §11.2「身分一致」 | GLOBAL; `0/2` |
| `F-0102-052` | Award confirmed count | §11.2「獎項確定」 | GLOBAL; `0/2` |
| `F-0102-053` | Training-link complete count | §11.2「可核實訓練關聯」 | GLOBAL; `0/2` |
| `F-0102-054` | Disclosure authority count | §11.2「揭露權限具備」 | GLOBAL; `0/2` |
| `F-0102-055` | Third-party original count | §11.2「已收第三方原件」 | GLOBAL; `0` |
| `F-0102-056` | Claim intake rate | §11.4「主張收件率」 | GLOBAL; `2/2=100%` |

**Duplicate alias outside the fact rows**

`F-0102-036` → `DUPLICATE_OF=F-0102-016` → `RETIRED`。不列入一事實一列、不計數；與 `F-0102-016` 共用來源替換要求與查核紀錄；不得重複索取、重複計數，亦不得將此標記放入訓練關聯欄。穩定定位：§7.3 CASE-02 Form D `#12`；§10.2 處理經過第 4 點；§12.1 CASE-02 `notes`。

## E. `EXACT_TEXT_REPLACEMENTS`

**§4**

- `7. 開 Form F 作判定摘要：五項核心條件須全部成立，並完成 Form D 15 項逐項查核；適用項目均須為「是」，第 10、12、14 項不得略過。第 11、15 項僅可依表 16 所列紙本或已核實官方公開頁分支附理由記「不適用」。Form F 須完整記錄並與核心條件、Form D 一致，但不是第二組十項全是的獨立門檻；若不一致先 HOLD 更正。任何必要條件為否／未知即 HOLD；可靠反證才 REJECTED。` → `7. 開 Form F 作五項核心條件判定：①官方來源／獎項確認；②身分對照；③訓練關聯；④有效同意／揭露權限；⑤來源定位與保存。全部「是」才可進入真實來源審查，完成真實來源審查後才可記 VERIFIED_REAL；任一「未知」或可補正之「否」→ HOLD；已確認偽造／矛盾 → REJECTED（僅該證據項）；未授權揭露 → 立即 STOP_DISCLOSURE。Form F 與 Form D 是同一門檻，不是額外十項門檻；不一致先 HOLD 更正。`
- CASE-01 `consent_status`：`UNKNOWN（無有效同意）` → `UNKNOWN（真實世界；無有效同意、無簽署；SAMPLE workflow 的限縮同意僅為流程模擬）`
- CASE-02 `consent_status`：`UNKNOWN（無有效同意）` → `UNKNOWN（真實世界；無有效同意、無簽署／明確授權；無模擬同意）`
- CASE-01 `consent_scope`：`未取得；不得對外查證/揭露` → `真實世界未取得，不得對外查證／揭露；SAMPLE workflow 僅模擬「內部查核＋向主辦查證、不含公開」，不是真實同意。`
- CASE-02 `consent_scope`：`未取得；不得對外查證/揭露` → `未取得，不得對外查證／揭露；無模擬同意。`
- CASE-01 `course_source`：`SYNTHETIC ONLY；無真實課程計畫、名冊或評量來源已核實` → `UNKNOWN`
- CASE-02 `course_source`：`SYNTHETIC ONLY；無真實課程來源已核實` → `UNKNOWN`
- CASE-01 `notes`：`無第三方原件；不得寫成已得獎` → `SAMPLE／SYNTHETIC。無真實課程計畫、名冊或評量；課程來源 UNKNOWN，未核實。無第三方原件，不得寫成已得獎。`
- CASE-02 `notes`：`截圖與另一貼文相似，尚未查證，不得指控` → `SAMPLE／SYNTHETIC。無真實課程計畫、名冊或評量；課程來源 UNKNOWN，未核實。截圖與另一貼文相似，尚未查證，不得指控。`
- CASE-01 `internal_review_date`：`2026-10-26（SAMPLE，非外部期限）` → `2026-10-26（SAMPLE only；非外部期限；檢查模擬限縮同意可否轉為真實同意／授權）`
- CASE-02 `internal_review_date`：`2026-10-20（SAMPLE，非外部期限）` → `2026-10-30（SAMPLE only；2026-10-20 覆核已完成；非外部期限；原因：同意及身分／隊名對照缺件未補，維持 HOLD）`

**§7.3**

- `綜合： RECEIVED_UNVERIFIED，案件狀態 HOLD。原因不是「證明造假」，而是「無法確認＋同意不足＋身分對不上」。在沒有可靠反證前，不能用 REJECTED。` → `綜合：RECEIVED_UNVERIFIED，案件狀態 HOLD。原因不是「證明造假」，而是「無法確認＋同意不足＋身分 UNKNOWN／目前無法對照」。在沒有可靠反證前，不能用 REJECTED；只有經官方名單或可靠來源完成比對且確認不同人，才可記身分不符。`
- §7.4 `證據狀態：RECEIVED_UNVERIFIED。已收到合成無網址截圖，尚無獎狀、官方公告或主辦回覆；取得有效同意及聯繫授權後再找官方來源，不能推論得獎或未得獎。` → `證據狀態：RECEIVED_UNVERIFIED。已收到合成無網址截圖，尚無獎狀、官方公告或主辦回覆；真實世界 consent_status=UNKNOWN，SAMPLE workflow 僅 SYNTHETIC_SIMULATED_LIMITED_CONSENT，OUTBOUND_REQUEST=NOT_SENT；取得真實同意及聯繫授權後再找官方來源，不能推論得獎或未得獎。`

**§9.3–§9.4**

- §9.3 `示範判定：HOLD（待真實來源）。...` → `示範判定：HOLD（來源＋有效同意／聯繫及揭露授權）。已收到一張合成無網址截圖，證據狀態 RECEIVED_UNVERIFIED；SAMPLE 請求待源，OUTBOUND_REQUEST=NOT_SENT；不得寫成已得獎、已查證或可公開。`
- §9.3 `缺少項目： 官方結果頁或主辦確認、獎狀影本、得獎者身分對照、競賽規則。` → `缺少項目：有效同意與對外聯繫／揭露授權；官方結果頁或主辦確認；獎狀影本；得獎者身分對照（UNKNOWN／目前無法對照）；競賽規則；真實課程／評量紀錄。`
- §9.3 `內部檢視： 2026-10-26 為合成內部覆核日，不是外部期限；未取得同意與聯繫授權前不得追蹤或對外聯繫。` → `內部檢視：2026-10-26 為 SAMPLE-only 內部檢視日，不是外部期限；SAMPLE workflow 為 PENDING_REAL_SOURCE，實際 OUTBOUND_REQUEST=NOT_SENT；REAL_CONTACT=BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY。`
- §9.4 `示範判定： HOLD（同意不足＋身分不足）。...` → `示範判定：HOLD（有效同意缺席＋身分／隊名無從對照）。證據狀態 RECEIVED_UNVERIFIED；不得寫成已得獎、已查證、已拒絕或造假。`
- §9.4 `期限：internal_review_date 為 2026-10-20...` → `期限：2026-10-20 SAMPLE 覆核已完成並維持 HOLD；next SAMPLE-only internal_review_date 為 2026-10-30，原因為同意及身分／隊名對照缺件未補；非外部期限。external_due_date 未設定（OUTBOUND_REQUEST=NOT_SENT）。`
- §9.4 `內部檢視： 2026-10-20 為合成內部覆核日...` → `內部檢視：2026-10-20 SAMPLE 覆核已完成；2026-10-30 為下次 SAMPLE-only 內部檢視日，非外部期限；同意及身分／隊名缺件未補前維持 HOLD。`
- 刪除 §9.3／§9.4 原十項勾選列，換為 C 的兩案五 Gate 表。

**§10**

- §10 邊界聲明開頭：`邊界聲明： 以下兩案都是虛構的流程演練。為避免把演練誤認為真實紀錄，本文件不虛構任何送出、回覆、簽章、核准或得獎證明。` → `邊界聲明：以下兩案都是虛構的流程演練。本文件不虛構任何真實送出、第三方／主辦回覆、簽章、核准、獎項證明或真實成就；合成學員敘述（例如「我參加競賽得到佳作」、隊名是暱稱、含糊的「可以拿去用」）僅是流程模擬，均標示 SAMPLE／SYNTHETIC，不是真實對話、同意或第三方陳述。`
- §10.1 同意列：`未取得簽署或明確授權；不得對外查證或公開` → `真實世界 UNKNOWN；未取得簽署或明確授權，不得對外查證或公開。SAMPLE workflow 僅 SYNTHETIC_SIMULATED_LIMITED_CONSENT，非真實同意；OUTBOUND_REQUEST=NOT_SENT。`
- §10.1 處理第 2 點：`2026-10-06：合成流程原擬進行同意說明，但示範狀態設定為尚未取得簽署或明確授權；沒有實際同意書、簽名或對話紀錄。` → `2026-10-06：SAMPLE 流程設定為「模擬限縮同意」：僅供內部查核及向主辦查證，不含公開；沒有實際同意書、簽名、對話或真實授權。此狀態是工作流模擬，REAL_CONSENT=UNKNOWN。`
- §10.1 處理第 4 點：`2026-10-07：合成流程預定在取得同意及授權後搜尋主辦單位官方管道；本示範未實際搜尋、定位網址、撥打或寄出。` → `2026-10-07：SAMPLE 請求草稿完成，REQUEST_STATE=PENDING_REAL_SOURCE；本示範未實際搜尋、定位網址、撥打或寄出，OUTBOUND_REQUEST=NOT_SENT。`
- §10.1 目前判定：`HOLD。不是「已得獎」，也不是「未得獎」。...` → `HOLD（來源＋有效同意／聯繫及揭露授權）。不是「已得獎」，也不是「未得獎」。只有合成無網址截圖（RECEIVED_UNVERIFIED），沒有可核對官方來源，且沒有真實同意或授權角色；SAMPLE workflow 待源，實際 OUTBOUND_REQUEST=NOT_SENT，REAL_CONTACT=BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY。`
- §10.2 同意列：`未取得簽署或可用授權；情境文字不是實際對話或同意紀錄` → `真實世界 UNKNOWN；未取得簽署或可用授權；無模擬同意；情境文字不是實際對話或同意紀錄。`
- §10.2 處理第 3 點：`合成情境以含糊的「可以拿去用」作為待判斷文字；這不是實際對話或同意紀錄，不能視為授權，也不代表發生過聯繫。` → `合成情境以含糊的「可以拿去用」作為待判斷文字；這不是實際對話、同意或授權，也不代表發生過聯繫。`
- §10.2 處理第 6 點：`2026-10-20：維持 HOLD。不是 REJECTED，因為沒有可靠證據證明造假；也不是 VERIFIED_REAL，因為關鍵事實都無法確認。` → `2026-10-20：SAMPLE 覆核完成，維持 HOLD。不是 REJECTED，因為沒有可靠證據證明造假；也不是 VERIFIED_REAL，因為關鍵事實都無法確認。下次 SAMPLE-only 內部檢視日：2026-10-30；原因：同意及身分／隊名對照缺件未補。`
- §10.2 目前判定：`HOLD。阻擋事項有兩項：同意不足、身分無法對應。...` → `HOLD。阻擋事項：有效同意缺席、身分／隊名 UNKNOWN／目前無法對照（非已確認不符）。在同意與身分未補前，不向主辦查個人資料，也不公開截圖。`
- §10.3 同意列：CASE-01 → `真實世界未取得簽署；SAMPLE 僅模擬限縮同意（非真實）`；CASE-02 → `未取得簽署或明確授權；無模擬同意`
- §10.3 身分列：CASE-01 → `UNKNOWN／目前無法對照`；CASE-02 → `UNKNOWN／隊名無從對照（未取得官方名單）`
- §10.3 新增／替換「請求狀態」：CASE-01 → `PENDING_REAL_SOURCE；OUTBOUND_REQUEST=NOT_SENT`；CASE-02 → `NOT_READY_FOR_REQUEST；OUTBOUND_REQUEST=NOT_SENT`
- §10.3 主要阻擋：CASE-01 → `第三方來源未核實；有效同意與聯繫／揭露授權未取得；OUTBOUND_REQUEST=NOT_SENT`；CASE-02 → `有效同意缺席；身分／隊名無從對照`

**§12.2**

- `一個合成事實一行。未來取得真實資料時，逐行替換，不要整份文件改寫。doc_id 固定為 0102。` → `一個合成事實一行；F-0102-036 不列入事實列，另列別名 DUPLICATE_OF=F-0102-016。未來取得真實資料時，逐行替換，不要整份文件改寫。doc_id 固定為 0102。`
- 表頭 `文件位置` → `穩定定位（章節＋指名表單／欄位／案例）`
- `訓練關聯欄記錄是否已有可追溯的課程、練習與評量資料；本文件此示範案例尚未建立該關聯。` → `訓練關聯欄記錄是否已有可追溯的課程、練習與評量資料；本文件此示範案例尚未建立該關聯。訓練關聯欄不得放 DUPLICATE_OF 或其他別名標記。`
- 逐列套用 D：每一 `fact_id` 的「穩定定位」全文替換為 D 的 Exact corrected locator；不得保留任何表號、列號或 ordinal。
- 表後加：`別名（不列入事實列、不計數）：F-0102-036 DUPLICATE_OF=F-0102-016。F-0102-036 已 RETIRED；與 F-0102-016 共用同一來源替換要求與查核紀錄；不得重複索取、重複計數或放入訓練關聯欄。`

**§14**

- `身分只是對不上` → `身分 UNKNOWN／目前無法對照`
- 該列門檻 `可能是暱稱、隊名或資料缺漏` → `尚無官方名單、隊名或可對照資料`
- 該列判定 `HOLD` 不變；後續 `補隊名、參賽證明、主辦對照` 保留。
- `沒有同意` → `沒有同意（真實世界）`
- 該列門檻 `未簽署或只口頭` → `未簽署、只口頭，或僅有 SAMPLE 模擬限縮同意（非真實同意）`
- `表 16 的紙本無數位檔或已核實官方公開頁無附件分支` → `§7.1 Form D #11／#15 的紙本無數位檔或已核實官方公開頁無附件分支`
- `不是額外全是門檻` 保留，並在其後加 `；Form F 五項全部為是，仍須完成真實來源審查才可記 VERIFIED_REAL。`

**§15.4 版本歷史**

在 R33 列後新增，不刪不改 R33：

| R34 | 2026-10-23 | 將 §12.1 改為一案一行；全面校正 §12.2 全部 F-0102 定位並移除表號／列號座標；重建 Form F 五項核心條件；釐清 CASE-01 合成限縮同意／請求待源與 CASE-02 同意／身分對照 HOLD 之差異；course_source 改為 UNKNOWN；修正 CASE-01 身分用語及 CASE-02 覆核日；F-0102-036 改列別名；限縮不捏造聲明。 | 文件維護角色 | SAMPLE／SYNTHETIC 候選；未正式接受；真實得獎與核准狀態 UNKNOWN；0/2=0% 僅流程示例。 |
|---|---|---|---|---|

**§15.5／全域表號清理**

- 所有 `表 16 所列紙本或已核實官方公開頁分支` → `§7.1 Form D #11／#15 所列紙本或已核實官方公開頁分支`
- `表 26 第 9 列` → `§9.2「判定門檻」疑似重複列`
- `表 43「疑似重複」列` → `§14.1「疑似重複」列`
- `見表 36` → `見 §11.4「已驗證率」`
- `表 18A` → `§7.3 CASE-01 Form D 逐項結果`
- `Table 19 row 13` → `§7.3 CASE-02 Form D #12`
- 所有頁首頁尾 `候選 R33` → `候選 R34`；封面 `版本 R33` → `版本 R34`。

## F. `CONSISTENCY_CHECK`

- `case_id`：`SYN-0102-CASE-01`、`SYN-0102-CASE-02`；各出現為獨立列，不重複貼標籤。
- CASE-01 dates：claim `2026-10-05`；course `2026-03-02～2026-04-10`；competition `2026-08-22`；review `2026-10-26`。
- CASE-02 dates：claim `2026-09-30`；course `2026-01-05～2026-02-15`；competition `2026-08-22`；review completed `2026-10-20`；next review `2026-10-30`。
- `course_source`：兩案均為 `UNKNOWN`；兩案 `notes` 均說明無真實課程來源且未核實。
- Real consent：兩案均 `UNKNOWN`；CASE-01 僅 `SYNTHETIC_SIMULATED_LIMITED_CONSENT`；CASE-02 為 `NO_SIMULATED_CONSENT`。
- Request state：CASE-01 `PENDING_REAL_SOURCE`；CASE-02 `NOT_READY_FOR_REQUEST`；兩案 `OUTBOUND_REQUEST=NOT_SENT`。
- Real contact：CASE-01 `BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY`；CASE-02 `BLOCKED_CONSENT_ABSENT`。
- Identity：CASE-01 `UNKNOWN／目前無法對照`；CASE-02 `UNKNOWN／無對照基礎`；不得寫成已確認不符。
- Case dispositions：兩案均 `HOLD`；無 `REJECTED`；無 `VERIFIED_REAL`。
- Evidence states：兩案均 `RECEIVED_UNVERIFIED`；無第三方原件；無官方來源；無主辦回覆；locator 均 `NONE／UNLOCATED`。
- Form locations：CASE-01 Form E = §8.3；CASE-02 Form E = §8.4；CASE-02 duplicate check = §7.3 Form D `#12`。
- Form F：五 Gate 均為 `YES／NO／UNKNOWN`；`Form F` 與 `Form D` 同一門檻，不是額外十項門檻。
- Fact count：55 個事實列（001–035、037–056）＋1 個 `F-0102-036` 別名；合計 56 個既有 ID；036 不計事實、不放訓練關聯欄。
- Arithmetic unchanged：`2` synthetic claims；`0` verified award cases；`0/2=0%`；不得改寫為協會績效或 TTQS 分數。
- Synthetic boundary：不主張真實送出、第三方／主辦回覆、簽名、核准、獎項證明或真實成就；合成學員敘述均標 `SAMPLE／SYNTHETIC`。
- Official interpretation unchanged：I18-E09；p.7 award reference is a 4-point evidence example, not a score guarantee；p.4 2-point standard remains learner/target-customer belief in ability improvement.
- No repair is asserted as applied, and no formal acceptance is granted.