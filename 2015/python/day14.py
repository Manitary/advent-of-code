import re

from aocd import get_data, submit

DAY = 14
YEAR = 2015

TIME_LIMIT = 2503
RE_REINDEER = re.compile(r"\d+")


def pos(reindeer: dict[str, int], elapsed: int) -> int:
    s, ft, rt = (
        reindeer["speed"],
        reindeer["max_time_flying"],
        reindeer["max_time_resting"],
    )
    return s * (elapsed // (ft + rt) * ft + min(ft, elapsed % (ft + rt)))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    reindeers: dict[int, dict[str, int]] = {}
    for i, row in enumerate(data):
        s, ft, rt = map(int, tuple(RE_REINDEER.findall(row)))
        reindeers[i] = {
            "speed": s,
            "max_time_flying": ft,
            "max_time_resting": rt,
            "time_flying": 0,
            "time_resting": 0,
        }

    part1 = max(iter(pos(reindeer, TIME_LIMIT) for reindeer in reindeers.values()))

    distance = [0] * len(reindeers)
    score = [0] * len(reindeers)
    for _ in range(TIME_LIMIT):
        for i, r in reindeers.items():
            if r["time_flying"] < r["max_time_flying"]:
                r["time_flying"] += 1
                distance[i] += r["speed"]
            else:
                r["time_resting"] += 1
                if r["time_resting"] == r["max_time_resting"]:
                    r["time_flying"] = 0
                    r["time_resting"] = 0
        best = max(distance)
        for i, d in enumerate(distance):
            if d == best:
                score[i] += 1
    part2 = max(score)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
