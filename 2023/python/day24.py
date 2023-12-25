import itertools
import re
from typing import NamedTuple

from aocd import get_data, submit
from z3 import Real, Solver, sat

DAY = 24
YEAR = 2023
HAIL_RE = re.compile(r"-?\d+")

Hail = NamedTuple(
    "Hail",
    [("x", int), ("y", int), ("z", int), ("vx", int), ("vy", int), ("vz", int)],
)


def rock_coords(hailstones: list[Hail]) -> int:
    solver = Solver()
    x, y, z, vx, vy, vz = map(Real, ("x", "y", "z", "vx", "vy", "vz"))
    for i, h in enumerate(hailstones[:3]):
        t = Real(f"t{i}")
        solver.add(t > 0)
        solver.add(x + vx * t == h.x + h.vx * t)
        solver.add(y + vy * t == h.y + h.vy * t)
        solver.add(z + vz * t == h.z + h.vz * t)
    assert solver.check() == sat
    m = solver.model()
    return sum(m.eval(var).as_long() for var in (x, y, z))


def xy_paths_intersect_future(
    h1: Hail,
    h2: Hail,
    min_coord: int = 200000000000000,
    max_coord: int = 400000000000000,
) -> bool:
    d = h1.vx * h2.vy - h1.vy * h2.vx
    if d == 0:
        return False
    t1 = (h2.vx * (h1.y - h2.y) - h2.vy * (h1.x - h2.x)) / d
    if t1 <= 0:
        return False
    t2 = (h1.x + h1.vx * t1 - h2.x) / h2.vx
    if t2 <= 0:
        return False
    x = h1.x + h1.vx * t1
    if not min_coord <= x <= max_coord:
        return False
    y = h1.y + h1.vy * t1
    if not min_coord <= y <= max_coord:
        return False
    return True


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    hailstones = [Hail(*map(int, HAIL_RE.findall(row))) for row in data.splitlines()]

    part1 = sum(
        xy_paths_intersect_future(h1, h2)
        for h1, h2 in itertools.combinations(hailstones, 2)
    )

    part2 = rock_coords(hailstones)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
