from typing import Self

from aocd import get_data, submit

DAY = 13
YEAR = 2018

TEXT_DIR = {"v": (1, 0), "<": (0, -1), ">": (0, 1), "^": (-1, 0)}

Coords = tuple[int, int]


class Cart:
    def __init__(self, coords: Coords, direction: Coords) -> None:
        self.coords: Coords = coords
        self.direction: Coords = direction
        self.turns = 0

    def __lt__(self, other: Self) -> bool:
        return self.coords < other.coords

    def move(self, grid: dict[Coords, str]) -> None:
        self.coords: Coords = tuple(map(sum, zip(self.coords, self.direction)))
        grid_tile = grid.get(self.coords, "")
        if grid_tile == "/":
            self.direction = (-self.direction[1], -self.direction[0])
        elif grid_tile == "\\":
            self.direction = (self.direction[1], self.direction[0])
        elif grid_tile == "+":
            if self.turns == 0:
                self.direction = (-self.direction[1], self.direction[0])
            elif self.turns == 2:
                self.direction = (self.direction[1], -self.direction[0])
            self.turns += 1
            self.turns %= 3


def move_all(
    grid: dict[Coords, str], carts: list[Cart]
) -> tuple[list[Cart], Coords | None]:
    i = -1
    carts = sorted(carts)
    coords = None
    while i < len(carts) - 1:
        i += 1
        carts[i].move(grid)
        crashing = [
            (idx, c)
            for idx, c in enumerate(carts)
            if idx != i and c.coords == carts[i].coords
        ]
        if not crashing:
            continue
        idx, c = crashing[0]
        carts.remove(carts[i])
        carts.remove(c)
        i -= 2 if idx < i else 1
        coords = c.coords
    return carts, coords


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)
    grid = {
        (row, col): x
        for row, line in enumerate(data.split("\n"))
        for col, x in enumerate(line)
        if x in {"+", "\\", "/"}
    }
    carts = [
        Cart((row, col), TEXT_DIR[x])
        for row, line in enumerate(data.split("\n"))
        for col, x in enumerate(line)
        if x in TEXT_DIR
    ]
    part1 = 0
    i = 0
    while not part1:
        i += 1
        carts, part1 = move_all(grid, carts)
    while len(carts) > 1:
        i += 1
        carts, _ = move_all(grid, carts)
    part2 = carts[0].coords
    return ",".join(map(str, part1[::-1])), ",".join(map(str, part2[::-1]))


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
