from collections import Counter

from aocd import get_data, submit

DAY = 4
YEAR = 2016


def decode(name: str, key: int) -> str:
    key = key % 26
    return "".join(
        " " if c == "-" else chr((ord(c) + key - 97) % 26 + 97) for c in name
    )


def is_room(s: str) -> tuple[int, str]:
    name = s[:-10]
    sector = s[-10:-7]
    checksum = s[-6:-1]
    count = Counter(name)
    count.pop("-")
    if (
        "".join(
            sorted(
                count,
                key=lambda k: (count[k], ord("z") - ord(k)),
                reverse=True,
            )[:5]
        )
        == checksum
    ):
        return int(sector), decode(name, int(sector))
    return 0, ""


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split()
    tot = 0
    storage = 0
    for row in data:
        val, room = is_room(row)
        tot += val
        if val and "north" in room:
            storage = val
    return tot, storage


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
