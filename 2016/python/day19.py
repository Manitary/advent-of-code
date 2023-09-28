from math import log

from aocd import get_data, submit

DAY = 19
YEAR = 2016


def solve_1(num: int) -> int:
    return (num << 1) & ~(1 << num.bit_length()) | 1


def solve_2(num: int) -> int:
    power = 3 ** int(log(num, 3))
    residue = num - power
    if residue == 0:
        return power
    if residue < power:
        return residue
    if residue > power:
        return residue + 1
    raise ValueError("Invalid input")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = int(data)
    part1 = solve_1(data)
    part2 = solve_2(data)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
