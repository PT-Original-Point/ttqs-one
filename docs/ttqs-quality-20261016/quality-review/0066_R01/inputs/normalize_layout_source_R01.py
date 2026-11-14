from pathlib import Path
import re,hashlib,json
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01')
p=root/'inputs'/'0066_BODY_R01_HUMAN_READY.md'
s=p.read_text(encoding='utf-8')
repls={
'- **閱讀路徑**：第 1 頁導讀 → 第 2 頁官方要求追溯與文件辨析 → 第 3 頁結案形成程序 → 第 4 頁來源清冊與班級資料卡 → 第 5 頁證據鏈與課表 → 第 6 頁分母橋接 → 第 7 頁評量與問卷 → 第 8 頁資源與財務 → 第 9 頁改善閉環 → 第 10 頁一致性、連結、HOLD 與附件 → 第 11 頁空白採集表。':'- **閱讀路徑**：導讀 → 官方要求追溯與文件辨析 → 結案程序與來源 → 需求、課表及成果計算 → 資源、財務及改善閉環 → 一致性、HOLD 與附件 → 空白採集表。',
'| 資源的運用 | 第 8 頁 資源計畫／使用差異 | 資源表 | SAMPLE |':'| 資源的運用 | 資源計畫／使用差異 | 資源表 | SAMPLE |',
'| 財務的支配 | 第 8 頁 財務核算 | 財務表 | SAMPLE（無真憑證） |':'| 財務的支配 | 財務核算 | 財務表 | SAMPLE（無真憑證） |',
'| 訓練成果的展現 | 第 6、7 頁 | 分母橋接表、評量量規、問卷逐題分布、追蹤表 | SAMPLE |':'| 訓練成果的展現 | 分母橋接與成果評量 | 分母橋接表、評量量規、問卷逐題分布、追蹤表 | SAMPLE |',
'| 檢討及改進的方法 | 第 9 頁 | 改善閉環表 | SAMPLE 建議、未核定 |':'| 檢討及改進的方法 | 改善閉環 | 改善閉環表 | SAMPLE 建議、未核定 |',
'| 課後檢討、學員建議／回饋、需求、目標及方法 | 第 5、7、9 頁 | 需求至評量鏈、問卷分布、改善閉環 | SAMPLE |':'| 課後檢討、學員建議／回饋、需求、目標及方法 | 需求至評量及改善 | 需求至評量鏈、問卷分布、改善閉環 | SAMPLE |',
'| 6. HOLD／退件 | 依缺證條件判定暫緩或退件 | 班務功能 | 見第 10 頁 |':'| 6. HOLD／退件 | 依缺證條件判定暫緩或退件 | 班務功能 | 見「缺證／HOLD／退件條件」章 |',
'| A-11 | 空白採集表 | 空白工作表 | 見第 11 頁 |':'| A-11 | 空白採集表 | 空白工作表 | 見附錄 |'
}
for old,new in repls.items():
    if old not in s: raise SystemExit('missing exact source string: '+old[:100])
    s=s.replace(old,new,1)
lines=[]
for line in s.splitlines():
    if re.match(r'^〔第\s*\d+\s*頁〕',line.strip()): continue
    if line.strip().startswith('（全頁提醒：'): continue
    lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
manifestp=root/'evidence'/'source_manifest_R01.json'
m=json.loads(manifestp.read_text(encoding='utf-8'))
m['body_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
m['body_layout_source_sha256']=m['body_sha256']
m['pagination_policy']='Natural page flow; former page-number cross-references replaced with section titles; sample/synthetic status appears in every page footer.'
manifestp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'body_sha256':m['body_sha256'],'remaining_page_refs':len(re.findall(r'第\s*\d+\s*頁',p.read_text(encoding='utf-8'))),'remaining_page_markers':len(re.findall(r'^〔第',p.read_text(encoding='utf-8'),re.M))},ensure_ascii=False))
