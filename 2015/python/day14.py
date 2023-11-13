import re
from typing import NamedTuple

from aocd import get_data, submit

DAY = 14
YEAR = 2015

TIME_LIMIT = 2503
RE_REINDEER = re.compile(r"\d+")

Reindeer = NamedTuple(
    "Reindeer", [("speed", int), ("max_time_flying", int), ("max_time_resting", int)]
)


def pos(reindeer: Reindeer, elapsed: int) -> int:
    s, ft, rt = reindeer.speed, reindeer.max_time_flying, reindeer.max_time_resting
    f1, f2 = divmod(elapsed, ft + rt)
    return s * (f1 * ft + min(ft, f2))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    reindeers = tuple(
        Reindeer(*map(int, tuple(RE_REINDEER.findall(row)))) for row in data
    )
    part1 = max(iter(pos(reindeer, TIME_LIMIT) for reindeer in reindeers))
    scores = [0] * len(reindeers)
    for i in range(1, TIME_LIMIT + 1):
        dists = tuple(pos(reindeer, i) for reindeer in reindeers)
        best = max(dists)
        for j, dist in enumerate(dists):
            if dist == best:
                scores[j] += 1
    part2 = max(scores)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
