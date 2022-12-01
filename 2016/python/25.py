from aocd import get_data, submit
from itertools import count
from typing import Union
DAY = 25
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = [instr.split() for instr in data.split("\n")]

def val(s: Union[str, int]):
    if s in registers:
        return registers[s]
    return int(s)

def executeInstruction(i: int, instructions: list[list[str]]):
    opcode, *v = instructions[i]
    match opcode:
        case 'cpy':
            registers[v[1]] = val(v[0])
        case 'inc':
            registers[v[0]] += 1
        case 'dec':
            registers[v[0]] -= 1
        case 'jnz':
            if val(v[0]) != 0:
                return i + val(v[1]), None
        case 'out':
            return i + 1, val(v[0])
    return i + 1, None

def assemBunny(instructions: list[list[str]]):
    i = 0
    visited = set()
    signal_parity = 0
    while i < len(instructions):
        i, signal = executeInstruction(i, instructions)
        if signal is not None:
            if signal != signal_parity:
                return False
            new_state = (tuple(registers.values()), signal_parity)
            if new_state in visited:
                return True
            visited.add(new_state)
            signal_parity = 1 - signal_parity
    return False

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def resetRegisters(initialValue: int = 0):
    for register in registers:
        registers[register] = initialValue if register == 'a' else 0

for a in count():
    resetRegisters(initialValue=a)
    finished = assemBunny(data)
    if finished:
        ans1 = a
        break

submit(ans1, part="a", day=DAY, year=YEAR)