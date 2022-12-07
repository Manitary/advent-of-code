"""Solve Advent of Code Day 2 Year 2022."""

from aocd import get_data, submit

RPS_1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
RPS_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=2, year=2022).split("\n")
    part1 = sum(map(lambda x: RPS_1[x], data))
    part2 = sum(map(lambda x: RPS_2[x], data))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
