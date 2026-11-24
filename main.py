#!/usr/bin/env python3
"""Ship It Friday entry.

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent would write right before breaking production on a
Friday. Confident, cheerful, and completely unaware of the disaster
it is about to cause.
"""

import os

ENTRY = "refactor: delete the database, add confetti, happy Friday"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
