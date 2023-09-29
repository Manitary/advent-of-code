from aocd import get_data, submit

DAY = 10
YEAR = 2015


def say(s: str) -> str:
    ans = ""
    count = 1
    new = s[0]
    for c in s[1:]:
        if c != new:
            ans += f"{count}{new}"
            new = c
            count = 1
        else:
            count += 1
    ans += f"{count}{new}"
    return ans


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    part1 = 0
    for i in range(50):
        data = say(data)
        if i == 39:
            part1 = len(data)

    return part1, len(data)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
