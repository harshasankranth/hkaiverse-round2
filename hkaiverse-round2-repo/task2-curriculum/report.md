# Task 2: Audit and redesign of my curriculum

**Question.** What should the B.Tech CSE (AI) programme keep, update, reduce or add to prepare graduates for applied GenAI engineering work in 2030?

**This is a student proposal, not an official ICFAI syllabus revision.** Official facts and my proposal are kept apart: official facts are in `baseline.md` and marked "official"; everything in sections 4 to 7 is mine.

## 1. Summary

- **Baseline:** 144 credits (Semesters I to VI plus the summer internship), 48 courses, from the public IcfaiTech structure page. That page may not match my 2023-batch version (see section 2).
- **Proposal:** add three 3-credit courses (LLM application engineering; agentic systems, evaluation and observability; deploying AI services), update seven existing courses, and move three core courses (Blockchain, Soft Computing, Big Data Systems) to elective status.
- **Size:** 9 credits freed and 9 added, so the total stays **144**. Affected credits = 25 (updated) + 9 (freed) = **34, which is 23.6%** of the baseline. Each semester's credit total is unchanged.
- **Evidence:** five dated job postings and a check of five subjects with AI (all five answers verified, no errors found).
- **Biggest weakness:** I judged existing courses from titles and credits only, not from syllabus contents or assessments, and four of the five job postings ask for 3 or more years of experience.

## 2. Starting point

| Item | Value |
|---|---|
| Campus, degree, branch | IFHE Hyderabad, IcfaiTech, B.Tech CSE (Artificial Intelligence) |
| Admission batch | 2023 to 2027 (my record) |
| Curriculum source | R1: public programme-structure page, accessed 24 Oct 2026 |
| Version confirmed for my batch | **No.** The registration notice for my Semester VII lists courses and codes that differ from R1 (see `baseline.md`, section 3) |
| Regulations | R2 (academic features page) only; the full Academic Regulations were not found. |

Credits by semester (my sum of the listed courses): I 21, II 22, III 24, IV 25, summer 5, V 24, VI 23. Total 144. Semesters VII and VIII are excluded because the page does not say how the internship, thesis and elective options combine, and I do not add mutually exclusive options. Elective slots are counted once at 3 credits each (assumption). Full table: `appendix-course-map.md`.

## 3. Evidence: job postings

Five dated postings (6 Aug to 21 Sep 2026) for GenAI and LLM engineer roles are summarised in `job-descriptions.md`, with URLs and access dates. The recurring requirements are: Python and REST services (4 of 5 postings), building LLM applications with retrieval and prompts (all 5), agent orchestration (3), evaluation and observability (3), containers, CI/CD and monitoring (3), databases and vector stores (4), fine-tuning (2), and engineering hygiene such as tests and runbooks (3).

**Caveat:** only one posting is near entry level; the rest ask for 3 to 13 years. They show where skills are heading, not what a fresher is hired for today.

## 4. Proposal: KEEP, UPDATE, REDUCE, ADD

| Status | Courses | Credits |
|---|---|---|
| ADD (new) | LLM Application Engineering (Sem V); Agentic Systems, Evaluation and Observability (Sem VI); Deploying AI Services (Sem IV) | +9 |
| UPDATE (same credits, new content) | ES202, AI208, AI202, AI203, AI306, AI310, SP301 | 25 |
| REDUCE (core to elective) | AI303 Blockchain Technology, AI211 Soft Computing, AI308 Big Data Systems | −9 |
| KEEP | Everything else | 110 |

### The 12 reasons

| # | Change | Courses | Evidence | Absent, or present but needs practice? |
|---|---|---|---|---|
| 1 | ADD LLM Application Engineering (3 cr, Sem V) | New | J1, J2, J4, J5 (and J3): retrieval-augmented generation, prompts, embeddings, vector stores | **Absent** as a course; AI306 NLP touches language models but is in Sem VI. A Generative AI course appears in my batch's Semester VII notice (R3), which is later than the skill is needed |
| 2 | ADD Agentic Systems, Evaluation and Observability (3 cr, Sem VI) | New | J1, J3, J4: agent workflows, tool calling, evaluation sets, tracing, cost and latency | **Absent** |
| 3 | ADD Deploying AI Services (3 cr, Sem IV) | New | J2, J3, J4: Docker, CI/CD, cloud, logging and monitoring | **Absent**; AI205 gives Linux basics only |
| 4 | UPDATE ES202 Industry Coding Practices | ES202 | J2, J3, J4: Git workflow, tests, documentation and runbooks | **Present, needs more practice** (title only; syllabus not seen) |
| 5 | UPDATE AI208 Web Enabled Technologies | AI208 | J1, J2, J3, J4: REST and async API services | **Present, needs more practice**; the WEB 3.0 emphasis may not cover Python API services |
| 6 | UPDATE AI202 Database Management Systems | AI202 | J1, J2, J4, J5: SQL tuning, caching, vector search | **Present**; vector stores and caching absent |
| 7 | UPDATE AI203 Artificial Intelligence and REDUCE AI211 Soft Computing | AI203, AI211 | J1, J3: agents and tool use; none of the five mention fuzzy or evolutionary methods | AI203 present; search and optimisation essentials move into it. Evidence on AI211 is weak |
| 8 | UPDATE AI306 NLP and AI310 Deep Learning | AI306, AI310 | J2, J4, J5: embeddings, chunking, diagnosing retrieval failures; J3, J4: LoRA fine-tuning and serving | **Present**; depth unknown |
| 9 | UPDATE SP301 Special Project (capstone host) | SP301 | J3, J4: end-to-end ownership, tests, runbooks, evaluation records | **Present**; becomes the Task 1 capstone (`capstone.md`) |
| 10 | REDUCE AI303 Blockchain Technology | AI303 | None of the five mention it | Not called obsolete; kept as an elective. Evidence is limited to one job family |
| 11 | REDUCE AI308 Big Data Systems | AI308 | Postings stress vector stores, caching and event-driven services more than batch big-data stacks | Content remains in the AI406 to AI410 big-data electives on R1 |
| 12 | KEEP foundations | BS105, ES105, ES106, AI204, AI304 and others | J4 asks for strong statistics and model evaluation; all postings assume programming | Present and essential |

The three reductions are explained in reasons 7 (Soft Computing), 10 (Blockchain) and 11 (Big Data Systems). I kept foundations (reason 12) and did not touch first-year courses, which are common across branches.

### Credits by semester

| Semester | Current | Freed | Added | Proposed | Updated credits |
|---|---|---|---|---|---|
| I | 21 | 0 | 0 | 21 | 0 |
| II | 22 | 0 | 0 | 22 | 0 |
| III | 24 | 0 | 0 | 24 | 7 |
| IV | 25 | 3 | 3 | 25 | 8 |
| Summer | 5 | 0 | 0 | 5 | 0 |
| V | 24 | 3 | 3 | 24 | 0 |
| VI | 23 | 3 | 3 | 23 | 10 |
| **Total** | **144** | **9** | **9** | **144** | **25** |

**Definition of the 20 to 25% share (mine):** affected credits = UPDATE credits + credits freed by REDUCE = 25 + 9 = 34; 34 / 144 = **23.6%**. If a reader counts only credits that move (9), the figure is 6.3%. I state both so the choice is visible. The interactive calculator (`calculator/index.html`) recomputes all of this and lets you try other scenarios.

### Prerequisites (my assumptions)

- LLM Application Engineering: ES105, ES201, AI202, AI203; AI304 Machine Learning taken together with it.
- Agentic Systems, Evaluation and Observability: LLM Application Engineering; SP301 taken together.
- Deploying AI Services: ES202 and AI205 (taken together).

### Regulatory conditions and feasible alternatives

- Removing or demoting a core course, and adding core courses, normally needs approval by the university's academic bodies. I have not seen the Academic Regulations, so **all REDUCE and ADD changes are conditional**.
- **Feasible alternative if core changes are refused:** offer the three new courses as professional electives using the elective slots (Digital Humanities, Elective-I, PE 2, Elective-II, PE 1: 15 credits in total) and leave the three reduced courses as core. The structure page also says students may take electives from other programmes if prerequisites are met and up to two additional electives (R2).
- Updates to course content are the least restricted change, but they still need syllabus approval.

## 5. AI-assisted exercises

Five subjects, one exercise each (`ai-exercises.md`): Data Structures, DBMS, Probability and Statistics, Computer Networks, Operating Systems. All five answers were verified by running code or exact arithmetic (`ai-exercises/verify_all.py`), and **no errors were found**. The verification was done by the same AI assistant, so a human recheck remains.

**Implication.** Well-defined textbook problems can be answered correctly without understanding, so assessment should weigh explaining assumptions, verifying outputs and open-ended project work, which is what the new courses and the capstone do. This is a small sample of easy problems.

## 6. Task 1 turned into a capstone

`capstone.md`: host course SP301 Special Project, prerequisites, five learning outcomes, a synthetic dataset, six milestones and seven acceptance tests covering approval control, failure recovery and measured value. A demo (`capstone/demo_run.py`) on invented data shows the rules are order-independent and that submission-time allocation **moves** seats between students rather than creating them.

## 7. Validation and what would change my mind

- **Faculty or graduate feedback:** none obtained (`feedback.md`). I could not reach anyone in time.
- **What changed my mind while drafting.** I first considered also reducing AI301 Predictive Analytics and first-year foundation courses (Engineering Graphics, Digital Fabrication). I dropped both: J4 asks for strong statistics and model evaluation, and first-year courses are common across branches, so one branch's proposal cannot change them.
- **My strongest claim:** the Semester I to VI structure has no dedicated course on LLM application engineering, evaluation and deployment. **Evidence that would disprove it:** the real 2023-batch syllabi for AI306, AI310, AI304 or the Semester VII Generative AI course already teaching retrieval, evaluation and deployment with hands-on assessment.
- **Evidence that would shrink the proposal:** postings aimed at graduates (not 3 to 13 years of experience) that ask for different skills, or employers who still want blockchain or big-data stacks.

## 8. Limitations

- The baseline is the current public structure, not confirmed for my batch.
- Existing courses were judged from titles and credits, not syllabi, assessments or depth.
- Five postings from one board, aimed at experienced engineers, are a small and skewed sample. I read excerpts, not full pages.
- Elective credits (3 each) and the Semester VI total (23 versus the page's 24) are unresolved.
- Semesters VII and VIII are not in the baseline.
- No faculty or graduate feedback.
- The 20 to 25% share depends on my own definition.
- The AI exercises were drafted and verified by the AI assistant; they are not an independent human check.

## Appendices

- A: `appendix-course-map.md` (full course map, current versus proposed)
- B: `job-descriptions.md`
- C: `ai-exercises.md`
- D: `calculator/index.html`, `data/`
