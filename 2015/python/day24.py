from itertools import combinations
from math import prod

from aocd import get_data, submit

DAY = 24
YEAR = 2015


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    weights = {int(x) for x in data.split()}
    target = sum(weights) // 3
    min_size = len(weights)
    best = float("inf")
    for i in range(len(weights)):
        if i > min_size:
            break
        for g1 in (set(y) for y in combinations(weights, i) if sum(y) == target):
            if prod(g1) >= best:
                continue
            if any(
                sum(g2) == target
                for j in range(len(weights) - i)
                for g2 in combinations(weights - g1, j)
            ):
                min_size = i
                best = min(best, prod(g1))

    part1 = best

    min_size = len(weights)
    best = float("inf")
    target = sum(weights) // 4
    for i in range(len(weights) - 3):
        if i > min_size:
            break
        for g1 in (set(y) for y in combinations(weights, i) if sum(y) == target):
            if prod(g1) >= best:
                continue
            for g2 in (
                set(x)
                for j in range(len(weights) - i - 2)
                for x in combinations(weights - g1, j)
                if sum(x) == target
            ):
                if any(
                    sum(g3) == target
                    for k in range(len(weights) - i - len(g2) - 1)
                    for g3 in combinations(weights - g1 - g2, k)
                    if sum(g3) == target
                ):
                    min_size = i
                    best = min(best, prod(g1))
                break

    part2 = best
    return int(part1), int(part2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
