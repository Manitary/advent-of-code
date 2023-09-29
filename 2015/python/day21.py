from itertools import combinations, product

from aocd import get_data, submit

DAY = 21
YEAR = 2015

HP = 100

WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMOURS = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
RINGS = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def is_win(player: list[int], boss: list[int]) -> bool:
    while player[0] > 0:
        # Player's turn
        boss[0] -= max(1, player[1] - boss[2])
        if boss[0] <= 0:
            return True
        # Boss' turn
        player[0] -= max(1, boss[1] - player[2])
    return False


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    boss = tuple(int(row.split()[-1]) for row in data.split("\n"))

    best = float("inf")
    worst = 0
    for w, a, (r1, r2) in product(WEAPONS, ARMOURS, combinations(RINGS, 2)):
        cost, attack, armour = (sum(x) for x in zip(*[w, a, r1, r2]))
        if cost < best or cost > worst:
            if is_win([HP, attack, armour], list(boss)):
                best = min(best, cost)
            else:
                worst = max(worst, cost)

    return int(best), worst


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
