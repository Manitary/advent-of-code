from aocd import get_data, submit

DAY = 7
YEAR = 2016


def is_abba(s: str, i: int) -> bool:
    return s[i] == s[i + 3] != s[i + 1] == s[i + 2] and s[i : i + 4].isalpha()


def is_aba(s: str, i: int) -> bool:
    return s[i] == s[i + 2] != s[i + 1] and s[i : i + 3].isalpha()


def is_tls(s: str) -> bool:
    abba = False
    brackets = 0
    for i in range(len(s) - 3):
        if s[i] == "[":
            brackets += 1
            continue
        if s[i] == "]":
            brackets -= 1
            continue
        if brackets and is_abba(s, i):
            return False
        if (not abba) and is_abba(s, i):
            abba = True
    return abba


def is_ssl(s: str) -> bool:
    outside: set[str] = set()
    inside: set[str] = set()
    brackets = 0
    for i in range(len(s) - 2):
        if s[i] == "[":
            brackets += 1
            continue
        if s[i] == "]":
            brackets -= 1
            continue
        if is_aba(s, i):
            aba = s[i : i + 3]
            bab = aba[1] + aba[0] + aba[1]
            if brackets:
                if bab in outside:
                    return True
                inside.add(aba)
            else:
                if bab in inside:
                    return True
                outside.add(aba)
    return False


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    part1 = sum(map(is_tls, data))
    part2 = sum(map(is_ssl, data))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
