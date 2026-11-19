# 0122 R02 OpenCode free-limit dispatch evidence

Work: `TTQS-0122-I19-E10-R02-W1-GLM53-FREE-EXACT-SHA-REVIEW`  
Document / requirement: 0122 / I19-E10  
Candidate SHA-256: `d3a6a1222d0389172dc6ab9737d06c5e46f4b45ed3a661324f3b885b751b7b86`  
Input bundle SHA-256: `ac6efb18ffb6c9768fdbc8cb7741ed2f852815d559004b21f4c00cf7508d7600`  
Review request SHA-256: `6b01dbff35419dd416ef21bdef416fe0ab97a6a928481cb5ebd02232742a2eaf`

The single bounded OpenCode v2 CLI request selected `opencode/glm-5.3-flash-free` explicitly. It returned `provider.free-limit` / `FreeUsageLimitError` (status 429) before producing review content. Sanitized session metadata records provider `opencode` and model ID `glm-5.3-flash-free`; inference did not complete, so no semantic verdict exists. Cost and token counters are zero. The DOCX SHA before and after is unchanged. No fallback or second model was attempted.

Provider retry delay: 44111000 ms. Error event: 2026-10-27 19:44:49.090 +08:00. Same-route retry not before: 2026-10-28 08:00:00.090 +08:00. This is a provider delay, not a guarantee that capacity will return.

The attached public OpenCode monitoring report describes cross-user incidents and model availability, not this account. This Windows 429 is the direct account evidence. We will not switch models to work around this provider quota response. This blocks the 0122 exact-SHA semantic review pending a legitimate capacity reset; unrelated READY stages may continue. Formal acceptance remains NOT_GRANTED; REAL evidence remains UNKNOWN_NOT_SUPPLIED.
