from aocd import get_data, submit
from hashlib import md5
from numpy import array, array_equal
from collections import deque

DAY = 17
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

SIZE = 4
START = array((1, 1))
END = array((SIZE, SIZE))
OPEN = {"b", "c", "d", "e", "f"}
DIRECTIONS = tuple(map(lambda x: array(x, int), ((0, -1), (0, 1), (-1, 0), (1, 0))))
DIRECTIONS_CODE = ("U", "D", "L", "R")


def checkDoors(path: str):
    return tuple(
        True if char in OPEN else False
        for char in md5(f"{data}{path}".encode()).hexdigest()[:4]
    )


def neighbours(cell: tuple, path: str = ""):
    doors = checkDoors(path)
    for i, move in enumerate(DIRECTIONS):
        if doors[i] and 0 < (cell + move)[0] <= SIZE and 0 < (cell + move)[1] <= SIZE:
            yield (cell + move, f"{path}{DIRECTIONS_CODE[i]}")


def findShortestPath(cell: tuple, target: tuple):
    visited = set()
    queue = deque([(cell, "")])
    while queue:
        current_cell, current_path = queue.popleft()
        if array_equal(current_cell, target):
            return current_path
        cell_info = (tuple(current_cell), checkDoors(current_path))
        if cell_info not in visited:
            visited.add(cell_info)
            for neighbour in neighbours(current_cell, current_path):
                queue.append(neighbour)


def findLongestPath(cell: tuple, target: tuple):
    queue = deque([(cell, "")])
    best = 0
    while queue:
        current_cell, current_path = queue.popleft()
        if array_equal(current_cell, target):
            best = max(best, len(current_path))
        else:
            for neighbour in neighbours(current_cell, current_path):
                queue.append(neighbour)
    return best


ans1 = findShortestPath(START, END)
ans2 = findLongestPath(START, END)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
