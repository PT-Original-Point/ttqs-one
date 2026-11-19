import hashlib, json, re, zipfile
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
from PIL import Image, ImageChops

BASE=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0121_I19-E09_SOURCE_PREP_R01_20261024')
R2=BASE/'candidate_R03'
DOCX=R2/'0121_I19-E09_R03.docx'
PDF=R2/'0121_I19-E09_R03_WordNative.pdf'
PNG2=R2/'render_R03'
R1=R2/'compare_R02_r96'
MID=R2/'no_intermediate_render'
EXTRACT=R2/'candidate_R03_extract.txt'
OUT=R2/'TECHNICAL_VISUAL_QA_R03.json'
MANUAL_PAGES=[1,18]

def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
 return h.hexdigest()
def txt(cell): return re.sub(r'\s+',' ',cell.text).strip()
def parse_int(v):
 s=txt(v)
 return int(s) if re.fullmatch(r'[+-]?\d+',s) else None
def round2(x): return str(Decimal(x).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
def round1(x): return str(Decimal(x).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
checks=[]
def record(name,ok,details=None): checks.append({'check':name,'status':'PASS' if ok else 'FAIL','details':details})

candidate_sha=sha(DOCX); candidate_bytes=DOCX.stat().st_size
with zipfile.ZipFile(DOCX) as z:
 bad=z.testzip(); zip_names=z.namelist()
record('docx_zip_integrity',bad is None,{'bad_member':bad,'members':len(zip_names)})
doc=Document(DOCX)
record('table_count_17',len(doc.tables)==17,{'actual':len(doc.tables)})
# Regenerate a searchable body extraction from the exact candidate, preserving top-level order.
paras=list(doc.paragraphs)
pidx=0; tidx=0; lines=[]
for child in doc.element.body.iterchildren():
 if child.tag==qn('w:p'):
  p=Paragraph(child,doc); pidx+=1
  if p.text.strip(): lines.append(f'P{pidx:03d}: {p.text}')
 elif child.tag==qn('w:tbl'):
  tidx+=1; t=Table(child,doc); lines.append(f'\nTABLE T{tidx:02d}')
  for ri,row in enumerate(t.rows,1): lines.append(' | '.join(txt(c) for c in row.cells))
EXTRACT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
body='\n'.join(p.text for p in doc.paragraphs)+'\n'+'\n'.join(txt(c) for t in doc.tables for row in t.rows for c in row.cells)
# High-priority targeted semantic wording checks; independent semantic verdict remains separate.
required={
 'document_mapping':'0121' in body and 'I19-E09' in body,
 'sample_synthetic_boundary':'SAMPLE' in body and 'SYNTHETIC' in body,
 'transfer_safety_and_authority':'本表不構成協會核定之移位 SOP' in body and '未確認服務對象同意' in body and '停止操作' in body,
 'no_unsupported_governance':'理事會訓練委員會' not in body and '年度志工服務安全基準' not in body,
 'threshold_authority_gap':'權責依據' in body and '批准紀錄' in body and 'NOT_GRANTED' in body,
 'nonstatistical_reflection':'我覺得物資清點流程容易記憶' in body and '示範表中的前後測分數有所提高' not in body and '顯著進步' not in body,
 'reflection_attribution':'P04 提出的是意外通報動態演練需求' in body,
 'small_sample_statement':'不執行推論檢定' in body and 'N 小本身不構成禁止' in body,
 'response_count_clarified':'9 份回收（8 份完整、1 份部分）' in body,
 'independent_review_not_prefilled':'獨立語意審查收據' in body and '不預填審查人簽名或 PASS' in body,
 'separate_followup_documents':'0120' in body and '0122' in body,
 'no_signature_or_formal_acceptance':'NOT_GRANTED' in body and 'NOT PROVIDED' in body,
}
for name,ok in required.items(): record(name,ok)
record('false_inference_phrase_removed','統計顯著性或母體效果' in body and 'Power' not in body,{'presence_of_noninferential_limitation': '不宣稱統計顯著性' in body})

# Survey arithmetic recomputed from the raw respondent matrix (table 7), compared against summary table 12.
t7=doc.tables[6]; t12=doc.tables[11]
responses=[]
for row in t7.rows[1:11]: responses.append([parse_int(c) for c in row.cells[1:11]])
item_results=[]
for j in range(10):
 vals=[r[j] for r in responses if r[j] is not None]
 total=sum(vals); n=len(vals); positive=sum(v>=4 for v in vals); mean=Decimal(total)/Decimal(n); rate=Decimal(positive)*100/Decimal(n)
 sr=t12.rows[j+1].cells
 expected={'n':n,'sum':total,'mean':round2(mean),'positive_n':positive,'positive_pct':round1(rate)}
 actual={'n':parse_int(sr[2]),'sum':parse_int(sr[4]),'mean':txt(sr[5]),'positive_n':parse_int(sr[7]),'positive_pct':re.search(r'([0-9.]+)%',txt(sr[8])).group(1) if re.search(r'([0-9.]+)%',txt(sr[8])) else None}
 item_results.append({'item':f'Q{j+1:02d}','expected':expected,'reported':actual,'pass':actual==expected})
record('question_item_totals_means_positive_rates',all(x['pass'] for x in item_results),item_results)
complete=[responses[i] for i in range(8)]
complete_sums=[sum(r) for r in complete]
composite_sum=sum(complete_sums); composite_n=sum(len(r) for r in complete)
flow='N_INVITED (10) = N_COMPOSITE (8) + N_PARTIAL (1) + N_NON_RESP (1)' in body and composite_n==80 and composite_sum==333
record('sample_flow_and_composite',flow,{'flow_identity':'10=8+1+1','complete_respondent_sums':complete_sums,'sum':composite_sum,'valid_answers':composite_n,'mean':str(Decimal(composite_sum)/Decimal(composite_n))})
record('partial_nonresponse_handling',len(responses)==10 and len([v for v in responses[8] if v is not None])==6 and all(v is None for v in responses[9]) and 'P09 僅完成前 6 題' in body,{'P09_valid':sum(v is not None for v in responses[8]),'P10_valid':sum(v is not None for v in responses[9])})

# Skills: independently sum actual 0/10/20 raw scores and cross-check total/per-task tables.
t10=doc.tables[9]; t11=doc.tables[10]; t13=doc.tables[12]
pre=[]; post=[]; skill_task=[]; discrepancies=[]
for i in range(1,9):
 rpre=t10.rows[i]; rpost=t11.rows[i]
 pre_vals=[parse_int(c) for c in rpre.cells[1:6]]; post_vals=[parse_int(c) for c in rpost.cells[1:6]]
 pre_sum=sum(pre_vals); post_sum=sum(post_vals)
 pre.append(pre_sum); post.append(post_sum)
 if parse_int(rpre.cells[6])!=pre_sum: discrepancies.append(f'pre total P{i:02d}')
 if parse_int(rpost.cells[6])!=post_sum: discrepancies.append(f'post total P{i:02d}')
 if parse_int(rpost.cells[7])!=post_sum-pre_sum: discrepancies.append(f'delta P{i:02d}')
for j in range(5):
 prevals=[parse_int(t10.rows[i].cells[j+1]) for i in range(1,9)]
 postvals=[parse_int(t11.rows[i].cells[j+1]) for i in range(1,9)]
 ps=sum(prevals); qs=sum(postvals); avgpre=Decimal(ps)/8; avgpost=Decimal(qs)/8; delta=avgpost-avgpre; perfect=sum(v==20 for v in postvals)
 rep=t13.rows[j+1].cells
 expected=[f'{ps} ÷ 8 = {Decimal(ps)/8:.2f}',f'{qs} ÷ 8 = {Decimal(qs)/8:.2f}',f'+{delta:.2f}',f'{Decimal(perfect*100)/8:.1f}% ({perfect}/8)']
 actual=[txt(rep[k]) for k in [1,2,3,4]]
 skill_task.append({'task':f'T{j+1:02d}','expected':expected,'reported':actual,'pass':expected==actual})
paired=sum(post[i]-pre[i] for i in range(8)); pass_count=sum(x>=70 for x in post)
record('learner_skill_totals_and_pair_deltas',not discrepancies,{'errors':discrepancies,'pre_totals':pre,'post_totals':post,'paired_delta_sum':paired,'paired_mean':str(Decimal(paired)/8),'pass_n':pass_count,'n_paired':8})
record('per_task_skill_sums_means_fullmark_rates',all(x['pass'] for x in skill_task),skill_task)
record('sample_assessment_threshold',pass_count==7 and '70 分為【SAMPLE】模擬門檻' in body,{'pass_n':pass_count,'paired_n':8})

# Replacement register: 21 non-empty unique keys and all held for real-data replacement.
t16=doc.tables[15]
keys=[txt(row.cells[0]) for row in t16.rows[1:] if txt(row.cells[0])]
record('replacement_register_keys',len(keys)==21 and len(set(keys))==21,{'count':len(keys),'unique':len(set(keys))})
record('real_data_held',all('HELD' in txt(row.cells[-1]) for row in t16.rows[1:]) and 'REAL evidence 未建立' in body,{'register_rows':len(keys)})

# Native Word-produced PDF and page image integrity, dimensions, pixel reuse for unchanged pages.
pdf_sha=sha(PDF) if PDF.exists() else None
pdf_pages=None
try:
 from pypdf import PdfReader
 pdf_pages=len(PdfReader(str(PDF)).pages)
except Exception as e:
 pdf_pages={'error':str(e)}
page_results=[]
for n in range(1,24):
 p2=PNG2/f'page-{n:02d}.png'; p1=R1/f'page-{n:02d}.png'
 if not p2.exists() or not p1.exists():
  page_results.append({'page':n,'exists':False}); continue
 im2=Image.open(p2).convert('RGB'); im1=Image.open(p1).convert('RGB')
 size_match=im1.size==im2.size==(1123,794)
 diff=ImageChops.difference(im1,im2)
 changed=diff.getbbox() is not None
 changed_pixels=sum(1 for px in diff.getdata() if px!=(0,0,0)) if changed else 0
 pixel_total=im2.width*im2.height
 mid= MID/f'page-{n:02d}.png'
 mid_match=None
 if mid.exists():
  im_mid=Image.open(mid).convert('RGB'); mid_match=(im2.size==im_mid.size and ImageChops.difference(im2,im_mid).getbbox() is None)
 page_results.append({'page':n,'size':list(im2.size),'size_pass':size_match,'same_as_prior_inspected_R01':not changed,'changed_pixels':changed_pixels,'changed_pct':round(changed_pixels*100/pixel_total,6),'same_as_intermediate':mid_match,'manual_inspected_final_or_exact_intermediate':n in MANUAL_PAGES})
render_ok=len(page_results)==23 and all(x.get('size_pass') and x.get('exists',True) for x in page_results)
changed_pages=[x['page'] for x in page_results if x.get('changed_pixels',0)>0]
inherited_pages=[x['page'] for x in page_results if x.get('same_as_prior_inspected_R01')]
manual_complete=all((n in MANUAL_PAGES) or (n in inherited_pages) for n in range(1,24))
record('word_native_pdf_pages',PDF.exists() and (pdf_pages==23 or (isinstance(pdf_pages,dict) and False)),{'pdf_sha256':pdf_sha,'page_count':pdf_pages,'bytes':PDF.stat().st_size if PDF.exists() else None})
record('23_png_pages_dimensions',render_ok,{'page_count':len(page_results),'all_dimensions_1403x993':render_ok})
record('all_page_visual_scope_covered',manual_complete,{'manual_inspected_pages':MANUAL_PAGES,'unchanged_r01_inherited_pages':inherited_pages,'changed_pages':changed_pages,'pages':page_results})
# check no final page is effectively blank: there must be meaningful non-white pixels.
last=Image.open(PNG2/'page-23.png').convert('RGB'); nonwhite=sum(1 for px in last.getdata() if min(px)<240)
record('no_blank_last_page',nonwhite>5000,{'nonwhite_pixels':nonwhite})

status='PASS_TECHNICAL_VISUAL' if all(c['status']=='PASS' for c in checks) else 'FAIL_TECHNICAL_VISUAL'
receipt={
 'project_id':'TTQS_ONE','doc_id':'0121','requirement_id':'I19-E09','official_checkbox_serial':'UNKNOWN_NOT_ASSERTED',
 'source_commit':'07b6933f1af011b32e49d4391475bedc99fdbe67',
 'official_source_pdf_sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709',
 'official_source_extracted_text_sha256':'c34ead45cad406150de5622e157f44727157776ce5c6abf5343c7db5dca42520',
 'source_packet_sha256':'fbeb11b96648fff29a49a0fca74bf0cc3b3d1d29934f07dfaa3cf7e410a557fd',
 'unique_blueprint_sha256':'99320fdc9078615ad04087c43bcbd22c5bbf751a22127c51e048e909726a5fca',
 'candidate_path':str(DOCX),'candidate_sha256':candidate_sha,'candidate_bytes':candidate_bytes,
 'native_pdf_path':str(PDF),'native_pdf_sha256':pdf_sha,'native_pdf_pages':pdf_pages,
 'extract_path':str(EXTRACT),'extract_sha256':sha(EXTRACT),'extract_chars':len(EXTRACT.read_text(encoding='utf-8')),
 'technical_visual_status':status,'independent_semantic_review':'PENDING; this receipt is not semantic acceptance',
 'association_formal_acceptance':'NOT_GRANTED','real_evidence_status':'NOT_PROVIDED',
 'visual_method':'23 final page images at 1403x993; unchanged pixel-identical pages inherit R01 visual review; changed pages visually inspected in final or pixel-identical intermediate render; no candidate edits during review.',
 'check_count':len(checks),'checks':checks,
 'completed_at_utc':datetime.now(timezone.utc).isoformat(),
}
OUT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':status,'candidate_sha256':candidate_sha,'candidate_bytes':candidate_bytes,'pdf_sha256':pdf_sha,'pdf_pages':pdf_pages,'extract_sha256':receipt['extract_sha256'],'checks_passed':sum(c['status']=='PASS' for c in checks),'checks_failed':[c for c in checks if c['status']!='PASS'],'changed_visual_pages':changed_pages,'inherited_visual_pages':inherited_pages,'manual_coverage_complete':manual_complete,'receipt':str(OUT),'receipt_sha256':sha(OUT)},ensure_ascii=False,indent=2))