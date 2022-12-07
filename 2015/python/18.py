# Better solution with numpy at https://www.reddit.com/r/adventofcode/comments/3xb3cj/day_18_solutions/cy368tv/
from aocd import get_data, submit
from itertools import product

DAY = 18
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

LENGTH = 100
lights = [[0] + [1 if c == "#" else 0 for c in row] + [0] for row in data.split()]
pad = [0 for _ in range(len(lights[0]))]
lights.append(pad)
lights.insert(0, pad)


def lightsOn(panel):
    return sum(sum(panel, []))


def neighbours(panel, x, y):
    return (
        sum((panel[b][a] for a, b in product(*(range(n - 1, n + 2) for n in (x, y)))))
        - panel[y][x]
    )


def newState(panel, x, y, c, part=1):
    if x == 0 or y == 0 or x == LENGTH + 1 or y == LENGTH + 1:
        return 0
    if part == 2 and (x, y) in product(*((1, LENGTH) for _ in range(2))):
        return 1
    if c == 1:
        return 1 if neighbours(panel, x, y) in {2, 3} else 0
    return 1 if neighbours(panel, x, y) == 3 else 0


def switchLights(panel, part=1):
    return [
        [newState(panel, x, y, c, part) for x, c in enumerate(row)]
        for y, row in enumerate(panel)
    ]


lights2 = [row[:] for row in lights]

for _ in range(100):
    lights = switchLights(lights)
    lights2 = switchLights(lights2, 2)

ans1 = lightsOn(lights)
ans2 = lightsOn(lights2)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
