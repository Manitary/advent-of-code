from aocd import get_data, submit
import hashlib
DAY = 5
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

pwd1, pwd2 = '', [None] * 8
i = 0
c = 0

while True:
    word = hashlib.md5(f"{data}{i}".encode()).hexdigest()
    if word.startswith('0' * 5):
        if len(pwd1) < 8:
            pwd1 += word[5]
        if int(word[5], 16) < 8 and pwd2[int(word[5])] is None:
            pwd2[int(word[5])] = word[6]
            c += 1
            if c == 8:
                pwd2 = ''.join(pwd2)
                break
    i += 1

submit(pwd1, part="a", day=DAY, year=YEAR)
submit(pwd2, part="b", day=DAY, year=YEAR)