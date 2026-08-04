"""
Ask a question, get several chunks back, glue them together.

Run 02_build_brain.py first.

Setup:
  pip install chromadb openai python-dotenv
"""

import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

db = chromadb.PersistentClient(path="./chroma_db")
brain = db.get_or_create_collection("my_project")

question = "What can players do in the game?"

for how_many in (1, 3):
    hits = brain.query(query_texts=[question], n_results=how_many)
    notes = "\n".join(hits["documents"][0])

    print(f"\n=== n_results={how_many} ===")
    print(notes)

load_dotenv()
ai = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

hits = brain.query(query_texts=[question], n_results=3)
notes = "\n".join(hits["documents"][0])

prompt = f"""Answer using ONLY these notes.
{notes}

Question: {question}"""

r = ai.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
)

print("\n=== the answer ===")
print(r.choices[0].message.content)
