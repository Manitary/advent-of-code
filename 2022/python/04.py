from aocd import get_data, submit

def main() -> tuple[int, int]:
    ans1, ans2 = 0, 0
    for row in get_data(day=4, year=2022).split('\n'):
        row = row.replace(',', '-').split('-')
        a, b, x, y = map(int, row)
        ans1 += (a <= x and y <= b) or (x <= a and b <= y)
        ans2 += (a <= x <= b) or (a <= y <= b) or (x <= a <= y)

    return ans1, ans2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")