"""Solve Advent of Code Day 11 Year 2022."""

import re
from dataclasses import dataclass, field
from collections import deque
from copy import deepcopy
from math import prod, lcm
from functools import cached_property
from aocd import get_data, submit

PATTERN_OP = r"Operation: new = ((?:old\s?|\*\s?|\+\s?|\d+\s?)+)$"
re.compile(PATTERN_OP)

@dataclass
class Monkey:
    operation: callable
    test: int
    true: int
    false: int
    worry_control: callable = lambda x: x//3
    items: deque[int] = field(default_factory=deque)
    inspections: int = field(default=0, init=False)

    def clear_items(self):
        self.items = []

    def grab_item(self):
        return self.items.popleft()

    def obtain_item(self, item):
        self.items.append(item)

    def set_worry_control(self, worry_control):
        self.worry_control = worry_control

    def inspect(self):
        item = self.worry_control(self.operation(self.grab_item()))
        self.inspections += 1
        target_num = self.false if item % self.test else self.true
        return item, target_num

    def play(self):
        while self.items:
            yield self.inspect()

@dataclass
class Zoo:
    _monkeys: list[Monkey] = field(default_factory=list)

    def __getitem__(self, num: int):
        return self._monkeys[num]

    @cached_property
    def total_worry(self):
        return lcm(*(monkey.test for monkey in self._monkeys))

    def set_worry_control(self, worry_control):
        for monkey in self._monkeys:
            monkey.set_worry_control(worry_control)

    def addMonkey(self, monkey_data: str):
        monkey_data = monkey_data.split('\n')
        starting_items = deque(map(int, re.findall(r"(\d+)", monkey_data[1])))
        operation = eval("lambda old: " + re.findall(PATTERN_OP, monkey_data[2])[0])
        test = int(monkey_data[3].split()[-1])
        true = int(monkey_data[4].split()[-1])
        false = int(monkey_data[5].split()[-1])
        new_monkey = Monkey(items=starting_items, operation=operation, test=test, true=true, false=false)
        self._monkeys.append(new_monkey)

    def play(self):
        for monkey in self._monkeys:
            for item, target in monkey.play():
                self[target].obtain_item(item)

    @property
    def inspections(self):
        return (monkey.inspections for monkey in self._monkeys)

    @property
    def monkey_business(self):
        return prod(sorted(self.inspections)[-2:])

def main():
    data = get_data(day=11, year=2022)
    data = data.split('\n\n')

    zoo_1 = Zoo()
    for monkey in data:
        zoo_1.addMonkey(monkey)

    zoo_2 = deepcopy(zoo_1)

    for _ in range(20):
        zoo_1.play()

    part1 = zoo_1.monkey_business

    zoo_2.set_worry_control(lambda x: x % zoo_2.total_worry)

    for _ in range(10000):
        zoo_2.play()

    part2 = zoo_2.monkey_business
    return part1, part2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
