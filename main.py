#!/usr/bin/env python3
"""One Star, Five Stars for the Food.

An alien tourist's one-star review of planet Earth that still compliments
the food. Writes the single sentence to /output/entry.txt and prints it.
"""

import os

LINE = (
    "One star: your species queues for hours to stare at glowing rectangles, "
    "your weather has no off switch, and gravity is frankly rude \u2014 but the "
    "tacos alone justify the parking ticket on my saucer."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
