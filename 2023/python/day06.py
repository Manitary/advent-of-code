import math

from aocd import get_data, submit

DAY = 6
YEAR = 2023


def num_winning_times(time: int, distance: int) -> int:
    """Return the number of integer solutions of `(t-x)x > d`."""
    root_discriminant = (time**2 - 4 * distance) ** (1 / 2)
    t0 = (time - root_discriminant) / 2
    t1 = (time + root_discriminant) / 2
    return math.ceil(t1) - int(t0) - 1


def parse_part_1(data: list[str]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    times = tuple(map(int, data[0].split()[1:]))
    records = tuple(map(int, data[1].split()[1:]))
    return times, records


def parse_part_2(data: list[str]) -> tuple[int, int]:
    t = int("".join(data[0].split()[1:]))
    d = int("".join(data[1].split()[1:]))
    return t, d


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    part1 = math.prod(num_winning_times(t, d) for t, d in zip(*parse_part_1(data)))
    part2 = num_winning_times(*parse_part_2(data))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
