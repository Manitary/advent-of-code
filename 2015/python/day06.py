import itertools
import re

from aocd import get_data, submit

DAY = 6
YEAR = 2015

SIZE = 1000
PATTERN = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    lights = {(x, y): [0, 0] for x, y in itertools.product(range(SIZE), repeat=2)}

    def switch(x: int, y: int, instr: str) -> None:
        if instr == "turn on":
            lights[(x, y)][0] = 1
            lights[(x, y)][1] += 1
        elif instr == "turn off":
            lights[(x, y)][0] = 0
            lights[(x, y)][1] = max(0, lights[(x, y)][1] - 1)
        elif instr == "toggle":
            lights[(x, y)][0] = 1 - lights[(x, y)][0]
            lights[(x, y)][1] += 2

    for row in data:
        m = PATTERN.match(row)
        if not m:
            raise ValueError("Failed to parse data")
        for x, y in itertools.product(
            range(int(m.group(2)), int(m.group(4)) + 1),
            range(int(m.group(3)), int(m.group(5)) + 1),
        ):
            switch(x, y, m.group(1))

    part1, part2 = map(sum, zip(*lights.values()))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
