from typing import Generator

from aocd import get_data, submit

DAY = 13
YEAR = 2016


def count_ones(n: int) -> int:
    ans = 0
    while n:
        ans += n & 1
        n = n >> 1
    return ans


def is_open(x: int, y: int, par: int) -> bool:
    if x < 0 or y < 0:
        return False
    n = x**2 + 3 * x + 2 * x * y + y + y**2 + par
    return count_ones(n) % 2 == 0


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = int(data)

    visited: set[tuple[int, int]] = set()

    def ngbh(x: int, y: int) -> Generator[tuple[int, int], None, None]:
        for coord in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if coord in visited:
                continue
            if is_open(*coord, data):
                yield coord
            else:
                visited.add(coord)

    start = (1, 1)
    end = (31, 39)
    bound = 50
    queue: list[tuple[tuple[int, int], int]] = [(start, 0)]

    part1, part2 = 0, 0
    while queue:
        curr, steps = queue.pop(0)
        if curr == end:
            part1 = steps
        if steps > bound and part1:
            break
        if curr in visited:
            continue
        visited.add(curr)
        if steps <= bound:
            part2 += 1
        for new in ngbh(*curr):
            queue.append((new, steps + 1))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
