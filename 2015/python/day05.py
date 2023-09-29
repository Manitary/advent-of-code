from aocd import get_data, submit

DAY = 5
YEAR = 2015

VOWELS = {"a", "e", "i", "o", "u"}
BAD = {"a": "b", "c": "d", "p": "q", "x": "y"}


def is_nice_1(s: str) -> bool:
    vowels = 0
    double = False
    for i, c in enumerate(s):
        if i < len(s) - 1:
            if c in BAD and s[i + 1] == BAD[c]:
                return False
            if (not double) and s[i + 1] == c:
                double = True
        if c in VOWELS:
            vowels += 1
    if vowels >= 3 and double:
        return True
    return False


def is_nice_2(s: str) -> bool:
    rule1, rule2 = False, False
    pairs: dict[str, int] = {}
    for i, c in enumerate(s):
        if (not rule1) and i < len(s) - 1:
            pair = c + s[i + 1]
            if pair in pairs:
                if pairs[pair] < i - 1:
                    rule1 = True
            else:
                pairs[pair] = i
        if (not rule2) and i < len(s) - 2:
            if c == s[i + 2]:
                rule2 = True
        if rule1 and rule2:
            return True
    return False


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    return sum(map(is_nice_1, data)), sum(map(is_nice_2, data))


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
