from aocd import get_data, submit
from re import findall
DAY = 25
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

y, x = tuple(map(int, findall("\d+", data)))

a0 = 20151125
k = 252533
q = 33554393

def getIndex(x, y):
    return (x + y - 1)*(x + y - 2)//2 + x

def getNumber(x, y):
    ans = a0
    for _ in range(getIndex(x, y) - 1):
        ans = (ans * k) % q
    return ans

ans1 = getNumber(x, y)
submit(ans1, part="a", day=DAY, year=YEAR)