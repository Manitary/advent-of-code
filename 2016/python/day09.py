from aocd import get_data, submit

DAY = 9
YEAR = 2016


def decompress(s: str, part: int) -> int:
    length = 0
    while "(" in s:
        start = s.find("(")
        length += start
        end = s.find(")", start + 1)
        n1, n2 = map(int, tuple(s[start + 1 : end].split("x")))
        if part == 1:
            length += n1 * n2
        elif part == 2:
            length += decompress(s[end + 1 : end + n1 + 1], part=2) * n2
        else:
            raise ValueError("Invalid part")
        s = s[end + 1 + n1 :]
    length += len(s)
    return length


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    part1 = decompress(data, part=1)
    part2 = decompress(data, part=2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
