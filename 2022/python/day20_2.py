"""Solve Advent of Code Day 20 Year 2022."""

from itertools import chain, repeat
from typing import Sequence

from aocd import get_data, submit


DAY = 20
YEAR = 2022

DECRYPTION_KEY = 811589153


def grove_coordinates(nums: Sequence[int], n_mix: int = 1, key: int = 1) -> int:
    """Return the grove coordinates of a list of numbers."""
    if key != 1:
        nums = [x * key for x in nums]
    l = len(nums)
    indices = list(range(l))
    for i in chain(*repeat(range(l), n_mix)):
        indices.pop(j := indices.index(i))
        indices.insert((j + nums[i]) % (l - 1), i)
    start = indices.index(nums.index(0))
    return sum(nums[indices[(start + offset) % l]] for offset in (1000, 2000, 3000))


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = tuple(map(int, get_data(day=DAY, year=YEAR).split()))
    part1 = grove_coordinates(data)
    part2 = grove_coordinates(data, 10, DECRYPTION_KEY)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
