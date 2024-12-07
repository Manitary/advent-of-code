from itertools import product
from operator import add, mul
from typing import Callable

from aocd import get_data, submit

DAY = 7
YEAR = 2024

op_map = {
    "+": add,
    "*": mul,
}


def join(x: int, y: int) -> int:
    return int(x * 10 ** len(f"{y}") + y)


op_map_2 = op_map | {"|": join}


def is_valid(row: str, rules: dict[str, Callable[[int, int], int]]) -> bool:
    n = row.split()
    total = int(n[0][:-1])
    others = tuple(map(int, n[1:]))
    num_ops = len(others) - 1
    for ops in product(rules.keys(), repeat=num_ops):
        ans = others[0]
        for i, o in enumerate(ops):
            ans = rules[o](ans, others[i + 1])
        if ans == total:
            return True
    return False


def part_1(data: list[str]):
    return sum(int(row.split(":")[0]) for row in data if is_valid(row, op_map))


def part_2(data: list[str]):
    return sum(int(row.split(":")[0]) for row in data if is_valid(row, op_map_2))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    return part_1(data), part_2(data)


if __name__ == "__main__":
    part1, part2 = main()
    print(part1)
    submit(part1, part="a", day=DAY, year=YEAR)
    submit(part2, part="b", day=DAY, year=YEAR)
