import hashlib

from aocd import get_data, submit

DAY = 4
YEAR = 2015


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    part1 = 0
    i = -1
    while True:
        i += 1
        val = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        if not val.startswith("0" * 5):
            continue
        if not part1:
            part1 = i
        if val.startswith("0" * 6):
            return part1, i


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
