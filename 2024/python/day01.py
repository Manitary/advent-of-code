from collections import Counter
from itertools import batched
from typing import Iterable

from aocd import get_data, submit

DAY = 1
YEAR = 2024


def distance(t: tuple[int, int]) -> int:
    return abs(t[0] - t[1])


def part_1(data: Iterable[list[int]]) -> int:
    return sum(map(distance, zip(*map(sorted, data))))


def part_2(data: tuple[list[int], ...]) -> int:
    nums = Counter(set(data[0]))
    for i in data[1]:
        nums[i] += 1
    return sum(k * (v - 1) for k, v in nums.items())


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    lists = tuple(zip(*batched(map(int, data.split()), 2)))
    return part_1(lists), part_2(lists)


if __name__ == "__main__":
    part1, part2 = main()
    submit(part1, part="a", day=DAY, year=YEAR)
    submit(part2, part="b", day=DAY, year=YEAR)
