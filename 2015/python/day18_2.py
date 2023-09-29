import itertools

from aocd import get_data, submit

DAY = 18
YEAR = 2015

Coords = tuple[int, int]

LENGTH = 100
CORNERS: set[Coords] = {
    (0, 0),
    (0, LENGTH - 1),
    (LENGTH - 1, 0),
    (LENGTH - 1, LENGTH - 1),
}


def neighbours(panel: set[Coords], x: int, y: int) -> int:
    return sum(
        (a, b) in panel
        for a in (x - 1, x, x + 1)
        for b in (y - 1, y, y + 1)
        if (a, b) != (x, y)
    )


def switch_lights(panel: set[Coords]) -> set[Coords]:
    return {
        (x, y)
        for x, y in itertools.product(range(LENGTH), repeat=2)
        if ((x, y) in panel and 2 <= neighbours(panel, x, y) <= 3)
        or ((x, y) not in panel and neighbours(panel, x, y) == 3)
    }


def switch_lights_2(panel: set[Coords]) -> set[Coords]:
    return CORNERS | switch_lights(panel)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    lights = {
        (x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == "#"
    }
    lights2 = CORNERS | lights
    for _ in range(100):
        lights = switch_lights(lights)
        lights2 = switch_lights_2(lights2)

    return len(lights), len(lights2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
