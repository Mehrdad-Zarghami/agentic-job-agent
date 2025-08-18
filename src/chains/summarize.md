
This function takes a raw job posting dictionary, sends it to an OpenAI model with instructions to produce a **structured JSON summary**, and returns the parsed JSON.
If the model’s response isn’t valid JSON, it falls back to returning a minimal dictionary with basic fields.

<details>
<summary>Full Explanation</summary>

### Key parts of the code

#### **Imports**

* `Dict` (from `typing`): Type hint — `job` is expected to be a dictionary, and the function will return a dictionary.
* `OpenAI`: Client for communicating with OpenAI’s API.
* `OPENAI_API_KEY` and `MODEL`: Loaded from the project’s `.env` file via `config.py`.

---

#### **Prompt design**

* **`SYSTEM`**: System message telling the AI how to behave (“helpful analyst”) and what fields the output should have (role\_title, company, etc.).
* **`PROMPT`**: Template for the user message. Inserts job details from the `job` dict into a text block.
  Example after formatting:

  ```
  Job posting:
  Title: AI Engineer
  Company: TechCorp
  Location: Remote
  Description: Build AI systems...
  URL: https://example.com/jobs/1

  Return ONLY valid JSON, no extra text.
  ```

---

#### **`summarize_job(job)` workflow**

1. **Create API client**

   ```python
   client = OpenAI(api_key=OPENAI_API_KEY)
   ```

   Uses your API key to authenticate with OpenAI.

2. **Format the prompt**

   * `PROMPT.format(...)` fills in the placeholders (`{title}`, `{company}`, etc.) from the `job` dictionary using `.get()` (avoids errors if keys are missing).

3. **Send request to OpenAI**

   ```python
   resp = client.chat.completions.create(
       model=MODEL,
       messages=[
           {"role": "system", "content": SYSTEM},
           {"role": "user", "content": content}
       ],
       temperature=0.2,
   )
   ```

   * **`model`**: The LLM to use (e.g., `"gpt-4o-mini"`).
   * **`messages`**: Conversation format — first the system instruction, then the user prompt.
   * **`temperature=0.2`**: Keeps output focused and less random.

4. **Parse the AI’s response**

   ```python
   text = resp.choices[0].message.content.strip()
   return json.loads(text)
   ```

   * Takes the LLM’s first choice.
   * Strips whitespace.
   * Parses it as JSON.

5. **Fallback if parsing fails**

   * If `json.loads()` raises an error (because the AI’s output wasn’t valid JSON), it returns a minimal dictionary using fields from the original `job` with empty placeholders for missing info.

---

### Why this design

* **Type safety**: `Dict` hint signals structured input/output.
* **Prompt control**: Splitting into `SYSTEM` and `PROMPT` makes it easy to tweak instructions.
* **Error handling**: The fallback ensures the function never crashes due to bad AI output.
* **Extensibility**: You can add more fields to `SYSTEM` and `PROMPT` without changing the rest of the pipeline.

---

### Example usage

```python
job_posting = {
    "title": "AI Engineer",
    "company": "TechCorp",
    "location": "Remote",
    "description": "Build and deploy AI models...",
    "url": "https://example.com/jobs/1"
}

summary = summarize_job(job_posting)
print(summary)
```

**Possible output:**

```json
{
  "role_title": "AI Engineer",
  "company": "TechCorp",
  "location": "Remote",
  "core_skills": ["Python", "TensorFlow", "MLOps"],
  "nice_to_have": ["LangChain", "Docker"],
  "salary": null,
  "seniority": "Mid-level",
  "responsibilities": [
    "Design and implement AI models",
    "Deploy AI services to production"
  ],
  "url": "https://example.com/jobs/1"
}
```

</details>

---

\#python #openai #prompt-engineering #json #llm


