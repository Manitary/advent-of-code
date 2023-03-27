from aocd import get_data, submit
from functools import reduce
import re

DAY = 15
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = data.split("\n")


def chinese_remainder(n, a):
    ans = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        ans += a_i * pow(p, -1, n_i) * p
    return ans % prod


pattern = re.compile(r" (\d+)")
mods = []
residues = []
for i, row in enumerate(data):
    total, start = tuple(map(int, pattern.findall(row)))
    mods.append(total)
    residues.append(total - (start + i + 1))

ans1 = chinese_remainder(mods, residues)
submit(ans1, part="a", day=DAY, year=YEAR)

new_len = 11
mods.append(new_len)
residues.append(new_len - (len(mods)))
ans2 = chinese_remainder(mods, residues)
submit(ans2, part="b", day=DAY, year=YEAR)
