from collections import defaultdict, deque
from functools import cache
from hashlib import md5
from itertools import count, groupby

from aocd import get_data, submit

DAY = 14
YEAR = 2016


@cache
def md5hash(s: str) -> str:
    return md5(s.encode()).hexdigest()


def rehash(s: str) -> str:
    ans = s
    for _ in range(2016):
        ans = md5hash(ans)
    return ans


def solve(data: str, part: int = 1) -> int:
    keys: set[int] = set()
    repeats: dict[str, deque[int]] = defaultdict(deque)
    for i in count():
        s = md5hash(f"{data}{i}")
        if part == 2:
            s = rehash(s)
        new = True
        for v, g in groupby(s):
            l = len(tuple(g))
            if l < 3:
                continue
            if new:
                repeats[v].append(i)
                new = False
            if l < 5:
                continue
            while repeats[v] and repeats[v][0] < i:
                n = repeats[v].popleft()
                if n + 1000 < i:
                    continue
                keys.add(n)
                while len(keys) > 64:
                    keys.remove(max(keys))
                if len(keys) == 64 and (m := max(keys)) + 1000 <= i:
                    return m
    raise ValueError("Invalid input")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = solve(data)
    part2 = solve(data, 2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
