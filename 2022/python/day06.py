"""Solve Advent of Code Day 6 Year 2022."""

from aocd import get_data, submit


def find_marker(string: str, length: int, start: int = 0) -> tuple[int, int]:
    """
    Return the first and last index of the start-of-packet marker of given length.
    The search begins from the given start index.
    """
    for i in range(start, len(string) - length):
        if len(set(string[i : i + length])) == length:
            return i, i + length
    return None


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=6, year=2022)
    start, part1 = find_marker(data, 4)
    _, part2 = find_marker(data, 14, start)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
