from aocd import get_data, submit
from re import findall, compile

DAY = 16
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")

target = {
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


def findAunt(target, part=1):
    for i, aunt in aunts.items():
        if all(
            compareItem(thing, amount, target[thing], part)
            for thing, amount in aunt.items()
        ):
            return i


def compareItem(item, auntAmount, targetAmount, part=1):
    if part == 1:
        return auntAmount == targetAmount
    else:
        match item:
            case "cats" | "trees":
                return auntAmount > targetAmount
            case "pomeranians" | "goldfish":
                return auntAmount < targetAmount
            case _:
                return auntAmount == targetAmount


pattern = r"(\w+): (\d+)"
compile(pattern)
aunts = {
    i + 1: {p[0]: int(p[1]) for p in findall(pattern, row)}
    for i, row in enumerate(data)
}

ans1 = findAunt(target)
ans2 = findAunt(target, 2)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
