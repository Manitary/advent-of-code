from aocd import get_data, submit

DAY = 8
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split()


def realCount(s):
    count = 0
    encoded = 6
    i = 1
    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i + 1] == "\\" or s[i + 1] == '"':
                i += 2
                encoded += 4
            elif s[i + 1] == "x":
                i += 4
                encoded += 5
        else:
            i += 1
            encoded += 1
        count += 1
    return count, encoded


ans1, ans2 = 0, 0
for row in data:
    real, encoded = realCount(row)
    ans1 += len(row) - real
    ans2 += encoded - len(row)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
