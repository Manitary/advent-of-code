from aocd import get_data, submit
from itertools import chain
DAY = 20
YEAR = 2019

data = get_data(day=DAY, year=YEAR)
data = data.split('\n')

size_y = len(data) - 4
size_x = len(data[0]) - 4
maze = {(x, y) for y, row in enumerate(data[2:-2]) for x, char in enumerate(row[2:-2]) if char == '.'}

def isLetter(char: str) -> bool:
    return char != char.lower()

def getPortals(data: list[str]) -> tuple[dict]:
    outer_portals = {}
    inner_portals = {}
    inner_y_min, _ = next((y, row) for y, row in enumerate(data[2:]) if ' ' in row[2:-2])
    inner_x_min = data[2+inner_y_min][2:].index(' ')
    # Outer teleports
    for x, char in enumerate(data[0][2:]):
        if isLetter(char):
            outer_portals[f"{char}{data[1][2+x]}"] = (x, 0)

    for x, char in enumerate(data[-2][2:]):
        if isLetter(char):
            outer_portals[f"{char}{data[-1][2+x]}"] = (x, size_y - 1)

    for y, char in enumerate([row[0] for row in data[2:]]):
        if isLetter(char):
            outer_portals[f"{char}{data[y+2][1]}"] = (0, y)

    for y, char in enumerate([row[-2] for row in data[2:]]):
        if isLetter(char):
            outer_portals[f"{char}{data[y+2][-1]}"] = (size_x -1, y)

    # Inner teleports
    for x, char in enumerate(data[2 + inner_y_min][2:-2]):
        if isLetter(char) and isLetter(char1 := data[3 + inner_y_min][2+x]):
            inner_portals[f"{char}{char1}"] = (x, inner_y_min - 1)

    for x, char in enumerate(data[-4 - inner_y_min][2:-2]):
        if isLetter(char) and isLetter(char1 := data[-3 - inner_y_min][2+x]):
            inner_portals[f"{char}{char1}"] = (x, size_y - inner_y_min)

    for y, char in enumerate([row[2 + inner_x_min] for row in data[2:-2]]):
        if isLetter(char) and isLetter(char1 := data[y+2][3 + inner_x_min]):
            inner_portals[f"{char}{char1}"] = (inner_x_min - 1, y)

    for y, char in enumerate([row[-4 - inner_x_min] for row in data[2:-2]]):
        if isLetter(char) and isLetter(char1 := data[y+2][-3 - inner_x_min]):
            inner_portals[f"{char}{char1}"] = (size_x - inner_x_min, y)

    return outer_portals, inner_portals

def neighbours(maze: set, coords: tuple[int]) -> set[tuple[int]]:
    x, y = coords
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}.intersection(maze)

def findAdjacent(maze: set, start: tuple[int], portals: dict) -> dict:
    ans = {}
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current in portals and steps > 0:
                ans[current] = steps
            for new in neighbours(maze, current):
                queue.append((new, steps + 1))
    return ans

def getPathsToLabels(maze: set, outer_portals: dict, inner_portals: dict) -> dict:
    paths = {x: {} for x in (set(outer_portals.values()) | set(inner_portals.values()))}
    labels = set.intersection(set(outer_portals), set(inner_portals))
    for label in labels:
        paths[outer_portals[label]][inner_portals[label]] = {'length': 1, 'diff': -1}
        paths[inner_portals[label]][outer_portals[label]] = {'length': 1, 'diff': 1}
    for portal in chain(outer_portals.values(), inner_portals.values()):
        ngbhs = findAdjacent(maze, portal, paths)
        for ngbh, dist in ngbhs.items():
            paths[portal][ngbh] = {'length': dist, 'diff': 0}
            paths[ngbh][portal] = {'length': dist, 'diff': 0}
    return paths

def BFS1(start: tuple[int], end: tuple[int], paths: dict) -> int:
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current == end:
            return steps
        if current not in visited:
            visited.add(current)
            for portal, values in paths[current].items():
                queue.append((portal, steps + values['length']))
            queue.sort(key=lambda x: x[1])

def BFS2(start: tuple[int], end: tuple[int], paths: dict) -> int:
    visited = set()
    queue = [(start, 0, 0)]
    while queue:
        current, steps, depth = queue.pop(0)
        if depth == 0 and current == end:
            return steps
        if (current, depth) not in visited:
            visited.add((current, depth))
            for portal, values in paths[current].items():
                if depth + values['diff'] >= 0:
                    queue.append((portal, steps + values['length'], depth + values['diff']))
            queue.sort(key=lambda x: x[1])

outer_portals, inner_portals = getPortals(data)
paths = getPathsToLabels(maze, outer_portals, inner_portals)

ans1 = BFS1(outer_portals['AA'], outer_portals['ZZ'], paths)
ans2 = BFS2(outer_portals['AA'], outer_portals['ZZ'], paths)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)