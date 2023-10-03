import re

import numpy as np
from aocd import get_data, submit

DAY = 3
YEAR = 2018

RE_PARSE = re.compile(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    rectangles = tuple(map(lambda x: tuple(map(int, x)), RE_PARSE.findall(data)))
    grid = np.zeros((1000, 1000), dtype=np.uint)
    for r in rectangles:
        x, y, dx, dy = r
        grid[x : x + dx, y : y + dy] += 1

    part1 = int(np.sum(grid > 1))

    part2 = 0
    for i, r in enumerate(rectangles, 1):
        x, y, dx, dy = r
        if np.all(grid[x : x + dx, y : y + dy] == 1):
            part2 = i
            break

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
