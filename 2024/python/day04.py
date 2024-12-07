with open("input.txt") as f:
    data = f.read().splitlines()

ncol = len(data[0])
nrow = len(data)

dirs = ((0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1))

word = "XMAS"


def search(grid: list[str], y: int, x: int):
    ans = 0
    for d in dirs:
        for i in range(1, 4):
            r = y + i * d[0]
            c = x + i * d[1]
            if r < 0 or r >= nrow:
                break
            if c < 0 or c >= ncol:
                break
            if grid[r][c] != word[i]:
                break
        else:
            ans += 1
    return ans


def search_2(grid: list[str], y: int, x: int):
    try:
        assert grid[y][x] == "A"
        assert y > 0
        assert x > 0
        assert {grid[y - 1][x - 1], grid[y + 1][x + 1]} == {"M", "S"}
        assert {grid[y + 1][x - 1], grid[y - 1][x + 1]} == {"M", "S"}
        return 1
    except (AssertionError, IndexError):
        return 0


def main():
    ans = 0
    ans2 = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            ans2 += search_2(data, r, c)
            if col != "X":
                continue
            ans += search(data, r, c)
    return ans, ans2


print(main())
