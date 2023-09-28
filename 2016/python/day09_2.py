# Solution using itertools from r/AdventOfCode (5hbygy)
from itertools import islice, takewhile

from aocd import get_data, submit

DAY = 9
YEAR = 2016


def decompress(data: str, recurse: bool) -> int:
    answer = 0
    chars = iter(data)
    for c in chars:
        if c != "(":
            answer += 1
            continue
        n, m = map(
            int,
            ["".join(takewhile(lambda c: c not in "x)", chars)) for _ in (0, 1)],
        )
        s = "".join(islice(chars, n))
        answer += (decompress(s, recurse) if recurse else len(s)) * m
    return answer


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = decompress(data, False)
    part2 = decompress(data, True)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
