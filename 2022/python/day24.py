"""Solve Advent of Code Day 24 Year 2022."""

from collections import defaultdict
from typing import Self

from aocd import get_data, submit

Coord = tuple[int, int]
Blizzard = dict[Coord, set[Coord]]

DIRECTIONS_BLIZZARD: dict[str, Coord] = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}
DIRECTIONS_PLAYER: set[Coord] = {(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)}


class Grid:
    """A blizzard and its walls.

    Attributes:
        blizzard_data: a dict mapping coordinates occupied by blizzard
            -> direction of each unit of blizzard at the coordinates.
        walls: a set of the coordinates occupied by walls;
            include additional walls blocking the entrances.
        rows: number of rows.
        cols: number of columns."""

    def __init__(
        self, blizzard: Blizzard, walls: set[Coord], rows: int, cols: int
    ) -> None:
        self.blizzard_data = blizzard
        self.walls: set[Coord] = walls | {(-2, 0), (rows + 1, cols - 1)}
        self.rows = rows
        self.cols = cols

    def update(self) -> None:
        """Update the blizzard after one unit of time."""
        new_blizzard: Blizzard = defaultdict(set)
        for (r, c), directions in self.blizzard_data.items():
            for dr, dc in directions:
                new_blizzard[((r + dr) % self.rows, (c + dc) % self.cols)].add((dr, dc))
        self.blizzard_data = new_blizzard

    @property
    def blizzard(self) -> set[Coord]:
        """Return the coordinates occupied by blizzard."""
        return set(self.blizzard_data.keys())

    @classmethod
    def from_data(cls, data: list[str]) -> Self:
        """Create a grid from the given data."""
        rows, cols = len(data) - 2, len(data[0]) - 2
        walls: set[Coord] = set()
        blizzard: Blizzard = defaultdict(set)
        for row, line in enumerate(data, -1):
            for col, char in enumerate(line, -1):
                if char == "#":
                    walls.add((row, col))
                elif char != ".":
                    blizzard[(row, col)].add(DIRECTIONS_BLIZZARD[char])
        return Grid(blizzard=blizzard, walls=walls, rows=rows, cols=cols)


def bfs(grid: Grid, start: Coord, goal: Coord) -> int:
    """Return the minimum distance from start to goal.

    After each step, the current position(s) cannot overlap with any unit of blizzard.
    """
    steps = 0
    queue: set[Coord] = {start}
    while goal not in queue:
        steps += 1
        grid.update()
        queue = {(r + dr, c + dc) for r, c in queue for dr, dc in DIRECTIONS_PLAYER}
        queue -= grid.walls | grid.blizzard
    return steps


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=24, year=2022)
    grid = Grid.from_data(data.split())
    start = (-1, 0)
    end = (grid.rows, grid.cols - 1)
    part1 = bfs(grid, start, end)
    part2 = part1 + bfs(grid, end, start) + bfs(grid, start, end)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
