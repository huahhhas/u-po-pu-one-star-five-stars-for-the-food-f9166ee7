#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes exactly one line — an alien tourist's one-star review of Earth
that still compliments the food — to /output/entry.txt (no trailing
newline).
"""

import hashlib
import os

LINE = (
    "One star: Earth made me pay rent to sit in traffic beneath a burning "
    "sky, but the tacos were so good I nearly applied for citizenship."
)
# Why this line fits the brief: a first-person alien-tourist review of
# Earth with a clear one-star verdict, a grievance only an outsider
# would frame this way (paying rent to sit in traffic under a burning
# sky), and a real compliment about the food (the tacos) that lands as
# the turn — nearly applying for citizenship is the punchline, and it
# only works because the food was that good.
# One sentence, one joke, no generic complaint list.

OUTPUT = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(raw: bytes) -> str:
    """Check the written file against the bounty gate; return its text."""
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not equal the expected line"
    # Exactly one line: no newline anywhere, not just no trailing one.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # No trailing newline: the file must be exactly the line.
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert len(raw) == len(text.encode("utf-8")), "byte length mismatch"
    # It reads as a review: it carries a one-star verdict and a food compliment.
    assert "One star" in text, "entry carries no one-star verdict"
    assert "tacos" in text, "entry carries no food compliment"
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT, "rb") as f:
        raw = f.read()
    text = validate(raw)
    print(text)
    print("sha256:", hashlib.sha256(raw).hexdigest())
    print("chars:", len(text))


if __name__ == "__main__":
    main()
