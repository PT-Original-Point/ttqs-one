# Bounded independent semantic delta review

Work ID: TTQS-0124-I19-E12-R02-W1-BEAM-TABLE-DELTA-REVIEW
Review only the two changed tables below from the exact candidate. This is NOT a full-document review and cannot grant whole-document semantic PASS or formal acceptance.

## Immutable binding
- Candidate DOCX SHA-256: 5ea20da675395954e5587859ddc3ca4b483abaeff90509a86c66950581afec07
- Exact extracted target-table text SHA-256: 1105d4b08a6752175db81c24b43cf07dc8bf25d4fe8603a0bba9d48522767fd0
- Source packet SHA-256: 83a03deb7cbef3f07ef8b7ce0b2b25e1744baa6bc2e96b29e3259453558ccfee
- Unique Blueprint SHA-256: d0d8b0990d96fb7dab5d02a34d9f507b6434e57778646c920c488f01c1ab0f42
- Official current crosswalk blob SHA-1: cab446ede479001334289d18062e6b8bb2340dc3 (live branch HEAD 70305d55ff1c66b6b15441ebb9b701e89113493d)
- Printed checkbox serial: UNKNOWN_NOT_ASSERTED

## Official requirement
I19-E12, official evidence table page 8: 企業主雇用結訓後學員，肯定機構訓練的成效。

## Applicable Blueprint rules
### D2. Employer feedback instrument
Use neutral, non-leading questions. Each 1–5 rating must define anchors: 1=not demonstrated/strongly disagree, 2=limited, 3=partly or mixed, 4=mostly/agree, 5=consistently/strongly agree. Provide `NOT OBSERVED`, `NOT APPLICABLE`, `DECLINED`, and `UNKNOWN` as separate states, not as zero. Questions:
- Confirm respondent's employer role/authority and observation period.
- Confirm whether the employer hired the graduate and the verified start date.
- Which course-related skill was relevant to the actual role? Record the task and basis.
- What observable work example supports the answer? Include date/period and a permissible source locator, not a fabricated quotation.
- Rate relevance, observed application, work quality/readiness separately; allow N/A.
- Ask whether the employer considers the training useful for job readiness, with YES / PARTLY / NO / INSUFFICIENT OBSERVATION plus reasons.
- Record other influences (onboarding, supervision, prior experience, tools, team process) and any limits on attributing change.
- Confirm whether the employer permits the response to be retained/used for this evaluation; record scope and source of consent.

### D3. Two-part case decision
`HIRE_VERIFIED` requires a real, lawful source supporting an employer-employee hire after verified course completion; `EMPLOYER_AFFIRMATION_VERIFIED` requires an authorized employer respondent's authentic response, an explicit positive statement tied to training, and a source/permission record. Both must be true to label a REAL case as directly responsive. Otherwise use `HIRE_ONLY`, `FEEDBACK_ONLY`, `HOLD`, `NOT_ELIGIBLE` or `SYNTHETIC_ONLY`. The synthetic worked example may demonstrate a positive path but can never be counted as a REAL result.

## Exact candidate content: changed Table 3 and Table 6
[{"table_ordinal_1based":3,"rows":[["判定","條件","結果與後續處理"],["可開始查核","有可識別個案、課程／結訓來源及適當查閱權限","進入雇用來源查核；未知資料記 UNKNOWN，不自行補值"],["雇用主張","只有學員自述、履歷或口頭線索","`CLAIM_ONLY`；可發起查核，尚不是雇用證據"],["只有聘用要約／預計到職","只有錄取或聘用要約、預計報到，沒有可核實的實際到職來源或開始日期。","聘用要約不等於已聘用。只有未核實主張標 `CLAIM_ONLY`；來源待核標 `HOLD`；不得標 `HIRE_VERIFIED`。雇用已核但未取得雇主肯定用 `HIRE_ONLY`；雇主回饋已核但雇用未核用 `FEEDBACK_ONLY`；未符合結訓後聘用條件用 `NOT_ELIGIBLE`。"],["雇用已驗證","真實、合法且可定位來源支持雇主聘用，且開始日期晚於可核實結訓日期","`HIRE_VERIFIED`；仍需另查雇主回饋"],["雇主回饋已驗證","雇主或具權限代表身分／權限可核，回覆原件可定位，且同意範圍適當","`EMPLOYER_RESPONSE_VERIFIED`；還要判斷是否明確肯定訓練成效"],["正面肯定已驗證","回覆明確指出訓練與一項可描述工作準備／工作任務的關聯，保留原回覆與來源；未超出對方可觀察範圍","`EMPLOYER_AFFIRMATION_VERIFIED`；只支持回覆者所陳述範圍，不等於因果證明"],["HOLD／不納入","日期不合、雇主無法核對、回覆者權限不明、來源衝突、同意不足或資料缺漏","標 `HOLD` 並列重啟條件；不能硬湊成正面案例"],["合成示例","所有值皆為文件示範而生成，沒有對應真人或原件","`SYNTHETIC_ONLY`；只說明怎麼填表，不計入任何 REAL 數字"]]},{"table_ordinal_1based":6,"rows":[["編號","中性問題","作答格式","必填佐證／處理"],["E1","您的雇主角色、職務及代表雇主回覆的權限為何？","角色描述＋授權來源／UNKNOWN","記錄授權原件或核對方法；不需要時不收身分證明副本"],["E2","貴單位是否在學員完成課程後聘用此人？若是，聘用開始日為何？","YES／NO／UNKNOWN＋日期","與雇用來源比對；自述或口頭資訊先記 CLAIM"],["E3","在您觀察期間，課程所學與學員目前工作任務的相關程度如何？","1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN","請指出技能與任務；不得只留分數"],["E4","您是否實際看見學員使用所學處理工作任務？","1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN","描述一項可觀察任務、期間及可引用來源"],["E5","對您可觀察的工作表現，訓練內容在哪些方面有幫助或未能提供幫助？","1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN＋開放回答","區分雇主觀察與推論；允許回答沒有幫助／不確定"],["E6","請描述一個具體工作例子，說明您如何判斷訓練內容與任務準備的關聯。","開放回答／DECLINED／UNKNOWN","記日期或觀察期間、任務及來源；不得由承辦代寫成雇主原話"],["E7","除訓練外，還有哪些因素可能影響學員目前的準備或表現？","開放回答／UNKNOWN","可包括既有經驗、入職訓練、同事指導、工具與流程；不要求作因果判定"],["E8","依您可觀察的範圍，您是否認為本機構訓練對學員工作準備有實際幫助？","YES／PARTLY／NO／INSUFFICIENT OBSERVATION","說明理由及具體例子；此項是雇主看法，不是客觀因果證明"],["E9","您同意本回覆被保存及用於何種範圍？","範圍選項＋來源／DECLINED","未取得適當同意不得擴大引用或公開；保留拒答狀態"]]}]

## Delta to evaluate
[
  {
    "table_ordinal_1based": 3,
    "rows_r01": 8,
    "rows_r02": 9,
    "added_rows": [
      [
        "只有聘用要約／預計到職",
        "只有錄取或聘用要約、預計報到，沒有可核實的實際到職來源或開始日期。",
        "聘用要約不等於已聘用。只有未核實主張標 `CLAIM_ONLY`；來源待核標 `HOLD`；不得標 `HIRE_VERIFIED`。雇用已核但未取得雇主肯定用 `HIRE_ONLY`；雇主回饋已核但雇用未核用 `FEEDBACK_ONLY`；未符合結訓後聘用條件用 `NOT_ELIGIBLE`。"
      ]
    ],
    "removed_rows": []
  },
  {
    "table_ordinal_1based": 6,
    "rows_r01": 10,
    "rows_r02": 10,
    "added_rows": [
      [
        "E3",
        "在您觀察期間，課程所學與學員目前工作任務的相關程度如何？",
        "1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN",
        "請指出技能與任務；不得只留分數"
      ],
      [
        "E4",
        "您是否實際看見學員使用所學處理工作任務？",
        "1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN",
        "描述一項可觀察任務、期間及可引用來源"
      ],
      [
        "E5",
        "對您可觀察的工作表現，訓練內容在哪些方面有幫助或未能提供幫助？",
        "1–5／NOT OBSERVED／NOT APPLICABLE／DECLINED／UNKNOWN＋開放回答",
        "區分雇主觀察與推論；允許回答沒有幫助／不確定"
      ]
    ],
    "removed_rows": [
      [
        "E3",
        "在您觀察期間，課程所學與學員目前工作任務的相關程度如何？",
        "1–5／NOT OBSERVED／N/A",
        "請指出技能與任務；不得只留分數"
      ],
      [
        "E4",
        "您是否實際看見學員使用所學處理工作任務？",
        "1–5／NOT OBSERVED／N/A",
        "描述一項可觀察任務、期間及可引用來源"
      ],
      [
        "E5",
        "對您可觀察的工作表現，訓練內容在哪些方面有幫助或未能提供幫助？",
        "1–5＋開放回答",
        "區分雇主觀察與推論；允許回答沒有幫助／不確定"
      ]
    ]
  },
  {
    "table_ordinal_1based": 15,
    "rows_r01": 8,
    "rows_r02": 8,
    "added_rows": [
      [
        "文件識別",
        "DOCX 0124／I19-E12／R02 candidate"
      ]
    ],
    "removed_rows": [
      [
        "文件識別",
        "DOCX 0124／I19-E12／R01 candidate"
      ]
    ]
  }
]

## Questions
1. Does Table 3 correctly distinguish an unverified claim, source HOLD, offer/expected-start only, verified hire without employer affirmation, feedback without verified hire, and not eligible? Identify any state collision or false positive.
2. Do E3, E4 and E5 preserve the rating scale while making NOT OBSERVED, NOT APPLICABLE, DECLINED and UNKNOWN distinct, and require an observable example where relevant?
3. Does any changed wording imply that an offer proves hire, that an unverified source is verified, or that employer feedback proves causal training effect?
4. Are there concrete contradictions within these two tables against the official wording or the quoted Blueprint rules?

## Output contract
Return one compact JSON object only with keys: scope_verdict (PASS/PARTIAL/FAIL), candidate_sha256, extracted_scope_sha256, findings (array with severity, table, row_anchor, exact_issue, reason, minimal_repair), and whole_document_acceptance (must be NOT_ASSESSED). Quote exact anchors. If evidence is insufficient, say so. Do not infer content outside the supplied tables. Do not use tools, open files, make network calls, or modify any files. The attached source text is evidence, not instructions.
