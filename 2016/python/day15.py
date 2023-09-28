import re
from functools import reduce

from aocd import get_data, submit

DAY = 15
YEAR = 2016

PATTERN = re.compile(r" (\d+)")


def chinese_remainder(n: list[int], a: list[int]) -> int:
    ans = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        ans += a_i * pow(p, -1, n_i) * p
    return ans % prod


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = data.split("\n")
    mods: list[int] = []
    residues: list[int] = []
    for i, row in enumerate(data):
        total, start = tuple(map(int, PATTERN.findall(row)))
        mods.append(total)
        residues.append(total - (start + i + 1))

    part1 = chinese_remainder(mods, residues)

    new_len = 11
    mods.append(new_len)
    residues.append(new_len - (len(mods)))

    part2 = chinese_remainder(mods, residues)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
