## Question
If `path.parent.mkdir(parents=True, exist_ok=True)` creates the parent folders, does that also create the `jobs.json` file itself when it doesn't exist?

## Short Answer
No — `path.parent.mkdir(...)` only creates **folders**, not the file itself.  
The file (`jobs.json`) is actually created later when you call `open(path, "w", ...)` and write to it.

<details>
<summary>Full Explanation</summary>

### What happens step-by-step
1. **`path.parent.mkdir(parents=True, exist_ok=True)`**
   - Ensures the folder structure exists.
   - Example: For `data/processed/jobs.json`, this creates `data/` and `data/processed/` if missing.
   - It does **not** create `jobs.json`.

2. **`open(path, "w", encoding="utf-8")`**
   - Opens the file for writing.
   - If the file doesn’t exist, it will be created automatically.
   - If the file exists, it will be **overwritten**.

3. **`json.dump(...)`**
   - Writes your Python object as JSON into the file.

### Analogy
Think of `mkdir()` as **building the folder where the file will go**, and `open(..., "w")` as **placing the file inside it**.

### Example
```python
from pathlib import Path
import json

path = Path("data/processed/jobs.json")

# Step 1: Create folders
path.parent.mkdir(parents=True, exist_ok=True)

# Step 2 & 3: Create/write the file
with open(path, "w", encoding="utf-8") as f:
    json.dump({"job": "AI Engineer"}, f, indent=2)
