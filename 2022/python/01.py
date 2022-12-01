from aocd import get_data, submit

def main():
    data = sorted([sum(map(int, row.split())) for row in list(get_data().split('\n\n'))])
    ans1 = data[-1]
    ans2 = sum(data[-3:])

    return ans1, ans2

if __name__ == '__main__':
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")