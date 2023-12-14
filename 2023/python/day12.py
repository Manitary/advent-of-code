from functools import cache

from aocd import get_data, submit

DAY = 12
YEAR = 2023


@cache
def count(row: str, pattern: tuple[int, ...]) -> int:
    if not pattern:
        return "#" not in row

    if len(row) < sum(pattern) + len(pattern) - 1:
        return 0

    if row.startswith("."):
        next_valid = next((i for i, c in enumerate(row) if c != "."), 0)
        return count(row[next_valid:], pattern) if next_valid else 0

    if row.startswith("?"):
        return count(f"#{row[1:]}", pattern) + count(row[1:], pattern)

    # starts with #
    l = pattern[0]
    if len(row) < l or "." in row[:l] or (len(row) > l and row[l] == "#"):
        return 0

    return count(row[l + 1 :], pattern[1:])


def main() -> tuple[int, int]:
    data = [
        (x.split()[0], tuple(map(int, x.split()[1].split(","))))
        for x in get_data(day=DAY, year=YEAR).splitlines()
    ]
    part1 = sum(count(row, pattern) for row, pattern in data)
    part2 = sum(
        count("?".join(row for _ in range(5)), pattern * 5) for row, pattern in data
    )
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
