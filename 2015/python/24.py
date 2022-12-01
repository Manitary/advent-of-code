from aocd import get_data, submit
from itertools import combinations
from math import prod
DAY = 24
YEAR = 2015

data = get_data(day=DAY, year=YEAR)
weights = {int(x) for x in data.split()}

target = sum(weights) // 3

min_size = len(weights)
best = float('inf')
for i in range(len(weights)):
    for g1 in sorted(list({frozenset(x) for x in combinations(weights, i)}), reverse=True):
        if sum(g1) == target:
            if i <= min_size and prod(g1) < best:
                for j in range(len(weights) - i):
                    for g2 in {frozenset(x) for x in combinations(weights - g1, j)}:
                        if sum(g2) == target:
                            min_size = i
                            best = min(best, prod(g1))
                            break
                    else:
                        continue
                    break
    if i > min_size:
        break

ans1 = best
submit(ans1, part="a", day=DAY, year=YEAR)

min_size = len(weights)
best = float('inf')
target = sum(weights) // 4
for i in range(len(weights) - 3):
    for g1 in {frozenset(x) for x in combinations(weights, i)}:
        if sum(g1) == target and prod(g1) < best:
            for j in range(len(weights) - i - 2):
                for g2 in {frozenset(x) for x in combinations(weights - g1, j)}:
                    if sum(g2) == target:
                        for k in range(len(weights) - i - j - 1):
                            for g3 in {frozenset(x) for x in combinations(weights - g1 - g2, k)}:
                                if sum(g3) == target:
                                    min_size = i
                                    best = min(best, prod(g1))
                                    break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                else:
                    continue
                break
    if i > min_size:
        break

ans2 = best
submit(ans2, part="b", day=DAY, year=YEAR)