# Capstone demo results (synthetic data)

Invented requests: 208 (200 students plus duplicates), seed 2026.

| Outcome under the proposed rules | Count |
|---|---|
| DUPLICATE_MERGED | 8 |
| NEEDS_CORRECTION | 7 |
| REGISTERED | 164 |
| REJECTED | 3 |
| WAITLISTED | 26 |

Seat assignments identical when requests arrive in two different random orders: **True**

| Preference received | Proposed (by submission time) | Modelled old behaviour (late forms first) |
|---|---|---|
| First choice | 130 | 126 |
| Second choice | 26 | 26 |
| Third choice | 8 | 13 |
| No seat (waitlisted) | 26 | 25 |

Compared with the modelled old behaviour, 62 students get a better-ranked outcome under submission-time allocation and 58 get a worse-ranked one.
The totals barely change. The rule moves popular seats to whoever submitted first; it does not create seats. Its value is fairness and predictability, not more first choices.

This models my **hypothesis** about the cause (processing order). It is not evidence that the real process behaves this way.
