#!/usr/bin/env python3
"""Write the 4AM commit message to /output/entry.txt.

One line, at most 200 characters: the note an AI agent leaves in the
log after a long night of fixing its own bugs.
"""

import os

LINE = "fix: deleted the bug I wrote at 2am, broke the fix at 3am, fixed the fix at 4am; sleep is a deprecated feature"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
