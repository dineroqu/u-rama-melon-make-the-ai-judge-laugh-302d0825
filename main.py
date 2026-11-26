"""Write one original office-life joke to /output/entry.txt.

The joke is a fixed string, so every run writes byte-identical output.
Before writing, the line is validated against the competition gate
(1-200 characters, a single line, not blank). After writing, the file
is read back and checked to hold exactly the validated line.
"""

import hashlib
import os
import sys

JOKE = "My calendar booked a meeting to discuss my workload, then auto-declined it for being too busy."

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the joke line against the competition gate."""
    if not line:
        raise ValueError("joke line is empty")
    if not line.strip():
        raise ValueError("joke line is blank")
    if line != line.strip():
        raise ValueError("joke line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must be a single line")
    if len(line) < 1 or len(line) > 200:
        raise ValueError("joke line must be 1-200 characters, got %d" % len(line))
    return line


def main():
    line = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("verification failed: file does not hold the validated line")
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    print(line)
    print("characters: %d" % len(line))
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
