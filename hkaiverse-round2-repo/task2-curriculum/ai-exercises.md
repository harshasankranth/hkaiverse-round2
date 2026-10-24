# AI-assisted exercises: five subjects

**Model and date:** Claude (Anthropic), Sonnet 5.5, 24 Oct 2026, in a claude.ai chat.
**Authorization and safety:** every task is a generic textbook-style problem with invented data. No confidential or college material is used.

**How this was done (read this).**
1. I (the student) did not type these prompts fresh. They were drafted by the same AI assistant that helped build this repo, for subjects in my programme. I have not rerun any exercise myself.
2. For each exercise the model's answer was written **first**. Then `ai-exercises/verify_all.py` checked it independently, by running code or exact arithmetic. Output saved in `ai-exercises/verification-output.txt`.
3. The verification was also written by the AI assistant, so it is not an independent human check. Human checking that remains is listed under each exercise.
4. **Errors found: none.** All five answers matched. I did not invent an error. The value of the exercise is the checking method, not a corrected mistake.

---

## 1. Data Structures (ES106): LRU cache

**Prompt.** "Write a Python class LRUCache(capacity) with get(key) returning -1 when the key is missing and put(key, value). Both operations must be O(1) on average and evict the least recently used item when full. Add five unit tests."

**Output (summary).** A class built on `collections.OrderedDict`. `get` moves a found key to the end; `put` inserts or updates the key, moves it to the end, and removes the oldest item if the size exceeds the capacity. Five tests: basic get, eviction of the least recently used key, `get` refreshing recency, updating an existing key, capacity 1. The code is the `LRUCache` class in `ai-exercises/verify_all.py`.

**Verification.** Ran the five tests; compared the class against a slow list-based reference on 20,000 random operations across capacities 1, 2, 3, 5 and 8; timed 10 times more operations to check the cost grows about 10 times, not 100 times.
**Result.** All five tests passed, 0 mismatches, time ratio 10.2.
**What the model did.** Chose a sensible structure, wrote the code and tests.
**Human checking that remains.** Whether the tests cover thread safety (they do not), and whether the course expects a hand-built linked-list version.

## 2. Database Management Systems (AI202): normalisation and SQL

**Prompt.** "Relation R(StudentID, CourseID, StudentName, CourseTitle, Instructor, Grade) has these dependencies: StudentID determines StudentName; CourseID determines CourseTitle and Instructor; (StudentID, CourseID) determines Grade. Find the candidate key and the normal form, decompose to 3NF, and write SQL for students whose average grade is above 8."

**Output (summary).** Candidate key (StudentID, CourseID). StudentName depends on part of the key, so R is in 1NF but not 2NF. Decomposition: Student(StudentID, StudentName), Course(CourseID, CourseTitle, Instructor), Enrollment(StudentID, CourseID, Grade). Each dependency is kept, so the result is dependency-preserving, and each table's determinant is its key, so it is also in BCNF. SQL: join Student and Enrollment, GROUP BY student, HAVING AVG(Grade) > 8.

**Verification.** Computed attribute closures in Python to confirm the only candidate key; confirmed a partial dependency exists; loaded invented rows into SQLite, decomposed, rejoined and compared with the original; ran the SQL and compared with a hand computation.
**Result.** Key confirmed; lossless join true on the invented rows; query returned students 1 and 3 with averages 8.5 and 9.5, matching the manual calculation. The BCNF and dependency-preservation claims were checked by reasoning only, not by the script.
**What the model did.** Applied the normal-form rules and wrote the query.
**Human checking that remains.** Whether my course's notation and the exam marking scheme expect the same steps; whether real grades could be missing (NULLs).

## 3. Probability and Statistics (BS105): Bayes' rule

**Prompt.** "A test has 95% sensitivity and 90% specificity, and the condition affects 2% of people. What is the chance someone has the condition given a positive result? What if two independent tests are both positive? State your assumptions."

**Output (summary).** P(positive) = 0.95 x 0.02 + 0.10 x 0.98 = 0.117, so the chance is 0.019 / 0.117, about 16.2%. For two positives, assuming the tests are independent given the person's condition: 0.0180 / 0.0279, about 64.8%.

**Verification.** Exact fractions (19/117 and 361/557) and a 2,000,000-trial simulation.
**Result.** Exact values 0.1624 and 0.6481; simulation 0.1620 and 0.6460.
**What the model did.** Set up Bayes' rule and stated the independence assumption.
**Human checking that remains.** Whether independence given the condition is realistic for a real test, because repeated tests often share errors.

## 4. Computer Networks (AI302): subnetting with VLSM

**Prompt.** "From 172.16.40.0/22, allocate subnets for 300, 120, 50 and 20 hosts using VLSM, largest first. Give network address and mask for each and say what space is left."

**Output (summary).** 300 hosts: 172.16.40.0/23. 120 hosts: 172.16.42.0/25. 50 hosts: 172.16.42.128/26. 20 hosts: 172.16.42.192/27. Left over: 172.16.42.224/27 and 172.16.43.0/24.

**Verification.** Python `ipaddress`: every subnet lies inside the /22, none overlap, each holds the required hosts, each is the smallest possible size, and the free space matches.
**Result.** All checks true.
**What the model did.** Sorted by size, chose masks and placed blocks without overlap.
**Human checking that remains.** Whether the course counts network and broadcast addresses the same way, and whether growth space is expected.

## 5. Operating Systems (AI205): Round Robin scheduling

**Prompt.** "Processes P1 (arrival 0, burst 5), P2 (1, 3), P3 (2, 8), P4 (3, 6). Round Robin, quantum 4. Give the Gantt chart, completion, turnaround and waiting times, and the averages. State your queue convention."

**Output (summary).** Gantt: P1 0-4, P2 4-7, P3 7-11, P4 11-15, P1 15-16, P3 16-20, P4 20-22. Completion: P1 16, P2 7, P3 20, P4 22. Turnaround 16, 6, 18, 19 (average 14.75). Waiting 11, 3, 10, 13 (average 9.25). Convention: processes that arrive during a time slice join the queue before the preempted process.

**Verification.** Wrote a Round Robin simulator using the same convention and compared the Gantt chart, times and averages.
**Result.** Everything matched. In this data set no process arrives at the exact moment another is preempted, so the other common convention gives the same answer.
**What the model did.** Simulated the schedule by hand and stated the convention.
**Human checking that remains.** Whether the course uses a different convention, and whether context-switch time is included.

---

## Summary

| Subject | Task | Verified by | Result |
|---|---|---|---|
| Data Structures (ES106) | LRU cache | Tests, random comparison, timing | Pass |
| DBMS (AI202) | Normalisation and SQL | Closure computation, SQLite | Pass |
| Probability and Statistics (BS105) | Bayes' rule | Exact fractions, simulation | Pass |
| Computer Networks (AI302) | VLSM subnetting | `ipaddress` checks | Pass |
| Operating Systems (AI205) | Round Robin | Independent simulator | Pass |

**What this tells me for the curriculum.** The model handled these well-defined exercises correctly, so assessments that only ask for such answers can be completed without understanding. That supports moving assessment weight toward explaining assumptions, verifying outputs and working on open-ended projects, which is what the proposed ADD courses and the capstone do. This is one small sample on easy textbook problems and does not show how the model would do on harder or ambiguous tasks.
