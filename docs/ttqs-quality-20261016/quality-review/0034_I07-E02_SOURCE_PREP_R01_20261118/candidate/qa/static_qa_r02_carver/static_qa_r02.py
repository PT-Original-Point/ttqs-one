"""Read-only, standard-library static QA for TTQS ONE 0034 R02.
Reads only the named candidate, R02 scoped-repair source, source packet,
Blueprint, and R02 build receipt. Emits one JSON object to stdout; writes nothing.
"""
import hashlib, json, re, zipfile
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import xml.etree.ElementTree as ET

BASE=Path(r"E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0034_I07-E02_SOURCE_PREP_R01_20261118")
CAND=BASE/"candidate"/"0034_I07-E02_R02_RAWLS_SCOPED_REPAIR.docx"
BUILD=BASE/"candidate"/"qa"/"build_r02"/"BUILD_RECEIPT_0034_I07-E02_R02.json"
PACKET=BASE/"SOURCE_PACKET_0034_I07-E02_R01.md"
BLUEPRINT=BASE/"UNIQUE_BLUEPRINT_0034_I07-E02_R01.md"
EXPECTED_CAND="A743BE3A26EF3C9D241CEDDD5147402714E96D31C640B7D8CA3DEE56F0213336"
NS={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel":"http://schemas.openxmlformats.org/package/2006/relationships"}
W="{"+NS["w"]+"}"
ID_RE=re.compile(r"(?<![A-Za-z0-9_-])SYN-0034-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?![A-Za-z0-9_-])")
FILL_RE=re.compile(r"^(?:待填|待核|待補|待確認|待填寫|會後填寫|空白|TBD|TODO|N/?A|_{3,}|…+|\.\.\.)$",re.I)
GENERIC_RE=re.compile(r"^(?:待補充|見附件|詳如另冊|相關資料|依實際情況|依需要|同上|TBD|TODO|N/?A)$",re.I)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest().upper()
def tx(el):return "".join(x.text or "" for x in el.iter(W+"t"))
def status(ok):return "PASS" if ok else "FAIL"
def normalized(s):return re.sub(r"\s+","",s)
def md_table_shapes(source):
    groups=[]; cur=[]
    for line in source.splitlines():
        if line.strip().startswith("|") and line.strip().endswith("|"):
            cur.append(line)
        elif cur:
            groups.append(cur);cur=[]
    if cur:groups.append(cur)
    shapes=[]
    for g in groups:
        rows=[]
        for line in g:
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?",c or "-") for c in cells):continue
            rows.append(cells)
        shapes.append({"row_count_including_header":len(rows),"column_counts":[len(x) for x in rows]})
    return shapes
def run_sizes(p, base, loc, out):
    for ri,r in enumerate(p.findall(".//w:r",NS),1):
        if not tx(r).strip():continue
        rp=r.find("w:rPr",NS);sz=rp.find("w:sz",NS) if rp is not None else None
        if sz is None and rp is not None:sz=rp.find("w:szCs",NS)
        pt=Decimal(sz.get(W+"val"))/2 if sz is not None and sz.get(W+"val") else base
        if pt is None:out["unresolved"].append({"location":loc,"run":ri,"text":tx(r)[:90]})
        else:out["sizes"].append(float(pt))

def main():
    started=datetime.now(timezone.utc).isoformat()
    before=sha(CAND); build=json.loads(BUILD.read_text(encoding="utf-8"))
    packet=PACKET.read_text(encoding="utf-8"); blueprint=BLUEPRINT.read_text(encoding="utf-8")
    repair_path=Path(build["content_source"]["path"]); repair=repair_path.read_text(encoding="utf-8")
    bindings={"candidate":{"path":str(CAND),"expected_sha256":EXPECTED_CAND,"sha256_before":before},
      "source_packet":{"path":str(PACKET),"sha256":sha(PACKET),"build_receipt_expected_sha256":build["inputs"]["source_packet"]["sha256"]},
      "blueprint":{"path":str(BLUEPRINT),"sha256":sha(BLUEPRINT),"build_receipt_expected_sha256":build["inputs"]["unique_blueprint"]["sha256"]},
      "r02_scoped_repair":{"path":str(repair_path),"sha256":sha(repair_path),"build_receipt_expected_sha256":build["content_source"]["sha256"]},
      "build_receipt":{"path":str(BUILD),"sha256":sha(BUILD),"candidate_sha256":build["output"]["sha256"]}}
    gates={}
    gates["candidate_exact_sha_matches_request_and_build_receipt"]=status(before==EXPECTED_CAND and build["output"]["sha256"].upper()==EXPECTED_CAND)
    gates["source_packet_sha_matches_build_binding"]=status(bindings["source_packet"]["sha256"]==bindings["source_packet"]["build_receipt_expected_sha256"])
    gates["blueprint_sha_matches_build_binding"]=status(bindings["blueprint"]["sha256"]==bindings["blueprint"]["build_receipt_expected_sha256"])
    gates["repair_source_sha_matches_build_binding"]=status(bindings["r02_scoped_repair"]["sha256"]==bindings["r02_scoped_repair"]["build_receipt_expected_sha256"])
    gates["build_receipt_doc_requirement_scope"]=status(build.get("doc_id")=="0034" and build.get("requirement_id")=="I07-E02" and build.get("revision")=="R02")

    with zipfile.ZipFile(CAND) as z:
        bad=z.testzip(); names=set(z.namelist()); missing=sorted({"[Content_Types].xml","word/document.xml","word/styles.xml"}-names)
        parts={};xml_errors=[]
        for name in sorted(names):
            if name.endswith((".xml",".rels")):
                try:parts[name]=ET.fromstring(z.read(name))
                except Exception as e:xml_errors.append({"part":name,"error":str(e)})
        doc=parts.get("word/document.xml")
        if doc is None:raise RuntimeError("word/document.xml is absent or unparsable")
        gates["ooxml_zip_and_all_xml_parts_open"]=status(bad is None and not missing and not xml_errors)
        body=doc.find("w:body",NS); seq=[]; paragraphs=[];table_nodes=[]
        for x in list(body):
            if x.tag==W+"p":paragraphs.append(x);seq.append(("p",x))
            elif x.tag==W+"tbl":table_nodes.append(x);seq.append(("tbl",x))
        tables=[];table_text=[];empty_cells=[];empty_rows=[];empty_cell_paras=[]
        for ti,t in enumerate(table_nodes,1):
            rows=[]
            for ri,row in enumerate(t.findall("w:tr",NS),1):
                cells=[]
                for ci,cell in enumerate(row.findall("w:tc",NS),1):
                    ps=cell.findall(".//w:p",NS); parts_text=[]
                    for pi,p in enumerate(ps,1):
                        val=tx(p);parts_text.append(val)
                        if not val.strip():empty_cell_paras.append(f"table{ti}/r{ri}/c{ci}/p{pi}")
                    val="".join(parts_text);cells.append(val)
                    if not val.strip():empty_cells.append(f"table{ti}/r{ri}/c{ci}")
                rows.append(cells)
                if not "".join(cells).strip():empty_rows.append(f"table{ti}/r{ri}")
            tables.append(rows);table_text.append("\n".join("\t".join(r) for r in rows))
        ordered=[]
        for kind,x in seq:
            ordered.append(tx(x) if kind=="p" else table_text[table_nodes.index(x)])
        whole="\n".join(ordered);para_text="\n".join(tx(p) for p in paragraphs)

        # Size each nonempty body/table run, resolving paragraph style/default only when necessary.
        sr=parts.get("word/styles.xml");styles={};default=None
        if sr is not None:
            d=sr.find("w:docDefaults/w:rPrDefault/w:rPr/w:sz",NS)
            if d is not None and d.get(W+"val"):default=Decimal(d.get(W+"val"))/2
            for s in sr.findall("w:style",NS):
                sid=s.get(W+"styleId");based=s.find("w:basedOn",NS);sz=s.find("w:rPr/w:sz",NS)
                styles[sid]={"based":based.get(W+"val") if based is not None else None,
                    "pt":Decimal(sz.get(W+"val"))/2 if sz is not None and sz.get(W+"val") else None}
        def inherited(sid,seen=None):
            seen=seen or set()
            if not sid or sid in seen or sid not in styles:return None
            seen.add(sid);o=styles[sid]
            return o["pt"] if o["pt"] is not None else inherited(o["based"],seen)
        fs={"body":{"sizes":[],"unresolved":[],"empty_paragraphs":[]},"tables":{"sizes":[],"unresolved":[]}}
        for pi,p in enumerate(paragraphs,1):
            if not tx(p).strip():fs["body"]["empty_paragraphs"].append(f"body/p{pi}")
            pp=p.find("w:pPr",NS);ps=pp.find("w:pStyle",NS) if pp is not None else None
            psize=pp.find("w:rPr/w:sz",NS) if pp is not None else None
            base=(Decimal(psize.get(W+"val"))/2 if psize is not None and psize.get(W+"val") else inherited(ps.get(W+"val") if ps is not None else None)) or default
            run_sizes(p,base,f"body/p{pi}",fs["body"])
        for ti,t in enumerate(table_nodes,1):
            for ri,row in enumerate(t.findall("w:tr",NS),1):
                for ci,cell in enumerate(row.findall("w:tc",NS),1):
                    for pi,p in enumerate(cell.findall(".//w:p",NS),1):
                        pp=p.find("w:pPr",NS);ps=pp.find("w:pStyle",NS) if pp is not None else None
                        psize=pp.find("w:rPr/w:sz",NS) if pp is not None else None
                        base=(Decimal(psize.get(W+"val"))/2 if psize is not None and psize.get(W+"val") else inherited(ps.get(W+"val") if ps is not None else None)) or default
                        run_sizes(p,base,f"table{ti}/r{ri}/c{ci}/p{pi}",fs["tables"])
        for k,minimum in (("body",10.5),("tables",9.5)):
            vals=fs[k]["sizes"];fs[k]["min_pt"]=min(vals) if vals else None;fs[k]["threshold_pt"]=minimum
            fs[k]["run_count"]=len(vals)+len(fs[k]["unresolved"]);fs[k]["below_threshold_count"]=sum(v<minimum for v in vals)
        gates["body_text_font_at_least_10_5pt"]=status(bool(fs["body"]["sizes"]) and not fs["body"]["unresolved"] and not fs["body"]["below_threshold_count"])
        gates["table_text_font_at_least_9_5pt"]=status(bool(fs["tables"]["sizes"]) and not fs["tables"]["unresolved"] and not fs["tables"]["below_threshold_count"])

        # Compare physical OOXML structure to a fresh Markdown table parse, not Builder counts.
        source_shapes=md_table_shapes(repair);ooxml_shapes=[{"row_count_including_header":len(t),"column_counts":[len(r) for r in t]} for t in tables]
        structure={"top_level_paragraph_count":len(paragraphs),"empty_body_paragraphs":fs["body"]["empty_paragraphs"],
          "table_count":len(tables),"table_row_counts":[len(t) for t in tables],"source_markdown_table_shapes":source_shapes,
          "ooxml_table_shapes":ooxml_shapes,"empty_table_paragraphs":empty_cell_paras,"empty_table_cells":empty_cells,"empty_table_rows":empty_rows,
          "body_text_characters":len(para_text),"table_text_characters":sum(map(len,table_text))}
        gates["candidate_table_count_matches_repair_source"]=status(len(tables)==len(source_shapes))
        gates["candidate_table_row_counts_match_repair_source"]=status(len(tables)==len(source_shapes) and [x["row_count_including_header"] for x in ooxml_shapes]==[x["row_count_including_header"] for x in source_shapes])
        gates["no_empty_table_cells_or_rows"]=status(not empty_cells and not empty_rows)

        # SAMPLE/REAL/UNKNOWN markers, table-local labels and persistent header/footer design.
        sample=bool(re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",whole,re.I));real=bool(re.search(r"\bREAL\b",whole,re.I));unknown=bool(re.search(r"UNKNOWN",whole,re.I))
        table_marks=[];seq_positions={id(x):j for j,(_,x) in enumerate(seq)}
        for i,(tt,rows) in enumerate(zip(table_text,tables),1):
            preceding="";pos=seq_positions.get(id(table_nodes[i-1]),0)
            for j in range(pos-1,-1,-1):
                if seq[j][0]=="p" and tx(seq[j][1]).strip():preceding=tx(seq[j][1]);break
            table_marks.append({"table":i,"sample_in_table":bool(re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",tt,re.I)),
              "sample_in_immediately_preceding_paragraph":bool(re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",preceding,re.I)),
              "has_status_marker":bool(re.search(r"SAMPLE|SYNTHETIC|UNKNOWN|REAL SOURCE|待取得的 REAL",tt,re.I))})
        relroot=parts.get("word/_rels/document.xml.rels");relmap={}
        if relroot is not None:
            for r in relroot.findall("rel:Relationship",NS):relmap[r.get("Id")]=r.get("Target")
        sections=[]
        for si,sec in enumerate(body.findall(".//w:sectPr",NS),1):
            refs=[]
            for typ in ("headerReference","footerReference"):
                for ref in sec.findall("w:"+typ,NS):
                    target=relmap.get(ref.get("{"+NS["r"]+"}id"),"");part="word/"+target.replace("\\","/").lstrip("/")
                    pp=[]
                    for seg in part.split("/"):
                        if seg=="..":
                            if pp:pp.pop()
                        elif seg not in ("", "."):pp.append(seg)
                    part="/".join(pp);node=parts.get(part);marker=bool(node is not None and re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",tx(node),re.I))
                    refs.append({"kind":typ,"part":part,"sample_marker":marker})
            sections.append({"section":si,"references":refs,"sample_header_or_footer":any(x["sample_marker"] for x in refs)})
        gates["document_sample_real_unknown_boundary_present"]=status(sample and real and unknown)
        gates["tables_have_local_or_adjacent_sample_or_status_marker"]=status(bool(table_marks) and all(x["has_status_marker"] or x["sample_in_immediately_preceding_paragraph"] for x in table_marks))
        gates["persistent_page_sample_marker_design"]=status(bool(sections) and all(x["sample_header_or_footer"] for x in sections)) if sections else "UNKNOWN"

        # Placeholder and low-information shell scan. Workflow explanations are not treated as blanks.
        units=[]
        for pi,p in enumerate(paragraphs,1):units.append((f"body/p{pi}",tx(p)))
        for ti,rows in enumerate(tables,1):
            for ri,row in enumerate(rows,1):
                for ci,cell in enumerate(row,1):units.append((f"table{ti}/r{ri}/c{ci}",cell))
        placeholders=[];generic=[]
        for loc,value in units:
            v=value.strip(); compact=re.sub(r"[【】\[\]（）()\s]","",v)
            if FILL_RE.fullmatch(compact) or re.search(r"(?:此處|本欄|請|應)\s*(?:待填|待核|待補|填入|補入)|(?:\[|【|（|\()\s*(?:待填|待核|待補|TBD|TODO)\s*(?:\]|】|）|\))",v,re.I):
                placeholders.append({"location":loc,"value":v[:240]})
            if len(v)<=32 and GENERIC_RE.fullmatch(v):generic.append({"location":loc,"value":v})
        gates["no_live_fill_or_shell_placeholders"]=status(not placeholders and not generic)

        # Unique fact ledger and per-row REAL replacement guidance.
        doc_ids=set(ID_RE.findall(whole));fact_tables=[];ledger_ids=set();duplicate_ids=[];ledger_rows=[];missing_ledger_fields=[];sample_rows_missing=[]
        for ti,rows in enumerate(tables,1):
            if not rows:continue
            hdr=[x.strip() for x in rows[0]]
            fact_cols=[i for i,x in enumerate(hdr) if re.search(r"fact[_ ]?id|唯一\s*fact_id",x,re.I)]
            if not fact_cols:continue
            fact_tables.append(ti)
            desc_cols=[i for i,x in enumerate(hdr) if re.search(r"完整登錄|合成事實|描述|assertion",x,re.I)]
            repl_cols=[i for i,x in enumerate(hdr) if re.search(r"替換|replacement|REAL\s*(?:source|證據)|邊界",x,re.I)]
            for ri,row in enumerate(rows[1:],2):
                for fi in fact_cols:
                    cell=row[fi] if fi<len(row) else ""; ids=set(ID_RE.findall(cell))
                    if not ids:
                        missing_ledger_fields.append({"table":ti,"row":ri,"field":"fact_id","value":cell});continue
                    over=ledger_ids & ids
                    if over:duplicate_ids.extend(sorted(over))
                    ledger_ids.update(ids)
                    desc=" ".join(row[x] for x in desc_cols if x<len(row)).strip()
                    repl=" ".join(row[x] for x in repl_cols if x<len(row)).strip()
                    if not desc:missing_ledger_fields.append({"table":ti,"row":ri,"ids":sorted(ids),"field":"fact_description"})
                    if not repl:missing_ledger_fields.append({"table":ti,"row":ri,"ids":sorted(ids),"field":"replacement_guidance"})
                    if not re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",repl,re.I):sample_rows_missing.append({"table":ti,"row":ri,"ids":sorted(ids)})
                    ledger_rows.append({"table":ti,"row":ri,"ids":sorted(ids),"description_present":bool(desc),"replacement_guidance_present":bool(repl),"sample_real_boundary_present":bool(re.search(r"SAMPLE\s*/\s*SYNTHETIC|SAMPLE/SYNTHETIC",repl,re.I))})
        unregistered=sorted(doc_ids-ledger_ids);unused=sorted(ledger_ids-doc_ids)
        gates["synthetic_ids_all_have_unique_fact_ledger_rows"]=status(bool(fact_tables) and not unregistered and not unused and not duplicate_ids and not missing_ledger_fields)
        gates["replacement_guidance_complete_per_fact_id"]=status(bool(fact_tables) and not missing_ledger_fields and not any(x.get("field")=="replacement_guidance" for x in missing_ledger_fields))
        gates["fact_ledger_rows_state_sample_real_boundary"]=status(bool(ledger_rows) and not sample_rows_missing)

        # Recompute all 12x3 gap vectors from table 2 (target=3 per stated source rule).
        matrix_rows=[];row_checks=[]
        for ti,rows in enumerate(tables,1):
            hdr=" ".join(rows[0]).casefold() if rows else ""
            if "現況 c1/c2/c3" not in hdr or "差距 c1/c2/c3" not in hdr:continue
            for ri,row in enumerate(rows[1:],2):
                if not row:continue
                m=re.search(r"SYN-0034-L(\d{2})",row[0])
                if not m:continue
                current=[int(x) for x in re.findall(r"\d+",row[1])] if len(row)>1 else []
                gaps=[int(x) for x in re.findall(r"\d+",row[2])] if len(row)>2 else []
                ident="SYN-0034-L"+m.group(1);record={"table":ti,"row":ri,"id":ident,"current":current,"reported_gap":gaps,"target":[3,3,3]}
                if len(current)==3 and len(gaps)==3:
                    expected=[3-x for x in current];ok=expected==gaps
                    record["recomputed_gap"]=expected;record["pass"]=ok
                    for k in range(3):row_checks.append({"id":ident,"competency":f"C{k+1}","target":3,"current":current[k],"reported_gap":gaps[k],"computed_gap":expected[k],"pass":expected[k]==gaps[k]})
                else:record["pass"]=None
                matrix_rows.append(record)
        totals={f"C{k+1}":{"below_target":sum(1 for r in matrix_rows if r.get("pass") and r["reported_gap"][k]>0),
              "gap_sum":sum(r["reported_gap"][k] for r in matrix_rows if r.get("pass")),"n":sum(1 for r in matrix_rows if r.get("pass"))} for k in range(3)}
        for k in range(3):
            totals[f"C{k+1}"]["percent_below_target"]=str((Decimal(totals[f"C{k+1}"]["below_target"])/Decimal(totals[f"C{k+1}"]["n"])*100).quantize(Decimal("0.1"),rounding=ROUND_HALF_UP)) if totals[f"C{k+1}"]["n"] else None
        summary_claims=[];summary_checks=[]
        for k in range(1,4):
            pat=rf"C{k}\s*[：:]\s*低於目標者為\s*(\d+)\s*筆\s*；\s*比例\s*[=＝]\s*(\d+)\s*[÷/]\s*(\d+)\s*[×x]\s*100\s*%\s*[=＝]\s*([\d.]+)\s*%\s*。\s*差距總和\s*[=＝]\s*((?:\d+\s*\+\s*)+\d+)\s*[=＝]\s*(\d+)"
            m=re.search(pat,para_text,re.I)
            if m:
                below,num,den,pct,gap_expression,gapsum=m.groups();calc=totals[f"C{k}"];gap_operands=[int(x) for x in re.findall(r"\d+",gap_expression)];gap_expression_total=sum(gap_operands)
                ok=(int(below)==calc["below_target"] and int(num)==calc["below_target"] and int(den)==calc["n"] and Decimal(pct)==Decimal(calc["percent_below_target"]) and gap_expression_total==int(gapsum)==calc["gap_sum"])
                summary_claims.append({"competency":f"C{k}","reported_below":int(below),"fraction_numerator":int(num),"fraction_denominator":int(den),"reported_percent":pct,"gap_sum_expression":gap_expression,"gap_sum_operands":gap_operands,"gap_expression_total":gap_expression_total,"reported_gap_sum":int(gapsum),"recomputed":calc,"pass":ok})
                summary_checks.append(ok)
        gates["all_matrix_row_gap_formulas_recompute"]=status(len(matrix_rows)==12 and len(row_checks)==36 and all(x["pass"] for x in row_checks)) if matrix_rows else "UNKNOWN"
        gates["all_three_summary_totals_and_fractions_recompute"]=status(len(summary_claims)==3 and all(summary_checks)) if summary_claims else "UNKNOWN"

        # Explicit additive formula and course-hour totals.
        additions=[]
        for m in re.finditer(r"((?:\d+\s*\+\s*)+\d+)\s*[=＝]\s*(\d+)",para_text):
            vals=[int(x) for x in re.findall(r"\d+",m.group(1))];expected=sum(vals);reported=int(m.group(2))
            additions.append({"expression":m.group(),"operands":vals,"computed_sum":expected,"reported_sum":reported,"pass":expected==reported})
        hours=[]
        for m in re.finditer(r"總計\s*(\d+)\s*小時.{0,45}?分三個單元各\s*(\d+)\s*小時",whole):
            total,each=map(int,m.groups());hours.append({"reported_total_hours":total,"unit_count":3,"hours_per_unit":each,"computed_total":3*each,"pass":total==3*each})
        gates["explicit_additive_formulas_consistent"]=status(bool(additions) and all(x["pass"] for x in additions)) if additions else "UNKNOWN"
        gates["course_hour_total_consistent"]=status(bool(hours) and all(x["pass"] for x in hours)) if hours else "UNKNOWN"

        # Literal source/genre anchors and negative-neighbor boundaries.
        quote="針對學員做職能盤點或職能分析並據以規劃適切課程的證明資料"
        source_checks={"candidate_doc_requirement_id":"I07-E02" in whole,"candidate_doc_id":"0034" in whole,
          "official_checkbox_core_text_present":normalized(quote) in normalized(whole),
          "blueprint_genre_present":"學員職能盤點與課程適配分析報告" in whole,
          "negative_neighbor_0033":"0033" in whole,"negative_neighbor_0035":"0035" in whole,
          "negative_neighbor_0036":"0036" in whole,"negative_neighbor_0049":"0049" in whole}
        gates["literal_requirement_and_genre_pointers_present"]=status(all(source_checks.values()))

    after=sha(CAND)
    gates["candidate_unchanged_and_exact_sha_after_read"]=status(after==before==EXPECTED_CAND)
    gates["source_packet_sha_matches_build_binding"]=status(bindings["source_packet"]["sha256"]==bindings["source_packet"]["build_receipt_expected_sha256"])
    gates["blueprint_sha_matches_build_binding"]=status(bindings["blueprint"]["sha256"]==bindings["blueprint"]["build_receipt_expected_sha256"])
    gates["repair_source_sha_matches_build_binding"]=status(bindings["r02_scoped_repair"]["sha256"]==bindings["r02_scoped_repair"]["build_receipt_expected_sha256"])
    script_path=Path(__file__).resolve();script_hash=sha(script_path)
    all_values=list(gates.values());overall="PASS" if all(x=="PASS" for x in all_values) else "FAIL" if any(x=="FAIL" for x in all_values) else "UNKNOWN"
    out={"work_id":"TTQS_ONE_0034_I07-E02_STATIC_QA_R02","started_utc":started,"completed_utc":datetime.now(timezone.utc).isoformat(),
      "scope":"0034 R02 only; deterministic OOXML/content checks; no 0035 access, Word COM, render, visual or semantic acceptance.",
      "bindings":bindings,"script_path":str(script_path),"script_sha256":script_hash,"candidate_sha256_after":after,
      "gates":gates,"overall_static_status":overall,
      "findings":{"zip":{"bad_member":bad,"missing_required_parts":missing,"xml_parse_errors":xml_errors},
       "structure":structure,"font_sizes":fs,"sample_real_boundary":{"document_sample_synthetic":sample,"document_real":real,"document_unknown":unknown,
         "tables":table_marks,"page_header_footer_sections":sections,"physical_page_layout":"UNKNOWN_NOT_RENDERED"},
       "placeholders":{"live_placeholder_locations":placeholders,"generic_shell_locations":generic},
       "synthetic_fact_ledger":{"candidate_unique_id_count":len(doc_ids),"candidate_unique_ids":sorted(doc_ids),
         "fact_ledger_tables":fact_tables,"fact_ledger_unique_id_count":len(ledger_ids),"registered_fact_ids":sorted(ledger_ids),
         "unregistered_candidate_ids":unregistered,"unused_registered_ids":unused,"duplicate_fact_id_definitions":sorted(set(duplicate_ids)),
         "row_completeness_findings":missing_ledger_fields,"rows_without_sample_real_boundary":sample_rows_missing,"fact_ledger_rows":ledger_rows},
       "matrix_recalculation":{"matrix_learner_row_count":len(matrix_rows),"row_formula_check_count":len(row_checks),"row_checks":row_checks,
         "recomputed_totals":totals,"reported_summary_claims":summary_claims},
       "arithmetic":{"explicit_additions":additions,"course_hours":hours},"literal_source_genre_checks":source_checks,
       "build_receipt_comparison":{"receipt_claimed_table_count":build.get("ooxml_checks",{}).get("table_count"),
         "independently_extracted_table_count":len(tables),"receipt_candidate_sha256":build.get("output",{}).get("sha256")}},
      "limitations":["No Word COM or render was run; physical pagination/layout remains UNKNOWN.","No semantic or evaluator-facing acceptance is claimed."]}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=="__main__":main()
