from aocd import get_data, submit
from intcode import Computer

DAY = 21
YEAR = 2019

INSTRUCTIONS_1 = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
NOT D T
NOT T T
AND T J
WALK
"""

INSTRUCTIONS_2 = """NOT E J
NOT H T
AND T J
NOT J J
NOT A T
NOT T T
AND B T
AND C T
NOT T T
AND T J
AND D J
RUN
"""


def execute_instructions(jumpdroid: Computer, instructions: str) -> int:
    jumpdroid.push(list(map(ord, instructions)))
    jumpdroid.run()
    return jumpdroid.output[-1]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = execute_instructions(Computer(data), INSTRUCTIONS_1)
    part2 = execute_instructions(Computer(data), INSTRUCTIONS_2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
