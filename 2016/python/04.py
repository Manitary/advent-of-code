from aocd import get_data, submit

DAY = 4
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split()


def decode(name, key):
    key = key % 26
    ans = ""
    for c in name:
        if c == "-":
            ans += " "
        else:
            ans += chr((ord(c) + key - 97) % 26 + 97)
    return ans


def isRoom(s):
    name = s[:-10]
    sector = s[-10:-7]
    checksum = s[-6:-1]
    count = {}
    for c in name:
        if c != "-":
            if c not in count:
                count[c] = 0
            count[c] += 1
    if (
        "".join(
            sorted(
                list(count.keys()),
                key=lambda k: (count[k], ord("z") - ord(k)),
                reverse=True,
            )[:5]
        )
        == checksum
    ):
        return int(sector), decode(name, int(sector))
    return 0, None


tot = 0
storage = ""
for row in data:
    val, room = isRoom(row)
    tot += val
    if val > 0 and "north" in room:
        storage = val

submit(tot, part="a", day=DAY, year=YEAR)
submit(storage, part="b", day=DAY, year=YEAR)
