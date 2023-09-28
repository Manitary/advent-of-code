"""Solve Advent of Code Day 18 Year 2022."""

from typing import Iterator

from aocd import get_data, submit

Point = tuple[int, int, int]


def ngbh(x: int, y: int, z: int) -> Iterator[Point]:
    """Yield the orthogonally adjacent coordinates."""
    for c in (
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ):
        yield c


def get_exterior(points: set[Point]) -> set[Point]:
    """Return the exterior of the set of points within their bounding box."""
    x0 = min(x for x, _, _ in points)
    x1 = max(x for x, _, _ in points)
    y0 = min(y for _, y, _ in points)
    y1 = max(y for _, y, _ in points)
    z0 = min(z for _, _, z in points)
    z1 = max(z for _, _, z in points)
    exterior: set[Point] = set()
    queue = {(x0 - 1, y0 - 1, z0 - 1)}
    while queue:
        curr = queue.pop()
        if curr in points:
            continue
        exterior.add(curr)
        for new in ngbh(*curr):
            x, y, z = new
            if (
                new not in exterior
                and new not in points
                and x0 - 1 <= x <= x1 + 1
                and y0 - 1 <= y <= y1 + 1
                and z0 - 1 <= z <= z1 + 1
            ):
                queue.add(new)
    return exterior


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=18, year=2022)
    data = set(tuple(map(int, row.split(","))) for row in data.split())
    part1 = sum(6 - len(set(ngbh(*point)).intersection(data)) for point in data)
    exterior = get_exterior(data)
    part2 = sum(len(set(ngbh(*point)).intersection(exterior)) for point in data)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
