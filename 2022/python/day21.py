"""Solve Advent of Code Day 21 Year 2022."""

from typing import Callable
from operator import add, mul, sub, truediv
from aocd import get_data, submit

OPERATORS = {"+": add, "*": mul, "-": sub, "/": truediv}


def parse_monkeys(
    data: str,
) -> dict[
    str, dict[str, int | str | Callable[[int | float, int | float], int | float]]
]:
    """Parse the input.

    Format of input rows:
    - "$str: $int"
    - "$str: $str $op $str"

    Return:
    - A dictionary of monkeys with their corresponding data.
    - A function that, given a monkey, returns the number yelled by the monkey.
    - A function that, given a monkey, returns whether its number depends on the number of "humn".
    """
    monkeys = {}
    for row in data.split("\n"):
        row = row.split()
        if len(row) == 2:
            monkeys[row[0][:-1]] = {"num": int(row[1])}
        else:
            monkeys[row[0][:-1]] = {
                "operation": OPERATORS[row[2]],
                "args": tuple((row[1], row[3])),
                "arg_1": row[1],
                "arg_2": row[3],
            }

    def yell(monkey: str) -> int | float:
        """Return the number yelled by the given monkey."""
        if "num" in monkeys[monkey]:
            return monkeys[monkey]["num"]
        return monkeys[monkey]["operation"](
            yell(monkeys[monkey]["args"][0]), yell(monkeys[monkey]["args"][1])
        )

    def has_human(monkey: str) -> bool:
        """Return whether the number yelled by the given monkey depends on the monkey "humn"."""
        if monkey == "humn":
            return True
        if "num" in monkeys[monkey]:
            return False
        return any(has_human(monkeys[monkey]["args"][x]) for x in (0, 1))

    return monkeys, yell, has_human


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=21, year=2022)
    monkeys, yell, has_human = parse_monkeys(data)
    part1 = int(yell("root"))
    # Only one side of root depends on "humn", find which one.
    q = next(x for x in (0, 1) if has_human(monkeys["root"]["args"][x]))
    # Compute the number that does not depend on "humn".
    goal = yell(monkeys["root"]["args"][1 - q])
    # Since the other number depends linearly on "humn", find the answer with a binary search.
    left, right = 1, 10**15
    while left < right:
        mid = (left + right) // 2
        monkeys["humn"]["num"] = mid
        ans = yell(monkeys["root"]["args"][q])
        if ans == goal:
            part2 = mid
            break
        if ans > goal:
            left = mid
        elif ans < goal:
            right = mid

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
