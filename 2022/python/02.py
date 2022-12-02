from aocd import get_data, submit

RPS_SCORES_1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
RPS_SCORES_2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

def main() -> tuple[int, int]:
    data = get_data(day=2, year=2022).split('\n')
    ans1 = sum(map(lambda x: RPS_SCORES_1[x], data))
    ans2 = sum(map(lambda x: RPS_SCORES_2[x], data))

    return ans1, ans2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")