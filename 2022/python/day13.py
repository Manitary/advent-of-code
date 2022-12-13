"""Solve Advent of Code Day 13 Year 2022."""

import json
from functools import cmp_to_key
from math import prod
from aocd import get_data, submit

DIVIDER_PACKETS = [[[2]], [[6]]]


def compare(elt1: list[int] | int, elt2: list[int] | int) -> int:
    """Return the comparison result of the arguments.

    Rules:
    * If both values are integers, the lower integer should come first.
    * If both values are lists, compare the first value of each list, then the second value,
    and so on. If the left list runs out of items first, the inputs are in the right order.
    * If exactly one value is an integer, convert the integer to a list
    which contains that integer as its only value, then retry the comparison.
    """
    match elt1, elt2:
        case [] | None, _:
            return -1
        case _, [] | None:
            return 1
        case [*x], [*y]:
            return compare(x[0], y[0]) or compare(x[1:], y[1:])
        case [*x], y:
            return compare(x, [y])
        case x, [*y]:
            return compare([x], y)
        case x, y:
            return x - y


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=13, year=2022)
    data = [json.loads(row) for row in data.split()]
    part1 = sum(
        i
        for i, (a, b) in enumerate(zip(data[::2], data[1::2]), 1)
        if compare(a, b) <= 0
    )
    data.extend(DIVIDER_PACKETS)
    data.sort(key=cmp_to_key(compare))
    part2 = prod(data.index(packet) + 1 for packet in DIVIDER_PACKETS)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
