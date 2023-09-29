from itertools import permutations

from aocd import get_data, submit

DAY = 9
YEAR = 2015


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")

    dists: dict[frozenset[str], int] = {}
    cities: set[str] = set()
    for row in data:
        c1, c2, d = row.split()[::2]
        cities |= {c1, c2}
        dists[frozenset((c1, c2))] = int(d)

    part1, part2 = float("inf"), 0
    for path in permutations(cities):
        dist = sum(dists[frozenset(edge)] for edge in zip(path, path[1:]))
        if dist < part1:
            part1 = dist
        if dist > part2:
            part2 = dist
    assert isinstance(part1, int)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
