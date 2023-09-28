from aocd import get_data, submit
from intcode import Arcade

DAY = 13
YEAR = 2019


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    arcade = Arcade(data)
    arcade.run()
    part1 = sum(1 for i in range(2, len(arcade.output), 3) if arcade.output[i] == 2)

    arcade = Arcade(data)
    arcade[0] = 2
    arcade.autoplay()
    part2 = arcade.score

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
