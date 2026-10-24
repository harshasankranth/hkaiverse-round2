# AI-use record

**Tool:** Claude (Anthropic), Sonnet 5.5, in a claude.ai chat, 24 Oct 2026. Web search and page fetching were used by the assistant.

## What the AI did

| Area | AI contribution |
|---|---|
| Task 1 | Structured the evidence log, drafted the report text and diagrams, wrote `simulator.py` and `time_savings.py`, built the synthetic capstone demo |
| Task 2 | Fetched the official structure and academic features pages, built the credit map and calculator, found and summarised the five job postings, drafted the proposal and report, drafted and verified the five exercises, drafted the capstone |

## What was checked, and how

| Item | Check |
|---|---|
| Simulator | Ran `simulator.py`: 7 of 7 cases pass |
| Time arithmetic | Ran `time_savings.py` and re-derived a worked example by hand |
| Credit map | Totals computed by script from the page's L-T-P-C columns; Semester VI discrepancy flagged |
| Calculator | JavaScript syntax checked and logic tested on two hand-checkable scenarios; **not viewed in a browser by the assistant** |
| AI exercises | Five answers verified by running code or exact arithmetic (`ai-exercises/verify_all.py`) |
| Job postings | Read from search-result excerpts, not full pages. Links need a human check |

## Where the AI's own work needed correction

- While designing the capstone demo the assistant noticed that its duplicate-request rule assumed requests arrive in time order. It fixed `simulator.py` and added test case 3b.
- A first draft of the demo summary described the comparison backwards; it was corrected before saving.
- The assistant first told me I had 3 days left; the deadline was actually the same day. I noticed and corrected the plan.

## What I must still verify myself

As of 24 Oct 2026 these checks are **still open**: I have not opened each job-posting link myself; I could not compare the credit map with my own registration slips (I do not have them with me); I have not viewed the calculator in a browser; and I have not rerun any AI exercise myself. The reports state these gaps as limitations.
