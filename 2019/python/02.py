from itertools import product

from aocd import get_data, submit
from intcode import Computer

DAY = 2
YEAR = 2019


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    computer = Computer()
    part1, part2 = 0, 0
    for noun, verb in product(range(1, 100), range(1, 100)):
        computer = Computer(program=data)
        computer[1] = noun
        computer[2] = verb
        computer.run()
        if noun == 12 and verb == 2:
            part1 = computer.state
            if part2:
                break
        if computer.state == 19690720:
            part2 = 100 * noun + verb
            if part1:
                break

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
