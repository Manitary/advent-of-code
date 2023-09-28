from aocd import get_data, submit

DAY = 18
YEAR = 2016

NUM1 = 40
NUM2 = 400000


def is_trap(row: list[int], i: int) -> int:
    if i in (0, len(row) - 1):
        return 0
    return row[i - 1] ^ row[i + 1]


def next_row(row: list[int]) -> list[int]:
    return [is_trap(row, i) for i in range(len(row))]


def num_safe(n: int, c: int, l: int) -> int:
    return n * (l - 1) - c


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    row = [0] + [1 if c == "^" else 0 for c in data] + [0]
    count = sum(row)
    part1 = 0
    for i in range(NUM2 - 1):
        row = next_row(row)
        count += sum(row)
        if i == NUM1 - 2:
            part1 = num_safe(NUM1, count, len(data) + 1)

    part2 = num_safe(NUM2, count, len(data) + 1)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
