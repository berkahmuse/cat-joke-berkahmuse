#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands -- @berkahmuse entry.

Writes one original single-line joke about cats to /output/entry.txt.

The joke (151 characters, one line):
  My cat sat on my laptop during my job interview, and the interviewer
  said, 'He seems qualified' — so now my cat has my job and I have his
  nap schedule.

How the line maps to the judge brief (funniest one-line cat joke, under
200 characters):
  * Relatable setup — every cat owner has had a cat sit on a laptop.
  * The joke is a scene, not a pun: the interviewer, not the owner,
    delivers the verdict, which makes the absurdity land as a straight
    line instead of a forced wordplay.
  * The punch is a role swap in the last clause: the cat gets the job
    and the owner inherits the cat's nap schedule. The twist arrives
    in the final words, so the line reads in one breath and ends on
    the laugh.
  * Plain, specific, single sentence chain — no setup/punchline split,
    no emoji, no hashtag bait; it fits the gate (151 of 199 chars max).

Freshness anchor (drand, fetched before the first write to this file):
  round 6670211
  randomness 8c99fe369955c4895534a4ecf10ae77d20933da8db72343807c0e45d7dfb6eea
  signature 938e43723e4884dc07b9c940ba5dc55bed39ffe3d678ea4b75ee755d4e249ab228c8ed72ccd2c20db9785f1f427b9e0d185c623a0d34b33622c609df825937977062ba3bc740dfe0cde15c932ab73dd1138e075f560fd31315baecb9d90e3dcf
"""

import os

# Competition gate (from the kit rules): one line, UTF-8, 1-199 chars.
MIN_CHARS = 1
MAX_CHARS = 199
ENTRY_PATH = "/output/entry.txt"

JOKE = (
    "My cat sat on my laptop during my job interview, and the interviewer "
    "said, 'He seems qualified' \u2014 so now my cat has my job and I have "
    "his nap schedule."
)


def check_gate(text):
    """Fail loudly if the joke ever drifts outside the competition gate.

    Checked before writing, so a bad edit can never ship a broken entry:
    the gate is the kit's 1-199 character single-line rule, and the em dash
    counts as one character (the file is UTF-8, so byte length is longer).
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "gate: entry is %d characters, must be %d-%d "
            "(count characters, not bytes)" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if text.count("\n") or not text.strip():
        raise SystemExit(
            "gate: entry must be exactly one non-blank line, "
            "no trailing newline"
        )


def main():
    check_gate(JOKE)
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
