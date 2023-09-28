# See https://redd.it/5ititq for a solution that uses properties of the dragon curve construction

from typing import Generator, TypeVar

from aocd import get_data, submit

DAY = 16
YEAR = 2016

T = TypeVar("T")

SIZE1 = 272
SIZE2 = 35651584


def dragon_curve(lst: list[int]) -> list[int]:
    return [*lst, *(0,), *reversed(list(map(lambda x: 1 - x, lst)))]


def expand(data: str, size: int) -> list[int]:
    ans = list(map(int, list(data)))
    while len(ans) < size:
        ans = dragon_curve(ans)
    return ans[:size]


def pairs(lst: list[T]) -> Generator[list[T], None, None]:
    for i in range(0, len(lst), 2):
        yield lst[i : i + 2]


def checksum(lst: list[int]) -> list[int]:
    return [1 if p[0] == p[1] else 0 for p in pairs(lst)]


def full_checksum(lst: list[int]) -> str:
    ans = checksum(lst)
    while len(ans) % 2 == 0:
        ans = checksum(ans)
    return "".join(map(str, ans))


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)
    part1 = full_checksum(expand(data, SIZE1))
    part2 = full_checksum(expand(data, SIZE2))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
