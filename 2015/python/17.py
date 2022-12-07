from aocd import get_data, submit

DAY = 17
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

barrels = sorted(list(map(int, data.split())))
amount = 150

best = len(barrels)
ans2 = 0


def numComb(index: int, amount: int, curr: int = 0):
    global best, ans2
    if amount == 0:
        if curr < best:
            best = curr
            ans2 = 1
        elif curr == best:
            ans2 += 1
        return 1
    if sum(barrels[:index]) < amount:
        return 0
    if barrels[0] > amount:
        return 0
    return numComb(index - 1, amount, curr) + numComb(
        index - 1, amount - barrels[index - 1], curr + 1
    )


ans1 = numComb(len(barrels), amount)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
