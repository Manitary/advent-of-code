from copy import deepcopy

from aocd import get_data, submit
from intcode import Droid

DAY = 15
YEAR = 2019

Coords = tuple[int, int]


def newCoordinates(coordinates: Coords, direction: int) -> Coords:
    x, y = coordinates
    if direction == 1:
        return (x, y + 1)
    if direction == 2:
        return (x, y - 1)
    if direction == 3:
        return (x - 1, y)
    if direction == 4:
        return (x + 1, y)
    raise ValueError("Invalid direction")


def BFS(start: Droid, explore: bool = False) -> tuple[int, Droid]:
    queue: list[tuple[Coords, int, int, Droid]] = [
        (start.coordinates, 0, i, deepcopy(start)) for i in range(1, 5)
    ]
    visited = {start.coordinates}
    steps = 0
    while queue:
        current, steps, direction, droid = queue.pop(0)
        status = droid.move(direction)
        if (not explore) and status == 2:
            return steps + 1, droid
        if status == 1:
            for new_direction in range(1, 5):
                # Add to visited first to avoid unnecessary deepcopy() calls
                if (
                    new_coordinates := newCoordinates(current, new_direction)
                ) not in visited:
                    visited.add(new_coordinates)
                    queue.append(
                        (new_coordinates, steps + 1, new_direction, deepcopy(droid))
                    )
    return steps + 1, Droid()


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    droid = Droid(data)
    part1, droid = BFS(start=droid)
    part2, _ = BFS(start=droid, explore=True)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
