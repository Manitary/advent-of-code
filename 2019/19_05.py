from aocd import get_data, submit
from intcode import Computer
DAY = 5
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

computer = Computer()

computer.setProgram(data, input_=[1])
computer.run()
ans1 = computer.output[-1]

computer.setProgram(data, input_=[5])
computer.run()
ans2 = computer.output[-1]

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)