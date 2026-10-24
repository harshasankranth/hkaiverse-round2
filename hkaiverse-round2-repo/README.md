# HKAIVERSE Round 2: workflow investigation and curriculum redesign

Student work by Harsha Sankranth (B.Tech CSE (AI), ICFAI Hyderabad, batch 2023 to 2027). **This is a student proposal, not an official ICFAI process or syllabus change.** All data is public, synthetic or my own recollection. No names, student IDs, marks, fees, credentials or private messages are included.

## Reviewed revision

- **Release:** https://github.com/harshasankranth/hkaiverse-round2/releases/tag/v1.0-submission
- **Full commit URL (the commit the release points to):** https://github.com/harshasankranth/hkaiverse-round2/commit/6c80180840881a378f0cd0f8e04a19e428a156cf

The release was tagged first. These two links were then added in a documentation-only commit, so the tagged revision is the preserved one for review.

## Where to look

| What | Where |
|---|---|
| Task 1 report | [`task1-workflow/report.md`](task1-workflow/report.md) |
| Task 1 evidence log (dated, labelled) | [`task1-workflow/evidence-log.md`](task1-workflow/evidence-log.md) |
| Task 1 current and proposed process diagrams | [`task1-workflow/process-diagram.md`](task1-workflow/process-diagram.md) |
| Task 1 test cases and results | [`task1-workflow/tests/`](task1-workflow/tests/) |
| Task 1 time and effort arithmetic | [`task1-workflow/time-savings.md`](task1-workflow/time-savings.md) |
| Task 2 report | [`task2-curriculum/report.md`](task2-curriculum/report.md) |
| Task 2 official baseline and sources | [`task2-curriculum/baseline.md`](task2-curriculum/baseline.md) |
| Task 2 job descriptions (URLs, dates) | [`task2-curriculum/job-descriptions.md`](task2-curriculum/job-descriptions.md) |
| Task 2 five AI-assisted exercises | [`task2-curriculum/ai-exercises.md`](task2-curriculum/ai-exercises.md) |
| Task 2 capstone built from Task 1 | [`task2-curriculum/capstone.md`](task2-curriculum/capstone.md) |
| Task 2 validation (feedback) | [`task2-curriculum/feedback.md`](task2-curriculum/feedback.md) |
| Interactive credit calculator | [`task2-curriculum/calculator/index.html`](task2-curriculum/calculator/index.html) (open the file in a browser) |
| AI-use record | [`AI-USE.md`](AI-USE.md) |
| My contribution | [`CONTRIBUTION.md`](CONTRIBUTION.md) |
| Limitations | [`LIMITATIONS.md`](LIMITATIONS.md) |

## Headline results

**Task 1: semester registration.** Seats appear to be filled in the order forms are processed, not the order they are submitted (my own experience, one student's account; the cause is an unconfirmed hypothesis). I propose a rules-based workflow that allocates by submission time, with statuses, an accountable owner, approval boundaries, an audit record and a fallback. It passes 7 of 7 synthetic cases. Net time saved is estimated at roughly 36 to 83 hours a month on average for 200 students (conservative to base), from assumed inputs, with all arithmetic shown.

**Task 2: curriculum.** Baseline 144 credits (Semesters I to VI plus summer internship) from the public IcfaiTech structure page, which I could not confirm is the version for my batch. Proposal: add three 3-credit courses, update seven courses, move three core courses to elective status. Credits stay balanced at 144 and 23.6% of baseline credits are affected, using a stated definition. Evidence: five dated job postings and five verified AI-assisted exercises.

## Reproduce

```
python3 task1-workflow/tests/simulator.py          # five synthetic cases plus extras
python3 task1-workflow/calc/time_savings.py        # per request, per month, ranges
python3 task2-curriculum/ai-exercises/verify_all.py
python3 task2-curriculum/capstone/demo_run.py      # synthetic capstone demo
python3 task2-curriculum/data/make_courses.py && python3 task2-curriculum/build_calculator.py   # run from task2-curriculum/
```

Run the last two from inside `task2-curriculum/`. Only Python 3 is needed.

## Sources and access dates

Official structure page, academic features page and the five job postings were accessed on **24 Oct 2026**. URLs are in `task2-curriculum/baseline.md` and `task2-curriculum/job-descriptions.md`. The registration notice used in Task 1 is cited but not committed because it lists staff names.
