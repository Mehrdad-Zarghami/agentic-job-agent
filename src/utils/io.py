import json
from pathlib import Path
from typing import Any

def read_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_json(path:Path, obj:Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f: #The file (`jobs.json`) is actually created later when you call `open(path, "w", ...)` and write to it.
        json.dump(obj, f, ensure_ascii=False, indent=2)


###

"""
from pathlib import Path
import json

path = Path("data/processed/jobs.json")
path.parent.mkdir(parents=True, exist_ok=True)  # creates data/processed/ if not existed
with open(path, "w", encoding="utf-8") as f:  #The file (`jobs.json`) is actually created later when you call `open(path, "w", ...)` and write to it.
    json.dump({"key": "value"}, f, indent=2)
"""
