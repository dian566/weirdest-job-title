#!/usr/bin/env python3
"""Weirdest job title, entry 2: the CEO of Ctrl+Z."""

import os
import sys

TITLE = "Chief Executive Officer of Ctrl+Z"
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
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(TITLE)
    print("wrote %d characters" % len(TITLE))


if __name__ == "__main__":
    main()
