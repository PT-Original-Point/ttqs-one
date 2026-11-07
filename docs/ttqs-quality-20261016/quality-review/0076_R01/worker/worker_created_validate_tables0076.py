import csv, re
root=r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01"
body=root+r"\candidate\0076_R01_body.md"
lines=open(body,encoding='utf-8').read().split("\n")
# table consistency
blocks=[]; cur=[]
for ln in lines:
    if ln.strip().startswith("|"):
        cur.append(ln)
    else:
        if cur: blocks.append(cur); cur=[]
if cur: blocks.append(cur)
print("table blocks:",len(blocks))
badblocks=0
for bi,b in enumerate(blocks):
    counts={ln.count("|") for ln in b}
    if len(counts)!=1:
        badblocks+=1
        print("INCONSISTENT block",bi,"counts",counts)
        for ln in b: print("   ",ln[:100])
print("inconsistent blocks:",badblocks)

# response fidelity
data=list(csv.DictReader(open(root+r"\inputs\SYNTHETIC_ASSESSMENT_DATA_0076_R01.csv",encoding='utf-8-sig')))
def cells(ln): return [c.strip() for c in ln.strip().strip("|").split("|")]
miss=0
for r in data:
    code=r["learner_code"]
    exp1=[r["Q%02d_response"%i] for i in range(1,11)]
    exp2=[r["Q%02d_response"%i] for i in range(11,21)]
    found1=found2=False
    for ln in lines:
        c=cells(ln)
        if len(c)==11 and c[0]==code and c[1:11]==exp1: found1=True
        if len(c)==13 and c[0]==code and c[1:11]==exp2 and c[11]==r["correct_items"] and c[12]==r["posttest_total_from_0074_synthetic"]: found2=True
    if not found1: print("MISS table1",code); miss+=1
    if not found2: print("MISS table2",code); miss+=1
print("response fidelity misses:",miss)
print("bytes body",__import__('os').path.getsize(body))
