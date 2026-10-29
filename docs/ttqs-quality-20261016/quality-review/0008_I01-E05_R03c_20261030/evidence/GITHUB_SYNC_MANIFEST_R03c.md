# 0008 / I01-E05 — R03c candidate evidence manifest

Observed (Asia/Taipei): 2026-10-30T00:36:08.315689+08:00

- **Candidate state:** CANDIDATE / SAMPLE / SYNTHETIC; not formally accepted.
- **Official mapping:** doc_id `0008`; checkbox and requirement `I01-E05`; unique Blueprint row `I01-E05`.
- **Source SHA-256:** official requirement PDF `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; Blueprint file `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; Blueprint row `3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d`.

- **DOCX SHA-256:** `39a41b63f2e7704d9b004923e8fbc9d9dadc54855e229646ccbf080e1e8a9487`
- **Technical QA:** PASS within technical scope: DOCX package integrity, 20 tables, 3 sections, body text ≥10.5 pt, table text ≥9.5 pt, 594 unique fact IDs matching the source, and native render/PDF hash linkage.
- **Visual QA:** PASS within visual layout scope: native Word render, 117/117 pages reviewed through 30 contact sheets; pages 20, 116, 117 inspected at full resolution. R03c fixed SF fact_id wrapping and lifted caption text to the 10.5 pt floor.
- **Independent semantic QA:** PENDING for exact R03c SHA. Do not treat the R02 reviewer PARTIAL as an R03c review.
- **Real evidence:** UNKNOWN / NOT ASSERTED. SAMPLE data, assumptions, and replacement register remain synthetic; association-specific policy and approval remain UNKNOWN/HOLD.

## Included files

| File | SHA-256 | Bytes |
|---|---|---:|
| `candidate/0008_I01-E05_R03c.docx` | `39a41b63f2e7704d9b004923e8fbc9d9dadc54855e229646ccbf080e1e8a9487` | 109493 |
| `candidate/0008_I01-E05_R03.md` | `16f9a19a46fedc9f2207e558df268460a6014c1b6ea8bd2deb56e8fa816c936b` | 226725 |
| `evidence/0008_I01-E05_R03c.pdf` | `0142ac80bd551121b42b7f80da032c27120c17313c90f28cf1521bfcdffa292c` | 2226598 |
| `evidence/DOCX_TECHNICAL_QA_R03c.json` | `b1530bf4073287a5142fde80e9b50b44e71d391eeca9fcedd3260610b2b5dc61` | 2722 |
| `evidence/WORD_VISUAL_QA_R03c.json` | `b1d2445e62bf74ade575909a67c27cb4957fd1a700ffc2eb07b4f20e1717651a` | 1623 |
| `evidence/WORD_NATIVE_RENDER_RECEIPT.json` | `e081943075a20b243c45881c56f6f13648c0d02d16a5848846debb0558795a7f` | 727 |
| `evidence/DETERMINISTIC_QA_R03.json` | `63ba27f0e377744754c0abd09fbc8855cf50884f550fca69228480b0252d5b21` | 2077 |
| `evidence/R03_REPAIR_RECEIPT.json` | `33e97460fab592455664f9c16dfc5500d0dc61ee96d1a92094d075842d3447d6` | 2371 |
| `evidence/SEMANTIC_REVIEW_R02_ORIGINAL.json` | `62e70314115e0ebc5fe2e78971629eff9a9b9cc10cf198396c6591cfcfc8524d` | 18685 |
| `evidence/WRITER_RECEIPT_R02_ORIGINAL.json` | `37498005fb2fbaab3f394af04236ae663f27d13d79ce0c8928453cdd340bbd33` | 6582 |
| `build/build_0008_r03_docx.py` | `b8f7cdb8fb4886143b43807a1b0a54405bac0e87ba3990b5a7707c2922dcb13e` | 11137 |
| `build/audit_R03c.py` | `6de1e90879d96fe18385f8cde98b414c464e85d548d91c9ce15cc8d95091fc4a` | 6450 |
| `build/make_contact_sheets_R03c.py` | `01cefe97446a70ae616014924a291fda5da4f3c0efc0615e89d7811febe8e6a1` | 1624 |
| `build/make_manifest_R03c.py` | `9bfb94c1b32b9c4f17c336140459fb6034c526e6355adbff1023c663e31fda50` | 5637 |
| `build/word_native_render_R03.ps1` | `e5a87f257a64d94be8f4de617c829a544f1296a108f1dc35ecd65d65180aedd8` | 2445 |

## Artifact status

This package supports technical and visual layout inspection only. It is not a formal acceptance or real-world evidence package. The R02 independent review and its original writer receipt are retained as historical inputs; their verdict is not transferred to R03c.
