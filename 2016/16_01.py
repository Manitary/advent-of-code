from aocd import get_data, submit
DAY = 1
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split(", ")

x, y = 0, 0
dx, dy = 0, 1
visited = set()
ans = None

for instr in data:
    if instr[0] == 'R':
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx
    l = int(instr[1:])
    for _ in range(l):
        x += dx
        y += dy
        if not ans:
            if (x, y) in visited:
                ans = (x, y)
            visited.add((x, y))

submit(x + y, part="a", day=DAY, year=YEAR)
submit(ans[0] + ans[1], part="b", day=DAY, year=YEAR)