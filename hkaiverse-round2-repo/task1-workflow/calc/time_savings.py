"""Time and effort per request, per event and per month, including rework.

EVERY input is an ASSUMPTION or a personal estimate, not a measured value.
Edit the numbers and re-run:  python3 time_savings.py
Registration happens in peaks (assumed 2 per year), so "per month" is an average.
"""

SCENARIOS = {
    "Base": dict(
        old_day_min=150,         # student minutes on registration day, old process
        rework_share=0.25,       # share of requests needing rework, old process
        rework_student_min=45,   # student minutes per rework
        rework_staff_min=10,     # staff minutes per rework
        old_staff_per=6,         # staff minutes per request, old process
        new_student_min=15,      # student minutes: submit preferences, check status
        correction_share=0.10,   # share needing correction, new process
        correction_student_min=10,
        new_staff_per=2,         # staff minutes per request, new process
        review_min=10,           # staff minutes per exception reviewed
        support_per=1,           # support minutes per request (questions, status help)
        setup_per_event=120,     # staff minutes per event: section lists and slots
        implementation=2400,     # one-off: build form and rules (40 hours)
        training=60,             # one-off: brief the office
    ),
    "Conservative": dict(
        old_day_min=90,
        rework_share=0.15,
        rework_student_min=45,
        rework_staff_min=10,
        old_staff_per=4,
        new_student_min=25,
        correction_share=0.20,
        correction_student_min=15,
        new_staff_per=3,
        review_min=15,
        support_per=2,
        setup_per_event=240,
        implementation=4800,     # 80 hours
        training=120,
    ),
}
VOLUMES = [150, 200, 300]   # students per event: uncertain, so shown as a range
EVENTS_PER_YEAR = 2         # assumption


def per_request(p):
    old = p["old_day_min"] + p["rework_share"] * (p["rework_student_min"] + p["rework_staff_min"]) + p["old_staff_per"]
    new = (p["new_student_min"] + p["correction_share"] * p["correction_student_min"]
           + p["new_staff_per"] + p["correction_share"] * p["review_min"] + p["support_per"])
    return old, new


def main():
    print("| Scenario | Students | Old min/request | New min/request | Net saved per event (min) | Avg per month (hours) | One-off cost (min) | First-year net (hours) | Events to break even |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, p in SCENARIOS.items():
        old, new = per_request(p)
        for n in VOLUMES:
            per_event = n * (old - new) - p["setup_per_event"]
            monthly_h = per_event * EVENTS_PER_YEAR / 12 / 60
            one_off = p["implementation"] + p["training"]
            first_year_h = (per_event * EVENTS_PER_YEAR - one_off) / 60
            breakeven = one_off / per_event
            print(f"| {name} | {n} | {old:.1f} | {new:.1f} | {per_event:,.0f} | {monthly_h:,.0f} | {one_off:,.0f} | {first_year_h:,.0f} | {breakeven:.2f} |")


if __name__ == "__main__":
    main()
