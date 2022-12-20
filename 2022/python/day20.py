"""Solve Advent of Code Day 20 Year 2022."""

from itertools import chain, repeat
from collections import deque
from aocd import get_data, submit

DECRYPTION_KEY = 811589153


class Num:
    """A wrapper to distinguish copies of the same number."""

    def __init__(self, n: int) -> None:
        self.num = n


def grove_coordinates(original: list[int], n_mix: int = 1, key: int = 1) -> int:
    """Return the grove coordinates of a list of numbers."""
    original = [Num(x * key) for x in original]
    nums = deque(original)
    for n in chain(*repeat(original, n_mix)):
        idx = nums.index(n)
        nums.rotate(-idx)
        nums.popleft()
        nums.rotate(-n.num)
        nums.appendleft(n)
    nums = [x.num for x in nums]
    idx = nums.index(0)
    return sum(nums[(idx + i) % len(nums)] for i in (1000, 2000, 3000))


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = tuple(map(int, get_data(day=20, year=2022).split()))
    part1 = grove_coordinates(data)
    part2 = grove_coordinates(data, 10, DECRYPTION_KEY)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    print(ans1, ans2)
    submit(ans1, part="a")
    submit(ans2, part="b")
