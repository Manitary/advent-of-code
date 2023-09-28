import re
from functools import cache

from aocd import get_data, submit

DAY = 12
YEAR = 2016

PATTERN = re.compile(r"cpy (\d+) (?:c|d)")


@cache
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    d0, c0, c1, d1 = map(int, tuple(PATTERN.findall(data)))
    part1 = fibonacci(2 + d0) + c1 * d1
    part2 = fibonacci(2 + d0 + c0) + c1 * d1
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
