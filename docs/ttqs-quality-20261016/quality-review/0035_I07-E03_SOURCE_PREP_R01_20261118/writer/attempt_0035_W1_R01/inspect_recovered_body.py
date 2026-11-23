import re,hashlib,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
p=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118\writer\attempt_0035_W1_R01\recovered_payloads\WRITE_INPUT_LINE_13.md')
s=p.read_text(encoding='utf-8')
ids=re.findall(r'SYN-0035-[A-Za-z0-9-]+',s); counts=collections.Counter(ids)
print('bytes',len(p.read_bytes()),'chars',len(s),'sha256',hashlib.sha256(p.read_bytes()).hexdigest().upper())
print('headings',[x for x in s.splitlines() if re.match(r'^#{1,4} ',x)])
print('tables',sum(1 for l in s.splitlines() if l.strip().startswith('|---') or l.strip().startswith('| ---')),'rows',sum(1 for l in s.splitlines() if l.strip().startswith('|')))
print('IDs unique',len(counts),'occurrences',len(ids),'duplicates',[(k,v) for k,v in counts.items() if v>1][:20])
print('begin',repr(s[:700])); print('end',repr(s[-1200:]))
for pat in ['UNKNOWN','REAL SOURCE','SAMPLE/SYNTHETIC','finding_id','fact_id','下一次檢討','下一次檢討觸發','分子','分母','待填','待核','簽名','已實施','已驗證']:
 print(pat, s.count(pat))
