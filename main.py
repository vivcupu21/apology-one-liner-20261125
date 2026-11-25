#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single apology line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no files besides the output.
"""

import os

ENTRY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def load_line() -> str:
    """Read the apology line from entry.txt next to this script."""
    with open(ENTRY_FILE, "r", encoding="utf-8") as fh:
        return fh.read().strip()


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    text = load_line()
    if not (1 <= len(text) <= 159):
        raise SystemExit(f"entry length {len(text)} is outside 1-159")
    if not text.strip():
        raise SystemExit("entry is blank")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {target} ({len(text)} characters, 1 line)")


if __name__ == "__main__":
    main()
