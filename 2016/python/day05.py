import hashlib

from aocd import get_data, submit

DAY = 5
YEAR = 2016


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)

    pwd1, pwd2 = "", [""] * 8
    i = 0
    c = 0
    while True:
        word = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        if word.startswith("0" * 5):
            if len(pwd1) < 8:
                pwd1 += word[5]
            if int(word[5], 16) < 8 and not pwd2[int(word[5])]:
                pwd2[int(word[5])] = word[6]
                c += 1
                if c == 8:
                    pwd2 = "".join(pwd2)
                    break
        i += 1
    return pwd1, pwd2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
