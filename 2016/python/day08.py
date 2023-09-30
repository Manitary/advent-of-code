import numpy as np
from advent_of_code_ocr import convert_array_6
from aocd import get_data, submit
from numpy.typing import NDArray

DAY = 8
YEAR = 2016


def display(matrix: NDArray[np.int8]) -> str:
    return "\n".join("".join("#" if p else " " for p in row) for row in matrix)


def execute(screen: NDArray[np.int8], instr: list[str]) -> None:
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


def main() -> tuple[int, str]:
    data = get_data(day=DAY, year=YEAR).split("\n")

    screen = np.zeros((6, 50), dtype=np.int8)
    for row in data:
        execute(screen, row.split())

    part1: int = screen.sum()
    part2 = convert_array_6(screen, fill_pixel=1, empty_pixel=0)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
