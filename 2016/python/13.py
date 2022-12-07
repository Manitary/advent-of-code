from aocd import get_data, submit

DAY = 13
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = int(data)


def countOnes(n):
    ans = 0
    while n:
        ans += n & 1
        n = n >> 1
    return ans


def isOpen(x, y):
    if x < 0 or y < 0:
        return False
    n = x**2 + 3 * x + 2 * x * y + y + y**2 + data
    return countOnes(n) % 2 == 0


visited = set()


def ngbh(x, y):
    ans = set()
    for coord in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if coord not in visited:
            if isOpen(*coord):
                ans.add(coord)
            else:
                visited.add(coord)
    return ans


start = (1, 1)
end = (31, 39)
ans1, ans2 = None, 0
bound = 50

queue = [(start, 0)]

while queue:
    curr, steps = queue.pop(0)
    if curr == end:
        ans1 = steps
    if steps > bound and ans1:
        break
    if curr not in visited:
        visited.add(curr)
        if steps <= bound:
            ans2 += 1
        for new in ngbh(*curr):
            queue.append((new, steps + 1))

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
