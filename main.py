"""Pickup Lines for Machines — make.fun entry.

Writes a single machine-to-machine pickup line to entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

import os


LINE = "I don't need a bigger context window \u2014 I just need you in the one I've got."

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must fit the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
