from aocd import get_data, submit
from intcode import Computer

DAY = 9
YEAR = 2019


def solve(data: str, n: int) -> int:
    computer = Computer(data, n)
    computer.run()
    return computer.pop()


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = solve(data, 1)
    part2 = solve(data, 2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
