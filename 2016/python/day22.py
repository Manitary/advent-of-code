import functools
import re
from itertools import product
from typing import Generator, cast

from aocd import get_data, submit

DAY = 22
YEAR = 2016

Coords = tuple[int, int]
NodeInfo = dict[str, int]

PATTERN = re.compile(r"x(\d+)-y(\d+)")


def _available_moves(
    unavailable: set[Coords], max_x: int, max_y: int, node: Coords
) -> Generator[Coords, None, None]:
    x, y = node
    candidates = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    for c in candidates:
        if c not in unavailable and 0 <= c[0] <= max_x and 0 <= c[1] <= max_y:
            yield c


def part2_bfs(
    nodes: dict[Coords, NodeInfo], target: Coords, start: Coords, free_node: Coords
) -> int:
    # Properties of the input we can exploit:
    # * There is only one "free node" (with no data).
    # * No data can be merged, the only possible moves are moving data into the free node.
    # * There is a bunch of nodes with too much data that is impossible to move around.
    # Hence, the only information needed is the location of the data we want, and of the free cell;
    # we don't need to store anything else to keep track of visited states for a BFS.

    available_moves = functools.partial(
        _available_moves,
        unavailable={node for node, value in nodes.items() if value["used"] > 400},
        max_x=max(node[0] for node in nodes),
        max_y=max(node[1] for node in nodes),
    )

    visited: set[tuple[Coords, Coords]] = set()
    queue: list[tuple[Coords, Coords, int]] = [(start, free_node, 0)]
    while queue:
        current_goal, current_free, steps = queue.pop(0)
        if current_goal == target:
            return steps
        if (current_goal, current_free) in visited:
            continue
        visited.add((current_goal, current_free))
        for move in available_moves(node=current_free):
            new_free = move
            if current_goal == move:
                new_goal = current_free
            else:
                new_goal = current_goal
            queue.append((new_goal, new_free, steps + 1))
    raise ValueError("No path found")


def solve_1(nodes: dict[Coords, NodeInfo]) -> int:
    ans = 0
    for node1, node2 in product(nodes, repeat=2):
        if node1 == node2:
            continue
        if 0 < nodes[node1]["used"] <= nodes[node2]["avail"]:
            ans += 1
    return ans


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [row.split() for row in data.split("\n")]

    nodes: dict[Coords, NodeInfo] = {
        cast(Coords, tuple(map(int, PATTERN.search(row[0]).groups()))): {
            "size": int(row[1][:-1]),
            "used": int(row[2][:-1]),
            "avail": int(row[3][:-1]),
        }
        for row in data[2:]
    }

    part1 = solve_1(nodes)

    target_cell = (0, 0)
    data_position = (max(node[0] for node in nodes), 0)
    free_node = [node for node, value in nodes.items() if value["used"] == 0][0]
    part2 = part2_bfs(nodes, target_cell, data_position, free_node)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
