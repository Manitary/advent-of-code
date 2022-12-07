from aocd import get_data, submit
from intcode import Computer

DAY = 9
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

computer = Computer(data, 1)
computer.run()
ans1 = computer.pop()

computer = Computer(data, 2)
computer.run()
ans2 = computer.pop()

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
