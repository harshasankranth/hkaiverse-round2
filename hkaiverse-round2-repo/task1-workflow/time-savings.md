# Time and effort: per request, per event, per month

All inputs are **assumptions or personal estimates** (evidence log A3, P2). Nothing here is measured. The script is `calc/time_savings.py`; edit any number and re-run it.

## Arithmetic

Per request (one student's registration):

- Old minutes = day minutes + rework share x (rework student min + rework staff min) + staff minutes
- New minutes = student minutes + correction share x correction minutes + staff minutes + correction share x review minutes + support minutes
- Net saved per event = students x (old - new) - setup per event
- Average per month = net per event x 2 events a year / 12 (registration comes in peaks, so a monthly figure is only an average)
- One-off cost = implementation + training. Events to break even = one-off cost / net saved per event

Worked example (Base, 200 students):
- Old = 150 + 0.25 x (45 + 10) + 6 = 169.75 min per request
- New = 15 + 0.10 x 10 + 2 + 0.10 x 10 + 1 = 20.0 min per request
- Net per event = 200 x (169.75 - 20.0) - 120 = 29,830 min (about 497 hours)
- Per month on average = 29,830 x 2 / 12 = 4,972 min (about 83 hours)

"Waited one day" in my account (P6) is elapsed time, not active time, so it is not counted as 1,440 minutes.

## Inputs

| Input | Base | Conservative | Label |
|---|---|---|---|
| Students per event | 150 / 200 / 300 | 150 / 200 / 300 | Estimate (P2), range because volume is uncertain |
| Events per year | 2 | 2 | Assumption |
| Student minutes on the day, old process | 150 | 90 | Assumption |
| Share of requests needing rework, old process | 25% | 15% | Assumption |
| Rework minutes (student / staff) | 45 / 10 | 45 / 10 | Assumption |
| Staff minutes per request, old process | 6 | 4 | Assumption |
| Student minutes, new process | 15 | 25 | Assumption |
| Share needing correction, new process | 10% | 20% | Assumption |
| Correction minutes (student) | 10 | 15 | Assumption |
| Staff minutes per request, new process | 2 | 3 | Assumption |
| Review minutes per exception | 10 | 15 | Assumption |
| Support minutes per request | 1 | 2 | Assumption |
| Setup per event (section lists, slots) | 120 | 240 | Assumption |
| Implementation, one-off | 2,400 (40 h) | 4,800 (80 h) | Assumption |
| Training, one-off | 60 | 120 | Assumption |

## Results

| Scenario | Students | Old min/request | New min/request | Net saved per event (min) | Avg per month (hours) | One-off cost (min) | First-year net (hours) | Events to break even |
|---|---|---|---|---|---|---|---|---|
| Base | 150 | 169.8 | 20.0 | 22,342 | 62 | 2,460 | 704 | 0.11 |
| Base | 200 | 169.8 | 20.0 | 29,830 | 83 | 2,460 | 953 | 0.08 |
| Base | 300 | 169.8 | 20.0 | 44,805 | 124 | 2,460 | 1,452 | 0.05 |
| Conservative | 150 | 102.2 | 36.0 | 9,698 | 27 | 4,920 | 241 | 0.51 |
| Conservative | 200 | 102.2 | 36.0 | 13,010 | 36 | 4,920 | 352 | 0.38 |
| Conservative | 300 | 102.2 | 36.0 | 19,635 | 55 | 4,920 | 572 | 0.25 |

## How to read this

- Across every scenario and volume the estimate stays positive, but every figure rests on assumed minutes. Treat the result as an order of magnitude, not a precise number.
- The result is most sensitive to "student minutes on the day, old process". If real waiting was much shorter, the saving shrinks quickly.
- Implementation effort is a guess at 40 to 80 hours of build time. If the college needed a formal approval or integration, it would be much higher and the break-even point would move.
- The saving mixes student time and staff time. Staff time may matter more to the college than student time; I have not weighted them differently.
