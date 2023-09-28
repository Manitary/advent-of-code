"""Solve Advent of Code Day 3 Year 2022."""

from typing import Iterable

from aocd import get_data, submit


def item_priority(char: str) -> int:
    """Return the priority of a letter."""
    return 1 + ord(char) - ord("a") if char.islower() else 27 + ord(char) - ord("A")


def group_priority(*string_list: Iterable[str]) -> int:
    """Return the priority of a list of strings."""
    return item_priority(set.intersection(*(set(x) for x in string_list)).pop())


def string_priority(string: str) -> int:
    """Return the priority of a single string."""
    return group_priority(string[: len(string) // 2], string[len(string) // 2 :])


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=3, year=2022).split()
    part1 = sum(map(string_priority, data))
    part2 = sum(map(group_priority, data[::3], data[1::3], data[2::3]))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
