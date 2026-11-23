#!/usr/bin/env python3
"""Deterministic OOXML effective-font floor audit for TTQS ONE DOCX candidates."""
import argparse, hashlib, json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from docx import Document
from lxml import etree

NS={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def read_size(rpr, tag):
    el=rpr.find("w:"+tag,NS) if rpr is not None else None
    if el is None: return None
    try: return int(el.get("{%s}val"%NS["w"])) / 2
    except (TypeError,ValueError): return None

def effective(run, para, defaults, tag):
    value=read_size(run._r.rPr,tag)
    if value is not None: return value,"run"
    style=run.style; seen=set()
    while style is not None and style.style_id not in seen:
        seen.add(style.style_id)
        value=read_size(style._element.rPr,tag)
        if value is not None: return value,"character_style:"+style.style_id
        style=style.base_style
    style=para.style; seen=set()
    while style is not None and style.style_id not in seen:
        seen.add(style.style_id)
        value=read_size(style._element.rPr,tag)
        if value is not None: return value,"paragraph_style:"+style.style_id
        style=style.base_style
    value=read_size(defaults,tag)
    if value is not None: return value,"document_defaults"
    return None,"unresolved"

def table_paragraphs(table):
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs: yield paragraph
            for nested in cell.tables: yield from table_paragraphs(nested)

def audit(path, is_table, defaults, floor):
    d=Document(str(path)); paragraphs=[]
    if is_table:
        for table in d.tables: paragraphs.extend(table_paragraphs(table))
    else:
        paragraphs=list(d.paragraphs)
    checked=unresolved=below=0; minimum=None; sources={}; examples=[]
    for paragraph in paragraphs:
        for run in paragraph.runs:
            if not run.text.strip(): continue
            for tag in ("sz","szCs"):
                size,source=effective(run,paragraph,defaults,tag)
                if size is None: unresolved+=1; continue
                checked+=1; minimum=size if minimum is None else min(minimum,size)
                sources[source]=sources.get(source,0)+1
                if size<floor:
                    below+=1
                    if len(examples)<10: examples.append({"pt":size,"channel":tag,"source":source,"text":run.text[:60]})
    return {"floor_pt":floor,"run_size_channels_checked":checked,"unresolved_channel_count":unresolved,"minimum_effective_pt":minimum,"below_floor_count":below,"below_floor_examples":examples,"resolved_from":sources}

def main():
    p=argparse.ArgumentParser()
    for key in ("doc-id","requirement-id","candidate","source-packet-sha256","blueprint-sha256","technical-receipt","visual-receipt","semantic-receipt","github-commit","github-doc-path","github-blob-sha1","github-sha256","output"):
        p.add_argument("--"+key,required=True)
    a=p.parse_args(); path=Path(a.candidate); data=path.read_bytes(); candidate_sha=hashlib.sha256(data).hexdigest()
    with __import__("zipfile").ZipFile(path) as z:
        styles=etree.fromstring(z.read("word/styles.xml")); defaults=styles.find("w:docDefaults/w:rPrDefault/w:rPr",NS)
    script_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result={"schema":"TTQS_ONE_DOCX_FONT_FLOOR_AUDIT_R12_V1","project_id":"TTQS_ONE","work_id":"TTQS_ONE_"+a.doc_id+"_R12_FONT_FLOOR_AUDIT_20261031","observed_at_taipei":datetime.now().astimezone().isoformat(),"doc_id":a.doc_id,"requirement_id":a.requirement_id,"candidate_state":"CANDIDATE_NOT_FORMALLY_ACCEPTED","candidate_path":str(path),"candidate_bytes":len(data),"candidate_sha256":candidate_sha,"source_packet_sha256":a.source_packet_sha256,"unique_blueprint_sha256":a.blueprint_sha256,"technical_receipt_sha256":hashlib.sha256(Path(a.technical_receipt).read_bytes()).hexdigest(),"visual_receipt_sha256":hashlib.sha256(Path(a.visual_receipt).read_bytes()).hexdigest(),"semantic_receipt_sha256":hashlib.sha256(Path(a.semantic_receipt).read_bytes()).hexdigest(),"audit_script_sha256":script_sha,"method":"Resolve w:sz and w:szCs independently by direct run properties, character-style inheritance, paragraph-style inheritance, then document defaults; inspect text-bearing body paragraphs and all top-level/nested table cells; no DOCX write operation.","body":audit(path,False,defaults,10.5),"tables":audit(path,True,defaults,9.5),"github_raw_readback":{"repository":"PT-Original-Point/ttqs-one","commit":a.github_commit,"path":a.github_doc_path,"blob_sha1":a.github_blob_sha1,"raw_sha256":a.github_sha256,"exact_local_remote_match":candidate_sha==a.github_sha256},"formal_acceptance":"NOT_GRANTED","real_evidence":"NOT_ASSERTED"}
    result["status"]="PASS_WITHIN_FONT_FLOOR_SCOPE" if result["body"]["unresolved_channel_count"]==0 and result["tables"]["unresolved_channel_count"]==0 and result["body"]["below_floor_count"]==0 and result["tables"]["below_floor_count"]==0 and result["github_raw_readback"]["exact_local_remote_match"] else "FAIL_OR_UNVERIFIED"
    out=Path(a.output)
    if out.exists(): raise SystemExit("Refusing to overwrite existing receipt: "+str(out))
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"receipt":str(out),"status":result["status"],"candidate_sha256":candidate_sha,"audit_script_sha256":script_sha,"body":result["body"],"tables":result["tables"]},ensure_ascii=False))
if __name__=="__main__": main()

