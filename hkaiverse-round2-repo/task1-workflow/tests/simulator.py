"""Process simulator for the PROPOSED semester-registration workflow.

All data here is SYNTHETIC. No real students, IDs, marks or fees are used.

Run:   python3 simulator.py        (prints a Markdown results table)
Exit code is non-zero if any case does not behave as expected.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import sys

T0 = datetime(2026, 1, 1, 9, 0)  # synthetic clock, not a real date


def at(minutes):
    return T0 + timedelta(minutes=minutes)


# Statuses
SUBMITTED = "SUBMITTED"
NEEDS_CORRECTION = "NEEDS_CORRECTION"
DUPLICATE_MERGED = "DUPLICATE_MERGED"
REJECTED = "REJECTED"
PAYMENT_PENDING = "PAYMENT_PENDING"
PAYMENT_VERIFIED = "PAYMENT_VERIFIED"
ALLOCATED = "ALLOCATED"
WAITLISTED = "WAITLISTED"
REGISTERED = "REGISTERED"


@dataclass
class Request:
    req_id: str
    student_id: str  # synthetic, e.g. S001
    branch: str
    preferences: list
    submitted_at: datetime
    status: str = SUBMITTED
    section: str = ""
    notes: list = field(default_factory=list)

    def note(self, text):
        self.notes.append(text)


class RegistrationSystem:
    def __init__(self, capacity, restricted=None):
        self.seats_left = dict(capacity)
        self.restricted = restricted or {}  # section -> set of allowed branches
        self.requests = []
        self.first_request = {}
        self.payment_service_up = True
        self.paid = set()  # synthetic student ids with verified payment

    # ---- intake -------------------------------------------------------
    def _eligible(self, branch, section):
        if section not in self.seats_left:
            return False
        return section not in self.restricted or branch in self.restricted[section]

    def _validate(self, req):
        if not req.preferences:
            req.status = NEEDS_CORRECTION
            req.note("No section preferences; student asked to resubmit; original timestamp kept")
            return
        allowed = [p for p in req.preferences if self._eligible(req.branch, p)]
        if not allowed:
            req.status = REJECTED
            req.note("No eligible section for this branch; request logged")
            return
        if len(allowed) < len(req.preferences):
            req.note("Ineligible preferences removed")
        req.preferences = allowed
        req.status = SUBMITTED

    def submit(self, req):
        self.requests.append(req)
        if req.student_id in self.first_request:
            first = self.first_request[req.student_id]
            if req.submitted_at < first.submitted_at and first.status in (SUBMITTED, NEEDS_CORRECTION):
                # The EARLIER submission arrived later at the desk: it becomes the main request.
                first.status = DUPLICATE_MERGED
                first.note(f"Merged into {req.req_id}; earliest timestamp kept")
                self.first_request[req.student_id] = req
                self._validate(req)
                return req
            req.status = DUPLICATE_MERGED
            req.note(f"Merged into {first.req_id}; earliest timestamp kept")
            return req
        self.first_request[req.student_id] = req
        self._validate(req)
        return req

    def correct(self, req, preferences):
        """Student fixes a request. The ORIGINAL submitted_at is kept."""
        if req.status != NEEDS_CORRECTION:
            return
        req.preferences = preferences
        self._validate(req)
        req.note("Corrected by student; original timestamp kept")

    # ---- processing ---------------------------------------------------
    def verify_payments(self):
        for r in self.requests:
            if r.status in (SUBMITTED, PAYMENT_PENDING):
                if not self.payment_service_up:
                    r.status = PAYMENT_PENDING
                    r.note("Payment service down; retry later; manual desk fallback available")
                elif r.student_id in self.paid:
                    r.status = PAYMENT_VERIFIED
                else:
                    r.status = NEEDS_CORRECTION
                    r.note("No payment found; student notified")

    def allocate(self):
        """Seats go by SUBMISSION time, never by processing order."""
        ready = sorted(
            (r for r in self.requests if r.status == PAYMENT_VERIFIED),
            key=lambda r: (r.submitted_at, r.req_id),
        )
        for r in ready:
            for p in r.preferences:
                if self.seats_left[p] > 0:
                    self.seats_left[p] -= 1
                    r.section = p
                    r.status = ALLOCATED
                    if p != r.preferences[0]:
                        r.note("Lower preference given because higher ones were full")
                    break
            else:
                r.status = WAITLISTED
                r.note("All preferred sections full; waitlisted")

    def confirm(self):
        """Registration office (accountable owner) confirms allocations."""
        for r in self.requests:
            if r.status == ALLOCATED:
                r.status = REGISTERED
                r.note("Confirmed by registration office")


def fresh(capacity=None, restricted=None):
    cap = capacity or {"SEC-A": 2, "SEC-B": 2, "AI-ONLY": 2}
    res = restricted if restricted is not None else {"AI-ONLY": {"AI", "AIML"}}
    return RegistrationSystem(cap, res)


# ---- the five synthetic cases ------------------------------------------
def case_normal():
    s = fresh()
    s.paid = {"S001"}
    r = s.submit(Request("R1", "S001", "CSE", ["SEC-A", "SEC-B"], at(0)))
    s.verify_payments(); s.allocate(); s.confirm()
    ok = r.status == REGISTERED and r.section == "SEC-A"
    return ("1. Normal", "Complete request, payment found, SEC-A has seats",
            "REGISTERED in SEC-A", f"{r.status} in {r.section}", ok)


def case_missing_info():
    s = fresh()
    s.paid = {"S002"}
    r = s.submit(Request("R2", "S002", "CSE", [], at(0)))
    first = r.status
    s.correct(r, ["SEC-A"])
    s.verify_payments(); s.allocate(); s.confirm()
    kept = r.submitted_at == at(0)
    ok = first == NEEDS_CORRECTION and r.status == REGISTERED and kept
    return ("2. Missing information", "No section preferences entered",
            "NEEDS_CORRECTION, then REGISTERED after fix, original timestamp kept",
            f"{first}, then {r.status}; timestamp kept: {kept}", ok)


def case_duplicate():
    s = fresh()
    s.paid = {"S003"}
    r1 = s.submit(Request("R3a", "S003", "CSE", ["SEC-A"], at(0)))
    r2 = s.submit(Request("R3b", "S003", "CSE", ["SEC-A"], at(5)))
    s.verify_payments(); s.allocate(); s.confirm()
    ok = (r2.status == DUPLICATE_MERGED and r1.status == REGISTERED
          and s.seats_left["SEC-A"] == 1)
    return ("3. Duplicate", "Same student submits twice",
            "Second request merged; only one seat used",
            f"first={r1.status}, second={r2.status}, SEC-A seats left={s.seats_left['SEC-A']}", ok)


def case_duplicate_out_of_order():
    """Added after I noticed, while designing the capstone demo, that duplicate handling assumed requests arrive in time order."""
    s = fresh()
    s.paid = {"S007"}
    late = s.submit(Request("R7b", "S007", "CSE", ["SEC-A"], at(30)))   # submitted at minute 30, processed first
    early = s.submit(Request("R7a", "S007", "CSE", ["SEC-A"], at(0)))   # submitted at minute 0, processed second
    s.verify_payments(); s.allocate(); s.confirm()
    ok = (early.status == REGISTERED and early.submitted_at == at(0)
          and late.status == DUPLICATE_MERGED and s.seats_left["SEC-A"] == 1)
    return ("3b. Duplicate arriving out of order", "Earlier copy reaches the desk after the later copy",
            "Earlier submission kept as the main request; later copy merged; one seat used",
            f"early={early.status} (t={early.submitted_at.strftime('%H:%M')}), late={late.status}, SEC-A seats left={s.seats_left['SEC-A']}", ok)


def case_unauthorized():
    s = fresh()
    s.paid = {"S004"}
    r = s.submit(Request("R4", "S004", "CSE", ["AI-ONLY"], at(0)))
    s.verify_payments(); s.allocate(); s.confirm()
    ok = r.status == REJECTED and s.seats_left["AI-ONLY"] == 2
    return ("4. Unauthorized", "CSE student requests a section restricted to AI/AIML",
            "REJECTED with reason, no seat used",
            f"{r.status}, AI-ONLY seats left={s.seats_left['AI-ONLY']}", ok)


def case_failed_step():
    s = fresh({"SEC-A": 1, "SEC-B": 1}, {})
    s.paid = {"S005", "S006"}
    s.payment_service_up = False
    r5 = s.submit(Request("R5", "S005", "CSE", ["SEC-A", "SEC-B"], at(0)))
    r6 = s.submit(Request("R6", "S006", "CSE", ["SEC-A", "SEC-B"], at(10)))
    s.verify_payments()
    during = (r5.status, r6.status)
    s.payment_service_up = True
    s.verify_payments(); s.allocate(); s.confirm()
    ok = (during == (PAYMENT_PENDING, PAYMENT_PENDING)
          and r5.section == "SEC-A" and r6.section == "SEC-B"
          and r5.status == REGISTERED and r6.status == REGISTERED)
    return ("5. Failed step", "Payment service down; two students waiting (1 seat in SEC-A)",
            "Both PAYMENT_PENDING; after recovery the EARLIER submitter gets SEC-A",
            f"during outage={during}; S005 -> {r5.section}, S006 -> {r6.section}", ok)


# ---- root-cause illustration (not one of the five required cases) ------
def illustration_processing_order():
    capacity = {"SEC-A": 2}
    submitted = {"S101": 0, "S102": 5, "S103": 10, "S104": 15}  # minutes after start
    legacy_order = ["S104", "S103", "S102", "S101"]  # latest forms processed first

    seats = capacity["SEC-A"]
    legacy_winners = []
    for sid in legacy_order:
        if seats > 0:
            seats -= 1
            legacy_winners.append(sid)

    proposed_winners = sorted(submitted, key=submitted.get)[: capacity["SEC-A"]]
    ok = proposed_winners == ["S101", "S102"] and legacy_winners == ["S104", "S103"]
    return ("6. Illustration: processing order vs submission order",
            "4 students want SEC-A (2 seats); latest forms are processed first",
            "Legacy: seats go to the latest submitters. Proposed: seats go to the earliest.",
            f"legacy winners={legacy_winners}; proposed winners={proposed_winners}", ok)


def main():
    cases = [case_normal(), case_missing_info(), case_duplicate(), case_duplicate_out_of_order(),
             case_unauthorized(), case_failed_step(), illustration_processing_order()]
    print("# Test results (synthetic data)\n")
    print("| Case | Setup | Expected | Actual | Result |")
    print("|---|---|---|---|---|")
    failed = 0
    for name, setup, expected, actual, ok in cases:
        failed += 0 if ok else 1
        print(f"| {name} | {setup} | {expected} | {actual} | {'PASS' if ok else 'FAIL'} |")
    print(f"\n{len(cases) - failed}/{len(cases)} cases passed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
