"""The One-Line Cat Joke That Lands -- make.fun entry.

Writes a single cat joke (under 200 characters) to /output/entry.txt.
Pure standard library, deterministic, no network, no input, no randomness.
"""

import os

LINE = "My cat slow-blinks at me, which is either 'I love you' or 'I've seen your search history.'"
# Setup (slow blink = cat "I love you") flips on the last word: affection
# swaps for embarrassment — the cat has seen the search history.


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
