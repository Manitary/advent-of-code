from itertools import groupby

from aocd import get_data, submit

DAY = 10
YEAR = 2015

N1, N2 = 40, 50


def say(s: str) -> str:
    return "".join(f"{len(tuple(g))}{c}" for c, g in groupby(s))


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    part1 = 0
    for i in range(N2):
        data = say(data)
        if i == N1 - 1:
            part1 = len(data)

    return part1, len(data)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
