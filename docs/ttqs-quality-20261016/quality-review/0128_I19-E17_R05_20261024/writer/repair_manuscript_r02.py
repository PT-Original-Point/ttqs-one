from pathlib import Path
from datetime import datetime
import hashlib, json, re

root = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024")
writer = root / "writer"
src = writer / "MANUSCRIPT_0128_I19-E17_R01.md"
dst = writer / "MANUSCRIPT_0128_I19-E17_R02.md"
if dst.exists():
    raise SystemExit("R02 already exists; inspect it before any rerun")
text = src.read_text(encoding="utf-8")

def replace_section(body, start, next_start, replacement):
    i = body.index(start)
    j = body.index(next_start, i + len(start))
    return body[:i] + replacement.strip() + "\n\n" + body[j:]

sec2 = r"""## 貳、作業路徑與績效指標資料字典

### 一、實際使用時的作業路徑

1. **確認工作任務與能力缺口。** 先從有權限的職務資料或訓練需求紀錄，寫明員工要完成的工作、目前落差及本次訓練要練習的能力。本頁示例只提供「資料欄位／程序核對能力缺口」與「報名資料首次核對正確率」；沒有提供真實需求紀錄。
2. **先定義量法，再收集前測。** 由有權責者在量測前核定工作任務、正確分子的判準、分母範圍、排除條件、資料期間、抽樣方式及合理樣本量。這些是實際執行前要確認的項目，不是本範例已完成的核定，也沒有統一官方數值門檻。
3. **記錄訓練和學習評量。** 連結課程計畫、出席資料及實作評量原件。本範例僅有課程代碼與技能示範分數；課程名稱、課程內容、時數、實際出席及原始測驗卷均為 `UNKNOWN_UNTIL_SOURCE`。
4. **使用同一工作定義收集訓後資料。** 訓後資料須按事前核定的期間及抽樣規則取得，保留來源定位及排除紀錄。示例期間與每期 20 件只是合成資料設定，不能當作協會已執行的抽樣或官方最低樣本數。
5. **檢查可比性並重算。** 對照任務、分子分母、工具版本、案件組成及工作環境；無法確認或校正的差異應標示並暫緩解讀。先合併分子與分母算整體率，再計算百分點差，不以六個百分率的簡單平均取代加權比率。
6. **作出描述性判讀並追蹤。** 先說清楚觀察到上升、持平或下降，再交代證據限制；不能單憑前後比較宣稱訓練造成結果。若資料未取得或不具可比性，維持 `HOLD`，並列出補件及下一個責任角色。

### 二、欄位與計算字典

| 欄位 | 定義及使用方式 | 本範例可確認的內容 |
| :--- | :--- | :--- |
| 工作指標 | 報名資料首次核對正確率；只描述指定工作任務，不代表整體工作表現。 | SAMPLE 情境。 |
| 正確分子 | 依事前核定判準，第一次核對即符合要求的案件數。需能回查逐件紀錄。 | 合成資料提供各案分子；沒有 REAL 原始紀錄。 |
| 分母 | 同期間納入相同任務的可比案件總數；排除規則及其理由須事前記錄。 | 每案每期 20 件是此 SAMPLE 的設定，非官方門檻。 |
| 比率 | 正確分子 ÷ 分母 × 100%。 | 六案前後比率可由合成分子分母重算。 |
| 百分點差 | 訓後百分率 − 訓前百分率。不得寫成相對成長百分率。 | 合併分子/分母計算；此處為 +6.6667 個百分點。 |
| 技能示範 | 課堂或練習中的學習表現，須與工作資料分欄呈現。 | 合成分數 33/60 至 48/60；不等於職場 KPI。 |
| 來源定位 | 使用經授權的系統紀錄、工作樣本或評量原件位置，保留版本及期間；公開稿僅留去識別化索引。 | `SAMPLE/SYS-LOG-*` 是示例代碼，並無真實系統日誌。 |
| 目標與樣本充分性 | 由具權責者在量測前，依工作任務、風險、資料量和取樣方法設定並留痕。 | 無統一官方及格門檻；本範例沒有核定門檻。 |

排除特殊任務、協作案件或系統異常案件時，應先訂出可重現規則，保留排除筆數與理由；不能看到結果後才選擇性剔除。實際抽樣方法、案件難度分層及核定角色均須由 REAL 來源確認，本範例不宣稱已採用隨機抽樣。"""

sec4 = r"""## 肆、S-EMP-01 完整計算示範

### 一、示例中可用的已知欄位

S-EMP-01 是虛構代碼，角色為 `SAMPLE_ROLE_COURSE_ADMIN`。資料只標示能力落差為「資料欄位／程序核對能力缺口」，工作任務為「報名資料首次核對正確率」，課程代碼為 `S-COURSE-01`。課程實際名稱、教材、時數、出席及學員身分均沒有 REAL 原件，不能補寫成已發生的事實。

### 二、工作 KPI 逐式重算

訓前 SAMPLE 期間為 2026-03-16 至 2026-04-14，首次核對正確 14 件、納入 20 件：

**訓前比率 = 14 ÷ 20 × 100% = 70.00%。**

訓後 SAMPLE 期間為 2026-05-16 至 2026-06-14，首次核對正確 18 件、納入 20 件：

**訓後比率 = 18 ÷ 20 × 100% = 90.00%。**

**前後百分點差 = 90.00% − 70.00% = +20.00 個百分點。** 這是合成資料中的描述性變化；沒有逐件 REAL 日誌，因此不能說真實工作績效已改善。

### 三、學習示範與工作成果分開

本案技能示範分數由 4/10 到 8/10，表示 SAMPLE 練習分數增加 4 分。該分數不是職場 KPI，也沒有提供題本、評分規準或正式測驗紀錄。示範工作 KPI 的變化是另一個資料欄位；兩者同時變化也不能證明因果。

### 四、解讀及建議後續

此示例只能說：在設定的合成數據中，工作指標由 70.00% 變成 90.00%。實際任務難度、工作量、流程版本、同期訓練、觀察者及原始紀錄均未查證。取得 REAL 原件前，應將結論維持 `SAMPLE_ONLY / REAL=UNKNOWN_UNTIL_SOURCE`。若實際資料也出現下降或缺漏，再由有權責者按第捌節流程判讀；本範例沒有記錄任何主管晤談、輔導或核定決議。"""

sec5 = r"""## 伍、個人訓練到工作成果的佐證鏈

每個節點都要連到可授權查閱的實際紀錄。下表只說明應蒐集的資料種類；除合成 CSV 中的數字外，沒有任何一項 REAL 原件在本範例中可供查證。

| 佐證節點 | 需要核對的內容 | 本範例狀態 |
| :--- | :--- | :--- |
| 需求與能力落差 | 工作任務、能力差距及訓練需求的核定紀錄。 | 只有 SAMPLE 情境文字；REAL=UNKNOWN。 |
| 課程與參訓 | 課程計畫、實際課程日期、出席與完成紀錄。 | 代碼及示例日期不等於實際課程或出席證據；REAL=UNKNOWN。 |
| 學習評量 | 題本、評分規準、原始答題或實作結果。 | 只有合成分數；原始評量件不存在於本範例。 |
| 訓前工作資料 | 指標定義、期間、分母、逐件工作樣本及來源系統。 | 僅有合成分子分母；`SAMPLE/SYS-LOG-*` 不是實際日誌。 |
| 訓後工作資料 | 同口徑期間、逐件結果、資料來源及排除清冊。 | 僅有合成分子分母；REAL=UNKNOWN。 |
| 覆核與觀察 | 覆核者被授權的角色、核對方法及可追溯紀錄。 | `SAMPLE_ONLY_NO_REAL_OBSERVER`；沒有主管觀察或簽核。 |
| 限制及結論 | 可比性、混雜因素、資料完整性及後續處理。 | 假設不得當作查證結果；REAL=UNKNOWN。 |
| 隱私及存取 | 處理依據、去識別化方式、代碼對照表的權限與保存期限。 | 僅為操作要求；沒有實際授權或存取紀錄。 |

取得原件後，正文只記必要的去識別化摘要、資料期間、版本和受權核實角色；身分對照表另置於有權限的位置，不放入公開候選。"""

sec6 = r"""## 陸、訓後 30、60、90 日追蹤

下列日期由 SAMPLE 課程日期 2026-04-15 推算，只示範如何排程；不是實際課程或追蹤紀錄。所有實際結果仍為 `UNKNOWN / NOT COLLECTED`。

| 節點 | SAMPLE 示範到期日 | 實際要收集的內容 | 判讀方式 | REAL 狀態 |
| :--- | :--- | :--- | :--- | :--- |
| T+30 日 | 2026-05-15 | 確認是否有工作應用樣本、流程障礙或需要的支持。 | 按事前核定的觀察方式記錄，不以單次訪談取代工作資料。 | UNKNOWN / NOT COLLECTED |
| T+60 日 | 2026-06-14 | 在可比任務上收集訓後工作 KPI 和來源定位。 | 按相同指標定義重算；缺來源或口徑改變則 HOLD。 | UNKNOWN / NOT COLLECTED |
| T+90 日 | 2026-07-14 | 檢查工作運用是否持續、是否有新干擾因素及後續需求。 | 記錄實際證據、限制、責任角色與下一期限。 | UNKNOWN / NOT COLLECTED |

本示例沒有提供任何 30／60／90 日觀察值，也沒有協會核定的目標值。實際目標、樣本充分性及介入方式應由有權責者在資料收集前核定；不能以本表日期或合成結果替代核准。"""

sec7 = r"""## 柒、資料品質與混雜因素檢查

在比較前後數據時逐項檢查。只要有重大差異未能排除或說明，就暫緩把變化解讀成可比較結果。以下檢查方法是操作建議；本範例沒有實際查核紀錄。

| 檢查項目 | 為何會影響比較 | 實際查核及處理方法 | 本範例查證狀態 |
| :--- | :--- | :--- | :--- |
| 任務及案件難度 | 後測較簡單可能抬高正確率；較困難則可能壓低。 | 對照任務類型與複雜度；差異不能校正時 HOLD。 | UNKNOWN_UNTIL_SOURCE；同質性只是 SAMPLE 假設。 |
| 工作量與人力 | 工作量、排班或協作改變會影響個人結果。 | 取得期間工作量與協助紀錄，分清個人與共同作業。 | UNKNOWN_UNTIL_SOURCE。 |
| 系統、表單及程序版本 | 防呆或欄位變更可能造成表面改善。 | 查版本及變更日期；有變更時分層比較或另建基線。 | UNKNOWN_UNTIL_SOURCE；沒有已查證版本。 |
| 旺淡季與案件組成 | 不同時段工作結構可能不同。 | 對照期間及案件組成，說明是否可比。 | UNKNOWN_UNTIL_SOURCE。 |
| 同期訓練或其他支持 | 其他介入可能同時影響結果。 | 查訓練及支持紀錄，不以未詢問代替證據。 | UNKNOWN_UNTIL_SOURCE。 |
| 抽樣偏差及遺漏 | 選件方式或遺漏可能改變分子分母。 | 保存事前抽樣規則、抽樣框、排除筆數及缺漏原因。 | UNKNOWN_UNTIL_SOURCE；方法未提供。 |
| 指標判準漂移 | 前後對「正確」的定義不同，比例不可直接相比。 | 使用同一版判準；如有修訂，逐項說明並重新計算。 | UNKNOWN_UNTIL_SOURCE。 |
| 覆核者偏差 | 覆核者知道受訓狀態可能影響判斷。 | 依權責安排覆核並保留角色、日期、判準及核實紀錄。 | UNKNOWN_UNTIL_SOURCE；本例無 REAL observer。 |
| 日誌完整性 | 缺漏或重複紀錄會改變分母。 | 與來源系統總量勾稽，保存差異及更正軌跡。 | UNKNOWN_UNTIL_SOURCE。 |
| 個資與授權 | 不當識別或分享會造成隱私風險。 | 確認處理依據、最小揭露、保存期限及存取權限。 | UNKNOWN_UNTIL_SOURCE。 |"""

sec8 = r"""## 捌、判讀流程與 HOLD／REJECT 條件

### 一、先檢查資料，再描述變化

1. **來源與授權。** 訓前、訓後資料及工作者身分須能由合法來源核對。缺原件、授權或去識別化依據時，標 `HOLD`，不得以 SAMPLE 取代 REAL。
2. **口徑與期間。** 確認任務、KPI 定義、分子、分母及期間一致。無法比較或排除重大變更時，先 `HOLD`，不能直接解讀增減。
3. **重算。** 對照逐件來源重算分子、分母、比率和百分點差。數字不一致時停止使用該結論，修正資料或計算後再核對。
4. **描述方向。** 資料可比時，百分點差大於零記為「觀察到上升」、等於零記為「觀察到持平」、小於零記為「觀察到下降」。這些是描述性分類，不代表統計顯著、官方及格、或因訓練造成。
5. **套用事前標準。** 若機構需要判斷是否達到內部目標，必須使用資料收集前由有權責者核定的目標及樣本充分性方法，記下來源與日期。本範例沒有這類核定，不設定固定百分比或筆數門檻。

### 二、後續處理

| 結果狀態 | 判定原則 | 建議下一步（須依實際權責核定） |
| :--- | :--- | :--- |
| 觀察到上升 | 同口徑資料重算後，訓後比率高於訓前。 | 查混雜因素並描述限制；不把全部變化歸因於訓練。 |
| 觀察到持平 | 同口徑資料重算後，前後相同；若有事前容忍區間，按核定規則判斷。 | 查是否有維持能力、工作環境障礙或指標敏感度問題。 |
| 觀察到下降 | 同口徑資料重算後，訓後比率低於訓前。 | 保留負向個案，核對原件及任務難度，再由有權角色決定支持措施。 |
| 證據不足／HOLD | 缺一方原件、身分或授權不明、口徑/期間不同、樣本不足以回答事前問題、追蹤未到或未收集，或重大混雜因素未釐清。 | 列出缺項、責任角色和可補正日期；補證前不下 REAL 成效結論。 |
| REJECT 資料 | 發現偽造原件/簽章、把 SAMPLE 冒充 REAL、隱藏指標定義改變、算式無法重現，或刪去負向個案。 | 隔離有問題的證據、保留更正軌跡；不得用該資料作正式佐證。REJECT 指資料，不是對人員下人事判決。 |

本表沒有設定「顯著改善」或統計檢定結論；未提供抽樣設計與統計假設，故不宣稱統計顯著性。樣例中的 S-EMP-03 下降 5 個百分點、S-EMP-06 持平，都必須留在比較表中。"""

text = replace_section(text, "## 捌、決策判讀樹與營運處置流程", "## 玖、", sec8)
text = replace_section(text, "## 柒、干擾變數與資料品質查核清單", "## 捌、", sec7)
text = replace_section(text, "## 陸、訓後 30 / 60 / 90 天長期追蹤機制表", "## 柒、", sec6)
text = replace_section(text, "## 伍、結構化佐證鏈結清單", "## 陸、", sec5)
text = replace_section(text, "## 肆、典型個案深度鑽研示範", "## 伍、", sec4)
text = replace_section(text, "## 貳、標準作業路徑與績效指標資料字典", "## 參、", sec2)

text = text.replace("（非通性問卷、非滿意度調查", "（非一般問卷、非滿意度調查")
text = text.replace("顯著改善（大幅超越基準）", "觀察到上升（+20.00 pp；SAMPLE）")
text = text.replace("穩定改善（達高標水平）", "觀察到上升（+10.00 pp；SAMPLE）")
text = text.replace("邊際改善（維持高水準）", "觀察到上升（+5.00 pp；SAMPLE）")
text = text.replace("明顯改善（脫離低標區）", "觀察到上升（+10.00 pp；SAMPLE）")
text = text.replace("整體平均淨改善 +6.6667 pp", "整體加權比率差 +6.6667 pp（SAMPLE）")
text = text.replace("展示真實營運環境中績效分化之常態，未經人為剔除或粉飾。", "展示合成案例中不同方向的變化；資料來源未提供抽樣方法，因此不宣稱真實營運型態或抽樣完整性。")
text = text.replace("**內部核定合格門檻：** ＿＿＿＿＿＿＿＿＿＿＿＿（核定主管核章：＿＿＿＿＿＿＿＿）", "**事前核定的內部目標（如適用）：** ＿＿＿＿＿＿＿＿＿＿＿＿（核定角色／日期／依據：＿＿＿＿＿＿＿＿）本欄不是官方通用門檻。")
text = text.replace("## 拾、真實資料替換查核清單（RR-01 至 RR-12 稽核對照表）", "## 拾、真實資料替換清單（RR-01 至 RR-12）")
text = text.replace("| 檢核編號 | 查核要項 (Check Item) | 正式所需佐證文件／資料源 | 驗證標準與合規要求 | 當前狀態 (Current Status) |", "| 檢核編號 | 查核要項 | 建議取得的真實資料來源 | 填表前需確認的內容 | 當前狀態 |")
text = text.replace("出席率須符合機構參訓及格規範", "依實際課程及機構適用規範核對出席情形；本範例未提供紀錄")
text = text.replace("抽樣時點符合訓後 30~60 天規範", "依事前核定的追蹤期間核對；本範例日期僅為 SAMPLE")
text = text.replace("完成簽署且代碼表單獨加密保存", "確認授權與代碼表分離保管的實際紀錄")
text = text.replace("載明明確分子分母與權責主管簽章", "載明分子分母、核定者角色與日期")
text = text.replace("具客觀給分標準，區隔於滿意度", "保留給分規準與原始結果，區隔於滿意度")
text = text.replace("具體待解決之工作任務缺口", "能連結到具體工作任務與能力落差")
text = text.replace("具完整時間戳記與初審紀錄筆數", "可追溯期間、逐件資料及初審紀錄")
text = text.replace("具可比性，抽樣代表性無偏差", "說明可比性、抽樣方法及已知偏差")
text = text.replace("非虛構角色，具同質業務覆核權限", "確認覆核者真實角色及其查核權限")
text = text.replace("查明評估期內無破壞可比性之變數", "記錄已查明的變數與未能排除的限制")
text = text.replace("公開版本無洩漏真實姓名或工號", "檢查公開版本的資料最小化與識別風險")
text = text.replace("經訓練主管與業務主管共同簽署", "依機構核定的責任與授權流程辦理")

[dst.parent.mkdir(parents=True, exist_ok=True)]
dst.write_text(text, encoding="utf-8", newline="")
sha = hashlib.sha256(dst.read_bytes()).hexdigest()
log = {
    "project_id": "TTQS_ONE", "work_id": "TTQS-0128-I19-E17-CODEX-BOUNDED-REPAIR-R02",
    "doc_id": "0128", "official_requirement_id": "I19-E17",
    "input_sha256": hashlib.sha256(src.read_bytes()).hexdigest(), "output_sha256": sha,
    "repair_scope": ["removed unsupported sample event/course/system/sampling assertions", "removed unsupported thresholds and significance language", "set unverified REAL evidence states to UNKNOWN_UNTIL_SOURCE", "replaced decision rules with descriptive sign-based classifications and source/ comparability HOLD checks", "retained all six supplied sample rows and arithmetic", "kept REAL blank form distinctly labeled"],
    "result": "TARGETED_REPAIR_APPLIED_NOT_INDEPENDENTLY_ACCEPTED",
    "performed_at_local": datetime.now().astimezone().isoformat(),
    "remaining_review": ["semantic reviewer exact DOCX SHA", "DOCX technical package", "Word render and every-page visual inspection", "public GitHub raw-byte readback"]
}
log_path = writer / "CODEX_BOUNDED_REPAIR_0128_R02.json"
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"manuscript": str(dst), "sha256": sha, "bytes": len(text.encode("utf-8")), "repair_log": str(log_path), "repair_log_sha256": hashlib.sha256(log_path.read_bytes()).hexdigest(), "sections": len(re.findall(r"^## ", text, re.M))}, ensure_ascii=False))
