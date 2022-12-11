"""Solve Advent of Code Day 11 Year 2022."""

import re
from copy import deepcopy
from functools import cache
from math import prod
from operator import add, mul
from aocd import get_data, submit

OPERATOR_TOKEN = {"+": add, "*": mul}
INT_REGEX = re.compile(r"(\d+)")

# Monkey attributes.
ITEMS = "items"
OPERATION = "op"
TEST = "test"
TRUE = "true"
FALSE = "false"
INSPECT = "inspect"


def create_operation(operation: list[str]) -> callable:
    """Return a lambda function corresponding to the given operation.

    Input format:
        ["old", $operator, $arg_2]

    $operator: "+" or "*".
    $arg_2: "old" or a string representing an integer.
    """
    _, operator, arg_2 = operation
    operator = OPERATOR_TOKEN[operator]
    return lambda x: operator(x, x if arg_2 == "old" else int(arg_2))


def parse_monkey(monkey_data: str) -> dict:
    """Return a monkey corresponding to the given data.

    Input format:
        "Monkey $number:
            Starting items: $int, ..., $int
            Operation: new = $function(old)
            Test: divisible by $int
            If true: throw to monkey $int
            If false: throw to monkey $int"
    """
    monkey_data = monkey_data.split("\n")
    starting_items = list(map(int, INT_REGEX.findall(monkey_data[1])))
    operation = create_operation(monkey_data[2].split()[-3:])
    test_value = int(monkey_data[3].split()[-1])
    target_true = int(monkey_data[4].split()[-1])
    target_false = int(monkey_data[5].split()[-1])
    return {
        ITEMS: starting_items,
        OPERATION: operation,
        TEST: test_value,
        TRUE: target_true,
        FALSE: target_false,
        INSPECT: 0,
    }


def monkey_business(monkeys: list[dict], num: int, part: int = 1) -> int:
    """Return the monkey business value of a given list of monkeys after num rounds."""
    # Calculate the appropriate method for keeping worries in check.
    if part == 1:
        worry_control = lambda x: x // 3
    else:
        total = prod(monkey[TEST] for monkey in monkeys)
        worry_control = lambda x: x % total

    # Create the corresponding function to compute a step of an item's orbit.
    @cache
    def result(worry_control: callable, source: int, item: int) -> tuple[int, int]:
        """Return the target monkey and item, after inspection by the source monkey."""
        new_item = worry_control(monkeys[source][OPERATION](item))
        if new_item % monkeys[source][TEST]:
            target = monkeys[source][FALSE]
        else:
            target = monkeys[source][TRUE]
        return target, new_item

    # Each monkey inspects all of its items during a round:
    # that means we can analyse the orbit of each item separately.
    # This removes the need of pushing/popping items between the monkeys' lists of items.
    for i, monkey in enumerate(monkeys):
        for item in monkey[ITEMS]:
            turn = 0
            curr = i
            while turn < num:
                new, item = result(worry_control, curr, item)
                monkeys[curr][INSPECT] += 1
                if new < curr:
                    turn += 1
                curr = new
    return prod(sorted(monkey[INSPECT] for monkey in monkeys)[-2:])


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=11, year=2022).split("\n\n")
    monkeys_1 = [parse_monkey(monkey_data) for monkey_data in data]
    monkeys_2 = deepcopy(monkeys_1)
    part1 = monkey_business(monkeys=monkeys_1, num=20, part=1)
    part2 = monkey_business(monkeys=monkeys_2, num=10000, part=2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
