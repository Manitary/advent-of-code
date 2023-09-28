"""Solve Advent of Code Day 23 Year 2022."""

from collections import defaultdict, deque
from itertools import count
from typing import Self

from aocd import get_data, submit

Elf = tuple[int, int]

INSPECTIONS = deque(
    [
        ((-1, 0), (-1, 1), (-1, -1)),
        ((1, 0), (1, 1), (1, -1)),
        ((0, -1), (-1, -1), (1, -1)),
        ((0, 1), (-1, 1), (1, 1)),
    ]
)

DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def move(r: int, c: int, dr: int, dc: int) -> Elf:
    """Return (r, c) + (dr, dc)"""
    return r + dr, c + dc


class Elves:
    """A bunch of elves.

    Attributes:
        elves: a set of elves' positions using coordinates (r, c).
        directions: a deque of directions each elf checks in order to decide the next move.
    """

    def __init__(self, elves: set[Elf]) -> None:
        self.elves = elves
        self.directions = INSPECTIONS

    @classmethod
    def from_data(cls, grid: str) -> Self:
        """Create a bunch of elves from a drawn map."""
        return Elves(
            elves={
                (row, col)
                for row, line in enumerate(grid.split())
                for col, char in enumerate(line)
                if char == "#"
            }
        )

    @property
    def bounds(self) -> tuple[int, int, int, int]:
        """Return the min/max row/col occupied by the elves."""
        min_row = min(row for row, _ in self.elves)
        max_row = max(row for row, _ in self.elves)
        min_col = min(col for _, col in self.elves)
        max_col = max(col for _, col in self.elves)
        return min_row, max_row, min_col, max_col

    @property
    def empty_space(self) -> int:
        """Return the number of unoccupied tiles within the smallest bounding box."""
        min_row, max_row, min_col, max_col = self.bounds
        area = (max_row - min_row + 1) * (max_col - min_col + 1)
        return area - len(self.elves)

    def __str__(self) -> str:
        min_row, max_row, min_col, max_col = self.bounds
        ans = (
            "\n".join(
                (
                    "".join(
                        (
                            "#" if (row, col) in self.elves else "."
                            for col in range(min_col, max_col + 1)
                        )
                    )
                    for row in range(min_row, max_row + 1)
                )
            )
            + "\n"
        )
        return ans

    def update_directions(self) -> None:
        """Update the order of directions to check."""
        self.directions.rotate(-1)

    @property
    def planned_moves(self) -> dict[Elf, set[Elf]]:
        """Return a dict: tile -> elves who want to move to the tile."""
        plans: dict[Elf, set[Elf]] = defaultdict(set)
        for elf in self.elves:
            if all(move(*elf, *d) not in self.elves for d in DIRECTIONS):
                plans[elf].add(elf)
            else:
                for directions in self.directions:
                    if all(move(*elf, *d) not in self.elves for d in directions):
                        plans[move(*elf, *directions[0])].add(elf)
                        break
                else:
                    plans[elf].add(elf)
        return plans

    @property
    def new_positions(self) -> set[Elf]:
        """Return the new elves' positions based on the plans."""
        plans = self.planned_moves
        single = {tile for tile, elves in plans.items() if len(elves) == 1}
        multiple = {
            elf for _, elves in plans.items() for elf in elves if len(elves) > 1
        }
        return single | multiple

    def move(self) -> int:
        """Update the elves' positions and instructions; return the number of elves who moved."""
        new_elves = self.new_positions
        num_moved = len(new_elves.difference(self.elves))
        self.elves = new_elves
        self.update_directions()
        return num_moved


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    part1, part2 = 0, 0
    data = get_data(day=23, year=2022)
    elves = Elves.from_data(data)
    for i in count(start=1):
        num_moved = elves.move()
        if num_moved == 0:
            part2 = i
            break
        if i == 10:
            part1 = elves.empty_space

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
