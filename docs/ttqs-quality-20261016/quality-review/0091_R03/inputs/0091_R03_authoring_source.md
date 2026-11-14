# 0091 R03｜學員就業證明：協會端請求、收件、查核與追溯紀錄（可直接使用成品）

> **`SAMPLE / SYNTHETIC — 本文件不含任何協會核發證書或真實學員就業紀錄`**
>
> 本文件供協會授權訓練行政人員使用。官方勾選項原文、PDF頁次與SHA-256、需求代碼及方框序號均為核對後的REAL來源識別事實；本文案例、角色、日期、定位碼、聯繫、檢視、授權、處置及結果均為SAMPLE/SYNTHETIC，不代表原始點協會曾執行、核准或收件。本文件不是雇主、政府機關或第三方核發的證明。

---

## 1. 白話封面：這份文件是什麼

| 欄位 | 內容 |
|---|---|
| 文件編號 | 0091 |
| 官方需求代碼 | `I17D-E05` |
| 官方勾選項序號 | `098` |
| 官方勾選項文字（原文） | `學員就業證明。` |
| 文件用途 | 當學員**自願**提供就業證明時，協會端如何安全地「提出請求 → 收件 → 檢視 → （必要時）向核發單位查核 → 建檔 → 調閱 → 更正」之完整作業流程與紀錄表單 |
| 適用對象 | 小型訓練協會之**授權訓練行政人員**（多為無全職人資部門之志工型組織） |
| 何時使用 | 學員結訓後之追蹤期間內，學員表達願意提供就業證明時；或協會依已核准之佐證用途需要建立就業證明收案紀錄時 |
| 本文件「記錄什麼」 | 記錄**協會收取與查核就業證明之過程與判定**，不記錄、不生成、不代替任何就業證明本身 |
| 本文件「不記錄什麼」 | 不收錄真實身分證字號、住址、電話、簽名、印章、薪資數字、雇主營業資料 |
| 先決條件 | 必須先有 REAL 來源（真實名冊、追蹤到期日、已核准之佐證用途）才能開案；缺任一項即為 `HOLD_SOURCE_NOT_CONFIRMED` |

**一句話定位：** 這是一份「協會向學員索取就業證明並留下收案與查核痕跡」的作業手冊與表單集，不是就業證明本身。

---

## 2. 需求與邊界

### 2.1 官方來源引用（唯一直接引用之 REAL 事實）

| 項目 | 值 |
|---|---|
| 官方勾選項文字 | `學員就業證明。` |
| 出處頁次 | 官方 PDF 第 6 頁 |
| 官方 PDF SHA-256 | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` |
| 需求代碼 | `I17D-E05` |
| 勾選項序號 | `098`（注意：與 DOCX ID 0098 無關） |

> 官方勾選項文字、PDF頁次及SHA、需求代碼、方框序號是REAL來源識別資訊；其餘案例、角色、日期、定位碼、狀態與結果均為SYNTHETIC。

### 2.2 證據等級三層區分（不可混用）

本文件之核心紀律：**學員自述 ≠ 收到文件 ≠ 向核發單位查證**。三者為不同證據等級，任何紀錄欄位不得互相頂替。

| 證據等級 | 名稱 | 「證明了什麼」 | 「沒有證明什麼」 |
|---|---|---|---|
| G0 | 學員自述（Self-report） | 該學員曾以口頭或表單表示其已就業 | 不證明就業事實存在、不證明雇主身分、不證明期間 |
| G1 | 學員自願提供之原件／可驗文件，**未經檢視** | 某份文件曾送達協會收件流程 | 不證明文件真實、不證明內容正確、不證明與學員之關聯 |
| G2 | 文件完成協會內部形式檢視 | 已逐項記錄可見欄位、可讀性、缺漏及表面連結；只代表形式檢視完成 | 不證明文件真實、內容正確、核發者同意或學員確已就業；不是獨立查證 |
| G3 | 已向核發單位／授權來源查核 | 在特定授權範圍內，經指定管道向核發單位確認過該文件之存在與欄位 | 不證明就業續存、不證明超出查核範圍之事項 |
| GX | 未解決／無效 | 收到但無法支持就業事實，或已判定為不可用 | — |

### 2.3 本文件不能取代什麼

- 本文件**不能取代**任何雇主、政府機關或第三方核發之就業證明；本文件只是該證明之「收案與查核痕跡」。
- 本文件**不能取代** 0090（`I17D-E04`，主管觀察之學習成果評量）；主管觀察之學習成果不是雇主證據，也不是學員就業證明。
- 本文件**不能取代** 0092（`I17D-E06`，感謝函請求與原件追蹤）；感謝函不是就業證明。
- 本文件**不能取代** 0088（`I17D-E02`，較廣義之結訓後追蹤）之任何分母、個案或結論；若未確認共享之真實個案來源，本文件之合成個案保持獨立。

---

## 3. 角色與低維運作流程（志工型協會）

> 不新增部門、不臆造授權層級。以下角色皆為**稱呼**，實際由協會現有人力兼任即可。

| 角色代碼 | 稱呼 | 職責範圍 | 不可為之事 |
|---|---|---|---|
| `ADMIN-ROLE` | 訓練行政人員 | 開案、寄送請求範本、收件、初檢、填寫登錄表 | 不得在無授權下聯繫雇主；不得自行判定 G3 |
| `REVIEW-ROLE` | 複核人員（同一協會內第二人） | 覆核證據等級與處置、核定 STOP/HOLD | 不得為同一案件之原始收件人兼任放行 |
| `PRIV-ROLE` | 隱私／同意事項窗口（可由 `ADMIN-ROLE` 兼任，但欄位須分開簽） | 確認同意書範圍、效期、撤回狀態 | 不得在無書面授權下核准對外聯繫 |
| `LEARNER` | 學員 | 自願提供證明、決定是否授權聯繫雇主 | — |

**低維運作原則：** 每案僅需兩名不同人員（`ADMIN-ROLE` + `REVIEW-ROLE`）簽核即可結案；若協會僅有一人，`REVIEW-ROLE` 欄位應保留並標記 `UNASSIGNED_SINGLE_STAFF`，案件不得升級至 G3。

---

## 4. 聯繫授權與隱私關卡（Pre-contact Authorization Gate）

### 4.1 協會主動聯繫學員前檢核

| 欄位 | 核對事項 | 結果值 |
|---|---|---|
| LEARNER_CONTACT_BASIS | REAL班期及追蹤作業依據 | REAL locator 或 NOT_PROVIDED |
| APPROVED_PURPOSE | 已核准且涵蓋本次追蹤之用途 | REAL locator 或 NOT_PROVIDED |
| NOTICE_VERSION | 自願性、用途、必要欄位、保留及拒絕無不利後果告知 | 核准版本或 NOT_PROVIDED |
| LEARNER_CHANNEL | 協會授權且適用的管道 | 管道名稱及REAL依據 |
| LEARNER_GATE_RESULT | 主動請求關卡 | PASS / HOLD / STOP / INBOUND_VOLUNTARY |

任一依據、用途、告知或管道不明時為HOLD，不得主動寄送。學員主動來訊／來電可記INBOUND_VOLUNTARY，不補造外呼依據。雇主外查授權另按4.2下表檢核。本表及範本不構成同意書或聯繫權限。



### 4.2 雇主／核發單位外部查證授權檢核表（只有需要外聯時）

| 欄位 | 說明 | 可接受值 |
|---|---|---|
| `AUTH_BASIS` | 授權依據（同意書編號／個別書面授權） | REAL locator 或 `NOT_PROVIDED` |
| AUTH_TARGET | 實際獲授權聯繫的雇主／核發單位及指定窗口 | REAL locator 或 NOT_PROVIDED |
| `AUTH_SCOPE` | 授權範圍（可聯繫對象、可查證欄位） | 文字描述，須明確 |
| `AUTH_DATE` | 授權日期 | 日期 |
| `AUTH_EXPIRY` | 授權效期 | 日期或 `NOT_PROVIDED`（視同無效期＝不予 PASS） |
| `PERMITTED_CHANNEL` | 核准管道（官方信箱、掛號等） | 明確管道名稱 |
| WITHDRAWAL_STATUS | 撤回狀態 | NONE / WITHDRAWN / UNKNOWN；不得以沉默推定NONE |
| `CHECKER` | 檢核者角色 | 角色代碼 |
| `EVIDENCE_LOCATOR` | 支持上述欄位之 REAL 定位碼 | REAL locator |
| `GATE_RESULT` | 關卡結果 | `PASS` / `HOLD` / `STOP` |

**判定規則：**
- `EVIDENCE_LOCATOR` 為空、`AUTH_EXPIRY` 為空、或 `WITHDRAWAL_STATUS = WITHDRAWN` → **不得**填 `PASS`。
- `AUTH_BASIS = NOT_PROVIDED` 或 `PERMITTED_CHANNEL` 未指定 → `HOLD`。
- 學員明確拒絕 → `STOP`（記錄 `DECLINED`，無不利語句）。

---

## 5. 逐步作業流程（SOP）與例外分支

### 步驟 1：確認來源後才開案
- 確認：(a) 訓練班期（REAL）；(b) 追蹤到期日（REAL）；(c) 已核准之佐證用途（REAL）。
- 任一缺失 → 處置 `HOLD_SOURCE_NOT_CONFIRMED`，不得開案、不得寄送任何請求。

### 步驟 2：隱私／同意關卡
- 協會主動聯繫學員前完成學員聯繫檢核；聯繫雇主／核發單位前另完成書面授權檢核並經第二角色複核 PASS。學員主動聯繫只記錄為 INBOUND_VOLUNTARY。
- 學員拒絕或撤回 → 記錄 `STOP_WITHDRAWN` 或 `DECLINED`，停止選擇性聯繫，語句不含任何懲罰或不利暗示。

### 步驟 3：向學員提出自願請求
- 只有學員聯繫關卡 PASS 時才使用第 6.1 節範本，經核准管道寄出；學員自願來訊則直接記錄，不補造外呼依據。
- 明確告知：可不提供、可不授權聯繫雇主、亦有不涉雇主之替代選項（見 6.3）。
- 只索取必要欄位，不索取與佐證無關之敏感欄位。

### 步驟 4：收件與限制存取
- 收到文件後，於登錄表記錄：收到日期、項目類型、核發者代碼、限制存取定位碼。
- **原件置於協會限制存取儲存處**；公開證據包／登錄表**僅**記載合成定位碼或遮罩參照，**絕不**收錄真實證明影本、姓名、身分證字號。

### 步驟 5：形式檢視（不判真偽）
- 逐項記錄已檢視：文件類型、核發者欄位、日期、與學員／班期之連結、可讀性、完整性、**是否足以支持所稱就業事實**。
- 同時記錄**未檢視**之項目（例：未向核發單位確認、未查核期間續存）。

### 步驟 6：核發單位查核（僅在必要且已 PASS 時）
- 前置：關卡 `PASS` + 學員授權範圍涵蓋本次查核欄位。
- 僅使用核准管道；記錄方法、日期、角色。
- **不得在未發生聯繫時暗示已聯繫。**

### 步驟 7：判定處置
- 依第 7 節決策表，指定：證據等級、理由、複核角色、到期日、更正路徑、下一步行動。

### 步驟 8：登錄表與來源母體勾稽
- 將登錄表與**已確認之來源母體**及追蹤期間勾稽後，才可計算任何彙總統計。
- 母體或分母為未知 → **不報比率**，改報 `NO_RATE_UNKNOWN_DENOMINATOR`。

### 例外分支速查

| 例外情境 | 分支 |
|---|---|
| 缺 REAL 來源 | 停於步驟 1，`HOLD_SOURCE_NOT_CONFIRMED` |
| 未通過授權關卡 | 停於步驟 2，改走 6.3 替代路徑 |
| 學員中途撤回 | 立即 `STOP_WITHDRAWN`，停止一切對外聯繫 |
| 收到文件但不足以支持就業事實 | `NOT_SUPPORTED`，等級 GX，給予更正路徑 |
| 查核管道無回應 | `PENDING_AUTHORIZED_CHECK`，非 `VERIFIED` |
| 協會僅有單一承辦人員 | `REVIEW-ROLE = UNASSIGNED_SINGLE_STAFF`，禁止升級至 G3 |

---

## 6. 表單與範本

> **所有範本均標記 `SAMPLE / SYNTHETIC`，僅供格式示範；本文件不主張任何範本曾被寄出。**

### 6.1 學員請求範本（協會 → 學員）【SAMPLE】

```
主旨：【SAMPLE】關於結訓後就業狀況佐證資料之自願提供說明

您好：

本協會依【班期代碼 REAL】結訓後追蹤作業，若您願意，可自願提供
就業相關證明，供本協會建立佐證紀錄之用。

重點說明：
1. 提供與否完全自願；不提供不影響您任何權益。
2. 您可選擇「僅提供文件、不授權我們聯繫雇主」。
3. 您亦可選擇不提供文件，改以其他方式表達（見替代選項）。
4. 我們只會收集與佐證目的相關之必要欄位。

如您願意提供，請於【SAMPLE 到期日】前，透過協會授權管道
【PERMITTED_CHANNEL 欄位】送達。

（本文件為 SAMPLE / SYNTHETIC，非已寄出之通知）
```

### 6.2 雇主請求範本（協會 → 雇主）【SAMPLE，僅限授權關卡 PASS 後】

> ⚠️ 此為**協會發出之請求**格式，非雇主回覆，不得改寫為雇主語氣或格式。

```
主旨：【SAMPLE】學員【SYN-0091-CASE-01】在職證明資料查詢請求

本協會（【協會 REAL 名稱】）已取得該學員【授權文件 REAL locator】之
書面授權，授權範圍為【AUTH_SCOPE】。謹此函請於【到期日】前，
透過【PERMITTED_CHANNEL】惠予確認下列欄位：

- 在職狀態（查詢基準日：【日期】）
- 到職日期

本請求僅涉上述欄位，不涉及薪資或其他非必要個資。
（本文件為 SAMPLE / SYNTHETIC，非已寄出之請求）
```

### 6.3 無回應、拒絕與不涉雇主替代路徑【SAMPLE】

| 情境 | 可用回覆或動作 | 結果與限制 |
|---|---|---|
| 學員拒絕提供 | 「了解，謝謝您回覆。本案會記錄為『學員拒絕提供』，不影響您任何權益。」 | DECLINED；停止追問 |
| 學員撤回授權 | 「了解，我們會停止尚未進行的外部聯繫並記錄撤回時間。」 | STOP_WITHDRAWN；已發生事項照實保留 |
| 只交文件、不授權聯繫雇主 | 接受自願交件，由協會按核准用途做內部形式檢視；不聯繫雇主 | 最多記G2，不宣稱真偽或已查證 |
| 不交件且不授權外查 | 記NOT_PROVIDED；依正式政策提供非雇主選項，否則暫停 | UNKNOWN / NOT_VERIFIED；不作不利推論 |
| 必要外查缺授權 | 不寄出雇主請求，列出授權缺項 | HOLD_NO_AUTHORIZATION；不得以G2冒充G3 |
| 已授權外查但無回應 | 記錄等待狀態，不寫成已查證 | PENDING_AUTHORIZED_CHECK |

以上是合成範例，不代表曾寄送或發生。無正式核准時，不自行創設替代佐證要求。

### 6.4 就業證明收案與查核登錄表（欄位定義）

本表是限制存取的內部主表；公開摘錄須另建遮罩視圖，不得直接匯出或與受限欄位混存。每欄填實值、NOT_PROVIDED、NOT_APPLICABLE或定義狀態碼，不留白。

| 欄位 | 說明 |
|---|---|
| `CASE_ID` | 合成個案代碼 |
| `COHORT_LOCATOR` | 班期／來源定位碼（REAL） |
| `DUE_WINDOW` | 追蹤到期期間 |
| `SELF_REPORT_STATUS` | 學員自述狀態 |
| `CONSENT_STATUS` | 同意／授權狀態 |
| `ITEM_TYPE` | 收到之文件類型 |
| `ISSUER_CODE` | 核發者代碼（不得寫真實雇主名） |
| `RECEIVED_DATE` | 收到日期 |
| `RESTRICTED_ORIGINAL_LOCATOR` | 限制存取原件定位碼（REAL，不公開） |
| `CHECKS_PERFORMED` | 已檢視項目 |
| `CHECKS_NOT_PERFORMED` | 未檢視項目 |
| `VERIFICATION_METHOD` | 查核方法 |
| `VERIFICATION_DATE_ROLE` | 查核日期與角色 |
| `EVIDENCE_GRADE` | G0–G3 或 GX |
| RESULT_STATUS | UNKNOWN / PENDING / NOT_VERIFIED等結果狀態；不能只靠證據等級推論 |
| ACCESS_LOG_REF | 連結每次讀取受限案件／原件的調閱紀錄 |
| RETENTION_STORE | REAL受限儲存位置locator；不可用公開路徑代替 |
| LEARNER_CONTACT_BASIS / LEARNER_GATE_RESULT | 協會外呼依據或學員主動接觸狀態 |
| `DISPOSITION` | 處置（見決策表） |
| `REVIEWER_ROLE` | 複核角色 |
| `HOLD_REASON` | 暫停理由 |
| `RESPONSIBLE_ROLE` | 負責下一步之角色 |
| `NEXT_DUE_DATE` | 下次到期日 |
| `CORRECTION_TRAIL` | 更正軌跡 |

---
## 7. SAMPLE / SYNTHETIC 案例：已填欄位但來源證據不足

> 以下為**完整填寫之合成案例**，演示一個「欄位已填但來源證據不足而暫停」之完整作業決定。**不演示成功查證。**

### 7.1 登錄表：SYN-0091-CASE-01【SAMPLE / SYNTHETIC】

| 欄位 | 值 |
|---|---|
| `CASE_ID` | `SYN-0091-CASE-01` |
| `COHORT_LOCATOR` | `SYN-COHORT-2026-Q1`（← 須以 REAL 班期定位碼替換） |
| `DUE_WINDOW` | `2026-06-01 ～ 2026-08-31`（← 須以 REAL 追蹤期間替換） |
| LEARNER_CONTACT_BASIS / LEARNER_GATE_RESULT | INBOUND_VOLUNTARY；學員主動來電，協會未外呼 |
| NOTICE_VERSION | NOT_APPLICABLE；本例無協會主動聯繫 |
| SELF_REPORT_STATUS | 學員主動來電口述「已就業」；只記其陳述，不證明就業 |
| `CONSENT_STATUS` | 未提供雇主聯繫之書面授權 |
| `ITEM_TYPE` | 無（未收到任何文件） |
| `ISSUER_CODE` | `NOT_APPLICABLE` |
| `RECEIVED_DATE` | `NOT_APPLICABLE` |
| `RESTRICTED_ORIGINAL_LOCATOR` | `NOT_APPLICABLE`（無原件） |
| CHECKS_PERFORMED | 僅檢查本合成表單欄位一致性；未核對REAL班期、期間或用途 |
| `CHECKS_NOT_PERFORMED` | 未向任何雇主聯繫（因授權關卡未 PASS）；未檢視任何文件 |
| VERIFICATION_METHOD | NOT_APPLICABLE；未作外查 |
| `VERIFICATION_DATE_ROLE` | `NOT_APPLICABLE` |
| `EVIDENCE_GRADE` | `G0`（僅學員自述） |
| RESULT_STATUS | UNKNOWN / NOT_VERIFIED |
| `DISPOSITION` | `HOLD_NO_AUTHORIZATION_OR_ORIGINAL` |
| `REVIEWER_ROLE` | `REVIEW-ROLE`（合成） |
| `HOLD_REASON` | 無雇主聯繫授權 **且** 未收到任何可檢視之文件；兩項均缺，不得升級證據等級 |
| `RESPONSIBLE_ROLE` | `ADMIN-ROLE` |
| `NEXT_DUE_DATE` | `2026-07-15`（SAMPLE） |
| `CORRECTION_TRAIL` | 無 |
| RETENTION_STORE | NOT_APPLICABLE；沒有原件 |
| ACCESS_LOG_REF | SYN-0091-ACCESS-01（僅合成受限主表讀取示例） |

### 7.2 已完成之授權關卡

| 欄位 | 值 |
|---|---|
| `AUTH_BASIS` | `NOT_PROVIDED` |
| AUTH_TARGET | NOT_PROVIDED |
| `AUTH_SCOPE` | NOT_PROVIDED |
| `AUTH_DATE` | NOT_PROVIDED |
| `AUTH_EXPIRY` | NOT_PROVIDED |
| `PERMITTED_CHANNEL` | NOT_PROVIDED |
| WITHDRAWAL_STATUS | UNKNOWN；不能推定未撤回 |
| `CHECKER` | `PRIV-ROLE` |
| EVIDENCE_LOCATOR | NOT_PROVIDED |
| `GATE_RESULT` | **`HOLD`**（無依據可 PASS） |

**結論：不得聯繫雇主。下一步由 `ADMIN-ROLE` 於 `2026-07-15` 前，改以 6.3 替代腳本向學員提供「不涉雇主之替代選項」。**

### 7.3 判定說明：為何「學員自述就業」不是「就業證明」

學員自述屬 **G0**。它證明的是「學員曾作出一項陳述」，而非「就業事實存在」。就業證明之所以為證明，是因為存在一份**由核發者具名、可追溯、可受檢視**的文件（G1/G2），或經核發單位確認（G3）。本案例中既無文件、又無授權聯繫核發者，因此證據等級停留於 G0，處置為 `HOLD_NO_AUTHORIZATION_OR_ORIGINAL`，結果欄位維持 `UNKNOWN / NOT_VERIFIED`。此為**完整且可辯證之作業決定**，非失敗，亦非成功。

---

## 8. 決策表、更正路徑與拒絕／暫停條件

### 8.1 處置決策表

| 處置代碼 | 觸發條件 | 可用證據等級 | 是否可對外聯繫 | 結果語句 |
|---|---|---|---|---|
| HOLD_INSPECTION_PENDING | 已收件但尚未形式檢視 | G1 | 否；外查另需授權 | 暫停；指定檢視人及期限 |
| G2_NO_EXTERNAL_CHECK | 形式檢視完成但未外查 | G2 | 否，除非另有授權 | UNKNOWN / NOT_VERIFIED；僅稱內部檢視完成 |
| HOLD_NO_AUTHORIZATION | 必要外查缺有效授權 | G0–G2 | 否 | UNKNOWN / NOT_VERIFIED；列缺欄，不妨礙自願交件後內檢 |
| `HOLD_SOURCE_NOT_CONFIRMED` | 缺 REAL 班期／到期日／用途之一 | — | 否 | 未開案 |
| `HOLD_NO_ORIGINAL` | 有授權但無可檢視文件 | G0 | 否 | `UNKNOWN` |
| `HOLD_NO_AUTHORIZATION_OR_ORIGINAL` | 授權與原件皆缺 | G0 | 否 | `UNKNOWN / NOT_VERIFIED` |
| `PENDING_AUTHORIZED_CHECK` | 已 PASS、已聯繫、等待回應 | G2 | 已聯繫（限範圍內） | `PENDING` |
| `VERIFIED_WITH_SCOPE` | 已於授權範圍內獲核發單位確認 | G3 | — | **僅限範圍內成立** |
| `NOT_SUPPORTED` | 文件不足以支持所稱就業事實 | GX | 否 | `NOT_SUPPORTED` |
| `DECLINED` | 學員明確拒絕 | — | 否 | `DECLINED` |
| `STOP_WITHDRAWN` | 學員撤回授權 | — | **立即停止** | `STOP_WITHDRAWN` |

> ⚠️ **合成案例禁用 `VERIFIED`**。任何 SYNTHETIC 範例不得填入 `VERIFIED_WITH_SCOPE`。

### 8.2 更正與申訴路徑

1. 學員或相關方提出更正 → `ADMIN-ROLE` 於登錄表 `CORRECTION_TRAIL` 新增一列（不覆寫原列）。
2. `REVIEW-ROLE` 覆核更正後之證據等級與處置。
3. 申訴案件僅以代碼追蹤；公開儲存庫**不得**出現真實個資。

### 8.3 保留與調閱定位欄位

| 欄位 | 說明 |
|---|---|
| `RETENTION_STORE` | 限制存取儲存位置之 REAL locator |
| `ACCESS_LOG_REF` | 調閱紀錄參照（見 8.4） |
| `PUBLIC_LOCATOR` | 公開登錄表中之遮罩參照（不得含真實個資） |

### 8.4 調閱紀錄（Access Log）

| ACCESS_LOG_REF | CASE_ID | 日期 | 角色 | 目的 | 實際讀取範圍 | 授權／依據 | 結果 |
|---|---|---|---|---|---|---|---|
| SYN-0091-ACCESS-01 | SYN-0091-CASE-01 | 2026-06-20（SYNTHETIC） | REVIEW-ROLE | 複核暫停處置 | 僅合成受限主表G0與處置欄；未讀原件（無原件） | 合成內部角色權限演練，非雇主聯繫授權 | ACCESS_RECORDED_SYNTHETIC |

### 8.5 拒絕／暫停條件總表

- 未確認 REAL 來源 → 暫停開案。
- 授權關卡非 PASS → 暫停對外聯繫。
- 文件不足以支持就業事實 → 拒絕升級（`NOT_SUPPORTED`）。
- 學員撤回 → 立即停止。
- 分母未知 → 拒絕計算比率（`NO_RATE_UNKNOWN_DENOMINATOR`）。

---

## 9. 合成替換登錄表與 REAL 替換清單

> 本表逐一映射文中每個合成值至其欄位，以及**必須取代它之 REAL 事項**。

| 合成值 | 所屬欄位 | 必須取代之 REAL 事項 |
|---|---|---|
| `SYN-0091-CASE-01` | `CASE_ID` | 協會實際個案編號規則產出之編號 |
| `SYN-COHORT-2026-Q1` | `COHORT_LOCATOR` | 實際訓練班期之定位碼 |
| `2026-06-01 ～ 2026-08-31` | `DUE_WINDOW` | 實際追蹤到期期間 |
| `2026-07-15` | `NEXT_DUE_DATE` | 實際排定之下次到期日 |
| `2026-06-20` | 調閱紀錄日期 | 實際調閱日期 |
| `ADMIN-ROLE` / `REVIEW-ROLE` / `PRIV-ROLE` | 各角色欄 | 實際承辦人員之角色指派 |
| 「學員表示已就業」 | `SELF_REPORT_STATUS` | 實際收到之學員陳述紀錄 |
| `NOT_PROVIDED`（授權） | `AUTH_BASIS` 等 | 實際同意書或個別授權之 REAL locator |
| `HOLD_NO_AUTHORIZATION_OR_ORIGINAL` | `DISPOSITION` | 實際判定之處置 |
| `G0` | `EVIDENCE_GRADE` | 實際判定之證據等級 |
| UNKNOWN / NOT_VERIFIED | RESULT_STATUS | 依實際證據及外查狀態更新；未知不得改為成功 |
| `UNKNOWN / NOT_VERIFIED` | 結果 | 實際結論 |
| 6.1／6.2／6.3 範本文字 | 各請求／腳本 | 實際經核准之範本版本 |
| `NOT_APPLICABLE` 各項 | 收件／查核欄 | 實際收件與查核紀錄 |

| SYN-0091-ACCESS-01／SYN-PUBLIC-0091-01 | ACCESS_LOG_REF／PUBLIC_LOCATOR | 真實受限讀取事件及獨立遮罩摘錄；無真實事件不造列 |
| AUTH_SCOPE／AUTH_DATE／AUTH_EXPIRY／PERMITTED_CHANNEL／EVIDENCE_LOCATOR=NOT_PROVIDED | 授權表 | 只能由有效書面授權與REAL locator取代；否則HOLD |
| G0、G1、G2、G3、GX及全部處置碼 | 證據／決策欄 | 依實際檢視與授權範圍判定；合成例不得填VERIFIED |
| 2026-06-20、REVIEW-ROLE、檢視目的與範圍 | 調閱示例 | 僅有真實存取時逐欄記錄；未發生不建立紀錄 |
| 第6.1至6.3節範本文字 | 請求／回覆模板 | 正式核准前不得發送；樣本不構成授權 |

| 資料群 | 對應欄位 | REAL 替換要求 |
|---|---|---|
| 學員主動聯繫狀態、4.1來源、用途、告知版本與管道 | LEARNER_CONTACT_BASIS / LEARNER_GATE_RESULT / APPROVED_PURPOSE / NOTICE_VERSION / LEARNER_CHANNEL | 只由真實紀錄及核准依據取代；沒有依據就不外呼 |
| AUTH_TARGET與AUTH_SCOPE等授權欄位 | 雇主／核發單位外查 | 書面授權未列目標、範圍、效期或管道時保持HOLD，不外聯 |

### REAL 替換清單（開案前逐項打勾）


- [ ] REAL 班期定位碼已取得
- [ ] REAL 追蹤到期日已取得
- [ ] REAL 已核准佐證用途已取得
- [ ] REAL 同意／授權文件定位碼已取得
- [ ] REAL 限制存取儲存位置已指定
- [ ] REAL 角色指派已確認（非單人兼任 G3）
- [ ] 本合成案例之所有欄位均已替換或明確標記為不適用
- [ ] 全文件已重新掃描，確認未殘留 SYNTHETIC 值被誤當事實

---

## 10. 跨文件連結與不可替代聲明

| 鄰近文件 | 需求代碼 | 關係 | 明確不可替代 |
|---|---|---|---|
| **0090** | `I17D-E04` | 主管觀察之**學習成果**評量 | 學習成果**不是**雇主證據，**不能**替代學員就業證明；兩者流程與產出分離 |
| **0091（本文件）** | `I17D-E05` | 學員就業證明之**協會端**請求／收件／查核流程 | — |
| **0092** | `I17D-E06` | 感謝函請求與原件追蹤 | 感謝函**不是**就業證明；工作流程與文件產出須分開保存 |
| **0088** | `I17D-E02` | 較廣義之結訓後追蹤 | 僅在確認共享之 REAL 個案來源時引用其來源；**不得**複製其個案、結果、分母或結論至本文件。未確認共享來源時，本文件合成個案保持獨立 |

---

> **`SAMPLE / SYNTHETIC — 結語`**
>
> 本文件之目的，是讓小型協會在**不偽造任何原件**之前提下，仍能完整記錄「曾請求、曾收件、曾檢視、曾（或未曾）查核」之事實與理由。所有合成欄位均須以 REAL 證據替換後，方可作為實際作業紀錄使用。本文件不得改寫為雇主、政府機關或第三方核發之任何證明。
