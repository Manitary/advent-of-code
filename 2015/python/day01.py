from aocd import get_data, submit

DAY = 1
YEAR = 2015


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    floor = 0
    part2 = 0
    for i, c in enumerate(data):
        if c == "(":
            floor += 1
        else:
            floor -= 1
            if (not part2) and floor < 0:
                part2 = i + 1
    return floor, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
