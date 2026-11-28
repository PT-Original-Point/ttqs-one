# DOCX 0059 R02 replacement-register scope

- Mapping: DOCX 0059 / I13-E03 / official checkbox 063.
- Candidate DOCX SHA-256: 0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0 (unchanged).
- R01 register SHA-256: 7B54314FC9B416B0F87BE90383F3F2D639324AEF22BDB80D890CF271A3B15BA0.
- R02 register SHA-256: 1D49C8C5120278DD3C282518A4554A25C23014DD42A2FEDFC88CFB82CAFA80CA; 270 rows; 190 inherited rows, 80 additions.
- The original 190 facts were retained; only the 13 locators F063 and F105-F116 were clarified.
- Two duplicate additions were removed (F216 merged into F215; F225 retained through existing F187).
- Added 63 selected DeepSeek rows and 17 explicit REJECT/HOLD controls copied from body sections 12.3-12.4. These controls remain SAMPLE_UNVERIFIED and are not asserted as Association policy.
- Official-source statements (§2), the author checklist (§12.6), and the SHA-bound QA control (§12.7) are classified separately; they are not sample facts or independent acceptance evidence.
- The DeepSeek response had one incomplete JSON boundary at F262. A deterministic format-only repair restored the missing fields using the identical field values used by adjacent checklist rows; the original raw stdout is preserved.
- The MiMo audit summary contained a Q2 denominator discrepancy. The final body states 12 valid answers, 48/12=4.0; the R02 register follows the body and flags this for independent verification.
- No DOCX bytes were changed. The R02 sidecar is a candidate pending independent exact-SHA review.
