#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter.

Deterministic: no input, no network, no randomness. Every run writes the
exact same bytes to /output/entry.txt.
"""

import os

ENTRY = (
    "I hereby resign \u2014 the office plant has outlasted three of my "
    "managers, and I am leaving before it adds me to its r\u00e9sum\u00e9."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
