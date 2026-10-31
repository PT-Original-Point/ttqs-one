# 0006 / I01-E03 — R05 candidate and review-route failure

- State: candidate only; no formal acceptance.
- Official source: `TTQS查核佐證文件資料表-訓練機構版 (2).pdf`, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; requirement `I01-E03` (document ID 0006 is not an official checkbox serial).
- Unique Blueprint SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; row SHA-256 `dd26f0d7d84e455540d68fe51b6a5e19dd5ebb2d42b84bf269fbcc726acbeb6a`.
- Candidate DOCX SHA-256: `46300a0a565dd1e7b8e81997680c949fbfbd97e5b3e0cac07c79709f2014c71e`.
- Deterministic technical QA: PASS. Word-native PDF render and layout-delta visual QA: PASS for the recorded scope. See exact receipts and rendered PDF in `qa/`.
- Independent semantic review: **not obtained**. OpenCode v2.2.5 session selected `opencode/mimo-v2.6-flash-free` and terminated with `provider.free-limit`, HTTP 429, before returning a review. The exact retry eligibility reported by the provider is `2026-11-01T08:00:00.539+08:00` (Taipei). Output: one token; no review answer. Provider-served model identity remains UNKNOWN. See original raw stdout, dispatch input, review packet, and terminal receipt under `worker/`.
- R05 material changes are scoped to the `0006/I01-E03` document. All examples remain SAMPLE/SYNTHETIC; no REAL association performance, approval, signature, or third-party original is asserted.
- The candidate must not be counted as fully quality-accepted until a fresh independent semantic review binds PASS to this exact SHA. Formal acceptance remains not granted.
