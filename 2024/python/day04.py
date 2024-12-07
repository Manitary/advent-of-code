import functools

from aocd import get_data, submit

DAY = 4
YEAR = 2024


DIRS = ((0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1))
XMAS = "MAS"
X_MAS = {"M", "S"}


def search_xmas(y: int, x: int, grid: list[str], nr: int, nc: int) -> int:
    ans = 0
    for d in DIRS:
        for i, w in enumerate(XMAS, 1):
            r = y + i * d[0]
            c = x + i * d[1]
            if r < 0 or r >= nr:
                break
            if c < 0 or c >= nc:
                break
            if grid[r][c] != w:
                break
        else:
            ans += 1
    return ans


def search_x_mas(y: int, x: int, grid: list[str], nr: int, nc: int) -> bool:
    if x == 0 or y == 0 or x == nr - 1 or y == nc - 1:
        return False
    if {grid[y - 1][x - 1], grid[y + 1][x + 1]} == X_MAS and {
        grid[y + 1][x - 1],
        grid[y - 1][x + 1],
    } == X_MAS:
        return True
    return False


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    search_1 = functools.partial(search_xmas, grid=data, nr=len(data), nc=len(data[0]))
    search_2 = functools.partial(search_x_mas, grid=data, nr=len(data), nc=len(data[0]))

    part1, part2 = 0, 0
    for r, row in enumerate(data):
        for c, tile in enumerate(row):
            if tile == "A":
                part2 += search_2(r, c)
            elif tile == "X":
                part1 += search_1(r, c)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
