# Better solution with numpy at https://www.reddit.com/r/adventofcode/comments/3xb3cj/day_18_solutions/cy368tv/
from itertools import product

from aocd import get_data, submit

DAY = 18
YEAR = 2015

LENGTH = 100


def lights_on(panel: list[list[int]]) -> int:
    start: list[int] = []
    return sum(sum(panel, start=start))


def neighbours(panel: list[list[int]], x: int, y: int) -> int:
    return (
        sum(panel[b][a] for a, b in product(*(range(n - 1, n + 2) for n in (x, y))))
        - panel[y][x]
    )


def new_state(panel: list[list[int]], x: int, y: int, c: int, part: int = 1) -> int:
    if x == 0 or y == 0 or x == LENGTH + 1 or y == LENGTH + 1:
        return 0
    if part == 2 and (x, y) in product((1, LENGTH), repeat=2):
        return 1
    if c == 1:
        return int(neighbours(panel, x, y) in {2, 3})
    return int(neighbours(panel, x, y) == 3)


def switch_light(panel: list[list[int]], part: int = 1) -> list[list[int]]:
    return [
        [new_state(panel, x, y, c, part) for x, c in enumerate(row)]
        for y, row in enumerate(panel)
    ]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    lights = [[0] + [1 if c == "#" else 0 for c in row] + [0] for row in data.split()]
    pad = [0] * len(lights[0])
    lights.append(pad)
    lights.insert(0, pad)
    lights2 = [row[:] for row in lights]

    for _ in range(100):
        lights = switch_light(lights)
        lights2 = switch_light(lights2, 2)

    return lights_on(lights), lights_on(lights2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
