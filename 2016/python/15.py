from aocd import get_data, submit
from functools import reduce
from re import findall, compile
DAY = 15
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = data.split("\n")

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

pattern = r" (\d+)"
compile(pattern)

mods = []
residues = []
for i, row in enumerate(data):
    total, start = tuple(map(int, findall(pattern, row)))
    mods.append(total)
    residues.append(total - (start + i + 1))

ans1 = chinese_remainder(mods, residues)
submit(ans1, part="a", day=DAY, year=YEAR)

new_len = 11
mods.append(new_len)
residues.append(new_len - (len(mods)))
ans2 = chinese_remainder(mods, residues)
submit(ans2, part="b", day=DAY, year=YEAR)
