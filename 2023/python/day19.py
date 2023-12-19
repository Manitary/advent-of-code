import enum
import functools
import itertools
import math
import re
from typing import Self

from aocd import get_data, submit

DAY = 19
YEAR = 2023

type Part = dict[str, int]
type PartRange = dict[str, tuple[int, int]]

RE_NUMS = re.compile(r"\d+")

RATINGS = "xmas"


class Op(enum.Enum):
    NOOP = ""
    LT = "<"
    GT = ">"


class Status(enum.Enum):
    CONTINUE = 0
    ACCEPT = 1
    REJECT = 2


class Instruction:
    __slots__ = (
        "next_label",
        "rating",
        "op",
        "value",
        "status",
        "_next_success",
        "_next_fail",
    )

    def __init__(
        self,
        next_label: str = "",
        rating: str = "",
        op: Op = Op.NOOP,
        value: int = 0,
        status: Status = Status.CONTINUE,
    ) -> None:
        self.next_label = next_label
        self.rating = rating
        self.op = op
        self.value = value
        self.status = status
        self._next_success: Self | None = None
        self._next_fail: Self | None = None

    @classmethod
    def from_str(cls, string: str) -> Self:
        if ":" not in string:
            return cls(next_label=string)
        a, b = string.split(":")
        return cls(next_label=b, rating=a[0], op=Op(a[1]), value=int(a[2:]))

    @property
    def success(self) -> Self:
        if self._next_success is None:
            return type(self)()
        return self._next_success

    @success.setter
    def success(self, _next: Self) -> None:
        self._next_success = _next

    @property
    def fail(self) -> Self:
        if self._next_fail is None:
            return type(self)()
        return self._next_fail

    @fail.setter
    def fail(self, _next: Self) -> None:
        self._next_fail = _next

    def accept_part(self, part: Part) -> bool:
        if (self.op == Op.GT and part[self.rating] <= self.value) or (
            self.op == Op.LT and part[self.rating] >= self.value
        ):
            return False
        return True

    def validate_parts(self, parts: PartRange) -> tuple[PartRange, PartRange]:
        """Return a tuple accepted parts | rejected parts."""
        if self.op == Op.NOOP:
            return parts, {}

        r = parts[self.rating]

        if self.op == Op.LT:
            if r[1] < self.value:
                return parts, {}
            if r[0] >= self.value:
                return {}, parts
            return parts | {self.rating: (r[0], self.value - 1)}, parts | {
                self.rating: (self.value, r[1])
            }

        if self.op == Op.GT:
            if r[1] <= self.value:
                return {}, parts
            if r[0] > self.value:
                return parts, {}
            return parts | {self.rating: (self.value + 1, r[1])}, parts | {
                self.rating: (r[0], self.value)
            }

        raise ValueError("Unexpected error")


def parse_rules(data: str) -> dict[str, list[Instruction]]:
    rules = {
        "A": [Instruction(status=Status.ACCEPT)],
        "R": [Instruction(status=Status.REJECT)],
    } | {
        r[0]: list(map(Instruction.from_str, r[1][:-1].split(",")))
        for row in data.splitlines()
        if (r := row.split("{"))
    }
    for label, instructions in rules.items():
        if label in "AR":
            continue
        for i, instruction in enumerate(instructions):
            instruction.success = rules[instruction.next_label][0]
            if i < len(instructions) - 1:
                instruction.fail = instructions[i + 1]
    return rules


def parse_inputs(data: str) -> list[dict[str, int]]:
    return [dict(zip(RATINGS, map(int, RE_NUMS.findall(i)))) for i in data.splitlines()]


def _workflow(part: dict[str, int], instruction: Instruction) -> int:
    while instruction.status == Status.CONTINUE:
        if instruction.accept_part(part):
            instruction = instruction.success
        else:
            instruction = instruction.fail

    return sum(part.values()) if instruction.status == Status.ACCEPT else 0


def num_valid_inputs(instr: Instruction, min_range: int, max_range: int) -> int:
    queue = [({r: (min_range, max_range) for r in RATINGS}, instr)]
    ans = 0
    while queue:
        ranges, rule = queue.pop(0)
        if rule.status == Status.ACCEPT:
            ans += math.prod(x[1] - x[0] + 1 for x in itertools.chain(ranges.values()))
            continue
        if rule.status == Status.REJECT:
            continue
        accepted, rejected = rule.validate_parts(ranges)
        if accepted:
            queue.append((accepted, rule.success))
        if rejected:
            queue.append((rejected, rule.fail))

    return ans


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    rules, inputs = data.split("\n\n")
    rules = parse_rules(rules)
    inputs = parse_inputs(inputs)

    first_instruction = rules["in"][0]
    workflow = functools.partial(_workflow, instruction=first_instruction)

    part1 = sum(map(workflow, inputs))
    part2 = num_valid_inputs(first_instruction, 1, 4000)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
