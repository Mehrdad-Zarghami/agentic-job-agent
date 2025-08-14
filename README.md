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

```



### Configuration (.env file)

This project uses a .env file to store environment variables — settings and secrets that the application needs to run but should never be hard-coded into the source code.

#### Why use a .env file?

- **Security** : Keeps sensitive information (like API keys) out of the codebase and Git history.

- **Flexibility**: Allows you to change settings (e.g., models, directories) without modifying the code.

- **Portability**: Anyone running the project can create their own .env file with their own credentials.

#### Creating your .env file
You can use eather of the folloing ways:

1. Copy the example file:

```bash
cp .env.example .env
```


2. Open .env in a text editor and fill in your own values:
```ini
OPENAI_API_KEY=sk-yourkeyhere            # Your OpenAI API key from https://platform.openai.com/api-keys
MODEL=gpt-4o-mini                        # Default LLM model (e.g., gpt-4o, gpt-4.1, gpt-3.5-turbo)
EMBED_MODEL=text-embedding-3-small       # Embedding model for semantic search
DATA_DIR=./data                          # Path to store raw and processed data
VECTOR_DIR=./data/vectorstore            # Path to store vector database files
```
#### How the project uses ```.env```

* The file is loaded at runtime by ```python-dotenv```.

* Variables are accessed in ```src/config.py``` using ```os.getenv(...)```.

* For example:

```python
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

How ```.env``` variables flow through the system  
```bash
              +----------------------+  
              |  .env file           |  
              |----------------------|  
              | OPENAI_API_KEY=...   |  
              | MODEL=gpt-4o-mini    |  
              | EMBED_MODEL=...      |  
              +----------+-----------+  
                         |  
                         v  
            +------------+------------+    
            |  python-dotenv          |  
            |  load_dotenv()          |  
            +------------+------------+  
                         |  
                         v  
            +------------+------------+  
            | config.py                |  
            | os.getenv("VAR_NAME")    |  
            +------------+-------------+  
                         |  
                         v  
       +-----------------+-----------------+  
       | Rest of the project (agents, LLMs)|  
       | - Summarization chain             |  
       | - Vector store embedding          |  
       | - Query handling                  |  
       +------------------------------------+  
    
```
    
##### Flow:

* Secrets and settings are stored in .env.

* python-dotenv loads them into environment variables.

* config.py reads them using os.getenv().

* The agent system (LangChain, OpenAI API, ChromaDB) uses them without exposing the actual keys in the code.

**Note**: .env is listed in .gitignore to ensure it is never committed to GitHub.
