## Question
What is the purpose of the `jobs_sample.json` file in the project?

## Short Answer
It’s a **demo dataset** containing example job postings so you can run and test the project without connecting to a real job API or scraper.

<details>
<summary>Full Explanation</summary>

### Why it exists
- **Quick testing**: Lets you verify that the summarization chain, vector store, and query system work before building a real data fetcher.
- **No API dependency**: You don’t need API keys, network access, or scraping code to see the project in action.
- **Repeatable results**: Since the data is fixed, you get consistent output, which helps during debugging and development.
- **Portfolio demo**: Recruiters can run the project immediately without setting up any external data source.

### Typical content
`jobs_sample.json` is a small JSON array where each element is a job posting dictionary:
```json
[
  {
    "title": "Computer Vision Engineer",
    "company": "VisionWorks",
    "location": "Remote UK",
    "description": "OpenCV, PyTorch, YOLO; deploy on edge",
    "url": "https://example.com/jobs/1"
  },
  {
    "title": "AI Agent Developer",
    "company": "FlowOps",
    "location": "Hybrid London",
    "description": "LangChain/CrewAI, vector DB, API integrations",
    "url": "https://example.com/jobs/2"
  }
]