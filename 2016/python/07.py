from aocd import get_data, submit

DAY = 7
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split()


def isABBA(s, i):
    return s[i] == s[i + 3] != s[i + 1] == s[i + 2] and s[i : i + 4].isalpha()


def isABA(s, i):
    return s[i] == s[i + 2] != s[i + 1] and s[i : i + 3].isalpha()


def isTLS(s):
    ABBA = False
    brackets = 0
    for i in range(len(s) - 3):
        if s[i] == "[":
            brackets += 1
        elif s[i] == "]":
            brackets -= 1
        else:
            if brackets and isABBA(s, i):
                return False
            elif (not ABBA) and isABBA(s, i):
                ABBA = True
    return ABBA


def isSSL(s):
    outside = set()
    inside = set()
    brackets = 0
    for i in range(len(s) - 2):
        if s[i] == "[":
            brackets += 1
        elif s[i] == "]":
            brackets -= 1
        else:
            if isABA(s, i):
                aba = s[i : i + 3]
                bab = aba[1] + aba[0] + aba[1]
                if brackets:
                    if bab in outside:
                        return True
                    inside.add(aba)
                else:
                    if bab in inside:
                        return True
                    outside.add(aba)
    return False


ans1, ans2 = 0, 0
for row in data:
    if isTLS(row):
        ans1 += 1
    if isSSL(row):
        ans2 += 1

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
