import sys,re,zipfile,hashlib,json,datetime
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import xml.etree.ElementTree as ET

mdp=Path(sys.argv[1]); docp=Path(sys.argv[2]); outp=Path(sys.argv[3])
md=mdp.read_text(encoding="utf-8-sig")
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; DC="http://purl.org/dc/elements/1.1/"
q=lambda x:"{%s}%s"%(W,x)
checks={}; issues=[]
try:
    with zipfile.ZipFile(docp) as z:
        checks["zip_integrity"]=z.testzip() is None
        parts={n:ET.fromstring(z.read(n)) for n in z.namelist() if n.endswith(".xml")}
        document=parts["word/document.xml"]; styles=parts["word/styles.xml"]
        core=parts["docProps/core.xml"]
except Exception as e:
    result={"status":"FAIL","exception":repr(e)}
    outp.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(2)

body=document.find(".//"+q("body")); direct=[]; tables=[]
for node in list(body):
    if node.tag==q("p"): direct.append("".join(t.text or "" for t in node.iter(q("t"))))
    elif node.tag==q("tbl"): tables.append(node)
alltext="\n".join(t.text or "" for t in document.iter(q("t")))
checks["candidate_bytes"]=docp.stat().st_size
checks["paragraph_count"]=len(direct); checks["table_count"]=len(tables)
checks["doc_id_requirement"]="0025" in alltext and "I04-E04" in alltext
checks["official_requirement_exact"]="訓練結果的評估、訓練實施的依據及標準化作業流程（SOP）。" in alltext
checks["official_systematic_item_scope"]="「系統性」構面" in alltext and "訓練品質管理系統系統化" not in alltext
checks["negative_neighbors_present"]="0024" in alltext and "0026" in alltext and "不複製正文" in alltext
checks["sample_real_boundary"]="SAMPLE／SYNTHETIC" in alltext and "不代表真實核准" in alltext and "不得據此公告" in alltext
checks["no_hard_placeholders"]=not re.search(r"待填|待核|空白表|保持空白|會後填寫|待 REAL 核准|待 R05 核准|待訂定|待授權替換",alltext)
checks["no_unconverted_latex"]=not re.search(r"\\(?:begin|frac|sum|text|left|right)\b|\\\(|\\\)|\$\$",alltext)
checks["no_cant_split_rows"]=not any(x.tag==q("cantSplit") for x in document.iter())
checks["first_heading_exact"]=direct[0]=="訓練評估與實施標準化作業程序SOP"
title_style=next((x for x in styles.findall("./"+q("style")) if x.attrib.get(q("styleId"))=="Title"),None)
title_size=title_style.find("./"+q("rPr")+"/"+q("sz")) if title_style is not None else None
checks["title_style_black"]=title_style is not None and (title_style.find("./"+q("rPr")+"/"+q("color")) is not None) and title_style.find("./"+q("rPr")+"/"+q("color")).attrib.get(q("val"))=="000000"
checks["title_style_min_pt"]=int(title_size.attrib.get(q("val")))/2 if title_size is not None else None
core_title=core.find("{%s}title"%DC)
checks["core_title_doc_id"]=core_title is not None and "0025" in (core_title.text or "")
def strip_md(s):
    s=re.sub(r"\*\*(.+?)\*\*",r"\1",s);s=re.sub(r"\*([^*]+)\*",r"\1",s)
    return s.replace(chr(96),"")
expected_paras=[]; expected_rows=[]
for raw in md.splitlines():
    s=raw.strip()
    if s.startswith("|") and s.endswith("|"):
        if re.match(r"^\|\s*:?-{3,}",s): continue
        expected_rows.append([strip_md(c.strip()) for c in s.strip("|").split("|")]); continue
    if not s or re.fullmatch(r"-{3,}",s): continue
    is_heading=bool(re.match(r"^#{1,6}\s+",s))
    s=re.sub(r"^#{1,6}\s+","",s)
    if not is_heading:
        s=re.sub(r"^[-*+]\s+","",s);s=re.sub(r"^\d+[.)]\s+","",s)
    s=re.sub(r"^>\s?","",s)
    expected_paras.append(strip_md(s))
actual_rows=[]
for tbl in tables:
    for tr in tbl.findall("./"+q("tr")):
        actual_rows.append(["".join(t.text or "" for t in tc.iter(q("t"))) for tc in tr.findall("./"+q("tc"))])
missing_paras=[s for s in expected_paras if s not in direct]
missing_rows=[r for r in expected_rows if r not in actual_rows]
checks["markdown_paragraphs_expected"]=len(expected_paras);checks["markdown_paragraphs_missing"]=len(missing_paras)
checks["markdown_table_rows_expected"]=len(expected_rows);checks["markdown_table_rows_missing"]=len(missing_rows)
run_sizes=[int(x.attrib.get(q("val"),"0")) for x in document.iter(q("sz"))]
table_sizes=[int(x.attrib.get(q("val"),"0")) for tbl in tables for x in tbl.iter(q("sz"))]
style_sizes={}
for st in styles.findall("./"+q("style")):
    sid=st.attrib.get(q("styleId")); sz=st.find("./"+q("rPr")+"/"+q("sz"))
    if sid and sz is not None: style_sizes[sid]=int(sz.attrib.get(q("val"),"0"))/2
checks["min_body_run_pt"]=min(run_sizes)/2 if run_sizes else None
checks["min_table_run_pt"]=min(table_sizes)/2 if table_sizes else None
checks["normal_style_pt"]=style_sizes.get("Normal")
checks["table_style_pt"]=style_sizes.get("TableText")
checks["font_floors_pass"]=style_sizes.get("Normal",0)>=10.5 and style_sizes.get("TableText",0)>=9.5 and (min(table_sizes)/2 if table_sizes else 0)>=9.5 and (min(run_sizes)/2 if run_sizes else 0)>=9.5
width_ok=True; table_cols=[]
for tbl in tables:
    pr=tbl.find("./"+q("tblPr")); tblw=pr.find("./"+q("tblW")) if pr is not None else None
    grid=tbl.find("./"+q("tblGrid"))
    total=sum(int(c.attrib.get(q("w"),"0")) for c in grid.findall("./"+q("gridCol"))) if grid is not None else 0
    expected=int(tblw.attrib.get(q("w"),"0")) if tblw is not None else 0
    width_ok=width_ok and total==expected
    table_cols.append(len(grid.findall("./"+q("gridCol"))) if grid is not None else 0)
checks["table_grid_widths_sum_to_table_width"]=width_ok
checks["max_table_columns"]=max(table_cols,default=0)
reg_match=re.search(r"### 14\.3 .*?\n(.*?)(?=\n### 14\.4)",md,re.S)
reg_rows=[]
if reg_match:
    for line in reg_match.group(1).splitlines():
        if re.match(r"^\|\s*\d+\s*\|",line):
            cells=[c.strip() for c in line.strip("|").split("|")]
            if len(cells)>=3: reg_rows.append((int(cells[0]),cells[1]))
checks["replacement_register_rows"]=len(reg_rows)
checks["replacement_register_sequential"]=([x[0] for x in reg_rows]==list(range(1,94)))
checks["replacement_fact_keys_unique"]=len({x[1] for x in reg_rows})==len(reg_rows)
checks["replacement_register_count_statement"]="（共 93 列；" in md
react=(Decimal(357)/Decimal(17*5)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
checks["reaction_average_recomputes"]=react==Decimal("4.20")
checks["behavior_rate_recomputes"]=(Decimal(10)/Decimal(18)*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("55.56")
checks["result_rate_recomputes"]=(Decimal(8)/Decimal(18)*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("44.44")
checks["scenario_fails_correct_thresholds"]="55.56%" in alltext and "未達 T-BEHAV" in alltext and "44.44%" in alltext and "未達 T-RESULT" in alltext and "通過 T-BEHAV（邊界）" not in alltext and "通過 T-RESULT（邊界）" not in alltext
checks["no_stale_scenario_values"]=not any(x in alltext for x in ["71.4 ÷ 17","11/18 完成 = 61.11%","9/18 達成 = 50.00%","E-05?"])
checks["all_tables_repeat_header"]=all(tbl.find("./"+q("tr")+"/"+q("trPr")+"/"+q("tblHeader")) is not None for tbl in tables)
critical=["zip_integrity","doc_id_requirement","official_requirement_exact","official_systematic_item_scope","negative_neighbors_present","sample_real_boundary","no_hard_placeholders","no_unconverted_latex","no_cant_split_rows","first_heading_exact","title_style_black","core_title_doc_id","font_floors_pass","table_grid_widths_sum_to_table_width","replacement_register_sequential","replacement_fact_keys_unique","replacement_register_count_statement","reaction_average_recomputes","behavior_rate_recomputes","result_rate_recomputes","scenario_fails_correct_thresholds","no_stale_scenario_values","all_tables_repeat_header"]
for key in critical:
    if checks.get(key) is not True: issues.append(key)
if checks["markdown_paragraphs_missing"]!=0: issues.append("markdown_paragraphs_missing")
if checks["markdown_table_rows_missing"]!=0: issues.append("markdown_table_rows_missing")
result={"status":"PASS" if not issues else "FAIL","work_id":"TTQS_ONE_0025_I04-E04_DETERMINISTIC_QA_R02_20261119","candidate_sha256":hashlib.sha256(docp.read_bytes()).hexdigest(),"manuscript_sha256":hashlib.sha256(mdp.read_bytes()).hexdigest(),"issues":issues,"checks":checks,"missing_paragraph_examples":missing_paras[:5],"missing_row_examples":missing_rows[:4],"scope":"OpenXML integrity, exact-source coverage, official requirement/title, font floors, table structure, placeholders, SAMPLE arithmetic and threshold adjudication; no semantic or visual pass implied","checked_at_local":datetime.datetime.now().astimezone().isoformat()}
outp.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(0 if not issues else 2)
