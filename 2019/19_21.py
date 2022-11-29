from aocd import get_data, submit
from intcode import Computer
DAY = 21
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

def executeInstructions(instructions: str):
    jumpdroid = Computer(data)
    jumpdroid.push(list(map(ord, instructions)))
    jumpdroid.run()
    return jumpdroid.output[-1]

instructions_1 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
NOT D T
NOT T T
AND T J
WALK
'''

instructions_2 = '''NOT E J
NOT H T
AND T J
NOT J J
NOT A T
NOT T T
AND B T
AND C T
NOT T T
AND T J
AND D J
RUN
'''

ans1 = executeInstructions(instructions_1)
ans2 = executeInstructions(instructions_2)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)