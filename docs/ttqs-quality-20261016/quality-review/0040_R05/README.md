# DOCX 0040 R05 — targeted repair

**State:** candidate only. Technical and primary visual checks passed; independent semantic exact-SHA review is pending. No promotion or formal acceptance is granted.

- Official requirement: I08-E03 / evidence-table sequence 040; training-institution evidence table PDF p.3.
- Unique Blueprint row SHA-256: `ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`.
- R05 candidate SHA-256: `95531ac5f8a79eed7c605f3ab1f42da3948e8f15316499d325b606bd6d434384`.
- Parent R04 candidate SHA-256: `be163030c29effe4067e4be1d5bc6f041a48020fbbaf5659716c87094305a44e`; R04 is preserved at `../0040_R04/` with exact-SHA PARTIAL review and raw reviewer reply.
- Synthetic replacement register: 39/39 rows bound to the R05 exact SHA; register SHA-256 `35cdb226aa14f8b36304ed5d22031e3ccd5f1c77d98851e968f8ca64ee0e1788`.
- Word render: 8 pages; PDF SHA-256 `dd4d8ea87cdb8ca22ef549ef496e61a5da38ffd0720c548413895988f39daf7e`. All eight page images were directly inspected. Pages 1–6 have identical normalized extracted text to R04. Technical receipt reports 39/39 current printed-page anchors.
- The R04 repair was limited to pages 7–8 and the documented locator gaps. Scores, thresholds, formulas and D04 sample facts remain unchanged.
- The body now provides use/effectivity guidance and a task-based operating index. Internal hashes, item IDs, reviewer history and line-by-line audit mappings stay in sidecars.
- The example is SAMPLE/SYNTHETIC only. No association approval, actual course execution, attendance, learner scores, outcomes, signature or third-party original is claimed.

**Quality evidence**

- Technical: PASS — `evidence/qa/0040_technical_review_r05_exact.json`.
- Primary visual: PASS — `evidence/qa/0040_visual_review_r05_primary.json`; direct inspection covered printed pages 1–8 at 140 dpi.
- Independent semantic: PENDING — must review the exact candidate SHA above after GitHub synchronization.
- Candidate state: CANDIDATE_NOT_PROMOTED; formal acceptance NOT_GRANTED.

The canonical LibreOffice renderer was unavailable because `soffice.exe` is not installed on PATH. Rendering used Microsoft Word COM `ExportAsFixedFormat` and bundled Poppler `pdftoppm`; the source DOCX SHA remained unchanged during rendering.
