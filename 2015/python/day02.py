from typing import Sequence

from aocd import get_data, submit

DAY = 2
YEAR = 2015


def area(sides: Sequence[int]) -> tuple[int, int]:
    a, b, c = sorted(sides)
    return 3 * a * b + 2 * (b * c + c * a), 2 * (a + b) + a * b * c


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    data = (tuple(map(int, d.split("x"))) for d in data)
    part1, part2 = map(sum, zip(*map(area, data)))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
