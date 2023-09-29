from typing import TypedDict

from aocd import get_data, submit

DAY = 7
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")


class Wire(TypedDict):
    input: list[str]
    output: int | None


def main() -> tuple[int, int]:
    wires: dict[str, Wire] = {}

    def num(s: str) -> int:
        if s not in wires:
            return int(s)
        wires[s]["output"] = (n := wires[s]["output"] or execute(wires[s]["input"]))
        return n

    def execute(instr: list[str]) -> int:
        match instr:
            case [n1]:
                return num(n1)
            case ["NOT", n1]:
                return ~num(n1)
            case [n1, "AND", n2]:
                return num(n1) & num(n2)
            case [n1, "OR", n2]:
                return num(n1) | num(n2)
            case [n1, "LSHIFT", n2]:
                return num(n1) << num(n2)
            case [n1, "RSHIFT", n2]:
                return num(n1) >> num(n2)
            case _:
                raise ValueError("Invalid instruction")

    for instr in data:
        m = instr.split()
        wires[m[-1]] = {
            "output": None,
            "input": m[:-2],
        }
    part1 = num("a")

    for wire in wires.values():
        wire["output"] = None
    wires["b"]["output"] = part1
    part2 = num("a")

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
