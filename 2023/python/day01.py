import re

from aocd import get_data, submit

DAY = 1
YEAR = 2023

RE_P2 = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")

NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def p1_num(s: str) -> int:
    nums = tuple(filter(str.isdigit, s))
    return int(f"{nums[0]}{nums[-1]}")


def p2_num(s: str) -> int:
    matches = tuple(RE_P2.finditer(s))
    n1, n2 = matches[0].group(1), matches[-1].group(1)
    return int(NUM.get(n1, n1) + NUM.get(n2, n2))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    part1 = sum(map(p1_num, data))
    part2 = sum(map(p2_num, data))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
