from aocd import get_data, submit
from copy import deepcopy

DAY = 23
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = [instr.split() for instr in data.split("\n")]

instructions = deepcopy(data)


def val(s):
    if s in registers:
        return registers[s]
    return int(s)


def executeInstruction(i, instructions):
    opcode, *v = instructions[i]
    match opcode:
        case "cpy":
            registers[v[1]] = val(v[0])
        case "inc":
            registers[v[0]] += 1
        case "dec":
            registers[v[0]] -= 1
        case "jnz":
            if val(v[0]) != 0:
                return i + val(v[1])
        case "tgl":
            if 0 <= (j := i + val(v[0])) < len(instructions):
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
    return i + 1


def assemBunny(instr):
    i = 0
    while i < len(instr):
        i = executeInstruction(i, instr)
    return registers["a"]


instructions = deepcopy(data)
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
ans1 = assemBunny(instructions)
submit(ans1, part="a", day=DAY, year=YEAR)

# This will take forever by problem design, the solution is in 23_2.py
instructions = deepcopy(data)
registers = {"a": 12, "b": 0, "c": 0, "d": 0}
ans2 = assemBunny(instructions)
submit(ans2, part="b", day=DAY, year=YEAR)
