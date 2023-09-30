from collections import defaultdict
from typing import Self

from aocd import get_data, submit

DAY = 10
YEAR = 2016


class Output:
    def __init__(self) -> None:
        self.value: int | None = None

    def add_value(self, value: int) -> None:
        self.value = value


class Bot:
    def __init__(self) -> None:
        self.values: list[int] = []
        self.high: Self | Output = Output()
        self.low: Self | Output = Output()

    def add_value(self, value: int) -> Self | None:
        self.values.append(value)

    def sort_values(self) -> None:
        self.values.sort()

    def give_values(self) -> None:
        self.sort_values()
        self.low.add_value(self.values[0])
        self.high.add_value(self.values[1])


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")

    queue: list[Bot] = []
    bots: dict[int, Bot] = defaultdict(Bot)
    outputs: dict[int, Output] = defaultdict(Output)

    for row in data:
        instr = row.split()
        if instr[0] == "value":
            num = int(instr[-1])
            bots[num].add_value(int(instr[1]))
            if len(bots[num].values) == 2:
                queue.append(bots[num])
        else:
            num, low, high = int(instr[1]), int(instr[6]), int(instr[-1])
            if instr[5] == "bot":
                bots[num].low = bots[low]
            else:
                bots[num].low = outputs[low]
            if instr[-2] == "bot":
                bots[num].high = bots[high]
            else:
                bots[num].high = outputs[high]
    pair = {17, 61}
    part1, part2 = 0, 0
    while queue:
        curr = queue.pop(0)
        if (not part1) and set(curr.values) == pair:
            part1 = tuple(bots)[tuple(bots.values()).index(curr)]
        curr.give_values()
        if isinstance(curr.low, Bot) and len(curr.low.values) == 2:
            queue.append(curr.low)
        if isinstance(curr.high, Bot) and len(curr.high.values) == 2:
            queue.append(curr.high)
        if (not part2) and outputs[0].value and outputs[1].value and outputs[2].value:
            part2 = outputs[0].value * outputs[1].value * outputs[2].value
        if part1 and part2:
            break
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
