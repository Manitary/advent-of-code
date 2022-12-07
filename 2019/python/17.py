from aocd import get_data, submit
from intcode import Computer
from collections import deque
from re import match

DAY = 17
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
ORIENTATIONS = ("^", ">", "v", "<")


def getScaffolding(output: deque[int], display: bool = False) -> set[tuple[int]]:
    scaffolding = set()
    view = ""
    x, y = 0, 0
    while output:
        c = output.popleft()
        if c == 10:
            y += 1
            x = -1
            view += "\n"
        elif c == 46:
            view += " "
        else:
            scaffolding.add((x, y))
            view += chr(c)
            if c != 35:
                start = (x, y)
                direction = chr(c)
        x += 1
    if display:
        print(view)
    return scaffolding, start, direction


def neighbours(coords: tuple[int], scaffolding: set[tuple[int]]) -> set[tuple[int]]:
    x, y = coords
    return {
        coord
        for coord in {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
        if coord in scaffolding
    }


def nextStep(coords: tuple[int], direction: int) -> tuple[int]:
    x, y = coords
    dx, dy = DIRECTIONS[direction]
    return (x + dx, y + dy)


def pathFromEnd(scaffolding: set[tuple[int]], start: tuple[int], direction: int) -> str:
    current_tile = start
    current_direction = direction
    path = ""
    length = 0
    while True:
        if (new_tile := nextStep(current_tile, current_direction)) in scaffolding:
            length += 1
            current_tile = new_tile
        else:
            if length > 0:
                path += str(length) + ","
            for turn in {1, -1}:
                new_direction = (current_direction + turn) % 4
                if nextStep(current_tile, new_direction) in scaffolding:
                    current_direction = new_direction
                    path += "R," if turn == 1 else "L,"
                    length = 0
                    break
            else:
                return path


def findRoutine(path: str, *functions: str, routine: list[int] = None) -> list[int]:
    routine = routine or []
    for i, f in enumerate(functions):
        if path.startswith(f):
            if newRoutine := findRoutine(
                path[len(f) :], *functions, routine=routine + [ord("A") + i, 44]
            ):  # 44 = ,
                return newRoutine[:-1] + [10]  # 10 = \n
    return routine


def formatString(string: str) -> list[int]:
    return [ord(c) for c in string[:-1]] + [10]


computer = Computer(data)
computer.run()
scaffolding, start, direction = getScaffolding(computer.output)
direction = ORIENTATIONS.index(direction)
path = pathFromEnd(scaffolding, start, direction)
pattern = r"^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$"
m = match(pattern, path)

routine = findRoutine(path, *m.groups())
functions = tuple(formatString(x) for x in m.groups())
inputs = [routine, *functions, [ord("n"), 10]]

computer.reset()
computer[0] = 2
for i in inputs:
    computer.push(i)
    computer.run()

ans1 = sum([s[0] * s[1] for s in scaffolding if len(neighbours(s, scaffolding)) == 4])
ans2 = computer.output[-1]

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
