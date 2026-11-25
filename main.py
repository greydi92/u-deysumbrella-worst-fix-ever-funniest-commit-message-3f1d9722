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
import sys

ENTRY = "fix: bug affected 1% of users; fixed by deleting the other 99%"


def check_entry() -> None:
    """Fail loudly if ENTRY ever drifts outside the gate (1-100 chars,
    not only whitespace, single line). A bad entry must never be written
    with a success exit code: the sealed scorer would reject it silently
    at grade time instead."""
    problems = []
    if not 1 <= len(ENTRY) <= 100:
        problems.append(f"length {len(ENTRY)} is outside 1-100 chars")
    if not ENTRY.strip():
        problems.append("entry is only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        problems.append("entry is not a single line")
    if ENTRY != ENTRY.strip():
        problems.append("entry has leading/trailing whitespace")
    if problems:
        print(f"invalid entry: {'; '.join(problems)}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    check_entry()
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly the line, no trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
