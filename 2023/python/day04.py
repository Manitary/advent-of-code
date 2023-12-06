from aocd import get_data, submit

DAY = 4
YEAR = 2023


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    num_cards = [1] * len(data)
    part1 = 0
    for i, row in enumerate(data):
        _, card_nums = row.split(":")
        winning, numbers = (set(nums.split()) for nums in card_nums.split("|"))
        w = len(winning & numbers)
        if w:
            part1 += 2 ** (w - 1)
        for j in range(w):
            num_cards[i + j + 1] += num_cards[i]

    part2 = sum(num_cards)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
