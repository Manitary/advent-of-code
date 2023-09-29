from aocd import get_data, submit

DAY = 8
YEAR = 2015


def real_count(s: str) -> tuple[int, int]:
    count = 0
    encoded = 6
    i = 1
    while i < len(s) - 1:
        count += 1
        if s[i] == "\\":
            if s[i + 1] == "\\" or s[i + 1] == '"':
                i += 2
                encoded += 4
            elif s[i + 1] == "x":
                i += 4
                encoded += 5
        else:
            i += 1
            encoded += 1
    return count, encoded


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    part1, part2 = 0, 0
    for row in data:
        real, encoded = real_count(row)
        part1 += len(row) - real
        part2 += encoded - len(row)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
