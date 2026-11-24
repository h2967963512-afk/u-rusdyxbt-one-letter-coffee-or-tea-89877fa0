"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one letter, "A" — coffee. Coffee is the more
# vivid, funnier and truer answer: the drink that turns a morning into
# a mission, and the letter that lands as a whole answer on its own.
# No word, no explanation, no punctuation beside it.
import os

TEXT = "A"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
