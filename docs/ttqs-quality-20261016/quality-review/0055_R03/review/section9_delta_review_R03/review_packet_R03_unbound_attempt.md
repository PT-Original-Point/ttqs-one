# Independent semantic delta review — DOCX 0055 R03

- Official mapping: I12-E03; official checkbox sequence 058; instructor selection and appointment workflow.
- Candidate status: SAMPLE/SYNTHETIC CANDIDATE ONLY; no association acceptance.
- Exact candidate DOCX SHA-256: {hashlib.sha256(docx.read_bytes()).hexdigest()}
- Exact replacement-register SHA-256: {hashlib.sha256(reg.read_bytes()).hexdigest()}
- Predecessor DOCX SHA-256: {hashlib.sha256((r2/"candidate/0055_R02.docx").read_bytes()).hexdigest()}
- Scope: review only the change in Section 9 attendance/quorum row and corresponding register row FAC-0055-038. Prior full semantic PASS and 11-page visual review on the predecessor remain historical evidence; do not claim a full re-review.
- Prior delta finding: denominator ambiguous because P-01 was listed with M-01/M-02/M-03 while the count said 3/3.

## Exact DOCX change
BEFORE: 主席 P-01、委員 M-01、M-02、M-03、紀錄員 S-01（全為合成代碼）；示範設定 3/3 有表決權委員出席。
AFTER: 主席 P-01（本示範設定不表決）、表決委員 M-01、M-02、M-03、紀錄員 S-01（全為合成代碼）；示範設定 3/3 表決委員出席。

## Exact candidate page 8 excerpt
```text
原始點協會｜講師遴選與聘任流程範例 • 示範文件，非正式任命紀錄 
講師遴選與聘任流程範例 • SAMPLE / SYNTHETIC • 第 8 頁 
8｜利益衝突處理與推薦規則 
狀況 處理方式 紀錄欄位 
評審與候選人有近親、財
務、督導、競爭或其他可
能影響公正的關係 
評審於看分前申報；承辦判斷迴避範圍；需要時由有權
者指定替代評審。 
申報人、關係類型、評估
者、處置、替代人、日期。 
候選人資料涉及不必要個
資 
只保留評選必要欄位；限制存取；依組織正式保存規則
處理到期刪除。 
資料項目、用途、存取人、
保存期限、刪除核准。 
資料不一致或資格查不到 
先凍結該候選評分結論；要求補件或以獨立來源查驗；
保留往返紀錄。 
缺件、查驗來源、聯絡日
期、期限、結果。 
 
本合成情境設定三名評審均申報「無已知衝突」，僅供示範表單填寫。真實評審必須分別簽署日期與申報內
容；空白不等於無衝突。 
9｜訓練管理委員會議程與決定紀錄（模擬） 
完全合成的會議情境｜以下會議日期、出席、權限、討論與決定均為虛構。文件以「假設權限已由真實文件證明」
示範決議記錄形式，並不證明原始點協會已成立委員會或作出決議。 
 
欄位 SAMPLE 填寫示例／真實替換要求 
會議基本資料 
合成日期：2026-11-10（未來示例）；14:00–15:00；會議方式：合成實體會議；地點：
SAMPLE。正式使用需填實際日期、場地、通知與簽到原件。 
出席及法定人數 
主席 P-01（本示範設定不表決）、表決委員 M-01、M-02、M-03、紀錄員 S-01（全為
合成代碼）；示範設定 3/3 表決委員出席。須附真實委員任期、簽到及法定人數算法。 
議程一：權限確認 
示範決定前先檢視章程、委員會任期、決議門檻、聘書簽發權與費用核定權；本樣本假設
附件均已驗證，真實情形目前 UNKNOWN。 
議程二：需求與流程 確認課程需求摘要、評選量尺、同題試教、三位評審的利益衝突申報及資格查驗清單。 
議程三：比較結果 
審閱 C-01 82.6、C-02 81.0、C-03 87.6；討論 C-03 教學適配較完整，但須在實際聘任前
完成原件查驗及排程確認。 
合成決議 
SAMPLE：在假設委員會權限有效、表決程序完備且原始資格查驗通過的前提下，決議優
先推薦 C-03；承辦人應先完成所有 HOLD 項目，主席確認無未解異議後，始得依法定授
權簽發聘書。此為教學用模擬文字，並非協會真實決議。 
反對／迴避／附件 
示例：無（合成設定）。真實會議須逐一記錄反對票、棄權、迴避、附件版本及頁數，不
可用「無」代替未記錄。 
```

## Exact current register row FAC-0055-038
{
  "register_id": "FAC-0055-038",
  "fact_id": "FAC-0055-038",
  "case_id": "SYN-0033-PLAN-01",
  "doc_id": "0055",
  "docx_locator": "第 9 節議程表「出席及法定人數」列",
  "synthetic_value_or_field": "合成出席代碼：主席 P-01（本示範設定不表決）、表決委員 M-01/M-02/M-03、紀錄員 S-01；示範設定 3/3 表決委員出席",
  "assumption_rationale": "示範法定人數記錄格式，非真實簽到",
  "cross_doc_reference": "無（本件新增合成，無跨文件事實引用）",
  "real_source_to_obtain": "真實通知、簽到及法定人數規則",
  "responsible_verifier": "委員會紀錄員",
  "evidence_status": "SYNTHETIC／REAL 未知",
  "hold_condition": "無原始簽到／法定人數來源即 HOLD"
}

## Review checks
1. Does the edit make the SAMPLE voting denominator explicit and reconcile the role list to 3/3?
2. Does it remain clearly a synthetic example rather than a real association rule, meeting, vote, or approval?
3. Is the text consistent with the neighboring paragraph that says the meeting context is entirely synthetic and real authority/quorum rules remain unverified?
4. Return PASS / PARTIAL / FAIL bound to the supplied current candidate SHA and register SHA. Cite the exact section and row. State the narrow scope and any remaining defect. Do not claim to have opened/rehashed the binary DOCX, reviewed unaffected sections, or inspected page images.
