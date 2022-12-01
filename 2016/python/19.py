from aocd import get_data, submit
from math import log
DAY = 19
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = int(data)

def part1(num):
    return (num << 1) & ~(1 << num.bit_length()) | 1

def part2(num):
    power = 3**int(log(num, 3))
    residue = num - power
    if residue == 0:
        return power
    if residue < power:
        return residue
    if residue > power:
        return residue + 1

ans1 = part1(data)
ans2 = part2(data)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)