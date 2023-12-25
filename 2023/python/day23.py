from collections import defaultdict

from aocd import get_data, submit

DAY = 23
YEAR = 2023

type Coord = tuple[int, int]


ROTATE_DIR: dict[Coord, tuple[Coord, ...]] = {
    (1, 0): ((0, 1), (0, -1)),
    (-1, 0): ((0, 1), (0, -1)),
    (0, 1): ((-1, 0), (1, 0)),
    (0, -1): ((-1, 0), (1, 0)),
}

SLOPE_DIR = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}


def ngbh(c: Coord) -> set[Coord]:
    x, y = c
    return {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}


def make_graph(
    data: list[str], start: Coord, end: Coord
) -> dict[Coord, dict[Coord, int]]:
    slopes: dict[Coord, Coord] = {}
    empty: set[Coord] = set()
    for r, row in enumerate(data):
        for c, elt in enumerate(row):
            if elt in "<>v^":
                slopes[r, c] = SLOPE_DIR[elt]
            elif elt in ".":
                empty.add((r, c))

    crossroads = set(filter(lambda p: len(ngbh(p).intersection(slopes)) >= 2, empty))

    queue: list[tuple[Coord, Coord, int, tuple[Coord, ...]]] = [
        (start, (1, 0), 0, (start,))
    ]

    graph: dict[Coord, dict[Coord, int]] = defaultdict(dict)

    while queue:
        curr, d, steps, crosses = queue.pop(0)
        old = curr
        while (new := (curr[0] + d[0], curr[1] + d[1])) in empty:
            curr = new
            steps += 1
        if curr == end:
            graph[crosses[-1]][end] = steps
            continue
        if curr == old and new not in slopes:
            continue
        if new not in slopes:
            for new_dir in ROTATE_DIR[d]:
                queue.append((curr, new_dir, steps, crosses))
            continue
        # new is a slope tile
        new_dir = slopes[new]
        curr = (new[0] + new_dir[0], new[1] + new_dir[1])
        steps += 2
        if curr in crossroads:
            if curr != crosses[-1]:
                graph[crosses[-1]][curr] = steps
            if curr in crosses:
                continue
            crosses = crosses + (curr,)
            steps = 0
        for d in (new_dir,) + ROTATE_DIR[new_dir]:
            queue.append((curr, d, steps, crosses))

    return graph


def dfs(
    graph: dict[Coord, dict[Coord, int]],
    so_far: dict[Coord, int],
    curr: Coord,
    end: Coord,
) -> int:
    if end in graph[curr]:
        return sum(so_far.values()) + graph[curr][end]
    best = 0
    for neighbour in graph[curr]:
        if neighbour in so_far:
            continue
        res = dfs(graph, so_far | {neighbour: graph[curr][neighbour]}, neighbour, end)
        best = max(best, res)
    return best


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    start = (0, 1)
    end = (len(data) - 1, len(data[0]) - 1 - 1)

    graph = make_graph(data, start, end)

    part1 = dfs(graph, {start: 0}, start, end)

    for node_1, targets in graph.items():
        if node_1 == start or end in targets:
            continue
        for node_2, steps in targets.items():
            graph[node_2][node_1] = steps

    part2 = dfs(graph, {start: 0}, start, end)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
