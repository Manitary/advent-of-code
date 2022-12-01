from aocd import get_data, submit
DAY = 1
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split(", ")

x, y = 0, 0
dx, dy = 0, 1
visited = set()
ans2 = None

for instr in data:
    dx, dy = (dy, -dx) if instr[0] == 'R' else (-dy, dx)
    for _ in range(int(instr[1:])):
        x += dx
        y += dy
        if not ans2:
            if (x, y) in visited:
                ans2 = x + y
            visited.add((x, y))
ans1 = x + y

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)