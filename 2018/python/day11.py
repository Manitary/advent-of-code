from aocd import get_data, submit

DAY = 11
YEAR = 2018

R = 300
ID = 10


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)
    data = int(data)

    g = [
        tuple(
            (((((x + 1 + ID) * (y + 1) + data) * (x + 1 + ID)) % 1000) // 100) - 5
            for x in range(R)
        )
        for y in range(R)
    ]

    p = [list(g[0])]
    for y in range(1, R):
        p.append([g[y][0] + p[y - 1][0]])
    for y in range(1, R):
        for x in range(1, R):
            p[y].append((g[y][x] + p[y - 1][x] + p[y][x - 1] - p[y - 1][x - 1]))

    f = tuple(
        (
            x + 1,
            y + 1,
            l,
            p[y + l - 1][x + l - 1]
            - (p[y - 1][x + l - 1] if y > 0 else 0)
            - (p[y + l - 1][x - 1] if x > 0 else 0)
            + (p[y - 1][x - 1] if y > 0 and x > 0 else 0),
        )
        for l in range(R)
        for x in range(R - l)
        for y in range(R - l)
    )

    part1 = max(filter(lambda c: c[2] == 3, f), key=lambda c: c[3])
    part2 = max(f, key=lambda c: c[3])
    return ",".join(map(str, part1[:-2])), ",".join(map(str, part2[:-1]))


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
