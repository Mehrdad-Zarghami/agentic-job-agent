from typing import Dict
from openai import OpenAI
from ..config import OPENAI_API_KEY, MODEL, TEMPERATURE

SYSTEM = """You are a helpful analyst. Summarize job postings into a compact JSON with:
role_title, company, location, core_skills (list), nice_to_have (list), salary (if any), seniority, responsibilities (bullets), url.
Keep it short and factual; infer skills from text if needed."""

PROMPT = """Job posting:
Title: {title}
Company: {company}
Location: {location}
Description: {description}
URL: {url}

Return ONLY valid JSON, no extra text."""

def summarize_job(job: Dict) -> Dict:
    client = OpenAI(api_key=OPENAI_API_KEY)
    content = PROMPT.format(
        title=job.get("title",""),
        company=job.get("company",""),
        location=job.get("location",""),
        description=job.get("description",""),
        url=job.get("url",""),
    )

    # Send request to the model (OpenAI)
    try: 

        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system","content":SYSTEM},
                {"role":"user","content":content}
            ],
            temperature=TEMPERATURE,
        )
    except:
            resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system","content":SYSTEM},
                {"role":"user","content":content}
            ],
            temperature=1,
        )


    # Parse the responce
    import json
    text = resp.choices[0].message.content.strip()
    try:
        return json.loads(text)
    
    # Fallback if parsing fails If json.loads() raises an error (because the AI’s output wasn’t valid JSON),
    #  it returns a minimal dictionary using fields from the original job with empty placeholders for missing info.
    except Exception:
        # fall back: wrap into a minimal schema
        return {
            "role_title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("location"),
            "core_skills": [],
            "nice_to_have": [],
            "salary": None,
            "seniority": None,
            "responsibilities": [],
            "url": job.get("url"),
        }