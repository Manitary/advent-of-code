import itertools
from typing import Sequence

from aocd import get_data, submit

DAY = 11
YEAR = 2023

type Coord = tuple[int, int]


def galaxies_between(g1: int, g2: int, galaxies: Sequence[int]) -> int:
    count = 0
    for g in galaxies:
        if g <= g1:
            continue
        if g > g2:
            break
        count += 1
    return count


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    galaxies = {
        (r, c) for r, row in enumerate(data) for c, elt in enumerate(row) if elt == "#"
    }

    occupied_rows = sorted({g[0] for g in galaxies})
    occupied_cols = sorted({g[1] for g in galaxies})

    part1, part2 = 0, 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        min_r, max_r = sorted((g1[0], g2[0]))
        min_c, max_c = sorted((g1[1], g2[1]))
        row_extra = galaxies_between(min_r, max_r, occupied_rows)
        col_extra = galaxies_between(min_c, max_c, occupied_cols)
        part1 += 2 * (max_r - min_r + max_c - min_c) - (row_extra + col_extra)
        part2 += 1000000 * (max_r - min_r + max_c - min_c) - (1000000 - 1) * (
            row_extra + col_extra
        )

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
