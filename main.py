#!/usr/bin/env python3
"""Weirdest job title, entry 2: the senior taster of stale sky snacks."""

# A perfectly ordinary corporate title, until you read what gets tasted:
# airline peanuts, long past their best, one tiny bag at a time.

import os
import sys

TITLE = "Senior Taste Tester for Expired Airline Peanuts"
LIMIT = 60


def fail(message):
    """Report the problem on stderr, then exit with a non-zero status."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    """Check the title, then file it at /output/entry.txt."""
    if not TITLE.strip():
        fail("the job title is empty")
    if len(TITLE) > LIMIT:
        fail("the job title is %d characters, over the %d limit" % (len(TITLE), LIMIT))
    if any(ord(ch) < 32 for ch in TITLE):
        fail("the job title must be a single line of printable text")
    if TITLE != TITLE.strip():
        fail("the job title must not start or end with whitespace")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(TITLE)
    print("wrote %d characters" % len(TITLE))


if __name__ == "__main__":
    main()
