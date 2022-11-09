from aocd import get_data, submit
DAY = 9
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

def decompress(s, version=2):
    length = 0
    while '(' in s:
        start = s.find('(')
        length += start
        end = s.find(')', start + 1)
        n1, n2 = map(int, tuple(s[start + 1 : end].split('x')))
        if version == 1:
            length += n1 * n2
        elif version == 2:
            length += decompress(s[end + 1 : end + n1 + 1]) * n2
        s = s[end + 1 + n1:]
    length += len(s)
    return length

ans1 = decompress(data, version=1)
ans2 = decompress(data)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)