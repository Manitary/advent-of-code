import itertools as it

from aocd import get_data, submit

DAY = 1
YEAR = 2018


def main() -> tuple[int, int]:
    data = tuple(map(int, get_data(day=DAY, year=YEAR).split("\n")))
    visited: set[int] = {0}
    freq = 0
    for freq in it.accumulate(it.chain.from_iterable(it.repeat(data))):
        if freq in visited:
            break
        visited.add(freq)

    return sum(data), freq


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
