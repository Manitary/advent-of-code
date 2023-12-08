import functools

from aocd import get_data, submit

DAY = 3
YEAR = 2023

type Coord = tuple[int, int]
type NumCoord = tuple[int, int, int]


def parse_input(data: list[str]) -> tuple[dict[NumCoord, int], dict[Coord, str]]:
    digits: dict[NumCoord, int] = {}
    symbols: dict[Coord, str] = {}
    for r, row in enumerate(data):
        c = 0
        while c < len(row):
            if row[c] == ".":
                c += 1
                continue
            if not row[c].isdigit():
                symbols[(r, c)] = row[c]
                c += 1
                continue
            start = c
            while c < len(row) and row[c].isdigit():
                c += 1
            digits[(r, start, c - 1)] = int(row[start:c])
    return digits, symbols


def _is_valid_num(row: int, col_start: int, col_end: int, symbols: set[Coord]) -> bool:
    return any(
        (r, c) in symbols
        for r in (row - 1, row, row + 1)
        for c in range(col_start - 1, col_end + 2)
    )


def _gear_ratio(r: int, c: int, digits: dict[NumCoord, int]) -> int:
    ngbhs: list[int] = []
    for p, n in digits.items():
        if r + 1 < p[0]:
            break
        if p[0] - 1 <= r <= p[0] + 1 and p[1] - 1 <= c <= p[2] + 1:
            ngbhs.append(n)
            if len(ngbhs) > 2:
                return 0
    if len(ngbhs) < 2:
        return 0
    return ngbhs[0] * ngbhs[1]


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).splitlines()
    digits, symbols = parse_input(data)

    is_valid_num = functools.partial(_is_valid_num, symbols=set(symbols.keys()))
    part1 = sum(n for p, n in digits.items() if is_valid_num(*p))

    gear_ratio = functools.partial(_gear_ratio, digits=digits)
    part2 = sum(gear_ratio(*p) for p, s in symbols.items() if s == "*")

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
