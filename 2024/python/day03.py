import re

mul = re.compile(r"mul\((\d+),(\d+)\)")
mul_not = re.compile(r"(?:do\(\)|don't\(\)|mul\((\d+),(\d+)\))")


with open("input.txt") as f:
    data = f.read()

print(sum(int(g.group(1)) * int(g.group(2)) for g in mul.finditer(data)))

ans = 0
m = True
for g in mul_not.finditer(data):
    if g.group(0).startswith("do("):
        m = Trsue
    elif g.group(0).startswith("don"):
        m = False
    else:
        if m:
            ans += int(g.group(1)) * int(g.group(2))

print(ans)