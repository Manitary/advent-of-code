import enum
import functools
import re
from functools import cache

from aocd import get_data, submit

DAY = 15
YEAR = 2023

RE_INSTR = re.compile(r"(\w+)(-|=)(\d+)?")


class OP(enum.StrEnum):
    REMOVE = "-"
    UPDATE = "="


def hash_step(value: int, char: str) -> int:
    return (value + ord(char)) * 17 % 256


@cache
def hash_label(string: str) -> int:
    return functools.reduce(hash_step, string, 0)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).strip().split(",")

    part1 = sum(map(hash_label, data))

    boxes: list[dict[str, int]] = [{} for _ in range(256)]
    for instruction in data:
        match = RE_INSTR.match(instruction)
        assert match
        label, op, length = match.groups()
        box = hash_label(label)
        if op == OP.REMOVE:
            boxes[box].pop(label, None)
        elif op == OP.UPDATE:
            boxes[box][label] = int(length)
        else:
            raise ValueError("Invalid instruction")

    part2 = sum(
        i * j * length
        for i, box in enumerate(boxes, 1)
        for j, length in enumerate(box.values(), 1)
    )

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
