"""Verification for the five AI-assisted exercises (see ../ai-exercises.md).

For each exercise the model's ANSWER was written first (it is reproduced in
ai-exercises.md). This script then checks it independently, by running code or by
exact arithmetic. Run:  python3 verify_all.py
"""
import ipaddress, itertools, random, sqlite3, time
from collections import OrderedDict
from fractions import Fraction

results = []
def record(name, ok, detail):
    results.append((name, ok, detail))
    print(("PASS  " if ok else "FAIL  ") + name + " :: " + detail)

# ---------------------------------------------------------------- Exercise 1
# Model output (ES106 Data Structures): LRU cache
class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.data = OrderedDict()
    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]
    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

class BruteLRU:  # slow, obviously-correct reference: list ordered oldest -> newest
    def __init__(self, capacity):
        self.capacity, self.items = capacity, []
    def get(self, key):
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items.append(self.items.pop(i)); return v
        return -1
    def put(self, key, value):
        for i, (k, _) in enumerate(self.items):
            if k == key:
                self.items.pop(i); break
        self.items.append((key, value))
        if len(self.items) > self.capacity:
            self.items.pop(0)

def ex1():
    # five unit tests (the ones the model supplied)
    c = LRUCache(2); c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1                      # test 1: basic get
    c.put(3, 3); assert c.get(2) == -1        # test 2: evicts least recently used (2)
    c.put(4, 4); assert c.get(1) == -1 and c.get(3) == 3 and c.get(4) == 4   # test 3: get refreshes recency
    c = LRUCache(2); c.put(1, 1); c.put(2, 2); c.put(1, 10); c.put(3, 3)
    assert c.get(1) == 10 and c.get(2) == -1  # test 4: updating an existing key refreshes it
    c = LRUCache(1); c.put(1, 1); c.put(2, 2); assert c.get(1) == -1 and c.get(2) == 2  # test 5: capacity 1
    # randomised comparison against the brute-force reference
    rng = random.Random(7); mismatches = 0; ops = 0
    for cap in (1, 2, 3, 5, 8):
        a, b = LRUCache(cap), BruteLRU(cap)
        for _ in range(4000):
            k = rng.randint(0, 10); ops += 1
            if rng.random() < 0.5:
                v = rng.randint(0, 99); a.put(k, v); b.put(k, v)
            elif a.get(k) != b.get(k):
                mismatches += 1
    # rough O(1) check: 10x more operations should take roughly 10x longer, not 100x
    def timed(n):
        c = LRUCache(1000); t = time.perf_counter()
        for i in range(n):
            c.put(i % 2000, i); c.get((i * 7) % 2000)
        return time.perf_counter() - t
    t1, t2 = timed(20000), timed(200000)
    ratio = t2 / t1
    record("Ex1 LRU cache", mismatches == 0 and ratio < 30,
           f"5 unit tests passed; {ops} random ops, {mismatches} mismatches vs brute force; time ratio for 10x ops = {ratio:.1f}")

# ---------------------------------------------------------------- Exercise 2
def closure(attrs, fds):
    cl = set(attrs); changed = True
    while changed:
        changed = False
        for lhs, rhs in fds:
            if set(lhs) <= cl and not set(rhs) <= cl:
                cl |= set(rhs); changed = True
    return cl

def ex2():
    R = ["StudentID", "CourseID", "StudentName", "CourseTitle", "Instructor", "Grade"]
    fds = [(["StudentID"], ["StudentName"]),
           (["CourseID"], ["CourseTitle", "Instructor"]),
           (["StudentID", "CourseID"], ["Grade"])]
    keys = []
    for r in range(1, len(R) + 1):
        for combo in itertools.combinations(R, r):
            if closure(combo, fds) == set(R) and not any(set(k) < set(combo) for k in keys):
                keys.append(combo)
    key_ok = keys == [("StudentID", "CourseID")]
    # partial dependency check -> not 2NF
    partial = closure(["StudentID"], fds) > {"StudentID"} or closure(["CourseID"], fds) > {"CourseID"}
    # lossless join + query on synthetic data (all invented)
    con = sqlite3.connect(":memory:"); cur = con.cursor()
    cur.execute("CREATE TABLE R(StudentID, CourseID, StudentName, CourseTitle, Instructor, Grade)")
    students = {1: "Asha", 2: "Ben", 3: "Chitra"}   # synthetic
    courses = {"C1": ("Databases", "Inst-A"), "C2": ("Networks", "Inst-B"), "C3": ("AI", "Inst-C")}
    enroll = [(1, "C1", 9), (1, "C2", 8), (2, "C1", 7), (2, "C3", 8), (3, "C2", 10), (3, "C3", 9)]
    for s, c, g in enroll:
        cur.execute("INSERT INTO R VALUES (?,?,?,?,?,?)", (s, c, students[s], courses[c][0], courses[c][1], g))
    cur.execute("CREATE TABLE Student AS SELECT DISTINCT StudentID, StudentName FROM R")
    cur.execute("CREATE TABLE Course AS SELECT DISTINCT CourseID, CourseTitle, Instructor FROM R")
    cur.execute("CREATE TABLE Enrollment AS SELECT StudentID, CourseID, Grade FROM R")
    joined = set(cur.execute("""SELECT e.StudentID, e.CourseID, s.StudentName, c.CourseTitle, c.Instructor, e.Grade
                                FROM Enrollment e JOIN Student s USING(StudentID) JOIN Course c USING(CourseID)""").fetchall())
    original = set(cur.execute("SELECT * FROM R").fetchall())
    lossless = joined == original
    sql = """SELECT s.StudentID, s.StudentName, AVG(e.Grade) AS avg_grade
             FROM Student s JOIN Enrollment e USING(StudentID)
             GROUP BY s.StudentID, s.StudentName HAVING AVG(e.Grade) > 8 ORDER BY s.StudentID"""
    got = [(r[0], round(r[2], 2)) for r in cur.execute(sql).fetchall()]
    expect = []
    for s in sorted(students):
        gs = [g for (ss, _, g) in enroll if ss == s]
        if sum(gs) / len(gs) > 8:
            expect.append((s, round(sum(gs) / len(gs), 2)))
    record("Ex2 DBMS normalisation + SQL", key_ok and partial and lossless and got == expect,
           f"candidate key {keys}; partial dependency found: {partial}; lossless join: {lossless}; query rows {got} match manual {expect}")

# ---------------------------------------------------------------- Exercise 3
def ex3():
    sens, spec, prev = Fraction(95, 100), Fraction(90, 100), Fraction(2, 100)
    p_pos = sens * prev + (1 - spec) * (1 - prev)
    post1 = sens * prev / p_pos
    num2 = sens**2 * prev; den2 = num2 + (1 - spec)**2 * (1 - prev)
    post2 = num2 / den2
    rng = random.Random(11); n = 2_000_000
    pos1 = hit1 = pos2 = hit2 = 0
    for _ in range(n):
        has = rng.random() < 0.02
        t1 = rng.random() < (0.95 if has else 0.10)
        t2 = rng.random() < (0.95 if has else 0.10)
        if t1:
            pos1 += 1; hit1 += has
            if t2:
                pos2 += 1; hit2 += has
    mc1, mc2 = hit1 / pos1, hit2 / pos2
    ok = (post1 == Fraction(19, 117) and post2 == Fraction(361, 557)
          and abs(mc1 - float(post1)) < 0.01 and abs(mc2 - float(post2)) < 0.02)
    record("Ex3 Bayes (probability)", ok,
           f"exact: 19/117={float(post1):.4f}, 361/557={float(post2):.4f}; simulation {mc1:.4f}, {mc2:.4f} ({n:,} trials)")

# ---------------------------------------------------------------- Exercise 4
def ex4():
    parent = ipaddress.ip_network("172.16.40.0/22")
    claimed = [("300 hosts", "172.16.40.0/23", 300), ("120 hosts", "172.16.42.0/25", 120),
               ("50 hosts", "172.16.42.128/26", 50), ("20 hosts", "172.16.42.192/27", 20)]
    nets = [ipaddress.ip_network(c[1]) for c in claimed]
    inside = all(n.subnet_of(parent) for n in nets)
    no_overlap = all(not a.overlaps(b) for a, b in itertools.combinations(nets, 2))
    enough = all(n.num_addresses - 2 >= need for n, (_, _, need) in zip(nets, claimed))
    tight = all((n.num_addresses // 2) - 2 < need for n, (_, _, need) in zip(nets, claimed))  # one bit smaller would not fit
    free = [str(x) for x in ipaddress.collapse_addresses(
        [h for h in itertools.chain.from_iterable(_exclude(parent, nets))])]
    record("Ex4 Subnetting (VLSM)", inside and no_overlap and enough and tight and free == ["172.16.42.224/27", "172.16.43.0/24"],
           f"inside parent: {inside}; no overlap: {no_overlap}; each fits: {enough}; each as small as possible: {tight}; free space {free}")

def _exclude(parent, nets):
    remaining = [parent]
    for n in nets:
        nxt = []
        for r in remaining:
            if n.subnet_of(r):
                nxt.extend(r.address_exclude(n))
            else:
                nxt.append(r)
        remaining = nxt
    return [remaining]

# ---------------------------------------------------------------- Exercise 5
def round_robin(procs, q):
    procs = sorted(procs, key=lambda p: p[1])
    rem = {p[0]: p[2] for p in procs}; arr = {p[0]: p[1] for p in procs}; burst = dict(rem)
    t = 0; queue = []; idx = 0; done = {}; gantt = []
    def admit(upto):
        nonlocal idx
        while idx < len(procs) and procs[idx][1] <= upto:
            queue.append(procs[idx][0]); idx += 1
    admit(0)
    while len(done) < len(procs):
        if not queue:
            t = procs[idx][1]; admit(t); continue
        pid = queue.pop(0); run = min(q, rem[pid])
        gantt.append((pid, t, t + run)); t += run; rem[pid] -= run
        admit(t)                      # arrivals up to and including time t enter first
        if rem[pid] > 0: queue.append(pid)
        else: done[pid] = t
    tat = {p: done[p] - arr[p] for p in done}; wt = {p: tat[p] - burst[p] for p in done}
    return gantt, done, tat, wt

def ex5():
    procs = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 8), ("P4", 3, 6)]
    gantt, ct, tat, wt = round_robin(procs, 4)
    claimed_gantt = [("P1", 0, 4), ("P2", 4, 7), ("P3", 7, 11), ("P4", 11, 15), ("P1", 15, 16), ("P3", 16, 20), ("P4", 20, 22)]
    claimed_ct = {"P1": 16, "P2": 7, "P3": 20, "P4": 22}
    avg_tat, avg_wt = sum(tat.values()) / 4, sum(wt.values()) / 4
    ok = gantt == claimed_gantt and ct == claimed_ct and avg_tat == 14.75 and avg_wt == 9.25
    record("Ex5 Round Robin scheduling", ok,
           f"gantt matches: {gantt == claimed_gantt}; completion {ct}; turnaround {tat}; waiting {wt}; averages {avg_tat}/{avg_wt}")

if __name__ == "__main__":
    for f in (ex1, ex2, ex3, ex4, ex5):
        f()
    print(f"\n{sum(1 for r in results if r[1])}/{len(results)} exercises verified")
