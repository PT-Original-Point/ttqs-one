# DOCX 0064 R06 — targeted layout repair

- Requirement: I14-E05; official checkbox 069; unique Blueprint R02. The printed document ID is 0064 and is not the checkbox serial.
- Parent: `../0064_R05/0064_R05.docx`, SHA-256 `54888e13f954478051a49839d8b67ff845992c72811e41e09d90045e512c69e1`. R05 content and its 24 paired synthetic timing rows are preserved.
- R05 had a directly inspected, material defect: the §13.3 six-column table header was stranded at the bottom of page 19.
- R06 changes only six `w:keepNext` paragraph properties on that header row. After removing those six properties from R06 XML, its canonical Word document XML is byte-semantically equal to R05; visible-text SHA-256 remains `f36d9406f395f0f32416c600b165d0c5810d9040d0c4265e1838e3761b76aedf`.
- R06 DOCX SHA-256: `7dd39bffc4aa7ac94eeace73bec6135bfd1c9b8c216e2de7579d0cc4c35d2764`. Word COM produced a 28-page PDF. Page 19 is the only rendered PNG whose hash differs from R05; it was directly inspected and the orphan header is gone. The other 27 images match R05 exactly, including page 20's repeated header and data rows.
- Technical/layout status: targeted repair PASS. Semantic status: R05's independent semantic PASS is inherited for unchanged visible content only; no fresh exact-R06 SHA semantic review is claimed. Overall remains a CANDIDATE pending that review; no REAL evidence or formal Human acceptance is claimed.
- Source/Blueprint/replacement register remain in the unchanged R05 package: `0064_R05/official_source.pdf`, `0064_R05/0064_UNIQUE_BLUEPRINT_R02.md`, and `0064_R05/evidence/synthetic_replacement_register_R05.csv`; exact SHA values are recorded in the R06 receipts.
