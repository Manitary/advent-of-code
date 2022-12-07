from aocd import get_data, submit
from itertools import combinations, permutations
from collections import defaultdict

DAY = 24
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

maze = set()
targets = {}

for y, row in enumerate(data.split("\n")):
    for x, char in enumerate(row):
        if char == "#":
            continue
        else:
            maze.add((x, y))
            if char != ".":
                targets[char] = (x, y)


def neighbours(tile: tuple[int]):
    x, y = tile
    for c in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}:
        if c in maze:
            yield c


def lengthShortestPathPair(a: str, b: str):
    visited = set()
    start, end = targets[a], targets[b]
    queue = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current == end:
            return steps
        if current not in visited:
            visited.add(current)
            for new in neighbours(current):
                if new not in visited:
                    queue.append((new, steps + 1))


dists = defaultdict(dict)
for t1, t2 in combinations(targets, 2):
    d = lengthShortestPathPair(t1, t2)
    dists[t1][t2] = d
    dists[t2][t1] = d


def findShortestPath(start: str, cycle: bool = False):
    best = float("inf")
    for points in permutations(set(targets.keys()) - {start}):
        dist = 0
        for p1, p2 in zip((start,) + points, points + ((start,) if cycle else ())):
            dist += dists[p1][p2]
            if dist > best:
                break
        else:
            best = min(best, dist)
    return best


start = "0"
ans1 = findShortestPath(start)
ans2 = findShortestPath(start, cycle=True)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
