"""Solve Advent of Code Day 12 Year 2022."""

from typing import Iterator
from collections import deque
from aocd import get_data, submit


def height(letter: str) -> int:
    """Return the height represented by a letter on the map."""
    if letter == "S":
        return 0
    if letter == "E":
        return ord("z") - ord("a")
    return ord(letter) - ord("a")


def ngbh_orthogonal(coordinates: tuple[int, int]) -> Iterator[tuple[int, int]]:
    """Return the orthogonal neighbours of a pair of 2d-coordinates."""
    x, y = coordinates
    for coords in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        yield coords


def bfs(
    grid: dict[tuple[int, int], int], start: set[tuple[int, int]], goal: tuple[int, int]
) -> int:
    """Do a BFS and return the minimum path length from any of the starting points to the goal."""
    visited = set()
    queue = deque(((coords, 0) for coords in start))
    while queue:
        current, steps = queue.popleft()
        if current == goal:
            return steps
        if current not in visited:
            visited.add(current)
            for ngbh in ngbh_orthogonal(current):
                if (
                    ngbh not in visited
                    and 0 <= grid.get(ngbh, -1) <= grid.get(current) + 1
                ):
                    queue.append((ngbh, steps + 1))


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=12, year=2022)
    s_coords = data.index("S")
    e_coords = data.index("E")
    data = data.split("\n")
    x_size = len(data[0]) + 1
    s_coords = (s_coords // x_size, s_coords % x_size)
    e_coords = (e_coords // x_size, e_coords % x_size)
    grid = {
        (x, y): height(char) for x, row in enumerate(data) for y, char in enumerate(row)
    }
    part1 = bfs(grid=grid, start={s_coords}, goal=e_coords)
    lowest_coords = {coords for coords, value in grid.items() if value == 0}
    part2 = bfs(grid=grid, start=lowest_coords, goal=e_coords)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
