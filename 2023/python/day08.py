import functools
import itertools
import re
from collections import defaultdict
from math import lcm
from typing import Callable

from aocd import get_data, submit

DAY = 8
YEAR = 2023

NODE_RE = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

type Nodes = dict[str, tuple[str, str]]


def parse_input(data: str) -> tuple[str, Nodes]:
    moves, nodes_list = data.split("\n\n")
    nodes: Nodes = defaultdict(tuple)

    for node in nodes_list.splitlines():
        match = NODE_RE.match(node)
        if not match:
            raise ValueError("Match not found")
        root = match.group(1)
        nodes[root] = (match.group(2), match.group(3))

    return moves, nodes


def _distance(
    moves: str, nodes: Nodes, start: str, end_criterion: Callable[[str], bool]
) -> int:
    curr = start
    steps = 0
    for c in itertools.cycle(moves):
        if end_criterion(curr):
            break
        if c == "L":
            curr = nodes[curr][0]
        else:
            curr = nodes[curr][1]
        steps += 1
    return steps


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    moves, nodes = parse_input(data)

    distance = functools.partial(_distance, moves=moves, nodes=nodes)
    part1 = distance(start="AAA", end_criterion=lambda x: x == "ZZZ")
    # For part 2, the input is such that for each of the __A nodes
    # __A --> __Z --> __Z takes the same number of steps
    part2 = lcm(
        *(
            distance(start=node, end_criterion=lambda x: x.endswith("Z"))
            for node in nodes
            if node.endswith("A")
        )
    )

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
