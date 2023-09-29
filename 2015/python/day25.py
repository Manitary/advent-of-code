import re

from aocd import get_data, submit

DAY = 25
YEAR = 2015

A0 = 20151125
K = 252533
Q = 33554393


def get_index(x: int, y: int) -> int:
    return (x + y - 1) * (x + y - 2) // 2 + x


def get_number(x: int, y: int) -> int:
    ans = A0
    for _ in range(get_index(x, y) - 1):
        ans = (ans * K) % Q
    return ans


def main() -> int:
    data = get_data(day=DAY, year=YEAR)
    y, x = tuple(map(int, re.findall(r"\d+", data)))
    return get_number(x, y)


if __name__ == "__main__":
    ans1 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
