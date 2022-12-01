from aocd import get_data, submit
DAY = 2
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split()

data = [list(map(int, d.split('x'))) for d in data]

def area(sides):
    a, b, c = tuple(sorted(sides))
    return 3 * a * b + 2 * (b * c + c * a), 2 * (a + b) + a * b * c

ans1, ans2 = 0, 0
for sides in data:
    a1, a2 = area(sides)
    ans1 += a1
    ans2 += a2

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)