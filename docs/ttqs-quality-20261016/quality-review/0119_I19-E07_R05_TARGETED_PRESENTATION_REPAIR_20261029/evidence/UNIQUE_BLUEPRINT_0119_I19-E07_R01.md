# 0119 / I19-E07 專屬 Unique Blueprint R01

**狀態：SOURCE BLUEPRINT CANDIDATE；未代表協會正式核定。**

## 1. 身分與唯一用途

- doc_id `0119`；requirement_id `I19-E07`；官方文件名 `0119__目標市場及顧客價值部分提升證據分析表.docx`。
- 文類：雙構面證據分析表兼可重複填寫的核驗工作表；不是空白模板、單一市場調查、感謝函或滿意度報告。
- 主要讀者：小型訓練機構的訓練行政承辦人、資料整理者及第二位覆核者。實際任命／授權 UNKNOWN，正文只寫角色。
- 標題盲測：遮住標題後，仍能從雙構面指標定義、比較表、來源／分母核驗和保留規則辨認它在分析「市場與顧客價值是否均有部分提升」。

## 2. 官方與唯一 Mapping

- Official PDF `official_source_0108_r11.pdf` p.8，SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。官方 2 分常見佐證列出雙構面部分提升；此只說明參考佐證，不保證任何分數。
- 157 清單 ordinal 131，位於 I19-L2 / official p.8；PR #92 `03_157_CHECKBOX_BLUEPRINTS.md` blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`，文字為「市場價值部分提升：真實可驗的案例證據」。131 是候選清單序位，不是官方印刷 serial。
- `official_printed_checkbox_serial=UNKNOWN_NOT_ASSERTED`；doc 0119、I19-E07、seed row 119、crosswalk data row 106 均各自記錄，不互換。
- Crosswalk CSV SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`；I19-E07 row=`1/0/0119`。
- Seed CSV SHA-256 `280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0`；seed 119.
- PR #92 mission document blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` is candidate quality policy only; it prohibits inferring the association’s actual mission facts, audiences, programs or outcomes from filenames.

## 3. Required body and artifacts

1. Cover / quick-use panel with document identity, candidate state, sample boundary and “not formal acceptance” notice.
2. Official requirement locator and scope: separately explain target market and customer value; explain why both must have support; exclude score guarantees and causal overclaim.
3. Measurement protocol: define target group, observation window, collection channels, inclusion/exclusion, missingness, numerator, denominator, baseline and comparison period before interpreting results.
4. Paired evidence table with at least one measure per construct and fields for raw n/N, percentage, delta in percentage points, source locator, comparability, permission and reviewer status.
5. Full synthetic worked example using the source packet values: market-fit proxy 8/20=40.0% vs 12/25=48.0%, +8.0 pp; self-reported use-case value 10/16=62.5% vs 15/20=75.0%, +12.5 pp; response rates 16/20=80% and 20/25=80%. Clearly label every number and conclusion synthetic.
6. Interpretation matrix that yields `BOTH_PARTIAL_CANDIDATE`, `ONE_DIMENSION_ONLY`, `NO_COMPARABLE_BASELINE`, `UNKNOWN`, `DECLINE/NEGATIVE`, or `HOLD`; explain action and do not output score.
7. Evidence register with one row per metric/timepoint and source locator, data owner role, extracted numerator/denominator, exclusions, access permission, recalculation and second-check fields.
8. Limitations section: small n, nonresponse/self-selection, channel shifts, seasonality, changes in target definition; self-report is not skill/behavior/economic outcome; observation is not causal attribution.
9. Replacement register covering every synthetic field/value/period/indicator/interpretation and preventing partial realisation or sample residue.
10. Cross-document boundary section distinguishing 0118/I19-E05 original-letter custody, 0120/I19-E08 preliminary training outcome, 0117 exam outcomes and 0116 employment evidence.
11. Closeout checklist and conservative decision statement: data absent or incompatible -> HOLD/NOT_DEMONSTRATED; both supported -> human review only, no association approval implied.

## 4. Worked-example values and formulas (all synthetic)

- Market measure is a **target-group-fit share among valid inquiries**, not total market penetration: `eligible inquiries matching predeclared target-group definition / all valid inquiries in same channel and period`. Synthetic periods: 8/20 = 40.0%; 12/25 = 48.0%; difference = 48.0−40.0 = +8.0 percentage points.
- Customer-value measure is a self-report answer to one concrete usefulness prompt among valid responses: 10/16=62.5%; 15/20=75.0%; difference = +12.5 percentage points. Invite counts 20/20? More precisely baseline invited 20, valid replies 16, response rate 80%; comparison invited 25, replies 20, response rate 80%.
- Every value is fictional for method demonstration and has no association source, participant, real date, approval, letter, or actual outcome. Do not make a causal or formal achievement claim.

## 5. Required forms / rejection tests

A reviewer must be able to reproduce all percentages and percentage-point differences from displayed n/N; if not, FAIL. The two constructs may not share one undifferentiated “improvement” score. Missing baseline, denominator zero, changed population/channel without disclosure, unavailable source, unverified permission, selective omission of decline, or sample values left in a REAL record must force HOLD/NOT_DEMONSTRATED.

## 6. Negative neighbors and evidence ownership

- 0118/I19-E05 received-thank-you-letter custody is not a market/customer outcome.
- 0120/I19-E08 preliminary training outcomes may be referenced only through a traced same-case source, not substituted for market data.
- 0117/I19-E04 exam pass evidence and 0116/I19-E03 employment status are distinct indicators and cohorts.
- General market-demand survey requirements elsewhere in the 157 list concern needs/demand and are not automatically I19-E07 post-period improvement evidence.

## 7. Acceptance gates

- Source tuple exactly reconciles official page 8, doc_id, requirement ID, candidate list ordinal, seed row, and crosswalk row; no false printed serial.
- Genre and title-blind identity pass; both constructs have separate measures and complete comparable paired calculations.
- SAMPLE/SYNTHETIC is unmistakable and no real association outcome, approval, person or external source is fabricated.
- Every example value has replacement-register coverage; there is no missing source, formula, denominator, limitation or HOLD rule.
- Word renders and page-by-page visual QA pass on the exact final DOCX SHA; independent exact-SHA semantic review passes; GitHub raw bytes read back match. Formal acceptance remains NOT_GRANTED until Human/authorized association decision.