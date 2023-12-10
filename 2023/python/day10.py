import itertools

from aocd import get_data, submit

DAY = 10
YEAR = 2023

type Coord = tuple[int, int]
type Grid = dict[Coord, str]


TILES = "|-LJ7F"
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


valid_moves: dict[tuple[str, Coord], Coord] = {
    # (tile shape, direction entering) -> direction leaving
    ("|", (1, 0)): (1, 0),
    ("|", (-1, 0)): (-1, 0),
    ("-", (0, 1)): (0, 1),
    ("-", (0, -1)): (0, -1),
    ("L", (1, 0)): (0, 1),
    ("L", (0, -1)): (-1, 0),
    ("J", (1, 0)): (0, -1),
    ("J", (0, 1)): (-1, 0),
    ("7", (-1, 0)): (0, -1),
    ("7", (0, 1)): (1, 0),
    ("F", (-1, 0)): (0, 1),
    ("F", (0, -1)): (1, 0),
}


def move(curr: Coord, direction: Coord, tile: str) -> tuple[Coord, Coord]:
    """
    Return the new position and direction based on the current tile.

    Args:
        curr (Coord): current tile coordinates
        direction (Coord): direction the current tile was entered
        tile (str): current tile

    Raises:
        KeyError: if the current state is invalid
        (e.g. `|` tile entered with horizontal direction `(0,1)`)

    Returns:
        tuple[Coord, Coord]: new coordinates, new direction
    """
    new_dir = valid_moves[(tile, direction)]
    return (curr[0] + new_dir[0], curr[1] + new_dir[1]), new_dir


def find_loop(grid: Grid, start: Coord) -> tuple[Grid, list[Coord]]:
    """
    Find the loop as described by part 1.

    Args:
        grid (Grid): coordinates of the non-`.` tiles
        start (Coord): coordinates of the `S` tile

    Raises:
        ValueError: if no substitution for `S` forms a loop in the grid

    Returns:
        tuple[Grid, list[Coord]]:
        an updated grid where `S` is replaced with the appropriate character,
        a list of coordinates of the loop (sorted in traverse order from `S`)
    """
    for t, (d1, d2) in itertools.product(TILES, itertools.combinations(DIRECTIONS, 2)):
        grid[start] = t
        curr1, curr2 = start, start
        loop1: list[Coord] = [start]
        loop2: list[Coord] = []
        while True:
            try:
                curr1, d1 = move(curr1, d1, grid[curr1])
            except KeyError:
                break
            if curr1 == curr2:
                return grid, loop1 + list(reversed(loop2))
            loop1.append(curr1)
            try:
                curr2, d2 = move(curr2, d2, grid[curr2])
            except KeyError:
                break
            if curr1 == curr2:
                return grid, loop1 + list(reversed(loop2))
            loop2.append(curr2)

    raise ValueError("No loop found")


def count_inner(grid: Grid, loop: set[Coord], height: int, width: int) -> int:
    """Return the number of tiles inside the loop perimeter."""
    ans = 0
    for r in range(height):
        inside = False
        section = ""
        for c in range(width):
            if (r, c) not in loop:
                if inside:
                    ans += 1
                continue
            tile = grid[(r, c)]
            if tile == "-":
                continue
            if tile in "FL":
                section = tile
            else:
                if (
                    tile == "|"
                    or (tile == "J" and section == "F")
                    or (tile == "7" and section == "L")
                ):
                    inside = not inside
                    # |, F--J, L--7 change the inside/outside status of adjacent cells
                    # F--7, L--J do not

                    # e.g.
                    #     OOOOOO            OOOO|I
                    # --> OF--7O <-- vs --> OF--JI <--
                    #     O|II|O            O|IIII

                section = ""

    return ans


def parse_input(data: list[str]) -> tuple[Grid, Coord]:
    grid = {
        (r, c): elt
        for r, row in enumerate(data)
        for c, elt in enumerate(row)
        if elt != "."
    }
    start = {c for c, v in grid.items() if v == "S"}.pop()
    return grid, start


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()

    grid, start = parse_input(data)
    grid, loop = find_loop(grid, start)

    part1 = len(loop) // 2
    part2 = count_inner(grid, set(loop), len(data), len(data[0]))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
