# Task 2 baseline: B.Tech CSE (Artificial Intelligence), IcfaiTech

This file separates **official curriculum facts** from my own proposal. Nothing here is an official syllabus revision.

## 1. Identity of the programme

| Item | Value | Label |
|---|---|---|
| Campus | The ICFAI Foundation for Higher Education (IFHE), Hyderabad, IcfaiTech | Official |
| Degree and branch | B.Tech, Computer Science and Engineering (Artificial Intelligence) | Official |
| Admission batch | 2023 to 2027 | My own record |
| Curriculum version applying to my batch | **Not yet confirmed** | See section 3 |

## 2. Sources (accessed 24 Oct 2026)

| ID | Source | URL | Used for |
|---|---|---|---|
| R1 | IcfaiTech B.Tech Program Structure | https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure | Course codes, titles, L-T-P-C, semester placement |
| R2 | IcfaiTech Academic Features | https://www.ifheindia.org/icfai-tech-school-hyderabad/academics/icfaitech-academic-features | Choice-based credits, electives from other programmes allowed if prerequisites are met, audit courses, up to two additional electives |
| R3 | Registration notice, A.Y. 2026-27 V Semester (not committed; it lists staff names) | Distributed by the college | Evidence that my batch's Semester VII differs from R1 (section 3) |

**Still needed (regulations).** The brief asks for the applicable regulations. I have R2 only. I did not find the Academic Regulations document on the pages I used, so every regulatory statement in my proposal is conditional.

## 3. Version problem (read this first)

R1 shows the **current public** structure. The brief says the admissions website alone does not establish a batch's syllabus. Evidence that my batch's scheme may differ:

- R1 places Computer Vision (AI307) in Semester VI, and shows Semester VII as Internship / Thesis / Electives.
- R3 (IV Year, Semester VII, 2026-27) lists taught courses with different codes, including Computer Vision (CS305), Cloud Computing (CS307), Generative AI (DS408), Quantum Computing (CS413), Human Computer Interaction (DS401), Professional Ethics (HS206) and Introduction to Entrepreneurship (MG401).

So the proposal below uses R1 as a **declared working baseline**, not as proof of my batch's syllabus. I do not have my registration slips or marksheets with me, so I could not compare the Semester I to VI table with my own records. The only cross-check done is against the Semester VII registration notice, which shows a different structure.

## 4. Credit map from R1 (Semesters I to VI plus summer term)

| Semester | Courses | Credits (my sum of listed courses) |
|---|---|---|
| I | 7 | 21 |
| II | 7 | 22 |
| III | 8 | 24 |
| IV | 8 | 25 |
| Summer term (IP201 Internship 1) | 1 | 5 |
| V | 9 | 24 |
| VI | 8 | 23 |
| **Verified baseline** | **48** | **144** |

The full course-by-course table is `data/courses.json`, built by `data/make_courses.py`, and is viewable in `calculator/index.html`.

By category (credits): Core computing 44, Core AI and data 32, Humanities and skills 18, Mathematics 12, Elective slots 12, Engineering basics 10, Basic sciences 8, Project and internship 8. Slot credits in total, including the Digital Humanities slot, are 15.

## 5. What I could not verify

- **Semester VI total.** R1 states 24 credits for Semester VI, but the listed courses plus one 3-credit Professional Elective add up to 23. I used the course-level sum (23) and flag a 1-credit discrepancy.
- **Elective credits.** R1 prints no credit next to "PE 1", "PE 2", "Elective-I" or "Elective-II". I assumed 3 each, matching the 3-credit electives in R1's elective table. These are **elective alternatives**: I counted each slot once and did not sum the options inside a slot.
- **Semesters VII and VIII.** R1 shows Internship / Research (15), Thesis and Seminar (15) and "Electives, PE/OE (5)" for each semester without saying how they combine. The first two look like alternatives, so I **did not sum them**. They are excluded from the baseline until the Academic Regulations confirm the composition.
- **Programme total.** Because Semesters VII and VIII are unconfirmed, I do not claim a total programme credit figure. The 144-credit baseline covers Semesters I to VI plus the summer term only.
- **Prerequisites.** R1 does not list prerequisites. R2 says electives need prerequisites "if any" but names none. I mark prerequisites in my proposal as my own assumptions.

## 6. Baseline definition used for the 20 to 25% target

Baseline B = 144 credits (Semesters I to VI plus IP201). A change of 20 to 25% therefore means about 29 to 36 credits. The exact share is computed in the calculator and in the proposal report, using this definition:

- **Affected credits = UPDATE credits + credits freed by REDUCE.** (UPDATE keeps credits but changes content; REDUCE removes credits.)
- **ADD credits must equal credits freed by REDUCE**, so the total stays balanced at 144.
- Share = affected credits / 144.

I chose this definition myself. The brief says "roughly 20 to 25%" without defining it, so I state it openly.
