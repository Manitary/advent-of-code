from time import perf_counter
from aocd import get_data, submit
from itertools import groupby
DAY = 10
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

def say(s):
    return ''.join(f"{len(tuple(g))}{c}" for c, g in groupby(iter(s)))

start = perf_counter()
N1, N2 = 40, 50
for i in range(N2):
    data = say(data)
    if i == N1 - 1:
        ans1 = len(data)
ans2 = len(data)
end = perf_counter()

print('time:', end - start)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)