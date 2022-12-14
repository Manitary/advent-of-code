"""Solve Advent of Code Day 11 Year 2022."""

from __future__ import annotations
import re
from dataclasses import dataclass, field
from copy import deepcopy
from math import prod, lcm
from operator import add, mul
from aocd import get_data, submit

OPERATOR_TOKEN = {"+": add, "*": mul}
INT_REGEX = re.compile(r"(\d+)")


@dataclass
class Monkey:
    """A monkey.

    Attributes:
        items: a list of items held by the monkey.
        operation: the operation applied to the item when the monkey inspects it.
        worry_control: the operation applied to the item after the monkey inspected it.
        test_value: the number used for divisibility check.
        target_true: the target monkey (or its number) if test_value divides the item.
        target_false: the target monkey (or its number) if test_value does not divide the item.
        inspections: the number of inspections done by the monkey.
    """

    operation: callable
    test_value: int
    target_true: int | Monkey
    target_false: int | Monkey
    worry_control: callable = lambda x: x // 3
    items: list[int] = field(default_factory=list)
    inspections: int = field(default=0, init=False)

    def play(self) -> None:
        """Make the monkey inspect and throw all of its items according to its rules."""
        for item in self.items:
            new_item = self.worry_control(self.operation(item))
            if new_item % self.test_value:
                self.target_false.items.append(new_item)
            else:
                self.target_true.items.append(new_item)
        self.inspections += len(self.items)
        self.items = []


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


def parse_monkey(monkey_data: str) -> Monkey:
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
    return Monkey(
        items=starting_items,
        operation=operation,
        test_value=test_value,
        target_true=target_true,
        target_false=target_false,
    )


def monkey_business(zoo: list[Monkey]) -> int:
    """Return the level of monkey business of a list of monkeys.

    The level of monkey business is the product of the number of inspections
    done by the two most active monkeys.
    """
    return prod(sorted(monkey.inspections for monkey in zoo)[-2:])


def monkey_play(zoo: list[Monkey], num: int) -> int:
    """Let the monkeys in a given list play a given number of times."""
    for _ in range(num):
        for monkey in zoo:
            monkey.play()


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=11, year=2022).split("\n\n")
    zoo_1 = [parse_monkey(monkey_data) for monkey_data in data]
    for monkey in zoo_1:
        monkey.target_false = zoo_1[monkey.target_false]
        monkey.target_true = zoo_1[monkey.target_true]
    zoo_2 = deepcopy(zoo_1)
    # Part 1
    monkey_play(zoo=zoo_1, num=20)
    part1 = monkey_business(zoo_1)
    # Part 2
    total_worry = lcm(*(monkey.test_value for monkey in zoo_2))
    for monkey in zoo_2:
        monkey.worry_control = lambda x: x % total_worry
    monkey_play(zoo=zoo_2, num=10000)
    part2 = monkey_business(zoo_2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
