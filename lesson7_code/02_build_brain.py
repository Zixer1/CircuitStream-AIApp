"""
Build the knowledge base for your final project.

Takes your cleaned text, cuts it into chunks, turns each chunk into
coordinates, and stores them in Chroma. Run this once per document.

Setup:
  pip install chromadb

The first run downloads a small model (about 80 MB). Be patient once.
"""

import chromadb

# ---------- 1. your cleaned text from Lesson 6 ----------
# replace this with your own, or read it from a file:
#   text = open("my_notes.txt").read()
TEXT = (
    "Minecraft is a sandbox game developed by Mojang Studios. "
    "Players explore a blocky, procedurally generated world. "
    "They can gather raw materials, craft tools, and build structures. "
    "The game has several modes, including survival and creative. "
    "It became the best-selling video game of all time."
)


def chunk_by_sentence(text, max_size=150):
    sentences = text.split(". ")
    chunks, current = [], ""
    for s in sentences:
        if len(current) + len(s) < max_size:
            current += s + ". "
        else:
            chunks.append(current.strip())
            current = s + ". "
    if current:
        chunks.append(current.strip())
    return chunks


chunks = chunk_by_sentence(TEXT)
print(f"cut into {len(chunks)} chunks")

# ---------- 2. store them ----------
db = chromadb.PersistentClient(path="./chroma_db")
brain = db.get_or_create_collection("my_project")

brain.add(
    documents=chunks,
    ids=[f"chunk{i}" for i in range(len(chunks))],
)

# ---------- 3. check it worked ----------
print("chunks now stored:", brain.count())
print("\na peek at what's in there:")
print(brain.peek(2)["documents"])
