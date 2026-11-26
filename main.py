#!/usr/bin/env python3
"""Make the AI Judge Laugh -- office-life one-liner.

Writes a single original joke about office life, one line under
200 characters, to /output/entry.txt.

The joke is built from two halves: a straight office observation
(the setup) and the turn that lands it (the punchline). The output
is a fixed string, so every run writes byte-identical text.
"""

import os

# --- the joke -----------------------------------------------------------
# Setup: the calendar, the one office tool that owns everyone's time,
# does something a calendar should never need to do.
SETUP = "My calendar booked a meeting to discuss my workload,"
# Turn: the calendar itself gives up -- the meeting is cancelled by the
# very tool that called it, because even it can see the day is full.
TURN = "then auto-declined it for being too busy."

JOKE = SETUP + " " + TURN

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry line, validated against the competition gate."""
    line = JOKE.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the joke, byte for byte.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read it back and prove the file holds exactly the validated line:
    # a program that cannot vouch for its own output should not ship it.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip check failed: file differs from the entry")
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
