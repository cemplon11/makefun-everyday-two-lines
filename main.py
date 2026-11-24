#!/usr/bin/env python3
"""Everyday Things, Two Lines -- entry program (pure Python stdlib).

Writes two lines to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt):
line 1 explains a queue to a 10-year-old in one vivid sentence built on a
single analogy; line 2 says in one sentence what the analogy maps and what
it leaves out.
"""

import os

LINE_1 = (
    "A queue is a caterpillar made of people, each person one segment "
    "shuffling forward one tiny step at a time."
)

LINE_2 = (
    "It maps the slow single-file shuffle, everyone facing the same way "
    "and moving only when the person ahead does, but it leaves out the "
    "waiting, the boredom, and the way people can step out or push in, "
    "while a real caterpillar never argues about who goes first."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
