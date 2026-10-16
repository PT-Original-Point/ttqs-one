from pathlib import Path
import csv, hashlib

ROOT=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review')
P=ROOT/'0040_R06'; doc=P/'candidate/0040_R06.docx'
register=P/'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R06.csv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED='115caf94165263040b27dbea5a2c83e02f94253d361e16784da398cefd3562d7'
if sha(doc)!=EXPECTED: raise SystemExit('R06 DOCX bytes changed; refusing locator rebinding')
with register.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
locators={
 '0040-SYN-004':'列印第3頁矩陣表「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」；K1-K4四列均在本頁，定位於各列的基線平均、目標與缺口欄。',
 '0040-SYN-005':'第3頁評分表K1-K2列；第4頁重複表頭下K3-K4列及「計分」段。',
 '0040-SYN-006':'第4頁「計分」段（四項完整、總分至少6/8、K3至少1分）；第5頁「五筆示範資料」表，完整前後測表頭與D01-D05判定欄。',
 '0040-SYN-010':'第3–4頁評量矩陣責任欄；第6頁D04示例表「後續行動（示範待辦）」列／完整合成填寫示例欄。',
 '0040-SYN-BL-K3':'列印第3頁評量矩陣表「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」；K3「同意與隱私界線」列／第1欄基線平均、目標與缺口。',
 '0040-SYN-BL-K4':'列印第3頁評量矩陣表「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」；K4「收尾與交接」列／第1欄基線平均、目標與缺口。',
 '0040-SYN-CALC-002':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；平均前測列／代入合成資料及結果欄。',
 '0040-SYN-CALC-003':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；平均後測列／代入合成資料及結果欄。',
 '0040-SYN-CALC-004':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；配對平均變化列／代入合成資料及結果欄。',
 '0040-SYN-CALC-005':'第5頁「五筆示範資料」表，完整五欄表頭及D01、D02、D03、D05判定列；同頁後測達標率列。',
 '0040-SYN-CALC-006':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；後測達標率列／代入合成資料及結果欄。',
 '0040-SYN-CALC-007':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；構面平均列／代入合成資料之前測K1-K4數列。',
 '0040-SYN-CALC-008':'第5頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；構面平均列／結果及解讀限制欄之後測K1-K4平均數列。',
 '0040-SYN-CALC-009':'第6頁表頭「欄位｜完整合成填寫示例｜實際使用時檢查」；後續行動列。另見第7頁改善追蹤表D04列。',
 '0040-SYN-034':'第7頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／差距欄。',
 '0040-SYN-035':'第7頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／示範風險欄。',
 '0040-SYN-036':'第7頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／責任角色欄。',
 '0040-SYN-037':'第7頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／示範期限及未執行狀態欄。',
 '0040-SYN-038':'第7頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／交接資料與結案規則欄。',
 '0040-SYN-039':'列印第3頁 K1-K4矩陣末欄各列；列印第6頁 D04示例表「原始評量證據定位」列。'
}
for kind, label in [('PRE','前測'),('POST','後測')]:
    for code in ('D01','D02','D03','D04','D05'):
        field='前測 K1/K2/K3/K4；總分' if kind=='PRE' else '後測 K1/K2/K3/K4；總分'
        locators[f'0040-SYN-{kind}-{code}']=f'第5頁「五筆示範資料」表之{label}欄；{code}列／「{field}」欄。'
seen=set()
for row in rows:
    fid=row['fact_id']
    if fid in locators:
        row['body_locator']=locators[fid]; seen.add(fid)
    row['bound_candidate_sha256']=EXPECTED
if seen!=set(locators): raise SystemExit(f'Locator rows missing: {sorted(set(locators)-seen)}')
if len(rows)!=40 or len({r['fact_id'] for r in rows})!=40: raise SystemExit('Unexpected R06 register structure')
with register.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'candidate_sha256={EXPECTED}\nregister_rows={len(rows)}\nregister_sha256={sha(register)}\nupdated_locators={len(locators)}')
