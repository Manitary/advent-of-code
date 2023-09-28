from collections import deque
from hashlib import md5
from typing import Generator

import numpy as np
from aocd import get_data, submit
from numpy.typing import NDArray

DAY = 17
YEAR = 2016

Coords = NDArray[np.uint]


SIZE = 4
START = np.array((1, 1))
END = np.array((SIZE, SIZE))
OPEN = {"b", "c", "d", "e", "f"}
DIRECTIONS = tuple(map(lambda x: np.array(x, int), ((0, -1), (0, 1), (-1, 0), (1, 0))))
DIRECTIONS_CODE = ("U", "D", "L", "R")


def check_doors(data: str, path: str) -> tuple[bool, ...]:
    return tuple(char in OPEN for char in md5(f"{data}{path}".encode()).hexdigest()[:4])


def neighbours(
    cell: Coords, data: str, path: str = ""
) -> Generator[tuple[Coords, str], None, None]:
    doors = check_doors(data, path)
    for i, move in enumerate(DIRECTIONS):
        if doors[i] and 0 < (cell + move)[0] <= SIZE and 0 < (cell + move)[1] <= SIZE:
            yield (cell + move, f"{path}{DIRECTIONS_CODE[i]}")


def find_shortest_path(data: str, cell: Coords, target: Coords) -> str:
    visited: set[tuple[tuple[int, ...], tuple[bool, ...]]] = set()
    queue: deque[tuple[Coords, str]] = deque([(cell, "")])
    while queue:
        current_cell, current_path = queue.popleft()
        if np.array_equal(current_cell, target):
            return current_path
        cell_info = (tuple(current_cell), check_doors(data, current_path))
        if cell_info in visited:
            continue
        visited.add(cell_info)
        queue.extend(neighbours(current_cell, data, current_path))
    raise ValueError("No path found")


def find_longest_path(data: str, cell: Coords, target: Coords) -> int:
    queue: deque[tuple[Coords, str]] = deque([(cell, "")])
    best = 0
    while queue:
        current_cell, current_path = queue.popleft()
        if np.array_equal(current_cell, target):
            best = max(best, len(current_path))
        else:
            queue.extend(neighbours(current_cell, data, current_path))
    return best


def main() -> tuple[str, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = find_shortest_path(data, START, END)
    part2 = find_longest_path(data, START, END)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
