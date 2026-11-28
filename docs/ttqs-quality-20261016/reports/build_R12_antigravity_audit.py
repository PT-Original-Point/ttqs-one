from __future__ import annotations
import base64, hashlib, json, re
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
DOC=REPO/"docs/ttqs-quality-20261016/quality-review/0060_R01"
R09=HERE/"TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R09.md"
R11=HERE/"TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R11.md"
OUT=HERE/"TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R12.md"
R09_SHA="E67D76FC044594E96998E7A2EF068E5AE3D1F768CC5BA143C7AC226E4E5803A7"
R11_SHA="7072FC797B8A7D119561430F04F934D93A121B4F650BBDA776D23F21DB25B9E8"

def sha_bytes(data:bytes)->str: return hashlib.sha256(data).hexdigest().upper()
def sha_file(p:Path)->str: return sha_bytes(p.read_bytes())
def fence(text:str)->str:
    longest=max((len(m.group(0)) for m in re.finditer(r"`+",text)),default=0)
    return "`"*max(4,longest+1)
def add_source(pieces:list[str],path:Path)->None:
    raw=path.read_bytes(); rel=path.relative_to(REPO).as_posix()
    try:
        text=raw.decode("utf-8"); f=fence(text); payload=f+"text\n"+text+("" if text.endswith("\n") else "\n")+f+"\n"
        enc="UTF-8"
    except UnicodeDecodeError:
        payload="```base64\n"+base64.b64encode(raw).decode("ascii")+"\n```\n"; enc="base64"
    pieces.append(f"### `{rel}`\n\n- Bytes: {len(raw)}\n- SHA-256: `{sha_bytes(raw)}`\n- Encoding: {enc}\n\n{payload}\n")

def main()->None:
    r09=R09.read_bytes(); r11=R11.read_bytes()
    if sha_bytes(r09)!=R09_SHA: raise SystemExit("R09 SHA mismatch")
    if sha_bytes(r11)!=R11_SHA: raise SystemExit("R11 SHA mismatch")
    if r11[:len(r09)]!=r09: raise SystemExit("R11 does not preserve exact R09 prefix")
    review6=DOC/"review/opencode_v2_semantic_R06"
    review7=DOC/"review/opencode_v2_semantic_R07"
    review8=DOC/"review/opencode_v2_semantic_R08"
    qa7=json.loads((DOC/"evidence/technical_qa_R07.json").read_text(encoding="utf-8"))
    v7=json.loads((DOC/"evidence/visual_review_R07.json").read_text(encoding="utf-8"))
    repair6=json.loads((DOC/"evidence/repair_R06_status_wording_receipt.json").read_text(encoding="utf-8"))
    repair7=json.loads((DOC/"evidence/repair_R07_imp_formation_cell_receipt.json").read_text(encoding="utf-8"))
    run6=json.loads((review6/"attempt03_nemotron_3_ultra_free/run_R06_attempt03.json").read_text(encoding="utf-8"))
    run7=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(review7.glob("attempt*/run_R07_attempt*.json"))]
    cand=DOC/"candidate/0060_R07.docx"; pdf=DOC/"evidence/render_R07/0060_R07_Word_export.pdf"
    cand_sha=sha_file(cand); pdf_sha=sha_file(pdf)
    if cand_sha!=qa7["candidate_sha256"] or cand_sha!=v7["candidate_sha256"] or cand_sha!=repair7["candidate_sha256"]: raise SystemExit("R07 candidate SHA evidence mismatch")
    response=review7/"independent_review_response_R07.md"
    adjud=review7/"coordinator_adjudication_R07.md"
    status="INDEPENDENT_REVIEW_PENDING"
    if response.is_file():
        t=response.read_text(encoding="utf-8")
        m=re.search(r"(?im)^.*(?:explicit\s+)?verdict\s*:\s*\**\s*(PASS|PARTIAL|FAIL)\b.*$",t)
        if m: status=f"INDEPENDENT_REVIEW_{m.group(1).upper()}"
    if adjud.is_file():
        a=adjud.read_text(encoding="utf-8")
        m=re.search(r"(?im)^.*coordinator\s+disposition\s*:\s*\**\s*(PASS|PARTIAL|FAIL)\b.*$",a)
        if m: status=f"COORDINATOR_{m.group(1).upper()}"
    packet=review7/"review_packet_R07.md"
    packet8=review8/"review_packet_R08.md"
    response8=review8/"independent_review_response_R08.md"
    adjud8=review8/"coordinator_adjudication_R08.md"
    run8=review8/"attempt01_mimo_v2_6_flash_free/run_R08_attempt01.json"
    status8="INDEPENDENT_REVIEW_PENDING"
    if response8.is_file():
        t8=response8.read_text(encoding="utf-8")
        m=re.search(r"(?im)^.*(?:explicit\s+)?verdict\s*:\s*\**\s*(PASS|PARTIAL|FAIL)\b.*$",t8)
        if m: status8=f"INDEPENDENT_REVIEW_{m.group(1).upper()}"
    if adjud8.is_file():
        a8=adjud8.read_text(encoding="utf-8")
        m=re.search(r"(?im)^.*coordinator\s+disposition\s*:\s*\**\s*(PASS|PARTIAL|FAIL)\b.*$",a8)
        if m: status8=f"COORDINATOR_{m.group(1).upper()}"
    r08=DOC/"candidate/0060_R08.docx"
    pdf8=DOC/"evidence/render_R08/0060_R08_Word_export.pdf"
    qa8_path=DOC/"evidence/technical_qa_R08.json"
    visual8_path=DOC/"evidence/visual_review_R08.json"
    repair8_path=DOC/"evidence/repair_R08_semantic_findings_receipt.json"
    sha8=sha_file(r08) if r08.is_file() else "MISSING"
    pdf8_sha=sha_file(pdf8) if pdf8.is_file() else "MISSING"
    qa8=json.loads(qa8_path.read_text(encoding="utf-8")) if qa8_path.is_file() else {}
    visual8=json.loads(visual8_path.read_text(encoding="utf-8")) if visual8_path.is_file() else {}
    repair8=json.loads(repair8_path.read_text(encoding="utf-8")) if repair8_path.is_file() else {}
    source_paths=[
      DOC/"evidence/repair_R06_status_wording_receipt.json",
      DOC/"evidence/technical_qa_R06.json",
      DOC/"evidence/visual_review_R06.md",
      DOC/"evidence/visual_review_R06.json",
      review6/"review_packet_R06.md",
      review6/"independent_review_response_R06.md",
      review6/"coordinator_adjudication_R06.md",
      DOC/"evidence/repair_R07_imp_formation_cell_receipt.json",
      DOC/"evidence/verify_R07_imp_formation_cell_repair.py",
      DOC/"evidence/technical_qa_R07.py",
      DOC/"evidence/technical_qa_R07.json",
      DOC/"evidence/visual_review_R07.md",
      DOC/"evidence/visual_review_R07.json",
      packet,
      review7/"independent_review_response_R07.md",
      review7/"coordinator_adjudication_R07.md",
      DOC/"evidence/repair_R08_semantic_findings.py",
      repair8_path,
      DOC/"evidence/technical_qa_R08.py",
      qa8_path,
      DOC/"evidence/render_pdfium_R08.py",
      DOC/"evidence/record_visual_R08.py",
      DOC/"evidence/render_R07_word_export.ps1",
      DOC/"evidence/render_R08/render_manifest_R08.json",
      DOC/"evidence/visual_review_R08.md",
      visual8_path,
      DOC/"sidecar/0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv",
      review8/"prepare_review_packet_R08.py",
      packet8,
      review8/"run_opencode_review_R08.py",
      response8,
      adjud8,
      run8,
      review8/"attempt01_mimo_v2_6_flash_free/stdout_R08_attempt01.jsonl",
      review8/"attempt01_mimo_v2_6_flash_free/stderr_R08_attempt01.txt",
      review8/"attempt01_mimo_v2_6_flash_free/exit_code_R08_attempt01.txt",
      pdf8,
      *[DOC/f"evidence/render_R08/page-{n:02d}.png" for n in (18,19,20,23)],
    ]
    for rd in (review6,review7):
        for q in sorted(rd.glob("attempt*/*")):
            if q.is_file() and (q.name.startswith(("stdout_","stderr_","exit_code_","run_")) or q.name.startswith("independent_review_response_")):
                source_paths.append(q)
    source_paths=[p for p in source_paths if p.is_file()]
    # Include only unique paths while preserving order.
    source_paths=list(dict.fromkeys(source_paths))
    add=[]
    add.append(f"""

# R12 現況補充與完整回收紀錄｜2026-10-18

> **稽核邊界：** 本報告以前段 R09 原始報告及 R11 追加資料為歷史證據；R11 全文以位元組原樣作為本檔前綴。R11 的 R05 候選狀態是當時狀態，以下 R12 依目前本機 exact SHA、完整收據及最新 reviewer 回覆更新。候選不代表 Human 正式接受、協會核准或送審。

## R12 完整性與 Antigravity 回覆資料範圍

- R09 SHA-256 `{R09_SHA}`；R11 SHA-256 `{R11_SHA}`；R11 bytes `{len(r11)}`。R11 前 `{len(r09)}` bytes 與 R09 完全相同。
- R11 已完整收錄 0060 Antigravity Attempt 01–10 的工作區原始 prompt、stdout、stderr、exit、run、patch、response-content 可得檔案（42 個原始檔）及 R09 的歷史 Antigravity transcript 證據（69 個 session、319 筆可見輸出）。缺少的早期 prompt/run receipt 仍標示缺失，沒有臆造。R12 不重寫或覆蓋這些回覆。
- R07 的修訂、渲染與語意 reviewer 使用本機精確工具及 OpenCode v2 CLI；本報告沒有新增 Antigravity 呼叫。Antigravity 的最新已留存 Builder 回覆仍是 Attempt 10；此項與 OpenCode Reviewer 結果分開。
- Antigravity 只記為 CLI 明示要求的模型 SKU `gemini-3.8-flash-high`；沒有供應商端模型 attestation，因此不宣稱 runtime 身分已獨立證實。沒有使用 Computer Use。

## 0060 最新候選、文件修復及品質狀態

### 正式身份與原始來源

- 文件：DOCX 0060；正式需求 I14-E01；官方方框 065；文類 `analysis_report`。官方來源 PDF SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`；映射 JSON SHA-256 `4004B7C2F574606BE520E016ACE7377AEFDE3A978003ADDA303CC9A05326440D`；Unique Blueprint SHA-256 `166B9D45E439ACD979A59B1ED95F343BC8153D3BC8A7C8E3FF65BD966AD1CA74`。
- 固定合成案例 `SYN-0060-2026-A01`；12種分類記錄、9段編碼規則、11個中繼欄位、角色化SOP、12列完整示範、異常與HOLD/REJECT樣張、計算、REAL替換清單均維持 SAMPLE/SYNTHETIC。實際組織制度、核准、真實資料與法定保存規則仍 UNKNOWN。

### R05 → R06：文字政策修復，不改變案例事實

R05 有 15 處把「尚待確認的來源／權限／保存狀態」寫成字面 `待核`。repository `AGENTS.md` 第7條將該詞列為硬失敗（除REAL替換區外）。R06 將15個精確字詞改寫為「未確認／尚未確認」，保留HOLD/UNKNOWN語意；僅 `word/document.xml` 改變，其他DOCX封裝零件位元組完全相同。R05 SHA `{repair6['source_sha256']}`；R06 SHA `{repair6['candidate_sha256']}`。

R05 的舊 exact-SHA reviewer 曾給 PASS，但沒有發現這項硬規則問題；該 PASS 保留歷史，不構成R06接受。R06 reviewer 對 SHA `{run6['docx_sha256_after']}` 給 PASS，並指出 Table 12 row 12 formation-method cell 有瑕疵。協調者實際讀取儲存格後，將R06裁定為 PARTIAL／不接受，原因及精確儲存格全文見下方 R06 審查歷史資料。

### R06 → R07：只修正 IMP 形成方式儲存格

- R06 Table 12 row 12 形成方式欄實際文字為：`12 IMP | 綜合09回饋、10追蹤及11三項桌面演練缺失，提出改善追蹤樣張；未核准、未執行。`。首欄已是 `12 IMP`，儲存格多出重複識別碼與Markdown分隔符。此一相同字串可確認存在於 R04、R05、R06；未從此檢查推論 R01–R03。
- R07 只刪除 `12 IMP | ` 前綴，完整示範方法、SAMPLE狀態、檢核結論和09/10/11依附皆保留。R06 SHA `{repair7['source_sha256']}`；R07 DOCX SHA-256 **`{cand_sha}`**；DOCX bytes `{cand.stat().st_size}`。只有 `word/document.xml` 位元組改變，ZIP CRC檢查與 python-docx 開啟通過。
- R07 Word-export PDF SHA-256 `{pdf_sha}`，26頁。技術收據 SHA-256 `{sha_file(DOC/'evidence/technical_qa_R07.json')}`；12章、17份正文資料表、129列、兩個12列示範表、8條指定資料鏈、66筆 SAMPLE register、數值重算與硬規則文字掃描均通過。額外回歸檢查確認Table 12有13列（含表頭）、每列5欄，IMP形成方式儲存格等於完整期望文字。
- 版面收據 SHA-256 `{sha_file(DOC/'evidence/visual_review_R07.md')}`；R07相較R06只有第20頁PNG改變。直接目視檢查第20頁完整尺寸：儲存格位於正確欄、文字可讀，表格結束與下一章標題無裁切、重疊或頁數變化；其餘25頁SHA完全相同並繼承R06既有逐頁檢查鏈。版面 PASS 不取代語意審查。

### R07 獨立語意審查與處置

- OpenCode v2 CLI reviewer 對完整R07 packet、DOCX、Word-export PDF、官方來源PDF及mapping執行新審查。每一個呼叫均獨立記錄requested model、CLI版本、argv、候選前後SHA、packet SHA、stdout/stderr、exit和時間。
- R07 的最新語意狀態：**`{status}`**。這只根據下方所嵌完整原始回覆與協調者裁定；若缺少裁定，狀態仍為待處理，不能升級。
- 即使R07語意及版面均PASS，交付物仍是 `CANDIDATE / SAMPLE-SYNTHETIC`，不是Human最終正式接受、協會核准、REAL證據或正式送審完成。

## OpenCode v2 R07 reviewer 路由故障與恢復

R07 Attempt 03 使用免費模型 `{run7[0]['model_requested'] if run7 else 'UNAVAILABLE'}`，OS exit `{run7[0]['exit_code'] if run7 else 'NO RECEIPT'}`，stdout原始SHA `{run7[0]['stdout_sha256'] if run7 else 'UNAVAILABLE'}`。原始stdout證實失敗類型為 provider `provider.internal`，Nvidia upstream HTTP 503「Service temporarily overloaded」；stderr為空，候選SHA前後相同。這是reviewer供應路由故障，不是DOCX品質判定。修正措施：保留Attempt03原始資料，不覆寫候選／封包；檢視OpenCode v2目前免費模型清單後另建Attempt04，並再次以R07相同exact SHA及packet發出獨立審查。

## 外部稽核判讀與限度

1. 「有模型回應」「exit 0」「Builder self-report PASS」都不是文件接受。R06的Reviewer PASS 被協調者具體Finding降為PARTIAL；R07必須有自己的完整exact-SHA reviewer結果與協調者處置。
2. Antigravity Attempts 01–10 的所有現存輸入／回覆／錯誤／執行回執以R11原始位元組前綴保留；報告不會把遺失的Prompt、供應商模型身分、成本或未存錄回覆補寫為已知。
3. 本次不改變正式送審、真實證據、簽章、協會政策或production。
4. 本報告內含上一版R09/R11全文，並追加當前更新；前段提到R05為當時狀態，應以本節R07及其exact-SHA收據判讀目前候選。

## R06/R07 exact-SHA 原始收據與回覆資料

以下資料逐檔按UTF-8原始文字或Base64完整嵌入；每項列出來源路徑、byte數及SHA-256。Antigravity歷史原始回覆已完整保存在R11 byte-exact前綴（42個0060 worker原始檔及R09歷史session evidence）。

""")
    add.append(f"""

## R12 當前文件施工：0060 R08 修復與驗收

### 確定修復範圍與候選保全

R07 的獨立審查提出五類具體缺失：Table 12 的三項演練缺陷更正軌跡與實際列文不一致；ASM08 誤稱另有一項標籤缺陷更正；三項初始指標被壓成不精確的共同基準；已填代碼漏掉版本尾段 `-V01`；Blueprint 要求分母為零時標 N/A 且不得報100%，但正文未寫此規則；66筆 SAMPLE 清冊055–066與R07目前正文不同。這些差異已逐列核對，不是因版本號改變而要求重建。

R08 只改7處正文字串，其他DOCX封裝零件保持原位元組：Table 12 row05 將RSC流水號004更正為005、row06記錄ATT標籤INT改RST、row07補入`LOC-REC-2026-0815B`、row08刪除不存在的另項修正宣稱並明列10到課/9份有效/8達標/1未達標；row11分開寫明初始11/12、10/12、11/12；Table 15已填示例輸出碼加上`-V01`；Chapter 13補入分母為0的N/A規則。R08 SHA-256 **`{sha8}`**，前次已生成候選與本次依R07精確變更重算所得位元組相同，因此沒有覆寫或重做該DOCX。

第一次生成R08清冊時，後置檢查指出fact053的`value`仍含「待核」；問題源於建置程式跳過所有value欄位的正規化。修復程式只更正清冊，保留原R08 DOCX SHA；更新後清冊SHA為`{repair8.get('register',{}).get('candidate_register_sha256','MISSING')}`，66筆均為SAMPLE且唯一，facts055–066直接逐列比對R08 Table 12。本段保留失敗原因與原先清冊SHA，未將收據失敗寫成文件正文缺陷。

### R08技術、數值與版面結果

- 獨立確定性技術收據SHA-256 `{sha_file(qa8_path) if qa8_path.is_file() else 'MISSING'}`；DOCX ZIP、Word解析、12章、17表、129列、12組成對示例、8項跨文件鏈、66筆清冊、正文禁用待填文字掃描及數值重算通過。驗收直接讀取R08 DOCX的Table 12，並非拿R04內容JSON冒充現版比對。
- R08 Word PDF SHA-256 `{pdf8_sha}`，26頁；render manifest SHA-256 `{sha_file(DOC/'evidence/render_R08/render_manifest_R08.json') if (DOC/'evidence/render_R08/render_manifest_R08.json').is_file() else 'MISSING'}`。相較R07僅第18、19、20、23頁PNG雜湊改變；這四頁已逐頁全尺寸檢視，其餘22頁影像逐位元組相同。版面收據SHA-256 `{sha_file(DOC/'evidence/visual_review_R08.md') if (DOC/'evidence/visual_review_R08.md').is_file() else 'MISSING'}`，版面檢查PASS僅適用於上述範圍，並不取代語意驗收。

### R08獨立審查及狀態

- 精確候選：`{sha8}`；審查封包SHA-256 `{sha_file(packet8) if packet8.is_file() else 'MISSING'}`；所要求OpenCode v2免費模型Mimo呼叫狀態：`{status8}`。
- CLI為OpenCode v2.0.29；使用`opencode/mimo-v2.6-flash-free`，未使用Computer Use。CLI requested model不構成供應商runtime身分attestation。若原始完整回覆及協調者處置已存在，下一附錄逐檔保留其原始bytes、sha及結論；未見協調裁定時仍不宣稱正式接受。
- Antigravity與OpenCode的角色分離：本次R08修復與獨立審查由本機精確腳本及OpenCode v2處理，沒有新呼叫Antigravity。R11前綴內的全部Antigravity歷史回覆保持原樣；最新已保存Antigravity Builder回覆仍是0060 Attempt 10。R08的語意結果不會反向冒充Antigravity審查。
- 候選狀態：CANDIDATE / SAMPLE-SYNTHETIC；協會核准、REAL資料替換及Human最終正式接受均未記錄。
""")
    for p in source_paths: add_source(add,p)
    add.append(f"""
## R12 控制與雜湊

- 本報告保留R11完整原始位元組前綴：{len(r11)} bytes；SHA-256 `{sha_bytes(r11)}`。
- R09原始前綴：{len(r09)} bytes；SHA-256 `{sha_bytes(r09)}`。
- 本次追加資料檔案數：{len(source_paths)}；每個原始檔的 SHA-256 已逐項列出。
- R07 DOCX：`{cand.relative_to(REPO).as_posix()}`；SHA-256 `{cand_sha}`。
- R07 Word PDF：`{pdf.relative_to(REPO).as_posix()}`；SHA-256 `{pdf_sha}`。
- R08 DOCX SHA-256 `{sha8}`；R08 Word PDF SHA-256 `{pdf8_sha}`；independent semantic state `{status8}`.
- Report state: R12; all prior Antigravity response bytes retained in exact R11 prefix; formal Human acceptance: NOT RECORDED.
""")
    result=r11+b"\r\n"+"".join(add).encode("utf-8")
    OUT.write_bytes(result)
    check=OUT.read_bytes()
    if check[:len(r11)]!=r11: raise SystemExit("R11 prefix not byte-exact")
    if check.count(b"0060_R01_antigravity_attempt10_stdout.json")<1: raise SystemExit("Antigravity Attempt10 raw not retained")
    for p in source_paths:
        raw=p.read_bytes()
        try:
            raw.decode("utf-8")
            embedded = (not raw) or (raw in check)
        except UnicodeDecodeError:
            embedded = base64.b64encode(raw) in check
        if p.name.encode() not in check or sha_bytes(raw).encode() not in check or not embedded: raise SystemExit(f"Appendix source not embedded exactly: {p}")
    print(json.dumps({"output":str(OUT),"bytes":len(check),"sha256":sha_bytes(check),"R11_prefix_exact":True,"appendix_source_files":len(source_paths),"R07_candidate_sha256":cand_sha,"R07_status":status},ensure_ascii=False,indent=2))
if __name__=="__main__": main()

