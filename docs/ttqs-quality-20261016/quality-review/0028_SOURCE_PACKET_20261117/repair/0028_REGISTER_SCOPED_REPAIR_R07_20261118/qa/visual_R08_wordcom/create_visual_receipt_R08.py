from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
qa=base/'qa'/'visual_R08_wordcom'; pages=sorted((qa/'pages').glob('page-*.png'))
if len(pages)!=21: raise SystemExit('PAGE_COUNT_NOT_21')
metrics=[]
for i,p in enumerate(pages,1):
    im=Image.open(p).convert('L'); hist=im.histogram(); nonwhite=sum(hist[:250])
    metrics.append({'page':i,'image_sha256':sha256(p.read_bytes()).hexdigest().upper(),'dimensions_px':list(im.size),'nonwhite_pixels_lt250':nonwhite,'nonwhite_ratio':round(nonwhite/(im.width*im.height),6)})
if any(x['nonwhite_ratio']<0.0001 for x in metrics): raise SystemExit('BLANK_PAGE_DETECTED')
sheets=['CONTACT_SHEET_R08_01_06.png','CONTACT_SHEET_R08_07_12.png','CONTACT_SHEET_R08_13_18.png','CONTACT_SHEET_R08_19_21.png']
sheet_data=[]
for name in sheets:
    f=qa/name
    if not f.exists(): raise SystemExit('CONTACT_SHEET_MISSING_'+name)
    sheet_data.append({'file':name,'sha256':sha256(f.read_bytes()).hexdigest().upper()})
receipt={
 'schema':'TTQS_ONE_0028_FULL_PAGE_VISUAL_QA_R08',
 'work_id':'TTQS_ONE_0028_I05-E02_FULL_PAGE_VISUAL_QA_R08_20261118',
 'candidate_docx_sha256':'1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70',
 'source_candidate_sha256':'06BE5AD01D3B96EC1CA98D9787EF37161C17B39AAFF2CFD943A3FB2C5BB2EEEA',
 'pdf_sha256':'3EC2455B1F0C5A8357987D6200F19DE1793D64AA913792AEF18CB204D9E53CB5',
 'page_count':21,
 'renderer':'Microsoft Word COM PDF; rasterized by Poppler pdftoppm at 110 dpi',
 'visual_inspection_scope':'All 21 complete page images reviewed in four contact sheets; final page additionally inspected at full resolution.',
 'checks':{'all_pages_rendered':True,'blank_pages':[],'page_content_clipped':False,'overlapping_text_or_tables':False,'table_borders_and_row_continuations_visible':True,'candidate_sha_exact':True,'same_sha_as_render_receipt':True},
 'observed_layout':'Dense but legible 9.5 pt minimum tables; no blank pages; section and table continuations are intact; final evidence-index/replacement workflow is complete on page 21.',
 'contact_sheets':sheet_data,
 'page_image_metrics':metrics,
 'pixel_identity_with_R07_not_used':'R08 was freshly inspected; R07 pixel hash comparison was false and is not used as inherited PASS.',
 'reviewer':'Codex visual inspection',
 'result':'PASS_FULL_PAGE_VISUAL_R08',
 'formal_acceptance':'NOT_CLAIMED'
}
out=qa/'FULL_PAGE_VISUAL_QA_R08.json'
if out.exists(): raise SystemExit('VISUAL_REVIEW_RECEIPT_EXISTS')
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'result':receipt['result'],'pages':len(metrics),'blank_pages':[],'candidate_sha':receipt['candidate_docx_sha256'],'receipt':str(out)},ensure_ascii=False))

