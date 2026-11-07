import hashlib,json,re,sys
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
candidate=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03\candidate\0053_R03.docx')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def tag(k):return '{%s}%s'%(ns['w'],k)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
with ZipFile(candidate) as z:
 doc=etree.fromstring(z.read('word/document.xml')); styles=etree.fromstring(z.read('word/styles.xml'))
defaults=styles.xpath('./w:docDefaults/w:rPrDefault/w:rPr',namespaces=ns)
def size_from(node,tagname):
 vals=node.xpath(f'./w:rPr/w:{tagname}/@w:val',namespaces=ns) if node is not None and node.tag==tag('style') else node.xpath(f'./w:{tagname}/@w:val',namespaces=ns) if node is not None else []
 return int(vals[0]) if vals else None
default_rpr=defaults[0] if defaults else None
default_sz=default_rpr.xpath('./w:sz/@w:val',namespaces=ns) if default_rpr is not None else []
default_cs=default_rpr.xpath('./w:szCs/@w:val',namespaces=ns) if default_rpr is not None else []
default_sz=int(default_sz[0]) if default_sz else 22
default_cs=int(default_cs[0]) if default_cs else default_sz
style_map={s.get(tag('styleId')):s for s in styles.xpath('./w:style',namespaces=ns)}
def style_size(style_id,kind='sz'):
 seen=set()
 while style_id and style_id not in seen and style_id in style_map:
  seen.add(style_id); style=style_map[style_id]; vals=style.xpath(f'./w:rPr/w:{kind}/@w:val',namespaces=ns)
  if vals:return int(vals[0])
  base=style.xpath('./w:basedOn/@w:val',namespaces=ns);style_id=base[0] if base else None
 return default_cs if kind=='szCs' else default_sz
def in_table(node):
 while node is not None:
  if node.tag==tag('tc'):return True
  node=node.getparent()
 return False
runs=[]; used_styles=Counter()
for para in doc.xpath('.//w:body//w:p',namespaces=ns):
 ps=para.xpath('./w:pPr/w:pStyle/@w:val',namespaces=ns); sid=ps[0] if ps else 'Normal';used_styles[sid]+=1
 ppr=para.xpath('./w:pPr/w:rPr/w:sz/@w:val',namespaces=ns); psize=int(ppr[0]) if ppr else style_size(sid,'sz')
 pcs=para.xpath('./w:pPr/w:rPr/w:szCs/@w:val',namespaces=ns); pcsize=int(pcs[0]) if pcs else style_size(sid,'szCs')
 ptext=''.join(para.xpath('.//w:t/text()',namespaces=ns)).strip()
 for run in para.xpath('.//w:r',namespaces=ns):
  text=''.join(run.xpath('.//w:t/text()',namespaces=ns)).strip()
  if not text:continue
  direct=run.xpath('./w:rPr/w:sz/@w:val',namespaces=ns); point=int(direct[0]) if direct else psize
  directcs=run.xpath('./w:rPr/w:szCs/@w:val',namespaces=ns);pointcs=int(directcs[0]) if directcs else pcsize
  rec={'text':text,'pt':point/2,'complex_script_pt':pointcs/2,'paragraph_style':sid,'paragraph_text':ptext[:100]}
  runs.append((in_table(run),rec))
labels=re.compile(r'^(?:\d{2}\s|附錄\s*[A-Z]|附錄[A-Z]|附件\s*[A-Z]|附件[A-Z])')
body_low=[r for is_table,r in runs if not is_table and r['pt']<10.5]
table_low=[r for is_table,r in runs if is_table and r['pt']<9.5]
non_kicker=[r for r in body_low if not labels.match(r['text']) and not labels.match(r['paragraph_text'])]
table_styles=set(doc.xpath('.//w:tblPr/w:tblStyle/@w:val',namespaces=ns));low_table_style=[]
for sid in table_styles:
 if sid in style_map:
  for v in style_map[sid].xpath('.//w:tblStylePr/w:rPr/w:sz/@w:val|./w:rPr/w:sz/@w:val',namespaces=ns):
   if int(v)<19:low_table_style.append({'style':sid,'pt':int(v)/2})
small_style_defs=[]
for sid,s in style_map.items():
 sv=s.xpath('./w:rPr/w:sz/@w:val',namespaces=ns);sc=s.xpath('./w:rPr/w:szCs/@w:val',namespaces=ns)
 vals=[int(x) for x in sv+sc]
 if vals and min(vals)<19:small_style_defs.append({'style_id':sid,'name':(s.xpath('./w:name/@w:val',namespaces=ns) or [''])[0],'min_pt':min(vals)/2,'used_paragraph_count':used_styles.get(sid,0)})
report={'schema':'ttqs.0053.font_size_qa_receipt.v1','candidate_sha256':sha(candidate),'candidate_bytes':candidate.stat().st_size,'normal_style_run_pt':style_size('Normal','sz')/2,'doc_defaults_run_pt':default_sz/2,'doc_defaults_complex_script_pt':default_cs/2,'document_text_run_count':len(runs),'paragraph_style_usage':dict(used_styles),'section_kicker_min_pt':min([r['pt'] for r in body_low] or [0]),'section_kicker_runs_below_10_5pt':body_low,'non_kicker_body_runs_below_10_5pt':non_kicker,'minimum_table_text_run_pt':min([r['pt'] for is_table,r in runs if is_table] or [0]),'table_text_runs_below_9_5pt':table_low,'minimum_complex_script_run_pt':min([r['complex_script_pt'] for _,r in runs] or [0]),'table_styles_in_use':sorted(table_styles),'table_style_runs_below_9_5pt':low_table_style,'small_style_definitions_not_assumed_in_use':small_style_defs,'body_floor_pt':10.5,'table_floor_pt':9.5,'body_floor_status':'PASS' if not non_kicker else 'FAIL','table_floor_status':'PASS' if not table_low and not low_table_style else 'FAIL','status':'PASS' if not non_kicker and not table_low and not low_table_style else 'FAIL'}
path=candidate.parent.parent/'evidence'/'font_size_qa_receipt_R03.json'
with path.open('w',encoding='utf-8',newline='\n') as f:f.write(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('section_kicker_runs_below_10_5pt','small_style_definitions_not_assumed_in_use')},ensure_ascii=False,indent=2))
print('LOW_STYLE_DEFINITIONS',json.dumps(small_style_defs,ensure_ascii=False))
print('LOW_KICKER_TEXTS',json.dumps([r['text'] for r in body_low],ensure_ascii=False))

