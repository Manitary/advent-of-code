from itertools import count, product

from aocd import get_data, submit
from intcode import Computer

DAY = 19
YEAR = 2019


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    drone = Computer(data)

    def isValid(x: int, y: int) -> int:
        drone.reset()
        drone.push([x, y])
        drone.run()
        return drone.pop()

    ans1 = sum([isValid(*coords) for coords in product(range(50), range(50))])

    y = 0
    min_x = 0
    ans2 = 0
    while not ans2:
        for x in count(min_x):
            if not isValid(x, y):
                if x > min_x + 5:  # Some of the early lines have no valid tiles
                    break
            min_x = x
            for x1 in count(x):
                if not isValid(x1 + 99, y):
                    break
                if not isValid(x1, y + 99):
                    if x1 == min_x:
                        min_x += 1
                    break
                if isValid(x1 + 99, y + 99):
                    ans2 = 10000 * x1 + y
                    break
            break
        y += 1

    return ans1, ans2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
