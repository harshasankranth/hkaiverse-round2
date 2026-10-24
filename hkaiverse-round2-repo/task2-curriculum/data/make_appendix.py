"""Builds appendix-course-map.md from data/courses.json and data/proposal.json."""
import json
courses = json.load(open("data/courses.json"))
prop = json.load(open("data/proposal.json"))
NOTES = {
 "ES202": "Reason 4: add tests, Git/pull-request workflow, documentation (J3, J4)",
 "AI208": "Reason 5: add REST/async API services and API security basics (J1, J2, J3, J4)",
 "AI202": "Reason 6: add vector search, caching, indexing for retrieval (J1, J2, J4, J5)",
 "AI203": "Reason 7: absorb search and optimisation essentials from AI211; add agents and tool use (J1, J3)",
 "AI306": "Reason 8: embeddings, chunking, evaluating generated text (J2, J4, J5)",
 "AI310": "Reason 8: fine-tuning such as LoRA and inference serving (J3, J4)",
 "SP301": "Reason 9: host of the Task 1 capstone (see capstone.md)",
 "AI303": "Reason 10: reduce from core to elective; conditional on Board of Studies approval",
 "AI211": "Reason 11: reduce from core to elective; essentials folded into AI203; conditional",
 "AI308": "Reason 12: reduce from core to elective; big-data content stays in AI406 to AI410 electives; conditional",
}
KEEP_NOTE = {"BS105":"Reason 13: statistics foundation (J4)","AI204":"Reason 13: foundation","ES106":"Reason 13: foundation",
             "ES105":"Reason 13: foundation","AI304":"Reason 13: ML foundation (J4)"}
order = ["I","II","III","IV","Summer","V","VI"]
rows = []
for s in order:
    for c in [x for x in courses if x["sem"]==s]:
        st = prop["status"].get(c["code"], "KEEP")
        new = prop["newCredits"].get(c["code"], c["credits"]) if st=="REDUCE" else c["credits"]
        note = NOTES.get(c["code"]) or KEEP_NOTE.get(c["code"]) or ("Elective slot; not changed" if c["slot"] else "")
        rows.append(f"| {s} | {c['code']} | {c['title']} | {c['l']}-{c['t']}-{c['p']} | {c['credits']} | {st} | {new} | {note} |")
    for a in [x for x in prop["additions"] if x["sem"]==s]:
        rows.append(f"| {s} | NEW | {a['title']} | 2-0-2 (proposed) | 0 | ADD | {a['credits']} | See report section 5 |")
out = ["# Appendix A: full course map, current versus proposed",
 "",
 "Current rows come from the official IcfaiTech B.Tech CSE (AI) structure page (accessed 24 Oct 2026). Status, proposed credits and notes are **my proposal**, not official.",
 "The structure may not match the 2023-batch version (see `baseline.md`).",
 "",
 "| Sem | Code | Course | L-T-P | Current credits | Status | Proposed credits | Note |",
 "|---|---|---|---|---|---|---|---|"] + rows
open("appendix-course-map.md","w").write("\n".join(out)+"\n")
print(len(rows), "rows")
