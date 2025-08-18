import typer
from typing import Optional, List
from pathlib import Path
from tqdm import tqdm
from .tools.jobs_adapter import fetch_sample, fetch_live
from .chains.summarize import summarize_job
from .memory.vectorstore import JobStore
from .config import PROC_DIR
from .utils.io import write_json

app = typer.Typer(help="Agentic Job Researcher")

@app.command()
def ingest(source: str = typer.Option("sample", help="sample | live"),
           q: Optional[str] = typer.Option(None),
           location: Optional[str] = typer.Option(None)):
    if source == "sample":
        jobs = fetch_sample()
    elif source == "live":
        jobs = fetch_live(q=q, location=location)  # implement in jobs_adapter.py
    else:
        raise typer.BadParameter("source must be 'sample' or 'live'")

    summarized = []
    for j in tqdm(jobs, desc="Summarizing"):
        s = summarize_job(j)
        summarized.append(s)

    out_path = PROC_DIR / f"{source}_summarized.json"
    write_json(out_path, summarized)
    typer.secho(f"Wrote {out_path}", fg=typer.colors.GREEN)

    store = JobStore()
    store.upsert_jobs(summarized)
    typer.secho("Indexed into vector store.", fg=typer.colors.GREEN)

@app.command()
def query(q: str = typer.Argument(..., help="Your semantic query"),
          k: int = typer.Option(5, help="how many results")):
    store = JobStore()
    hits = store.search(q, k=k)
    for i, (doc, meta, dist) in enumerate(hits, 1):
        typer.echo(f"\n[{i}] {meta.get('role_title')} @ {meta.get('company')}  ({meta.get('location')})")
        typer.echo(f"Skills: {', '.join(meta.get('core_skills',[]))}")
        typer.echo(f"URL: {meta.get('url')}")
        typer.echo(f"Score: {dist:.4f}")

if __name__ == "__main__":
    app()
