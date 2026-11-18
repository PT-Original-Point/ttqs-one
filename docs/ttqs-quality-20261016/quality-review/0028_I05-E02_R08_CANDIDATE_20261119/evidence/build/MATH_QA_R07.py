from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
import datetime, json
from lxml import html
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117')
folder=base/'repair'/'0028_REGISTER_SCOPED_REPAIR_R07_20261118'
candidate=folder/'candidate_0028_R07_20261118.html'
static_path=folder/'STATIC_QA_R07.json'
source=base/'source'/'SOURCE_PACKET_0028_I05-E02_R01.md'
blueprint=base/'blueprint'/'UNIQUE_BLUEPRINT_0028_I05-E02_R01.md'
out=folder/'MATH_QA_R07.json'
digest=lambda b:sha256(b).hexdigest().upper()
raw=candidate.read_bytes()
candidate_sha=digest(raw)
tree=html.fromstring(raw)
text=' '.join(tree.text_content().split())
static=json.loads(static_path.read_text(encoding='utf-8'))
table_index=static['register_table_index']
tables=tree.xpath('//table')
register_table=tables[table_index]
register={}
for row in register_table.xpath('.//tr'):
    cells=row.xpath('./td|./th')
    if len(cells)>=1:
        key=' '.join(cells[0].itertext()).strip()
        register[key]=' '.join(' '.join(c.itertext()) for c in cells)
kpi2=Fraction(2,3); kpi2_target=Fraction(2,3)
kpi3=Fraction(5,6); kpi3_target=Fraction(833,1000)
def display(v):
    return str((Decimal(v.numerator)*Decimal(100)/Decimal(v.denominator)).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
checks={
 'candidate_sha_matches_static':static.get('candidate_html_sha256')==candidate_sha,
 'static_qa_pass':static.get('result')=='PASS_STATIC_HTML_ONLY',
 'kpi2_register_denominator_3':'分母 3 個' in register.get('SYN-0028-NUM-003',''),
 'kpi2_register_numerator_2':'分子 2 個' in register.get('SYN-0028-NUM-004',''),
 'kpi2_exact_ratio_meets_2_3':kpi2>=kpi2_target,
 'kpi2_half_up_display_66_7':display(kpi2)=='66.7' and '66.7%' in text,
 'kpi3_register_denominator_6':'分母 6 個' in register.get('SYN-0028-NUM-005',''),
 'kpi3_register_numerator_5':'分子 5 個' in register.get('SYN-0028-NUM-006',''),
 'kpi3_exact_ratio_exceeds_833_1000':kpi3>kpi3_target,
 'kpi3_half_up_display_83_3':display(kpi3)=='83.3' and '83.3%' in text,
 'kpi3_exact_threshold_registered':'833/1000' in register.get('SYN-0028-PCT-006',''),
 'kpi3_monthly_cadence_registered':'SYN-0028-CADENCE-001' in text,
 'date002_registered_once':sum(1 for key in register if key=='SYN-0028-DATE-002')==1,
 'date006_duplicate_absent':'SYN-0028-DATE-006' not in text,
 'source_packet_and_blueprint_bindings_present':source.is_file() and blueprint.is_file(),
}
result='PASS_DETERMINISTIC_MATH_AND_FACT_REGISTER_R07' if all(checks.values()) else 'FAIL_DETERMINISTIC_MATH_OR_FACT_REGISTER_R07'
report={
 'schema':'TTQS_ONE_0028_MATH_QA_R07','work_id':'TTQS_ONE_0028_I05-E02_MATH_QA_R07_20261118',
 'doc_id':'0028','requirement_id':'I05-E02',
 'candidate_html_sha256':candidate_sha,'candidate_html_bytes':len(raw),
 'static_qa_sha256':digest(static_path.read_bytes()),
 'source_packet_sha256':digest(source.read_bytes()),'blueprint_sha256':digest(blueprint.read_bytes()),
 'calculations':{
  'kpi2':{'numerator':2,'denominator':3,'exact':'2/3','exact_target':'2/3','display_percent_1dp':display(kpi2),'decision':'PASS_SAMPLE_ONLY'},
  'kpi3':{'numerator':5,'denominator':6,'exact':'5/6','exact_target':'833/1000','actual_exceeds_target':kpi3>kpi3_target,'display_percent_1dp':display(kpi3)},
  'rounding':'ROUND_HALF_UP, 1 decimal place'},
 'date_id_reconciliation':{'retained':'SYN-0028-DATE-002','removed':'SYN-0028-DATE-006','reason':'same 2027-03-31 milestone and decision completion date'},
 'checks':checks,'result':result,
 'candidate_status':'CANDIDATE; SAMPLE/SYNTHETIC; visual and independent semantic review pending; formal acceptance not claimed',
 'measured_at_tpe':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
if result!='PASS_DETERMINISTIC_MATH_AND_FACT_REGISTER_R07':
    raise SystemExit(2)