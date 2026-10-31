# OpenCode narrow independent review packet — TTQS ONE 0110 / I18-E19

## Identity and hashes
- Candidate revision: R09; exact DOCX SHA-256: `7fc82ba7ae25ba3fd422d7abcae2618176f64d4e2e118021122912440d9b740f`
- Source packet SHA-256: `e3db8f4ed82b21de4dc8cfb5886c4387c123d49a0465356354a18a9be39a8d38`
- Unique Blueprint SHA-256: `81ec1fc96c9d48fa2a088fbe32ecf8bc31abd88a3d8945ba22585226440a8796`
- Deterministic mapping receipt SHA-256: `8ea8d3072e67daa258e6d8820fad01434c0e980a0e31488bb22ebd5a7b456d53`
- Candidate state: reversible CANDIDATE; formal acceptance NOT_GRANTED; REAL evidence UNKNOWN/HOLD.
- This request is only a narrow consistency review, not full-document semantic or visual review.

## Official requirement and governing boundaries
Official I18-E19 wording: 「問卷調查及課後行動計畫評估表等顯示目標客戶及學員認為訓練對組織績效的改善及提升均有顯著的效果。」
Blueprint: separate learner and target-client/service-partner questionnaires plus post-course action-plan/follow-up; do not claim causal/statistical significance from a small self-report sample. All demonstrated people, dates, answers, measures, action decisions and outcomes are SAMPLE/SYNTHETIC. No association execution/approval is established. Checkbox serial is UNKNOWN.

## Candidate Table 6: item-to-construct mapping
編號 | 觀察焦點 | 分析構面 | 回答尺度與使用規則
L01 | 標準作業指引理解 | 操作指引理解 | 同意尺度；單題呈現
L02 | 受訓前後自覺執行信心變化（學員主觀自我效能） | 自我效能感知（非組織績效） | 變化尺度；題幹須寫明比較基準
L03 | 交接紀錄查核要點執行 | 查核步驟執行 | 同意尺度；單題呈現
L04 | 符合條件班次的實際使用頻率 | 實際使用頻率 | 專用頻率代碼；不作Likert平均或有利率
L05 | 突發情境依流程處置 | 情境處置能力 | 同意尺度；單題呈現
L06 | 換班口頭及書面交接 | 交接執行能力 | 同意尺度；單題呈現
L07 | 報到資料完整度的前後變化 | 資料完整度變化 | 變化尺度；與可追溯操作紀錄分開呈現
L08 | 交接等待時間的前後變化 | 交接流程變化 | 變化尺度；不與資料完整度平均
L09 | 團隊協作的前後變化 | 協作變化 | 改為明確、可觀察的比較題；使用變化尺度
C03 | 接待流暢及服務表現變化 | 服務體驗變化 | 由指定期間內直接觀察者作答
C04 | 物資及資料正確、齊全程度變化 | 資料物資完整正確變化 | 改用前後比較，不用滿意度錨點
C05 | 交接時段服務連續性變化 | 服務連續性變化 | 明列觀察期間及比較基準
C06 | 突發狀況回應時間前後變化 | 應變回應時間變化 | 改為可觀察的比較題，不用同意度錨點
C07 | 整體可觀察的組織績效變化 | 整體績效變化 | 單題報告；不與 C03–C06 合成分數

## Candidate Table 30: learner SAMPLE raw rows
合成填答代碼 | L01–L09 原始答案（依題號順序）
L01 | L01=4；L02=3；L03=4；L04=3；L05=4；L06=4；L07=4；L08=3；L09=4
L02 | L01=4；L02=4；L03=4；L04=3；L05=3；L06=4；L07=4；L08=4；L09=3
L03 | L01=5；L02=4；L03=4；L04=2；L05=4；L06=3；L07=3；L08=3；L09=4
L04 | L01=3；L02=3；L03=3；L04=3；L05=3；L06=4；L07=4；L08=4；L09=3
L05 | L01=4；L02=5；L03=5；L04=1；L05=4；L06=4；L07=4；L08=4；L09=3
L06 | HOLD／INVALID（不合格 respondent；原始值保留：L01=4；L02=4；L03=4；L04=0；L05=5；L06=3；L07=3；L08=3；L09=3）〔SAMPLE〕
L07 | L01=5；L02=3；L03=3；L04=4；L05=2；L06=5；L07=5；L08=2；L09=4
L08 | L01=4；L02=4；L03=4；L04=2；L05=0；L06=4；L07=0；L08=0；L09=0

## Candidate Table 32: client/partner SAMPLE raw rows
合成填答代碼 | C01、C02、C03–C07、C08 原始答案（全為 SAMPLE／SYNTHETIC）
C01 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），2 次，F2；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），3 次，F2；C03=4；C04=4；C05=3；C06=3；C07=4；C08=是（SAMPLE 練習：使用檢核表完成活動報到與志工交接）；匿名回覆代碼=C01；填答日期=SAMPLE 2026-03-02
C02 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），2 次，F2；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），2 次，F2；C03=4；C04=3；C05=4；C06=4；C07=3；C08=是；匿名回覆代碼=C02；填答日期=SAMPLE 2026-03-02
C03 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），1 次，F1；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），2 次，F2；C03=3；C04=4；C05=4；C06=3；C07=4；C08=不確定；匿名回覆代碼=C03；填答日期=SAMPLE 2026-03-02
C04 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），3 次，F2；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），4 次，F3；C03=5；C04=4；C05=3；C06=4；C07=4；C08=是；匿名回覆代碼=C04；填答日期=SAMPLE 2026-03-02
C05 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），2 次，F2；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），2 次，F2；C03=4；C04=5；C05=4；C06=4；C07=4；C08=否；匿名回覆代碼=C05；填答日期=SAMPLE 2026-03-02
C06 | C01=是；C02=SAMPLE：基線 2025-12-31 至 2026-01-30（D−30～D0），1 次，F1；訓練後 2026-01-31 至 2026-03-01（D0＋1～D0＋30），1 次，F1；C03=0；C04=0；C05=0；C06=0；C07=0；C08=不確定；匿名回覆代碼=C06；填答日期=SAMPLE 2026-03-02

## Candidate Table 34: displayed item summaries
群體／題號 | 有效 N；0／空白／無效／重複 | 有效總分 | 平均 | 4–5人數／比例
學員／L01 | N=7；0=0／0／0／0（L06 respondent 已排除） | 29 | 4.143 | 6/7＝85.7%
學員／L02 | N=7；0=0／0／0／0（L06 respondent 已排除） | 26 | 3.714 | 4/7＝57.1%
學員／L03 | N=7；0=0／0／0／0（L06 respondent 已排除） | 27 | 3.857 | 5/7＝71.4%
學員／L04（頻率） | 1–4 有機會者 7；0／不合格=1（L06）；空白／無效／重複=0 | — | 不計分 | 1=1；2=2；3=3；4=1（合計 7），不計有利比例
學員／L05 | N=6；0=1／0／0／0（L06 respondent 已排除） | 20 | 3.333 | 3/6＝50.0%
學員／L06 | N=7；0=0／0／0／0（L06 respondent 已排除；本列為題目 L06） | 28 | 4.000 | 6/7＝85.7%
學員／L07 | N=6；0=1／0／0／0（L06 respondent 已排除） | 24 | 4.000 | 5/6＝83.3%
學員／L08 | N=6；0=1／0／0／0（L06 respondent 已排除） | 20 | 3.333 | 3/6＝50.0%
學員／L09 | N=6；0=1／0／0／0（L06 respondent 已排除） | 21 | 3.500 | 3/6＝50.0%
客戶／夥伴／C03 | N=5；0=1／0／0／0 | 20 | 4.000 | 4/5＝80.0%
客戶／夥伴／C04 | N=5；0=1／0／0／0 | 20 | 4.000 | 4/5＝80.0%
客戶／夥伴／C05 | N=5；0=1／0／0／0 | 18 | 3.600 | 3/5＝60.0%
客戶／夥伴／C06 | N=5；0=1／0／0／0 | 18 | 3.600 | 3/5＝60.0%
客戶／夥伴／C07 | N=5；0=1／0／0／0 | 19 | 3.800 | 4/5＝80.0%

## Candidate Table 28: operational example
項目 | 基線 | 期中追蹤（＋30 天）
分子（完成服務簽到紀錄筆數） | 6 | 7
分母（抽樣調閱紀錄筆數；固定） | 8 | 8
分數表示 | 6／8 | 7／8（期中；不得重寫為 90%）
比率（分子 ÷ 分母 × 100） | 75.0% | 87.5%
目標 | 至少 90.0%（固定分母 8 時須 8/8＝100.0%） | 至少 90.0%（最終門檻，D0＋60；固定分母 8 時須 8/8＝100.0%）
與目標差（百分點，pp） | −15.0 | −2.5
前後差（追蹤 − 基線） | ＋12.5 個百分點（pp） | 
目標達成判定 | 期中未達（87.5%＜至少 90.0%）；最終門檻於 D0＋60 判定 | —（D0＋60 未到；尚無最終結果）
處置 | REVISE（期中） | 

## Deterministic independent recomputation bound to this exact SHA
R04 verifier directly extracted the tables from the above exact DOCX SHA, matched all 14 Table 6 mappings, recalculated all 14 item summaries from Tables 30/32, and compared them to Table 34. Result: PASS_DETERMINISTIC_DIRECT_CANDIDATE_CROSSCHECK. The example is: baseline 6/8=75.0%; D0+30 7/8=87.5%; +12.5 percentage points; fixed denominator 8 means a >=90% target requires 8/8=100%; D0+30 is REVISE; D0+60 is pending, not CLOSE. L04 is a frequency distribution and excluded from Likert mean/favorable rate. L06 learner is HOLD/INVALID and excluded where applicable; client rows require C01=Yes and C08 is not eligibility.
