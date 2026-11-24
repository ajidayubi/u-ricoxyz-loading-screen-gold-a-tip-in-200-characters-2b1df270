#!/usr/bin/env python3
"""Loading Screen Gold: a single loading-screen tip (<=200 chars).

Writes one fixed tip to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Zero dependencies, no input, no network, no randomness, no clock.
"""

import os

TIP = (
    "Tip: while this loads, your agent already fixed the bug, "
    "broke it again, and is writing a confident summary of the fix."
)


def _validate(text):
    """Mirror the competition gate: 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("tip is not text")
    if not 1 <= len(text) <= 200:
        raise ValueError("tip must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("tip must be a single line")
    if not text.strip():
        raise ValueError("tip must not be only whitespace")


def main():
    _validate(TIP)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    with open(path, "rb") as f:
        written = f.read()
    if written != TIP.encode("utf-8"):
        raise ValueError("entry.txt did not round-trip byte for byte")
    print(TIP)


if __name__ == "__main__":
    main()
