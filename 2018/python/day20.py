import functools
from collections import defaultdict

from aocd import get_data, submit

DAY = 20
YEAR = 2018

Coords = tuple[int, int]
Graph = dict[Coords, set[Coords]]

DIRS: dict[str, Coords] = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def make_map(data: str) -> Graph:
    graph: Graph = defaultdict(set)
    curr: Coords = (0, 0)
    branch: list[Coords] = []
    for char in data:
        if char in "NESW":
            new = (curr[0] + DIRS[char][0], curr[1] + DIRS[char][1])
            graph[new].add(curr)
            graph[curr].add(new)
            curr = new
        elif char == "(":
            branch.append(curr)
        elif char == "|":
            curr = branch[-1]
        elif char == ")":
            curr = branch.pop()
    return graph


def solve(
    graph: Graph, start: Coords = (0, 0), p2_limit: int = 1000
) -> tuple[int, int]:
    num_rooms = 0
    i = 0
    visited: set[Coords] = set()
    last: set[Coords] = {start}
    while last:
        i += 1
        new = functools.reduce(set.union, (graph[c] for c in last))
        visited |= last
        last = new - visited
        if i >= p2_limit:
            num_rooms += len(last)
    return i - 1, num_rooms


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    graph = make_map(data)
    part1, part2 = solve(graph)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    print(ans1, ans2)
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
