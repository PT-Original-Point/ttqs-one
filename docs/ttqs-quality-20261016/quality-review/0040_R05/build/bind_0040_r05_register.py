from pathlib import Path
import csv,hashlib
from docx import Document
ROOT=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review')
P=ROOT/'0040_R05'
doc=P/'candidate/0040_R05.docx'
register=P/'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R05.csv'
sha=hashlib.sha256(doc.read_bytes()).hexdigest()
with register.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
locators={
 '0040-REF-001':'第1頁「官方要求（逐字引用）」及「來源」段；來源為勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》PDF 第3頁。',
 '0040-SYN-006':'第3頁「計分」段（四項完整、總分至少6/8、K3至少1分）；第4頁「五筆示範資料」表，表頭「前測 K1/K2/K3/K4；總分」及「後測 K1/K2/K3/K4；總分」，D01–D05列／「依門檻判定」欄。',
 '0040-SYN-009':'第1頁步驟表「4 定時點」列／操作欄（30日追蹤另行核准）；第6頁D04追蹤列「本例尚未執行，沒有重評結果」；前者是另行授權規則，後者是本合成示範未執行界線。',
 '0040-SYN-CALC-005':'第4頁「五筆示範資料」表，完整表頭「合成代碼」「前測 K1/K2/K3/K4；總分」「後測 K1/K2/K3/K4；總分」「總分變化」「依門檻判定」；D01、D02、D03、D05列／判定欄；另見同頁「後測達標率」列。'
}
ids=set()
for row in rows:
    if row['fact_id'] in ids: raise ValueError('Duplicate fact id '+row['fact_id'])
    ids.add(row['fact_id'])
    row['bound_candidate_sha256']=sha
    if row['fact_id'] in locators: row['body_locator']=locators[row['fact_id']]
if len(rows)!=39: raise ValueError(f'Expected 39 register facts, got {len(rows)}')
with register.open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(f'bound_rows={len(rows)} candidate_sha256={sha} register={register}')
