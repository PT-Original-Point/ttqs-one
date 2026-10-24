from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


BASE = Path(r"E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022")
RAW = BASE / "writer" / "opencode_writer_manuscript_0105_R07_raw.md"
OUT = BASE / "writer" / "opencode_writer_manuscript_0105_R07_release.md"
RECEIPT = BASE / "evidence" / "manuscript_release_transform_receipt_0105_R07.json"
EXPECTED_RAW_SHA256 = "31b7de140f4cd93169c709f30e111ca0994267b59fa6a76ec06ccc1fda5cea12"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


raw_bytes = RAW.read_bytes()
raw_sha = hashlib.sha256(raw_bytes).hexdigest()
if raw_sha != EXPECTED_RAW_SHA256:
    raise SystemExit(f"Raw manuscript changed: expected {EXPECTED_RAW_SHA256}; got {raw_sha}")

text = raw_bytes.decode("utf-8")
changes: list[str] = []


def replace_exact(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one source match, found {count}")
    text = text.replace(old, new, 1)
    changes.append(label)


replace_exact(
    "- 專案 `03_157_CHECKBOX_BLUEPRINTS.md` index 114：「績效改善調查與行動計畫追蹤」。index 114 為專案索引，**不**宣稱為官方印刷序號；相鄰 index 113 為獨立「其他」項目，**不得**與 0105 混用。本文件**不發明任何勾選序號**。",
    "- 本文件只依官方第 7 頁所列的調查與課後行動計畫佐證用途設計；其他評核項目須各依其正式來源核對。",
    "removed internal project index and neighboring-item crosswalk note",
)
replace_exact(
    "- **要求識別碼邊界（不作推定）**：本文件對應之官方要求識別碼為 `I18-E13`（依 R04 142 文件 crosswalk）。`I18-E12` **未**出現於本次取得之 crosswalk 列與官方要求內涵摘錄中；其官方意義、以及與本文件或其他文件之對照關係，狀態一律為 `UNKNOWN`。本文件**不**宣稱 `I18-E12` 為提示錯誤、**不**宣稱其屬於或不屬於任何特定文件，亦不據以推定任何關係。",
    "- 本工具只用於本節所述的問卷調查與課後行動追蹤，不取代其他指標各自要求的佐證。",
    "removed internal crosswalk uncertainty note while retaining human-facing scope boundary",
)
replace_exact(
    "**登錄原則**：①每一列只記**一項**虛構事實、數值、陳述或決策；②同一事實出現於多處者，於「位置」欄列出**全部**出現處；③「位置」採**手稿相對定位**（第 X 節／小節／表／欄／列），**全清冊禁止使用「同上」**，每一列之位置欄皆須可獨立解析；④同一數值若跨列重複登錄，必須指定**單一 owner 列**，其餘列以 fact_id 交叉引用並註明「須與 owner 列同步替換，不得各自替換」；⑤多事實列一律拆為多列單一事實（本版已拆分 F149→F149＋F155、F152→F152＋F156＋F157）；⑥狀態一律 `SAMPLE/SYNTHETIC; HOLD (unverified)`，**無任何一列為 REAL-VERIFIED**；⑦所有列同屬 `case_id = SYN-0105-CASE-01`、`document = 0105`（此二識別碼本身亦為虛構／文件事實，見 F001、F002）；⑧本清冊之**節次／表／欄／列定位索引**見第十五之一節；Word 頁碼與表格列索引之對照為**必要配套附件（REQUIRED_COMPANION）**，未交付前不得宣稱已完成頁碼層級定位替換。",
    "**登錄原則**：①每列記錄一項虛構資料、數值、規則或示範結論；②同一事實出現在多處時，逐一列出位置；③每列的位置均可單獨辨識，不使用「同上」；④重複數值指定一列作為主要替換來源，其他列以 fact_id 交叉引用並同步更新；⑤不同事實分列登錄；⑥所有列均為 `SAMPLE/SYNTHETIC; HOLD (unverified)`，沒有任何 REAL-VERIFIED 資料；⑦範例案件為 `SYN-0105-CASE-01`，文件編號為 0105。章節定位索引見本節後段；Word 頁碼與表格列定位另見隨附的〈0105虛構資料替換與頁碼定位清冊〉。",
    "replaced engineering-oriented register instructions with user-facing locator instructions",
)
replace_exact(
    "【SAMPLE/SYNTHETIC】本替換清冊共 **162 列**（F001–F162），涵蓋本文件中的虛構資料、題面、流程規則與示範結論。相對 R06 之 152 列：新增 F153–F162 共 10 列（F-03 兩列、F-06 拆分三列＋登錄規則一列、F-08 一列、F-02／F-09／F-10 相關三列），並將原「同上」定位列全部改為完整定位、對重複覆蓋組（F031↔F142、F032↔F143、F044↔F144）指定 owner 與同步替換要求。所有列均須以有權來源提供的真實資料逐項替換；本清冊沒有任何 REAL-VERIFIED 項目。",
    "【SAMPLE/SYNTHETIC】本替換清冊共 **162 列**（F001–F162），涵蓋文件中的虛構資料、題面、流程規則與示範結論。所有列均須由有權者依真實來源逐項替換；目前沒有任何 REAL-VERIFIED 項目。重複出現的事實已標示主要替換列，其他位置須同步更新。",
    "removed revision and reviewer-finding history from register summary",
)
replace_exact(
    "### 15-4 其餘操作欄位、示範文本與 R07 新增事實（F142–F162）",
    "### 15-4 其餘操作欄位、示範文本與流程規則（F142–F162）",
    "renamed register section without revision history",
)
replace_exact(
    "> 分段說明：本段收錄**敘述性示範文本、決策規則、檢核清單與 R07 修復新增**之虛構事實。R07 相對 R06 之新增列為 F153–F162。",
    "> 本段收錄敘述性示範文本、決策規則、檢核清單與操作欄位所需的虛構事實。",
    "removed internal repair-cycle note",
)

row_reasons = {
    "SYN-0105-F153": "表單版本與日期須由有權者填寫並確認；未完成前不得發放",
    "SYN-0105-F154": "資料保管角色須明確指定並確認後，才能啟動存取流程",
    "SYN-0105-F158": "使用前檢核與結案檢核屬不同時點，應分開記錄",
    "SYN-0105-F159": "逐題輸入與揭露限制可避免把診斷題誤作對外結果",
    "SYN-0105-F160": "目標差距計算只示範算法，不代表真實達標或結案",
    "SYN-0105-F161": "示範同意欄不得被誤認為真實同意或簽署證明",
    "SYN-0105-F162": "清冊須使每項示範事實可獨立定位並同步替換",
}
lines = text.splitlines()
for fact_id, new_reason in row_reasons.items():
    matches = [i for i, line in enumerate(lines) if line.startswith(f"| {fact_id} |")]
    if len(matches) != 1:
        raise SystemExit(f"{fact_id}: expected one register row, found {len(matches)}")
    i = matches[0]
    cells = lines[i].strip().strip("|").split("|")
    if len(cells) != 7:
        raise SystemExit(f"{fact_id}: expected 7 register columns, found {len(cells)}")
    if re.search(r"R0[1-9]|F-\d{2}", cells[3]):
        cells[3] = f" {new_reason} "
        lines[i] = "|" + "|".join(cells) + "|"
        changes.append(f"replaced internal change-history text in {fact_id}")
    else:
        raise SystemExit(f"{fact_id}: expected internal revision/finding note in reason column")
text = "\n".join(lines) + "\n"

replace_exact(
    "> 本索引為**文件內定位索引**，使每一列之「位置」可由節次層級獨立解析。**Word 頁碼與表格列索引對照為必要配套附件（REQUIRED_COMPANION）**：本手稿未附該對照；在該附件交付並經核對前，任何以頁碼／列索引宣稱完成的替換作業一律視為**未完成**，且不得標記為 REAL-VERIFIED。",
    "> 本索引提供章節層級的定位；Word 頁碼與表格列對照另見隨附的〈0105虛構資料替換與頁碼定位清冊〉。文件版面變更後，須重新核對附件中的頁碼與列次。",
    "replaced missing-companion warning with deliverable attachment reference",
)
replace_exact(
    "**替換清冊定位原則（R07）**：本文件的位置欄採**節次／小節／表／欄／列**之手稿相對定位，**全清冊禁用「同上」**；第十五之一節提供**文件內定位索引**（節次 → fact_id）。**Word 匯出 PDF 頁碼及表格／資料列索引對照為必要配套附件（REQUIRED_COMPANION）**，本手稿未附該附件；在該附件交付並經逐列核對前，頁碼層級之替換作業一律視為**未完成**。每次改版後須重新核對所有定位。來源無法查證時標示 `UNKNOWN`／`NOT_RECEIVED` 並 `HOLD`。",
    "**替換清冊定位原則**：清冊以節次、小節、表格、欄位與列次標示位置，並附 Word 頁碼及表格列索引。文件版面改動後，應重新核對所有位置；來源無法查證時標示 `UNKNOWN`／`NOT_RECEIVED` 並 `HOLD`。",
    "removed revision state and recorded the page/table locator attachment",
)
replace_exact(
    "**本手稿結束（R07 候選 Markdown 手稿；狀態：SAMPLE/SYNTHETIC、候選未驗收、非 CURRENT、非 REAL）。**",
    "**使用界線**：本文的題目、資料、流程與示範結論均為 SAMPLE/SYNTHETIC，不代表本會已採用、執行或核准。",
    "removed internal manuscript and candidate-status footer",
)

# Remove embedded engineering finding labels from instructions while preserving
# the substantive rules they annotate. Generalize the unresolved neighbor code
# instead of putting an internal crosswalk investigation into the association form.
text = re.sub(r"（F-\d{2}）", "", text)
replace_exact(
    "| 對 `I18-E12` 作任何歸屬或關係陳述 | 拒絕；狀態一律 `UNKNOWN`，不作推定（見第一節） |",
    "| 對未經正式來源支持的其他項目作歸屬或關係陳述 | 拒絕；先標示 `UNKNOWN`，不作推定 |",
    "generalized unresolved identifier hold rule",
)
replace_exact(
    "| 第一節 文件身分 | doc_id／requirement_id／index 114／I18-E12 邊界 | F001、F002（識別碼事實） |",
    "| 第一節 文件身分 | 文件編號、官方要求識別碼與用途界線 | F001、F002（識別碼事實） |",
    "removed internal index and unresolved neighbor identifier from section locator",
)
text = re.sub(
    r"\*\*本文件對應之官方要求識別碼為 `I18-E13`；`I18-E12` 未出現於本次取得之 crosswalk 列與官方要求內涵摘錄中，其官方意義與對照關係狀態為 `UNKNOWN`，本文件不作任何歸屬、錯誤與否或關係之推定。\*\*",
    "**本文件僅依其列明的官方要求與佐證用途設計；其他項目須另依正式來源核對，不作未經來源支持的歸屬或推定。**",
    text,
)
text = text.replace("I18-E12", "其他未經正式來源支持的要求項目")
if "I18-E12" in text:
    raise SystemExit("Unresolved internal identifier remains in release text")

for forbidden in (r"\bR0[1-9]\b", r"REVISION=", r"REQUIRED_COMPANION", r"F-\d{2}", r"I18-E12", r"R04 142"):
    if re.search(forbidden, text, flags=re.I):
        raise SystemExit(f"Internal engineering marker remains in release text: {forbidden}")

fact_ids = re.findall(r"^\| SYN-0105-F(\d{3}) \|", text, flags=re.M)
if fact_ids != [f"{n:03d}" for n in range(1, 163)]:
    raise SystemExit(f"Replacement register must retain contiguous F001-F162; got {len(fact_ids)} rows")
if "SAMPLE / SYNTHETIC" not in text or "NOT_RECEIVED" not in text or "HOLD" not in text:
    raise SystemExit("Required SAMPLE/REAL boundary or HOLD language missing")

OUT.write_text(text, encoding="utf-8", newline="\n")
receipt = {
    "receipt_id": "TTQS-0105-MANUSCRIPT-RELEASE-TRANSFORM-R07",
    "created_at_tpe": datetime.now().astimezone().isoformat(),
    "doc_id": "0105",
    "requirement_id": "I18-E13",
    "source_packet_sha256": "166338523fad5550511cd5f16fd7b347b28a23ef295fdc9396c21bb8728ae99e",
    "unique_blueprint_sha256": "0a457287fcc005e13408ad85763f4e7065dd1915f3f9b11757928c64715cb826",
    "writer_input_packet_sha256": "861d742be1f9b7dbb3bfc37f0b37957a42fd12064304f5c6342579cafbd60a71",
    "raw_worker_manuscript": str(RAW),
    "raw_worker_sha256": raw_sha,
    "release_manuscript": str(OUT),
    "release_sha256": sha256(OUT),
    "release_bytes": OUT.stat().st_size,
    "register_rows": len(fact_ids),
    "deterministic_changes": changes,
    "internal_metadata_scan": "PASS",
    "required_page_table_companion": "PLANNED_AS_SEPARATE_EXACT_SHA_ATTACHMENT; generated after final pagination",
    "formal_acceptance": "NOT_GRANTED",
}
RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
