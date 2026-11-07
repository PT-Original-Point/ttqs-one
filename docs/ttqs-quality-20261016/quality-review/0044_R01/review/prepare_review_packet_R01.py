from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
packet_name = sys.argv[1] if len(sys.argv) > 1 else "packet_R01"
if not re.fullmatch(r"packet_R01(?:_retry[0-9]+)?", packet_name):
    raise SystemExit("Packet directory name must be packet_R01 or packet_R01_retryN")
PACKET = ROOT / "review" / packet_name
SOURCE_FILES = [
    "candidate/0044_R01.docx",
    "inputs/official_checklist_full_source.pdf",
    "inputs/official_source_page_03.png",
    "inputs/official_sequence_045.md",
    "inputs/BLUEPRINT_0044_AND_NEIGHBORS.jsonl",
    "inputs/crosswalk_I09-E04.csv",
    "inputs/association_context_provenance.md",
    "inputs/historical_candidate_disposition.md",
    "inputs/SOURCE_MAP.md",
    "inputs/candidate_body_text_R01.txt",
    "evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv",
    "technical_integrity_R01.json",
    "evidence/visual_layout_receipt_R01_FINAL.json",
    *[f"evidence/render_final_0044_R01_final/page-{n}.png" for n in range(1, 9)],
    "evidence/render_final_0044_R01_final/0044_R01_Word.pdf",
]
EXPECTED_DOCX = "76bde5df4209abc6f102a15a02c5e51a5816ef3df309aaed0a0ab44ea9075644"
PROMPT = f"""你是與 DOCX Builder 獨立的語意及視覺審查者。只讀封存封包，不修改任何檔案；不得以 Builder 自報 PASS、標題、技術收據或摘要取代自己的檢查。

審查身分：TTQS ONE／DOCX 0044／I09-E04／官方清單方框流水號 045。三種編號不可混用。官方要求：「所有的討論、 會議或E-mail均留有完整紀錄並經簽核後存檔。」只判定本候選範例文件是否成熟、正確、可供使用；REAL 協會紀錄、有效簽核、授權、正式歸檔與 Human 接受均未證實，不得升格或暗示已發生。

候選 DOCX SHA-256 必須逐位元組確認為：{EXPECTED_DOCX}

先讀官方清單 PDF 第3頁與該頁影像、DOCX 0044 唯一 Blueprint 和 0043/0045 鄰項、交叉索引、完整正文、156列 SAMPLE 替換清冊、候選 DOCX、Word PDF 與8張逐頁 PNG。檢查全部頁面。獨立重算記錄筆數、欄位、3/4比例及事實列關係；確認合成值、角色、日期、訊息、附件版次、簽核狀態和保存定位一致，UNKNOWN/HOLD 不得猜填。資料不足應列 PARTIAL/UNKNOWN。

必須回答：
1. 是否精確涵蓋 I09-E04 的討論、會議、完整電子郵件往返、完整紀錄、有效簽核後存檔；是否清楚承認目前沒有本會 REAL 證據。
2. 文類是否為可操作的證據紀錄及行政表單，而非政策說明或空白模板；是否有已填的 SAMPLE 會議、當面討論、四封連續郵件及缺件 HOLD；小型協會行政人員能否直接使用。
3. 12個可複用欄位是否分別出現在會議和當面討論示範，且各有完整性判讀；覆核、簽核、保存是否正確區分；檢核是否被誤寫成核准。
4. 3/4=75% 是否只代表頁內四筆 SAMPLE 的紀錄欄位模型完整比例，非協會實績/法遵率；X01 的9/12與3個HOLD是否一致。
5. 156列清冊是否唯一、可定位正文、逐筆列出 REAL 替代來源和查證方法，覆蓋重要合成事實；不可有未註冊的重要合成主張。
6. 遮蔽標題後能否辨認用途；比較負鄰項 0043/I09-E03（需求訪談分析）與0045/I10-E01（採購遴選），確認沒有錯件或錯用官方流水號。
7. 獨立目視第1–8頁：可讀性、表格分頁/重複表頭、截字、重疊、過密、孤立內容、空白頁、樣式品質；逐頁回報。
8. 列出 material findings，附頁碼、章節/表列/短定位、影響及最小修法；若無則明確寫0。

以 JSON 回覆且附足夠證據：{{"reviewer_verdict":"PASS|PARTIAL|FAIL","candidate_sha256_read":"...","identity":{{"doc_id":"0044","requirement_id":"I09-E04","official_checkbox_sequence":"045"}},"criteria":[{{"criterion":"...","status":"PASS|PARTIAL|FAIL|UNKNOWN","locator":"...","evidence":"..."}}],"arithmetic_recheck":{{"records":4,"complete_model_records":3,"held_records":1,"record_level_rate":"3/4=75%","result":"..."}},"register_check":{{"rows":156,"unique_fact_ids":156,"body_locator_and_replacement_check":"...","result":"..."}},"page_visual_checks":[{{"page":1,"status":"PASS|PARTIAL|FAIL","finding":"..."}}],"title_blind_use":"...","negative_neighbor_check":"...","sample_real_boundary":"...","findings":[{{"severity":"P1|P2|P3","locator":"...","evidence":"...","impact":"...","minimum_repair":"..."}}],"findings_count":0,"formal_acceptance":"NOT_GRANTED"}}

實質缺陷請判 PARTIAL/FAIL 並精確定位。不要要求重建無缺陷文件。"""

if packet_name != "packet_R01":
    PROMPT = PROMPT.replace(
        "先讀官方清單 PDF 第3頁與該頁影像、DOCX 0044 唯一 Blueprint 和 0043/0045 鄰項、交叉索引、完整正文、156列 SAMPLE 替換清冊、候選 DOCX、Word PDF 與8張逐頁 PNG。檢查全部頁面。",
        "只使用 Antigravity 平台提供的原生檔案讀取/影像檢視能力讀取封包；嚴禁呼叫 RunCommand、shell、PowerShell、cmd 或任何 command 工具。檔案均在此工作目錄內，路徑相對於封包根目錄。先讀官方清單 PDF 第3頁與該頁影像、DOCX 0044 唯一 Blueprint 和 0043/0045 鄰項、交叉索引、完整正文、156列 SAMPLE 替換清冊、候選 DOCX、Word PDF 與8張逐頁 PNG。檢查全部頁面；若平台沒有原生能力讀取任一必要項，請如實回報 PARTIAL/UNKNOWN，不要用 shell 補救。"
    )


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


manifest_path = PACKET / "review_packet_manifest_R01.json"
if manifest_path.exists():
    raise SystemExit(f"Immutable review packet already exists: {PACKET}")
PACKET.mkdir(parents=True, exist_ok=True)
for rel in SOURCE_FILES:
    src = ROOT / rel
    if not src.is_file():
        raise SystemExit(f"Missing review source: {src}")
    dst = PACKET / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and sha(dst) != sha(src):
        raise SystemExit(f"Frozen packet conflict at {dst}; refusing to overwrite")
    if not dst.exists():
        shutil.copy2(src, dst)
candidate = PACKET / "candidate/0044_R01.docx"
candidate_sha = sha(candidate)
if candidate_sha != EXPECTED_DOCX:
    raise SystemExit(f"Exact candidate SHA mismatch: {candidate_sha}")
prompt_path = PACKET / "review_prompt_R01.txt"
prompt_path.write_text(PROMPT, encoding="utf-8")
files = []
for path in sorted(p for p in PACKET.rglob("*") if p.is_file() and p != manifest_path):
    files.append({"path": str(path.relative_to(PACKET)).replace("\\", "/"), "bytes": path.stat().st_size, "sha256": sha(path)})
manifest = {
    "project_id": "TTQS_ONE",
    "doc_id": "0044",
    "requirement_id": "I09-E04",
    "official_checkbox_sequence": "045",
    "candidate_sha256": candidate_sha,
    "candidate_status": "CANDIDATE_NOT_PROMOTED",
    "blueprint_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
    "official_source_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
    "rendered_page_count": 8,
    "prompt_path": "review_prompt_R01.txt",
    "prompt_sha256": sha(prompt_path),
    "file_count": len(files),
    "files": files,
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"packet": str(PACKET), "candidate_sha256": candidate_sha, "file_count": len(files), "manifest_sha256": sha(manifest_path), "prompt_sha256": sha(prompt_path)}, ensure_ascii=False))
