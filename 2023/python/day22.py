import copy
import functools
import itertools
import re
from collections import defaultdict

from aocd import get_data, submit

DAY = 22
YEAR = 2023

type Coord = tuple[int, int, int]

COORD_RE = re.compile(r"\d+")


def parse_block(block_data: str) -> set[Coord]:
    x1, y1, z1, x2, y2, z2 = map(int, COORD_RE.findall(block_data))
    if x1 != x2:
        return {(x, y1, z1) for x in range(min(x1, x2), max(x1, x2) + 1)}
    if y1 != y2:
        return {(x1, y, z1) for y in range(min(y1, y2), max(y1, y2) + 1)}
    if z1 != z2:
        return {(x1, y1, z) for z in range(min(z1, z2), max(z1, z2) + 1)}
    return {(x1, y1, z1)}


def can_fall(occupied: set[Coord], block: set[Coord]) -> int:
    h = min(x[2] for x in block)
    if h == 1:
        return 0
    other = occupied - block
    for i in range(1, h):
        if any((x[0], x[1], x[2] - i) in other for x in block):
            return i - 1
    return h - 1


def _count_falling(
    to_remove: int, supports: dict[int, set[int]], supported: dict[int, set[int]]
) -> int:
    ss = copy.deepcopy(supports)
    sd = copy.deepcopy(supported)
    to_process = {to_remove}
    count = 0
    while to_process:
        curr = to_process.pop()
        count += 1
        to_check = ss.pop(curr, set())
        for i in to_check:
            if i not in sd:
                continue
            sd[i].discard(curr)
            if not sd[i]:
                sd.pop(i)
                to_process.add(i)
    return count - 1


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    blocks = sorted(map(parse_block, data), key=lambda x: min(b[2] for b in x))

    occupied = set[Coord].union(*itertools.chain(blocks))

    while True:
        fell = False
        for i, b in enumerate(blocks):
            if h := can_fall(occupied, b):
                occupied -= b
                blocks[i] = {(x[0], x[1], x[2] - h) for x in b}
                occupied |= blocks[i]
                fell = True
        if not fell:
            break

    blocks.sort(key=lambda x: min(b[2] for b in x))

    supports: dict[int, set[int]] = defaultdict(set)
    for i1, i2 in itertools.combinations(range(len(blocks)), 2):
        b1 = blocks[i1]
        b2 = blocks[i2]
        if any((t[0], t[1], t[2] - 1) in b1 for t in b2):
            supports[i1].add(i2)

    part1 = len([i for i, _ in enumerate(blocks) if i not in supports])
    for i, j in supports.items():
        if all(any(x in v for k, v in supports.items() if k != i) for x in j):
            part1 += 1

    supported = {
        b: {s for s, l in supports.items() if b in l}
        for b in set[int].union(*supports.values())
    }

    count_falling = functools.partial(
        _count_falling, supports=supports, supported=supported
    )

    part2 = sum(count_falling(i) for i in supports.keys())

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
