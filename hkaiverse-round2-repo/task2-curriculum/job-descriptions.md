# Job descriptions used in the comparison

Chosen role: **Generative AI / LLM application engineer** (applied AI engineering). All postings were read on **24 Oct 2026**. Requirements below are **paraphrased**, not copied.

## How these were collected

- I searched the web for Hyderabad and India-wide GenAI/LLM engineer postings and kept five with a visible posting date.
- The posting pages are rendered by JavaScript, so I worked from the text excerpts the search returned, not from the full pages. A "not seen" mark in the matrix means I did not see it in the excerpt. It does **not** prove the posting omits it.
- Hirist shows dates as day/month/year. I read them that way because three of the dates (18, 19 and 21) cannot be months.
- A search assistant (Claude) found these postings. I should open each link and confirm the posting still exists and says what is summarised here. I have not yet opened each link myself, so a posting may have changed or been removed since 24 Oct 2026.

## The five postings

| ID | Title and employer | Posted | Experience asked | Location | URL |
|---|---|---|---|---|---|
| J1 | Artificial Intelligence Engineer I, The Reliable Jobs | 6 Aug 2026 | 1 to 5 years | Bangalore | https://www.hirist.tech/j/artificial-intelligence-engineer-i-1661029 |
| J2 | AI Engineer, Python/LLM, Workplace | 4 Aug 2026 | 3 to 10 years | Several cities including Hyderabad | https://www.hirist.tech/j/ai-engineer-pythonllm-1660237 |
| J3 | Senior Agentic AI Engineer, LLM/Agent Orchestration, Hire Global | 19 Sep 2026 | 7 to 12 years | Hyderabad | https://www.hirist.tech/j/senior-agentic-ai-engineer-llm-agent-orchestration-1672880 |
| J4 | Lead Applied AI/LLM Engineer, AKS Intelligent Systems LLP | 18 Aug 2026 | 3 to 7 years | Gurugram, remote-first | https://www.hirist.tech/j/lead-applied-ai-llm-engineer-1664136 |
| J5 | Generative AI Engineer, LLM, Sureminds Solutions | 21 Sep 2026 | 8 to 13 years | Hyderabad | https://www.hirist.tech/j/generative-ai-engineer-llm-1673205 |

**Important limitation.** Only J1 is close to entry level (it says strong internship experience counts). The others ask for 3 to 13 years. I found no dated entry-level posting from an employer's own site, so these show the direction of the skills a graduate would grow into, not what a fresher is hired for today. Five postings from one job board is also a small sample.

*Supplementary, not counted:* a Hyderabad "AI Engineer" posting on walkingtree.tech (about 2 years' experience) asks for LangGraph, LangChain, MCP, RAG, SQL and Docker, but its excerpt showed no posting date, so I did not count it.

## What each posting asks for (paraphrased)

- **J1:** Python backend services and REST APIs with FastAPI; shipping LLM features (RAG, prompt design, structured outputs, tool calling) using hosted model APIs; agent and multi-step workflows with LangChain and LangGraph; SQL on MySQL or PostgreSQL plus caching; building evaluation sets and watching latency and cost in production.
- **J2:** Python, SQL, FastAPI or Flask, REST APIs, Git and Docker; hosted LLM APIs, prompt engineering, LangChain and LangGraph, RAG, vector databases and embeddings; deploying with Docker on cloud platforms.
- **J3:** Agent pipelines with tool or function calling and structured outputs; treating evaluations as a first-class part of the work; async Python and FastAPI services, CI/CD and Docker; end-to-end testing and monitoring; cost optimisation; event-driven systems; some post-training experience (fine-tuning methods such as LoRA).
- **J4:** Applied LLM systems with RAG, agents and evaluation; FastAPI with PostgreSQL and vector stores; Docker, CI/CD, logging and monitoring on Linux; evaluation and observability tooling; statistics, experimental design and model evaluation; LoRA fine-tuning and serving; tests, runbooks and documentation kept with the code.
- **J5:** Building and shipping RAG systems; chunking strategies; vector databases; production LLM applications using orchestration frameworks.

## Requirement themes against the curriculum

Marks: ✓ = seen in the excerpt; – = not seen in the excerpt.

| Theme | J1 | J2 | J3 | J4 | J5 | What the current structure (R1) offers | Classification |
|---|---|---|---|---|---|---|---|
| T1 Python services and REST APIs | ✓ | ✓ | ✓ | ✓ | – | ES105, ES201, ES202, AI208 | Present, needs more practice |
| T2 LLM apps: prompts, RAG, embeddings, vector stores | ✓ | ✓ | ✓ | ✓ | ✓ | AI306 NLP only; no course by this name | Absent as a course |
| T3 Agent orchestration and tool calling | ✓ | ✓ | ✓ | ✓ | – | None listed | Absent |
| T4 Evaluation, observability, cost and latency | ✓ | – | ✓ | ✓ | – | AI304 covers model evaluation basics (my assumption) | Absent for LLM systems |
| T5 Containers, CI/CD, cloud, monitoring | – | ✓ | ✓ | ✓ | – | AI205 Operating Systems gives Linux basics | Absent |
| T6 SQL and databases, vector stores | ✓ | ✓ | – | ✓ | ✓ | AI202 DBMS | Present; vector stores absent |
| T7 Fine-tuning (for example LoRA) | – | – | ✓ | ✓ | – | AI310 Deep Learning | Present; fine-tuning content unknown |
| T8 Tests, Git workflow, documentation | – | ✓ | ✓ | ✓ | – | ES202 Industry Coding Practices (title only) | Present; depth unknown |
| T9 Statistics and ML foundations | – | – | – | ✓ | – | BS105, AI304 | Covered (keep) |

I judged "what R1 offers" from **course titles and L-T-P-C only**. I did not have syllabus contents or assessment details, so every "present" or "absent" call needs checking against the actual syllabi.

*Note on the blockchain, soft computing and big-data courses:* none of the five excerpts mentioned blockchain or fuzzy and evolutionary methods. Hadoop-style big-data stacks did not appear either, though event-driven systems and caching did. That is weak evidence about those courses, because the sample is small and aimed at one kind of role.
