"""Solve Advent of Code Day 24 Year 2022."""
from functools import reduce
from aocd import get_data, submit

SNAFU = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}


def snafu_to_int(snafu: str) -> int:
    """Convert from SNAFU to decimal."""
    return reduce(lambda x, y: 5 * x + y, (SNAFU[x] for x in snafu))


def int_to_snafu(num: int) -> str:
    """Convert from decimal to SNAFU."""
    if num == 0:
        return ""
    for snafu_digit, digit in SNAFU.items():
        if num % 5 == digit % 5:
            return int_to_snafu((num - digit) // 5) + snafu_digit
    raise ValueError(f"Cannot convert {num}")


def main() -> str:
    """Return the solution to part 1."""
    data = get_data(day=25, year=2022)
    return int_to_snafu(sum(map(snafu_to_int, data.split())))


if __name__ == "__main__":
    ans1 = main()
    submit(ans1, part="a")
