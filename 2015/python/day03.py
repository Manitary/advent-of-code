from aocd import get_data, submit

DAY = 3
YEAR = 2015

Coords = tuple[int, int]


def move(x: int, y: int, char: str, visited: set[Coords]) -> Coords:
    if char == "^":
        y += 1
    elif char == "v":
        y -= 1
    elif char == "<":
        x -= 1
    elif char == ">":
        x += 1
    visited.add((x, y))
    return x, y


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    x1, y1, x2, y2, x3, y3 = (0,) * 6
    visited1: set[Coords] = {(x1, y1)}
    visited2: set[Coords] = {(x2, y2)}

    for i, c in enumerate(data):
        x1, y1 = move(x1, y1, c, visited1)
        if i % 2 == 0:
            x2, y2 = move(x2, y2, c, visited2)
        else:
            x3, y3 = move(x3, y3, c, visited2)
    return len(visited1), len(visited2)


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
