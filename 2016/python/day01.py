from aocd import get_data, submit

DAY = 1
YEAR = 2016


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split(", ")

    x, y = 0, 0
    dx, dy = 0, 1
    visited: set[tuple[int, int]] = set()
    part2 = 0
    for instr in data:
        dx, dy = (dy, -dx) if instr[0] == "R" else (-dy, dx)
        for _ in range(int(instr[1:])):
            x += dx
            y += dy
            if part2:
                continue
            if (x, y) in visited:
                part2 = x + y
            visited.add((x, y))
    part1 = x + y
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
