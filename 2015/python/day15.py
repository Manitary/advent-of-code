import re

import numpy as np
from aocd import get_data, submit

DAY = 15
YEAR = 2015

PATTERN = re.compile(r"-?\d+")


def main(teaspoons: int = 100, cal: int = 500) -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    ingredients = np.matrix(
        [np.array(PATTERN.findall(ingredient), int) for ingredient in data]
    )

    part1, part2 = 0, 0
    for recipe in (
        np.array([a, b, c, teaspoons - a - b - c])
        for a in range(teaspoons)
        for b in range(teaspoons - a)
        for c in range(teaspoons - a - b)
    ):
        m = (recipe * ingredients).clip(min=0)
        score = int(np.prod(m[0, :-1]))
        part1 = max(part1, score)
        if m[0, -1] == cal:
            part2 = max(part2, score)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
