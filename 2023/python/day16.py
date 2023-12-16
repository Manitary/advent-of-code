import enum
import functools
import itertools

from aocd import get_data, submit

DAY = 16
YEAR = 2023


class Dir(enum.Enum):
    N = (-1, 0)
    E = (0, 1)
    S = (1, 0)
    W = (0, -1)


type Beam = tuple[int, int, Dir]


@functools.cache
def new_dir(d: Dir, tile: str) -> tuple[Dir, ...]:
    if (
        tile == "."
        or (tile == "|" and d in (Dir.N, Dir.S))
        or (tile == "-" and d in (Dir.E, Dir.W))
    ):
        return (d,)
    if tile == "|" and d in (Dir.E, Dir.W):
        return (Dir.N, Dir.S)
    if tile == "-" and d in (Dir.N, Dir.S):
        return (Dir.W, Dir.E)
    if tile == "\\":
        return (Dir((d.value[1], d.value[0])),)
    if tile == "/":
        return (Dir((-d.value[1], -d.value[0])),)

    raise ValueError("Invalid input")


@functools.cache
def move(beam: Beam, tile: str) -> list[Beam]:
    r, c, d = beam
    return [(r + d.value[0], c + d.value[1], d) for d in new_dir(d, tile)]


def trajectory(grid: list[str], start: Beam) -> set[Beam]:
    visited: set[Beam] = set()
    queue = [start]
    while queue:
        curr = queue.pop()
        if curr in visited:
            continue
        r, c, _ = curr
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid):
            continue
        visited.add(curr)
        queue.extend(move(curr, grid[r][c]))
    return visited


def num_energized(beams: set[Beam]) -> int:
    return len({(x[0], x[1]) for x in beams})


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    part1 = num_energized(trajectory(data, start=(0, 0, Dir.E)))

    max_r = len(data) - 1
    max_c = len(data[0]) - 1
    part2 = max(
        num_energized(trajectory(data, start))
        for start in itertools.chain(
            ((0, c, Dir.S) for c in range(max_c)),
            ((max_r, c, Dir.N) for c in range(max_c)),
            ((r, 0, Dir.E) for r in range(max_r)),
            ((r, max_c, Dir.W) for r in range(max_r)),
        )
    )

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    print(ans1, ans2)
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
