from collections import defaultdict
from itertools import permutations

from aocd import get_data, submit

DAY = 13
YEAR = 2015


def happiness(
    score: dict[frozenset[str], int], people: list[str], extra: str = ""
) -> int:
    return max(
        sum(score[frozenset((p1, p2))] for p1, p2 in zip(table, table[1:]))
        + (
            score[frozenset((table[0], extra))] + score[frozenset((table[-1], extra))]
            if extra
            else 0
        )
        for table in permutations(people)
    )


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [row.split() for row in data.split("\n")]

    score: dict[frozenset[str], int] = defaultdict(int)
    people: set[str] = set()
    for row in data:
        p1, p2 = row[0], row[-1][:-1]
        score[frozenset((p1, p2))] += int(f"{'' if row[2] == 'gain' else '-'}{row[3]}")
        people.add(p1)
        people.add(p2)

    people_list = list(people)
    part1 = happiness(score, people_list[:-1], people_list[-1])
    part2 = happiness(score, people_list)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
