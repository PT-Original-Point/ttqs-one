# 0142 I19-E32 Candidate Lineage Chain R08-TR01

## Identity and evidence boundary

Project TTQS ONE; doc_id 0142; official requirement I19-E32; checkbox index 156; printed checkbox serial UNKNOWN.
Source packet SHA-256: e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49.
Unique Blueprint SHA-256: 4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b.
Current R08-TR01 candidate SHA-256: 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78. Candidate remains SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD; formal acceptance NOT_GRANTED.
Parent lineage JSON CANDIDATE_LINEAGE_0142_R07.json SHA-256: 26649bd598d3f57739dee7e353e51cf181264d446580445462a2f78c27c639bc. R07-LF01 extension CANDIDATE_LINEAGE_0142_R07_LAYOUTFIX_R01.json SHA-256: f805ee51ee1a4a3b09d78eded51477e59f8a5bacd4ccf8a6e386dccb42a764e5.
R01 baseline hash is preserved exactly as recorded in the parent lineage. Original bytes were not found in the searched 0142 source tree, so the historical baseline hash is not claimed as independently recalculated.

## Selected parent chain

| Revision | Parent SHA-256 | Candidate SHA-256 | Local byte verification and note |
|---|---|---|---|
| R01 baseline | — | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | Hash recorded in parent lineage; original DOCX bytes not found in searched 0142 source tree, so not independently recomputed. |
| R03 selected table-cell margin | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | Local SHA-256 recomputed. |
| R04 selected table flow | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | Local SHA-256 recomputed. |
| R05 header contrast | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | Local SHA-256 recomputed. |
| R06 structural completion | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | Local SHA-256 recomputed; prior semantic review PARTIAL applies only to this exact SHA. |
| R07 targeted semantic repair | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | Local SHA-256 recomputed. |
| R07-LF01 layout-only repair | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | Local SHA-256 recomputed; only empty manual page-break paragraph before Section 5 removed; non-empty body/table text unchanged. |
| R08-TR01 targeted semantic repair | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78 | Local SHA-256 recomputed; repairs F1-F6 in the exact parent review. |

R02 math/flow candidates and the separate R03 flow-fix lineage are parallel historical branches in the supplied parent JSON; they are not ancestors of the selected R06 to R07 chain, and their verdicts are not transferred.

## Exact-SHA review and QA

R07-LF01 OpenCode review returned PARTIAL on exact candidate SHA ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f. Actual OpenCode route: opencode/deepseek-v4.1-flash-free; session ses_e7f5bb7edffeTU85K8yTYjVT8R; session outcome succeeded; reported cost 0; account billing remains UNKNOWN.
Original reviewer response SHA-256: 2adc48777fe86b044258b2aa79f00a104d11b734332bfa742f95342750b0f6a9; sanitized session export SHA-256: 3089622869d1de32bb4e28e0f203f8b35e3c81d0edab0e505acd9398fefdcae1; dispatch receipt SHA-256: 8d0c062d102a16806d20219e707318f2c480711fb3813a774e2b89970fc780b5.
The six findings and their R08 repairs are enumerated in PATCH_RECEIPT_0142_R08_TARGETED_REPAIR_R01.json.
R08 technical QA receipt SHA-256: 474094109308849a9bcfeddb7d94b0c068f93199082b8c72e19e48b81b38b1f1 (PASS).
Word-native render receipt SHA-256: d2d93a1fd7c8fb54c14da3ff180257ea02547bba60d9b5696c56d6f220eefc0e; PDF SHA-256: 718b5807164bec5e1d519f8ac52236f3e45ae17f040edc5b25f76791a4ca6c2e; 14 pages; DOCX unchanged by render.
Page-image manifest SHA-256: d5b7ab71332583549b1971f3599dae5cbc712712bc5e697f8f84a0c2ba5a561f; visual QA SHA-256: 0f08c04c7b9ae98ae3888703f1126537b16c5a37b2d8b74c19219997499530dc (all 14 pages visually inspected at original resolution, PASS).
Replacement register SHA-256: b9ef1b7f1c9b703377f0284582cc72c4251d483cbeeae3adf8f6279e6aaa372b.

No candidate evidence here establishes REAL association performance, formal acceptance, or an official score.

## R12 per-stage metadata readback

This table separates recorded build dates from filesystem timestamps. Filesystem mtime is observational metadata only and is not represented as a build event. R01 source bytes remain unavailable; its historical SHA is not independently verified. For each present selected-chain DOCX, the local SHA-256 and byte count below were read from the exact Windows path.

| Stage | Revision/version label | Candidate SHA-256 | Bytes | Recorded build date | Filesystem mtime (not build-date proof) | Change type | Verifier/evidence |
|---|---|---|---:|---|---|---|---|
| R01 baseline | R01 baseline | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | UNKNOWN | UNKNOWN | NOT_AVAILABLE | baseline candidate; original bytes absent from searched local source tree | No original binary; SHA exists only in historical parent lineage; not independently recomputed. |
| R03 selected table-cell margin | R03 | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | 44984 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:19:38+08:00 | selected table-cell margin repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R04 selected table flow | R04 | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | 44991 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:21:38+08:00 | table-flow repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R05 header contrast | R05 | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | 44998 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:23:50+08:00 | header-contrast repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R06 structural completion | R06 | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | 50454 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T10:48:30+08:00 | structural completion | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R07 targeted semantic repair | R07 | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | 52863 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T11:37:42+08:00 | targeted semantic repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R07-LF01 layout-only repair | R07-LF01 | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | 50156 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T11:46:42+08:00 | remove one empty manual page-break paragraph; non-empty body/table text unchanged | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R08-TR01 targeted repair | content version 1.3/R08; build R08-TR01 | 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78 | 53207 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T12:03:08+08:00 | targeted repairs for prior F1-F6; no financial figures changed | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |

R12 finding: the selected R01→R08 chain is recorded, but R01 bytes and build date remain UNKNOWN. Do not promote the historical R01 hash to a locally verified binary. This sidecar inventory does not change the R08 DOCX bytes.
