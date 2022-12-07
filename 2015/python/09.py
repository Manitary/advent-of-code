from aocd import get_data, submit
from itertools import permutations

DAY = 9
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")

dists = {}
cities = set()
for row in data:
    c1, c2, d = tuple(row.split()[::2])
    cities.add(c1)
    cities.add(c2)
    dists[frozenset((c1, c2))] = int(d)

ans1, ans2 = float("inf"), 0
for path in permutations(cities):
    dist = sum(dists[frozenset(edge)] for edge in zip(path, path[1:]))
    if dist < ans1:
        ans1 = dist
    if dist > ans2:
        ans2 = dist

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
