from aocd import get_data, submit

DAY = 2
YEAR = 2024


def is_safe(n: list[int]) -> bool:
    diffs = {n[i + 1] - n[i] for i in range(len(n) - 1)}
    if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
        return True
    return False


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [list(map(int, x.split())) for x in data.splitlines()]

    part1 = sum(is_safe(x) for x in data)
    part2 = sum(any(is_safe(x[:i] + x[i + 1 :]) for i in range(len(x))) for x in data)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
