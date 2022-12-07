# See https://redd.it/5ititq for a fast solution that uses properties of the dragon curve construction

from aocd import get_data, submit

DAY = 16
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
size1 = 272
size2 = 35651584


def dragonCurve(lst: list[int]):
    return [*lst, *(0,), *reversed(list(map(lambda x: 1 - x, lst)))]


def expand(data: str, size: int):
    ans = list(map(int, list(data)))
    while len(ans) < size:
        ans = dragonCurve(ans)
    return ans[:size]


def pairs(lst: list):
    i = 0
    for i in range(0, len(lst), 2):
        yield lst[i : i + 2]


def checksum(lst: list[int]):
    return [1 if p[0] == p[1] else 0 for p in pairs(lst)]


def fullChecksum(lst):
    ans = checksum(lst)
    while len(ans) % 2 == 0:
        ans = checksum(ans)
    return "".join(map(str, ans))


ans1 = fullChecksum(expand(data, size1))
ans2 = fullChecksum(expand(data, size2))

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
