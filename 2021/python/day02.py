"""Solve Advent of Code Day 2 Year 2021."""

from aocd import get_data, submit


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=2, year=2021).split("\n")
    horizontal_position, depth, depth_1, aim = 0, 0, 0, 0
    for row in data:
        command, value = row.split()
        value = int(value)
        if command.startswith("f"):
            horizontal_position += value
            depth_1 += aim * value
        elif command.startswith("u"):
            depth -= value
            aim -= value
        elif command.startswith("d"):
            depth += value
            aim += value
    part1 = horizontal_position * depth
    part2 = horizontal_position * depth_1

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
