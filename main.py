#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message line to /output/entry.txt.

The entry was drafted in this session by weighing candidates against the
judge brief: it must read as a real commit subject line about a fix that
backfired, be funny on its own, and capture the specific irony of a repair
that broke more than it mended. The winning line does all three with one
escalation: the bug touched 1% of users, so the "fix" deleted the other 99%.
"""

import os

ENTRY = "fix: bug affected 1% of users; fixed by deleting the other 99%"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly the line, no trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
