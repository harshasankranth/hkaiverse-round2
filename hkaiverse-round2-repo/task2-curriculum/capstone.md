# Proposed capstone: Request Workflow Desk

A student proposal for turning my Task 1 work (semester-registration workflow) into a lab. It is not an official course design.

## Summary

Student teams study a small, ordinary process (a real one with permission, or a clearly labelled hypothetical one), design a safer workflow for it, build the rules in code, test it on invented cases and measure what it saves. The Task 1 reference solution (`../task1-workflow/`) is the model answer.

## Host course and prerequisites

| Item | Proposal |
|---|---|
| Host course | **SP301 Special Project**, 3 credits, Semester VI (marked UPDATE) |
| Co-requisite | Agentic Systems, Evaluation and Observability (proposed ADD, Semester VI) |
| Prerequisite for the optional AI step | LLM Application Engineering (proposed ADD, Semester V) |
| Knowledge assumed | Python (ES105, ES201), databases (AI202), web and API basics (AI208), testing and Git (ES202), probability for ranges (BS105) |
| If new courses are not approved | Run it inside SP301 alone as a rules-only project; the AI step becomes optional and uses a hosted model API at the team's own risk |

## Learning outcomes

By the end, a student can:
1. Map a process from evidence and label each claim as observed, estimated or assumed.
2. Specify statuses, an accountable owner, approval boundaries, an audit record and a fallback.
3. Implement the workflow with ordinary rules and explain whether any AI step adds value.
4. Test five synthetic cases (normal, missing information, duplicate, unauthorized, failed step) and explain recovery and who decides.
5. Measure net time saved, including review, support and implementation effort, with a range.

## Synthetic dataset

- `capstone/demo_run.py` generates 208 invented registration requests (200 students plus duplicates) with seed 2026 and writes `synthetic_requests.csv`.
- Each row carries an injected-case label (normal, missing information, duplicate, unauthorized, unpaid) so tests have an expected answer.
- It contains no names, IDs, marks, fees or messages. Teams generate their own file for their own process.

## Milestones (about 12 weeks)

| Weeks | Milestone | Deliverable |
|---|---|---|
| 1 to 2 | M1 Understand | Evidence log with labels, process map, problem and scale estimate |
| 3 to 4 | M2 Design | Statuses, owner, approval boundary, audit record, fallback; instructor review |
| 5 to 7 | M3 Build and test | Rules in code; five synthetic cases plus an out-of-order duplicate; results table |
| 8 to 9 | M4 Optional AI step | Evaluation set, comparison against plain rules, human approval gate |
| 10 to 11 | M5 Measure | Net time saved per request and per month, with a range |
| 12 | M6 Defend | Demo and short viva; abandon-trigger statement |

## Acceptance tests (pass or fail)

| ID | Test |
|---|---|
| A1 | The five synthetic cases and the out-of-order duplicate give the expected statuses |
| A2 | **Approval control:** no automatic rule and no AI step can move a request to its final state; items needing a human stay pending until a recorded human decision |
| A3 | **Failure recovery:** with a simulated outage, requests wait in a pending status, retry works, and the manual fallback keeps the original submission time |
| A4 | Arrival order does not change who gets a seat (shuffle test) |
| A5 | Every status change is in the audit log with time, actor role and reason code, and the log holds no personal data |
| A6 | **Measured value:** a calculation with a stated range, including review, support and implementation effort |
| A7 | The report labels evidence honestly and states limitations and one observation that would change the design |

## Reference results from the demo

`capstone/demo_results.md` (invented data):
- Seat assignments were identical when requests arrived in two different random orders (A4 passes).
- Under submission-time allocation 130 students got their first choice, against 126 in a model of the old behaviour where late forms are processed first. Totals barely change.
- 62 students got a better-ranked outcome and 58 a worse-ranked one, so the rule **moves** popular seats to earlier submitters; it does not create seats.

This is a useful lesson for students: the value of the design is fairness and predictability, not more first choices. It also models my **hypothesis** about the cause, so it is not evidence about the real process.

## Suggested assessment weights (my proposal)

Process understanding and evidence 20%, design 20%, tests and recovery 25%, measured value 20%, honesty and documentation 15%.

## Risks

- Real processes need permission and can contain personal data, so the hypothetical option and synthetic data are the default.
- Supervision time is unknown; I have not asked faculty.
- Six practical hours a week (the 0-0-6 pattern of SP301 in the structure page) is an assumption for a project of this size.
