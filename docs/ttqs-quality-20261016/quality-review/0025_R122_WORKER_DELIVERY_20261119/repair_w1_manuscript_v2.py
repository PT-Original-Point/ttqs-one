import sys, hashlib, json, datetime
from pathlib import Path
src=Path(sys.argv[1]); out=Path(sys.argv[2]); rec=Path(sys.argv[3])
raw=src.read_bytes(); text=raw.decode("utf-8-sig")
before=hashlib.sha256(raw).hexdigest(); changes=[]
def replace_exact(old,new,label,expected=1):
    global text
    n=text.count(old)
    if n!=expected: raise SystemExit(f"{label}: expected {expected} occurrences, got {n}")
    text=text.replace(old,new)
    changes.append({"change":label,"occurrences":n})
replace_exact("# 訓練評估與實施標準化作業程序（SOP）","# 訓練評估與實施標準化作業程序SOP","exact_blueprint_title")
replace_exact("**適用評核指標：** TTQS 訓練品質管理系統，內涵說明第 4 項「訓練品質管理系統系統化」之子項。","**適用評核指標：** 官方查核佐證表第 2 頁 I04-E04「系統性」構面：訓練結果的評估、訓練實施的依據及標準化作業流程（SOP）。","official_scope_wording")
replace_exact("**決策門檻（Decision Threshold）** | 觸發分支判斷之數值或條件；本程序所有門檻均為 SAMPLE 參數，待授權替換。","**決策門檻（Decision Threshold）** | 觸發分支判斷之數值或條件；本程序門檻均為 SAMPLE 示範值，正式使用前須由有權角色確認。","definition_no_pending_placeholder")
replace_exact("### 8.1 決策門檻（SAMPLE 參數，待授權替換）","### 8.1 決策門檻（SAMPLE 示範參數）","threshold_heading")
replace_exact("| T-REACT | 反應評估 | 平均滿意度 ≥ 80%（4.0/5.0） | Σ滿意度分數 ÷ 有效問卷數 |","| T-REACT | 反應評估 | 平均滿意度 ≥ 80%（4.0/5.0） | 所有有效作答題目分數總和 ÷（有效問卷數 × 題目數） |","reaction_formula_gate")
replace_exact("| 反應平均分 | 小數 | 是 | 1~5 |","| 反應題目數 | 整數 | 是 | SAMPLE |\n| 各題分數總和（Q1~Q5） | 五個整數 | 是 | SAMPLE；各題總分須可回算至原始答題數 |\n| 反應分數總計 | 整數 | 是 | 各題分數總和 |\n| 反應平均分 | 小數 | 是 | 分數總計 ÷（有效問卷數 × 題目數），範圍 1~5 |","reaction_form_fields")
replace_exact("| 反應平均分 | 4.20（SAMPLE） |","| 反應題目數 | 5（SAMPLE） |\n| 各題分數總和（Q1~Q5） | Q1=70；Q2=72；Q3=73；Q4=71；Q5=71（SAMPLE） |\n| 反應分數總計 | 357（SAMPLE） |\n| 反應平均分 | 4.20（357 ÷（17 × 5）=4.20；SAMPLE） |","reaction_example_reconciled")
replace_exact("| 行為完成人數 | 11（SAMPLE） |","| 行為完成人數 | 10（SAMPLE） |","behavior_example_count")
replace_exact("| 成果達成人數 | 9（SAMPLE） |","| 成果達成人數 | 8（SAMPLE） |","result_example_count")
replace_exact("| 綜合判定 | 部分符合（行為、成果未達標）（SAMPLE） |","| 綜合判定 | 部分符合（行為、成果未達標；2/4 層次未通過）（SAMPLE） |","overall_example_result")
replace_exact("| S07 | 行為評估：11/18 完成 = 61.11% | 通過 T-BEHAV（邊界） |","| S07 | 行為評估：10/18 完成 = 55.56% | 未達 T-BEHAV，登錄 E-07 並擬定輔導（SAMPLE） |","scenario_behavior_decision")
replace_exact("| S08 | 成果評估：9/18 達成 = 50.00% | 通過 T-RESULT（邊界） |","| S08 | 成果評估：8/18 達成 = 44.44% | 未達 T-RESULT，登錄 E-08 並升級 R05（SAMPLE） |","scenario_result_decision")
replace_exact("| S09 | R01 草擬報告，R03 核准（2026-09-25 SAMPLE） | 綜合判定「部分符合」 |","| S09 | R01 草擬報告，R03 核准（2026-09-25 SAMPLE） | 綜合判定「部分符合」（2/4 層次未通過） |","scenario_consolidated_decision")
replace_exact("| S10 | 登錄例外 E-05? 否（反應通過）；E-07/E-08 邊界，登錄觀察項 | 登錄 R-0025-S10 |","| S10 | 登錄 E-07（行為未達標）與 E-08（成果未達標）；依升級路徑分別交 R03、R05 處理 | 完成 R-0025-S10 |","scenario_exception_logic")
replace_exact("| 例外／矯正紀錄 | 部分（觀察項） | R-0025-EX-2026-001 |","| 例外／矯正紀錄 | 是（登錄 E-07、E-08） | R-0025-EX-2026-001 |","scenario_exception_output")
replace_exact("| 反應平均 | Σ分數 ÷ 有效問卷數 | 71.4 ÷ 17 | 4.20 |","| 反應平均 | 各題分數總和 ÷（有效問卷數 × 題目數） | 357 ÷（17 × 5） | 4.20 |","reaction_calc_row")
replace_exact("| 行為完成率 | 完成人數 ÷ 追蹤人數 | 11 ÷ 18 | 61.11% |","| 行為完成率 | 完成人數 ÷ 追蹤人數 | 10 ÷ 18 | 55.56% |","behavior_calc_row")
replace_exact("| 成果達成率 | 達成人數 ÷ 追蹤人數 | 9 ÷ 18 | 50.00% |","| 成果達成率 | 達成人數 ÷ 追蹤人數 | 8 ÷ 18 | 44.44% |","result_calc_row")
replace_exact("註：Σ分數 71.4 為 17 份問卷加總（SAMPLE）；四捨五入至小數第 2 位。","註：Q1~Q5 的 SAMPLE 總分依序為 70、72、73、71、71，合計 357；17 份有效問卷 × 5 題 = 85 個作答，357 ÷ 85 = 4.20。平均以小數第 2 位四捨五入。","reaction_calc_note")
replace_exact("| 40 | SCENARIO_REACT_SUM | 71.4 | §11.4 | 合成情境 | 真實問卷加總 | R01 |","| 40 | SCENARIO_REACT_RAW_TOTAL | 357 | §9.3、§11.4 | 合成情境 | 真實問卷各題原始分數 | R01 |","register_reaction_total")
replace_exact("| 44 | SCENARIO_BEHAV_DONE | 11 人 | §9.3、§11.2、§11.4 | 合成情境 | 真實完成人數 | R01 |","| 44 | SCENARIO_BEHAV_DONE | 10 人 | §9.3、§11.2、§11.4 | 合成情境 | 真實完成人數 | R01 |","register_behavior_count")
replace_exact("| 45 | SCENARIO_BEHAV_RATE | 61.11% | §9.3、§11.2、§11.4 | 合成情境 | 真實計算結果 | R01 |","| 45 | SCENARIO_BEHAV_RATE | 55.56% | §9.3、§11.2、§11.4 | 合成情境 | 真實計算結果 | R01 |","register_behavior_rate")
replace_exact("| 47 | SCENARIO_RESULT_DONE | 9 人 | §9.3、§11.2、§11.4 | 合成情境 | 真實達成人數 | R02 |","| 47 | SCENARIO_RESULT_DONE | 8 人 | §9.3、§11.2、§11.4 | 合成情境 | 真實達成人數 | R02 |","register_result_count")
replace_exact("| 48 | SCENARIO_RESULT_RATE | 50.00% | §9.3、§11.2、§11.4 | 合成情境 | 真實計算結果 | R01 |","| 48 | SCENARIO_RESULT_RATE | 44.44% | §9.3、§11.2、§11.4 | 合成情境 | 真實計算結果 | R01 |","register_result_rate")
replace_exact("| 8 | ROLE_R05 | 高階主管（代碼 R05） | §5.1 | 角色 | 真實職稱與人員名冊 | R05 |","| 8 | ROLE_R05 | 高階主管（代碼 R05） | §5.1、§17 | 角色 | 真實職稱與人員名冊 | R05 |","register_role_location")
replace_exact("| 生效日 | 待 REAL 核准後訂定 |","| 生效日 | 2026-12-01（SAMPLE 示範值；非實際生效日） |","document_control_effective_date")
replace_exact("| 核准者 | 待 R05 核准（REAL） |","| 核准者 | R05 角色（SAMPLE 欄位示例；不代表真實核准） |","document_control_approver_sample")
replace_exact("| 下次檢討日 | 待訂定 |","| 下次檢討日 | 2027-03-01（SAMPLE 示範值；非實際排定日期） |\n\n以上日期與角色僅示範文件欄位；本候選未經實際核准，不得據此公告或作為生效依據。","document_control_review_date_and_disclaimer")
extra=[
"| 86 | SCENARIO_REACT_ITEM_COUNT | 5 題 | §9.3、§11.4 | 合成問卷結構 | 真實問卷題目數及題目清單 | R01 |",
"| 87 | SCENARIO_REACT_Q1_SUM | 70 | §9.3、§11.4 | 合成問卷總分 | 真實 Q1 作答總分 | R01 |",
"| 88 | SCENARIO_REACT_Q2_SUM | 72 | §9.3、§11.4 | 合成問卷總分 | 真實 Q2 作答總分 | R01 |",
"| 89 | SCENARIO_REACT_Q3_SUM | 73 | §9.3、§11.4 | 合成問卷總分 | 真實 Q3 作答總分 | R01 |",
"| 90 | SCENARIO_REACT_Q4_SUM | 71 | §9.3、§11.4 | 合成問卷總分 | 真實 Q4 作答總分 | R01 |",
"| 91 | SCENARIO_REACT_Q5_SUM | 71 | §9.3、§11.4 | 合成問卷總分 | 真實 Q5 作答總分 | R01 |",
"| 92 | DOC_EFFECTIVE_DATE_SAMPLE | 2026-12-01 | §17 | 文件控制示例 | REAL 核准生效日期及核准紀錄 | R05 |",
"| 93 | DOC_NEXT_REVIEW_DATE_SAMPLE | 2027-03-01 | §17 | 文件控制示例 | REAL 檢討週期與排定日期 | R03 |"
]
replace_exact("（共 85 列；替換時須逐列更新並保留本表。）","\n".join(extra)+"\n\n（共 93 列；替換時須逐列更新並保留本表。）","replacement_register_expanded")
replace_exact("（共 93 列；替換時須逐列更新並保留本表。）","（共 93 列；替換時須逐列更新並保留本表。）","register_count_marker")
fence=chr(96)*3
decision_start=text.index(fence,text.index("### 8.2"))
decision_end=text.index(fence,decision_start+len(fence))+len(fence)
decision_old=text[decision_start:decision_end]
decision_new="\n".join([
"**起點：** 取得完整評估數據。",
"",
"- 反應達到 T-REACT：記錄通過。未達門檻：登錄 E-05 並升級 R03。",
"- 學習達到 T-LEARN：記錄通過。未達門檻：登錄 E-06，擬定重訓或修課計畫。",
"- 行為達到 T-BEHAV：記錄通過。未達門檻：登錄 E-07，擬定輔導計畫。",
"- 成果達到 T-RESULT：記錄通過。未達門檻：登錄 E-08 並升級 R05。",
"",
"**綜合判定：**",
"",
"- 四項全通過：評估結論為「符合」，建議延續。",
"- 1 至 2 項未通過：評估結論為「部分符合」，擬定改善計畫。",
"- 3 至 4 項未通過：評估結論為「不符合」，升級 R05 並啟動矯正。"
])
replace_exact(decision_old,decision_new,"decision_tree_for_word_readability")
for bad in ["71.4","11/18 完成","9/18 達成","61.11%","50.00%","E-05?","待 REAL 核准","待 R05 核准","待訂定","待授權替換","待填","待核","空白表","保持空白","會後填寫"]:
    if bad in text: raise SystemExit("remaining defect: "+bad)
if "（共 93 列；" not in text: raise SystemExit("register count marker missing")
out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text,encoding="utf-8",newline="\n")
after=hashlib.sha256(out.read_bytes()).hexdigest()
result={"status":"SCOPED_REPAIR_APPLIED","source_path":str(src),"source_sha256":before,"derived_path":str(out),"derived_sha256":after,"source_bytes":len(raw),"derived_bytes":out.stat().st_size,"changes":changes,"replacement_register_rows":93,"reaction_mean_check":{"item_sums":[70,72,73,71,71],"raw_total":357,"valid_questionnaires":17,"item_count":5,"denominator":85,"mean":357/85},"behavior_rate":round(10/18*100,2),"result_rate":round(8/18*100,2),"performed_at_local":datetime.datetime.now().astimezone().isoformat()}
rec.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
