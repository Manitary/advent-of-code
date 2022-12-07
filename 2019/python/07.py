from aocd import get_data, submit
from intcode import Computer
from itertools import permutations

DAY = 7
YEAR = 2019

data = get_data(day=DAY, year=YEAR)


ans1 = 0
for phase in permutations(range(5)):
    input_ = 0
    for value in phase:
        amp = Computer(program=data, input_=[value, input_])
        amp.run()
        input_ = amp.pop()
    ans1 = max(ans1, input_)

ans2 = 0
for phase in permutations(range(5, 10)):
    amps = [Computer(data, phase[i]) for i in range(5)]
    amps[0].push(0)
    curr = 0
    while any(amp.running for amp in amps):
        next_ = (curr + 1) % 5
        amps[curr].run()
        while amps[curr].output:
            if amps[next_].running:
                amps[next_].push(amps[curr].pop())
            else:
                break
        curr = next_
    ans2 = max(ans2, amps[-1].pop())

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
