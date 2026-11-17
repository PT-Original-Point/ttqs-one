import hashlib, json, re, sys, zipfile
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(r"E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0034_I07-E02_SOURCE_PREP_R01_20261118")
CAND = BASE / "candidate" / "0034_I07-E02_R01_W1_NEMOTRON.docx"
OUT = CAND.parent / "qa" / "static_qa_r01_independent"
BUILD = CAND.parent / "qa" / "build_r01" / "BUILD_RECEIPT_0034_I07-E02_R01.json"
WORKER = BASE / "writer" / "attempt_0034_W1_R01" / "stdout.jsonl"
EXPECTED = "94604D86AF257A902385D28CCF988D1F62253439DAEED7979C984FF23DA0D076"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
Q = lambda s: "{" + NS["w"] + "}" + s
ID_RE = re.compile(r"SYN-0034-\d{3}[A-Za-z0-9]*")
PLACE_RE = re.compile(r"待填|待核|待確認|待補|會後填寫|保持空白|空白表|\bblank\b", re.I)

def sha(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""): h.update(b)
    return h.hexdigest().upper()

def text(el):
    return "".join((x.text or "") for x in el.iter(Q("t")))

def status(ok): return "PASS" if ok else "FAIL"

def main():
    if not OUT.is_dir(): raise RuntimeError("Authorized output directory absent")
    before = sha(CAND)
    build_obj = json.loads(BUILD.read_text(encoding="utf-8"))
    build_sha = sha(BUILD)
    worker_sha = sha(WORKER)
    result = {"qa_type":"DETERMINISTIC_DOCX_STATIC_QA", "doc_id":"0034", "requirement_id":"I07-E02",
              "candidate_path":str(CAND), "expected_candidate_sha256":EXPECTED, "observed_candidate_sha256_before":before,
              "build_receipt_path":str(BUILD), "build_receipt_sha256":build_sha,
              "worker_stdout_path":str(WORKER), "worker_stdout_sha256":worker_sha,
              "started_utc":datetime.now(timezone.utc).isoformat(), "gates":{}, "findings":{}}
    result["gates"]["exact_sha"] = status(before == EXPECTED and build_obj.get("output_sha256", "").upper() == EXPECTED)
    result["findings"]["build_receipt_output_sha_matches_expected"] = build_obj.get("output_sha256", "").upper() == EXPECTED
    z_ok = False
    try:
        with zipfile.ZipFile(CAND) as z:
            bad = z.testzip()
            names = set(z.namelist())
            required = {"[Content_Types].xml", "word/document.xml", "word/styles.xml"}
            missing = sorted(required - names)
            xml_errors = []
            for n in sorted(names):
                if n.endswith((".xml", ".rels")):
                    try: ET.fromstring(z.read(n))
                    except Exception as e: xml_errors.append({"part":n,"error":str(e)})
            z_ok = bad is None and not missing and not xml_errors
            doc = ET.fromstring(z.read("word/document.xml")) if "word/document.xml" in names else None
            styles_root = ET.fromstring(z.read("word/styles.xml")) if "word/styles.xml" in names else None
    except Exception as e:
        bad, missing, xml_errors, doc, styles_root = str(e), [], [], None, None
    result["gates"]["zip_docx_openable"] = status(z_ok)
    result["findings"]["zip"] = {"bad_member":bad,"missing_required_parts":missing,"xml_parse_errors":xml_errors}
    if doc is None: raise RuntimeError("Cannot inspect document.xml; receipt not emitted")

    styles = {}
    default_pt = None
    if styles_root is not None:
        dd = styles_root.find("w:docDefaults/w:rPrDefault/w:rPr/w:sz", NS)
        if dd is not None and dd.get(Q("val")): default_pt = Decimal(dd.get(Q("val"))) / 2
        for st in styles_root.findall("w:style", NS):
            sid = st.get(Q("styleId")); based = st.find("w:basedOn", NS)
            sz = st.find("w:rPr/w:sz", NS)
            styles[sid] = {"based":based.get(Q("val")) if based is not None else None,
                           "pt":Decimal(sz.get(Q("val")))/2 if sz is not None and sz.get(Q("val")) else None}
    def style_pt(sid, seen=None):
        seen = seen or set()
        if not sid or sid in seen or sid not in styles: return None
        seen.add(sid); x=styles[sid]
        return x["pt"] if x["pt"] is not None else style_pt(x["based"], seen)
    body = doc.find("w:body", NS)
    paras=[]; tables=[]
    for child in list(body):
        if child.tag == Q("p"): paras.append(child)
        elif child.tag == Q("tbl"): tables.append(child)
    def paragraph_data(p, loc, kind, stats):
        txt=text(p); stats["paragraph_count"]+=1
        if not txt.strip(): stats["empty_paragraphs"].append(loc)
        ppr=p.find("w:pPr",NS); ps=ppr.find("w:pStyle",NS) if ppr is not None else None
        sid=ps.get(Q("val")) if ps is not None else None
        psize=ppr.find("w:rPr/w:sz",NS) if ppr is not None else None
        inherited=(Decimal(psize.get(Q("val")))/2 if psize is not None and psize.get(Q("val")) else style_pt(sid)) or default_pt
        runs=p.findall(".//w:r",NS)
        for ri,r in enumerate(runs):
            rt=text(r)
            if not rt.strip(): continue
            rpr=r.find("w:rPr",NS); sz=rpr.find("w:sz",NS) if rpr is not None else None
            pt=Decimal(sz.get(Q("val")))/2 if sz is not None and sz.get(Q("val")) else inherited
            stats["runs"]+=1
            if pt is None: stats["unresolved_runs"].append({"location":loc,"run":ri,"text":rt[:80]})
            else: stats["sizes"].append(float(pt))
        return txt
    stats={"body":{"paragraph_count":0,"runs":0,"sizes":[],"unresolved_runs":[],"empty_paragraphs":[]},
           "table":{"paragraph_count":0,"runs":0,"sizes":[],"unresolved_runs":[],"empty_paragraphs":[]}}
    body_text=[]; table_texts=[]; cell_blanks=[]; row_blanks=[]; table_rows=[]
    for pi,p in enumerate(paras,1): body_text.append(paragraph_data(p,f"body/p{pi}","body",stats["body"]))
    for ti,t in enumerate(tables,1):
        rows=[]; tblparts=[]
        for ri,row in enumerate(t.findall("w:tr",NS),1):
            cells=[]
            for ci,cell in enumerate(row.findall("w:tc",NS),1):
                ps=cell.findall(".//w:p",NS)
                ct=[]
                for pj,p in enumerate(ps,1): ct.append(paragraph_data(p,f"table{ti}/r{ri}/c{ci}/p{pj}","table",stats["table"]))
                val="".join(ct); cells.append(val)
                if not val.strip(): cell_blanks.append(f"table{ti}/r{ri}/c{ci}")
            rows.append(cells)
            if not "".join(cells).strip(): row_blanks.append(f"table{ti}/r{ri}")
            tblparts.extend(cells)
        table_rows.append(rows); table_texts.append("\n".join(tblparts))
    whole="\n".join(body_text+table_texts)
    for k,minimum in (("body",10.5),("table",9.5)):
        vals=stats[k]["sizes"]
        stats[k]["min_pt"]=min(vals) if vals else None
        stats[k]["below_min_run_count"]=sum(x<minimum for x in vals)
        stats[k]["threshold_pt"]=minimum
        stats[k]["paragraph_count_with_text"]=sum(1 for p in (paras if k=="body" else []) if text(p).strip()) if k=="body" else None
    result["findings"]["font_sizes"]=stats
    result["gates"]["body_font_min_10_5pt"] = status(bool(stats["body"]["sizes"]) and not stats["body"]["below_min_run_count"] and not stats["body"]["unresolved_runs"])
    result["gates"]["table_font_min_9_5pt"] = status(bool(stats["table"]["sizes"]) and not stats["table"]["below_min_run_count"] and not stats["table"]["unresolved_runs"])
    result["findings"]["structure"]={"body_paragraphs_top_level":len(paras),"tables":len(tables),"table_row_counts":[len(x) for x in table_rows],
        "empty_body_paragraphs":stats["body"]["empty_paragraphs"],"empty_table_paragraphs":stats["table"]["empty_paragraphs"],
        "empty_table_cells":cell_blanks,"empty_table_rows":row_blanks}
    sample={"document_sample":bool(re.search(r"SAMPLE|SYNTHETIC",whole,re.I)),"document_real_boundary":bool(re.search(r"REAL",whole,re.I)),
            "sample_occurrences":len(re.findall(r"SAMPLE|SYNTHETIC",whole,re.I))}
    result["findings"]["sample_real_markers"]=sample
    result["gates"]["sample_marking"] = status(sample["document_sample"] and sample["document_real_boundary"])

    # Placeholder hits are retained with context; explicit negations are separated from live fill instructions.
    hits=[]
    for ix,m in enumerate(PLACE_RE.finditer(whole)):
        a=max(0,m.start()-65); b=min(len(whole),m.end()+65); ctx=whole[a:b].replace("\n"," ")
        neg=bool(re.search(r"未留|不得|不需|不應|不提供|不可|禁止|無須|沒有|not\s+blank|no\s+blank",ctx,re.I))
        hits.append({"term":m.group(),"context":ctx,"classified":("negated_instruction_or_claim" if neg else "possible_live_placeholder")})
    possible=[x for x in hits if x["classified"]=="possible_live_placeholder"]
    result["findings"]["placeholder_scan"]={"all_hits":hits,"possible_live_placeholder_count":len(possible)}
    result["gates"]["no_live_placeholder"] = status(not possible)

    # Register tables are identified from their header row; only the first ID column is authoritative.
    reg_tables=[]; reg_ids=set(); primary_ids=set(); reg_rows=[]; duplicates=[]; missing_fields=[]
    for ti,rows in enumerate(table_rows,1):
        if not rows: continue
        hdr=" ".join(rows[0]).casefold()
        if not ("事實id" in hdr or "fact_id" in hdr or "synthetic id" in hdr or "合成識別碼" in hdr): continue
        reg_tables.append(ti)
        headers=rows[0]
        for ri,cells in enumerate(rows[1:],2):
            first=cells[0] if cells else ""
            matches=ID_RE.findall(first)
            primary_ids.update(matches)
            ids=set(matches)
            # Expand only explicit same-prefix numeric ranges in the register's ID cell.
            ranges=re.findall(r"SYN-0034-(\d{3})\s*[-–—至到]\s*SYN-0034-(\d{3})",first)
            for lo,hi in ranges:
                for n in range(int(lo),int(hi)+1): ids.add(f"SYN-0034-{n:03d}")
            if ids:
                dup=sorted(reg_ids & ids)
                if dup: duplicates.extend(dup)
                reg_ids.update(ids); reg_rows.append({"table":ti,"row":ri,"ids":sorted(ids)})
                for ci,h in enumerate(headers):
                    if any(k in h.casefold() for k in ("登錄事實","目前狀態","required real","source/location","備註","replacement")):
                        if ci>=len(cells) or not cells[ci].strip(): missing_fields.append({"table":ti,"row":ri,"field":h})
    doc_ids=set(ID_RE.findall(whole))
    outside_ids=set()
    # Remove register-only mentions by scanning top-level paragraphs and non-register tables.
    for p in paras: outside_ids.update(ID_RE.findall(text(p)))
    for ti,t in enumerate(table_texts,1):
        if ti not in reg_tables: outside_ids.update(ID_RE.findall(t))
    unregistered=sorted(outside_ids-reg_ids)
    unused=sorted(reg_ids-doc_ids)
    worker_txt=WORKER.read_text(encoding="utf-8",errors="replace")
    claims=[int(x) for x in re.findall(r"(\d+)\s+unique\s+`?SYN-0034-[^\n]{0,80}?\bIDs?",worker_txt,re.I)]
    claim=57 if re.search(r"57 unique `?SYN-0034-",worker_txt,re.I) else (claims[0] if claims else None)
    result["findings"]["synthetic_register"]={"unique_id_count_in_document":len(doc_ids),"unique_ids_in_document":sorted(doc_ids),
        "unique_explicit_register_primary_column_id_count":len(primary_ids),"explicit_register_primary_column_ids":sorted(primary_ids),
        "range_expanded_unique_register_id_count":len(reg_ids),"register_ids":sorted(reg_ids),"register_tables":reg_tables,
        "register_rows":reg_rows,"duplicate_register_ids":sorted(set(duplicates)),"unregistered_ids_used_outside_register":unregistered,
        "registered_ids_not_found_in_document":unused,"missing_replacement_register_fields":missing_fields,
        "worker_claimed_unique_id_count":claim,"worker_claim_matches_doc_unique_count":claim==len(doc_ids),
        "build_receipt_listed_synthetic_id_count":build_obj.get("synthetic_identifier_count"),
        "build_receipt_listed_synthetic_id_values_count":len(build_obj.get("synthetic_identifier_values",[]))}
    result["gates"]["synthetic_ids_registered"] = status(bool(reg_tables) and not unregistered and not missing_fields and not duplicates)
    result["gates"]["worker_id_count_claim_matches"] = status(claim==len(doc_ids)) if claim is not None else "UNKNOWN"

    # Recompute rows in the comparison table using its named target/current/gap columns.
    checks=[]
    def first_number(s):
        m=re.search(r"-?\d+(?:\.\d+)?",s.replace(",",""))
        return Decimal(m.group()) if m else None
    for ti,rows in enumerate(table_rows,1):
        if not rows: continue
        hdr=[x.casefold() for x in rows[0]]
        target=next((i for i,x in enumerate(hdr) if "目標程度" in x),None)
        current=next((i for i,x in enumerate(hdr) if "目前程度" in x),None)
        gap=next((i for i,x in enumerate(hdr) if "差距" in x),None)
        if None in (target,current,gap): continue
        for ri,cells in enumerate(rows[1:],2):
            if max(target,current,gap)>=len(cells): continue
            a=first_number(cells[target]); b=first_number(cells[current]); c=first_number(cells[gap])
            if a is not None and b is not None and c is not None:
                expect=a-b; checks.append({"location":f"table{ti}/r{ri}","target":str(a),"current":str(b),"reported_gap":str(c),"expected_gap":str(expect),"pass":expect==c})
    # Recompute embedded narrative forms with a labelled current operand.
    for m in re.finditer(r"(目標\s*)(\d+(?:\.\d+)?)\s*[−–—-]\s*(?:現況|目前程度)\s*(\d+(?:\.\d+)?)\s*=\s*(\d+(?:\.\d+)?)",whole):
        a,b,c=map(Decimal,m.groups()[1:]); expect=a-b
        checks.append({"expression":m.group(),"expected_gap":str(expect),"reported_gap":str(c),"pass":expect==c})
    # Check explicit three-part cohort sums, if stated as an equality.
    for m in re.finditer(r"(\d+)\s*\+\s*(\d+)\s*\+\s*(\d+)\s*=\s*(\d+)",whole):
        nums=list(map(int,m.groups())); checks.append({"expression":m.group(),"expected":sum(nums[:3]),"pass":sum(nums[:3])==nums[3]})
    result["findings"]["arithmetic"]={"checks":checks,"checked_count":len(checks),"mismatches":[x for x in checks if not x["pass"]]}
    result["gates"]["visible_basic_arithmetic"] = status(bool(checks) and all(x["pass"] for x in checks)) if checks else "UNKNOWN"
    result["gates"]["table_cells_and_rows_nonempty"] = status(not cell_blanks and not row_blanks)
    result["findings"]["extracted_text"]={"body_characters":sum(map(len,body_text)),"table_characters":sum(map(len,table_texts)),
        "body_nonempty_paragraph_count":sum(1 for p in paras if text(p).strip()),"table_nonempty_cell_count":sum(1 for rows in table_rows for row in rows for c in row if c.strip())}
    result["findings"]["scope_note"]="Deterministic static checks only; no Rawls source-alignment/semantic review, Word COM, render, or visual-pagination claim."
    after=sha(CAND)
    result["observed_candidate_sha256_after"]=after
    result["gates"]["candidate_unchanged_during_qa"] = status(after==before==EXPECTED)
    result["completed_utc"]=datetime.now(timezone.utc).isoformat()
    result["overall_status"]="PASS" if all(v=="PASS" for v in result["gates"].values()) else "FAIL"
    result["script_path"]=str(Path(__file__).resolve()); result["script_sha256"]=sha(Path(__file__))
    receipt=OUT/"STATIC_QA_RECEIPT_R01.json"
    receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"receipt":str(receipt),"status":result["overall_status"],"gates":result["gates"],
        "candidate_sha256":after,"script_sha256":result["script_sha256"],"receipt_sha256":sha(receipt),
        "synthetic_register":result["findings"]["synthetic_register"],"font_sizes":result["findings"]["font_sizes"],
        "structure":result["findings"]["structure"],"arithmetic":result["findings"]["arithmetic"]},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
