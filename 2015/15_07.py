from aocd import get_data, submit
DAY = 7
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")

wires = {}
for instr in data:
    m = instr.split()
    wires[m[-1]] = {
        'output': None,
        'input': m[:-2],
    }

def num(s):
    if s in wires:
        if not wires[s]['output']:
            wires[s]['output'] = execute(wires[s]['input'])
        return wires[s]['output']
    else:
        return int(s)

def execute(instr):
    match instr:
        case [n1]:
            return num(n1)
        case ['NOT', n1]:
            return ~num(n1)
        case [n1, 'AND', n2]:
            return num(n1) & num(n2)
        case [n1, 'OR', n2]:
            return num(n1) | num(n2)
        case [n1, 'LSHIFT', n2]:
            return num(n1) << num(n2)
        case [n1, 'RSHIFT', n2]:
            return num(n1) >> num(n2)

ans1 = num('a')
wires['b']['output'] = int(ans1)
for wire in wires:
    if wire != 'b':
        wires[wire]['output'] = None
ans2 = num('a')

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)