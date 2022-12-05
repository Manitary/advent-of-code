"""Solve Advent of Code Day 1 Year 2022."""

from aocd import get_data, submit

def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = sorted([sum(map(int, row.split())) for row in get_data(day=1, year=2022).split('\n\n')])
    part1 = data[-1]
    part2 = sum(data[-3:])

    return part1, part2

if __name__ == '__main__':
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
