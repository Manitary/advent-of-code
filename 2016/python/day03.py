from typing import Callable, Generator

from aocd import get_data, submit

DAY = 3
YEAR = 2016


def scan1(data: list[list[int]]) -> Generator[tuple[int, ...], None, None]:
    for row in data:
        yield tuple(row)


def scan2(data: list[list[int]]) -> Generator[tuple[int, int, int], None, None]:
    r, c = 0, 0
    while c < len(data[0]):
        yield data[r][c], data[r + 1][c], data[r + 2][c]
        r += 3
        if r < len(data):
            continue
        r = 0
        c += 1


def count(
    data: list[list[int]],
    scan: Callable[[list[list[int]]], Generator[tuple[int, ...], None, None]],
) -> int:
    return sum(
        t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[2] + t[0] > t[1]
        for t in scan(data)
    )


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [list(map(int, row.split())) for row in data.split("\n")]
    return count(data, scan1), count(data, scan2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
