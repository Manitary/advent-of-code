from aocd import get_data, submit
from intcode import Droid
from copy import deepcopy
DAY = 15
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

def newCoordinates(coordinates: tuple[int], direction: int):
    x, y = coordinates
    if direction == 1:
        return (x, y+1)
    if direction == 2:
        return (x, y-1)
    if direction == 3:
        return (x-1, y)
    if direction == 4:
        return (x+1, y)

def BFS(start: Droid, explore: bool = False):
    queue = [(start.coordinates, 0, i, deepcopy(start)) for i in range(1, 5)]
    visited = set()
    visited.add(start.coordinates)
    while queue:
        current, steps, direction, droid = queue.pop(0)
        status = droid.move(direction)
        if (not explore) and status == 2:
            return steps + 1, droid
        if status == 1:
            for new_direction in range(1, 5):
                # Add to visited first to avoid unnecessary deepcopy() calls
                if (new_coordinates := newCoordinates(current, new_direction)) not in visited:
                    visited.add(new_coordinates)
                    queue.append((new_coordinates, steps + 1, new_direction, deepcopy(droid)))
    return steps + 1

droid = Droid(data)
ans1, droid = BFS(start=droid)
ans2 = BFS(start=droid, explore=True)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)