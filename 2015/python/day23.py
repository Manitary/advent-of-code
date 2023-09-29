from aocd import get_data, submit

DAY = 23
YEAR = 2015


def execute_instruction(
    registers: dict[str, int], idx: int, instruction: list[str]
) -> int:
    match instruction:
        case ["hlf", x]:
            registers[x] //= 2
            idx += 1
        case ["tpl", x]:
            registers[x] *= 3
            idx += 1
        case ["inc", x]:
            registers[x] += 1
            idx += 1
        case ["jmp", n]:
            idx += int(n)
        case ["jie", x, n]:
            if registers[x[0]] % 2 == 0:
                idx += int(n)
            else:
                idx += 1
        case ["jio", x, n]:
            if registers[x[0]] == 1:
                idx += int(n)
            else:
                idx += 1
        case _:
            raise ValueError("Invalid instruction")
    return idx


def run(registers: dict[str, int], program: list[list[str]]) -> int:
    i = 0
    while i < len(program):
        i = execute_instruction(registers, i, program[i])
    return registers["b"]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    program = [row.split() for row in data.split("\n")]

    registers = {"a": 0, "b": 0}
    part1 = run(registers, program)

    registers = {"a": 1, "b": 0}
    part2 = run(registers, program)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
