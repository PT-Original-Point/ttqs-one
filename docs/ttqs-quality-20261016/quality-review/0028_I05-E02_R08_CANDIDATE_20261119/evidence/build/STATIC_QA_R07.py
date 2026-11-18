import hashlib,json,re,datetime
from pathlib import Path
from html.parser import HTMLParser

root=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117')
candidate=root/'repair'/'0028_REGISTER_SCOPED_REPAIR_R07_20261118'/'candidate_0028_R07_20261118.html'
source=root/'source'/'SOURCE_PACKET_0028_I05-E02_R01.md'
blueprint=root/'blueprint'/'UNIQUE_BLUEPRINT_0028_I05-E02_R01.md'
out=candidate.parent/'STATIC_QA_R07.json'
raw=candidate.read_bytes()
html=raw.decode('utf-8')
sha=lambda b:hashlib.sha256(b).hexdigest().upper()

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title=[]; self.in_title=False; self.text=[]; self.styles=[]; self.in_style=False
        self.tables=[]; self.table=None; self.row=None; self.cell=None; self.scripts=0; self.forms=0; self.assets=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='title': self.in_title=True
        if tag=='style': self.in_style=True; self.styles.append('')
        if tag=='table': self.table=[]; self.tables.append(self.table)
        elif tag=='tr' and self.table is not None: self.row=[]; self.table.append(self.row)
        elif tag in ('td','th') and self.row is not None: self.cell=[]
        if tag=='script': self.scripts+=1
        if tag=='form': self.forms+=1
        if tag in ('img','script','iframe','link'):
            for k,v in attrs.items():
                if k in ('src','href') and re.match(r'(?i)^https?://',v or ''): self.assets.append([tag,k,v])
    def handle_endtag(self,tag):
        if tag=='title': self.in_title=False
        if tag=='style': self.in_style=False
        if tag in ('td','th') and self.row is not None:
            self.row.append(' '.join(''.join(self.cell or []).split())); self.cell=None
        if tag=='table': self.table=None
    def handle_data(self,data):
        self.text.append(data)
        if self.in_title: self.title.append(data)
        if self.in_style and self.styles: self.styles[-1]+=data
        if self.cell is not None: self.cell.append(data)

p=Parser(); p.feed(html); p.close()
visible=' '.join(' '.join(p.text).split())
css='\n'.join(p.styles)
ids=sorted(set(re.findall(r'SYN-0028-[A-Za-z0-9_-]+',visible)))
id_counts={x:len(re.findall(re.escape(x),visible)) for x in ids}
id_per_table=[]
for table in p.tables:
    content=' '.join(' '.join(row) for row in table)
    id_per_table.append(sorted(set(re.findall(r'SYN-0028-[A-Za-z0-9_-]+',content))))
reg_index=max(range(len(id_per_table)),key=lambda i:len(id_per_table[i])) if id_per_table else -1
registered=set(id_per_table[reg_index]) if reg_index>=0 else set()
reg_row_counts={x:sum(1 for row in p.tables[reg_index] if x in ' '.join(row)) for x in registered} if reg_index>=0 else {}
body=re.search(r'(?is)body[^{}]*\{[^}]*font-size\s*:\s*([0-9.]+)pt',css)
table=re.search(r'(?is)table[^{}]*\{[^}]*font-size\s*:\s*([0-9.]+)pt',css)
minw=re.search(r'(?is)table[^{}]*\{[^}]*min-width\s*:\s*([0-9.]+)px',css)
bodypt=float(body.group(1)) if body else None
tablept=float(table.group(1)) if table else None
minwidth=float(minw.group(1)) if minw else 0
celltexts=[c for t in p.tables for row in t for c in row]
placeholder=[c for c in celltexts if re.search(r'^(?:待填|待核|TBD|TODO|PLACEHOLDER|XXX)$',c,re.I)]
checks={
 'complete_html':html.lstrip().lower().startswith('<!doctype html>') and html.rstrip().lower().endswith('</html>'),
 'exact_title':''.join(p.title).strip()=='訓練課程體系及訓練機構業務策略方向的相關資料_完整工作稿',
 'official_locator':'I05-E02' in visible and 'OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf' in visible,
 'body_font_at_least_11pt':bodypt is not None and bodypt>=11,
 'table_font_at_least_9_5pt':tablept is not None and tablept>=9.5,
 'A4_table_width_not_overflow':minwidth<=718,
 'no_scripts_forms_or_external_assets':p.scripts==0 and p.forms==0 and not p.assets,
 'no_empty_table_cells':all(c for c in celltexts),
 'no_placeholder_data_cells':not placeholder,
 'sample_unknown_boundaries':all(x in visible.upper() for x in ('SAMPLE','SYNTHETIC','UNKNOWN')),
 'negative_neighbors_named':'0027' in visible and '0029' in visible,
 'replacement_register_present':len(registered)==91 and all(reg_row_counts[x]==1 for x in registered),
 'expected_91_atomic_ids':len(ids)==91,
 'every_id_listed_in_max_id_table':len(ids)>0 and registered==set(ids),
 'each_id_has_register_and_use':bool(ids) and all(id_counts[x]>=2 for x in ids),
 'one_register_row_per_id':bool(registered) and all(reg_row_counts[x]==1 for x in registered),
}
result='PASS_STATIC_HTML_ONLY' if all(checks.values()) else 'FAIL_SCOPED_REPAIR_REQUIRED'
report={'schema':'TTQS_ONE_0028_STATIC_HTML_QA_R07','work_id':'TTQS_ONE_0028_I05-E02_STATIC_QA_R07_20261118','candidate_kind':'HTML candidate only; DOCX/visual/semantic acceptance pending','source_sha256':sha(source.read_bytes()),'blueprint_sha256':sha(blueprint.read_bytes()),'candidate_html_sha256':sha(raw),'candidate_html_bytes':len(raw),'table_count':len(p.tables),'table_row_counts':[len(t) for t in p.tables],'synthetic_id_count':len(ids),'register_table_index':reg_index,'register_id_count':len(registered),'body_font_pt':bodypt,'table_font_pt':tablept,'table_min_width_px':minwidth,'empty_or_placeholder_cells':placeholder,'checks':checks,'result':result,'measured_at_tpe':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))


