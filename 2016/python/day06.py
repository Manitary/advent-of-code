from collections import Counter

from aocd import get_data, submit

DAY = 6
YEAR = 2016


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR).split()

    count = [Counter(row) for row in data]
    part1 = "".join([c.most_common(1)[0][0] for c in count])
    part2 = "".join([c.most_common()[-1][0] for c in count])
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
