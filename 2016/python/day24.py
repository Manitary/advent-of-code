from collections import defaultdict
from itertools import combinations, permutations
from typing import Generator

from aocd import get_data, submit

DAY = 24
YEAR = 2016

Coords = tuple[int, int]


def neighbours(maze: set[Coords], tile: Coords) -> Generator[Coords, None, None]:
    x, y = tile
    for c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if c in maze:
            yield c


def length_shortest_path_pair(maze: set[Coords], start: Coords, end: Coords) -> int:
    visited: set[Coords] = set()
    queue: list[tuple[Coords, int]] = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current == end:
            return steps
        if current in visited:
            continue
        visited.add(current)
        queue.extend(
            (new, steps + 1) for new in neighbours(maze, current) if new not in visited
        )
    raise ValueError("No path found")


def find_shortest_path(
    start: str, others: set[str], dists: dict[str, dict[str, int]], cycle: bool = False
) -> int:
    best = float("inf")
    for points in permutations(others):
        dist = 0
        for p1, p2 in zip((start,) + points, points + ((start,) if cycle else ())):
            dist += dists[p1][p2]
            if dist > best:
                break
        else:
            best = min(best, dist)
    return int(best)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    targets: dict[str, Coords] = {}

    maze: set[Coords] = set()
    for y, row in enumerate(data.split("\n")):
        for x, char in enumerate(row):
            if char == "#":
                continue
            maze.add((x, y))
            if char != ".":
                targets[char] = (x, y)

    dists: dict[str, dict[str, int]] = defaultdict(dict)
    for t1, t2 in combinations(targets, 2):
        d = length_shortest_path_pair(maze, targets[t1], targets[t2])
        dists[t1][t2] = d
        dists[t2][t1] = d

    start = "0"
    part1 = find_shortest_path(start, set(targets) - {start}, dists)
    part2 = find_shortest_path(start, set(targets) - {start}, dists, cycle=True)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
