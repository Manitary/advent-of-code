from itertools import permutations

from aocd import get_data, submit
from intcode import Computer

DAY = 7
YEAR = 2019


def part_1(data: str) -> int:
    ans = 0
    for phase in permutations(range(5)):
        input_ = 0
        for value in phase:
            amp = Computer(program=data, input_=[value, input_])
            amp.run()
            input_ = amp.pop()
        ans = max(ans, input_)
    return ans


def part_2(data: str) -> int:
    ans = 0
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
        ans = max(ans, amps[-1].pop())
    return ans


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    part1 = part_1(data)
    part2 = part_2(data)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
