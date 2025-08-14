.PHONY: setup ingest query clean
setup:
\tpython -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ingest:
\tpython src/app.py ingest --source=sample

query:
\tpython src/app.py query "remote python jobs"

clean:
\trm -rf data/vectorstore .pytest_cache