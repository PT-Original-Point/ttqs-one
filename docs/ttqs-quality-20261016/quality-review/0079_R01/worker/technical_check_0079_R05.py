from __future__ import annotations
import csv, hashlib, json, re, zipfile
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
ROOT=Path(__file__).resolve().parents[1]
DOCX=ROOT/'candidate/0079_R05.docx'
BODY=ROOT/'candidate/0079_R01_body.md'
CASES=ROOT/'inputs/SYNTHETIC_GUIDANCE_CASES_0079_R01.csv'
REGISTER=ROOT/'inputs/SYNTHETIC_REPLACEMENT_REGISTER_0079_R01.csv'
EXTRACT=ROOT/'evidence/docx_extracted_R05.md'
RECEIPT=ROOT/'evidence/technical_review_R05.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def iter_blocks(doc):
    for child in doc.element.body.iterchildren():
        if child.tag==qn('w:p'): yield Paragraph(child,doc)
        elif child.tag==qn('w:tbl'): yield Table(child,doc)
def norm(s): return re.sub(r'\s+',' ',s).strip()
def main():
    zerr=None
    try:
        with zipfile.ZipFile(DOCX) as z:
            bad=z.testzip(); required={'[Content_Types].xml','word/document.xml','word/styles.xml'}
            missing=sorted(required-set(z.namelist()))
    except Exception as e: bad=str(e); missing=[]
    doc=Document(DOCX); ext=[]; tables=0; paragraphs=0
    for b in iter_blocks(doc):
        if isinstance(b,Paragraph):
            s=norm(b.text)
            if s: ext.append(s); paragraphs+=1
        else:
            tables+=1
            ext.append('\n'+'\n'.join('| '+' | '.join(norm(c.text) for c in row.cells)+' |' for row in b.rows)+'\n')
    text='\n'.join(ext)
    EXTRACT.write_text(text+'\n',encoding='utf-8',newline='\n')
    cases=list(csv.DictReader(CASES.open(encoding='utf-8-sig',newline='')))
    reg=list(csv.DictReader(REGISTER.open(encoding='utf-8-sig',newline='')))
    raw=BODY.read_text(encoding='utf-8-sig')
    sections={}
    matches=list(re.finditer(r'^### (P0[1-4])\b.*$',raw,re.M))
    for i,m in enumerate(matches): sections[m.group(1)]=raw[m.end():matches[i+1].start() if i+1<len(matches) else len(raw)]
    fact_checks={}
    for row in cases:
        code=row['learner_token']; sec=sections.get(code,'')
        wr=int(row['source_written_score'].split('/')[0]); pr=int(row['source_practical_total'].split('/')[0])
        fact_checks[code]={
          'written_score':bool(re.search(rf'{wr}\s*[／/]\s*100',sec)),
          'practical_score':bool(re.search(rf'{pr}\s*[／/]\s*20',sec)),
          'reflection_theme':row['source_reflection_theme'] in sec,
          'case_link':row['sample_case_id'] in sec or row['sample_case_id'] in raw,
          'assessment_status':row['source_practical_status'] in sec or ('HOLD' in sec and row['source_practical_status'].startswith('HOLD'))
        }
    body_han=len(re.findall(r'[\u3400-\u9fff]',raw))
    checks={
      'zip_integrity':bad is None,'required_ooxml_parts':not missing,
      'body_title':doc.core_properties.title=='訓後個別職涯與學習規劃建議表 0079 I17B-E01',
      'correct_requirement_and_checkbox':'I17B-E01' in text and '084' in text,
      'four_sample_cases':len(cases)==4 and set(r['learner_token'] for r in cases)=={'P01','P02','P03','P04'},
      'replacement_register_rows':len(reg)==104,
      'sample_real_boundary':'SAMPLE/SYNTHETIC' in text and 'REAL=UNKNOWN/HOLD' in text,
      'formal_status_hold':'NOT_GRANTED' in text and 'PARTIAL/HOLD' in text,
      'no_photo_crosswalk':'A01' in text and 'A08' in text and '不得' in text,
      'writer_body_7000_10000_han':7000<=body_han<=10000,
      'all_case_source_facts':all(all(v.values()) for v in fact_checks.values()),
      'p03_hold_with_14_of_20':('P03' in text and re.search(r'14\s*[／/]\s*20',text) is not None and 'HOLD_SAMPLE_RULE' in text),
      'blank_form_and_followup':'可複製使用的空白個別建議表' in raw and '訓後追蹤表' in raw,
    }
    receipt={'schema':'TTQS_ONE_0079_TECHNICAL_REVIEW_R05.v1','document_id':'0079','requirement_id':'I17B-E01','official_checkbox_serial':'084','docx_path':str(DOCX),'docx_sha256':sha(DOCX),'docx_bytes':DOCX.stat().st_size,'worker_body_sha256':sha(BODY),'worker_body_han_characters':body_han,'extracted_text_sha256':sha(EXTRACT),'extracted_text_path':str(EXTRACT),'paragraphs':paragraphs,'tables':tables,'sample_cases':len(cases),'replacement_register_rows':len(reg),'case_source_fact_checks':fact_checks,'checks':checks,'zip_bad_member':bad,'missing_ooxml_parts':missing,'status':'PASS' if all(checks.values()) else 'FAIL','builder_self_report_is_not_semantic_acceptance':True,'formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD'}
    RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'docx_sha256':receipt['docx_sha256'],'status':receipt['status'],'failed':[k for k,v in checks.items() if not v],'paragraphs':paragraphs,'tables':tables,'han_chars':body_han},ensure_ascii=False))
if __name__=='__main__': main()
