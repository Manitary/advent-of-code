import json

from aocd import get_data, submit

DAY = 12
YEAR = 2015

Element = int | str | list["Element"] | dict[str, "Element"]


def sum_all(elt: Element, excluded: list[str] | None = None) -> int:
    excluded = excluded or []
    if isinstance(elt, int):
        return elt
    if isinstance(elt, str):
        return 0
    if isinstance(elt, list):
        return sum(map(lambda x: sum_all(x, excluded), elt))
    if any(k in excluded for k in elt.values()):
        return 0
    return sum(map(lambda x: sum_all(x, excluded), elt.values()))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = json.JSONDecoder().decode(data)

    part1 = sum_all(data)
    part2 = sum_all(data, excluded=["red"])
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
