What is:

1. `List[Dict]`
2. Why is `sample_path` `"sample_data/jobs_sample.json"`? Does it have access to `sample_data` if it’s in a parent directory?
3. What does `out.write_text(...)` do?

## Short Answer

1. **`List[Dict]`** – A type hint meaning “a list of dictionaries,” where each dictionary represents a job posting.
2. **`sample_path`** – Points to the relative path of the sample JSON file; Python resolves it relative to where the script is run, so it can access `sample_data/` if the working directory is the repo root.
3. **`out.write_text(...)`** – Writes a string directly to a file (creating it if needed), replacing its contents if it already exists.

<details>
<summary>Full Explanation</summary>

### 1. `List[Dict]`

* Comes from `typing` module:

  * **`List`** – A generic list type.
  * **`Dict`** – A dictionary type.
* `List[Dict]` means the function returns a list where each element is a dictionary.
* Example return value:

  ```python
  [
      {"title": "AI Engineer", "company": "TechCorp"},
      {"title": "Data Scientist", "company": "DataWorks"}
  ]
  ```

---

### 2. Why `sample_path` = `"sample_data/jobs_sample.json"`

* `sample_path = Path("sample_data/jobs_sample.json")` creates a `Path` object for a file located at:

  ```
  project-root/sample_data/jobs_sample.json
  ```
* Python resolves relative paths based on the **current working directory** (CWD) — the folder you run the script from.
* If you run:

  ```bash
  python src/app.py ingest --source=sample
  ```

  from the project root, `"sample_data/jobs_sample.json"` will correctly point to the file in that folder.
* The script itself is inside `src/tools/`, but since it’s executed from the root, it *can* access `sample_data/` without needing `../`.

---

### 3. `out.write_text(...)`

* **`out`** is defined as:

  ```python
  out = RAW_DIR / "sample_raw.json"
  ```

  which creates a `Path` to a file named `sample_raw.json` inside the `RAW_DIR` directory (likely `data/raw/`).
* `.write_text(string, encoding="utf-8")`:

  * Opens the file for writing (creates it if missing).
  * Writes the given string into the file.
  * Overwrites existing contents if the file already exists.
* Here it’s used to:

  ```python
  out.write_text(sample_path.read_text(encoding="utf-8"), encoding="utf-8")
  ```

  Which means:

  * Read the text from `jobs_sample.json`.
  * Write that exact text into `sample_raw.json`.

This essentially **copies the sample JSON file into the `raw/` data directory** as a record of the original fetched data.

---

### Why this design

* **`List[Dict]`** makes it clear to readers and type checkers what kind of data to expect.
* Using `Path` and relative paths keeps the code portable — no absolute paths needed.
* Writing the raw file into `RAW_DIR` keeps a local copy of exactly what was ingested for debugging and auditing.

</details>

---

\#python #typing #pathlib #file-io #relative-path

```

