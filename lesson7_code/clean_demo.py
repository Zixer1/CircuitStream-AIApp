"""
Raw text out of a PDF is a mess. This cleans it up.

Run it on its own to see the before and after:
    python clean_demo.py
"""

import re

MESSY = """CHAPTER 3 - PHOTOSYNTHESIS                          Page 14

Plants   convert  sunlight into
chemical  energy.   This process
happens in the chloroplasts.

• Water goes in
• Carbon dioxide goes in
• Oxygen comes out

Smith, Biology 101, 2024                            Page 14
"""


def clean_text(text: str) -> str:
    # 1. join lines that were split mid-sentence
    text = re.sub(r"(?<![.!?:])\n(?=[a-z])", " ", text)

    # 2. drop page numbers and repeated headers/footers
    text = re.sub(r"\n?\s*Page \d+\s*\n?", "\n", text)

    # 3. squash runs of spaces and tabs down to one
    text = re.sub(r"[ \t]+", " ", text)

    # 4. squash three or more blank lines down to one gap
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # 5. turn bullet characters into a plain dash
    text = text.replace("•", "-").replace("●", "-")

    return text.strip()


if __name__ == "__main__":
    print("--- BEFORE ---")
    print(repr(MESSY[:120]), "...\n")
    print(MESSY)
    print("--- AFTER ---")
    print(clean_text(MESSY))
    print()
    print("characters before:", len(MESSY))
    print("characters after: ", len(clean_text(MESSY)))
