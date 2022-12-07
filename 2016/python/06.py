from aocd import get_data, submit
from collections import Counter

DAY = 6
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split()

count = [Counter() for _ in enumerate(data[0])]
for row in data:
    for i, char in enumerate(row):
        count[i][char] += 1

ans1 = "".join([c.most_common(1)[0][0] for c in count])
ans2 = "".join([c.most_common()[-1][0] for c in count])

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
