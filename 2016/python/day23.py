from copy import deepcopy

from aocd import get_data, submit

DAY = 23
YEAR = 2016


def val(registers: dict[str, int], s: str) -> int:
    if s in registers:
        return registers[s]
    return int(s)


def execute_instruction(
    registers: dict[str, int], i: int, instructions: list[list[str]]
) -> int:
    opcode, *v = instructions[i]
    match opcode:
        case "cpy":
            registers[v[1]] = val(registers, v[0])
        case "inc":
            registers[v[0]] += 1
        case "dec":
            registers[v[0]] -= 1
        case "jnz":
            if val(registers, v[0]) != 0:
                return i + val(registers, v[1])
        case "tgl":
            if 0 <= (j := i + val(registers, v[0])) < len(instructions):
                match instructions[j]:
                    case [opcode, _]:
                        if opcode == "inc":
                            instructions[j][0] = "dec"
                        else:
                            instructions[j][0] = "inc"
                    case [opcode, _, _]:
                        if opcode == "jnz":
                            instructions[j][0] = "cpy"
                        else:
                            instructions[j][0] = "jnz"
                    case _:
                        raise ValueError("Invalid instruction")
        case _:
            raise ValueError("Invalid OpCode")
    return i + 1


def assembunny(registers: dict[str, int], instr: list[list[str]]) -> int:
    i = 0
    while i < len(instr):
        i = execute_instruction(registers, i, instr)
    return registers["a"]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [instr.split() for instr in data.split("\n")]

    instructions = deepcopy(data)
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    part1 = assembunny(registers, instructions)

    # This will take forever by problem design, the solution is in 23_2.py
    instructions = deepcopy(data)
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    part2 = assembunny(registers, instructions)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
