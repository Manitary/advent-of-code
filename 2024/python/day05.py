import re
from itertools import batched, combinations

with open("input.txt") as f:
    data = f.read()


def parse(d: str):
    a, b = data.split("\n\n")
    rules = {(x[0], x[1]) for x in batched(map(int, re.split(r"[|\s]", a)), 2)}
    manuals = [list(map(int, m.split(","))) for m in b.splitlines()]
    return rules, manuals


def part_1(rules: set[tuple[int, int]], manual: list[int]):
    return all(pages in rules for pages in combinations(manual, 2))


def part_2(rules: set[tuple[int, int]], manual: list[int]):
    while True:
        for p1, p2 in combinations(range(len(manual)), 2):
            if (manual[p1], manual[p2]) not in rules:
                manual[p1], manual[p2] = manual[p2], manual[p1]
                break
        else:
            return manual[len(manual) // 2]


def main():
    part1, part2 = 0, 0
    r, m = parse(data)
    print(r)
    print(m)
    part1 = sum(mm[len(mm) // 2] for mm in m if part_1(r, mm))
    part2 = sum(part_2(r, mm) for mm in m if not part_1(r, mm))
    return part1, part2


if __name__ == "__main__":
    print(main())
