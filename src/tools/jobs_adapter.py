from pathlib import Path
from typing import List, Dict, Optional
from ..utils.io import read_json
from ..config import RAW_DIR

def fetch_sample() -> List[Dict]:
    # In a real run, you'd hit APIs; for MVP we load sample JSON.
    sample_path = Path("sample_data/jobs_sample.json")
    jobs = read_json(sample_path)
    # Save raw
    out = RAW_DIR / "sample_raw.json"
    out.write_text(sample_path.read_text(encoding="utf-8"), encoding="utf-8")
    return jobs

def fetch_live(q: Optional[str]=None, location: Optional[str]=None) -> List[Dict]:
    """
    Stub: implement your preferred source API here (e.g., Greenhouse/Lever/RemoteOK).
    Return a list of dicts with at least: title, company, location, description, url
    """
    raise NotImplementedError("Implement your live adapter (API/scraper) here.")