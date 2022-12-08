"""Solve Advent of Code Day 8 Year 2022."""

from itertools import product
from aocd import get_data, submit
import numpy


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=8, year=2022)
    forest = numpy.array(tuple(tuple(row) for row in data.split("\n")), int)
    part1 = numpy.zeros(forest.shape, int)
    part2 = numpy.ones(forest.shape, int)
    size_x, size_y = forest.shape
    part1[0] = part1[-1] = numpy.ones(size_y, int)
    part1[:, 0] = part1[:, -1] = numpy.ones(size_x, int)
    # The outer ring of part2 should be 0s, but it does not affect the results.
    for _ in range(4):
        for x, y in product(range(1, size_x - 1), range(1, size_y - 1)):
            next_taller = size_y - y
            for y_ in range(y + 1, size_y):
                if forest[x, y_] >= forest[x, y]:
                    next_taller = y_ - y
                    break
            if next_taller == size_y - y:
                part1[x, y] = 1
                part2[x, y] *= next_taller - 1
            else:
                part2[x, y] *= next_taller
        forest, part1, part2 = map(numpy.rot90, (forest, part1, part2))

    return part1.sum(), numpy.amax(part2)


# A more NumPy way, but ~20x slower due to the genexpr calls in the innermost loop.
def main2() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=8, year=2022)
    forest = numpy.array(tuple(tuple(row) for row in data.split("\n")), int)
    part1 = numpy.zeros(forest.shape, int)
    part2 = numpy.ones(forest.shape, int)
    for _ in range(4):
        for x, y in numpy.ndindex(forest.shape):
            is_shorter = (forest < forest[x, y])[x, y + 1 :]
            part1[x, y] |= all(is_shorter)
            part2[x, y] *= next(
                (i + 1 for i, x in enumerate(is_shorter) if not x), len(is_shorter)
            )

        forest, part1, part2 = map(numpy.rot90, (forest, part1, part2))

    return part1.sum(), numpy.amax(part2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
