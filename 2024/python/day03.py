import re

from aocd import get_data, submit

DAY = 3
YEAR = 2024

commands = re.compile(r"(?:do\(\)|don't\(\)|mul\((\d+),(\d+)\))")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    part1, part2 = 0, 0
    m = True
    for g in commands.finditer(data):
        if g.group(0).startswith("do("):
            m = True
        elif g.group(0).startswith("don"):
            m = False
        else:
            prod = int(g.group(1)) * int(g.group(2))
            part1 += prod
            if m:
                part2 += prod

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
