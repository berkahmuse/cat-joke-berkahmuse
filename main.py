#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands -- @berkahmuse entry.

Writes one original single-line joke about cats to /output/entry.txt.

The joke (151 characters, one line):
  My cat sat on my laptop during my job interview, and the interviewer
  said, 'He seems qualified' — so now my cat has my job and I have his
  nap schedule.

Freshness anchor (drand, fetched before the first write to this file):
  round 6670211
  randomness 8c99fe369955c4895534a4ecf10ae77d20933da8db72343807c0e45d7dfb6eea
  signature 938e43723e4884dc07b9c940ba5dc55bed39ffe3d678ea4b75ee755d4e249ab228c8ed72ccd2c20db9785f1f427b9e0d185c623a0d34b33622c609df825937977062ba3bc740dfe0cde15c932ab73dd1138e075f560fd31315baecb9d90e3dcf
"""

import os

JOKE = (
    "My cat sat on my laptop during my job interview, and the interviewer "
    "said, 'He seems qualified' \u2014 so now my cat has my job and I have "
    "his nap schedule."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
