from aocd import get_data, submit

DAY = 17
YEAR = 2015

AMOUNT = 150


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    barrels = sorted(list(map(int, data.split())))

    best = len(barrels)
    part2 = 0

    def num_comb(index: int, amount: int, curr: int = 0) -> int:
        nonlocal best, part2
        if amount == 0:
            if curr < best:
                best = curr
                part2 = 1
            elif curr == best:
                part2 += 1
            return 1
        if sum(barrels[:index]) < amount:
            return 0
        if barrels[0] > amount:
            return 0
        return num_comb(index - 1, amount, curr) + num_comb(
            index - 1, amount - barrels[index - 1], curr + 1
        )

    part1 = num_comb(len(barrels), AMOUNT)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
