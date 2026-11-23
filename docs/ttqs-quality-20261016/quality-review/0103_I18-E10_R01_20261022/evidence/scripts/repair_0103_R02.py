from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'writer'/'opencode_writer_manuscript_0103_R01.md'
OUT=ROOT/'writer'/'opencode_writer_manuscript_0103_R02.md'
DELTA=ROOT/'evidence'/'semantic_repair_delta_0103_R02.json'
BASE_DOCX=ROOT/'candidate'/'0103__I18-E10__感謝函取得與真偽查核工作紀錄_R01.docx'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
text=SRC.read_text(encoding='utf-8-sig')
changes=[]
def replace_once(old,new,finding):
    global text
    count=text.count(old)
    if count != 1: raise SystemExit(f'{finding}: expected exactly one source occurrence; found {count}')
    text=text.replace(old,new,1)
    changes.append({'finding':finding,'old':old,'new':new,'occurrences':count})
replace_once('使用第4.0節狀態碼','依「共用狀態碼」表選擇狀態','cross-reference to visible status heading')
replace_once('| 狀態 | `NOT_RECEIVED` | `NOT_SENT` | `NOT_APPLICABLE` |','| 狀態 | `NOT_RECEIVED` | `REQUEST_DRAFT_ONLY（未寄出）` | `NOT_APPLICABLE` |','use defined primary state for unsent request')
replace_once('- `VERIFIED_REAL` 必須附上 D01～D14 的必要證據；不能只寫「看起來是真的」。','- `VERIFIED_REAL` 必須具備 D01～D14 的必要證據，並確認 D15 無重大未解矛盾；若 D15 有未解矛盾，維持 `HOLD`。','state D15 conflict gate alongside D01-D14')
replace_once('| `VERIFIED_REAL` | 來源、權限／範圍、完整性、內容四類查核均有證據 | D01～D14 必要項均有支持 | 不得寫成評分、獎項或正式接受 | 可進入人類覆核，但仍非驗收 |','| `VERIFIED_REAL` | 來源、權限／範圍、完整性、內容四類查核均有證據 | D01～D14 必要項均有支持；D15 無重大未解矛盾 | 不得寫成評分、獎項或正式接受 | 可進入人類覆核，但仍非驗收 |','align VERIFIED_REAL status table with D15 gate')
replace_once('未確認前不 contact、不轉傳、不公開','未確認前不聯絡、不轉傳、不公開','replace mixed-language operational instruction')
replace_once('都要記入 Form 4.7。','都要記入「存取、更正與保存位置紀錄」表。','replace locator with visible record title')
row_old='| S-07 | 案例一／Form A | 關係 | `SAMPLE-REL-01` | 真實學員／客戶關係證明 | 承辦 | 關係可查 | SAMPLE_ONLY |'
row_new='| S-07 | 案例一／Form A | 關係 | `SAMPLE-REL-01` | 真實學員／客戶關係證明 | 承辦 | 關係可查且與課程一致 | SAMPLE_ONLY |'
replace_once(row_old,row_new,'merge the stronger S-07 replacement condition into its first row')
count=text.count(row_new)
if count != 2: raise SystemExit(f'duplicate S-07: expected two rows after merge; found {count}')
first=text.find(row_new); second=text.find(row_new,first+len(row_new)); end=second+len(row_new)
if text[end:end+2]=='\r\n': end+=2
elif text[end:end+1]=='\n': end+=1
text=text[:second]+text[end:]
changes.append({'finding':'remove duplicate S-07 continuation row','old':row_new,'new':'','occurrences_removed':1})
OUT.write_text(text,encoding='utf-8',newline='\n')
record={'doc_id':'0103','requirement_id':'I18-E10','unique_blueprint_item':111,'revision':'R02','status':'CANDIDATE_ONLY','base_docx_sha256':sha(BASE_DOCX),'base_manuscript_sha256':sha(SRC),'repair_script_sha256':sha(Path(__file__)),'repaired_manuscript_sha256':sha(OUT),'scope':'Bounded semantic repairs from independent R01 review; no third-party REAL evidence or approval added.','changes':changes}
DELTA.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'base_docx_sha256':record['base_docx_sha256'],'base_manuscript_sha256':record['base_manuscript_sha256'],'repair_script_sha256':record['repair_script_sha256'],'repaired_manuscript_sha256':record['repaired_manuscript_sha256'],'delta_sha256':sha(DELTA),'changes':len(changes)},ensure_ascii=False))
