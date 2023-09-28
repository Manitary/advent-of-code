import re
from math import factorial

from aocd import get_data, submit

DAY = 23
YEAR = 2016


PATTERN_1 = re.compile(r"cpy (\d+) \w")
PATTERN_2 = re.compile(r"jnz (\d+) \w")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    c = int(PATTERN_1.findall(data)[-1])
    d = int(PATTERN_2.findall(data)[-1])

    def solve(n: int) -> int:
        return factorial(n) + c * d

    part1 = solve(7)
    part2 = solve(12)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
