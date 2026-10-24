# Task 1: Semester Registration workflow

## 1. Summary

Students register for sections on a single day across three physical locations. In my own experience (P5 to P7), a request I submitted online was processed after later-arriving forms, my preferred section had filled by then, and I learned this a day later. This report maps the current process, estimates the problem's scale, proposes a rules-based process that allocates seats by **submission time**, and tests it on five synthetic cases.

## 2. How I found the process, sample size and access limits

- **Sources:** (S1) the official registration notice and (S2) my own registration experience. Details and labels are in `evidence-log.md`.
- **Sample size:** one document and one person's account (me). **No counts or timings were measured.** Every number in this report is an estimate or assumption.
- **Conversation with a process user:** none.
- **Permission and access:** I did not request access to the registration office or ask for permission to study the process. I used a notice distributed to students and my own experience only.
- **Fieldwork boundary:** no names, student IDs, marks, fees, signatures, credentials or private messages are collected. The notice is cited, not committed, because it lists staff names. Only synthetic data is used.

**Hypothetical walkthrough (NOT an observation).** Because I have no observed walkthrough, here is a labelled illustration of a typical day: a student collects the accounts slip, pays online if needed, queues at the verification desk, queues again at the registration desk, and finds the preferred section full. This is reasoning from the notice and my own case, not something I watched.

## 3. Current process

Diagram: `process-diagram.md`.

| Step | Who or where | Label |
|---|---|---|
| Collect accounts slip | Accounts | Observed (documented) |
| Pay on the online portal if not yet paid | Student | Observed (documented) |
| Payment verification | Auditorium; Transport desk in G-19 | Observed (documented) |
| Semester registration and form collection | G-23 | Observed (documented) |

Handoffs: student, then accounts, then verification, then registration desk. Approvals: verification and registration desks. Exceptions: the notice shows none (D6) and states no rule for how seats are allotted (D7).

## 4. The problem and its scale

**Problem.** Seats appear to be filled in processing order, not submission order (assumptions A1 and A2). A student who submits on time can lose a seat to later forms that happen to be processed first, and finds out only after waiting.

**Scale (estimates only).**
- About 200 students per registration event (P2); range 150 to 300 used below. Assumed 2 events a year.
- Per request under Base assumptions: about 170 minutes in the old process, including rework (25% of requests, 55 minutes each).
- Per event: 200 requests x 169.75 = about 33,950 minutes. Averaged over the year (2 events), roughly 5,660 minutes, or 94 hours, a month.
- How many students actually lost a preferred section is **unknown**. I only know my own case (P7).

Full arithmetic and ranges: `time-savings.md`.

## 5. Proposed process

Diagram: `process-diagram.md`.

**Inputs:** synthetic student key, branch, ranked section preferences (2 to 3), submission timestamp, payment status.

**Statuses**

| Status | Meaning |
|---|---|
| SUBMITTED | Complete, eligible request received |
| NEEDS_CORRECTION | Missing information or no payment found; original timestamp kept |
| DUPLICATE_MERGED | Second submission merged into the first |
| REJECTED | Not eligible for any requested section; logged with reason |
| PAYMENT_PENDING | Payment check could not run; will retry |
| PAYMENT_VERIFIED | Payment confirmed |
| ALLOCATED | Seat assigned by submission time |
| WAITLISTED | All preferred sections full |
| REGISTERED | Confirmed by the registration office |

**Accountable owner:** the registration office, as a role, not a named person. It owns every move from ALLOCATED to REGISTERED and every exception.

**Approval boundary**
- Automatic (rules): validation, duplicate merge, rejection of ineligible requests, allocation by submission time.
- Human decision: section changes after allocation, capacity overrides, waitlist promotion, appeals against a rejection, use of the manual fallback, and any case outside the five below.
- Results are published before a student has to visit any desk.

**Audit record.** An append-only log with one row per status change: request key (synthetic), timestamp, old status, new status, actor role (system or registration office), reason code, and rule version. It holds no names, IDs, fees or messages. Any allocation can be explained from this log.

**Fallback.** If the online step or payment check fails, the manual desk accepts the request and records the **original submission time**, so nobody loses priority because a system was down.

## 6. Rules versus AI

Ordinary rules and software are enough here. Validation, duplicate detection, eligibility by branch, ordering by timestamp and seat counts are deterministic, and fairness requires that any student can see why they got a section. I would **not** use AI for allocation, because an unexplainable decision is hard to audit or appeal. AI might add small value only in drafting plain-language notices or flagging unusual free-text requests for a human, and I have not tested that. It is not part of the core design.

## 7. Five synthetic cases

Code: `tests/simulator.py`. Output: `tests/test-results.md`. All data is invented.

| Case | Expected result and recovery | Who decides | Result |
|---|---|---|---|
| Normal | REGISTERED in first preference | System allocates; registration office confirms | PASS |
| Missing information | NEEDS_CORRECTION, then REGISTERED after fix, timestamp unchanged | Student corrects; no staff decision needed | PASS |
| Duplicate | Second request merged, only one seat used | System merges; office reviews only if the two requests differ | PASS |
| Unauthorized | REJECTED with reason, no seat used | System rejects by rule; office decides any appeal | PASS |
| Failed step | PAYMENT_PENDING during outage; after recovery the earlier submitter gets the seat | System retries; office decides when to use the manual fallback | PASS |

Two extra checks follow. Case 3b (a duplicate whose earlier copy reaches the desk later) was added after I noticed, while designing the Task 2 capstone demo, that my duplicate rule assumed requests arrive in time order. A sixth illustration shows the hypothesised root cause: when the latest forms are processed first they take the seats; under the proposed rule the earliest submitters do.

**What these tests show and do not show.** They show the rules behave as designed on cases I chose. They do not show the office would adopt them, that students would use the form, or that my guess about the cause (A2) is right. The simulator also keeps only the first of two duplicate requests; a student who wants to change preferences would need the office.

## 8. Net time saved

Per request, per event and per month, with rework, review, support and implementation effort: `time-savings.md`.

- Base, 200 students: about 29,830 minutes net per event, an average of roughly 83 hours a month, and a one-off cost of 2,460 minutes that is recovered within the first event.
- Conservative, 200 students: about 13,010 minutes net per event, an average of roughly 36 hours a month, and a one-off cost of 4,920 minutes, recovered in under one event.
- Across the 150 to 300 student range, first-year net saving is about 240 to 1,450 hours.

All of this rests on assumed minutes. Treat it as an order of magnitude.

## 9. Risks, unknowns and what would change my mind

**Risks**
- Students may not use an online form, or may gather at the desk anyway.
- Seats may be allotted by rules I do not know (for example merit or programme priority), so first come, first served may not be allowed.
- An online form needs hosting and support the college may not have.
- Friends-in-the-same-section requests are not handled fairly by a simple timestamp rule.

**Unknowns**
- The real allocation rule, section capacities, volumes and waiting times.
- Whether others had the same experience as me.

**An observation that would make me abandon or change the design.** If the registration office confirms that seats were already allocated by submission time and the delay came from the online submission not reaching them (or from something else), then the timestamp rule would not fix my case, and I would redirect the design to delivery and notification of submissions. If peers report no seat problems, I would treat my case as an outlier and shrink the problem statement.

## 10. Personal contribution

- I chose the workflow and supplied the problem from my own registration experience (P1 to P7).
- I supplied the original idea: collect section preferences first, then allocate, then give each section a time slot.

## 11. AI use in this task

- Tool: Claude (Anthropic), Sonnet 5.5, 24 Oct 2026.
- Used for: structuring the evidence log, drafting diagrams and report text, and writing the simulator and calculator.
- Verification: I ran `tests/simulator.py` (7 of 7 cases pass) and `calc/time_savings.py`, and checked the worked example by hand. The time inputs are assumptions I have not measured. The AI assistant compared the uploaded notice with entries D1 to D7; I have not rechecked it myself.

## 12. Limitations

- The problem rests mostly on one student's account (mine).
- The cause (processing order) is a hypothesis not confirmed with the office.
- The 200-student figure and every time input are estimates; no counts were measured.
- Any permission, interview or peer feedback appears only where I have written it above.
- Section capacity is assumed from the "75" in the notice (D3a).
- Implementation effort (40 to 80 hours) is a guess.
- This is student work, not an official proposal, and I do not promise implementation.
