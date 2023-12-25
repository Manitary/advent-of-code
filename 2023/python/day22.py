import re
from collections import defaultdict

from aocd import get_data, submit

DAY = 22
YEAR = 2023

type Coord2D = tuple[int, int]
type Coord3D = tuple[int, int, int]
type Brick = set[Coord3D]
type Graph = dict[int, set[int]]

COORD_RE = re.compile(r"\d+")


def parse_brick(brick_data: str) -> Brick:
    """Return the set of brick pieces.

    Only keep track of min/max height:
    if they are different, it means it is a vertical block, so they are
    the only parts of the block relevant to calculate the falling behaviour.
    """
    x1, y1, z1, x2, y2, z2 = map(int, COORD_RE.findall(brick_data))
    return {
        (x, y, z)
        for x in range(min(x1, x2), max(x1, x2) + 1)
        for y in range(min(y1, y2), max(y1, y2) + 1)
        for z in (z1, z2)
    }


def make_support_graph(bricks: list[Brick]) -> tuple[Graph, Graph]:
    xyz_to_brick: dict[Coord3D, int] = {}
    xy_highest_z: dict[Coord2D, int] = {}
    supports: Graph = defaultdict(set)
    supported: Graph = defaultdict(set)

    for i, brick in enumerate(bricks):
        fall_height = min(z - xy_highest_z.get((x, y), 0) - 1 for x, y, z in brick)
        fallen_brick = {(x, y, z - fall_height) for x, y, z in brick}
        for tile_under in ((x, y, z - 1) for x, y, z in fallen_brick):
            if brick_under := xyz_to_brick.get(tile_under):
                supports[brick_under].add(i)
                supported[i].add(brick_under)

        for x, y, z in fallen_brick:
            xyz_to_brick[x, y, z] = i
            xy_highest_z[x, y] = max(z, xy_highest_z.get((x, y), z))

        bricks[i] = fallen_brick

    return supports, supported


def num_falling_bricks(brick_to_remove: int, supports: Graph, supported: Graph) -> int:
    fell = 0
    supports_lost = {brick_to_remove}
    todo = supports[brick_to_remove]

    while todo:
        brick = todo.pop()
        if brick in supports_lost:
            continue

        if supported.get(brick, set()).issubset(supports_lost):
            fell += 1
            supports_lost.add(brick)
            todo |= supports.get(brick, set())

    return fell


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    bricks = sorted(
        map(parse_brick, data),
        key=lambda b: next(iter(b))[2] if len(b) > 2 else min(p[2] for p in b),
    )

    supports, supported = make_support_graph(bricks)

    part1 = sum(
        all((len(supported.get(x, set())) != 1) for x in supports.get(i, set()))
        for i in range(len(bricks))
    )

    part2 = sum(num_falling_bricks(i, supports, supported) for i in supports)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
