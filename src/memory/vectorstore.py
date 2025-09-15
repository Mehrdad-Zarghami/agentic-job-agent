import chromadb
from typing import List, Dict, Tuple
from openai import OpenAI
from ..config import VECTOR_DIR, EMBED_MODEL, OPENAI_API_KEY

_client = OpenAI(api_key=OPENAI_API_KEY)

def embed(texts: List[str]) -> List[List[float]]:
    resp = _client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]

class JobStore:
    def __init__(self, collection_name: str = "jobs"):
        
        self.chroma = chromadb.PersistentClient(path=str(VECTOR_DIR))
        self.col = self.chroma.get_or_create_collection(name=collection_name)

    def upsert_jobs(self, jobs: List[Dict]):
        ids, docs, metas = [], [], []
        for i, j in enumerate(jobs):
            # Build the searchable document (OK to keep lists here as text)
            doc = (
                f"{j.get('role_title')} at {j.get('company')} in {j.get('location')}\n"
                f"Skills: {', '.join(j.get('core_skills', []))}\n"
                f"Nice: {', '.join(j.get('nice_to_have', []))}\n"
                f"Resp: {', '.join(j.get('responsibilities', []))}\n"
                f"Salary: {j.get('salary')}\nURL: {j.get('url')}"
            )

            # ✅ Make metadata primitive-only
            meta = {
                "role_title": j.get("role_title"),
                "company": j.get("company"),
                "location": j.get("location"),
                "salary": j.get("salary") if isinstance(j.get("salary"), (str, int, float, bool)) else None,
                "seniority": j.get("seniority"),
                "url": j.get("url"),
                # Optional: store lists as comma-separated strings (or remove these lines)
                "core_skills": ", ".join(j.get("core_skills", [])),
                "nice_to_have": ", ".join(j.get("nice_to_have", [])),
            }

            ids.append(f"job-{i}-{j.get('company','')}-{j.get('role_title','')}")
            docs.append(doc)
            metas.append(meta)

        embs = embed(docs)
        self.col.upsert(ids=ids, documents=docs, embeddings=embs, metadatas=metas)

    def search(self, query: str, k: int = 5) -> List[Tuple[str, Dict, float]]:
        q_emb = embed([query])[0]
        res = self.col.query(query_embeddings=[q_emb], n_results=k, include=["documents","metadatas","distances","embeddings"])
        out = []
        for i in range(len(res["ids"][0])):
            out.append((res["documents"][0][i], res["metadatas"][0][i], res["distances"][0][i]))
        return out
