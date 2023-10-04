import re
from collections import defaultdict

from aocd import get_data, submit

DAY = 4
YEAR = 2018

RE_ENTRY = re.compile(r"\[(?P<date>.*)\] (?P<event>.*)\b")


def main() -> tuple[int, int]:
    data: list[tuple[str, str]] = sorted(RE_ENTRY.findall(get_data(day=DAY, year=YEAR)))
    guards_data: dict[int, list[int]] = defaultdict(lambda: [0] * 60)
    guard, sleep_start = 0, 0
    for entry in data:
        match entry[1].split():
            case ["Guard", n, *_]:
                guard = int(n[1:])
            case ["falls", "asleep"]:
                sleep_start = int(entry[0].split(":")[1])
            case ["wakes", "up"]:
                sleep_end = int(entry[0].split(":")[1])
                for i in range(sleep_start, sleep_end):
                    guards_data[guard][i] += 1
            case _:
                raise ValueError("Invalid input")

    worst = max(guards_data, key=lambda g: sum(guards_data[g]))
    part1 = worst * guards_data[worst].index(max(guards_data[worst]))

    hours = zip(*guards_data.values())
    worst_by_hour = [(a := max(c), c.index(a)) for c in hours]
    part2 = (idx := worst_by_hour.index(max(worst_by_hour, key=lambda x: x[0]))) * list(
        guards_data.keys()
    )[worst_by_hour[idx][1]]

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
