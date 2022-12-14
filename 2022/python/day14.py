"""Solve Advent of Code Day 14 Year 2022."""

import re
from typing import Iterator
from aocd import get_data, submit

START, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def create_rocks(data_rows: str) -> Iterator[tuple[int, int]]:
    """Yield the rocks on the paths of given endpoints.

    Input format:\n
    "$x,$y -> ... -> $x,$y\n
    ...\n
    $x,$y -> ... -> $x,$y"
    """
    for row in data_rows.split("\n"):
        coords = tuple(map(int, re.findall(r"(-?\d+)", row)))
        for x1, y1, x2, y2 in zip(
            coords[::2], coords[1::2], coords[2::2], coords[3::2]
        ):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    yield x1, y
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    yield x, y1


def simulate_sand(
    entrance: tuple[int, int], rocks: set[tuple[int, int]]
) -> tuple[int, int]:
    """Return the counts of sand units when the first one falls off, and the entrance is blocked.

    Rules:
    * Sand starts at the entrance.
    * Sand moves one unit down, or down-left, or down-right; it stops if no moves are possible.
    * The bottom floor is at +2 depth from the lowest rock.

    Return:
    * The number of sand units when the first sand falls of the rocks.
    * The number of sand units when the entrance is blocked by sand, and no more can flow in."""
    sands = set(rocks)
    lowest_rock = max(rock[1] for rock in rocks)
    limit = 2 + lowest_rock
    last_in = None
    moves = [START]
    while moves:
        # Change where to start the simulation based on the last movement of the previous sand unit.
        last_move = moves.pop()
        if last_move == START:
            x, y = entrance
        elif last_move == DOWN:
            y = y - 1
        elif last_move == LEFT:
            x, y = x + 1, y - 1
        elif last_move == RIGHT:
            x, y = x - 1, y - 1
        while True:
            if (x, y + 1) not in sands and y + 1 < limit:
                y += 1
                moves.append(DOWN)
                continue
            if (x - 1, y + 1) not in sands and y + 1 < limit:
                x -= 1
                y += 1
                moves.append(LEFT)
                continue
            if (x + 1, y + 1) not in sands and y + 1 < limit:
                x += 1
                y += 1
                moves.append(RIGHT)
                continue
            break
        if not last_in and y >= lowest_rock:
            last_in = len(sands) - len(rocks)
        sands.add((x, y))
    return last_in, len(sands) - len(rocks)


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=14, year=2022)
    rocks = set(create_rocks(data))
    part1, part2 = simulate_sand(entrance=(500, 0), rocks=rocks)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
