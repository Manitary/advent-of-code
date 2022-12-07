from aocd import get_data, submit

DAY = 2
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split()

pad1 = {(x, y): 3 * y + x + 1 for x in range(3) for y in range(3)}
pad2 = {
    (0, 2): 5,
    (1, 1): 2,
    (1, 2): 6,
    (1, 3): "A",
    (2, 0): 1,
    (2, 1): 3,
    (2, 2): 7,
    (2, 3): "B",
    (2, 4): "D",
    (3, 1): 4,
    (3, 2): 8,
    (3, 3): "C",
    (4, 2): 9,
}


def num(x, y, pad):
    return pad[(x, y)]


def move(x, y, char, pad):
    x1, y1 = x, y
    match char:
        case "U":
            y1 -= 1
        case "D":
            y1 += 1
        case "L":
            x1 -= 1
        case "R":
            x1 += 1
    if (x1, y1) in pad:
        return x1, y1
    return x, y


ans1 = ""
ans2 = ""
x1, y1 = 1, 1
x2, y2 = 0, 2
for line in data:
    for c in line:
        x1, y1 = move(x1, y1, c, pad1)
        x2, y2 = move(x2, y2, c, pad2)
    ans1 += str(num(x1, y1, pad1))
    ans2 += str(num(x2, y2, pad2))

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
