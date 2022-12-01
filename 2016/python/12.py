from aocd import get_data, submit
DAY = 12
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split("\n")
data = tuple(tuple(instr.split()) for instr in data)

def val(s):
    if s in registers:
        return registers[s]
    return int(s)

def executeInstruction(i):
    instr, *v = data[i]
    match instr:
        case 'cpy':
            registers[v[1]] = val(v[0])
        case 'inc':
            registers[v[0]] += 1
        case 'dec':
            registers[v[0]] -= 1
        case 'jnz':
            if val(v[0]) != 0:
                return i + val(v[1])
    return i + 1

def assemBunny(instr):
    i = 0
    while i < len(instr):
        i = executeInstruction(i)
    return registers['a']

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
ans1 = assemBunny(data)

# This will take forever by problem design, the solution is in 12_2.py
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
ans2 = assemBunny(data)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)