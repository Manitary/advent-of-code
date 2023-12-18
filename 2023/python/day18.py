from typing import Iterable

from aocd import get_data, submit

DAY = 18
YEAR = 2023


type Coord = tuple[int, int]

DIRS = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
DIRS_STR = "RDLU"


def solve(instructions: Iterable[tuple[str, int]]) -> int:
    # Shoelace formula + Pick's theorem
    area = 0
    perimeter_points = 0
    curr = (0, 0)
    for ds, n in instructions:
        d = DIRS[ds]
        new = (curr[0] + d[0] * n, curr[1] + d[1] * n)
        area += (curr[1] + new[1]) * (curr[0] - new[0])
        perimeter_points += n
        curr = new
    area = abs(area) // 2
    inner_points = area + 1 - perimeter_points // 2
    return perimeter_points + inner_points


def parse_1(instruction: str) -> tuple[str, int]:
    d, n, _ = instruction.split()
    return d, int(n)


def parse_2(instruction: str) -> tuple[str, int]:
    _, _, code = instruction.split()
    return DIRS_STR[int(code[-2])], int(code[2:-2], 16)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    part1 = solve(map(parse_1, data))
    part2 = solve(map(parse_2, data))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
