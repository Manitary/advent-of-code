from aocd import get_data, submit
DAY = 23
YEAR = 2015

data = get_data(day=DAY, year=YEAR)
program = [row.split() for row in data.split('\n')]

def executeInstruction(idx: int, instruction: list[str]):
    match instruction:
        case ['hlf', x]:
            registers[x] //= 2
            idx += 1
        case ['tpl', x]:
            registers[x] *= 3
            idx += 1
        case ['inc', x]:
            registers[x] += 1
            idx += 1
        case ['jmp', n]:
            idx += int(n)
        case ['jie', x, n]:
            if registers[x[0]] % 2 == 0:
                idx += int(n)
            else:
                idx += 1
        case ['jio', x, n]:
            if registers[x[0]] == 1:
                idx += int(n)
            else:
                idx += 1
    return idx

def run(program: list[list[str]]):
    i = 0
    while i < len(program):
        i = executeInstruction(i, program[i])
    return registers['b']

registers = {'a': 0, 'b': 0}
ans1 = run(program)

registers = {'a': 1, 'b': 0}
ans2 = run(program)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)