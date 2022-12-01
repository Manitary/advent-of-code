from aocd import get_data, submit
DAY = 3
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = [list(map(int, row.split())) for row in data.split('\n')]

def scan1(data):
    for row in data:
        yield tuple(row)

def scan2(data):
    r, c = 0, 0
    while c < len(data[0]):
        yield data[r][c], data[r+1][c], data[r+2][c]
        r += 3
        if r >= len(data):
            r = 0
            c += 1

def count(data, scan):
    ans = 0
    for t in scan(data):
        if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[2] + t[0] > t[1]:
            ans += 1
    return ans

submit(count(data, scan1), part="a", day=DAY, year=YEAR)
submit(count(data, scan2), part="b", day=DAY, year=YEAR)