from aocd import get_data, submit
DAY = 1
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
data = sorted([sum(map(int, row.split('\n'))) for row in list(data.split('\n\n'))])

ans1 = data[-1]
ans2 = sum(data[-3:])

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)