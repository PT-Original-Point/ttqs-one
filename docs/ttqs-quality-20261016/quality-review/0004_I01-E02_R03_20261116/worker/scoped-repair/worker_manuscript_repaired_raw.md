# 0004《目標市場調查執行與樣本紀錄》

## 0. 文件控制卡（CANDIDATE；SAMPLE/SYNTHETIC only）

| 項目 | 內容 |
|---|---|
| 文件代碼 | 0004 |
| 需求代碼 | I01-E02 |
| 專案 157 項次 | 002（專案 crosswalk serial；不是官方 PDF 流水號） |
| 文類 | 執行與樣本紀錄 |
| 官方查核佐證文字 | `目標市場需求調查。`（官方 PDF p.1） |
| 產出狀態 | CANDIDATE DOCX（候選；非正式接受） |
| 內容狀態 | SAMPLE/SYNTHETIC only |
| 正式接受 | NOT GRANTED |
| 真實施測狀態 | UNKNOWN（UNK-0004-REAL-EXECUTION） |
| 獨立語意審查 | pending（尚未進行；不得宣稱正式接受、核准或達成） |
| 程序標示 | 本文件每一項執行程序均為 SAMPLE workflow proposal，待有權限者核准採用 |

審查重點：(1) 官方來源、Blueprint row、crosswalk、來源封包與 register 的 ID、文字、頁次、SHA 是否一致；(2) 遮掉標題後仍可辨識為調查執行／樣本流向紀錄；(3) 篩選、邀請、回收、有效、排除、重複、覆核數字是否逐項對帳；(4) 每個合成日期、代碼、狀態、數量、比率與決定是否附 register fact ID；(5) 是否未把 SAMPLE 寫成 REAL、未重製 0003 題目/答案、未進行 0005 需求分析。

---

## 1. 開場說明、用途、範圍與審查重點

### 1.1 用途
本文件記錄一個目標市場調查批次如何界定接觸對象、實際執行（本示例為合成）邀請、同意、回收、有效性判定、排除／重複處理、覆核及交接。其核心是執行與樣本流向，不是問卷設計，也不是需求分析。

### 1.2 範圍內
- 目標母體描述、納入／排除判定、抽樣框與限制（全為 SAMPLE）。
- 依時間順序的篩選、邀請、同意、回覆收件、有效性判定、排除與覆核程序。
- 匿名接觸代碼、邀請狀態、同意狀態、回覆結果、回覆日期、連結回覆碼、處置理由。
- 有效列與無效列分開的唯一回覆紀錄。
- 批次流向對帳、原始整數、對帳等式、流程品質率。
- 隱私、缺漏、更正、拒答、撤回、去重、資料品質處理。
- 操作者／覆核者角色分離（僅 SAMPLE 角色代碼）。
- 僅向 0005 交接計數、有效匿名回覆碼與限制。

### 1.3 範圍外
- 0003《目標市場需求調查問卷》擁有題目文字、選項、量尺、跳答與完整單筆示範答卷；本文件不重印 Q1–Q13，不複製問卷內容，不另創量尺。
- 0005《目標市場需求分析報告》擁有逐題有效分母、需求排序／彙整、差距解讀、限制與後續決策；本文件不輸出平均分數、需求排名、代表性／因果／開課結論。
- 不分析市場需求、不計算各題平均或排名、不推估母體、不建議開課。
- 不建立或修改 DOCX、0003、0005、共享 dashboard、GitHub、CURRENT 或其他目錄。

### 1.4 狀態與限制
- 本文件所有 worked example 均為 SAMPLE/SYNTHETIC；不得寫成 REAL 施測、協會核准或市場成果。
- 真實施測是否發生、真實抽樣框、真實同意/撤回、真實角色指派、核准保存期限均為 UNKNOWN，必須取得原始證據後逐項替換。
- 本文件不包含真實姓名、身分證號、電話、電子郵件、地址、IP、敏感健康／財務資料或可反向識別真人的追蹤資訊。

---

## 2. 目標母體、納入／排除與抽樣框（SAMPLE）

### 2.1 目標母體描述（SAMPLE）
| 欄位 | 內容 | 事實ID |
|---|---|---|
| 批次代碼 | SYN-0004-CYCLE-01 | SYN-0004-CYCLE-01 |
| 抽樣框描述 | Fictional volunteer-segment contact list; no actual roster is represented. | SYN-0004-FRAME-01 |
| 批次開始日期 | 2026-10-28 | SYN-0004-DATE-OPEN；XREF-0003-SYN-001 |
| 批次截止日期 | 2026-10-29 | SYN-0004-DATE-CLOSE |
| 邀請管道 | Simulated online form invitation; no link was sent. | SYN-0004-CHANNEL-01 |
| 操作角色代碼（SAMPLE only） | SYN-OPS-01 | SYN-0004-ROLE-OPS-01 |
| 覆核角色代碼（SAMPLE only） | SYN-REV-01 | SYN-0004-ROLE-REV-01 |

說明：開始日期與 0003 合成樣本日期 `2026-10-28`（XREF-0003-SYN-001）對齊；此為 shared SAMPLE reference，不構成獨立接受或真實施測證據。

### 2.2 納入／排除判定（SAMPLE）
本來源包未提供真實納入／排除條文。下列資格判定為合成示範值；升 REAL 時必須取得核准的納入／排除證據，重新套用並記錄判定人與日期。

| 匿名接觸代碼 | 資格判定 | 事實ID |
|---|---|---|
| SYN-0004-U001 | ELIGIBLE | SYN-0004-U001-ELIGIBILITY |
| SYN-0004-U002 | ELIGIBLE | SYN-0004-U002-ELIGIBILITY |
| SYN-0004-U003 | ELIGIBLE | SYN-0004-U003-ELIGIBILITY |
| SYN-0004-U004 | ELIGIBLE | SYN-0004-U004-ELIGIBILITY |
| SYN-0004-U005 | INELIGIBLE | SYN-0004-U005-ELIGIBILITY |

### 2.3 抽樣框來源、涵蓋期間與限制（SAMPLE）
- 抽樣框為虛構接觸清單，不代表任何真實名冊、會員資料或可識別個人（SYN-0004-FRAME-01）。
- 涵蓋期間：2026-10-28（SYN-0004-DATE-OPEN）至 2026-10-29（SYN-0004-DATE-CLOSE）。
- 去重識別碼：匿名提交碼；不使用 IP、地址、裝置指紋或任何可識別個人資訊（RULE-0004-DUPLICATE-01）。
- 邀請管道為模擬線上表單邀請，未實際發送連結（SYN-0004-CHANNEL-01）。
- 限制：僅 5 筆虛構接觸代碼，其中 1 筆有效回覆；不得推估母體、不代表性、需求強度或組織績效（SYN-0004-LIMIT-N）。
- 真實抽樣框、授權範圍、抽取日期、去重規則與授權狀態均為 UNKNOWN（UNK-0004-REAL-FRAME）。

### 2.4 有效判定規則（SAMPLE workflow proposal；非已核准政策）
| 規則 | 內容 | 狀態 | 事實ID |
|---|---|---|---|
| 有效性規則 | 合格 + 同意已記錄 + 在核准期間內 + 必填欄位完整 + 一筆唯一匿名回覆 | PROPOSED_RULE_NOT_REAL_POLICY | RULE-0004-ELIGIBILITY-01 |
| 重複規則 | 同一授權匿名提交碼視為一筆唯一回覆；後續副本記錄並排除於唯一計數 | PROPOSED_RULE_NOT_REAL_POLICY | RULE-0004-DUPLICATE-01 |
| 保存規則 | 本來源包未指定保存期限；REAL 保存政策維持 UNKNOWN | UNKNOWN_REAL_SOURCE | RULE-0004-RETENTION-01 |

---

## 3. 執行計畫與流程控制（SAMPLE workflow proposal pending authorized adoption）

### 3.1 階段流程表
| 階段 | 輸入／操作角色 | 操作與控制點 | 輸出／例外路徑 | 相關事實ID |
|---|---|---|---|---|
| 1. 批次建立 | 來源封包、官方來源、Blueprint row、crosswalk；操作者 SYN-OPS-01 | 建立批次代碼 SYN-0004-CYCLE-01；凍結來源 hash；控制點：來源 ID/SHA 一致 | 批次控制卡；來源不一致 → HOLD，不往下執行 | SYN-0004-CYCLE-01；SYN-0004-ROLE-OPS-01 |
| 2. 抽樣框與資格篩選 | 虛構／真實抽樣框；操作者 SYN-OPS-01 | 建立匿名接觸代碼；套用納入／排除；去重 ID、資格理由 | 篩選清單；不合資格 → 不邀請，記錄理由 | SYN-0004-FRAME-01；SYN-0004-DATE-OPEN；SYN-0004-DATE-CLOSE；SYN-0004-U001-ELIGIBILITY 至 SYN-0004-U005-ELIGIBILITY |
| 3. 邀請 | 合格清單；操作者 SYN-OPS-01 | 記錄邀請日期、管道、送達狀態、期限；邀請數對帳 | 邀請紀錄；送達失敗 → 記錄狀態，不計入已邀請數 | SYN-0004-CHANNEL-01；SYN-0004-U001-INVITE-DATE 至 SYN-0004-U005-INVITE-DATE；SYN-0004-COUNT-ELIGIBLE_INVITES |
| 4. 同意／拒絕／未回覆管理 | 邀請紀錄；操作者 SYN-OPS-01 | 記錄明確同意、拒絕、截止無回覆；無回應不視為同意 | 同意狀態；拒絕 → NO_RETURN；無回覆 → NO_RETURN | SYN-0004-U001-CONSENT 至 SYN-0004-U005-CONSENT；SYN-0004-COUNT-REFUSALS；SYN-0004-COUNT-NO_RESPONSE |
| 5. 回收與去重 | 原始收件事件；操作者 SYN-OPS-01 | 依匿名提交碼去重；區分唯一回覆與副本；唯一計數／事件計數分離 | 唯一回覆清單；重複副本 → 去重並保留 lineage | RULE-0004-DUPLICATE-01；SYN-0004-DUP-01-ID；SYN-0004-DUP-01-DECISION；SYN-0004-COUNT-UNIQUE_RETURNS；SYN-0004-COUNT-DUPLICATE_EXTRAS；SYN-0004-COUNT-RAW_RECEIPT_EVENTS |
| 6. 有效性判定 | 唯一回覆；操作者 SYN-OPS-01 + 覆核者 SYN-REV-01 | 套用有效性規則；區分有效／無效；必填欄位、期間、唯一性 | 有效／無效紀錄；不完整／無效 → 記錄排除理由 | RULE-0004-ELIGIBILITY-01；SYN-0004-U001-OUTCOME；SYN-0004-U002-OUTCOME；SYN-0004-COUNT-VALID_UNIQUE；SYN-0004-COUNT-INVALID_UNIQUE |
| 7. 撤回／更正處理 | 撤回或更正請求；操作者 SYN-OPS-01 + 覆核者 SYN-REV-01 | 版本鏈、時間戳、覆核；不覆寫原始紀錄 | 更正軌跡；未核准更正 → 維持原判定 | RULE-0004-ELIGIBILITY-01（提案） |
| 8. 覆核與封存 | 全部紀錄；覆核者 SYN-REV-01 | 獨立重算計數與比率；分子／分母／等式 | 覆核紀錄；不符 → REWORK_REQUIRED | SYN-0004-ROLE-REV-01；SYN-0004-FLOW-SCREEN；SYN-0004-FLOW-INVITE；SYN-0004-FLOW-VALID；SYN-0004-FLOW-RECEIPT |
| 9. 交接 | 有效樣本與限制；覆核者 SYN-REV-01 | 交接計數、有效匿名回覆碼、限制；不含需求分析 | 0005 接收欄；超出交接範圍 → 拒絕 | SYN-0004-HANDOFF-N；SYN-0004-HANDOFF-ID；SYN-0004-LIMIT-N |

上表每一程序均為 SAMPLE workflow proposal pending authorized adoption；角色代碼僅為 SAMPLE，真實指派為 UNKNOWN（UNK-0004-REAL-ROLES）。

### 3.2 例外處理（SAMPLE 事件與提案路徑）
| 例外 | 本批次事件 | 處理 | 事實ID |
|---|---|---|---|
| 不合資格 | SYN-0004-U005 | 不邀請；理由為 OUTSIDE_FICTIONAL_TARGET_SEGMENT | SYN-0004-U005-ID；SYN-0004-U005-ELIGIBILITY；SYN-0004-U005-INVITE-STATE；SYN-0004-U005-DISPOSITION-REASON |
| 明確拒絕 | SYN-0004-U003 | 同意狀態 DECLINED_BEFORE_SUBMISSION；無回覆；不計入回覆數 | SYN-0004-U003-ID；SYN-0004-U003-CONSENT；SYN-0004-U003-OUTCOME；SYN-0004-U003-DISPOSITION-REASON |
| 截止無回覆 | SYN-0004-U004 | 同意狀態 CONSENT_UNKNOWN_NO_RESPONSE；無回覆；無回應不視為同意 | SYN-0004-U004-ID；SYN-0004-U004-CONSENT；SYN-0004-U004-OUTCOME；SYN-0004-U004-DISPOSITION-REASON |
| 不完整／無效回覆 | SYN-0004-U002 | 唯一回覆但排除於有效數；理由 REQUIRED_FIELD_MISSING | SYN-0004-U002-ID；SYN-0004-U002-OUTCOME；SYN-0004-U002-DISPOSITION-REASON |
| 重複回覆 | SYN-0004-DUP-01 | 去重；原始收件事件 +1，唯一回覆 +0 | SYN-0004-DUP-01-ID；SYN-0004-DUP-01-LINK；SYN-0004-DUP-01-DECISION |
| 撤回 | 本批次未登錄撤回事件 | 若撤回發生，標記 WITHDRAWN，排除於有效數與 0005 樣本數，保留審計軌跡 | RULE-0004-ELIGIBILITY-01（提案） |
| 更正 | 本批次未登錄更正事件 | 僅在核准更正窗口與版本鏈下更正；不覆寫原始紀錄；保留缺漏／更正歷程 | RULE-0004-ELIGIBILITY-01（提案） |

---

## 4. 聯絡／邀請紀錄（SAMPLE）

### 4.1 接觸與邀請紀錄
| 匿名接觸代碼（事實ID） | 篩選／邀請／回覆日期（事實ID） | 資格／邀請／同意狀態（事實ID） | 回覆結果／連結回覆碼（事實ID） | 處置理由（事實ID） |
|---|---|---|---|---|
| SYN-0004-U001（SYN-0004-U001-ID） | 篩選 2026-10-28（SYN-0004-U001-SCREEN-DATE）；邀請 2026-10-28（SYN-0004-U001-INVITE-DATE）；回覆 2026-10-28（SYN-0004-U001-RETURN-DATE） | ELIGIBLE（SYN-0004-U001-ELIGIBILITY）；INVITED（SYN-0004-U001-INVITE-STATE）；CONSENT_YES（SYN-0004-U001-CONSENT） | UNIQUE_RETURN_COMPLETE_VALID（SYN-0004-U001-OUTCOME）；SYN-0003-001（SYN-0004-U001-RESPONSE-REF；XREF-0003-SYN-002） | 無排除；有效唯一回覆（SYN-0004-U001-OUTCOME） |
| SYN-0004-U002（SYN-0004-U002-ID） | 篩選 2026-10-28（SYN-0004-U002-SCREEN-DATE）；邀請 2026-10-28（SYN-0004-U002-INVITE-DATE）；回覆 2026-10-28（SYN-0004-U002-RETURN-DATE） | ELIGIBLE（SYN-0004-U002-ELIGIBILITY）；INVITED（SYN-0004-U002-INVITE-STATE）；CONSENT_YES（SYN-0004-U002-CONSENT） | UNIQUE_RETURN_INCOMPLETE_INVALID（SYN-0004-U002-OUTCOME）；NO_ANSWER_CONTENT_CARRIED（SYN-0004-U002-RESPONSE-REF） | REQUIRED_FIELD_MISSING（SYN-0004-U002-DISPOSITION-REASON） |
| SYN-0004-U003（SYN-0004-U003-ID） | 篩選 2026-10-28（SYN-0004-U003-SCREEN-DATE）；邀請 2026-10-28（SYN-0004-U003-INVITE-DATE）；回覆 無回覆事件（SYN-0004-U003-OUTCOME） | ELIGIBLE（SYN-0004-U003-ELIGIBILITY）；INVITED（SYN-0004-U003-INVITE-STATE）；DECLINED_BEFORE_SUBMISSION（SYN-0004-U003-CONSENT） | NO_RETURN（SYN-0004-U003-OUTCOME）；無連結回覆碼（SYN-0004-U003-OUTCOME） | EXPLICIT_REFUSAL（SYN-0004-U003-DISPOSITION-REASON） |
| SYN-0004-U004（SYN-0004-U004-ID） | 篩選 2026-10-29（SYN-0004-U004-SCREEN-DATE）；邀請 2026-10-29（SYN-0004-U004-INVITE-DATE）；回覆 無回覆事件（SYN-0004-U004-OUTCOME） | ELIGIBLE（SYN-0004-U004-ELIGIBILITY）；INVITED（SYN-0004-U004-INVITE-STATE）；CONSENT_UNKNOWN_NO_RESPONSE（SYN-0004-U004-CONSENT） | NO_RETURN（SYN-0004-U004-OUTCOME）；無連結回覆碼（SYN-0004-U004-OUTCOME） | NO_RESPONSE_BY_CLOSE（SYN-0004-U004-DISPOSITION-REASON） |
| SYN-0004-U005（SYN-0004-U005-ID） | 篩選 2026-10-28（SYN-0004-U005-SCREEN-DATE）；邀請 未邀請（SYN-0004-U005-INVITE-STATE）；回覆 無回覆事件（SYN-0004-U005-OUTCOME） | INELIGIBLE（SYN-0004-U005-ELIGIBILITY）；NOT_INVITED（SYN-0004-U005-INVITE-STATE）；NOT_APPLICABLE（SYN-0004-U005-CONSENT） | NO_RETURN（SYN-0004-U005-OUTCOME）；無連結回覆碼（SYN-0004-U005-OUTCOME） | OUTSIDE_FICTIONAL_TARGET_SEGMENT（SYN-0004-U005-DISPOSITION-REASON） |

### 4.2 重複收件事件紀錄
| 重複收件事件代碼 | 收件日期 | 重複對象 | 處置決定 | 計數影響 |
|---|---|---|---|---|
| SYN-0004-DUP-01（SYN-0004-DUP-01-ID） | 2026-10-28（SYN-0004-DUP-01-DATE） | SYN-0003-001（SYN-0004-DUP-01-LINK） | EXCLUDE_EXTRA_COPY_FROM_UNIQUE_COUNTS（SYN-0004-DUP-01-DECISION） | 原始收件事件 +1；唯一回覆 +0；有效數 +0 |

---

## 5. 樣本與回收紀錄（SAMPLE）

### 5.1 有效唯一回覆紀錄（SAMPLE）
| 欄位 | 值 | 事實ID |
|---|---|---|
| 匿名接觸代碼 | SYN-0004-U001 | SYN-0004-U001-ID |
| 匿名回覆碼 | SYN-0003-001 | SYN-0004-U001-RESPONSE-REF；XREF-0003-SYN-002 |
| 回覆日期 | 2026-10-28 | SYN-0004-U001-RETURN-DATE |
| 完整度 | 完整（依回覆結果判定） | SYN-0004-U001-OUTCOME |
| 有效判定 | UNIQUE_RETURN_COMPLETE_VALID | SYN-0004-U001-OUTCOME |
| 排除理由 | 無 | SYN-0004-U001-OUTCOME |
| 重複／更正關係 | 重複副本 SYN-0004-DUP-01 指向同一匿名回覆碼，已去重 | SYN-0004-DUP-01-ID；SYN-0004-DUP-01-LINK；SYN-0004-DUP-01-DECISION |
| 覆核角色 | SYN-REV-01 | SYN-0004-ROLE-REV-01 |
| 原件索引 | SAMPLE/SYNTHETIC；真實原件未知 | UNK-0004-REAL-CONSENT |
| 0005 交接 | 有效樣本數 1 與匿名回覆碼 SYN-0003-001 | SYN-0004-HANDOFF-N；SYN-0004-HANDOFF-ID |

### 5.2 無效唯一回覆紀錄（SAMPLE）
| 欄位 | 值 | 事實ID |
|---|---|---|
| 匿名接觸代碼 | SYN-0004-U002 | SYN-0004-U002-ID |
| 連結回覆碼 | NO_ANSWER_CONTENT_CARRIED | SYN-0004-U002-RESPONSE-REF |
| 回覆日期 | 2026-10-28 | SYN-0004-U002-RETURN-DATE |
| 完整度 | 不完整 | SYN-0004-U002-OUTCOME |
| 有效判定 | UNIQUE_RETURN_INCOMPLETE_INVALID | SYN-0004-U002-OUTCOME |
| 排除理由 | REQUIRED_FIELD_MISSING | SYN-0004-U002-DISPOSITION-REASON |
| 重複／更正關係 | 無重複副本 | SYN-0004-U002-OUTCOME |
| 覆核角色 | SYN-REV-01 | SYN-0004-ROLE-REV-01 |
| 原件索引 | SAMPLE/SYNTHETIC；真實原件未知 | UNK-0004-REAL-CONSENT |
| 0005 交接 | 不交接；不計入有效樣本數 | SYN-0004-HANDOFF-N |

### 5.3 非回收與不合格紀錄（SAMPLE）
| 匿名接觸代碼 | 狀態 | 理由 | 事實ID |
|---|---|---|---|
| SYN-0004-U003 | NO_RETURN | EXPLICIT_REFUSAL | SYN-0004-U003-ID；SYN-0004-U003-OUTCOME；SYN-0004-U003-DISPOSITION-REASON |
| SYN-0004-U004 | NO_RETURN | NO_RESPONSE_BY_CLOSE | SYN-0004-U004-ID；SYN-0004-U004-OUTCOME；SYN-0004-U004-DISPOSITION-REASON |
| SYN-0004-U005 | NO_RETURN | OUTSIDE_FICTIONAL_TARGET_SEGMENT；未邀請 | SYN-0004-U005-ID；SYN-0004-U005-ELIGIBILITY；SYN-0004-U005-INVITE-STATE；SYN-0004-U005-DISPOSITION-REASON |

---

## 6. 流向對帳（SAMPLE）

### 6.1 批次流向對帳表
| 項目 | 數量 | 計數口徑 | 事實ID |
|---|---:|---|---|
| 篩選接觸數 | 5 | 唯一接觸代碼 | SYN-0004-COUNT-SCREENED |
| 資格不符數 | 1 | 已篩選但不合資格 | SYN-0004-COUNT-INELIGIBLE |
| 合資格邀請數 | 4 | 已邀請且符合資格 | SYN-0004-COUNT-ELIGIBLE_INVITES |
| 唯一回覆數 | 2 | 去重後唯一回覆 | SYN-0004-COUNT-UNIQUE_RETURNS |
| 有效唯一回覆數 | 1 | 符合有效性規則 | SYN-0004-COUNT-VALID_UNIQUE |
| 無效唯一回覆數 | 1 | 回收但無效 | SYN-0004-COUNT-INVALID_UNIQUE |
| 明確拒絕數 | 1 | 明確拒絕邀請 | SYN-0004-COUNT-REFUSALS |
| 截止無回覆數 | 1 | 截止日仍無回覆 | SYN-0004-COUNT-NO_RESPONSE |
| 重複副本數 | 1 | 額外收件事件 | SYN-0004-COUNT-DUPLICATE_EXTRAS |
| 原始收件事件數 | 3 | 含重複副本的事件計數 | SYN-0004-COUNT-RAW_RECEIPT_EVENTS |
| 0005 有效樣本數 | 1 | 僅有效唯一回覆 | SYN-0004-HANDOFF-N |
| 0005 有效匿名回覆碼 | SYN-0003-001 | 僅引用，不複製答案 | SYN-0004-HANDOFF-ID |
| 流程限制 | n=1 合成有效回覆；無母體推論 | 限制說明 | SYN-0004-LIMIT-N |

### 6.2 對帳等式
| 等式 | 計算 | 事實ID |
|---|---|---|
| 篩選數 = 不合資格 + 合資格邀請 | 5 = 1 + 4 | SYN-0004-FLOW-SCREEN |
| 合資格邀請 = 唯一回覆 + 拒絕 + 無回覆 | 4 = 2 + 1 + 1 | SYN-0004-FLOW-INVITE |
| 唯一回覆 = 有效 + 無效 | 2 = 1 + 1 | SYN-0004-FLOW-VALID |
| 原始收件事件 = 唯一回覆 + 重複副本 | 3 = 2 + 1 | SYN-0004-FLOW-RECEIPT |

---

## 7. 流程指標（SAMPLE）

### 7.1 指標表
| 指標 | 公式 | 分子／分母 | 結果 | 事實ID |
|---|---|---|---:|---|
| 回覆率 | 唯一回覆 / 合資格邀請 | 2 / 4 | 50.0% | SYN-0004-RATE-RESPONSE |
| 有效率（Blueprint 指定口徑） | 有效唯一回覆 / 唯一回覆 | 1 / 2 | 50.0% | SYN-0004-RATE-EFFECTIVE |
| 有效樣本產出率 | 有效唯一回覆 / 合資格邀請 | 1 / 4 | 25.0% | SYN-0004-RATE-YIELD |
| 資格通過率 | 合資格邀請 / 篩選接觸 | 4 / 5 | 80.0% | SYN-0004-RATE-ELIGIBLE |

### 7.2 算術規則
- 百分比以未四捨五入的原始比值計算後取小數一位。
- 重複副本先去重，再計算唯一回覆及有效率；重複副本不得視為另一位受訪者。
- 拒絕及無回覆不屬回收數；不完整唯一回覆屬回收但無效。
- 分母為 0 時寫 `N/A` 並註明原因，不得填 `0%` 或補造分母。例如：若合資格邀請數 = 0，回覆率 = `N/A`（原因：無合資格邀請，分母不可為 0）。
- 不計算各題平均、需求排名、母體推估、顯著性、因果、開課或組織績效。

---

## 8. 資料品質、隱私與保存（SAMPLE / UNKNOWN）

### 8.1 隱私與匿名化
- 不收或輸出真實姓名、身分證號、電話、電子郵件、地址、IP、敏感健康／財務資料。
- 匿名代碼不得反向識別真人；重複僅用依法核准的匿名提交碼判定（RULE-0004-DUPLICATE-01）。
- 同意狀態必須有明確證據；無回應不視為同意（SYN-0004-U003-CONSENT；SYN-0004-U004-CONSENT）。
- 拒絕前未提交者不產生有效回覆（SYN-0004-U003-OUTCOME）。
- 不完整／無效回覆排除並記錄理由（SYN-0004-U002-DISPOSITION-REASON）。

### 8.2 缺漏、更正、撤回處理
- 必填欄位缺漏使唯一回覆判定為無效（SYN-0004-U002-OUTCOME；SYN-0004-U002-DISPOSITION-REASON）。
- 更正僅能在核准更正窗口與版本鏈下進行；不得覆寫原始紀錄；必須保留缺漏／更正歷程。
- 撤回若發生，標記 WITHDRAWN，排除於有效數與 0005 樣本數，保留審計軌跡；本批次未登錄撤回事件。
- 原始收件事件與唯一回覆分離；重複副本保留 lineage（SYN-0004-DUP-01-ID；SYN-0004-DUP-01-DECISION）。

### 8.3 保存、權限與真實政策
| 未知事實 | 狀態 | 所需來源 | HOLD 動作 | 事實ID |
|---|---|---|---|---|
| 真實施測是否發生 | UNKNOWN | 實際執行紀錄與原始回覆 | 未驗證前不得宣稱已施測 | UNK-0004-REAL-EXECUTION |
| 真實抽樣框 | UNKNOWN | 核准抽樣框原件與版本/hash | 未驗證前不得宣稱有名冊或代表性 | UNK-0004-REAL-FRAME |
| 真實同意／撤回 | UNKNOWN | 原始同意／撤回證據 | 無明確證據不記錄同意 | UNK-0004-REAL-CONSENT |
| 真實角色指派 | UNKNOWN | 核准職責名冊與指派／審查紀錄 | 不得把合成角色代碼當真人 | UNK-0004-REAL-ROLES |
| 核准保存期限 | UNKNOWN | 協會核准保存／刪除政策 | 未提供前維持 UNKNOWN，不自行指定年限 | UNK-0004-REAL-RETENTION |

- 保存規則 ID：RULE-0004-RETENTION-01（本來源包未指定保存期限）。
- 操作者與覆核者代碼僅為 SAMPLE 角色，不是真實人員或核准（SYN-0004-ROLE-OPS-01；SYN-0004-ROLE-REV-01；UNK-0004-REAL-ROLES）。
- 保存位置、外部授權、真實抽樣代表性若無來源，一律為 UNKNOWN。

---

## 9. 覆核、決策與 0005 交接（SAMPLE）

### 9.1 角色分離
| 角色 | 代碼 | 職責 | 事實ID |
|---|---|---|---|
| 操作者 | SYN-OPS-01 | 建立批次、篩選、邀請、回收、去重、初判 | SYN-0004-ROLE-OPS-01 |
| 覆核者 | SYN-REV-01 | 獨立重算計數與比率、覆核排除理由、封存與交接 | SYN-0004-ROLE-REV-01 |

角色分離僅在 SAMPLE 層級描述；真實指派與審查紀錄為 UNKNOWN（UNK-0004-REAL-ROLES）。

### 9.2 明示決策
| 決策代碼 | 對象 | 決策 | 理由／事實ID | 狀態 |
|---|---|---|---|---|
| D-ACCEPT-SAMPLE-FLOW | 全批次合成流程 | 接受為 SAMPLE/SYNTHETIC 示範紀錄，僅供流程與可重算性驗證 | SYN-0004-COUNT-SCREENED、SYN-0004-COUNT-INELIGIBLE、SYN-0004-COUNT-ELIGIBLE_INVITES、SYN-0004-COUNT-UNIQUE_RETURNS、SYN-0004-COUNT-VALID_UNIQUE、SYN-0004-COUNT-INVALID_UNIQUE、SYN-0004-COUNT-REFUSALS、SYN-0004-COUNT-NO_RESPONSE、SYN-0004-COUNT-DUPLICATE_EXTRAS、SYN-0004-COUNT-RAW_RECEIPT_EVENTS；SYN-0004-FLOW-SCREEN、SYN-0004-FLOW-INVITE、SYN-0004-FLOW-VALID、SYN-0004-FLOW-RECEIPT；SYN-0004-RATE-RESPONSE、SYN-0004-RATE-EFFECTIVE、SYN-0004-RATE-YIELD、SYN-0004-RATE-ELIGIBLE | CANDIDATE；非正式接受 |
| D-REJECT-INVALID-UNIQUE | SYN-0004-U002 | 拒絕納入有效樣本數 | SYN-0004-U002-OUTCOME；SYN-0004-U002-DISPOSITION-REASON | REJECTED_FROM_VALID_COUNT |
| D-REJECT-DUPLICATE-EXTRA | SYN-0004-DUP-01 | 去重，不計唯一回覆或有效數 | SYN-0004-DUP-01-DECISION | EXCLUDED_FROM_UNIQUE_COUNTS |
| D-HOLD-REAL-EXECUTION | 真實施測 | HOLD；待原始執行紀錄與原始回覆 | UNK-0004-REAL-EXECUTION | UNKNOWN/HOLD |
| D-HOLD-REAL-FRAME | 真實抽樣框 | HOLD；待核准抽樣框原件 | UNK-0004-REAL-FRAME | UNKNOWN/HOLD |
| D-HOLD-REAL-CONSENT | 真實同意／撤回 | HOLD；待原始同意／撤回證據 | UNK-0004-REAL-CONSENT | UNKNOWN/HOLD |
| D-HOLD-REAL-ROLES | 真實角色 | HOLD；待核准職責名冊 | UNK-0004-REAL-ROLES | UNKNOWN/HOLD |
| D-HOLD-REAL-RETENTION | 真實保存政策 | HOLD；待協會核准保存／刪除政策 | UNK-0004-REAL-RETENTION；RULE-0004-RETENTION-01 | UNKNOWN/HOLD |
| D-REWORK-IF-MISMATCH | 計數／比率 | 若獨立重算與本文件不符，退回重作並保留差異紀錄 | RULE-0004-ELIGIBILITY-01；SYN-0004-FLOW-SCREEN；SYN-0004-FLOW-INVITE；SYN-0004-FLOW-VALID；SYN-0004-FLOW-RECEIPT | REWORK_REQUIRED |

### 9.3 0005 交接表（僅計數、有效匿名回覆碼、限制）
本節僅交接計數、有效樣本數、有效匿名回覆碼與限制；不進行需求分析。

| 交接項目 | 值 | 事實ID | 0005 可用範圍 | 禁止事項 |
|---|---|---|---|---|
| 篩選接觸數 | 5 | SYN-0004-COUNT-SCREENED | 流程品質數 | 不得解讀需求主題 |
| 資格不符數 | 1 | SYN-0004-COUNT-INELIGIBLE | 流程品質數 | 不得解讀需求主題 |
| 合資格邀請數 | 4 | SYN-0004-COUNT-ELIGIBLE_INVITES | 流程品質數 | 不得解讀需求主題 |
| 唯一回覆數 | 2 | SYN-0004-COUNT-UNIQUE_RETURNS | 流程品質數 | 不得解讀需求主題 |
| 有效唯一回覆數 | 1 | SYN-0004-COUNT-VALID_UNIQUE | 有效回覆分母之一 | 不得擴大為母體估計 |
| 無效唯一回覆數 | 1 | SYN-0004-COUNT-INVALID_UNIQUE | 流程品質數 | 不得解讀需求主題 |
| 明確拒絕數 | 1 | SYN-0004-COUNT-REFUSALS | 流程品質數 | 不得解讀需求主題 |
| 截止無回覆數 | 1 | SYN-0004-COUNT-NO_RESPONSE | 流程品質數 | 不得解讀需求主題 |
| 重複副本數 | 1 | SYN-0004-COUNT-DUPLICATE_EXTRAS | 流程品質數 | 不得解讀需求主題 |
| 原始收件事件數 | 3 | SYN-0004-COUNT-RAW_RECEIPT_EVENTS | 流程品質數 | 不得解讀需求主題 |
| 有效樣本數 | 1 | SYN-0004-HANDOFF-N | 作為有效回覆分母之一 | 不得擴大為母體估計 |
| 有效匿名回覆碼 | SYN-0003-001 | SYN-0004-HANDOFF-ID；XREF-0003-SYN-002 | 引用匿名代碼 | 不得複製題目、選項、量尺或答案 |
| 流程率 | 回覆率 50.0%、有效率 50.0%、有效樣本產出率 25.0%、資格通過率 80.0% | SYN-0004-RATE-RESPONSE；SYN-0004-RATE-EFFECTIVE；SYN-0004-RATE-YIELD；SYN-0004-RATE-ELIGIBLE | 作為流程品質率 | 不得推估代表性或因果 |
| 限制 | n=1 合成有效回覆；無母體推論 | SYN-0004-LIMIT-N | 作為限制說明 | 不得建議開課 |

---

## 10. REAL 替換清單與附件索引

### 10.1 REAL 替換清單
| REAL 原件 | 替換對象（SAMPLE ID） | 取得／驗證要求 | 事實ID |
|---|---|---|---|
| 實際核准調查批次紀錄與來源索引 | SYN-0004-CYCLE-01 | 核准批次識別、授權與來源定位 | SYN-0004-CYCLE-01 |
| 有權限真實抽樣框來源與版本/hash | SYN-0004-FRAME-01 | 驗證範圍、來源擁有人、抽取日期、去重規則、授權 | SYN-0004-FRAME-01 |
| 時間戳核准調查時程與原始事件紀錄 | SYN-0004-DATE-OPEN；SYN-0004-DATE-CLOSE | 日期必須在核准調查窗口內；不得由檔案修改時間推論 | SYN-0004-DATE-OPEN；SYN-0004-DATE-CLOSE |
| 核准發送紀錄與隱私核准 | SYN-0004-CHANNEL-01 | 通道與送達證據必須可驗證；不得捏造 email、QR 或發送回執 | SYN-0004-CHANNEL-01 |
| 核准職責名冊與指派紀錄 | SYN-0004-ROLE-OPS-01；SYN-0004-ROLE-REV-01 | 驗證責任與操作者／覆核者分離 | SYN-0004-ROLE-OPS-01；SYN-0004-ROLE-REV-01 |
| 核准納入／排除證據 | SYN-0004-U001-ELIGIBILITY 至 SYN-0004-U005-ELIGIBILITY | 重新套用核准條件並記錄理由與覆核人 | SYN-0004-U001-ELIGIBILITY；SYN-0004-U002-ELIGIBILITY；SYN-0004-U003-ELIGIBILITY；SYN-0004-U004-ELIGIBILITY；SYN-0004-U005-ELIGIBILITY |
| 原始發送／嘗試紀錄 | SYN-0004-U001-INVITE-STATE 至 SYN-0004-U005-INVITE-STATE | 以實際送達／嘗試回執替換；不得宣稱已發送 | SYN-0004-U001-INVITE-STATE；SYN-0004-U002-INVITE-STATE；SYN-0004-U003-INVITE-STATE；SYN-0004-U004-INVITE-STATE；SYN-0004-U005-INVITE-STATE |
| 原始同意／拒絕／撤回證據 | SYN-0004-U001-CONSENT 至 SYN-0004-U005-CONSENT | 僅在明確證據存在時記錄同意；無回應不視為同意 | SYN-0004-U001-CONSENT；SYN-0004-U002-CONSENT；SYN-0004-U003-CONSENT；SYN-0004-U004-CONSENT；SYN-0004-U005-CONSENT |
| 原始匿名回覆收件／拒絕／截止紀錄 | SYN-0004-U001-OUTCOME 至 SYN-0004-U005-OUTCOME | 以原始 intake 狀態替換並保留排除軌跡 | SYN-0004-U001-OUTCOME；SYN-0004-U002-OUTCOME；SYN-0004-U003-OUTCOME；SYN-0004-U004-OUTCOME；SYN-0004-U005-OUTCOME |
| 原始提交時間戳與時區 | SYN-0004-U001-RETURN-DATE；SYN-0004-U002-RETURN-DATE | 以原始收件 metadata 替換；不得用檔案建立時間 | SYN-0004-U001-RETURN-DATE；SYN-0004-U002-RETURN-DATE |
| 0003 register 精確目前 hash 與 SYN-002 | SYN-0004-U001-RESPONSE-REF；XREF-0003-SYN-002 | Writer 開工前重讀 0003 register；若變更，僅更新 0004 引用與本 register | XREF-0003-SYN-002 |
| 時間戳收件紀錄 | SYN-0004-DUP-01-ID；SYN-0004-DUP-01-DATE；SYN-0004-DUP-01-LINK；SYN-0004-DUP-01-DECISION | 以實際重複收件事件代碼替換，保留原始收件 | SYN-0004-DUP-01-ID；SYN-0004-DUP-01-DATE；SYN-0004-DUP-01-LINK；SYN-0004-DUP-01-DECISION |
| 經驗證的原始 frame/export/intake/refusal/close/duplicate ledger | SYN-0004-COUNT-SCREENED；SYN-0004-COUNT-INELIGIBLE；SYN-0004-COUNT-ELIGIBLE_INVITES；SYN-0004-COUNT-UNIQUE_RETURNS；SYN-0004-COUNT-VALID_UNIQUE；SYN-0004-COUNT-INVALID_UNIQUE；SYN-0004-COUNT-REFUSALS；SYN-0004-COUNT-NO_RESPONSE；SYN-0004-COUNT-DUPLICATE_EXTRAS；SYN-0004-COUNT-RAW_RECEIPT_EVENTS | 逐列重算，不得以歷史或合成總數覆寫 | SYN-0004-COUNT-SCREENED；SYN-0004-COUNT-INELIGIBLE；SYN-0004-COUNT-ELIGIBLE_INVITES；SYN-0004-COUNT-UNIQUE_RETURNS；SYN-0004-COUNT-VALID_UNIQUE；SYN-0004-COUNT-INVALID_UNIQUE；SYN-0004-COUNT-REFUSALS；SYN-0004-COUNT-NO_RESPONSE；SYN-0004-COUNT-DUPLICATE_EXTRAS；SYN-0004-COUNT-RAW_RECEIPT_EVENTS |
| 協會核准保存／刪除政策 | RULE-0004-RETENTION-01；UNK-0004-REAL-RETENTION | 僅插入已驗證政策引用與生效版本；否則維持 UNKNOWN | RULE-0004-RETENTION-01；UNK-0004-REAL-RETENTION |

### 10.2 來源身分與 hash（控制性來源）
| 來源 | SHA-256 | 本件用途 |
|---|---|---|
| 官方 PDF p.1 | 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709 | 官方文字 `目標市場需求調查。` |
| BLUEPRINT_CURRENT | 406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e | 0004 row |
| 129-to-142 crosswalk | 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679 | 0003/0004/0005 分件 |
| 需求來源對照表 | ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9 | 官方 p.1 與 PDF_TEXT_EXACT_PAGE_MATCH |
| 來源封包 R02 | 4535ac0b8275297ff60dabd7b4f7ada77bd8bd240b7200a6532ea32eec9aad0b | 本件輸入 |
| Unique Blueprint R02 | cdfaff45068df2c71bb582908c970ad67cd1a8a7ab973a8efd747cce66c4e375 | 本件結構與核算口徑 |
| 合成替換 register R03 | fe8b739b610f6571e54d89e3f1b7ff3fd8c799299084ea473c1f36be8f39a5ab | 84 筆 fact ID |
| 來源準備 manifest R03 | c80cea966a34006490cda6c9d1a832f308018208047326d0da10c09ef6270738 | 控制性驗證 |
| 來源準備 QA R03 | 16733b405001022a14578a2f0b6fddb60212e7d7e7ff1337a1dcf1ef26cfd7a2 | 控制性驗證 |
| 0003 register（read-only） | 646a5dff8a540d53033d1cf161a6d4839bbf9928d0ae4fece6b6a256764604e1 | shared SAMPLE reference |

### 10.3 附件索引
| 附件／來源 | 定位 | 用途 |
|---|---|---|
| SOURCE_PACKET_0004_I01-E02_R02.md | 本件來源封包 | 官方需求、邊界、算例 |
| UNIQUE_BLUEPRINT_0004_I01-E02_R02.md | 本件 Blueprint | 正文順序、表格、核算口徑 |
| SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R03.csv | 84 筆 register | fact ID、值、替換規則、驗證規則 |
| 來源準備 manifest R03 | 控制性來源 | manifest hash 與來源身分 |
| 來源準備 QA R03 | 控制性來源 | QA hash 與檢查結果 |
| source/BLUEPRINT_CURRENT_ROW_0004.jsonl | 控制來源 row | 0004 row |
| source/official_requirement.pdf | 官方 PDF | `目標市場需求調查。` p.1 |
| source/crosswalk_129_to_142.csv | crosswalk | 0003/0004/0005 分件 |
| source/requirement_source_reconciliation.csv | 來源對照 | PDF_TEXT_EXACT_PAGE_MATCH |
| 0003 register（read-only） | 0003 shared reference | SYN-001、SYN-002 |

---

## 11. 跨文件邊界與共享參考（SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE）

### 11.1 邊界
- 0003 擁有題目、選項、量尺、跳答與個別答案；本文件只引用 0003 的合成回覆碼，不複製問卷內容。
- 0004 擁有抽樣框／資格、執行步驟、邀請／同意、回收／有效判斷、缺漏／拒答／重複／撤回、紀錄追溯與資料交接；只計算流程品質率，不分析需求主題。
- 0005 擁有逐題有效分母、主題排序、描述統計、需求差距、解讀與決策；本文件只提供執行數、唯一回覆數、有效性、去重／排除軌跡與有效匿名代碼。
- 專案項次 002 是專案 157 項清單 crosswalk serial，不是官方 PDF 方框流水號。

### 11.2 共享參考欄位（validator correction）
| 事實ID | 類型 | 值 | 狀態 | 說明 |
|---|---|---|---|---|
| XREF-0003-SYN-001 | shared SAMPLE reference（date） | 2026-10-28 | SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE | 與 0003 SYN-001 對齊；非獨立接受或真實施測證據 |
| XREF-0003-SYN-002 | shared SAMPLE reference code（anonymous response code） | SYN-0003-001 | SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE | 與 0003 SYN-002 對齊；不複製問卷答案 |

兩者 scope 均為 `shared_reference`，status 均為 `SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE`；它們不是獨立接受或問卷答案。Writer 開工前必須重讀 0003 register 並比對上述 SHA；若變更，僅更新 0004 的引用與本 register，不得改寫 0003。

---

## 12. 候選狀態與權威邊界（非自證）

本文件為候選稿；其 fact ID、值、計算與來源 hash 的完整性由控制性來源與獨立審查決定，不由本文件自證。控制性來源包括來源封包 R02、Unique Blueprint R02、R03 register、R03 來源準備 manifest/QA、官方 PDF、BLUEPRINT_CURRENT、crosswalk 與 0003 shared register。正式接受、DOCX 品質、語意審查與 REAL 施測狀態均未由本文件宣稱；候選狀態、SAMPLE/SYNTHETIC、NOT GRANTED、UNKNOWN 與 pending 狀態見第 0 節。本文件不宣稱所有事實均已覆蓋或驗證。