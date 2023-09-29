import re

from aocd import get_data, submit

DAY = 16
YEAR = 2015

Properties = dict[str, int]

PATTERN = re.compile(r"(\w+): (\d+)")

TARGET: Properties = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def find_aunt(aunts: dict[int, Properties], target: Properties, part: int = 1) -> int:
    for i, aunt in aunts.items():
        if all(
            compare_item(thing, amount, target[thing], part)
            for thing, amount in aunt.items()
        ):
            return i
    raise ValueError("Aunt not found")


def compare_item(
    item: str, aunt_amount: int, target_amount: int, part: int = 1
) -> bool:
    if part == 1:
        return aunt_amount == target_amount
    if item in {"cats", "trees"}:
        return aunt_amount > target_amount
    if item in {"pomeranians", "goldfish"}:
        return aunt_amount < target_amount
    return aunt_amount == target_amount


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    aunts: dict[int, Properties] = {
        i + 1: {p[0]: int(p[1]) for p in PATTERN.findall(row)}
        for i, row in enumerate(data)
    }

    part1 = find_aunt(aunts, TARGET)
    part2 = find_aunt(aunts, TARGET, 2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
