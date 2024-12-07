with open("input.txt") as f:
    data = f.read().splitlines()

n_rows = len(data)
n_cols = len(data[0])

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

type Coord = tuple[int, int]


def read_map(m: str):
    x: set[tuple[int, int]] = set()
    g = (0, 0)
    for r, row in enumerate(m):
        for c, tile in enumerate(row):
            if tile == "^":
                g = (r, c)
            elif tile == "#":
                x.add((r, c))

    return g, x


def patrol(guard: Coord, obstacles: set[Coord]):
    visited: set[Coord] = set()
    d = 0
    while 0 <= guard[0] < n_rows and 0 <= guard[1] < n_cols:
        visited.add(guard)
        while (
            new_guard := (guard[0] + dirs[d][0], guard[1] + dirs[d][1])
        ) in obstacles:
            d += 1
            d %= 4
        guard = new_guard
    return visited


def patrol_with_dir(guard: Coord, obstacles: set[Coord]):
    visited: set[tuple[Coord, int]] = set()
    d = 0
    while 0 <= guard[0] < n_rows and 0 <= guard[1] < n_cols:
        visited.add((guard, d))
        while (
            new_guard := (guard[0] + dirs[d][0], guard[1] + dirs[d][1])
        ) in obstacles:
            d += 1
            d %= 4
        guard = new_guard
    return visited


def is_loop(guard: Coord, obstacles: set[Coord]):
    visited: set[tuple[Coord, int]] = set()
    d = 0
    while 0 <= guard[0] < n_rows and 0 <= guard[1] < n_cols:
        if (guard, d) in visited:
            return True

        visited.add((guard, d))
        while (
            new_guard := (guard[0] + dirs[d][0], guard[1] + dirs[d][1])
        ) in obstacles:
            d += 1
            d %= 4
        guard = new_guard
    return False


def find_loops(guard: Coord, obstacles: set[Coord], path: set[Coord]):
    ans = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if (r, c) == guard:
                continue
            if (r, c) in obstacles:
                continue
            if all(
                x not in path
                for x in ((r, c), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
            ):
                continue
            ans += is_loop(guard, obstacles | {(r, c)})

    return ans


def main():
    part1, part2 = 0, 0
    guard, obstacles = read_map(data)
    path = patrol(guard, obstacles)
    part1 = len(path)
    part2 = find_loops(guard, obstacles, path)

    return part1, part2


if __name__ == "__main__":
    # print(main())

    from sympy import Poly

    a = 1

    print(f"{a:+}")
