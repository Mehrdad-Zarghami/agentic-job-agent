# Agentic Job Researcher

An **agentic AI** that searches job posts, summarizes key requirements, and stores them in a **vector database** for semantic queries like:  
> “Remote computer vision roles in the UK posted last week with PyTorch.”

- **Why this project?** Agent roles (LangChain/Crew/Copilot-like tooling) are in demand. This repo shows end‑to‑end skills: LLM orchestration, tool use (job search), memory (vector DB), and a clean engineering layout.

## Features (MVP)
- 🔎 **Job fetch** via pluggable adapter (API/scrape/mock)
- 🧠 **LLM summarization** of each posting (role, skills, seniority, salary, location)
- 💾 **Semantic memory** using ChromaDB + OpenAI embeddings
- ❓ **Natural queries** over the stored postings

## Quickstart

### 1) Setup
```bash
git clone https://github.com/<you>/agentic-job-researcher.git
cd agentic-job-researcher
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
