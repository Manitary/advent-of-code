"""Solve Advent of Code Day 16 Year 2022."""

import re
import math
from functools import cache
from itertools import product
from collections import defaultdict
from aocd import get_data, submit


def parse_input(data: str) -> tuple[dict[str, int], dict[str, dict[str, int]]]:
    """Return the valves and flows (if non-zero), and their travel distance."""
    valves = {}
    dists = defaultdict(lambda: defaultdict(lambda: math.inf))
    for row in data.split("\n"):
        valve, *conns = re.findall(r"([A-Z]{2})", row)
        flow_rate = int(re.findall(r"(\d+)", row)[0])
        valves[valve] = flow_rate
        dists[valve][valve] = 0
        for other in conns:
            dists[valve][other] = 1
    for k, i, j in product(valves.keys(), repeat=3):
        dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    # Filter out 0-flow valves from the list of valves to traverse.
    flows = dict(filter(lambda v: v[1] > 0, valves.items()))
    valves = tuple(flows.keys())
    return valves, flows, dists


def create_dfs(flows, distances) -> callable:
    """Return the dfs functions to solve both parts with the given input."""

    # Check all paths with memoisation.
    # Whenever we reach a valve, we add all of its (future) total contribution.
    @cache
    def fun_1(
        current_valve: str,
        remaining_valves: tuple[str],
        time_left: int,
    ) -> int:
        return max(
            (
                flows[new_valve] * (time_left - distances[current_valve][new_valve] - 1)
                + fun_1(
                    current_valve=new_valve,
                    remaining_valves=tuple(remaining_valves[:i])
                    + tuple(remaining_valves[i + 1 :]),
                    time_left=time_left - distances[current_valve][new_valve] - 1,
                )
                for i, new_valve in enumerate(remaining_valves)
                if distances[current_valve][new_valve] < time_left
            ),
            default=0,
        )

    # Check all paths with memoisation...again.
    # When the candidates are unreachable in time, let the elephant go to them.
    # There are some inefficiencies, for example we are ignoring the symmetry
    # in the role of the player and the elephant.
    @cache
    def fun_2(
        current_valve: str,
        remaining_valves: tuple[str],
        time_left: int,
    ) -> tuple[tuple[int], int]:
        candidates = tuple(
            flows[new_valve] * (time_left - distances[current_valve][new_valve] - 1)
            + fun_2(
                current_valve=new_valve,
                remaining_valves=tuple(remaining_valves[:i])
                + tuple(remaining_valves[i + 1 :]),
                time_left=time_left - distances[current_valve][new_valve] - 1,
            )
            for i, new_valve in enumerate(remaining_valves)
            if distances[current_valve][new_valve] < time_left
        )
        if candidates:
            return max(candidates)
        return fun_1(
            current_valve="AA", remaining_valves=remaining_valves, time_left=26
        )

    return fun_1, fun_2


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=16, year=2022)
    valves, flows, distances = parse_input(data)
    dfs_part1, dfs_part2 = create_dfs(flows, distances)
    part1 = dfs_part1(current_valve="AA", remaining_valves=valves, time_left=30)
    part2 = dfs_part2(current_valve="AA", remaining_valves=valves, time_left=26)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
