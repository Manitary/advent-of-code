"""Solve Advent of Code Day 17 Year 2022."""

from typing import NewType
from itertools import cycle
from aocd import get_data, submit

MIN_X, MAX_X = 1, 7
MIN_Y = 1
OFFSET_X, OFFSET_Y = 3, 4
SHAPES = (
    {(0, x) for x in range(4)},  # I, horizontal
    {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},  # X
    {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)},  # V
    {(y, 0) for y in range(4)},  # I, vertical
    {(0, 0), (0, 1), (1, 0), (1, 1)},  # O
)
Rock = NewType("Rock", set[tuple[int, int]])


def create_rock(shape: int, max_height: int = 0) -> Rock:
    """Return a rock of the given shape at the appropriate height."""
    return {(max_height + OFFSET_Y + y, OFFSET_X + x) for y, x in SHAPES[shape]}


def rock_fall(rock: Rock, rocks: Rock) -> tuple[Rock, bool]:
    """Return the new position of a rock shifting its y-position by 1, and whether it stopped."""
    new = {(y - 1, x) for y, x in rock}
    if any(y < MIN_Y or (y, x) in rocks for y, x in new):
        return rock, True
    return new, False


def rock_shift(rock: Rock, dx: int, rocks: Rock) -> Rock:
    """Return the new position of a rock shifting its x-position by dx."""
    new = {(y, x + dx) for y, x in rock}
    if any(x < MIN_X or x > MAX_X for _, x in new) or any(r in rocks for r in new):
        return rock
    return new


def simulate(data: list[int], num_rocks: int) -> int:
    """Simulate a given number of rocks falling. Return the resulting height."""
    num = 0
    rocks = set()
    rock = create_rock(num)
    max_height = 0
    for d in cycle(data):
        rock = rock_shift(rock, d, rocks)
        rock, locked = rock_fall(rock, rocks)
        if locked:
            max_height = max(max_height, max(y for y, _ in rock))
            rocks.update(rock)
            num += 1
            rock = create_rock(num % 5, max_height)
            if num == num_rocks:
                break
    return max_height


def flood(rocks: Rock, max_height: int) -> frozenset:
    """Return a hashable describing the shape of the surface of the rock formation."""
    visited = set()
    queue = {
        (max_height, x) for x in range(MIN_X, MAX_X + 1) if (max_height, x) not in rocks
    }
    while queue:
        y, x = queue.pop()
        if (y, x) not in visited:
            visited.add((y, x))
            for new in ((y, x - 1), (y, x + 1), (y - 1, x)):
                if (
                    new[0] >= MIN_Y
                    and MIN_X <= new[1] <= MAX_X
                    and new not in visited
                    and new not in rocks
                ):
                    queue.add(new)
    visited = frozenset({(y - max_height, x) for y, x in visited})
    return visited


def simulate2(data: list[int], num_rocks: int) -> int:
    """Simulate a given number of rocks falling. Return the resulting height.

    This time, keep track of possible cycles in the mountain of rocks to skip calculations.
    It will not work if the rocks accumulate on one side, leaving a growing gap on the other."""
    num = 0
    rocks = set()
    rock = create_rock(num)
    max_height = 0
    history = {}
    i = 0
    while True:
        rock = rock_shift(rock, data[i], rocks)
        rock, locked = rock_fall(rock, rocks)
        if locked:
            max_height = max(max_height, max(y for y, _ in rock))
            rocks.update(rock)
            # Track:
            # 1) shape of last locked pieces
            # 2) current position in the list of instructions
            # 3) shape of the hole from the top (flood fill from maximum height)
            if history is not None:
                new_state = (num % len(SHAPES), i, flood(rocks, max_height))
                if new_state in history:
                    old_h, old_n = history[new_state]
                    cycle_length = num - old_n
                    num_cycles = (num_rocks - num) // cycle_length
                    h_gain = (max_height - old_h) * num_cycles
                    num += num_cycles * cycle_length
                    history = None  # Stop tracking once a cycle is found.
                else:
                    history[new_state] = (max_height, num)
            num += 1
            rock = create_rock(num % len(SHAPES), max_height)
            if num == num_rocks:
                break
        i = (i + 1) % len(data)
    return max_height + h_gain


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=17, year=2022)
    data = tuple(map(lambda x: -1 if x == "<" else 1, data))
    part1 = simulate(data, 2022)
    part2 = simulate2(data, 1000000000000)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
