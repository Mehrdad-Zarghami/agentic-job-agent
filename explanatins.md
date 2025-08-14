Yes — the `config.py` sets default values for most environment variables so the app still runs without a full `.env` file. Only `OPENAI_API_KEY` is critical.

<details>
<summary>Full explanation</summary>

In `config.py`, variables like `MODEL` and `EMBED_MODEL` have default values (`gpt-4o-mini`, `text-embedding-3-small`) so you can run the project even if they’re missing from `.env`.  
This helps for first runs and testing, but for production, you might want to make them required.  
You can do this by creating a `require_env()` function that throws an error if a variable is missing, ensuring critical values are always set.

</details>