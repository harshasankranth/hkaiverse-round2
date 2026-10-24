# Test results (synthetic data)

| Case | Setup | Expected | Actual | Result |
|---|---|---|---|---|
| 1. Normal | Complete request, payment found, SEC-A has seats | REGISTERED in SEC-A | REGISTERED in SEC-A | PASS |
| 2. Missing information | No section preferences entered | NEEDS_CORRECTION, then REGISTERED after fix, original timestamp kept | NEEDS_CORRECTION, then REGISTERED; timestamp kept: True | PASS |
| 3. Duplicate | Same student submits twice | Second request merged; only one seat used | first=REGISTERED, second=DUPLICATE_MERGED, SEC-A seats left=1 | PASS |
| 3b. Duplicate arriving out of order | Earlier copy reaches the desk after the later copy | Earlier submission kept as the main request; later copy merged; one seat used | early=REGISTERED (t=09:00), late=DUPLICATE_MERGED, SEC-A seats left=1 | PASS |
| 4. Unauthorized | CSE student requests a section restricted to AI/AIML | REJECTED with reason, no seat used | REJECTED, AI-ONLY seats left=2 | PASS |
| 5. Failed step | Payment service down; two students waiting (1 seat in SEC-A) | Both PAYMENT_PENDING; after recovery the EARLIER submitter gets SEC-A | during outage=('PAYMENT_PENDING', 'PAYMENT_PENDING'); S005 -> SEC-A, S006 -> SEC-B | PASS |
| 6. Illustration: processing order vs submission order | 4 students want SEC-A (2 seats); latest forms are processed first | Legacy: seats go to the latest submitters. Proposed: seats go to the earliest. | legacy winners=['S104', 'S103']; proposed winners=['S101', 'S102'] | PASS |

7/7 cases passed.
