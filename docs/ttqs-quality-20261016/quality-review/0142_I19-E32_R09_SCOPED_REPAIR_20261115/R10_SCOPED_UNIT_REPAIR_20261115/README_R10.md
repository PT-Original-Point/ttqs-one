# 0142 R10 Scoped Unit Repair

Scope: repair only four percentage-result unit cells in the I19-E32 candidate after the W1 exact-SHA review found that those rows displayed 新臺幣元 instead of %.

- Input candidate (R09) SHA-256: 5002813a2492cddbd304051b3af4dd40feb35d580956fcb86c1f10cf2b3fea19
- Output candidate (R10) SHA-256: 127d419e4b3814f66669730212b474b1d1219fa1377374cfdacd424798b27e1c
- Extracted body R10 SHA-256: 0fc364c97d6a559f0f0d4a013ac7bd1c0664a71d040726b7364b2c8ca5096bbd
- Official source packet SHA-256: e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49
- Unique Blueprint SHA-256: 4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b
- Crosswalk SHA-256: 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679

Deterministic Word COM readback confirmed the four changed cells. Four percentage calculations passed. The candidate rendered as a 10-page PDF; all ten page images were visually inspected and recorded in qa/VISUAL_RECEIPT_R10.json.

A fresh Antigravity CLI review was dispatched against the exact R10 DOCX/body SHA using the requested gemini-3.8-flash-high route. The returned text review is PASS_TEXT_ONLY, zero findings, and zero tool calls. Provider-serving model identity remains UNKNOWN; the response does not verify real financial records or confer association approval.

Status: CANDIDATE_QA_COMPLETE_NOT_ACCEPTED. REAL evidence and formal acceptance remain separate.