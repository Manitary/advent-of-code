from aocd import get_data, submit
import hashlib
DAY = 4
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

ans1, ans2 = None, None

i = 0
while True:
    val = hashlib.md5(f"{data}{i}".encode()).hexdigest()
    if val.startswith('0' * 5):
        if not ans1:
            ans1 = i
        if val.startswith('0' * 6):
            ans2 = i
            break
    i += 1

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
