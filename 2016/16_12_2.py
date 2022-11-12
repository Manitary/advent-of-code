from aocd import get_data, submit
from functools import cache
from re import findall
DAY = 12
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

@cache
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

pattern = r"cpy (\d+) (?:c|d)"
d0, c0, c1, d1 = map(int, tuple(findall(pattern, data)))

ans1 = Fibonacci(2 + d0) + c1*d1
ans2 = Fibonacci(2 + d0 + c0) + c1*d1

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)