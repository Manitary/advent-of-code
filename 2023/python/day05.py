import itertools
from typing import Sequence

from aocd import get_data, submit

type Rule = list[tuple[int, int, int]]
type Rules = list[Rule]
type Interval = tuple[int, int]


def parse_input(input_: str) -> tuple[list[int], Rules]:
    data = input_.split("\n\n")
    seeds = list(map(int, data[0].split()[1:]))
    rules: Rules = []
    for i, instr in enumerate(data[1:]):
        rules.append([])
        for nums in instr.splitlines()[1:]:
            x = tuple(map(int, nums.split()))
            rules[i].append((x[0], x[1], x[2]))
        rules[-1].sort(key=lambda m: m[1])
    return seeds, rules


def intersect_intervals(
    i1: Interval, i2: Interval
) -> tuple[Interval | None, list[Interval]]:
    """Intersect interval i1 with interval i2.

    Return:
    - The intersection of i1 and i2, if any.
    - The list of sub-intervals of i1 that do not intersect i2.

    All intervals are represented as tuples of left/right bounds."""
    if i1[1] < i2[0] or i1[0] > i2[1]:
        return None, [i1]
    residues: list[Interval] = []
    if i1[0] < i2[0]:
        residues.append((i1[0], i2[0] - 1))
        left = i2[0]
    else:
        left = i1[0]
    if i1[1] > i2[1]:
        residues.append((i2[1] + 1, i1[1]))
        right = i2[1]
    else:
        right = i1[1]
    return (left, right), residues


def update_intervals(intervals: list[Interval], rule: Rule) -> list[Interval]:
    """Transform the list of intervals according to the given rule.

    Rule is a `tuple[int, int, int]`:
    - Left bound of the new interval
    - Left bound of the original interval
    - Size of the interval

    The original list is destroyed in the process."""
    new_range: list[Interval] = []
    while intervals:
        s = intervals.pop(0)
        for r in rule:
            intersection, residues = intersect_intervals(s, (r[1], r[1] + r[2] - 1))
            if not intersection:
                continue
            new_range.append(
                (intersection[0] - r[1] + r[0], intersection[1] - r[1] + r[0])
            )
            intervals.extend(residues)
            break
        else:
            new_range.append(s)
    return new_range


def solve(intervals: Sequence[int], rules: Rules) -> int:
    """Return the minimum number in the list of intervals after applying all the rules."""
    seed_ranges = [(x[0], x[0] + x[1] - 1) for x in itertools.batched(intervals, 2)]
    for rule in rules:
        seed_ranges = update_intervals(seed_ranges, rule)

    return min(s[0] for s in seed_ranges)


def main() -> tuple[int, int]:
    data = get_data()
    seeds, rules = parse_input(data)
    part1 = solve(tuple(itertools.chain(*((x, 1) for x in seeds))), rules)
    part2 = solve(seeds, rules)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
