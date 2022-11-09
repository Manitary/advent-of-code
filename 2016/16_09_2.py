#Solution using itertools from r/AdventOfCode (5hbygy)
from aocd import get_data, submit
from itertools import takewhile, islice
DAY = 9
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

def decompress(data, recurse):
    answer = 0
    chars = iter(data)
    for c in chars:
        if c == '(':
            n, m = map(int, [''.join(takewhile(lambda c: c not in 'x)', chars)) for _ in (0, 1)])
            s = ''.join(islice(chars, n))
            answer += (decompress(s, recurse) if recurse else len(s))*m
        else:
            answer += 1
    return answer

ans1 = decompress(data, False)
ans2 = decompress(data, True)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)