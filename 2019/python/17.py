from collections import deque
from re import match
from typing import cast

from aocd import get_data, submit
from intcode import Computer

DAY = 17
YEAR = 2019

Coords = tuple[int, int]

DIRECTIONS: tuple[Coords, ...] = ((0, -1), (1, 0), (0, 1), (-1, 0))
ORIENTATIONS = ("^", ">", "v", "<")


def getScaffolding(
    output: deque[int], display: bool = False
) -> tuple[set[Coords], Coords, str]:
    scaffolding: set[Coords] = set()
    view = ""
    x, y = 0, 0
    start = (0, 0)
    direction = ""
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


def neighbours(coords: Coords, scaffolding: set[Coords]) -> set[Coords]:
    x, y = coords
    return {
        coord
        for coord in {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
        if coord in scaffolding
    }


def nextStep(coords: Coords, direction: int) -> Coords:
    return cast(Coords, tuple(map(sum, zip(coords, DIRECTIONS[direction]))))


def pathFromEnd(scaffolding: set[Coords], start: Coords, direction: int) -> str:
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


def findRoutine(
    path: str, *functions: str, routine: list[int] | None = None
) -> list[int]:
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


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    computer = Computer(data)
    computer.run()
    scaffolding, start, direction = getScaffolding(computer.output)
    direction = ORIENTATIONS.index(direction)
    path = pathFromEnd(scaffolding, start, direction)
    pattern = r"^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$"
    m = match(pattern, path)
    if not m:
        raise ValueError("Pattern not found")
    routine = findRoutine(path, *m.groups())
    functions = tuple(formatString(x) for x in m.groups())
    inputs = [routine, *functions, [ord("n"), 10]]

    computer.reset()
    computer[0] = 2
    for i in inputs:
        computer.push(i)
        computer.run()

    part1 = sum(
        [s[0] * s[1] for s in scaffolding if len(neighbours(s, scaffolding)) == 4]
    )
    part2 = computer.output[-1]
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
