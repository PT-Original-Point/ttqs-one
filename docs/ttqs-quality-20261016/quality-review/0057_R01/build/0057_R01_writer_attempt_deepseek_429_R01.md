# DOCX 0057 R01 Writer attempt — OpenCode DeepSeek free quota

- Requested route: OpenCode CLI v2.0.29, `opencode/deepseek-v4.1-flash-free`.
- Session: `ses_eb54f9733ffeXo3YWcFgugDHrL`.
- Result: provider returned `429 FreeUsageLimitError` / `provider.quota` before any tool call or file write; CLI exit code `1`.
- Raw stdout SHA-256: `a0ec547cf6fe3496968ccf7ee7ade616e8f0e450e954ce9dab6370bdb8275ced`; stderr is empty.
- Local readback: candidate `candidate/0057_R01.docx` does not exist; no partial artifact or active Writer remains. The only surviving OpenCode process is the background `serve --service` process.
- Recovery: keep the OpenCode route active and retry this same bounded build once using the recently successful `opencode/glm-5.3-flash-free` free model. Do not create another scheduler or Worker. This records one upstream quota error; fallback recovery remains pending verification.
