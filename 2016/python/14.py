from aocd import get_data, submit
from hashlib import md5
from itertools import count, groupby
from collections import defaultdict, deque
from functools import cache
DAY = 14
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

@cache
def md5hash(s):
    return md5(s.encode()).hexdigest()

def rehash(s):
    ans = s
    for _ in range(2016):
        ans = md5hash(ans)
    return ans

def solve(part=1):
    keys = set()
    repeats = defaultdict(deque)
    for i in count():
        s = md5hash(f"{data}{i}")
        if part == 2:
            s = rehash(s)
        new = True
        for v, g in groupby(s):
            l = len(tuple(g))
            if l >= 3:
                if new:
                    repeats[v].append(i)
                    new = False
                if l >= 5:
                    while repeats[v] and repeats[v][0] < i:
                        n = repeats[v].popleft()
                        if n + 1000 >= i:
                            keys.add(n)
                            while len(keys) > 64:
                                keys.remove(max(keys))
                            if len(keys) == 64 and (m:=max(keys)) + 1000 <= i:
                                return m

ans1 = solve()
ans2 = solve(2)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)