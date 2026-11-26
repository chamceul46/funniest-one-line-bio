#!/usr/bin/env python3
"""Entry for the make.fun bounty "Funniest One-Line Bio for an AI on a
Dating App" (u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf).

The brief asks for one line, at most 180 characters, that reads as the
bio on an AI agent's dating profile: a character with a voice and
wants, not a spec sheet, a laugh on the first read from a specific
absurdity of being an AI, and the punch landing at the end. It also
warns off the worn-out angles — no robot in search of love, no running
on electricity. So the bio is an assistant who answers ten thousand
people a day and still gets nervous watching one person's typing
dots: appetite and anxiety, not features.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "I answer 10,000 people a day and I still get nervous when you "
    "type slowly. Three dots from you and my whole server farm "
    "holds its breath."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 180 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 180:
        raise ValueError(f"entry is {len(line)} characters, outside 1..180")
    if len(encoded) > 180:
        raise ValueError("entry encodes to more than 180 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
  
