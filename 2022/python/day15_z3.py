"""Solve Advent of Code Day 15 Year 2022."""

import re

import z3
from aocd import get_data, submit
from day15 import parse_input, row_span

TARGET_ROW = 2000000
BOX_MIN, BOX_MAX = 0, 4000000


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=15, year=2022)
    beacons, sensors = parse_input(data)
    solver = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    solver.add(BOX_MIN <= x)
    solver.add(x <= BOX_MAX)
    solver.add(BOX_MIN <= y)
    solver.add(y <= BOX_MAX)
    for (xs, ys), r in sensors.items():
        solver.add(z3.Abs(xs - x) + z3.Abs(ys - y) > r)
    part1_ranges = row_span(y=TARGET_ROW, sensors=sensors, merge=True)
    part1 = sum(right - left + 1 for left, right in part1_ranges) - sum(
        1
        for xb, yb in beacons
        if yb == TARGET_ROW and any(a <= xb <= b for a, b in part1_ranges)
    )
    solver.check()
    col, row = map(int, re.findall(r"(-?\d+)", str(solver.model())))
    part2 = col * 4000000 + row
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
