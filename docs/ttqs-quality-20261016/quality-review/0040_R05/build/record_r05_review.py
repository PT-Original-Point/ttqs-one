from pathlib import Path
import hashlib, json

P = Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0040_R05')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
raw = P / 'evidence/qa/0040_semantic_review_r05_crossreview_raw.md'
candidate = P / 'candidate/0040_R05.docx'
raw_sha = sha(raw)
candidate_sha = sha(candidate)
if candidate_sha != '95531ac5f8a79eed7c605f3ab1f42da3948e8f15316499d325b606bd6d434384':
    raise SystemExit('R05 candidate bytes changed; refusing to bind review')
review = {
    'project_id': 'TTQS_ONE', 'doc_id': '0040', 'revision': 'R05',
    'requirement_id': 'I08-E03', 'official_checkbox_sequence': '040',
    'candidate_sha256': candidate_sha, 'verdict': 'PARTIAL',
    'reviewer_route': 'separate read-only cross-review agent; writer identity separation not independently documented',
    'raw_review_path': 'evidence/qa/0040_semantic_review_r05_crossreview_raw.md',
    'raw_review_sha256': raw_sha,
    'reviewed_artifact_sha256': {
        'rendered_pdf': 'dd4d8ea87cdb8ca22ef549ef496e61a5da38ffd0720c548895988f39daf7e',
        'synthetic_register': '35cdb226aa14f8b36304ed5d22031e3ccd5f1c77d98851e968f8ca64ee0e1788',
        'official_source_pdf': '805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709',
        'unique_blueprint_row': 'ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943'
    },
    'criteria': {
        'official_mapping_and_genre': 'PASS', 'title_blind_and_neighbor_distinction': 'PASS',
        'operational_maturity': 'PARTIAL', 'calculations_and_data_consistency': 'PASS',
        'cross_document_case_consistency': 'PASS', 'sample_real_and_authority_boundary': 'PASS',
        'replacement_register': 'PARTIAL', 'R04_regression_repair': 'PASS',
        'visual_readability': 'PASS', 'docx_version_metadata': 'PARTIAL'
    },
    'findings': [
        {'id':'R05-F01','locator':'printed p.3, K1-K4 evidence/locator/responsibility column; printed p.5 D04 table',
         'finding':'The matrix and D04 example do not provide a fillable original-record identifier or attachment/file/page location. Tool page navigation is not source-evidence location.',
         'required_action':'Add a usable evidence ID/location field with a clearly synthetic pointer and an instruction to enter the controlled real file/attachment/page when authorized.'},
        {'id':'R05-F02','locator':'replacement register row 0040-SYN-009; printed pp.1 and 6',
         'finding':'The 30-day follow-up authorization rule on p.1 and the D04 rescore-not-executed fact on p.6 are different facts; the combined locator incorrectly makes the latter evidence for the former.',
         'required_action':'Separate the register facts and bind each to its own precise locator.'},
        {'id':'R05-F03','locator':'DOCX package docProps/core.xml',
         'finding':'Document description still says R04 and revision is 4 although the candidate is R05.',
         'required_action':'Set document properties to the actual new revision; do not alter printed substantive content for this metadata correction.'}
    ],
    'scope_limitations': ['Reviewer directly inspected all eight rendered pages.', 'No claim of formal acceptance or association approval.', 'Builder identity not independently evidenced.'],
    'candidate_state': 'CANDIDATE_NOT_PROMOTED', 'formal_acceptance': 'NOT_GRANTED'
}
(P/'evidence/qa/0040_semantic_review_r05_exact.json').write_text(json.dumps(review, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
progress_path = P/'PROGRESS.json'
progress = json.loads(progress_path.read_text(encoding='utf-8'))
progress['status'] = 'CANDIDATE_SEMANTIC_PARTIAL_REPAIR_REQUIRED'
progress['independent_semantic_verdict'] = 'PARTIAL'
progress['independent_semantic_review_path'] = 'evidence/qa/0040_semantic_review_r05_crossreview_raw.md'
progress['independent_semantic_review_sha256'] = raw_sha
progress['known_limitations'] = [
    'R05-F01: add a usable, explicitly synthetic evidence ID and original attachment/file/page locator to the p.3 matrix and p.5 D04 example.',
    'R05-F02: split the p.1 30-day authorization rule from the p.6 D04 rescore-not-executed fact in the replacement register.',
    'R05-F03: correct core properties description and revision to the actual R06 candidate in the targeted repair.'
]
progress['github_sync_status'] = 'PENDING_R05_PARTIAL_REVIEW_SYNC'
progress['source_audit'] = {
    'command': 'TTQS_ONE_EXTERNAL_AUDIT_FINDINGS_20261016_CONTINUE',
    'path': 'docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md',
    'live_source_commit': '9c9bbfe537af6aecd616fcba85cfd1a10bbdb057',
    'live_source_blob_sha': '70449889fd464106fe204496004bee13018d4a51',
    'state': 'APPLIED_PARTIAL',
    'evidence': 'R05 exact-SHA semantic PARTIAL persisted; targeted R06 repair required; unrelated findings remain separately tracked.'
}
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
readme = f'''# DOCX 0040 R05 — semantic review disposition

**State:** candidate only. Technical and primary visual checks passed; the independent exact-SHA semantic review returned **PARTIAL**. R05 is preserved unchanged as the reviewed parent; no promotion or formal acceptance is granted.

- Official requirement: I08-E03 / evidence-table sequence 040; training-institution evidence table PDF p.3.
- R05 candidate SHA-256: `{candidate_sha}`; it remains byte-identical to the reviewed artifact.
- Independent verdict: PARTIAL — see `evidence/qa/0040_semantic_review_r05_crossreview_raw.md` and normalized receipt `evidence/qa/0040_semantic_review_r05_exact.json`.
- Reviewer raw-response SHA-256: `{raw_sha}`.
- R05 findings: (1) add a usable original-evidence identifier and file/attachment/page field to the p.3 matrix and p.5 D04 example; (2) separate the p.1 30-day authorization rule from the p.6 D04 rescore status in the synthetic register; (3) correct core properties that still identify the file as R04/revision 4.
- R05 technical receipt: PASS; primary visual review of all eight pages: PASS. Those results do not override the semantic PARTIAL.
- R05 remains `CANDIDATE_NOT_PROMOTED`; formal acceptance is `NOT_GRANTED`.

The findings are being addressed in a new R06 candidate with changes limited to those specific locations and document properties. No other R05 content is silently promoted or overwritten.
'''
(P/'README.md').write_text(readme, encoding='utf-8')
manifest_path=P/'artifact_manifest.json'
files=[]
for f in sorted(P.rglob('*')):
    if f.is_file() and f not in {manifest_path, progress_path}:
        files.append({'path': f.relative_to(P).as_posix(), 'bytes': f.stat().st_size, 'sha256': sha(f)})
manifest={'project_id':'TTQS_ONE','bundle':'0040_R05','manifest_scope':'All files except top-level artifact_manifest.json and mutable PROGRESS.json.','hash_method':'SHA-256 over exact files and Git blobs; .gitattributes prevents text normalization.','files':files}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'candidate_sha256':candidate_sha,'raw_review_sha256':raw_sha,'normalized_receipt_sha256':sha(P/'evidence/qa/0040_semantic_review_r05_exact.json'),'progress_status':progress['status'],'manifest_files':len(files)}, ensure_ascii=False))
