"""Solve Advent of Code Day 6 Year 2022."""

from aocd import get_data, submit

def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    part1, part2 = None, None
    data = get_data(day=6, year=2022)
    for i, _ in enumerate(data):
        if (not part1) and len(set(data[i:i+4])) == 4:
            part1 = i + 4
        if (not part2) and len(set(data[i:i+14])) == 14:
            part2 = i + 14
            break

    return part1, part2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
