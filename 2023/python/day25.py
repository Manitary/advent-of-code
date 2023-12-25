from math import prod

import networkx
from aocd import get_data, submit

DAY = 25
YEAR = 2023


def main() -> int:
    data = get_data(day=DAY, year=YEAR).splitlines()

    graph = networkx.Graph()
    for row in data:
        s, t = row.split(": ")
        graph.add_edges_from((s, x) for x in t.split())

    graph.remove_edges_from(networkx.minimum_edge_cut(graph))
    part1 = prod(map(len, networkx.connected_components(graph)))

    return part1


if __name__ == "__main__":
    ans1 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
