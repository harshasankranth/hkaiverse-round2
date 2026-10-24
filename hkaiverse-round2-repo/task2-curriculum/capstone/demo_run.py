"""Capstone reference demo (SYNTHETIC data only).

Generates 200 invented section-registration requests, runs the Task 1 reference
workflow (allocation by submission time), and compares it with a model of the
hypothesised old behaviour (late forms processed first). It shows what the design
does on invented data. It is NOT evidence that the old process really behaves this way.

Run:  python3 demo_run.py      (writes synthetic_requests.csv and demo_results.md)
"""
import csv, pathlib, random, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "task1-workflow" / "tests"))
import simulator as sim  # Task 1 reference implementation

CAP = {"SEC-A": 40, "SEC-B": 40, "SEC-C": 40, "SEC-D": 40, "AI-ONLY": 40}
RESTRICTED = {"AI-ONLY": {"AI", "AIML"}}
OPEN = ["SEC-A", "SEC-B", "SEC-C", "SEC-D"]
POP = [40, 25, 20, 15]  # SEC-A is the popular section
N = 200


def generate(seed=2026):
    rng = random.Random(seed)
    reqs, paid, fix, label = [], set(), {}, {}

    def prefs_for(branch):
        pool, w = OPEN[:], POP[:]
        if branch in ("AI", "AIML") and rng.random() < 0.2:
            pool.append("AI-ONLY"); w.append(20)
        out = []
        for _ in range(3):
            c = rng.choices(pool, weights=w)[0]
            i = pool.index(c); pool.pop(i); w.pop(i); out.append(c)
        return out

    for i in range(N):
        sid, branch = f"S{i:03d}", rng.choices(["CSE", "AI", "AIML"], weights=[40, 35, 25])[0]
        minute, prefs, tag = rng.randint(0, 480), prefs_for(branch), "normal"
        roll = rng.random()
        if roll < 0.10:
            fix[sid] = prefs; prefs = []; tag = "missing_info"
        elif roll < 0.13 and branch == "CSE":
            prefs = ["AI-ONLY"]; tag = "unauthorized"
        if rng.random() >= 0.03:
            paid.add(sid)
        else:
            tag += "+unpaid"
        reqs.append(sim.Request(f"R{i:03d}", sid, branch, list(prefs), sim.at(minute)))
        label[sid] = tag
        if rng.random() < 0.05:  # duplicate submission later
            reqs.append(sim.Request(f"R{i:03d}d", sid, branch, list(prefs), sim.at(minute + rng.randint(1, 60))))
            label[sid] += "+duplicate"
    return reqs, paid, fix, label


def run_proposed(reqs, paid, fix, shuffle_seed):
    system = sim.RegistrationSystem(CAP, RESTRICTED)
    system.paid = set(paid)
    order = [sim.Request(r.req_id, r.student_id, r.branch, list(r.preferences), r.submitted_at) for r in reqs]
    random.Random(shuffle_seed).shuffle(order)          # arrival order at the desk is arbitrary
    for r in order:
        system.submit(r)
    for r in system.requests:
        if r.status == sim.NEEDS_CORRECTION and r.student_id in fix:
            system.correct(r, fix[r.student_id])
    system.verify_payments(); system.allocate(); system.confirm()
    return system


def legacy_allocate(primaries, batch=25):
    """Model of the hypothesised old behaviour: later batches of forms are processed first."""
    ordered = sorted(primaries, key=lambda r: r.submitted_at)
    batches = [ordered[i:i + batch] for i in range(0, len(ordered), batch)]
    processing = [r for b in reversed(batches) for r in b]
    seats = dict(CAP); got = {}
    for r in processing:
        got[r.student_id] = next((p for p in r.preferences if seats[p] > 0), None)
        if got[r.student_id]:
            seats[got[r.student_id]] -= 1
    return got


def rank(prefs, section):
    return prefs.index(section) + 1 if section in prefs else 4


def main():
    reqs, paid, fix, label = generate()
    with open(HERE / "synthetic_requests.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["req_id", "student_key", "branch", "preferences", "submitted_minute", "paid", "injected_case"])
        for r in reqs:
            w.writerow([r.req_id, r.student_id, r.branch, "|".join(r.preferences),
                        int((r.submitted_at - sim.T0).total_seconds() // 60), r.student_id in paid, label[r.student_id]])

    a = run_proposed(reqs, paid, fix, shuffle_seed=1)
    b = run_proposed(reqs, paid, fix, shuffle_seed=2)
    snap = lambda s: {sid: (r.status, r.section) for sid, r in s.first_request.items()}
    order_independent = snap(a) == snap(b)

    status_counts = {}
    for r in a.requests:
        status_counts[r.status] = status_counts.get(r.status, 0) + 1

    eligible = [r for r in a.first_request.values() if r.status in (sim.REGISTERED, sim.WAITLISTED)]
    legacy = legacy_allocate(eligible)
    prop_rank = {r.student_id: rank(r.preferences, r.section) for r in eligible}
    leg_rank = {r.student_id: rank(r.preferences, legacy[r.student_id]) for r in eligible}
    worse = sum(1 for s in prop_rank if leg_rank[s] > prop_rank[s])
    better = sum(1 for s in prop_rank if leg_rank[s] < prop_rank[s])
    dist = lambda rk: [sum(1 for v in rk.values() if v == k) for k in (1, 2, 3, 4)]

    lines = ["# Capstone demo results (synthetic data)", "",
             f"Invented requests: {len(reqs)} (200 students plus duplicates), seed 2026.", "",
             "| Outcome under the proposed rules | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(status_counts.items())]
    lines += ["", f"Seat assignments identical when requests arrive in two different random orders: **{order_independent}**", "",
              "| Preference received | Proposed (by submission time) | Modelled old behaviour (late forms first) |", "|---|---|---|"]
    pd, ld = dist(prop_rank), dist(leg_rank)
    for i, name in enumerate(["First choice", "Second choice", "Third choice", "No seat (waitlisted)"]):
        lines.append(f"| {name} | {pd[i]} | {ld[i]} |")
    lines += ["", f"Compared with the modelled old behaviour, {worse} students get a better-ranked outcome under submission-time allocation and {better} get a worse-ranked one.",
              "The totals barely change. The rule moves popular seats to whoever submitted first; it does not create seats. Its value is fairness and predictability, not more first choices.",
              "", "This models my **hypothesis** about the cause (processing order). It is not evidence that the real process behaves this way."]
    open(HERE / "demo_results.md", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    assert order_independent


if __name__ == "__main__":
    main()
