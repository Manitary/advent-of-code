from aocd import get_data, submit
from math import prod
from re import findall

DAY = 23
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

pattern1 = r"cpy (\d+) \w"
pattern2 = r"jnz (\d+) \w"
c = int(findall(pattern1, data)[-1])
d = int(findall(pattern2, data)[-1])


def solve(n):
    return prod(range(1, n + 1)) + c * d


ans1 = solve(7)
ans2 = solve(12)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
