# 0110 / I18-E19 R07 candidate status

**State:** CANDIDATE; independent semantic review `PASS_CONTENT_TEXT_ONLY` on the extracted full candidate text and current register; formal acceptance NOT_GRANTED. All worked records are SAMPLE/SYNTHETIC; REAL association evidence remains UNKNOWN/HOLD.

## Exact binding

- DOCX SHA-256: `9a306bf5712437ee578867b745e7d0811959decaa862ed540a82e7e8553bd3c2`
- Official requirement: `I18-E19`; `doc_id=0110`; official checkbox serial remains UNKNOWN.
- Source packet SHA-256: `e3db8f4ed82b21de4dc8cfb5886c4387c123d49a0465356354a18a9be39a8d38`; source commit `db0cd977151dd8623ca6055acdc55dd9c852aa08`.
- Unique Blueprint SHA-256: `81ec1fc96c9d48fa2a088fbe32ecf8bc31abd88a3d8945ba22585226440a8796`.
- Synthetic replacement register SHA-256: `684f044816f0df740ab01dff92979fd47734e46e03fe5f037161ed56015ed3de`; 213 unique field paths, including 198 R03 base records plus R07 facts.
- Technical receipt SHA-256: `43cfbc116adda9abc38ed9b26a130dcda54ecfce273a534e04a69fe92935cfbf`; PASS for listed technical/content checks only.
- Word-native visual receipt SHA-256: `29ad9676fb91f2a344d17857b521c96e6ee6d297c6fefdac65b8cdbbf6f930c8`; Microsoft Word PDF SHA-256 `27a0564d5a628742b08c5c8b943941412f16d4c688accb933f8318b2a93204a7`, 26 pages; all 26 final2 images match that receipt.
- Independent semantic receipt SHA-256: `5e2387629c39e137a0c68e0bc6fd64bf5bd643fe70902aa18866c1dbee70ee56`; actual reviewer model `opencode/mimo-v2.6-flash-free`, session `ses_e98f805ffffeeg1EngR4tw3kme`; native session reports 43,126 input, 4,448 output, 9,920 reasoning and 4,800 cached input tokens; native cost 0, provider billing UNKNOWN.

## Scope, limits and remaining observations

The reviewer read the full extracted DOCX content (paragraphs P001–P302, tables T01–T37), official packet, Unique Blueprint, R06 FAIL review and full 213-record R07 register. The reviewer did not open or rehash the DOCX bytes or inspect page images; the local worker/packet-to-DOCX SHA binding and separate Word-native visual receipt are preserved independently. The reviewer returned PASS and recomputed the respondent and outcome arithmetic. Four non-blocking observations remain: P080 stop wording can be narrowed to C01; inline T37 should identify L02 as a self-efficacy proxy; some narrative synthetic strings rely on replacement instructions rather than individual register rows; L04 choices descend 4→1 while other items ascend. These do not change the reviewer verdict, but remain visible for future bounded polish.

R07 preserves raw learner L06 and excludes it as HOLD/INVALID (`L04=0`, `L10=X`): valid learner return is 7/8 = 87.5%. Baseline versus post-training client windows are distinct. D0+30 is interim: 7/8 = 87.5% is below the fixed-denominator ≥90% target, so REVISE; final D0+60 is pending and no CLOSE is asserted. No real association respondents, course, outcome, approval, signature or third-party evidence is claimed. Do not promote on technical/layout/content PASS alone.
