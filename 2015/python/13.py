from aocd import get_data, submit
from itertools import permutations
from collections import defaultdict

DAY = 13
YEAR = 2015

data = get_data(day=DAY, year=YEAR)
data = [row.split() for row in data.split("\n")]

score = defaultdict(int)
people = set()

for row in data:
    p1, p2 = row[0], row[-1][:-1]
    score[frozenset((p1, p2))] += int(f"{'' if row[2] == 'gain' else '-'}{row[3]}")
    people.add(p1)
    people.add(p2)

people = list(people)


def happiness(people, extra=None):
    ans = 0
    for table in permutations(people):
        curr = 0
        for p1, p2 in zip(table, table[1:]):
            curr += score[frozenset((p1, p2))]
        if extra:
            curr += (
                score[frozenset((table[0], extra))]
                + score[frozenset((table[-1], extra))]
            )
        if curr > ans:
            ans = curr
    return ans


ans1 = happiness(people[:-1], people[-1])
ans2 = happiness(people)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
