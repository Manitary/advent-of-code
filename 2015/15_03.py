from aocd import get_data, submit
DAY = 3
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

x1, y1, x2, y2, x3, y3 = (0 for _ in range(6))
visited1 = {(x1, y1)}
visited2 = {(x2, y2)}

def move(x, y, char, visited):
    match char:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '<':
            x -= 1
        case '>':
            x += 1
    visited.add((x, y))
    return x, y

for i, c in enumerate(data):
    x1, y1 = move(x1, y1, c, visited1)
    if i % 2 == 0:
        x2, y2 = move(x2, y2, c, visited2)
    else:
        x3, y3 = move(x3, y3, c, visited2)

submit(len(visited1), part="a", day=DAY, year=YEAR)
submit(len(visited2), part="b", day=DAY, year=YEAR)