from aocd import get_data, submit
import numpy as np

DAY = 8
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split("\n")

screen = np.zeros((6, 50), dtype=int)


def display(matrix):
    return "\n".join("".join("#" if p else " " for p in row) for row in matrix)


def execute(instr):
    if instr[0] == "rect":
        x, y = map(int, tuple(instr[1].split("x")))
        screen[:y, :x] = 1
        return
    if instr[1] == "row":
        y = int(instr[2][2:])
        r = int(instr[-1])
        screen[y] = np.roll(screen[y], r)
        return
    if instr[1] == "column":
        x = int(instr[2][2:])
        r = int(instr[-1])
        screen[:, x] = np.roll(screen[:, x], r)
        return
    return


for row in data:
    execute(row.split())

ans1 = screen.sum()
# np.savetxt("2016//16_08_screen.txt", screen, fmt="%d")
print(display(screen))
ans2 = "ZFHFSFOGPO"

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
