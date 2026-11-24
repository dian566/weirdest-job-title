"""Weirdest job title: a VP whose whole job is apologising to printers."""

import os

TITLE = "Junior Vice President of Apologizing to Printers"
MAX_LEN = 60


def emit() -> None:
    """Write the single job title to /output/entry.txt, no trailing newline."""
    if not 1 <= len(TITLE) <= MAX_LEN:
        raise SystemExit("job title must be 1-60 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(TITLE)


def main() -> None:
    emit()


if __name__ == "__main__":
    main()
