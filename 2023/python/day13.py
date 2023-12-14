from aocd import get_data, submit

DAY = 13
YEAR = 2023


def horizontal_reflection_with_smudges(pattern: list[str], smudges: int) -> int:
    for r in range(len(pattern) - 1):
        smudges_available = smudges
        for i in range(min(r, len(pattern) - 2 - r) + 1):
            diff = sum(a != b for a, b in zip(pattern[r - i], pattern[r + i + 1]))
            if diff > smudges_available:
                break
            smudges_available -= diff
        else:
            if smudges_available == 0:
                return r

    raise ValueError(f"No reflection with exactly {smudges} smudges found")


def summarize_pattern(pattern: list[str], smudges: int) -> int:
    try:
        return 100 * (1 + horizontal_reflection_with_smudges(pattern, smudges))
    except ValueError:
        return 1 + horizontal_reflection_with_smudges(list(zip(*pattern)), smudges)


def main() -> tuple[int, int]:
    data = [pattern.split() for pattern in get_data(day=DAY, year=YEAR).split("\n\n")]

    part1 = sum(summarize_pattern(pattern, 0) for pattern in data)
    part2 = sum(summarize_pattern(pattern, 1) for pattern in data)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
