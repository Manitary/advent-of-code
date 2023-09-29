from itertools import groupby
from typing import Any, Sequence

from aocd import get_data, submit

DAY = 11
YEAR = 2015


MIN = ord("a")
MAX = ord("z")
INVALID = set(ord(c) for c in ("i", "l", "o"))


def str_to_nums(s: str) -> list[int]:
    return [ord(c) for c in s]


def nums_to_str(l: Sequence[int]) -> str:
    return "".join(chr(n) for n in l)


def next_char(i: int) -> int:
    j = i + 1
    if j in INVALID:
        j += 1
    if j > MAX:
        j = MIN
    return j


def increment(l: list[int], i: int = -1) -> list[int]:
    l[i] = next_char(l[i])
    if l[i] == MIN:
        l = increment(l, i - 1)
    return l


def next_valid(l: list[int]) -> list[int]:
    for i, c in enumerate(l):
        if c not in INVALID:
            continue
        l = increment(l, i)
        l = l[: i + 1] + [MIN] * (len(l) - i)
        return next_valid(l)
    return l


def rule1(l: Sequence[int]) -> bool:
    for i in range(len(l) - 2):
        if l[i + 2] == l[i + 1] + 1 == l[i] + 2:
            return True
    return False


def rule3(l: Sequence[Any]) -> bool:
    pairs = 0
    for _, g in groupby(l):
        if len(tuple(g)) == 1:
            continue
        pairs += 1
        if pairs == 2:
            return True
    return False


def find_next(psw: str) -> str:
    psw_num = str_to_nums(psw)
    psw_num = next_valid(psw_num)
    while True:
        psw_num = increment(psw_num)
        if rule1(psw_num) and rule3(psw_num):
            return nums_to_str(psw_num)


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)
    part1 = find_next(data)
    return part1, find_next(part1)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
