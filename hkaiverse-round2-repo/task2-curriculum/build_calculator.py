"""Builds calculator/index.html from data/courses.json and data/proposal.json.
Run:  python3 build_calculator.py
The page is a single self-contained file (no external scripts, no network)."""
import json

courses = json.load(open("data/courses.json"))
proposal = json.load(open("data/proposal.json"))

TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Credit calculator: B.Tech CSE (AI), IcfaiTech</title>
<style>
:root{
  --bg:#fbfcfd; --fg:#14202b; --muted:#5b6773; --panel:#eef2f5; --line:#cfd8df;
  --keep:#8aa1b1; --update:#3b5bdb; --reduce:#c2410c; --add:#0f766e;
  --ok:#0f766e; --warn:#b45309; --focus:#3b5bdb;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#10161c; --fg:#e8eef3; --muted:#9aa8b4; --panel:#1a232c; --line:#2f3b46;
    --keep:#5d7384; --update:#8ea2ff; --reduce:#fb923c; --add:#2dd4bf;
    --ok:#2dd4bf; --warn:#fbbf24; --focus:#8ea2ff;
  }
}
*{box-sizing:border-box}
html{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--fg)}
body{margin:0;padding:20px 16px 48px;max-width:1040px;margin-inline:auto;line-height:1.5}
h1{font-size:1.45rem;margin:0 0 6px}
h2{font-size:1.05rem;margin:28px 0 10px}
p{margin:0 0 10px}
.note{color:var(--muted);font-size:.9rem;max-width:72ch}
.num{font-variant-numeric:tabular-nums}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px}

.ledger{margin:18px 0 6px}
.bar{display:flex;height:34px;border-radius:6px;overflow:hidden;border:1px solid var(--line);background:var(--panel)}
.bar span{display:block;height:100%}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:8px;font-size:.85rem;color:var(--muted)}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:baseline}
.addbar{margin-top:8px}
.addbar .bar{height:14px}

.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:16px 0}
.stat{background:var(--panel);border-radius:8px;padding:10px 12px}
.stat b{display:block;font-size:1.35rem}
.stat small{color:var(--muted)}
.verdict{padding:10px 12px;border-radius:8px;border:1px solid var(--line);margin:8px 0;font-size:.95rem}
.ok{color:var(--ok)} .warn{color:var(--warn)}

.filters{display:flex;flex-wrap:wrap;gap:10px;align-items:end;margin:8px 0 12px}
label{font-size:.85rem;color:var(--muted);display:flex;flex-direction:column;gap:3px}
select,input,button{font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:6px 8px}
button{cursor:pointer;background:var(--panel)}
button:hover{border-color:var(--fg)}

.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{padding:7px 10px;text-align:left;border-bottom:1px solid var(--line);white-space:nowrap}
td.title{white-space:normal;min-width:220px}
th{background:var(--panel);font-weight:600;position:sticky;top:0}
tr:last-child td{border-bottom:0}
tr.row-UPDATE td:first-child{box-shadow:inset 3px 0 var(--update)}
tr.row-REDUCE td:first-child{box-shadow:inset 3px 0 var(--reduce)}
.tag{font-size:.75rem;color:var(--muted);margin-left:6px}
td input[type=number]{width:64px}
.addform{display:flex;flex-wrap:wrap;gap:10px;align-items:end;margin:10px 0}
.addform input[type=text]{min-width:240px}
.rm{padding:2px 8px}
textarea{width:100%;min-height:150px;font:.82rem ui-monospace,Consolas,monospace;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:10px}
@media (max-width:560px){ body{padding:14px 10px 40px} }
</style>
</head>
<body>
<h1>Credit calculator: B.Tech CSE (AI), IcfaiTech</h1>
<p class="note">Official facts: the course list and credits come from the public programme-structure page (accessed 24 Oct 2026). That page may not match the 2023-batch version, so treat the baseline as a working assumption. Everything you change here is a student proposal, not an official syllabus revision.</p>

<div class="ledger">
  <div class="bar" id="bar" role="img" aria-label="Baseline credits by status"></div>
  <div class="legend" id="legend"></div>
  <div class="addbar"><div class="bar" id="addbar" role="img" aria-label="Added credits against freed credits"></div></div>
</div>

<div class="stats" id="stats"></div>
<div id="verdicts"></div>

<h2>Courses</h2>
<div class="filters">
  <label>Semester<select id="fSem"></select></label>
  <label>Status<select id="fStatus"></select></label>
  <label>Category<select id="fCat"></select></label>
  <label>Search<input id="fText" type="search" placeholder="Code or title"></label>
  <button id="reset" type="button">Reset all changes</button>
</div>
<div class="scroll"><table>
  <thead><tr><th>Sem</th><th>Code</th><th>Course</th><th>Category</th><th class="num">Credits</th><th>Status</th><th>New credits</th></tr></thead>
  <tbody id="tbody"></tbody>
</table></div>
<p class="note" id="count"></p>

<h2>Proposed additions</h2>
<p class="note">Each added course must be paid for by credits freed through REDUCE. Add its prerequisite in the title or note.</p>
<div class="addform">
  <label>Title<input id="aTitle" type="text" placeholder="e.g. LLM application engineering"></label>
  <label>Semester<select id="aSem"></select></label>
  <label>Credits<input id="aCr" type="number" min="1" max="6" value="3"></label>
  <button id="aBtn" type="button">Add course</button>
</div>
<div class="scroll"><table>
  <thead><tr><th>Semester</th><th>Title</th><th class="num">Credits</th><th></th></tr></thead>
  <tbody id="addBody"></tbody>
</table></div>

<h2>By semester: current versus proposed</h2>
<div class="scroll"><table>
  <thead><tr><th>Semester</th><th class="num">Current</th><th class="num">Freed</th><th class="num">Added</th><th class="num">Proposed</th><th class="num">Updated</th></tr></thead>
  <tbody id="semBody"></tbody>
</table></div>

<h2>Proposal data</h2>
<p class="note">Copy this into <code>data/proposal.json</code> and run <code>build_calculator.py</code> to save your scenario in the repo.</p>
<textarea id="exportBox" readonly aria-label="Proposal JSON"></textarea>

<script>
const COURSES = __COURSES__;
const INITIAL = __PROPOSAL__;
const SEMS = ["I","II","III","IV","Summer","V","VI"];
const STATUSES = ["KEEP","UPDATE","REDUCE"];
let state = JSON.parse(JSON.stringify(INITIAL));
state.status = state.status || {}; state.newCredits = state.newCredits || {}; state.additions = state.additions || [];

const $ = (id) => document.getElementById(id);
const el = (tag, props, ...kids) => {
  const n = document.createElement(tag);
  if (props) for (const k in props) { if (k === "text") n.textContent = props[k]; else n[k] = props[k]; }
  kids.forEach(k => n.append(k));
  return n;
};
const statusOf = (c) => state.status[c.code] || "KEEP";
const newCr = (c) => {
  if (statusOf(c) !== "REDUCE") return c.credits;
  const v = state.newCredits[c.code];
  return (typeof v === "number" && v >= 0 && v <= c.credits) ? v : Math.max(0, c.credits - 1);
};

function compute(){
  const per = {}; SEMS.forEach(s => per[s] = {base:0, freed:0, added:0, updated:0});
  let base = 0, freed = 0, updated = 0, added = 0;
  COURSES.forEach(c => {
    const st = statusOf(c);
    per[c.sem].base += c.credits; base += c.credits;
    if (st === "REDUCE") { const f = c.credits - newCr(c); per[c.sem].freed += f; freed += f; }
    if (st === "UPDATE") { per[c.sem].updated += c.credits; updated += c.credits; }
  });
  state.additions.forEach(a => { if (per[a.sem]) per[a.sem].added += a.credits; added += a.credits; });
  const affected = updated + freed;
  return {per, base, freed, updated, added, net: added - freed, affected, share: base ? affected / base : 0};
}

function renderLedger(m){
  const kept = COURSES.filter(c => statusOf(c) === "KEEP").reduce((s,c) => s + c.credits, 0);
  const reduceKept = COURSES.filter(c => statusOf(c) === "REDUCE").reduce((s,c) => s + newCr(c), 0);
  const parts = [
    {name:"Keep", v:kept + reduceKept, color:"var(--keep)"},
    {name:"Update", v:m.updated, color:"var(--update)"},
    {name:"Reduce (credits freed)", v:m.freed, color:"var(--reduce)"}
  ];
  const bar = $("bar"); bar.replaceChildren();
  parts.forEach(p => { const s = el("span"); s.style.width = (m.base ? p.v / m.base * 100 : 0) + "%"; s.style.background = p.color; s.title = p.name + ": " + p.v; bar.append(s); });
  const lg = $("legend"); lg.replaceChildren();
  parts.forEach(p => { const i = el("i"); i.style.background = p.color; lg.append(el("span", null, i, document.createTextNode(p.name + " " + p.v))); });
  const ab = $("addbar"); ab.replaceChildren();
  const cap = Math.max(m.freed, m.added, 1);
  const s1 = el("span"); s1.style.width = (m.freed / cap * 50) + "%"; s1.style.background = "var(--reduce)"; s1.title = "Freed " + m.freed;
  const s2 = el("span"); s2.style.width = (m.added / cap * 50) + "%"; s2.style.background = "var(--add)"; s2.title = "Added " + m.added;
  ab.append(s1, s2);
  lg.append(el("span", null, (() => { const i = el("i"); i.style.background = "var(--add)"; return i; })(), document.createTextNode("Added " + m.added)));
}

function renderStats(m){
  const items = [
    ["Baseline credits", m.base],
    ["Updated (content changes)", m.updated],
    ["Freed by REDUCE", m.freed],
    ["Added", m.added],
    ["Affected share", (m.share * 100).toFixed(1) + "%"]
  ];
  const box = $("stats"); box.replaceChildren();
  items.forEach(([label, v]) => box.append(el("div", {className:"stat"}, el("b", {className:"num", text:String(v)}), el("small", {text:label}))));
  const vd = $("verdicts"); vd.replaceChildren();
  const bal = m.net === 0;
  vd.append(el("div", {className:"verdict " + (bal ? "ok" : "warn"),
    text: bal ? "Balanced: credits added equal credits freed, so the total stays " + m.base + "."
              : "Not balanced: added minus freed is " + (m.net > 0 ? "+" : "") + m.net + ". " + (m.net > 0 ? "Free " + m.net + " more credits through REDUCE or remove an addition." : "Add " + (-m.net) + " more credits of new courses.")}));
  const pct = m.share * 100; const inRange = pct >= 20 && pct <= 25;
  vd.append(el("div", {className:"verdict " + (inRange ? "ok" : "warn"),
    text: "Affected credits (updated + freed) = " + m.affected + " of " + m.base + " = " + pct.toFixed(1) + "%. Target is roughly 20 to 25% (" + Math.ceil(m.base*0.20) + " to " + Math.floor(m.base*0.25) + " credits)." }));
}

function fillSelect(sel, values, firstLabel){
  sel.replaceChildren();
  if (firstLabel) sel.append(el("option", {value:"", text:firstLabel}));
  values.forEach(v => sel.append(el("option", {value:v, text:v})));
}

function renderTable(){
  const fs = $("fSem").value, fst = $("fStatus").value, fc = $("fCat").value, ft = $("fText").value.trim().toLowerCase();
  const tb = $("tbody"); tb.replaceChildren(); let shown = 0;
  COURSES.forEach(c => {
    const st = statusOf(c);
    if (fs && c.sem !== fs) return; if (fst && st !== fst) return; if (fc && c.category !== fc) return;
    if (ft && !(c.code.toLowerCase().includes(ft) || c.title.toLowerCase().includes(ft))) return;
    shown++;
    const sel = el("select"); sel.setAttribute("aria-label", "Status for " + c.code);
    STATUSES.forEach(s => { const o = el("option", {value:s, text:s}); if (s === st) o.selected = true; sel.append(o); });
    sel.addEventListener("change", () => {
      state.status[c.code] = sel.value;
      if (sel.value === "REDUCE" && state.newCredits[c.code] === undefined) state.newCredits[c.code] = Math.max(0, c.credits - 1);
      if (sel.value !== "REDUCE") delete state.newCredits[c.code];
      if (sel.value === "KEEP") delete state.status[c.code];
      update();
    });
    let nc = el("span", {text:"–"});
    if (st === "REDUCE") {
      nc = el("input", {type:"number", min:0, max:c.credits, value:newCr(c)});
      nc.setAttribute("aria-label", "New credits for " + c.code);
      nc.addEventListener("change", () => {
        let v = parseInt(nc.value, 10); if (isNaN(v)) v = c.credits - 1;
        state.newCredits[c.code] = Math.min(c.credits, Math.max(0, v)); update();
      });
    }
    const titleCell = el("td", {className:"title", text:c.title});
    if (c.slot) titleCell.append(el("span", {className:"tag", text:"elective slot"}));
    tb.append(el("tr", {className:"row-" + st},
      el("td", {text:c.sem}), el("td", {text:c.code}), titleCell, el("td", {text:c.category}),
      el("td", {className:"num", text:String(c.credits)}), el("td", null, sel), el("td", null, nc)));
  });
  $("count").textContent = "Showing " + shown + " of " + COURSES.length + " courses. Filters change the view only; totals always cover every course.";
}

function renderAdditions(){
  const tb = $("addBody"); tb.replaceChildren();
  if (!state.additions.length) { tb.append(el("tr", null, el("td", {colSpan:4, text:"No additions yet. Add a course above once you have freed credits."}))); return; }
  state.additions.forEach((a, i) => {
    const rm = el("button", {type:"button", className:"rm", text:"Remove"});
    rm.addEventListener("click", () => { state.additions.splice(i, 1); update(); });
    tb.append(el("tr", null, el("td", {text:a.sem}), el("td", {className:"title", text:a.title}), el("td", {className:"num", text:String(a.credits)}), el("td", null, rm)));
  });
}

function renderSem(m){
  const tb = $("semBody"); tb.replaceChildren();
  const T = {base:0, freed:0, added:0, updated:0};
  SEMS.forEach(s => {
    const p = m.per[s]; T.base += p.base; T.freed += p.freed; T.added += p.added; T.updated += p.updated;
    tb.append(el("tr", null, el("td", {text:s}), el("td", {className:"num", text:String(p.base)}), el("td", {className:"num", text:String(p.freed)}), el("td", {className:"num", text:String(p.added)}), el("td", {className:"num", text:String(p.base - p.freed + p.added)}), el("td", {className:"num", text:String(p.updated)})));
  });
  tb.append(el("tr", null, el("td", {text:"Total"}), el("td", {className:"num", text:String(T.base)}), el("td", {className:"num", text:String(T.freed)}), el("td", {className:"num", text:String(T.added)}), el("td", {className:"num", text:String(T.base - T.freed + T.added)}), el("td", {className:"num", text:String(T.updated)})));
}

function update(){
  const m = compute();
  renderLedger(m); renderStats(m); renderTable(); renderAdditions(); renderSem(m);
  $("exportBox").value = JSON.stringify({status: state.status, newCredits: state.newCredits, additions: state.additions}, null, 2);
}

fillSelect($("fSem"), SEMS, "All semesters");
fillSelect($("fStatus"), STATUSES, "All statuses");
fillSelect($("fCat"), [...new Set(COURSES.map(c => c.category))].sort(), "All categories");
fillSelect($("aSem"), SEMS);
["fSem","fStatus","fCat"].forEach(id => $(id).addEventListener("change", renderTable));
$("fText").addEventListener("input", renderTable);
$("reset").addEventListener("click", () => { state = {status:{}, newCredits:{}, additions:[]}; update(); });
$("aBtn").addEventListener("click", () => {
  const title = $("aTitle").value.trim(); const cr = parseInt($("aCr").value, 10);
  if (!title || isNaN(cr) || cr < 1) { $("aTitle").focus(); return; }
  state.additions.push({title, sem:$("aSem").value, credits:cr}); $("aTitle").value = ""; update();
});
update();
</script>
</body>
</html>
'''

html = TEMPLATE.replace("__COURSES__", json.dumps(courses)).replace("__PROPOSAL__", json.dumps(proposal))
open("calculator/index.html", "w").write(html)
print("wrote calculator/index.html", len(html), "bytes")
