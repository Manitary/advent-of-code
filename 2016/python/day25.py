from itertools import count

from aocd import get_data, submit

DAY = 25
YEAR = 2016


def val(registers: dict[str, int], s: str | int) -> int:
    if s in registers:
        return registers[s]
    return int(s)


def execute_instruction(
    registers: dict[str, int], i: int, instructions: list[list[str]]
) -> tuple[int, int | None]:
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
                return i + val(registers, v[1]), None
        case "out":
            return i + 1, val(registers, v[0])
        case _:
            raise ValueError("Invalid OpCode")
    return i + 1, None


def assembunny(registers: dict[str, int], instructions: list[list[str]]) -> bool:
    i = 0
    visited: set[tuple[tuple[int, ...], int]] = set()
    signal_parity = 0
    while i < len(instructions):
        i, signal = execute_instruction(registers, i, instructions)
        if signal is not None:
            if signal != signal_parity:
                return False
            new_state = (tuple(registers.values()), signal_parity)
            if new_state in visited:
                return True
            visited.add(new_state)
            signal_parity = 1 - signal_parity
    return False


def reset_registers(registers: dict[str, int], initial_value: int = 0) -> None:
    for register in registers:
        registers[register] = initial_value if register == "a" else 0


def main() -> int:
    data = get_data(day=DAY, year=YEAR)
    data = [instr.split() for instr in data.split("\n")]

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    for a in count():
        reset_registers(registers, initial_value=a)
        if assembunny(registers, data):
            return a

    raise ValueError()


if __name__ == "__main__":
    ans1 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
