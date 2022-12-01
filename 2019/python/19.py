from aocd import get_data, submit
from intcode import Computer
from itertools import product, count
DAY = 19
YEAR = 2019

data = get_data(day=DAY, year=YEAR)

drone = Computer(data)

def isValid(x, y):
    drone.reset()
    drone.push([x, y])
    drone.run()
    return drone.pop()

ans1 = sum([isValid(*coords) for coords in product(range(50), range(50))])

y = 0
min_x = 0
ans2 = None
while not ans2:
    for x in count(min_x):
        if isValid(x, y):
            min_x = x
            for x1 in count(x):
                if not isValid(x1 + 99, y):
                    break
                if not isValid(x1, y + 99):
                    if x1 == min_x:
                        min_x += 1
                    break
                if isValid(x1 + 99, y + 99):
                    ans2 = 10000*x1 + y
                    break
            break
        else:
            if x > min_x + 5: # Some of the early lines have no valid tiles
                break
    y += 1

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)