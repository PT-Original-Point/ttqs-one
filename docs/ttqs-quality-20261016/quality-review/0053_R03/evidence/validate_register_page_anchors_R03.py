import csv, json, sys, unicodedata
from pathlib import Path
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
pdf=root/'evidence'/'render_final_R03'/'0053_R03_Word_export.pdf'
def norm(s): return ''.join(c for c in unicodedata.normalize('NFKC',s) if not c.isspace())
pages=[norm(p.extract_text() or '') for p in PdfReader(str(pdf)).pages]
rows=list(csv.DictReader((root/'SYNTHETIC_REPLACEMENT_REGISTER_0053_R03.csv').open(encoding='utf-8-sig',newline='')))
rules={
'SYN-0053-F016':['SYN-0033-PLAN-01'], 'SYN-0053-F017':['志工服務紀錄'], 'SYN-0053-F018':['L2','12個'],
'SYN-0053-F019':['G1','90分鐘'], 'SYN-0053-F020':['G2','90分鐘'], 'SYN-0053-F021':['G3','120分'], 'SYN-0053-F022':['G4','60分'],
'SYN-0053-F023':['360','教學分鐘'], 'SYN-0053-F024':['2026-10-03'], 'SYN-0053-F025':['2026-10-08'],
'SYN-0053-F026':['11/15','73.3%'], 'SYN-0053-F027':['14/15','93.3%'], 'SYN-0053-F028':['+20.0'],
'SYN-0053-F029':['6個合成'], 'SYN-0053-F030':['4/6','六個合成'], 'SYN-0053-F031':['5/6','83.3%'],
'SYN-0053-F032':['35+20+35=90','38.9%'], 'SYN-0053-F033':['20+20+50=90','55.6%'],
'SYN-0053-F034':['SYN-COORD','SYN-REVIEWER'], 'SYN-0053-F035':['SYN-VENUE-A'], 'SYN-0053-F036':['SYN-MAT-G1-G4'],
'SYN-0053-F037':['90%'], 'SYN-0053-F038':['14/15','未關閉'], 'SYN-0053-F039':['P0-SYN','本案合成計畫草稿版號'], 'SYN-0053-F040':['50%','P2']}
labels=['L1','L2','L3','M1','M2','M3','T1','T2','T3','P1','P2','P3','F1','F2','F3']
for i,label in enumerate(labels,1): rules[f'SYN-0053-F{i:03d}']=[label]
errors=[]
for row in rows:
 page=int(row['rendered_page'])-1; anchors=rules[row['fact_id']]
 missing=[a for a in anchors if norm(a) not in pages[page]]
 if missing: errors.append({'fact_id':row['fact_id'],'recorded_page':page+1,'missing':missing,'actual_pages':{a:[i+1 for i,p in enumerate(pages) if norm(a) in p] for a in missing}})
result={'pdf_pages':len(pages),'register_rows':len(rows),'page_anchor_pass':len(rows)-len(errors),'page_anchor_failures':errors}
print(json.dumps(result,ensure_ascii=False,indent=2))
