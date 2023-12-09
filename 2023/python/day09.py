from aocd import get_data, submit

DAY = 9
YEAR = 2023


def extrapolate_values(history: tuple[int, ...]) -> tuple[int, int]:
    future, past = 0, 0
    i = 0
    while any(history):
        future += history[-1]
        past += -history[0] if i % 2 else history[0]
        history = tuple(history[k] - history[k - 1] for k in range(1, len(history)))
        i += 1
    return future, past


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    data = [tuple(map(int, row.split())) for row in data.splitlines()]
    part1, part2 = map(sum, zip(*map(extrapolate_values, data)))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
