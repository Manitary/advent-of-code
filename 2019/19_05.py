from aocd import get_data, submit
from intcode import Computer
DAY = 5
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

computer = Computer()

computer.setProgram(data, input_=1)
*tests, ans1 = computer.run()

computer.setProgram(data, input_=5)
*tests, ans2 = computer.run()

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)