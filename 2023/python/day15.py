import enum
import functools
import re
from functools import cache
from typing import NamedTuple

from aocd import get_data, submit

RE_INSTR = re.compile(r"(\w+)(-|=)(\d+)?")


class OP(enum.StrEnum):
    REMOVE = "-"
    UPDATE = "="


Lens = NamedTuple("Lens", [("label", str), ("focal_length", int)])


class LabelNotFoundError(Exception):
    ...


class Box:
    def __init__(self, num: int) -> None:
        self.number = num
        self.lenses: list[Lens] = []

    def locate_label(self, label: str) -> int:
        try:
            idx = next(i for i, lens in enumerate(self.lenses) if lens.label == label)
        except StopIteration as e:
            raise LabelNotFoundError from e
        return idx

    def remove_label(self, label: str) -> None:
        try:
            idx = self.locate_label(label)
        except LabelNotFoundError:
            return
        del self.lenses[idx]

    def update_lens(self, lens: Lens) -> None:
        try:
            idx = self.locate_label(lens.label)
        except LabelNotFoundError:
            self.lenses.append(lens)
        else:
            self.lenses[idx] = lens

    def focusing_power(self) -> int:
        return sum(
            (1 + self.number) * i * lens.focal_length
            for i, lens in enumerate(self.lenses, 1)
        )


def hash_step(value: int, char: str) -> int:
    return (value + ord(char)) * 17 % 256


@cache
def hash_label(string: str) -> int:
    return functools.reduce(hash_step, string, 0)


def main() -> tuple[int, int]:
    data = get_data().strip().split(",")

    part1 = sum(map(hash_label, data))

    boxes: list[Box] = [Box(i) for i in range(256)]
    for instruction in data:
        match = RE_INSTR.match(instruction)
        if not match:
            raise ValueError("Invalid instruction")
        label, op, length = match.groups()
        box = hash_label(label)
        if op == OP.REMOVE:
            boxes[box].remove_label(label)
        elif op == OP.UPDATE:
            boxes[box].update_lens(Lens(label, int(length)))
        else:
            raise ValueError("Invalid instruction")

    part2 = sum(box.focusing_power() for box in boxes)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
