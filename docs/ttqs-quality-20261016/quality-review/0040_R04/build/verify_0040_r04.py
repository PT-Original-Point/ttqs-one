from pathlib import Path
from zipfile import ZipFile
import csv, hashlib, json, re, xml.etree.ElementTree as ET
from pypdf import PdfReader
from docx import Document

base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R04")
docx=base/"candidate"/"0040__訓練評估方法與成效指標對照表_R04.docx"
pdf=base/"render"/"0040_R04_final_word_export.pdf"
reg=base/"sources"/"0040_SOURCES_AND_SYNTHETIC_REPLACEMENT_REGISTER_R04.csv"
r03img=base/"render"/"baseline_r03_120dpi"
r04img=base/"render"/"final_pages"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda s:re.sub(r"[\W_]+","",s,flags=re.UNICODE).lower()
with ZipFile(docx) as z:
    corrupt=z.testzip()
    xmlparts=[n for n in z.namelist() if n.endswith(".xml")]
    xmlerrors=[]
    for n in xmlparts:
        try: ET.fromstring(z.read(n))
        except Exception as e: xmlerrors.append((n,str(e)))
d=Document(docx)
reader=PdfReader(str(pdf))
pages=[" ".join((p.extract_text() or "").split()) for p in reader.pages]
joined=" ".join(pages)
with reg.open("r",encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
ids=[r["fact_id"] for r in rows]
binding=all(r["bound_candidate_sha256"].lower()==sha(docx) for r in rows)
badloc=[r["fact_id"] for r in rows if not r["body_locator"].strip() or "§" in r["body_locator"]]
def has(page, token):
    return norm(token) in norm(pages[page-1])
checks={}
for i in range(1,9):
    checks[f"page_{i}_numbered"]=has(i,f"第 {i} 頁")
checks["case_id_printed"]=has(1,"SAMPLE-0039-01")
checks["official_mapping_printed"]=has(7,"0040 → I08-E03 → 官方 checkbox 040")
checks["official_source_sha_printed"]=has(7,"805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709")
checks["revision_R04_printed"]=has(7,"R04")
checks["not_approved_boundary_printed"]=has(7,"尚未核准")
checks["audit_index_printed"]=has(7,"內容查核索引") or has(8,"內容查核索引")
checks["pre_post_sample_vectors"]=all(has(4,t) for t in ["D01","D02","D03","D04","D05","17÷5","31÷5","14÷5","4÷5"])
checks["followup_row_printed"]=all(has(6,t) for t in ["D04","2026-06-19","示範期限","交接資料"])
checks["source_row_text_visible"]=has(1,"課程規劃會議紀錄展現訓練課程設計流程")
anchors={
"0040-REF-001":[(1,"官方要求"),(7,"官方映射")],
"0040-SYN-001":[(1,"SAMPLE-0039-01")],
"0040-SYN-002":[(1,"社區服務志工接待與活動引導")],
"0040-SYN-003":[(1,"示範資料日期"),(1,"2026-06-12")],
"0040-SYN-004":[(3,"K1"),(3,"K2"),(3,"K3"),(3,"K4")],
"0040-SYN-005":[(3,"0分：未達"),(3,"1分：部分達成"),(3,"2分：完整達成")],
"0040-SYN-006":[(3,"總分至少6分"),(3,"K3至少1分")],
"0040-SYN-007":[(1,"開課前做基線")],
"0040-SYN-008":[(1,"結訓前做後測")],
"0040-SYN-009":[(1,"30日追蹤另行核准")],
"0040-SYN-010":[(3,"評量角色"),(3,"評量覆核角色"),(5,"課程設計角色")],
"0040-SYN-BL-K1":[(3,"K1 開場與角色說明"),(3,"基線 1.0，差距 1.0")],
"0040-SYN-BL-K2":[(3,"K2 澄清與摘要確認"),(3,"基線 0.6，差距 1.4")],
"0040-SYN-BL-K3":[(3,"K3 同意與隱私界線"),(3,"基線 1.2，差距 0.8")],
"0040-SYN-BL-K4":[(3,"K4 收尾與交接"),(3,"基線 0.6，差距 1.4")],
}
for i in range(1,6):
    checks[f"pre_D{i:02d}"]=has(4,f"D{i:02d}") and has(4,["1/0/1/0","0/1/1/1","1/1/2/0","1/0/1/1","2/1/1/1"][i-1])
    checks[f"post_D{i:02d}"]=has(4,f"D{i:02d}") and has(4,["2/1/2/1","2/2/2/1","2/2/1/1","2/1/1/1","2/2/2/1"][i-1])
    anchors[f"0040-SYN-PRE-D{i:02d}"]=[(4,f"D{i:02d}"),(4,["1/0/1/0","0/1/1/1","1/1/2/0","1/0/1/1","2/1/1/1"][i-1])]
    anchors[f"0040-SYN-POST-D{i:02d}"]=[(4,f"D{i:02d}"),(4,["2/1/2/1","2/2/2/1","2/2/1/1","2/1/1/1","2/2/2/1"][i-1])]
anchors.update({
"0040-SYN-CALC-001":[(2,"4 ÷ 4＝100%")],
"0040-SYN-CALC-002":[(4,"平均前測"),(4,"17÷5"),(4,"3.4/8")],
"0040-SYN-CALC-003":[(4,"平均後測"),(4,"31÷5"),(4,"6.2/8")],
"0040-SYN-CALC-004":[(4,"配對平均變化"),(4,"14÷5"),(4,"2.8 分/8")],
"0040-SYN-CALC-005":[(4,"D01、D02、D03、D05"),(4,"D04")],
"0040-SYN-CALC-006":[(4,"後測達標率"),(4,"4÷5"),(4,"80%")],
"0040-SYN-CALC-007":[(4,"前測 K1–K4"),(4,"1.0/0.6/1.2/0.6")],
"0040-SYN-CALC-008":[(4,"後測 2.0/1.6/1.6/1.0")],
"0040-SYN-CALC-009":[(5,"後續行動（示範待辦）"),(6,"D04")],
"0040-SYN-034":[(6,"D04"),(6,"5/8"),(6,"低於 6/8")],
"0040-SYN-035":[(6,"訓練練習風險"),(6,"不是實際服務事件")],
"0040-SYN-036":[(6,"課程設計角色"),(6,"評量覆核角色")],
"0040-SYN-037":[(6,"2026-06-19"),(6,"SAMPLE 目標期限")],
"0040-SYN-038":[(6,"交接資料／結案規則"),(6,"總分至少 6/8"),(6,"K3 至少 1 分")]
})
for fid, items in anchors.items():
    checks["locator_anchor_"+fid]=all(has(pg,token) for pg,token in items)
font_sizes=[]
for part in xmlparts:
    if part=="word/document.xml":
        root=ET.fromstring(ZipFile(docx).read(part))
        ns={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        # Direct font sizes; tables and body are reported separately.
        body=root.find("w:body",ns)
        for child in list(body):
            is_table=child.tag.endswith("}tbl")
            for r in child.findall(".//w:r",ns):
                sz=r.find("./w:rPr/w:sz",ns)
                if sz is not None:
                    try: font_sizes.append((int(sz.attrib.get("{"+ns["w"]+"}val"))/2,is_table))
                    except Exception: pass
min_body=min((v for v,t in font_sizes if not t),default=None)
min_table=min((v for v,t in font_sizes if t),default=None)
image_equal={}
for n in range(2,7):
    a=base/"render"/"baseline_r03_120dpi"/f"page-{n}.png"
    b=base/"render"/"final_pages"/f"page-{n}.png"
    image_equal[str(n)]=a.is_file() and b.is_file() and sha(a)==sha(b)
report={
"project_id":"TTQS_ONE","doc_id":"0040","revision":"R04","mapping":"I08-E03 / official checkbox sequence 040",
"candidate_sha256":sha(docx),"register_sha256":sha(reg),"rendered_pdf_sha256":sha(pdf),"rendered_pages":len(reader.pages),
"docx_zip_integrity":"PASS" if corrupt is None else "FAIL","xml_parts":len(xmlparts),"xml_parse_errors":xmlerrors,
"table_count":len(d.tables),"register_rows":len(rows),"register_unique_fact_ids":len(set(ids)),"register_all_bound_to_candidate_sha":binding,
"register_unusable_section_markers":badloc,"register_rows_with_validated_printed_anchors":sum(1 for k in checks if k.startswith("locator_anchor_") and checks[k]),
"locator_anchor_checks":{k:v for k,v in checks.items() if k.startswith("locator_anchor_")},
"content_checks":{k:v for k,v in checks.items() if not k.startswith("locator_anchor_")},
"min_direct_body_font_pt":min_body,"min_direct_table_font_pt":min_table,
"r03_pages_2_to_6_r04_pixel_identical":image_equal,
"visual_scope":"Primary direct visual inspection of R04 pages 1,7,8; pages 2-6 verified byte-identical rendered PNGs against the reviewed R03 layout.",
"semantic_status":"PENDING_INDEPENDENT_EXACT_SHA_REVIEW","promotion_status":"NOT_PROMOTED","formal_acceptance":"NOT_GRANTED"
}
out=base/"qa"/"0040_technical_review_r04_exact.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
