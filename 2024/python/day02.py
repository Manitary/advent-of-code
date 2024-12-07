with open("input.txt") as f:
    data = f.read()


def parse_data(d: str) -> list[list[int]]:
    return [list(map(int, x.split())) for x in d.splitlines()]


data = parse_data(data)


def is_safe(n: list[int], t: bool = True) -> bool:
    # if n[1] == n[0]:
    #   if t:
    #      return is_safe(n[1:], False)
    # return False
    c = sum(b - a > 0 for a, b in zip(n, n[1:])) > sum(
        b - a < 0 for a, b in zip(n, n[1:])
    )
    for i, (a, b) in enumerate(zip(n, n[1:])):
        if (c and a >= b) or ((not c) and a <= b) or abs(a - b) > 3:
            if not t:
                return False
            return is_safe(n[:i] + n[i + 1 :], False) or is_safe(
                n[: i + 1] + n[i + 2 :], False
            )
    return True


def is_safe_2(n: list[int]) -> bool:
    bad_reports = 0
    c = sum(b - a > 0 for a, b in zip(n, n[1:])) > sum(
        b - a < 0 for a, b in zip(n, n[1:])
    )
    for i, (a, b) in enumerate(zip(n, n[1:])):
        if (c and a >= b) or ((not c) and a <= b) or abs(a - b) > 3:
            bad_reports += 1
            if bad_reports > 1:
                return False
    return True


print(sum(is_safe(x, False) for x in data))
print(sum(is_safe(x) for x in data))
