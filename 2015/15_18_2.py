from aocd import get_data, submit
DAY = 18
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split()

LENGTH = 100
CORNERS = {(0, 0), (0, LENGTH - 1), (LENGTH - 1, 0), (LENGTH - 1, LENGTH - 1)}

lights = {(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == '#'}
lights2 = CORNERS | lights

def neighbours(panel, x, y):
    return sum((a, b) in panel for a in (x - 1, x, x + 1) for b in (y - 1, y, y + 1) if (a, b) != (x, y))

def switchLights(panel):
    return {(x, y) for x in range(LENGTH) for y in range(LENGTH) if ((x, y) in panel and 2 <= neighbours(panel, x, y) <= 3) or ((x, y) not in panel and neighbours(panel, x, y) == 3)}

def switchLights2(panel):
    return CORNERS | switchLights(panel)

for _ in range(100):
    lights = switchLights(lights)
    lights2 = switchLights2(lights2)

ans1 = len(lights)
ans2 = len(lights2)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)