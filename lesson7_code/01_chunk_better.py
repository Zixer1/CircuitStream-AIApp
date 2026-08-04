"""
Chunking without slicing words and sentences in half.

Run it:  python 01_chunk_better.py
"""

TEXT = (
    "Minecraft is a sandbox game developed by Mojang Studios. "
    "Players explore a blocky, procedurally generated world. "
    "They can gather raw materials, craft tools, and build structures. "
    "The game has several modes, including survival and creative. "
    "It became the best-selling video game of all time."
)


def chunk_with_overlap(text, size=100, overlap=20):
    """Cut into pieces, but let each one start a bit before the last ended."""
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks


def chunk_by_sentence(text, max_size=150):
    """Cut on full stops, so a chunk is always whole sentences."""
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


print("=== 100 characters, 20 overlap ===")
for c in chunk_with_overlap(TEXT, 100, 20):
    print("   |", c)

print("\n=== whole sentences, max 150 ===")
for c in chunk_by_sentence(TEXT, 150):
    print("   |", c)
