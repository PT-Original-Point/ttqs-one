import csv, hashlib, json, re, zipfile
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
import xml.etree.ElementTree as ET

BASE=Path(r"E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118")
ROOT=Path(r"E:\tqrepo")
CAND=BASE/"candidate"/"0035_I07-E03_R01_W1_NEMOTRON.docx"
OUT=CAND.parent/"qa"/"static_qa_r01_independent"
BUILD=CAND.parent/"qa"/"build_r01"/"BUILD_RECEIPT_0035_I07-E03_R01.json"
SOURCE_RECEIPT=BASE/"SHA_RECEIPT_0035_I07-E03_R01.json"
PACKET=BASE/"SOURCE_PACKET_0035_I07-E03_R01.md"
BLUEPRINT=BASE/"UNIQUE_BLUEPRINT_0035_I07-E03_R01.md"
WORKER=BASE/"writer"/"attempt_0035_W1_R01"/"WORKER_BODY_R01_RECOVERED.md"
TERMINAL=BASE/"writer"/"attempt_0035_W1_R01"/"WORKER_TERMINAL_RECEIPT_R01.json"
EXPECTED="D0D1A24852A93037F00041D3298042B720C64F621D0CB702E1414E2273C0A7B9"
NS={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel":"http://schemas.openxmlformats.org/package/2006/relationships"}
W="{"+NS["w"]+"}"
ID_RE=re.compile(r"(?<![A-Za-z0-9_-])SYN-0035-\d{2,4}(?:[A-Za-z][A-Za-z0-9_-]*)?(?![A-Za-z0-9_-])")
RANGE_RE=re.compile(r"SYN-0035-(\d{2,4})\s*[-–—~～至到]\s*(?:SYN-0035-)?(\d{2,4})")
PLACE_RE=re.compile(r"待填|待核|待確認|待補|會後填寫|保持空白|空白表|\bblank\b",re.I)
SAMPLE_RE=re.compile(r"SAMPLE|SYNTHETIC",re.I)

def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest().upper()
def txt(el): return "".join(x.text or "" for x in el.iter(W+"t"))
def st(ok): return "PASS" if ok else "FAIL"
def relpath(p):
    try:return str(Path(p).relative_to(ROOT))
    except ValueError:return str(p)
def norm(s):return re.sub(r"\s+","",s)

def main():
    if not OUT.is_dir(): raise RuntimeError("Authorized QA output directory absent")
    before=sha(CAND)
    build=json.loads(BUILD.read_text(encoding="utf-8"))
    sr=json.loads(SOURCE_RECEIPT.read_text(encoding="utf-8"))
    result={"qa_type":"DETERMINISTIC_STATIC_DOCX_QA","doc_id":"0035","requirement_id":"I07-E03",
      "candidate_path":str(CAND),"expected_candidate_sha256":EXPECTED,"candidate_sha256_before":before,
      "build_receipt_path":str(BUILD),"build_receipt_sha256":sha(BUILD),
      "source_preparation_receipt_path":str(SOURCE_RECEIPT),"source_preparation_receipt_sha256":sha(SOURCE_RECEIPT),
      "started_utc":datetime.now(timezone.utc).isoformat(),"gates":{},"findings":{}}
    result["gates"]["exact_candidate_sha"] = st(before==EXPECTED and build.get("output_sha256","").upper()==EXPECTED)
    result["findings"]["build_receipt_binding"]={"build_output_sha256":build.get("output_sha256"),"expected_matches":build.get("output_sha256","").upper()==EXPECTED,
      "build_receipt_table_count":build.get("tables"),"build_receipt_synthetic_identifier_count":build.get("synthetic_identifier_count"),
      "build_receipt_synthetic_identifier_values_count":len(build.get("synthetic_identifier_values",[]))}

    with zipfile.ZipFile(CAND) as z:
        bad=z.testzip(); names=set(z.namelist()); required={"[Content_Types].xml","word/document.xml","word/styles.xml"}
        missing=sorted(required-names); xml_errors=[]; parsed={}
        for name in sorted(names):
            if name.endswith((".xml",".rels")):
                try:parsed[name]=ET.fromstring(z.read(name))
                except Exception as e:xml_errors.append({"part":name,"error":str(e)})
        doc=parsed.get("word/document.xml"); styles_root=parsed.get("word/styles.xml")
        zipok=bad is None and not missing and not xml_errors and doc is not None
        result["gates"]["zip_docx_openable"] = st(zipok)
        result["findings"]["zip"]={"bad_member":bad,"missing_required_parts":missing,"xml_parse_errors":xml_errors}
        if doc is None: raise RuntimeError("word/document.xml absent or unreadable; no QA receipt emitted")

        body=doc.find("w:body",NS)
        top_paras=[]; table_nodes=[]; sequence=[]
        for child in list(body):
            if child.tag==W+"p":top_paras.append(child); sequence.append(("p",child))
            elif child.tag==W+"tbl":table_nodes.append(child); sequence.append(("tbl",child))
        tables=[]; table_text=[]; blank_cells=[]; blank_rows=[]; empty_table_paras=[]
        for ti,t in enumerate(table_nodes,1):
            rows=[]; cellloc=[]
            for ri,row in enumerate(t.findall("w:tr",NS),1):
                cells=[]
                for ci,cell in enumerate(row.findall("w:tc",NS),1):
                    ps=cell.findall(".//w:p",NS); parts=[]
                    for pj,p in enumerate(ps,1):
                        val=txt(p); parts.append(val)
                        if not val.strip():empty_table_paras.append(f"table{ti}/r{ri}/c{ci}/p{pj}")
                    val="".join(parts); cells.append(val)
                    if not val.strip():blank_cells.append(f"table{ti}/r{ri}/c{ci}")
                rows.append(cells)
                if not "".join(cells).strip():blank_rows.append(f"table{ti}/r{ri}")
            tables.append(rows); table_text.append("\n".join("\t".join(r) for r in rows))
        body_text="\n".join(txt(p) for p in top_paras)
        all_text="\n".join(txt(x) if k=="p" else table_text[table_nodes.index(x)] for k,x in sequence)

        # Effective run size: direct run -> paragraph mark -> paragraph style chain -> document default.
        styles={}; default_pt=None
        if styles_root is not None:
            d=styles_root.find("w:docDefaults/w:rPrDefault/w:rPr/w:sz",NS)
            if d is not None and d.get(W+"val"):default_pt=Decimal(d.get(W+"val"))/2
            for s in styles_root.findall("w:style",NS):
                sid=s.get(W+"styleId"); based=s.find("w:basedOn",NS); sz=s.find("w:rPr/w:sz",NS)
                styles[sid]={"based":based.get(W+"val") if based is not None else None,
                    "pt":Decimal(sz.get(W+"val"))/2 if sz is not None and sz.get(W+"val") else None}
        def style_size(sid,seen=None):
            seen=seen or set()
            if not sid or sid in seen or sid not in styles:return None
            seen.add(sid); o=styles[sid]
            return o["pt"] if o["pt"] is not None else style_size(o["based"],seen)
        fs={"body":{"sizes":[],"unresolved":[],"nonempty_paragraphs":0,"empty_paragraphs":[]},
            "table":{"sizes":[],"unresolved":[],"paragraph_count":0}}
        for i,p in enumerate(top_paras,1):
            if not txt(p).strip():fs["body"]["empty_paragraphs"].append(f"body/p{i}")
            else:fs["body"]["nonempty_paragraphs"]+=1
            ppr=p.find("w:pPr",NS); ps=ppr.find("w:pStyle",NS) if ppr is not None else None
            psize=ppr.find("w:rPr/w:sz",NS) if ppr is not None else None
            base=(Decimal(psize.get(W+"val"))/2 if psize is not None and psize.get(W+"val") else style_size(ps.get(W+"val") if ps is not None else None)) or default_pt
            scan_runs(p,f"body/p{i}",base,fs["body"])
        for ti,t in enumerate(table_nodes,1):
            for ri,row in enumerate(t.findall("w:tr",NS),1):
                for ci,cell in enumerate(row.findall("w:tc",NS),1):
                    for pj,p in enumerate(cell.findall(".//w:p",NS),1):
                        fs["table"]["paragraph_count"]+=1
                        ppr=p.find("w:pPr",NS); ps=ppr.find("w:pStyle",NS) if ppr is not None else None
                        psize=ppr.find("w:rPr/w:sz",NS) if ppr is not None else None
                        base=(Decimal(psize.get(W+"val"))/2 if psize is not None and psize.get(W+"val") else style_size(ps.get(W+"val") if ps is not None else None)) or default_pt
                        scan_runs(p,f"table{ti}/r{ri}/c{ci}/p{pj}",base,fs["table"])
        for kind,minimum in (("body",10.5),("table",9.5)):
            vals=fs[kind]["sizes"]; fs[kind]["minimum_required_pt"]=minimum; fs[kind]["minimum_observed_pt"]=min(vals) if vals else None
            fs[kind]["run_count"]=len(vals)+len(fs[kind]["unresolved"]); fs[kind]["below_minimum_run_count"]=sum(x<minimum for x in vals)
        result["findings"]["font_sizes"]=fs
        for kind,key,minimum in (("body","body_font_at_least_10_5pt",10.5),("table","table_font_at_least_9_5pt",9.5)):
            result["gates"][key]=st(bool(fs[kind]["sizes"]) and not fs[kind]["unresolved"] and not fs[kind]["below_minimum_run_count"])
        result["findings"]["structure"]={"body_top_level_paragraphs":len(top_paras),"nonempty_body_paragraphs":fs["body"]["nonempty_paragraphs"],
           "empty_body_paragraphs":fs["body"]["empty_paragraphs"],"table_count":len(tables),"table_row_counts":[len(t) for t in tables],
           "empty_table_paragraphs":empty_table_paras,"empty_table_cells":blank_cells,"empty_table_rows":blank_rows,
           "body_text_characters":len(body_text),"table_text_characters":sum(map(len,table_text))}
        result["gates"]["build_receipt_table_count_matches"] = st(len(tables)==build.get("tables"))
        result["gates"]["no_empty_table_cells_or_rows"] = st(not blank_cells and not blank_rows)

        # Per-table and page-marker design: structural checks only; physical pagination needs rendering.
        table_marks=[{"table":i,"header":rows[0] if rows else [],"sample_marker":bool(SAMPLE_RE.search(t))} for i,(t,rows) in enumerate(zip(table_text,tables),1)]
        header_parts=[]; footer_parts=[]; section_bindings=[]
        relroot=parsed.get("word/_rels/document.xml.rels")
        relmap={}
        if relroot is not None:
            for rel in relroot.findall("rel:Relationship",NS):relmap[rel.get("Id")]=rel.get("Target")
        sections=body.findall(".//w:sectPr",NS)
        for si,sec in enumerate(sections,1):
            refs=[]
            for typ in ("headerReference","footerReference"):
                for ref in sec.findall("w:"+typ,NS):
                    rid=ref.get("{"+NS["r"]+"}id"); target=relmap.get(rid)
                    if target:
                        part=str(Path("word")/target.replace("/","\\")); part=part.replace("\\","/")
                        # Resolve ../ targets relative to word/.
                        stack=[]
                        for item in part.split("/"):
                            if item=="..":
                                if stack:stack.pop()
                            elif item!=".":stack.append(item)
                        part="/".join(stack); root=parsed.get(part)
                        value=txt(root) if root is not None else ""
                        rec={"section":si,"kind":typ,"type":ref.get(W+"type"),"part":part,"sample_marker":bool(SAMPLE_RE.search(value))}
                        refs.append(rec)
                        (header_parts if typ=="headerReference" else footer_parts).append(rec)
            section_bindings.append({"section":si,"references":refs,"has_sample_header_or_footer":any(x["sample_marker"] for x in refs)})
        explicit_breaks=len(doc.findall(".//w:br[@w:type='page']",NS)); rendered_breaks=len(doc.findall(".//w:lastRenderedPageBreak",NS))
        result["findings"]["sample_marking"]={"document_sample_marker":bool(SAMPLE_RE.search(all_text)),"document_real_boundary_marker":bool(re.search(r"REAL",all_text,re.I)),
           "table_markers":table_marks,"tables_without_sample_marker":[x["table"] for x in table_marks if not x["sample_marker"]],
           "section_header_footer_markers":section_bindings,"explicit_page_break_count":explicit_breaks,"last_rendered_page_break_count":rendered_breaks,
           "physical_page_marker_status":"UNKNOWN_NO_RENDER; section header/footer and explicit markers inspected"}
        result["gates"]["document_sample_real_boundary"] = st(bool(SAMPLE_RE.search(all_text)) and bool(re.search(r"REAL",all_text,re.I)))
        result["gates"]["sample_marker_each_table"] = st(bool(tables) and all(x["sample_marker"] for x in table_marks))
        result["gates"]["persistent_sample_marker_each_section"] = st(bool(section_bindings) and all(x["has_sample_header_or_footer"] for x in section_bindings)) if section_bindings else "UNKNOWN"

        # Fillable placeholders are context-classified so policy statements do not count as live blanks.
        ph=[]
        for m in PLACE_RE.finditer(all_text):
            context=all_text[max(0,m.start()-70):min(len(all_text),m.end()+70)].replace("\n"," ")
            neg=bool(re.search(r"未留|不得|不需|不應|不提供|不可|禁止|無須|沒有|not\s+blank|no\s+blank",context,re.I))
            status_choice=m.group()=="待核" and bool(re.search(r"採納.{0,16}拒絕.{0,16}試行.{0,16}待核|待核.{0,16}四級",context))
            klass="workflow_status_choice_not_placeholder" if status_choice else "negated_claim_or_instruction" if neg else "possible_live_placeholder"
            ph.append({"term":m.group(),"context":context,"classification":klass})
        live=[x for x in ph if x["classification"]=="possible_live_placeholder"]
        result["findings"]["placeholder_scan"]={"hits":ph,"possible_live_placeholder_count":len(live)}
        result["gates"]["no_live_placeholder"] = st(not live)

        # Synthetic-ID reconciliation: fact_id and finding_id are separate named columns/namespaces.
        doc_ids=set(ID_RE.findall(all_text)); build_ids=set(build.get("synthetic_identifier_values",[]))
        fact_ids={x for x in doc_ids if re.fullmatch(r"SYN-0035-\d{4}",x)}
        finding_ids={x for x in doc_ids if re.fullmatch(r"SYN-0035-\d{2}",x)}
        register_tables=[]; registered=set(); explicit_primary=set(); finding_tables=[]; registered_findings=set()
        dups=[]; repl_cols=[]; missing_repl=[]; register_rows=[]; finding_rows=[]
        for ti,rows in enumerate(tables,1):
            if not rows:continue
            header=[x.strip() for x in rows[0]]; h=" ".join(header).casefold()
            fact_cols=[i for i,x in enumerate(header) if re.search(r"^fact[_ ]?id$|事實id|唯一事實|synthetic id",x,re.I)]
            find_cols=[i for i,x in enumerate(header) if re.search(r"^finding[_ ]?id$",x,re.I)]
            repl_idx=[i for i,x in enumerate(header) if re.search(r"替換|替代|replacement|real source|real evidence|替換指引",x,re.I)]
            if fact_cols:
                register_tables.append(ti)
                if repl_idx:repl_cols.extend({"table":ti,"index":i,"header":header[i]} for i in repl_idx)
            if find_cols:finding_tables.append(ti)
            for ri,row in enumerate(rows[1:],2):
                for ix in find_cols:
                    cell=row[ix] if ix<len(row) else ""; ids=set(ID_RE.findall(cell)); registered_findings.update(ids)
                    if ids:finding_rows.append({"table":ti,"row":ri,"ids":sorted(ids)})
                for ix in fact_cols:
                    cell=row[ix] if ix<len(row) else ""; ids={x for x in ID_RE.findall(cell) if re.fullmatch(r"SYN-0035-\d{4}",x)}; explicit_primary.update(ids)
                    expanded=set(ids)
                    for m in RANGE_RE.finditer(cell):
                        a,b=m.groups(); width=max(len(a),len(b)); lo,hi=int(a),int(b)
                        if hi>=lo and hi-lo<1000:
                            for n in range(lo,hi+1):expanded.add("SYN-0035-"+str(n).zfill(width))
                    if not expanded:continue
                    overlap=registered&expanded
                    if overlap:dups.extend(sorted(overlap))
                    registered.update(expanded)
                    register_rows.append({"table":ti,"row":ri,"fact_id_column":ix+1,"id_cell":cell,"explicit_ids":sorted(ids),"range_expanded_ids":sorted(expanded)})
                    if not repl_idx:
                        missing_repl.append({"table":ti,"row":ri,"fact_ids":sorted(expanded),"issue":"no replacement-guidance column exists in the fact_id table"})
                    else:
                        for rx in repl_idx:
                            if rx>=len(row) or not row[rx].strip():missing_repl.append({"table":ti,"row":ri,"fact_ids":sorted(expanded),"field":header[rx]})
        unregistered_fact=sorted(fact_ids-registered); extra_fact=sorted(registered-fact_ids); unregistered_finding=sorted(finding_ids-registered_findings)
        receipt_missing=sorted(build_ids-doc_ids); receipt_extra=sorted(doc_ids-build_ids)
        claim_matches=[int(x) for x in re.findall(r"\b(\d+)\s*(?:個)?\s*fact[_ -]?id\b",all_text,re.I)]
        claim_matches=list(dict.fromkeys(claim_matches))
        result["findings"]["synthetic_id_register"]={"unique_ids_extracted_from_candidate_count":len(doc_ids),"candidate_ids":sorted(doc_ids),
          "unique_fact_id_format_count":len(fact_ids),"fact_ids_extracted":sorted(fact_ids),"unique_finding_id_format_count":len(finding_ids),"finding_ids_extracted":sorted(finding_ids),
          "build_receipt_unique_id_count":build.get("synthetic_identifier_count"),"build_receipt_id_value_count":len(build_ids),
          "candidate_vs_build_receipt_missing_ids":receipt_missing,"candidate_vs_build_receipt_extra_ids":receipt_extra,
          "fact_id_register_tables":register_tables,"explicit_fact_id_column_unique_count":len(explicit_primary),"explicit_fact_id_column_ids":sorted(explicit_primary),
          "range_expanded_registered_fact_id_count":len(registered),"registered_fact_ids":sorted(registered),"unregistered_fact_ids":unregistered_fact,
          "fact_ids_not_found_in_candidate":extra_fact,"duplicate_fact_id_definitions":sorted(set(dups)),"fact_register_rows":register_rows,
          "finding_id_tables":finding_tables,"finding_id_column_rows":finding_rows,"unregistered_finding_ids":unregistered_finding,
          "replacement_guidance_columns":repl_cols,"rows_missing_replacement_guidance":missing_repl,
          "body_fact_id_count_claims":claim_matches,"body_fact_id_claim_matches_four_digit_fact_id_count":bool(claim_matches) and all(n==len(fact_ids) for n in claim_matches),
          "fact_id_rows_fully_registered":len(fact_ids)==len(registered) and not unregistered_fact}
        result["gates"]["build_receipt_id_inventory_matches_candidate"] = st(doc_ids==build_ids)
        result["gates"]["all_fact_ids_uniquely_registered"] = st(bool(register_tables) and not unregistered_fact and not extra_fact and not dups)
        result["gates"]["replacement_guidance_per_fact_id"] = st(bool(repl_cols) and not missing_repl) if register_tables else "UNKNOWN"
        result["gates"]["body_fact_id_count_matches_fact_id_format_count"] = st(not claim_matches or all(n==len(fact_ids) for n in claim_matches))
        result["gates"]["finding_ids_have_unique_finding_register_rows"] = st(bool(finding_tables) and not unregistered_finding)

        # Requirements/source/negative-neighbor checks are literal artifact/hash checks, not semantic review.
        packet_text=PACKET.read_text(encoding="utf-8"); blueprint_text=BLUEPRINT.read_text(encoding="utf-8")
        packet_hash=sha(PACKET); blueprint_hash=sha(BLUEPRINT)
        source_entries=sr.get("source_bindings",{})
        cross=source_entries.get("crosswalk",{}); bp=source_entries.get("blueprint_index",{}); off=source_entries.get("official_requirement",{}); pages=source_entries.get("page_readbacks",{})
        crosspath=ROOT/cross.get("path",""); bppath=ROOT/bp.get("path",""); pdfpath=ROOT/off.get("pdf_path","")
        pypdfpath=ROOT/pages.get("pypdf_path",""); plumberpath=ROOT/pages.get("pdfplumber_path","")
        source_checks={"source_packet_sha_matches_build_receipt":packet_hash==build.get("source_packet_sha256"),
          "unique_blueprint_sha_matches_build_receipt":blueprint_hash==build.get("unique_blueprint_sha256"),
          "crosswalk_file_sha_matches_source_receipt":bool(crosspath.exists()) and sha(crosspath)==cross.get("sha256"),
          "official_pdf_sha_matches_source_receipt":bool(pdfpath.exists()) and sha(pdfpath)==off.get("pdf_sha256"),
          "blueprint_index_sha_matches_source_receipt":bool(bppath.exists()) and sha(bppath)==bp.get("sha256"),
          "pypdf_readback_sha_matches_source_receipt":bool(pypdfpath.exists()) and sha(pypdfpath)==pages.get("pypdf_sha256"),
          "pdfplumber_readback_sha_matches_source_receipt":bool(plumberpath.exists()) and sha(plumberpath)==pages.get("pdfplumber_sha256")}
        row_checks={}
        if crosspath.exists():
            raw=crosspath.read_bytes().splitlines(); line=int(cross.get("selected_row_line",0)); row=raw[line-1] if 0<line<=len(raw) else b""
            row_checks["crosswalk_selected_row_hash_matches"] = hashlib.sha256(row).hexdigest().upper()==cross.get("selected_raw_row_sha256")
            row_checks["crosswalk_selected_row_maps_0035_I07_E03"] = b"I07-E03,1,0,0035," in row
        if bppath.exists():
            raw=bppath.read_bytes().splitlines(); line=int(bp.get("selected_row_line",0)); row=raw[line-1] if 0<line<=len(raw) else b""
            row_checks["blueprint_selected_row_hash_matches"] = hashlib.sha256(row).hexdigest().upper()==bp.get("selected_raw_row_sha256")
            row_checks["blueprint_row_is_035"] = row.startswith("035".encode("utf-8"))
        official_phrase=off.get("exact_text","")
        pypdf_text=pypdfpath.read_text(encoding="utf-8",errors="replace") if pypdfpath.exists() else ""
        phrase_core=official_phrase.rstrip("。.!！")
        page_checks={"pypdf_readback_contains_official_phrase_after_whitespace_normalization":bool(official_phrase) and norm(official_phrase) in norm(pypdf_text),
          "candidate_contains_requirement_id":"I07-E03" in all_text,
          "candidate_contains_official_phrase_after_whitespace_normalization":bool(official_phrase) and norm(official_phrase) in norm(all_text),
          "candidate_contains_official_phrase_core_ignoring_terminal_punctuation":bool(phrase_core) and norm(phrase_core) in norm(all_text),
          "candidate_mentions_official_page_2":bool(re.search(r"(?:PDF|官方|第)\s*2\s*頁|page\s*2",all_text,re.I))}
        boundary_text=table_text[23] if len(table_text)>=24 else ""
        neighbor_ids={n:n in boundary_text for n in ("0033","0034","0036","0031","0049")}
        neighbor_codes={n:n in all_text for n in ("I07-E01","I07-E02","I07-E04","I06-E02","I11-E01")}
        boundary_negation=bool(re.search(r"不延伸至|不包括|不涵蓋|不重製",boundary_text))
        result["findings"]["source_and_scope_literal_checks"]={"source_artifact_sha_checks":source_checks,"crosswalk_and_blueprint_row_checks":row_checks,
          "official_text_and_page_checks":page_checks,"negative_neighbor_deliverable_id_mentions":neighbor_ids,
          "negative_neighbor_requirement_code_mentions":neighbor_codes,"boundary_negation_in_same_table":boundary_negation,
          "scope_note":"Literal path/hash/text-presence checks only; these do not constitute source-alignment or semantic acceptance."}
        result["gates"]["bound_source_artifacts_and_rows"] = st(all(source_checks.values()) and all(row_checks.values()))
        result["gates"]["official_requirement_literal_pointer"] = st(page_checks["candidate_contains_requirement_id"] and page_checks["candidate_mentions_official_page_2"])
        result["gates"]["negative_neighbor_ids_present_with_boundary"] = st(all(neighbor_ids.values()) and boundary_negation)

        # Arithmetic/equation scan; preserve every explicit ratio or percentage with its context.
        equations=[]
        eq_re=re.compile(r"(?<![\w-])(\d+(?:\.\d+)?)\s*([+−–—×*/÷-])\s*(\d+(?:\.\d+)?)\s*=\s*(\d+(?:\.\d+)?)(\s*%)?")
        for m in eq_re.finditer(all_text):
            a,op,b,c,pct=m.groups(); A,B,C=map(Decimal,(a,b,c)); expected=None
            if op=="+":expected=A+B
            elif op in ("-","−","–","—"):expected=A-B
            elif op=="×":expected=A*B
            elif op in ("/","÷") and B!=0:expected=A/B
            ok=(expected==C) if expected is not None and not pct else (expected is not None and abs(expected*100-C)<=Decimal("0.11")) if pct else False
            equations.append({"expression":m.group(),"operator":op,"expected":str(expected) if expected is not None else None,"pass":ok,
              "locator_char_offset":m.start(),"context":all_text[max(0,m.start()-70):m.end()+70].replace("\n"," ")})
        fractions=[]
        frac_re=re.compile(r"(?<!\d)(\d+(?:\.\d+)?)\s*[/／÷]\s*(\d+(?:\.\d+)?)(?!\d)")
        for m in frac_re.finditer(all_text):
            n,d=map(Decimal,m.groups()); context=all_text[max(0,m.start()-55):min(len(all_text),m.end()+75)].replace("\n"," ")
            near=re.search(r"=\s*(\d+(?:\.\d+)?)\s*%",all_text[m.end():m.end()+30])
            pct=Decimal(near.group(1)) if near else None
            fractions.append({"numerator":str(n),"denominator":str(d),"fraction":m.group(),"reported_percent_after_fraction":str(pct) if pct is not None else None,
              "computed_percent":str((n/d*100).quantize(Decimal("0.01"))) if d else None,
              "percent_matches":abs(n/d*100-pct)<=Decimal("0.11") if d and pct is not None else None,
              "locator_char_offset":m.start(),"context":context})
        percentages=[]
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%",all_text):
            percentages.append({"value_percent":m.group(1),"locator_char_offset":m.start(),"context":all_text[max(0,m.start()-65):m.end()+65].replace("\n"," ")})
        total_rows=[]
        for ti,rows in enumerate(tables,1):
            for ri,row in enumerate(rows,1):
                if row and re.search(r"合計|總計|小計|total",row[0],re.I):
                    total_rows.append({"table":ti,"row":ri,"values":row,"status":"REQUIRES_COLUMN_SEMANTICS; values reported, not blindly summed"})
        result["findings"]["quantitative_checks"]={"explicit_equation_count":len(equations),"equations":equations,"equation_mismatches":[x for x in equations if not x["pass"]],
          "fraction_claim_count":len(fractions),"fractions_and_numerators_denominators":fractions,"fraction_percent_mismatches":[x for x in fractions if x["percent_matches"] is False],
          "percentage_claims":percentages,"explicit_total_rows":total_rows,
          "note":"Only explicit arithmetic and stated numerator/denominator claims are recomputed; totals without clear additive column semantics are listed for review, not inferred."}
        result["gates"]["explicit_equations_consistent"] = st(bool(equations) and not any(not x["pass"] for x in equations)) if equations else "UNKNOWN"
        result["gates"]["explicit_fraction_percentages_consistent"] = st(not any(x["percent_matches"] is False for x in fractions)) if fractions else "UNKNOWN"

    # Claim discrepancy is called out separately from the 82-token inventory and registration comparison.
    claim77=any(x==77 for x in claim_matches)
    result["findings"]["claim_count_reconciliation"]={"body_claims_77_fact_id":claim77,"unique_candidate_ids":len(doc_ids),
      "build_receipt_unique_ids":build.get("synthetic_identifier_count"),"delta_candidate_minus_claim":len(doc_ids)-77 if claim77 else None,
      "candidate_ids_not_in_fact_register":unregistered if 'unregistered' in locals() else []}
    result["findings"]["audit_boundary"]="Deterministic static checks only; no Word COM, render, visual-pagination claim, model call, or semantic/source-alignment acceptance."
    after=sha(CAND); result["candidate_sha256_after"]=after
    result["gates"]["candidate_unchanged_during_qa"] = st(before==after==EXPECTED)
    result["completed_utc"]=datetime.now(timezone.utc).isoformat()
    gatevals=list(result["gates"].values()); result["overall_status"]="PASS" if all(x=="PASS" for x in gatevals) else "FAIL" if any(x=="FAIL" for x in gatevals) else "UNKNOWN"
    result["script_path"]=str(Path(__file__).resolve()); result["script_sha256"]=sha(Path(__file__))
    receipt=OUT/"STATIC_QA_RECEIPT_R01.json"; receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["overall_status"],"gates":result["gates"],"candidate_sha256":after,"build_receipt_sha256":result["build_receipt_sha256"],
      "script_sha256":result["script_sha256"],"receipt_sha256":sha(receipt),"structure":result["findings"]["structure"],
      "sample_marking":result["findings"]["sample_marking"],"synthetic_id_register":result["findings"]["synthetic_id_register"],
      "claim_count_reconciliation":result["findings"]["claim_count_reconciliation"],"source_checks":result["findings"]["source_and_scope_literal_checks"],
      "quantitative_summary":{"equations":result["findings"]["quantitative_checks"]["explicit_equation_count"],
       "fractions":result["findings"]["quantitative_checks"]["fraction_claim_count"],
       "percentage_claims":len(result["findings"]["quantitative_checks"]["percentage_claims"]),
       "equation_mismatches":len(result["findings"]["quantitative_checks"]["equation_mismatches"]) }},ensure_ascii=False,indent=2))

def scan_runs(p,loc,base,s):
    for ri,r in enumerate(p.findall(".//w:r",NS),1):
        rt=txt(r)
        if not rt.strip():continue
        rp=r.find("w:rPr",NS); sz=rp.find("w:sz",NS) if rp is not None else None
        pt=Decimal(sz.get(W+"val"))/2 if sz is not None and sz.get(W+"val") else base
        if pt is None:s["unresolved"].append({"location":loc,"run":ri,"text":rt[:100]})
        else:s["sizes"].append(float(pt))

if __name__=="__main__":main()
