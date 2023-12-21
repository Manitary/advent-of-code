from functools import cached_property

from aocd import get_data, submit

DAY = 21
YEAR = 2023

type Coord = tuple[int, int]


class Grid:
    def __init__(
        self, height: int, width: int, rocks: set[Coord], start: Coord = (0, 0)
    ) -> None:
        self.height = height
        self.width = width
        self.rocks = rocks
        self.start = start

    def reachable_from(
        self, start: Coord, n_steps: int | float, parity: int = 0
    ) -> set[Coord]:
        visited: set[Coord] = set()
        queue: list[tuple[Coord, int]] = [(start, 0)]
        reachable: set[Coord] = set()
        while queue:
            curr, steps = queue.pop(0)
            if steps > n_steps:
                break
            if curr in visited:
                continue
            if steps % 2 == parity:
                reachable.add(curr)
            visited.add(curr)
            r, c = curr
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= x < self.height
                    and 0 <= y < self.width
                    and (x, y) not in visited
                    and (x, y) not in self.rocks
                ):
                    queue.append(((x, y), steps + 1))
        return reachable

    def num_reachable_from(
        self, start: Coord, n_steps: int | float, parity: int = 0
    ) -> int:
        return len(self.reachable_from(start, n_steps, parity))

    @cached_property
    def num_odd_reachable(self) -> int:
        return self.num_reachable_from(self.start, float("inf"), 1)

    @cached_property
    def num_even_reachable(self) -> int:
        return self.num_reachable_from(self.start, float("inf"))

    @property
    def nw(self) -> Coord:
        return (0, 0)

    @property
    def n(self) -> Coord:
        return (0, self.width // 2)

    @property
    def ne(self) -> Coord:
        return (0, self.width - 1)

    @property
    def e(self) -> Coord:
        return (self.height // 2, self.width - 1)

    @property
    def se(self) -> Coord:
        return (self.height - 1, self.width - 1)

    @property
    def s(self) -> Coord:
        return (self.height - 1, self.width // 2)

    @property
    def sw(self) -> Coord:
        return (self.height - 1, 0)

    @property
    def w(self) -> Coord:
        return (self.height // 2, 0)


def parse_grid(data: list[str]) -> Grid:
    start = (0, 0)
    rocks: set[Coord] = set()
    for r, row in enumerate(data):
        for c, elt in enumerate(row):
            if elt == ".":
                continue
            if elt == "S":
                start = (r, c)
                continue
            rocks.add((r, c))

    return Grid(len(data), len(data[0]), rocks, start)


def solve_p2(grid: Grid) -> int:
    # Key observations for part 2
    #
    # The grid is 131x131; the starting point is in the middle of the grid: (65, 65).
    # (*) The perimeter of the grid, as well as the middle row and column, are free of rocks.
    # Let s = 26501365 be the number of steps available: s % 131 = 65,
    # so we can walk straight through s // 131 full grids ("chunks") beyond the starting one.
    #
    # For any grid, the reachable points flip in parity, so "odd"/"even" grids form a checkerboard.
    # To calculate how many points of the "perimeter" grids we can reach, we divide them into:
    #   A) The furthest grid at each cardinal point.
    #   B) Perimeter grids adjacent to any (A) (and down diagonally).
    #   C) Perimeter grids between two consecutive (B)s.
    #
    # Due to (*), we can explore a perimeter grid starting from an optimal point:
    #   A) The middle point of the border, reached by walking straight from start.
    #   B) The corner closer to the start, reached from (A) by walking `half grid + 2` steps.
    #   C) The corner closer to the start, reached from (B) by backtracking a grid worth of steps.
    #      (keep in mind such starting points have flipped parity!)
    #
    # Then we count how many of each such grids there are, keeping in mind that s // 131 is even.

    steps = 26501365
    assert grid.width == grid.height
    assert grid.width % 2
    size = grid.width - 1
    half_size = (grid.width - 1) // 2
    chunks, residue = divmod(steps, grid.width)
    assert chunks % 2 == 0
    assert residue == half_size

    return (
        # cardinal grids (A)
        (
            grid.num_reachable_from(grid.n, size)
            + grid.num_reachable_from(grid.s, size)
            + grid.num_reachable_from(grid.w, size)
            + grid.num_reachable_from(grid.e, size)
        )
        # small corner grids (B)
        + chunks
        * (
            grid.num_reachable_from(grid.nw, half_size - 1)
            + grid.num_reachable_from(grid.ne, half_size - 1)
            + grid.num_reachable_from(grid.se, half_size - 1)
            + grid.num_reachable_from(grid.sw, half_size - 1)
        )
        # large corner grids (C)
        + (chunks - 1)
        * (
            grid.num_reachable_from(grid.nw, size + half_size, 1)
            + grid.num_reachable_from(grid.ne, size + half_size, 1)
            + grid.num_reachable_from(grid.se, size + half_size, 1)
            + grid.num_reachable_from(grid.sw, size + half_size, 1)
        )
        # odd full grids
        + grid.num_odd_reachable * (chunks - 1) ** 2
        # even full grids
        + grid.num_even_reachable * chunks**2
    )


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    grid = parse_grid(data)
    part1 = grid.num_reachable_from(grid.start, 64)
    part2 = solve_p2(grid)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="B", day=DAY, year=YEAR)
