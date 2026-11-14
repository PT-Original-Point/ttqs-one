# Word export attempt 01 — recovered stage transcript

Evidence source: the R11 pre-retry PowerShell readback of `word_export_R07_stages.log` in the active Codex execution. The original log file was not separately hashed before the subsequent run. The existing exporter clears that log at startup, so the earlier bytes were overwritten by the successful run. This note is a transcript reconstruction, not the original log; its original SHA-256 is UNKNOWN.

Observed prior stages (UTC):

```text
2026-10-23T23:29:26.6973435Z STAGE=inputs
2026-10-23T23:29:26.8384460Z STAGE=before_com_create
2026-10-23T23:29:29.5535429Z STAGE=after_com_create
2026-10-23T23:29:29.7017604Z STAGE=new_word_ids=14848
2026-10-23T23:29:30.0001042Z STAGE=before_open
2026-10-23T23:29:30.8110313Z STAGE=after_open
2026-10-23T23:29:31.8551551Z STAGE=before_export_pages=12
```

No exception or `after_export` line was present in the pre-retry log. PID 14848 was observed exited before the successful R11 rerun. The R07 DOCX stayed at SHA-256 `82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c`. A separate successful hidden Microsoft Word COM run later produced the 12-page PDF recorded in `visual_qa_R07_R11.json`.
