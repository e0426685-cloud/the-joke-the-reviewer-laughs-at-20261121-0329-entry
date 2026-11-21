#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one line to /output/entry.txt: a one-line joke about working
beside an AI coding agent. Deterministic, standard library only, no
network. The joke is a single fixed text, chosen for the judge's brief:
on-topic, a surprise at the end, a truth any reviewer of an agent's
diff recognises at once, and not one word more than it needs.
"""

import os
import sys

JOKE = (
    "My AI agent writes the code, reviews its own PR, and merges it - "
    "I just nod at the diff and stay on call for the outage."
)

MAX_CHARS = 280


def validate(text: str) -> str:
    """The gate: UTF-8 text of 1 to 280 code points, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 280 limit")
    text.encode("utf-8")
    return text


def main() -> int:
    entry = validate(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
