import copy

from aocd import get_data, submit

DAY = 14
YEAR = 2023

type Rocks = list[list[str]]


def tilt_up(rocks: Rocks) -> Rocks:
    for r, row in enumerate(rocks):
        if r == 0:
            continue
        for c, elt in enumerate(row):
            if elt != "O":
                continue
            new_stop = next(
                (i for i in range(r - 1, -1, -1) if rocks[i][c] in "O#"), -1
            )
            rocks[r][c] = "."
            rocks[new_stop + 1][c] = "O"
    return rocks


def north_load(rocks: Rocks) -> int:
    return sum(
        i * sum(x == "O" for x in row) for i, row in enumerate(reversed(rocks), 1)
    )


def spin(rocks: Rocks, n_spins: int) -> Rocks:
    visited = [copy.deepcopy(rocks)]
    for _ in range(1, n_spins + 1):
        for _ in range(4):
            rocks = [list(x[::-1]) for x in zip(*tilt_up(rocks))]
        if rocks in visited:
            break
        visited.append(copy.deepcopy(rocks))
    first_found = visited.index(rocks)
    cycle_length = len(visited) - first_found
    final_rocks = visited[first_found + ((n_spins - first_found) % cycle_length)]
    return final_rocks


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [list(x) for x in data.splitlines()]

    part1 = north_load(tilt_up(data))
    part2 = north_load(spin(data, 1000000000))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
