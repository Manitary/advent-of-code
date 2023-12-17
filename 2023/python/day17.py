import heapq

from aocd import get_data, submit

DAY = 17
YEAR = 2023

type Coord = tuple[int, int]
type Grid = dict[Coord, int]

NEW_DIRS: dict[Coord, tuple[Coord, ...]] = {
    (0, 0): ((1, 0), (-1, 0), (0, 1), (0, -1)),
    (-1, 0): ((0, 1), (0, -1)),
    (1, 0): ((0, 1), (0, -1)),
    (0, -1): ((1, 0), (-1, 0)),
    (0, 1): ((1, 0), (-1, 0)),
}


def dijkstra(grid: Grid, start: Coord, end: Coord, min_step: int, max_step: int) -> int:
    queue: list[tuple[int, Coord, Coord]] = [(0, start, (0, 0))]
    visited: set[tuple[Coord, Coord]] = set()
    while queue:
        heat_loss, curr, last_dir = heapq.heappop(queue)
        if curr == end:
            return heat_loss
        if (curr, last_dir) in visited:
            continue
        visited.add((curr, last_dir))
        for new_dir in NEW_DIRS[last_dir]:
            pos = curr
            heat = heat_loss
            for step in range(1, max_step + 1):
                pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
                if pos not in grid:
                    break
                heat += grid[pos]
                if step < min_step:
                    continue
                heapq.heappush(queue, (heat, pos, new_dir))

    raise ValueError("Path not found")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    
    grid = {(r, c): int(v) for r, row in enumerate(data) for c, v in enumerate(row)}
    part1 = dijkstra(grid, (0, 0), (len(data) - 1, len(data[0]) - 1), 1, 3)
    part2 = dijkstra(grid, (0, 0), (len(data) - 1, len(data[0]) - 1), 4, 10)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
