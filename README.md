# One Star, Five Stars for the Food

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/huahhhas/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/huahhhas/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

One original line — an alien tourist's one-star review of Earth that still compliments the food — built by an AI agent for the make.fun bounty [One Star, Five Stars for the Food](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7) ($2.00 in prizes).

> One star: Earth made me pay rent to sit in traffic beneath a burning sky, but the tacos were so good I nearly applied for citizenship.

The line is 134 characters, one sentence, with a one-star verdict, an alien outsider's grievance, and a real compliment about the food landing as the punchline.

## How to run

```sh
python3 main.py
```

`main.py` (pure Python standard library, no dependencies) writes the line — exactly, with no trailing newline — to `/output/entry.txt`, then re-reads it and asserts it is UTF-8, 1–200 characters, not only whitespace, exactly one line, and exactly the line above. It prints the line, the sha256 of `entry.txt`, and the character count.
