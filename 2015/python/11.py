from aocd import get_data, submit
from itertools import groupby

DAY = 11
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

MIN = ord("a")
MAX = ord("z")
INVALID = set(ord(c) for c in ("i", "l", "o"))


def strToNums(s):
    return [ord(c) for c in s]


def numsToStr(l):
    return "".join(chr(n) for n in l)


def nextChar(i):
    j = i + 1
    if j in INVALID:
        j += 1
    if j > MAX:
        j = MIN
    return j


def increment(l, i=-1):
    l[i] = nextChar(l[i])
    if l[i] == MIN:
        l = increment(l, i - 1)
    return l


def nextValid(l):
    for i, c in enumerate(l):
        if c in INVALID:
            l = increment(l, i)
            l = l[: i + 1] + [MIN for _ in range(len(l) - i)]
            return nextValid(l)
    return l


def rule1(l):
    for i in range(len(l) - 2):
        if l[i + 2] == l[i + 1] + 1 == l[i] + 2:
            return True
    return False


def rule3(l):
    pairs = 0
    for _, g in groupby(iter(l)):
        if len(tuple(g)) >= 2:
            pairs += 1
            if pairs == 2:
                return True
    return False


def findNext(psw):
    psw = strToNums(psw)
    psw = nextValid(psw)
    while True:
        psw = increment(psw)
        if rule1(psw) and rule3(psw):
            return numsToStr(psw)


ans1 = findNext(data)
ans2 = findNext(ans1)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
