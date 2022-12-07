"""Solve Advent of Code Day 1 Year 2021."""

from aocd import get_data, submit


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = tuple(map(int, get_data(day=1, year=2021).split()))
    part1 = sum(map(lambda x: x[0] < x[1], zip(data, data[1:])))
    part2 = sum(map(lambda x: x[0] < x[1], zip(data, data[3:])))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
