# OpenCode v2 native-session reconciliation (rolling 24 hours)

Observed 2026-10-22T03:57:34+08:00 TPE; interval 2026-10-21T03:57:34+08:00 to 2026-10-22T03:57:34+08:00.

- Native TTQS session rows: 38; exact CLI invocation count: UNKNOWN.
- Tokens: input 2,478,098; output 330,727; reasoning 947,845; cache read 11,855,644; cache write 0.
- Local SQLite cost 0.00; vendor billing UNKNOWN. Actual serving/fallback identity UNKNOWN.
- R16: one bounded writer and one separate exact-SHA text reviewer; both native sessions ended succeeded.
- R16 Writer selected deepseek-v4.1-flash-free; native session ses_ea00e6c9bffeRq91HBDZl6RZBb.
- R16 reviewer selected mimo-v2.6-flash-free; native session ses_ea002ffe1ffefP6DIiuFo8fPbr; CLI exit 1 is preserved with provider error and recovered response.

Session-row count is not treated as CLI invocation count. Local cost is not vendor billing proof.
