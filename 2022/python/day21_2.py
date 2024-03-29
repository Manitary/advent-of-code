"""Solve Advent of Code Day 21 Year 2022."""
from operator import add, mul, sub, truediv
from typing import Callable

import sympy
from aocd import get_data, submit

DAY = 21
YEAR = 2022

Num = int | float
Operation = Callable[[Num, Num], Num]
Monkey = dict[str, sympy.Symbol | int | tuple[str, ...] | Operation]

OPERATORS: dict[str, Operation] = {"+": add, "-": sub, "*": mul, "/": truediv}


def parse_monkeys(data: str) -> tuple[dict[str, Monkey], Callable[[str], Num]]:
    """Parse the input.

    Format of input rows:
    - "$str: $int"
    - "$str: $str $op $str"

    Return:
    - A dictionary of monkeys with their corresponding data.
    - A function that, given a monkey, returns the number yelled by the monkey.
    """
    monkeys: dict[str, Monkey] = {}
    for row in data.split("\n"):
        name, job = row.split(": ")
        try:
            monkeys[name] = {"num": int(job)}
        except ValueError:
            arg1, op, arg2 = job.split()
            monkeys[name] = {
                "operation": OPERATORS[op],
                "args": tuple((arg1, arg2)),
            }

    def yell(monkey: str) -> Num:
        """Return the number yelled by the given monkey."""
        if "num" in monkeys[monkey]:
            return monkeys[monkey]["num"]
        return monkeys[monkey]["operation"](
            yell(monkeys[monkey]["args"][0]), yell(monkeys[monkey]["args"][1])
        )

    return monkeys, yell


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    part1, part2 = 0, 0
    data = get_data(day=DAY, year=YEAR)
    monkeys, yell = parse_monkeys(data)
    part1 = int(yell("root"))
    x = sympy.Symbol("x")
    monkeys["humn"]["num"] = x
    monkey_1, monkey_2 = monkeys["root"]["args"]
    part2 = int(sympy.solve(yell(monkey_1) - yell(monkey_2), x)[0])

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
