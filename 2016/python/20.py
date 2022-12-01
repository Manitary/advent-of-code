from aocd import get_data, submit
DAY = 20
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

MIN = 0
MAX = 2**32 - 1

# Flatten intervals
intervals = []
for row in data.split():
    ans = []
    new = list(map(int, row.split('-')))
    added = False
    for i, interval in enumerate(intervals):
        # The +-1 makes contiguous intervals merge
        if interval[1] < new[0] - 1:
            ans.append(interval)
        elif interval[0] > new[1] + 1:
            ans.append(new)
            ans += intervals[i:]
            added = True
            break
        else:
            new[0] = min(new[0], interval[0])
            new[1] = max(new[1], interval[1])
    if not added:
        ans.append(new)
    intervals = ans

ans1 = intervals[0][1] + 1
ans2 = intervals[0][0] - MIN
for a, b in zip((x[0] for x in intervals[1:]), (x[1] for x in intervals)):
    ans2 += a - b - 1
ans2 += MAX - intervals[-1][1]

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)