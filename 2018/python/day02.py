import itertools
import math
from collections import Counter

from aocd import get_data, submit

DAY = 2
YEAR = 2018


def main() -> tuple[int, str]:
    data = get_data(day=DAY, year=YEAR).split("\n")
    freqs = (Counter(word) for word in data)
    part1 = math.prod(
        map(sum, zip(*((2 in freq.values(), 3 in freq.values()) for freq in freqs)))
    )

    part2 = ""
    for w1, w2 in itertools.combinations(data, 2):
        diffs = 0
        diff_pos = 0
        for c1, c2, idx in zip(w1, w2, range(len(w1))):
            if c1 == c2:
                continue
            diffs += 1
            diff_pos = idx
            if diffs > 1:
                break
        if diffs == 1:
            part2 = "".join(c for i, c in enumerate(w1) if i != diff_pos)
            break

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
