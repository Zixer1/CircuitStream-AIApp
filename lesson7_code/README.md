# Lesson 7 — building your project's knowledge base

## Install

```bash
pip install chromadb openai python-dotenv pypdf
```

The first run of `02_build_brain.py` downloads a small model (about 80 MB). Once only.

## Files

| File | What it does |
| --- | --- |
| `doc_helper.py` | Reads text out of a PDF or txt file. From last lesson, you need it again. |
| `clean_demo.py` | The cleaning function. Run it on its own to see before and after. |
| `00_chunk.py` | Cuts text at 20, 150 and 500 characters so you can see the difference. |
| `01_chunk_better.py` | Two smarter ways: overlap, and splitting on sentences. |
| `02_build_brain.py` | Chunks your text and stores it in Chroma. **This is the one that matters.** |
| `03_merge.py` | Asks a question, pulls several chunks back, glues them together. |

Run them in order.

## Use YOUR text

`02_build_brain.py` has a Minecraft paragraph in it as a placeholder. Replace it with your
cleaned text from Lesson 6:

```python
text = open("my_notes.txt").read()
```

And name the collection after your project, not `my_project`.

## Two things that go wrong

**count() says 0 or 1** — your chunks list was empty, or your document was too short to split.
Print `len(chunks)` before storing.

**Your first document disappears when you add a second** — you reused the ids. Give each
document its own prefix: `doc1_chunk0`, `doc2_chunk0`.
