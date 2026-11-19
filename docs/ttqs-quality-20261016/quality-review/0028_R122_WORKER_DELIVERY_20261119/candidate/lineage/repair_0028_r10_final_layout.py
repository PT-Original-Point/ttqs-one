import copy,hashlib,json,os,re,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CANDIDATES\0028_I05-E02_R01")
src=base/'0028_I05-E02_CANDIDATE_R08.docx'; out=base/'0028_I05-E02_CANDIDATE_R10.docx'
expected='dc1e38ebdaa3a01ceb6974f1da824930e5cb641f98026a0eea243392cb7ce931'
if hashlib.sha256(src.read_bytes()).hexdigest()!=expected: raise SystemExit('R08_INPUT_SHA_MISMATCH')
if out.exists(): raise SystemExit('REFUSE_OVERWRITE_R10')
if (base/'BODY_ADOPTED_R10.md').exists() or (base/'SCOPED_REPAIR_R10.json').exists(): raise SystemExit('R10_OUTPUT_EXISTS')
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ET.register_namespace('w',W)
with zipfile.ZipFile(src) as z: infos=z.infolist(); files={i.filename:z.read(i.filename) for i in infos}
xml=files['word/document.xml']
for prefix,uri in re.findall(rb'xmlns(?::([A-Za-z0-9_]+))?=[\"\']([^\"\']+)',xml): ET.register_namespace(prefix.decode() if prefix else '',uri.decode())
ns={'w':W}; root=ET.fromstring(xml); body=root.find('w:body',ns)
def txt(e): return ''.join((t.text or '') for t in e.findall('.//w:t',ns))
def ppr(e,create=False):
 q=e.find('w:pPr',ns)
 if q is None and create: q=ET.Element(f'{{{W}}}pPr');e.insert(0,q)
 return q
blocks=list(body)
h6=next((e for e in blocks if e.tag==f'{{{W}}}p' and txt(e).startswith('6. ')),None)
h113=next((e for e in blocks if e.tag==f'{{{W}}}p' and txt(e).startswith('11.3 ')),None)
last_decision=next((e for e in blocks if e.tag==f'{{{W}}}p' and 'SYN-0028-024' in txt(e)),None)
if not all((h6,h113,last_decision)): raise SystemExit('LAYOUT_ANCHOR_MISSING')
# Prevent a table heading row from being left alone at a page bottom.
h6p=ppr(h6,True)
if h6p.find('w:pageBreakBefore',ns) is not None: raise SystemExit('SECTION_6_ALREADY_FORCED')
h6p.append(ET.Element(f'{{{W}}}pageBreakBefore'))
# Let §11.3 flow naturally; remove the exact forced break from R08.
h113p=ppr(h113)
if h113p is None or h113p.find('w:pageBreakBefore',ns) is None: raise SystemExit('R08_11_3_PAGEBREAK_MISSING')
h113p.remove(h113p.find('w:pageBreakBefore',ns))
# Remove the portrait section break between §11.3 and §12.1. The existing
# landscape section break after the §12.1 table then governs both sections.
idx=blocks.index(last_decision)
if idx+1>=len(blocks): raise SystemExit('POST_DECISION_BLOCK_MISSING')
secpara=blocks[idx+1]
if secpara.tag!=f'{{{W}}}p' or txt(secpara).strip(): raise SystemExit('POST_DECISION_NOT_EMPTY_SECTION_PARAGRAPH')
sec=secpara.find('./w:pPr/w:sectPr',ns)
if sec is None: raise SystemExit('POST_DECISION_SECTION_BREAK_MISSING')
pg=sec.find('w:pgSz',ns)
if pg is None or (pg.get(f'{{{W}}}w'),pg.get(f'{{{W}}}h'),pg.get(f'{{{W}}}orient'))!=('11909','16834',None): raise SystemExit('POST_DECISION_SECTION_NOT_PORTRAIT')
body.remove(secpara)
# Correct the register locator for the coverage and traceability values.
locator_old='第 5 章及第 11.3 節'; locator_new='第 6 章映射表、第 6.2 節及第 11.3 節'; locator_hits=0
for table in body.findall('w:tbl',ns):
 for row in table.findall('w:tr',ns):
  cells=row.findall('w:tc',ns)
  vals=[''.join((t.text or '') for t in c.findall('.//w:t',ns)) for c in cells]
  if len(vals)>=4 and vals[0]=='SYN-0028-022' and '覆蓋率 100.0％' in vals[1]:
   ts=cells[3].findall('.//w:t',ns)
   if not ts or ''.join((t.text or '') for t in ts)!=locator_old: raise SystemExit('REGISTER_LOCATOR_SOURCE_MISMATCH')
   ts[0].text=locator_new
   for t in ts[1:]: t.text=''
   locator_hits+=1
if locator_hits!=1: raise SystemExit(f'REGISTER_LOCATOR_HITS_{locator_hits}')
marks=[]
for t in root.findall('.//w:t',ns):
 s=t.text or ''
 if s=='：R08': t.text='：R10';marks.append('R10')
 elif s.startswith('：V1.3（SAMPLE/SYNTHETIC 工作稿）'): t.text=s.replace('：V1.3（','：V1.5（',1);marks.append('V1.5')
if marks!=['R10','V1.5']: raise SystemExit('VERSION_MARKER_FAILURE '+repr(marks))
history=None;oldrow=None
for table in body.findall('w:tbl',ns):
 for row in table.findall('w:tr',ns):
  cells=row.findall('w:tc',ns); vals=[''.join((t.text or '') for t in c.findall('.//w:t',ns)) for c in cells]
  if len(vals)==4 and vals[0]=='V1.3': history,oldrow=table,row; break
 if oldrow is not None: break
if oldrow is None: raise SystemExit('V1_3_HISTORY_ROW_MISSING')
for version,date,summary in [
 ('V1.4','2026-11-17','調整 11.3 決策紀錄與 12.1 附表的版面分頁'),
 ('V1.5','2026-11-17','修正 §6 表格起頁、11.3/12.1 連續版面及合成登錄定位')]:
 row=copy.deepcopy(oldrow); values=[version,date,summary,'合成示例；無真實核定']
 for c,v in zip(row.findall('w:tc',ns),values):
  ts=c.findall('.//w:t',ns)
  if not ts: raise SystemExit('HISTORY_TEXT_MISSING')
  ts[0].text=v
  for t in ts[1:]: t.text=''
 history.append(row)
modified=ET.tostring(root,encoding='utf-8',xml_declaration=True)
def header(b):
 s=b.find(b'<w:document '); e=b.find(b'>',s)
 if s<0 or e<0: raise SystemExit('ROOT_HEADER_MISSING')
 return b[s:e+1],e+1
oldhead,_=header(xml); _,newend=header(modified); pos=modified.find(b'<w:document '); modified=modified[:pos]+oldhead+modified[newend:]
files['word/document.xml']=modified
tmp=out.with_suffix('.tmp.docx')
if tmp.exists(): raise SystemExit('REFUSE_TEMP_OVERWRITE')
with zipfile.ZipFile(src) as zin,zipfile.ZipFile(tmp,'x') as zout:
 for info in zin.infolist(): zout.writestr(info,files[info.filename])
with zipfile.ZipFile(tmp) as z:
 bad=z.testzip()
 if bad: raise SystemExit('ZIP_TEST_FAIL '+str(bad))
sha=hashlib.sha256(tmp.read_bytes()).hexdigest()
# Refuse replacement if another writer created the destination during this run.
if out.exists(): raise SystemExit('R10_DESTINATION_APPEARED')
os.rename(tmp,out)
body08=(base/'BODY_ADOPTED_R08.md').read_text(encoding='utf-8')
if '**候選稿次**：R08' not in body08 or '**版本**：V1.3（SAMPLE/SYNTHETIC 工作稿）' not in body08: raise SystemExit('BODY_MARKER_MISMATCH')
body10=body08.replace('**候選稿次**：R08','**候選稿次**：R10',1).replace('**版本**：V1.3（SAMPLE/SYNTHETIC 工作稿）','**版本**：V1.5（SAMPLE/SYNTHETIC 工作稿）',1)
if locator_old not in body10: raise SystemExit('BODY_LOCATOR_MISSING')
body10=body10.replace(locator_old,locator_new,1)
body10+='\n| V1.4 | 2026-11-17 | 調整 11.3 決策紀錄與 12.1 附表的版面分頁 | 合成示例；無真實核定 |\n| V1.5 | 2026-11-17 | 修正 §6 表格起頁、11.3/12.1 連續版面及合成登錄定位 | 合成示例；無真實核定 |\n'
(base/'BODY_ADOPTED_R10.md').write_text(body10,encoding='utf-8')
receipt={'work_id':'TTQS_ONE_0028_I05-E02_SCOPED_REPAIR_R10_20261117','doc_id':'0028_I05-E02','requirement_id':'I05-E02','input_candidate':'0028_I05-E02_CANDIDATE_R08.docx','input_candidate_sha256':expected,'supersedes_failed_visual_attempt':{'candidate':'0028_I05-E02_CANDIDATE_R09.docx','candidate_sha256':'f8f9ba78b1224cf738e8dd06f96fbcd6cda521287a71900a7b18bf6b1dc1f2d6','visual_review_sha256':'2a914fac5f02b7ed48beb4810daa382f440ff486555a686cef9de954a460acf0'},'candidate':'0028_I05-E02_CANDIDATE_R10.docx','candidate_sha256':sha,'body_sha256':hashlib.sha256(body10.encode('utf-8')).hexdigest(),'changes':['Set page break before §6 heading to keep its table header with content.','Removed forced page break before §11.3.','Removed portrait section break after §11.3 so §11.3 and §12.1 flow in the landscape section ending after the §12.1 table.','Corrected SYN-0028-022 locator to §6 mapping table, §6.2 and §11.3.','Updated candidate/version markers and synthetic revision history.'],'font_sizes_changed':False,'status':'PATCH_CREATED_PENDING_DETERMINISTIC_QA_WORD_VISUAL_AND_FRESH_SEMANTIC_REVIEW'}
(base/'SCOPED_REPAIR_R10.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
