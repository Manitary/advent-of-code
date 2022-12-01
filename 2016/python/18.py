from aocd import get_data, submit
DAY = 18
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
LENGTH = len(data) + 1

def isTrap(row, i):
    if i == 0 or i == LENGTH:
        return 0
    return row[i-1] ^ row[i+1]

def nextRow(row):
    return [isTrap(row, i) for i in range(LENGTH+1)]
    
def numSafe(n, c):
    return n * (LENGTH - 1) - c

num1 = 40
num2 = 400000
row = [0] + [1 if c == '^' else 0 for c in data] + [0]
count = sum(row)
for i in range(num2 - 1):
    row = nextRow(row)
    count += sum(row)
    if i == num1 - 2:
        ans1 = numSafe(num1, count)

ans2 = numSafe(num2, count)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
