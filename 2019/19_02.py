from aocd import get_data, submit
from intcode import Computer
from itertools import product
DAY = 2
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

computer = Computer()

ans1, ans2 = None, None
for noun, verb in product(range(1, 100), range(1, 100)):
    computer = Computer(program=data)
    computer[1] = noun
    computer[2] = verb
    computer.run()
    if noun == 12 and verb == 2:
        ans1 = computer.state
        if ans2:
            break
    if computer.state == 19690720:
        ans2 = 100*noun + verb
        if ans1:
            break

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)