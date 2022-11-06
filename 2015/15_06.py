from aocd import get_data, submit
import re
DAY = 6
YEAR = 2015

L = 1000
data = get_data(day=DAY, year=YEAR).split("\n")
lights = {(x, y): [0, 0] for x in range(L) for y in range(L)}

def switch(x, y, instr):
    match instr:
        case "turn on":
            lights[(x, y)][0] = 1
            lights[(x, y)][1] += 1
        case "turn off":
            lights[(x, y)][0] = 0
            lights[(x, y)][1] = max(0, lights[(x, y)][1] - 1)
        case "toggle":
            lights[(x, y)][0] = 1 - lights[(x, y)][0]
            lights[(x, y)][1] += 2

regex = r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"
for row in data:
    m = re.match(regex, row)
    for x in range(int(m.group(2)), int(m.group(4)) + 1):
        for y in range(int(m.group(3)), int(m.group(5)) + 1):
            switch(x, y, m.group(1))

ans1 = 0
ans2 = 0
for x in range(L):
    for y in range(L):
        ans1 += lights[(x, y)][0]
        ans2 += lights[(x, y)][1]

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
