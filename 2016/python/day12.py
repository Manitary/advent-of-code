from typing import Sequence

from aocd import get_data, submit

DAY = 12
YEAR = 2016


def val(registers: dict[str, int], s: str) -> int:
    if s in registers:
        return registers[s]
    return int(s)


def execute_instruction(
    registers: dict[str, int], i: int, data: Sequence[Sequence[str]]
) -> int:
    instr, *v = data[i]
    match instr:
        case "cpy":
            registers[v[1]] = val(registers, v[0])
        case "inc":
            registers[v[0]] += 1
        case "dec":
            registers[v[0]] -= 1
        case "jnz":
            if val(registers, v[0]) != 0:
                return i + val(registers, v[1])
        case _:
            raise ValueError("Instruction not registered")
    return i + 1


def assembunny(registers: dict[str, int], data: Sequence[Sequence[str]]) -> int:
    i = 0
    while i < len(data):
        i = execute_instruction(registers, i, data)
    return registers["a"]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    data = tuple(tuple(instr.split()) for instr in data)

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    part1 = assembunny(registers, data)

    # This will take forever by problem design, the solution is in 12_2.py
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    part2 = assembunny(registers, data)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
