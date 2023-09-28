from aocd import get_data, submit
from intcode import Computer

DAY = 5
YEAR = 2019


def solve(data: str, n: int) -> int:
    computer = Computer(program=data, input_=n)
    computer.run()
    return computer.output[-1]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = solve(data, 1)
    part2 = solve(data, 5)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
