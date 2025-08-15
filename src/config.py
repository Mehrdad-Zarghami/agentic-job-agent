from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

#The second argument is the deafult value in case any of the keys are not provided in .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("MODEL", "gpt-4o-mini") 
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))
RAW_DIR = DATA_DIR / "raw"
PROC_DIR = DATA_DIR / "processed"
VECTOR_DIR = Path(os.getenv("VECTOR_DIR", "./data/vectorstore"))

for p in [DATA_DIR, RAW_DIR, PROC_DIR, VECTOR_DIR]:
    p.mkdir(parents=True, exist_ok=True)