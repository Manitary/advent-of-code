import math
from collections import defaultdict

from aocd import get_data, submit

DAY = 2
YEAR = 2023

BAG = {"red": 12, "green": 13, "blue": 14}


def main() -> tuple[int, int]:
    part1, part2 = 0, 0
    data = get_data(day=DAY, year=YEAR).splitlines()
    for row in data:
        min_bag: dict[str, int] = defaultdict(int)
        game, turns = row.split(":")
        game_id = int(game.split()[-1])
        for turn in turns.split(";"):
            for cube in turn.split(","):
                amount, colour = cube.split()
                min_bag[colour] = max(min_bag[colour], int(amount))
        part2 += math.prod(min_bag.values())
        if all(min_bag[colour] <= BAG.get(colour, 0) for colour in min_bag):
            part1 += game_id

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
