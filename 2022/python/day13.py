"""Solve Advent of Code Day 13 Year 2022."""

import json
from math import prod

from aocd import get_data, submit

ListInt = int | list["ListInt"]

DIVIDER_PACKETS_SORTED: ListInt = [[[2]], [[6]]]


def compare(elt1: ListInt, elt2: ListInt) -> int:
    """Return the comparison result of the arguments.

    Rules:
    * If both values are integers, the lower integer should come first.
    * If both values are lists, compare the first value of each list, then the second value,
    and so on. If the left list runs out of items first, the inputs are in the right order.
    * If exactly one value is an integer, convert the integer to a list
    which contains that integer as its only value, then retry the comparison.
    """
    match elt1, elt2:
        case [], []:
            return 0
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
    indices = list(range(1, len(DIVIDER_PACKETS_SORTED) + 1))
    for packet in data:
        for i, divider in enumerate(DIVIDER_PACKETS_SORTED):
            if compare(packet, divider) < 0:
                for j in range(i, len(indices)):
                    indices[j] += 1
                break
    part2 = prod(indices)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
