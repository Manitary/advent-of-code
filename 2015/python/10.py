from aocd import get_data, submit

DAY = 10
YEAR = 2015

data = get_data(day=DAY, year=YEAR)


def say(s):
    ans = ""
    count = 1
    new = s[0]
    for c in iter(s[1:]):
        if c != new:
            ans += f"{count}{new}"
            new = c
            count = 1
        else:
            count += 1
    ans += f"{count}{new}"
    return ans


for i in range(50):
    data = say(data)
    if i == 39:
        ans1 = len(data)

ans2 = len(data)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
