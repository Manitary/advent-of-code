from aocd import get_data, submit

DAY = 1
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

floor = 0
ans = None
for i, c in enumerate(data):
    if c == "(":
        floor += 1
    else:
        floor -= 1
        if (not ans) and floor < 0:
            ans = i + 1

submit(floor, part="a", day=DAY, year=YEAR)
submit(ans, part="b", day=DAY, year=YEAR)
