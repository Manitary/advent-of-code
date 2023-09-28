from itertools import product
from typing import TypeVar

from aocd import get_data, submit

DAY = 2
YEAR = 2016

Coords = tuple[int, int]
T = TypeVar("T")

PAD1: dict[Coords, int] = {
    (x, y): 3 * y + x + 1 for x, y in product(range(3), repeat=2)
}

PAD2: dict[Coords, int | str] = {
    (0, 2): 5,
    (1, 1): 2,
    (1, 2): 6,
    (1, 3): "A",
    (2, 0): 1,
    (2, 1): 3,
    (2, 2): 7,
    (2, 3): "B",
    (2, 4): "D",
    (3, 1): 4,
    (3, 2): 8,
    (3, 3): "C",
    (4, 2): 9,
}


def num(x: int, y: int, pad: dict[Coords, T]) -> T:
    return pad[(x, y)]


def move(
    x: int, y: int, direction: str, pad: dict[Coords, int | str] | dict[Coords, int]
) -> tuple[int, int]:
    x1, y1 = x, y
    match direction:
        case "U":
            y1 -= 1
        case "D":
            y1 += 1
        case "L":
            x1 -= 1
        case "R":
            x1 += 1
        case _:
            raise ValueError("Invalid direction")
    if (x1, y1) in pad:
        return x1, y1
    return x, y


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR).split()
    part1, part2 = "", ""
    x1, y1, x2, y2 = 1, 1, 0, 2
    for line in data:
        for c in line:
            x1, y1 = move(x1, y1, c, PAD1)
            x2, y2 = move(x2, y2, c, PAD2)
        part1 += str(PAD1[(x1, y1)])
        part2 += str(PAD2[(x2, y2)])
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
