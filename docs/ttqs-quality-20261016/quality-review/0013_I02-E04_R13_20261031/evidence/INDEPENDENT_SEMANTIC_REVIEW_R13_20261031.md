# 0013 / I02-E04 R13 — independent semantic review

- Candidate state: `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`
- Candidate DOCX SHA-256: `bf13360703574a7e310864135dcb667314387462678ab8db12d63a0fe79ae31d`
- Reviewer context: independent Codex subagent `01a18f20-c637-7f52-8e00-ff278024a2de` (separate from Builder)
- Model identity: `UNKNOWN`
- Review result: `PASS` for semantic correctness and operational usability of the SAMPLE/SYNTHETIC candidate only.
- Review method: reviewer re-hashed the DOCX and reviewed all 154 body/table items; did not perform visual/layout review.

## Original reviewer response (verbatim)

VERDICT=PASS（限 SAMPLE／SYNTHETIC 候選的語意與可用性；不代表有真實公開紀錄）

CANDIDATE_SHA256=bf13360703574a7e310864135dcb667314387462678ab8db12d63a0fe79ae31d

EVIDENCE_SCOPE=我對指定 R13 DOCX 實算 SHA-256，與指定值一致；已逐項抽取並審閱該檔全部 154 個正文／表格項目。核對來源包括官方 PDF 第 1 頁、crosswalk 的 I02-E04 列、BLUEPRINT_CURRENT 的 0013／I02-E04 列，以及 R13 引用的 source_packet_R01（SHA-256 `b87440b249ec78c6bbe69ff001fe9d7dbb5060d65f27fe61d21ec48cdb5bfa63`）和繼承的 R11 合成登錄。R13 內容是直接依 exact SHA 重審，沒有沿用 R12 的語意 verdict。

FINDINGS=
- §1–§2.3、§11.1 的目的、文類和追溯內容，符合官方原文「公開公布訓練機構年度訓練課程。」；來源定位為 PDF 第 1 頁。Crosswalk 對應 0013，Blueprint row SHA-256 為 `b529f3c13e964b6edbec124158d3559df988b401ce3b97fd1984e90b0582d35b`。
- §3–§5 定義納入／排除規則、角色交接及九項課程公開欄位；§7–§10 提供一致性檢查、PASS／HOLD／REJECT 判定、例外更正及 REAL 替換流程，日常操作者可依步驟執行。
- §14 顯示版本 R13、日期 2026-10-31。§11.2 的標題盲識別段落位於鄰項拒絕表後、§12 前，內容仍與該節相符。

REGISTER_ALIGNMENT=§13「逐事實 SYNTHETIC 替換清冊」（DOCX 第 19 個表格）有 67 筆資料。與繼承的 R11 register（SHA-256 `ae3e266c878283538a8dd57991c02e2123ff24a2d72fa9f7d6833aa55c5b074c`）逐列比對，Fact ID、順序、合成值、定位、REAL 替換方式及角色碼均相符；67 筆皆無缺漏或多列。R12／R13 staging manifest 未附此 register；本次使用的是 R13 引用來源鏈上的繼承版。

MATH_AND_CLAIMS=
- §7.1：4 門 × 9 項公開欄位＝36；R-A 為 35/36＝97.2%，R-B 為 36/36＝100%。R-A 的單一缺欄是 C04 報名通路。
- §6.2–§6.5、§7.2：淨授課時數 6＋12＋6＋6＝30 小時；規劃名額 20＋18＋20＋16＝74 席。各課程時段扣除休息後與所列時數相符。
- §7.1、§9：四個報名通路均為 `.invalid`，可用／已核實通路為 0/4；將其列為不可用並維持 HOLD，判斷一致。
- 未發現算術或內文交叉引用矛盾。

SAMPLE_REAL_BOUNDARY=§1、§3–§4、§6、§9–§10、§12–§14 清楚標示合成機構 O-001、角色 R01–R05、2027 課程及演練日期為 SAMPLE／SYNTHETIC。`.invalid` 網址明示不可使用；沒有把核准、公開、報名、辦訓或成果說成真實。§9 的「官方核准／認證」只作無來源宣稱的 REJECT 測試例。實際核准與公開證據未提供，文件正確維持 HOLD。

TITLE_BLIND_NEGATIVE_NEIGHBORS=遮蔽標題、檔名及編號後，§5–§8 的年度公開課程欄位、排程完整度、發布閘門與讀回程序仍可辨認本件用途。§11.2 鄰項拒絕表明確區分 0012／I02-E03 優惠制度與 0014／I02-E05 客戶課程需求申請表，並說明本件不制定優惠條款，也不收集客製需求。

DEFECTS=未發現需修正的語意或可用性缺陷。此 PASS 僅適用於完整 SAMPLE 工作稿的語意與操作流程。

LIMITATIONS=未執行視覺或版面審查。文件沒有真實年度課程公告、核准原件或公開頁讀回證據，因此不能證明機構已實際公開年度課程。R12／R13 staging 未內含來源封包與 register；本次依 R13 所列 SHA 找到並核對繼承來源。未修改任何檔案，也未派送 CLI。

FORMAL_ACCEPTANCE=NOT_GRANTED