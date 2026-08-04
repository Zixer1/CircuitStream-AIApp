"""
Cutting a long document into bite-sized pieces.

Run it:  python 00_chunk.py
"""

TEXT = (
    "Minecraft is a sandbox game developed by Mojang Studios. "
    "Players explore a blocky, procedurally generated world. "
    "They can gather raw materials, craft tools, and build structures. "
    "The game has several modes, including survival and creative. "
    "It became the best-selling video game of all time."
)


def chunk_by_size(text, size):
    """Cut the text into pieces of `size` characters."""
    return [text[i:i + size] for i in range(0, len(text), size)]


for size in (20, 150, 500):
    chunks = chunk_by_size(TEXT, size)
    print(f"\n=== {size} characters -> {len(chunks)} chunks ===")
    for c in chunks[:3]:
        print("   |", c)
    if len(chunks) > 3:
        print(f"   ... and {len(chunks) - 3} more")
