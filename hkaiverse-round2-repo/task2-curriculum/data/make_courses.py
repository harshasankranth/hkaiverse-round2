"""Builds data/courses.json from the official IcfaiTech B.Tech CSE (AI) structure page.

Source: https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure
Accessed: 24 Oct 2026. Credits are copied from the page's L-T-P-C columns.
This is the CURRENT public structure. It is NOT confirmed as the 2023-batch version.
Elective slots (slot=True) are placeholders whose credit (3) follows the page's
elective tables; the page does not print a credit next to "PE 1"/"PE 2".
"""
import json

C = []
def add(sem, code, title, l, t, p, cr, cat, slot=False):
    C.append(dict(sem=sem, code=code, title=title, l=l, t=t, p=p, credits=cr, category=cat, slot=slot))

# Semester I
add("I","EG101","English Language Skills",2,0,2,3,"Humanities and skills")
add("I","ES101","Engineering Graphics",1,0,4,3,"Engineering basics")
add("I","BS101","Chemistry",2,1,2,4,"Basic sciences")
add("I","HS101","Understanding India",0,0,0,0,"Humanities and skills")
add("I","BS102","Physics",2,1,2,4,"Basic sciences")
add("I","BS103","Linear Algebra and Ordinary Differential Equations",2,1,0,3,"Mathematics")
add("I","ES105","Computer Programming",2,0,4,4,"Core computing")
# Semester II
add("II","EG102","Professional Communication",2,1,0,3,"Humanities and skills")
add("II","ES102","Digital Fabrication",1,1,2,3,"Engineering basics")
add("II","ES103","Environmental Sciences",2,0,0,2,"Humanities and skills")
add("II","ES104","Basic Electronics",2,1,2,4,"Engineering basics")
add("II","BS104","Higher Calculus",2,1,0,3,"Mathematics")
add("II","ES106","Data Structures",2,0,4,4,"Core computing")
add("II","ES107","Introduction to DS and AI",2,1,0,3,"Core AI and data")
# Semester III
add("III","MG201","Engineering Economics and Management",2,1,0,3,"Humanities and skills")
add("III","BS105","Probability and Statistics",2,1,0,3,"Mathematics")
add("III","ES201","Object Oriented Programming Concepts",2,0,4,4,"Core computing")
add("III","CR201","Power Skills I",0,0,2,1,"Humanities and skills")
add("III","AI201","Introduction to IoT",2,0,2,3,"Core computing")
add("III","AI202","Database Management Systems",2,1,2,4,"Core computing")
add("III","AI203","Artificial Intelligence",3,0,0,3,"Core AI and data")
add("III","AI204","Design and Analysis of Algorithms",3,0,0,3,"Core computing")
# Semester IV
add("IV","HSXX","Digital Humanities Elective",3,0,0,3,"Humanities and skills",True)
add("IV","CR202","Power Skills II",0,0,2,1,"Humanities and skills")
add("IV","ES202","Industry Coding Practices",2,1,2,4,"Core computing")
add("IV","AI205","Operating Systems",3,0,2,4,"Core computing")
add("IV","AI206","Computer Organization and Architecture",3,0,0,3,"Core computing")
add("IV","AI207","Discrete Mathematics",2,1,0,3,"Mathematics")
add("IV","AI208","Web Enabled Technologies (WEB 3.0)",2,1,2,4,"Core computing")
add("IV","AI211","Soft Computing",3,0,0,3,"Core AI and data")
# Summer term
add("Summer","IP201","Summer Term / Internship Program 1",0,0,0,5,"Project and internship")
# Semester V
add("V","HS301","Constitution of India",0,0,0,0,"Humanities and skills")
add("V","XXXX","Elective-I",3,0,0,3,"Elective slot",True)
add("V","CR301","Power Skills III",0,0,2,1,"Humanities and skills")
add("V","AI301","Predictive Analytics",3,0,0,3,"Core AI and data")
add("V","AI302","Computer Networks",3,0,2,4,"Core computing")
add("V","AI303","Blockchain Technology",3,0,0,3,"Core computing")
add("V","AI304","Machine Learning",3,0,2,4,"Core AI and data")
add("V","AI305","Data Wrangling and Visualization",2,0,2,3,"Core AI and data")
add("V","PE2","Professional Elective (PE 2)",3,0,0,3,"Elective slot",True)
# Semester VI
add("VI","SP301","Special Project",0,0,6,3,"Project and internship")
add("VI","DSXX","Elective-II",3,0,0,3,"Elective slot",True)
add("VI","CR302","Power Skills IV",0,0,2,1,"Humanities and skills")
add("VI","AI306","Natural Language Processing",3,0,0,3,"Core AI and data")
add("VI","AI307","Computer Vision",3,0,0,3,"Core AI and data")
add("VI","AI308","Big Data Systems",3,0,0,3,"Core AI and data")
add("VI","AI310","Deep Learning",2,1,2,4,"Core AI and data")
add("VI","PE1","Professional Elective (PE 1)",3,0,0,3,"Elective slot",True)

for c in C:
    assert c["credits"] >= 0
    # L-T-P-C check: where the page gives L,T,P and C, they should be plausible
json.dump(C, open("data/courses.json","w"), indent=1)

order = ["I","II","III","IV","Summer","V","VI"]
print("sem, courses, credits")
tot = 0
for s in order:
    cr = sum(c["credits"] for c in C if c["sem"]==s)
    n = sum(1 for c in C if c["sem"]==s)
    tot += cr
    print(s, n, cr)
print("TOTAL", len(C), tot)
print("elective slot credits:", sum(c["credits"] for c in C if c["slot"]))
print("by category:")
cats = {}
for c in C: cats[c["category"]] = cats.get(c["category"],0)+c["credits"]
for k,v in sorted(cats.items(), key=lambda x:-x[1]): print(" ",k,v)
