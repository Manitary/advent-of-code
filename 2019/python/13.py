from aocd import get_data, submit
from intcode import Arcade

DAY = 13
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

arcade = Arcade(data)
arcade.run()
ans1 = sum(1 for i in range(2, len(arcade.output), 3) if arcade.output[i] == 2)

arcade = Arcade(data)
arcade[0] = 2
arcade.autoplay()
ans2 = arcade.score

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
